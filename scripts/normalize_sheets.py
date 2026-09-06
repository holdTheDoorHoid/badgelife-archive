#!/usr/bin/env python3
"""Normalize the five badge.life DEF CON sheets (DC30-DC34) into one stub schema.

Input : <id>.csv files exported from Google Sheets (first tab) in the cwd.
Output: stubs.json  - list of entry dicts (one per badge/SAO row)
        stubs_report.txt - counts and anomalies
"""
import csv, json, re, sys, unicodedata
from collections import OrderedDict, Counter

SHEETS = OrderedDict([
    ("dc30", ("1cu99HozImdjNqTEM8iFsNzNswNw5De0Oe_hax3ywZ2U", 2022, "DEF CON 30")),
    ("dc31", ("1ll9GVWq1jELk79OyfdalMrgccdF3AGo2qEQIxnKsXdY", 2023, "DEF CON 31")),
    ("dc32", ("1POGyxIY4eBrXeD2hWqKz8fm9uuuy7yG1XwhVF1pnmzI", 2024, "DEF CON 32")),
    ("dc33", ("1_eJnHTbvm-uhvslkRayfEJ99Z5agVZCl1GPqbFqwMFg", 2025, "DEF CON 33")),
    ("dc34", ("1wQ6J0tJiVCPgppxiPg_mM6mS6Il-jm3Ez1fj3a-7XRs", 2026, "DEF CON 34")),
])

URL_RE = re.compile(r'(https?://[^\s,;<>()\[\]"\']+|(?<![\w@])(?:www\.|shop\.|[a-z0-9-]+\.)+(?:com|org|net|io|cc|co|pink|shop|dev|me|app|us|xyz|info|tech|store|life)(?:/[^\s,;<>()\[\]"\']*)?)', re.I)
EMAIL_RE = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
HANDLE_RE = re.compile(r'(?<![\w/])@([A-Za-z0-9_.]{2,32})')

def clean(s):
    return (s or "").replace("\r", "").strip()

def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return re.sub(r"-{2,}", "-", s)[:60].strip("-")

def urls_in(*texts):
    out = []
    for t in texts:
        for m in URL_RE.findall(t or ""):
            u = m.strip(".")
            if not u.lower().startswith("http"):
                u = "https://" + u
            if u not in out:
                out.append(u)
    return out

def classify_link(u):
    h = u.lower()
    if "github.com" in h or "gitlab.com" in h: return "repo"
    if "hackaday.io" in h: return "hackaday"
    if any(x in h for x in ("tindie", "uberflux", "shopify", "ko-fi", "etsy", "eventbrite", "kickstarter", "indiegogo", "crowdsupply", "shop.", "/shop", "store", "gumroad", "hackerboxes", "square.site", "bigcartel")): return "store"
    if any(x in h for x in ("twitter.com", "x.com", "bsky.app", "mastodon", "instagram", "discord", "linkedin", "facebook", "youtube", "youtu.be", "tiktok", "reddit")): return "social"
    if any(x in h for x in ("docs.google", "forms.gle", "notion.site")): return "doc"
    return "website"

def infer_type(explicit, *texts):
    e = (explicit or "").lower()
    if "sao" in e or "add on" in e or "add-on" in e: return "sao"
    if "badge" in e: return "badge"
    blob = " ".join(t or "" for t in texts).lower()
    if "minibadge" in blob or "mini badge" in blob: return "minibadge"
    if re.search(r"\bsao\b|shitty add|add-on|addon|add on", blob): return "sao"
    if "badge" in blob: return "badge"
    return "unknown"

def price_usd(s):
    m = re.search(r"\$\s?(\d+(?:\.\d+)?)", s or "")
    if m: return float(m.group(1))
    m = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*", s or "")
    if m: return float(m.group(1))
    if re.search(r"\bfree\b", (s or "").lower()): return 0.0
    return None

def availability_from(*texts):
    blob = " ".join(t or "" for t in texts).lower()
    if "sold out" in blob or "<sold out>" in blob: return "sold_out"
    if "cancel" in blob or "not happening" in blob or "no badge" in blob: return "cancelled"
    if "rumor" in blob or "rumour" in blob or "unconfirmed" in blob: return "rumored"
    if "free" in blob: return "free"
    return "unknown"

