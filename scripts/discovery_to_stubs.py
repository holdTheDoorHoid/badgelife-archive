#!/usr/bin/env python3
"""Turn discovery-sweep candidates (data/discovery_<name>.json) into stub records, deduplicated
against existing entries and against each other.

Input shape: {"results": [{"angle": str, "candidates": [{title, maker, event_hint, year, type, url,
extra_urls, image_url, note}]}]}

Dedup rules (a candidate is dropped if any hit):
  - its url (canonicalised) already appears in an existing entry's links/sources;
  - normalised title matches an existing entry title in the same event (or, for events unknown,
    in any event) with a similarity >= 0.88 and the maker names overlap or one is empty;
  - the same url or (title, event) was already emitted in this run.

Event resolution from event_hint/year: "DEF CON 27" / "DC27" / "DC 27" -> dc27; "Supercon 2023" ->
supercon-2023; known con names map to ids (created in _data/events.yml when missing); otherwise
"other". Output: data/stubs_<name>.json for gen_entries.py, plus a report of what was dropped.
"""
import argparse, difflib, glob, json, os, re, sys, unicodedata
from collections import OrderedDict
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVENTS_PATH = os.path.join(ROOT, "_data", "events.yml")

CON_FAMILIES = [
    (r"\b(def ?con|dc)\s*-?\s*(\d{2})\b", "defcon"),
    (r"\bsupercon(?:ference)?\s*(?:\d\s*)?\(?(20\d\d)\)?", "supercon"),
    (r"\bsupercon\s*(\d)\b", "supercon-n"),
    (r"\b(bsides\s*[a-z ]*?)\s*(20\d\d)", "bsides"),
    (r"\b(emf ?camp|electromagnetic field)\s*(20\d\d)", "camp"),
    (r"\b(mch|sha|why|campzone|hackerhotel|fri3d(?: camp)?|bornhack|cccamp|chaos communication (?:camp|congress)|\d\dc3)\s*-?\s*(20\d\d)?", "camp"),
    (r"\b(shmoocon|thotcon|cyphercon|derbycon|toorcon|carolinacon|grrcon|hope|saintcon|cactuscon|wild west hackin.? fest|circle city con|kiwicon|northsec|hackfest|layer ?8|blue team con|shellcon|sector|converge|dakotacon)\s*-?\s*(20\d\d|0x[0-9a-f]+|\d{1,2}|x+[iv]*)?", "other"),
]
DEFCON_YEAR = {n: 1992 + n for n in range(1, 40)}  # DEF CON 1 = 1993 -> dc24 = 2016

def norm(s):
    s = "" if s is None else str(s)  # YAML can hand back bools/numbers for names like "Yes" or "42"
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(the|a|an|badge|sao|shitty add[- ]?on|add[- ]?on|v\d+(\.\d+)?|dc\d+|def ?con \d+|20\d\d)\b", " ", s)
    return re.sub(r"[^a-z0-9]+", " ", s).strip()

def canon(u): return re.sub(r"^https?://(www\.)?", "", (u or "").strip().rstrip("/")).lower()

