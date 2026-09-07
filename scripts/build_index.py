#!/usr/bin/env python3
"""Build assets/data/badges.json (the search index) from every _badges/**/*.md entry.

Run before `jekyll build` (CI does this) and commit the result so the site also works
for anyone who builds without running the script.

Also validates entries and exits non-zero on hard errors (missing title/event/type,
unknown event, duplicate id) so CI catches broken entries.
"""
import glob, json, os, re, sys, collections
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVENTS = yaml.safe_load(open(os.path.join(ROOT, "_data", "events.yml")))
TYPES = {"badge", "sao", "minibadge", "kit", "accessory", "other", "unknown"}
AVAIL = {"unknown", "available", "sold_out", "free", "not_released", "cancelled", "rumored", "limited"}
RESEARCH = {"stub", "researched", "verified"}

def fm_of(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m: raise ValueError(f"{path}: no front matter")
    return yaml.safe_load(m.group(1)) or {}, m.group(2)

def as_list(v):
    if v is None or v == "": return []
    if isinstance(v, (list, tuple)): return [str(x) for x in v if x not in (None, "")]
    return [str(v)]

def main():
    check_only = "--check" in sys.argv
    errors, records, ids = [], [], collections.Counter()
    files = sorted(glob.glob(os.path.join(ROOT, "_badges", "**", "*.md"), recursive=True))
    for path in files:
        rel = os.path.relpath(path, ROOT)
        try:
            fm, body = fm_of(path)
        except Exception as e:
            errors.append(str(e)); continue
        for k in ("title", "event", "type"):
            if not fm.get(k): errors.append(f"{rel}: missing {k}")
            elif not isinstance(fm.get(k), str): errors.append(f"{rel}: {k} must be a quoted string, got {type(fm.get(k)).__name__} ({fm.get(k)!r})")
        for m in fm.get("makers") or []:
            if not isinstance(m, dict) or not isinstance(m.get("name"), str):
                errors.append(f"{rel}: maker name must be a quoted string, got {m!r}")
        ev = fm.get("event")
        if ev and ev not in EVENTS: errors.append(f"{rel}: unknown event '{ev}' (add to _data/events.yml)")
        if fm.get("type") not in TYPES: errors.append(f"{rel}: type '{fm.get('type')}' not in {sorted(TYPES)}")
        get = fm.get("get_one") or {}
        if get.get("availability") and get["availability"] not in AVAIL:
            errors.append(f"{rel}: availability '{get['availability']}' not in {sorted(AVAIL)}")
        rs = (fm.get("research") or {}).get("status", "stub")
        if rs not in RESEARCH: errors.append(f"{rel}: research.status '{rs}' not in {sorted(RESEARCH)}")
        if fm.get("status") == "not_an_item":
            continue  # sheet rows that turned out not to be a badge/SAO stay on disk for provenance but are not listed
        parts = rel[len("_badges/"):-3].split("/")
        if len(parts) != 2: errors.append(f"{rel}: must be _badges/<event>/<slug>.md"); continue
        if parts[0] != ev: errors.append(f"{rel}: directory '{parts[0]}' != event '{ev}'")
        eid = fm.get("id") or f"{parts[0]}-{parts[1]}"
        ids[eid] += 1
        look, tech, make = fm.get("look") or {}, fm.get("tech") or {}, fm.get("make_your_own") or {}
        leds = tech.get("leds") or {}
        images = fm.get("images") or []
        links = fm.get("links") or []
        text_blob = " ".join(filter(None, [
            fm.get("summary"), fm.get("functions"), " ".join(as_list(fm.get("notes"))),
            re.sub(r"[#*_`\[\]()>|-]+", " ", body)[:2000],
        ]))
        rec = {
            "id": eid,
            "url": f"/badges/{parts[0]}/{parts[1]}/",
            "title": fm.get("title", ""),
            "type": fm.get("type", "unknown"),
            "event": ev,
            "event_name": EVENTS.get(ev, {}).get("name", ev),
            "family": EVENTS.get(ev, {}).get("family", "other"),
            "year": fm.get("year") or EVENTS.get(ev, {}).get("year"),
            "makers": [m.get("name", "") for m in (fm.get("makers") or []) if isinstance(m, dict)],
            "summary": fm.get("summary") or "",
            "functions": fm.get("functions") or "",
            "colors": as_list(look.get("colors")),
            "shape": look.get("shape") or "",
            "themes": as_list(look.get("themes")),
            "form_factor": look.get("form_factor") or "",
            "mcu": tech.get("mcu") or "",
            "led_count": leds.get("count") if isinstance(leds, dict) else None,
            "led_type": (leds.get("type") if isinstance(leds, dict) else None) or "",
            "display": tech.get("display") or "",
            "connectivity": as_list(tech.get("connectivity")),
            "battery": tech.get("battery") or "",
            "sao_version": tech.get("sao_version") or "",
            "price": get.get("price") or "",
            "price_usd": get.get("price_usd"),
            "quantity": get.get("quantity") or "",
            "availability": get.get("availability") or "unknown",
            "distribution": as_list(get.get("distribution")),
            "open_source": str(make.get("open_source") or "unknown").lower(),
            "has_hardware": bool(make.get("hardware_url")),
            "has_firmware": bool(make.get("firmware_url")),
            "has_gerbers": bool(make.get("gerbers") or make.get("gerbers_url")),
            "has_model": bool((fm.get("model") or {}).get("file")) if isinstance(fm.get("model"), dict) else False,
            "has_bom": bool(make.get("bom") or make.get("bom_url")),
            "eda_tool": make.get("eda_tool") or "",
            "thumb": (images[0].get("file") if images and isinstance(images[0], dict) else "") or "",
            "image_count": len(images),
            "link_kinds": sorted({(l.get("kind") or "link") for l in links if isinstance(l, dict)}),
            "link_count": len(links),
            "status": fm.get("status") or "listed",
            "research": rs,
            "text": re.sub(r"\s+", " ", text_blob).strip()[:500],
        }
        records.append(rec)
    for eid, n in ids.items():
        if n > 1: errors.append(f"duplicate id: {eid} ({n} files)")
    if errors:
        print("\n".join("ERROR " + e for e in errors), file=sys.stderr)
    if check_only:
        print(f"checked {len(files)} entries, {len(errors)} errors")
        sys.exit(1 if errors else 0)
    records.sort(key=lambda r: (-(r["year"] or 0), r["event"], r["title"].lower()))
    out = os.path.join(ROOT, "assets", "data", "badges.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    facets = {
        "events": [{"id": k, "name": v.get("name"), "short": v.get("short"), "year": v.get("year"), "family": v.get("family"),
                    "count": sum(1 for r in records if r["event"] == k)} for k, v in EVENTS.items()],
    }
    json.dump({"generated_from": len(files), "entries": records, "facets": facets}, open(out, "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"wrote {out}: {len(records)} entries, {len(errors)} errors")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