def base_entry(event, year, event_name):
    return OrderedDict([
        ("id", None), ("title", None), ("type", "unknown"),
        ("event", event), ("event_name", event_name), ("year", year),
        ("makers", []), ("summary", ""), ("functions", ""), ("notes", []),
        ("how_to_get", ""), ("price", ""), ("price_usd", None), ("quantity", ""),
        ("availability", "unknown"), ("status", "listed"),
        ("links", []), ("contact", OrderedDict()),
        ("sources", []), ("research", OrderedDict([("status", "stub")])),
    ])

def add_contact(e, text):
    text = clean(text)
    if not text: return
    for em in EMAIL_RE.findall(text):
        e["contact"].setdefault("emails", [])
        if em not in e["contact"]["emails"]: e["contact"]["emails"].append(em)
    rest = EMAIL_RE.sub("", text)
    for u in urls_in(rest):
        add_link(e, u, "social" if classify_link(u) == "social" else classify_link(u), "contact")
    rest2 = URL_RE.sub("", rest)
    for h in HANDLE_RE.findall(rest2):
        e["contact"].setdefault("handles", [])
        if "@" + h not in e["contact"]["handles"]: e["contact"]["handles"].append("@" + h)
    leftover = HANDLE_RE.sub("", rest2).strip(" ,;/-|")
    if leftover and len(leftover) > 1:
        e["contact"].setdefault("raw", [])
        if leftover not in e["contact"]["raw"]: e["contact"]["raw"].append(leftover)

def _canon(u):
    u = u.strip().rstrip("/")
    return re.sub(r"^https?://(www\.)?", "", u).lower()

def add_link(e, url, kind=None, field=None):
    url = url.strip()
    if any(_canon(l["url"]) == _canon(url) for l in e["links"]): return
    e["links"].append(OrderedDict([("url", url), ("kind", kind or classify_link(url)), ("from", field)]))

def add_note(e, text, label=None):
    text = clean(text)
    if not text or text in ("??", "?", "-", "N/A", "n/a", "TBD", "tbd"): return
    e["notes"].append((label + ": " if label else "") + text)

def read_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    return rows[0], [r + [""] * (len(rows[0]) - len(r)) for r in rows[1:] if any(c.strip() for c in r)]

def parse_dc30(rows, ev):
    out = []
    for i, r in enumerate(rows, start=2):
        title, maker, how, link, price, notes, upd = (clean(c) for c in r[:7])
        if not title: continue
        e = base_entry(*ev)
        e["title"] = title
        e["type"] = infer_type(None, title, notes, how)
        if maker: e["makers"].append(OrderedDict([("name", maker)]))
        e["how_to_get"] = how if how not in ("??", "?") else ""
        e["price"] = price if price not in ("??", "?") else ""
        e["price_usd"] = price_usd(price)
        for u in urls_in(link, notes, how): add_link(e, u, None, "link")
        add_note(e, notes)
        e["availability"] = availability_from(title, notes, price, how)
        e["sources"].append(OrderedDict([("kind", "sheet"), ("event", ev[0]), ("row", i), ("updated", upd)]))
        out.append(e)
    return out

def parse_dc31(rows, ev):
    out = []
    for i, r in enumerate(rows, start=2):
        maker, title, info, link, price, notes, upd = (clean(c) for c in r[:7])
        if not title and not info and not link:
            # maker-only placeholder rows: keep as "listed, no details" stubs
            if not maker or maker.lower().startswith("please note") or re.fullmatch(r"[\$\d,.\s]+", maker):
                continue
            e = base_entry(*ev)
            e["title"] = f"{maker} (listed for {ev[2]}, no details)"
            e["type"] = "unknown"
            e["makers"].append(OrderedDict([("name", maker)]))
            e["status"] = "listed_no_details"
            e["sources"].append(OrderedDict([("kind", "sheet"), ("event", ev[0]), ("row", i), ("updated", upd)]))
            out.append(e)
            continue
        e = base_entry(*ev)
        e["title"] = title or f"{maker} (unnamed badge/SAO)"
        e["type"] = infer_type(None, title, info, notes)
        if maker: e["makers"].append(OrderedDict([("name", maker)]))
        e["how_to_get"] = info
        e["price"] = price if price not in ("??", "?") else ""
        e["price_usd"] = price_usd(price)
        for u in urls_in(link, info, notes): add_link(e, u, None, "link")
        add_note(e, notes)
        e["availability"] = availability_from(title, info, notes, price)
        e["sources"].append(OrderedDict([("kind", "sheet"), ("event", ev[0]), ("row", i), ("updated", upd)]))
        out.append(e)
    return out