def slugify(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    s = re.sub(r"^(def-?con-?|dc-?)(\d{2})-", "", s)
    return re.sub(r"-{2,}", "-", s)[:60].strip("-") or "untitled"

def resolve_event(hint, year, events, new_events):
    h = (hint or "").lower()
    m = re.search(CON_FAMILIES[0][0], h)
    if m:
        n = int(m.group(2))
        if 24 <= n <= 40: return f"dc{n}"
    m = re.search(CON_FAMILIES[1][0], h)
    if m: return ensure(events, new_events, f"supercon-{m.group(1)}", f"Hackaday Supercon {m.group(1)}", int(m.group(1)), "supercon", "Pasadena, CA")
    m = re.search(CON_FAMILIES[2][0], h)
    if m:
        y = 2016 + int(m.group(1))  # Supercon 1 = 2016 ... Supercon 8 = 2024 (skipping 2020/21 makes this approximate)
        if int(m.group(1)) >= 7: y = 2016 + int(m.group(1)) + 1  # Supercon 7 = 2023, 8 = 2024, 9 = 2025
        return ensure(events, new_events, f"supercon-{y}", f"Hackaday Supercon {y}", y, "supercon", "Pasadena, CA")
    if "supercon" in h and year: return ensure(events, new_events, f"supercon-{year}", f"Hackaday Supercon {year}", year, "supercon", "Pasadena, CA")
    for pat, fam in CON_FAMILIES[3:]:
        m = re.search(pat, h)
        if m:
            name = m.group(1).strip()
            name = {"fri3d camp": "fri3d", "chaos communication camp": "cccamp", "chaos communication congress": "ccc-congress", "cccamp": "cccamp"}.get(name, name)
            yr = m.group(2) if m.lastindex and m.lastindex >= 2 else None
            if yr and yr.startswith("0x"):  # THOTCON hex numbering: 0x1 = 2010 ... 0xA = 2019, 0xB = 2022 (2020-21 skipped), 0xC = 2023 ...
                n = int(yr, 16); yr = str(2009 + n) if n <= 10 else str(2011 + n)
            if yr and len(yr) <= 2 and yr.isdigit() and year: yr = str(year)  # a bare edition number: fall back to the candidate's year
            yr = yr or (str(year) if year else "")
            if not yr: return "other"  # no year at all: do not invent an event
            base = re.sub(r"[^a-z0-9]+", "-", name).strip("-")
            eid = f"{base}-{yr}" if yr else base
            pretty = name.title().replace("Bsides", "BSides").replace("Emf", "EMF").replace("Mch", "MCH").replace("Ccc", "CCC")
            return ensure(events, new_events, eid, f"{pretty} {yr}".strip(), int(yr) if yr and yr.isdigit() and len(yr) == 4 else (year or 0), fam if fam != "supercon-n" else "supercon", "")
    if year and ("def con" in h or "defcon" in h):
        n = year - 1992
        if 24 <= n <= 40: return f"dc{n}"
    return "other"

def ensure(events, new_events, eid, name, year, family, location):
    eid = re.sub(r"[^a-z0-9-]", "-", eid.lower()).strip("-")
    if eid not in events:
        events[eid] = OrderedDict([("name", name), ("short", name), ("year", year or 0), ("family", family), ("location", location)])
        new_events.append(eid)
    return eid

def load_entry(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    return yaml.safe_load(m.group(1)) or {}

TYPE_VOCAB = ("minibadge", "sao", "badge", "kit", "accessory", "other", "unknown")
def coerce_type(v):
    """Agents write free text like 'sao/kit' or 'badge (SAO-compatible)'; keep the first vocabulary word found."""
    s = norm(v).lower()
    if s in TYPE_VOCAB: return s
    for w in TYPE_VOCAB:
        if w in s: return w
    return "other" if s else "unknown"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("discovery_json"); ap.add_argument("--name", required=True); ap.add_argument("--date", required=True)
    ap.add_argument("--extra-stubs", nargs="*", default=[], help="other stubs_*.json files to dedupe against")
    a = ap.parse_args()
    data = json.load(open(a.discovery_json))
    results = data["results"] if isinstance(data, dict) else data
    events = yaml.safe_load(open(EVENTS_PATH)); new_events = []
    # existing entries
    existing = []
    for f in glob.glob(os.path.join(ROOT, "_badges", "*", "*.md")):
        fm = load_entry(f)
        urls = {canon(l.get("url")) for l in (fm.get("links") or []) if isinstance(l, dict)} | {canon(s.get("url")) for s in (fm.get("sources") or []) if isinstance(s, dict) and s.get("url")}
        existing.append({"id": fm.get("id"), "event": fm.get("event"), "title": norm(fm.get("title")), "makers": [norm(m.get("name")) for m in (fm.get("makers") or []) if isinstance(m, dict)], "urls": urls})
    for extra in a.extra_stubs:
        for s in json.load(open(extra)):
            existing.append({"id": s["id"], "event": s["event"], "title": norm(s["title"]), "makers": [norm(m.get("name")) for m in s.get("makers", [])], "urls": {canon(l["url"]) for l in s.get("links", [])}})
    url_index = {}
    for e in existing:
        for u in e["urls"]:
            if u: url_index.setdefault(u, e["id"])
    stubs, dropped, seen_urls, seen_keys = [], [], set(), set()
    for r in results:
        for c in r.get("candidates") or []:
            title = (c.get("title") or "").strip()
            url = (c.get("url") or "").strip()
            if not title or not url: continue
            cu = canon(url)
            if cu in url_index: dropped.append((title, url, "url matches " + url_index[cu])); continue
            if cu in seen_urls: dropped.append((title, url, "duplicate url in sweep")); continue
            ev = resolve_event(c.get("event_hint"), c.get("year"), events, new_events)
            nt, nm = norm(title), norm(c.get("maker"))
            hit = None
            for e in existing:
                if ev != "other" and e["event"] not in (ev, None): continue
                if not e["title"] or not nt: continue
                sim = difflib.SequenceMatcher(None, nt, e["title"]).ratio()
                if sim >= 0.88 and (not nm or not e["makers"] or any(nm in m or m in nm for m in e["makers"] if m)):
                    hit = e["id"]; break
            if hit: dropped.append((title, url, f"title ~ {hit}")); continue
            key = (nt, ev)
            if key in seen_keys: dropped.append((title, url, "duplicate title in sweep")); continue
            seen_keys.add(key); seen_urls.add(cu)
            slug = slugify(title)
            eid = f"{ev}-{slug}"
            n = 2
            ids_taken = {e["id"] for e in existing} | {s["id"] for s in stubs}
            while eid in ids_taken: eid = f"{ev}-{slug}-{n}"; n += 1
            urls = list(dict.fromkeys([url] + [u for u in (c.get("extra_urls") or []) if u]))
            def classify(u):
                h = u.lower()
                if "github.com" in h or "gitlab.com" in h: return "repo"
                if "hackaday.io" in h: return "hackaday"
                if any(x in h for x in ("tindie", "uberflux", "shopify", "etsy", "ko-fi", "/shop", "store")): return "store"
                if any(x in h for x in ("pcbway.com/project", "oshpark.com", "oshwlab")): return "fab"
                if any(x in h for x in ("hackaday.com", "hackster.io")): return "article"
                if any(x in h for x in ("youtube", "youtu.be")): return "video"
                if any(x in h for x in ("reddit", "forum.defcon", "twitter", "x.com", "bsky", "mastodon")): return "social"
                return "website"
            stubs.append(OrderedDict([
                ("id", eid), ("title", title), ("type", coerce_type(c.get("type"))), ("event", ev), ("event_name", events[ev]["name"]),
                ("year", c.get("year") or events[ev].get("year")),
                ("makers", [OrderedDict([("name", c["maker"].strip())])] if c.get("maker") else []),
                ("summary", ""), ("functions", ""), ("notes", [c["note"]] if c.get("note") else []), ("how_to_get", ""), ("price", ""), ("price_usd", None),
                ("quantity", ""), ("availability", "unknown"), ("status", "listed"),
                ("links", [OrderedDict([("url", u), ("kind", classify(u)), ("from", "discovery")]) for u in urls]),
                ("contact", OrderedDict()),
                ("sources", [OrderedDict([("kind", "url"), ("url", url), ("title", title), ("accessed", a.date), ("note", f"Found by the archive's discovery sweep (angle: {r.get('angle')}); event read as '{c.get('event_hint') or 'unknown'}'.")])]),
                ("research", OrderedDict([("status", "stub")])),
                ("intake", OrderedDict([("image_urls", [c["image_url"]] if c.get("image_url") else [])])),
            ]))
            existing.append({"id": eid, "event": ev, "title": nt, "makers": [nm], "urls": {cu}})
    if new_events:
        yaml.add_representer(OrderedDict, lambda d, x: d.represent_mapping("tag:yaml.org,2002:map", x.items()))
        open(EVENTS_PATH, "w", encoding="utf-8").write("# Events that badges and SAOs are catalogued under. Key = event id.\n" + yaml.dump(events, allow_unicode=True, sort_keys=False, width=1000))
    out = os.path.join(ROOT, "data", f"stubs_{a.name}.json")
    json.dump(stubs, open(out, "w"), indent=1, ensure_ascii=False)
    rep = os.path.join(ROOT, "data", f"discovery_{a.name}_dropped.json")
    json.dump(dropped, open(rep, "w"), indent=1, ensure_ascii=False)
    by_ev = {}
    for s in stubs: by_ev[s["event"]] = by_ev.get(s["event"], 0) + 1
    print(f"stubs: {len(stubs)} -> {out}; dropped as duplicates: {len(dropped)} ({rep}); new events: {new_events}")
    print("by event:", dict(sorted(by_ev.items(), key=lambda kv: -kv[1])))

if __name__ == "__main__":
    main()
