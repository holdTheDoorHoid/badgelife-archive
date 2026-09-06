#!/usr/bin/env python3
"""Turn intake-agent results (data/intake_<name>.json) into stub records for gen_entries.py.

Input JSON shape: {"results": [{"url", "page_kind", "items": [{title, type, event, year, maker,
maker_url, slug, summary, source_urls, image_urls, existing_entry_id, confidence}], "new_event": {...}, "notes"}]}

- Items with existing_entry_id are NOT turned into stubs; their source URLs are appended as links to
  that entry (if not already present) so the research pass sees them.
- New events proposed by agents are added to _data/events.yml (deduplicated by id) unless --no-events.
- Output: data/stubs_<name>.json ready for `scripts/gen_entries.py`.
"""
import argparse, glob, json, os, re, sys, unicodedata
from collections import OrderedDict
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVENTS_PATH = os.path.join(ROOT, "_data", "events.yml")

def slugify(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return re.sub(r"-{2,}", "-", s)[:60].strip("-") or "untitled"

def classify(u):
    h = u.lower()
    if "github.com" in h or "gitlab.com" in h: return "repo"
    if "hackaday.io" in h: return "hackaday"
    if any(x in h for x in ("tindie", "uberflux", "shopify", "ko-fi", "etsy", "eventbrite", "kickstarter", "indiegogo", "crowdsupply", "/shop", "store", "gumroad", "hackerboxes")): return "store"
    if any(x in h for x in ("pcbway.com/project", "oshpark.com")): return "fab"
    if any(x in h for x in ("youtube", "youtu.be", "vimeo")): return "video"
    if any(x in h for x in ("twitter.com", "x.com", "bsky.app", "mastodon", "instagram", "discord", "reddit")): return "social"
    if "hackaday.com" in h or "hackster.io" in h: return "article"
    return "website"

def load_entry(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    return yaml.safe_load(m.group(1)) or {}, m.group(2)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("intake_json"); ap.add_argument("--name", required=True); ap.add_argument("--no-events", action="store_true")
    ap.add_argument("--date", required=True)
    a = ap.parse_args()
    data = json.load(open(a.intake_json))
    results = data["results"] if isinstance(data, dict) else data
    events = yaml.safe_load(open(EVENTS_PATH))
    existing_ids = {}
    for f in glob.glob(os.path.join(ROOT, "_badges", "*", "*.md")):
        fm, _ = load_entry(f); existing_ids[fm.get("id")] = f
    # 1. new events
    added_events = []
    for r in results:
        ne = r.get("new_event") or {}
        if ne.get("id") and ne["id"] not in events and not a.no_events:
            eid = re.sub(r"[^a-z0-9-]", "-", ne["id"].lower())
            events[eid] = OrderedDict([("name", ne.get("name") or eid), ("short", ne.get("short") or ne.get("name") or eid),
                                       ("year", int(ne.get("year") or 0)), ("family", ne.get("family") or "other"),
                                       ("location", ne.get("location") or "")])
            added_events.append(eid)
    if added_events:
        yaml.add_representer(OrderedDict, lambda d, x: d.represent_mapping("tag:yaml.org,2002:map", x.items()))
        open(EVENTS_PATH, "w", encoding="utf-8").write("# Events that badges and SAOs are catalogued under. Key = event id.\n" + yaml.dump(events, allow_unicode=True, sort_keys=False, width=1000))
        print("added events:", added_events)
    # 2. stubs + link merges
    stubs, merged, seen = [], 0, set()
    for r in results:
        for it in r.get("items") or []:
            ex = (it.get("existing_entry_id") or "").strip()
            if ex and ex in existing_ids:
                fm, body = load_entry(existing_ids[ex])
                links = fm.setdefault("links", [])
                have = {l.get("url", "").rstrip("/") for l in links if isinstance(l, dict)}
                new = [u for u in (it.get("source_urls") or []) + [r["url"]] if u and u.rstrip("/") not in have]
                if new:
                    for u in dict.fromkeys(new):
                        links.append(OrderedDict([("label", u.replace("https://", "").replace("http://", "").rstrip("/")), ("url", u), ("kind", classify(u))]))
                    yaml.add_representer(OrderedDict, lambda d, x: d.represent_mapping("tag:yaml.org,2002:map", x.items()))
                    def _s(d, s): return d.represent_scalar("tag:yaml.org,2002:str", s, style="|" if "\n" in s else None)
                    yaml.add_representer(str, _s)
                    open(existing_ids[ex], "w", encoding="utf-8").write("---\n" + yaml.dump(fm, allow_unicode=True, sort_keys=False, width=1000) + "---\n" + body)
                    merged += 1
                continue
            ev = (it.get("event") or "other").strip().lower()
            if ev not in events: ev = "other"
            slug = slugify(it.get("slug") or it.get("title"))
            eid = f"{ev}-{slug}"
            n = 2
            while eid in existing_ids or eid in seen:
                eid = f"{ev}-{slug}-{n}"; n += 1
            seen.add(eid)
            srcs = list(dict.fromkeys([r["url"]] + [u for u in (it.get("source_urls") or []) if u]))
            stubs.append(OrderedDict([
                ("id", eid), ("title", it.get("title") or "Untitled"), ("type", it.get("type") or "unknown"),
                ("event", ev), ("event_name", events[ev]["name"]), ("year", it.get("year") or events[ev].get("year")),
                ("makers", [OrderedDict([("name", it.get("maker") or "")] + ([("url", it["maker_url"])] if it.get("maker_url") else []))] if it.get("maker") else []),
                ("summary", it.get("summary") or ""), ("functions", ""), ("notes", []), ("how_to_get", ""), ("price", ""), ("price_usd", None),
                ("quantity", ""), ("availability", "unknown"), ("status", "listed"),
                ("links", [OrderedDict([("url", u), ("kind", classify(u)), ("from", "intake")]) for u in srcs]),
                ("contact", OrderedDict()),
                ("sources", [OrderedDict([("kind", "url"), ("url", r["url"]), ("title", r.get("page_title") or r["url"]), ("accessed", a.date), ("note", "Found via the project's link list; intake pass identified this item here.")])]),
                ("research", OrderedDict([("status", "stub")])),
                ("intake", OrderedDict([("confidence", it.get("confidence") or "low"), ("image_urls", it.get("image_urls") or [])])),
            ]))
    out = os.path.join(ROOT, "data", f"stubs_{a.name}.json")
    json.dump(stubs, open(out, "w"), indent=1, ensure_ascii=False)
    print(f"stubs: {len(stubs)} -> {out}; links merged into existing entries: {merged}")

if __name__ == "__main__":
    main()