def parse_dc32(rows, ev):
    out, last_maker = [], ""
    for i, r in enumerate(rows, start=2):
        maker, title, links, price, contact, funcs, qty, notes, upd = (clean(c) for c in r[:9])
        if maker: last_maker = maker
        if not title and not links and not funcs:
            if maker and not price and not notes:
                e = base_entry(*ev)
                e["title"] = f"{maker} (listed for {ev[2]}, no details)"
                e["type"] = "unknown"
                e["makers"].append(OrderedDict([("name", maker), ("inherited", False)]))
                e["status"] = "listed_no_details"
                add_contact(e, contact)
                e["sources"].append(OrderedDict([("kind", "sheet"), ("event", ev[0]), ("row", i), ("updated", upd)]))
                out.append(e)
            continue
        e = base_entry(*ev)
        e["title"] = title or f"{last_maker} (unnamed badge/SAO)"
        e["type"] = infer_type(None, title, funcs, notes)
        if last_maker: e["makers"].append(OrderedDict([("name", last_maker), ("inherited", not bool(maker))]))
        e["how_to_get"] = links if not urls_in(links) else ""
        e["price"] = price
        e["price_usd"] = price_usd(price)
        e["functions"] = funcs
        e["quantity"] = qty
        for u in urls_in(links, notes, funcs): add_link(e, u, None, "links")
        add_contact(e, contact)
        add_note(e, notes)
        e["availability"] = availability_from(title, notes, price, links)
        e["sources"].append(OrderedDict([("kind", "sheet"), ("event", ev[0]), ("row", i), ("updated", upd)]))
        out.append(e)
    return out

def parse_dc33(rows, ev):
    out = []
    for i, r in enumerate(rows, start=2):
        (ts, maker, kind, bname, sname, haslink, link, hasprice, price, email,
         funcs, notes, othername) = (clean(c) for c in r[:13])
        name = maker if maker and maker.lower() not in ("other", "not listed", "") else othername
        if othername and othername != name: name = f"{name} / {othername}" if name else othername
        title = bname or sname
        if not title and not funcs and not link: continue
        e = base_entry(*ev)
        e["title"] = title or f"{name} (unnamed {kind or 'badge/SAO'})"
        e["type"] = infer_type(kind, title, funcs, notes)
        if name: e["makers"].append(OrderedDict([("name", name)]))
        e["price"] = price
        e["price_usd"] = price_usd(price)
        e["functions"] = funcs
        for u in urls_in(link, notes, funcs): add_link(e, u, None, "link")
        add_contact(e, email)
        add_note(e, notes)
        e["availability"] = availability_from(title, notes, price)
        e["sources"].append(OrderedDict([("kind", "sheet"), ("event", ev[0]), ("row", i), ("updated", ts)]))
        out.append(e)
    return out

def parse_dc34(rows, ev):
    out = []
    for i, r in enumerate(rows, start=2):
        (ts, maker, discord, email, other, newupd, kind, title, video, store,
         repo, price, funcs) = (clean(c) for c in r[:13])
        if not title and not funcs and not store and not repo: continue
        e = base_entry(*ev)
        e["title"] = title or f"{maker} (unnamed {kind or 'badge/SAO'})"
        e["type"] = infer_type(kind, title, funcs)
        if maker: e["makers"].append(OrderedDict([("name", maker)]))
        e["price"] = price
        e["price_usd"] = price_usd(price)
        e["functions"] = funcs
        if not price_usd(price) and price: e["how_to_get"] = price
        for u in urls_in(store): add_link(e, u, "store", "storefront")
        for u in urls_in(repo): add_link(e, u, "repo", "repo")
        for u in urls_in(video): add_link(e, u, "video", "video")
        for u in urls_in(funcs): add_link(e, u, None, "functions")
        if discord:
            e["contact"]["discord"] = discord
        add_contact(e, email)
        add_contact(e, other)
        e["availability"] = availability_from(title, funcs, price)
        e["sources"].append(OrderedDict([("kind", "sheet"), ("event", ev[0]), ("row", i), ("updated", ts), ("listing", newupd)]))
        out.append(e)
    return out

