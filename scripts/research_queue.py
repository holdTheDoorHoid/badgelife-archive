#!/usr/bin/env python3
"""Priority queue of entries still waiting for research (research.status: stub).

The queue is recomputed from the entry files every time, so it survives interruptions:
an entry leaves the queue the moment an agent sets research.status to researched/verified.

  scripts/research_queue.py --summary          # how many remain, by family/type
  scripts/research_queue.py --next 60          # the next 60 ids, highest priority first
  scripts/research_queue.py --next 60 --skip 60

Priority (highest first): entries not from the automated sweep (older intake stubs), then
entries confirmed on a real page before snippet-only ones, then by event family
(DEF CON, Supercon, camps, other, BSides), then by type (badge, sao, kit, minibadge,
accessory, other), then newest year first.
"""
import argparse, glob, os, re, sys, collections
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAM = {"defcon": 0, "supercon": 1, "camp": 2, "other": 3, "bsides": 4}
TYP = {"badge": 0, "sao": 1, "kit": 2, "minibadge": 3, "accessory": 4, "other": 5, "unknown": 6}

def load_queue():
    events = yaml.safe_load(open(os.path.join(ROOT, "_data", "events.yml"), encoding="utf-8")) or {}
    rows = []
    for path in sorted(glob.glob(os.path.join(ROOT, "_badges", "*", "*.md"))):
        text = open(path, encoding="utf-8").read()
        if "status: stub" not in text:
            continue
        m = re.match(r"^---\n(.*?)\n---", text, re.S)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except Exception:
            continue
        if (fm.get("research") or {}).get("status") != "stub":
            continue
        ev = fm.get("event") or os.path.basename(os.path.dirname(path))
        fam = (events.get(ev) or {}).get("family", "other")
        sweep = "event-year sweep" in text
        snippet = "search snippet" in text
        year = fm.get("year") or (events.get(ev) or {}).get("year") or 0
        try: year = int(year)
        except Exception: year = 0
        key = (1 if sweep else 0, 1 if snippet else 0, FAM.get(fam, 3), TYP.get(fm.get("type"), 6), -year, fm.get("id") or "")
        rows.append((key, fm.get("id") or os.path.basename(path)[:-3], ev, fam, fm.get("type"), snippet))
    rows.sort()
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--next", type=int, default=0)
    ap.add_argument("--skip", type=int, default=0)
    ap.add_argument("--summary", action="store_true")
    a = ap.parse_args()
    rows = load_queue()
    if a.summary or not a.next:
        fam = collections.Counter(r[3] for r in rows); typ = collections.Counter(r[4] for r in rows)
        snip = sum(1 for r in rows if r[5])
        print(f"remaining stubs: {len(rows)}  (snippet-only: {snip})")
        print("by family:", dict(fam.most_common()))
        print("by type:  ", dict(typ.most_common()))
    if a.next:
        for r in rows[a.skip:a.skip + a.next]:
            print(r[1])

if __name__ == "__main__":
    main()
