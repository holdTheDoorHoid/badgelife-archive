#!/usr/bin/env python3
"""Turn normalized stub records (JSON) into _badges/<event>/<slug>.md entry files.

Usage:
  scripts/gen_entries.py stubs.json            # create missing entries, leave existing ones alone
  scripts/gen_entries.py stubs.json --refresh  # also refresh `sources`/`notes` on entries still marked stub

Entry files are the single source of truth for the site. This script never overwrites an
entry whose research.status is not "stub" unless --force is given.

Canonical front-matter layout (see docs/contributing.md):
  title, id, type, event, year, series, makers[], summary, functions,
  look{colors[], shape, themes[], size_mm[], finish[], form_factor},
  tech{mcu, leds{count,type,note}, display, connectivity[], inputs[], power, battery,
       sao_version, sao_ports, sao_i2c, other[]},
  get_one{price, price_usd, quantity, availability, availability_note, distribution[], where},
  make_your_own{open_source, license, hardware_url, firmware_url, gerbers, gerbers_url,
                bom, bom_url, eda_tool, fab_url, notes},
  links[{label,url,kind,archived,note}], images[{file,source,credit,caption}],
  contact{discord, handles[], emails[], raw[]}, notes[], sources[], research{status,confidence,last_checked,notes},
  last_modified_date, layout: badge, parent, grand_parent, nav_exclude: true
"""
import argparse, json, os, re, sys, datetime
from collections import OrderedDict
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BADGES = os.path.join(ROOT, "_badges")
EVENTS = yaml.safe_load(open(os.path.join(ROOT, "_data", "events.yml")))

class OD(OrderedDict): pass
def _repr_od(dumper, data): return dumper.represent_mapping("tag:yaml.org,2002:map", data.items())
yaml.add_representer(OD, _repr_od)
yaml.add_representer(OrderedDict, _repr_od)

def _str_presenter(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)
yaml.add_representer(str, _str_presenter)

def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m: return None, text
    return yaml.safe_load(m.group(1)), m.group(2)

def dump_entry(fm, body):
    return "---\n" + yaml.dump(fm, allow_unicode=True, sort_keys=False, width=1000, default_flow_style=False) + "---\n" + (body or "")

def stub_to_front_matter(s, today):
    ev = EVENTS.get(s["event"], {})
    fm = OD()
    fm["title"] = s["title"]
    fm["id"] = s["id"]
    fm["layout"] = "badge"
    fm["parent"] = ev.get("short", s["event"].upper())
    fm["grand_parent"] = "Badge Archive"
    fm["nav_exclude"] = True
    fm["type"] = s.get("type", "unknown")
    fm["event"] = s["event"]
    fm["year"] = s.get("year", ev.get("year"))
    if s.get("series"): fm["series"] = s["series"]
    fm["makers"] = [OD((k, v) for k, v in m.items() if k != "inherited") for m in s.get("makers", [])]
    fm["summary"] = s.get("summary", "")
    fm["functions"] = s.get("functions", "")
    fm["look"] = OD([("colors", []), ("shape", None), ("themes", [])])
    fm["tech"] = OD([("mcu", None), ("leds", None), ("display", None), ("connectivity", []),
                     ("battery", None), ("sao_version", None)])
    fm["get_one"] = OD([("price", s.get("price", "")), ("price_usd", s.get("price_usd")),
                        ("quantity", s.get("quantity", "")), ("availability", s.get("availability", "unknown")),
                        ("distribution", []), ("where", s.get("how_to_get", ""))])
    fm["make_your_own"] = OD([("open_source", None), ("hardware_url", None), ("firmware_url", None), ("eda_tool", None)])
    links = []
    for l in s.get("links", []):
        links.append(OD([("label", l.get("label") or l["url"].replace("https://", "").replace("http://", "").rstrip("/")),
                         ("url", l["url"]), ("kind", l.get("kind", "website"))]))
    fm["links"] = links
    fm["images"] = []
    fm["contact"] = OD(s.get("contact", {}))
    fm["notes"] = list(s.get("notes", []))
    fm["status"] = s.get("status", "listed")
    fm["sources"] = [OD(x) for x in s.get("sources", [])]
    fm["research"] = OD([("status", "stub"), ("confidence", "low"), ("last_checked", today),
                         ("notes", "Imported from the community badge sheet; not yet researched.")])
    fm["last_modified_date"] = today
    return fm

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stubs")
    ap.add_argument("--refresh", action="store_true", help="refresh sheet-derived fields on entries still marked stub")
    ap.add_argument("--force", action="store_true", help="overwrite even researched entries (dangerous)")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    stubs = json.load(open(a.stubs))
    created = refreshed = skipped = 0
    for s in stubs:
        if s["event"] not in EVENTS:
            print(f"!! unknown event {s['event']} for {s['id']} — add it to _data/events.yml", file=sys.stderr)
            continue
        slug = s["id"][len(s["event"]) + 1:] if s["id"].startswith(s["event"] + "-") else s["id"]
        path = os.path.join(BADGES, s["event"], slug + ".md")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        fm_new = stub_to_front_matter(s, a.date)
        if os.path.exists(path):
            fm_old, body = split_front_matter(open(path, encoding="utf-8").read())
            status = (fm_old or {}).get("research", {}).get("status", "stub")
            if status != "stub" and not a.force:
                skipped += 1; continue
            if not a.refresh and not a.force:
                skipped += 1; continue
            # keep anything a human/agent may have touched, refresh sheet-derived bits
            for k in ("sources", "notes", "links", "contact", "functions", "get_one", "makers", "title", "type", "status"):
                fm_old[k] = fm_new[k]
            fm_old["last_modified_date"] = a.date
            open(path, "w", encoding="utf-8").write(dump_entry(fm_old, body))
            refreshed += 1
        else:
            body = "\n"
            open(path, "w", encoding="utf-8").write(dump_entry(fm_new, body))
            created += 1
    print(f"created={created} refreshed={refreshed} skipped={skipped}")

if __name__ == "__main__":
    main()