PARSERS = {"dc30": parse_dc30, "dc31": parse_dc31, "dc32": parse_dc32, "dc33": parse_dc33, "dc34": parse_dc34}

def parse_maker_list(path, ev):
    """Extra 'expected makers' tab (DC33 '2025' tab): one maker per line, tab-separated row number."""
    out = []
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip(): continue
        row, maker = line.split("\t", 1) if "\t" in line else ("", line)
        e = base_entry(*ev)
        e["title"] = f"{maker.strip()} (listed for {ev[2]}, no details)"
        e["type"] = "unknown"
        e["makers"].append(OrderedDict([("name", maker.strip())]))
        e["status"] = "listed_no_details"
        e["sources"].append(OrderedDict([("kind", "sheet"), ("event", ev[0]), ("row", int(row) if row.isdigit() else None), ("tab", "2025 (expected makers)"), ("updated", "")]))
        out.append(e)
    return out

def main():
    import os
    entries, report = [], []
    for ev, (sid, year, name) in SHEETS.items():
        path = f"{sid}.csv" if os.path.exists(f"{sid}.csv") else f"{ev}.csv"
        hdr, rows = read_rows(path)
        got = PARSERS[ev](rows, (ev, year, name))
        report.append(f"{ev}: {len(rows)} non-empty rows -> {len(got)} entries")
        entries.extend(got)
        extra = f"{ev}_makers.txt"
        if os.path.exists(extra):
            more = parse_maker_list(extra, (ev, year, name))
            report.append(f"{ev}: +{len(more)} expected-maker stubs from {extra}")
            entries.extend(more)
    # ids
    seen = Counter()
    for e in entries:
        slug = slugify(e["title"])
        # drop a leading event token ("dc30-jollybadge" -> "jollybadge") and handle empty slugs
        slug = re.sub(r"^(def-?con-?|dc-?)(\d{2}|xxx[iv]+)-", "", slug)
        if not slug:
            slug = (slugify(e["makers"][0]["name"]) + "-unnamed") if e["makers"] else "untitled"
        base = f"{e['event']}-{slug}"
        seen[base] += 1
        e["id"] = base if seen[base] == 1 else f"{base}-{seen[base]}"
    # merge DC34 "Update" listings into their originals (same maker+title)
    merged = []
    index = {}
    for e in entries:
        key = (e["event"], slugify(e["title"]), slugify(e["makers"][0]["name"]) if e["makers"] else "")
        src = e["sources"][0]
        if e["event"] == "dc34" and src.get("listing", "").lower().startswith("update") and key in index:
            tgt = index[key]
            for l in e["links"]:
                if not any(x["url"] == l["url"] for x in tgt["links"]): tgt["links"].append(l)
            for f in ("price", "functions", "how_to_get"):
                if e[f]: tgt[f] = e[f]
            if e["price_usd"] is not None: tgt["price_usd"] = e["price_usd"]
            tgt["notes"].extend(n for n in e["notes"] if n not in tgt["notes"])
            for k, v in e["contact"].items():
                if isinstance(v, list):
                    tgt["contact"].setdefault(k, [])
                    tgt["contact"][k].extend(x for x in v if x not in tgt["contact"][k])
                else: tgt["contact"][k] = v
            tgt["sources"].extend(e["sources"])
            report.append(f"  merged update row {src['row']} into {tgt['id']}")
            continue
        index[key] = e
        merged.append(e)
    entries = merged
    types = Counter(e["type"] for e in entries)
    links = sum(len(e["links"]) for e in entries)
    report.append(f"TOTAL {len(entries)} entries; types={dict(types)}; links={links}; with>=1 link={sum(1 for e in entries if e['links'])}")
    report.append("unknown-type titles: " + "; ".join(e["title"][:40] for e in entries if e["type"] == "unknown"))
    json.dump(entries, open("stubs.json", "w"), indent=1, ensure_ascii=False)
    open("stubs_report.txt", "w").write("\n".join(report) + "\n")
    print("\n".join(report))

if __name__ == "__main__":
    main()
