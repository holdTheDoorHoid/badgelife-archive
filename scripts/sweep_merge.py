#!/usr/bin/env python3
"""Fold an event-year sweep workflow's results into the archive's inputs.

  scripts/sweep_merge.py <workflow transcript dir>... [--name sweep] [--min-year 2006]

Reads journal.jsonl (type=result records from the sweep agents), then:
  1. writes data/discovery_<name>.json in the shape discovery_to_stubs.py expects (one result block per task);
  2. merges confirmed editions into _data/events.yml: new ids for editions reported held=true (with dates and
     location when given), and fills empty dates/location on existing events. Editions reported held=false are
     listed, never created; existing events are never removed.
  3. writes data/sweep_<name>_events.json with everything the agents said about each edition, for review.
"""
import argparse, json, os, re, sys
from collections import OrderedDict, defaultdict
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
EVENTS_PATH = os.path.join(ROOT, "_data", "events.yml")

def results_from_journal(d):
    out = {}
    for line in open(os.path.join(d, "journal.jsonl"), encoding="utf-8"):
        try: rec = json.loads(line)
        except ValueError: continue
        if rec.get("type") != "result": continue
        r = rec.get("result")
        if isinstance(r, str):
            try: r = json.loads(r)
            except ValueError: continue
        if isinstance(r, dict) and "candidates" in r and "key" in r:
            out[r["key"]] = r  # later records win (resumed runs)
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("run_dir", nargs="+", help="one or more workflow transcript dirs; later dirs override earlier results for the same task key"); ap.add_argument("--name", default="sweep"); ap.add_argument("--min-year", type=int, default=2006)
    ap.add_argument("--dry-run", action="store_true"); a = ap.parse_args()
    res = {}
    for d in a.run_dir: res.update(results_from_journal(d))
    plan = {t["key"]: t for t in json.load(open(os.path.join(ROOT, "data", "sweep_plan.json")))}
    missing = sorted(set(plan) - set(res))
    print(f"{len(res)} task results of {len(plan)} planned; missing: {missing if len(missing) <= 20 else str(len(missing)) + ' tasks'}")
    # 1. discovery json
    blocks = []
    for k, r in res.items():
        cands = []
        for c in r.get("candidates") or []:
            c = dict(c); c["note"] = (c.get("note") or "").strip()
            # Queercon and TiaraCon run during DEF CON week but are filed under their own events, whatever the task hinted
            tm = re.search(r"\b(queercon|tiaracon)\b", (c.get("title") or "") + " " + (c.get("maker") or ""), re.I)
            if tm:
                yr = c.get("year")
                dm = re.match(r"^dc(\d\d)$", (c.get("event_hint") or "").strip().lower())
                if dm: yr = 1992 + int(dm.group(1))
                if yr: c["event_hint"] = f"{tm.group(1).lower()}-{yr}"
            if c.get("evidence") == "snippet": c["note"] = (c["note"] + " (seen only in a search snippet; unconfirmed)").strip()
            c["note"] = (c["note"] + f" Found by the event-year sweep, task {k}.").strip()
            cands.append(c)
        blocks.append({"angle": "sweep:" + k, "candidates": cands})
    disc = os.path.join(ROOT, "data", f"discovery_{a.name}.json")
    if not a.dry_run: json.dump({"results": blocks}, open(disc, "w"), indent=1, ensure_ascii=False)
    print(f"candidates: {sum(len(b['candidates']) for b in blocks)} -> {disc}")
    # 2. events
    import discovery_to_stubs as dts
    events = yaml.safe_load(open(EVENTS_PATH)); new_events = []
    seen = defaultdict(list)
    for k, r in res.items():
        for e in r.get("events") or []:
            hint = (e.get("hint") or "").strip()
            year = e.get("year")
            if not hint or not year or int(year) < a.min_year: continue
            eid = dts.resolve_event(hint, int(year), events, new_events)
            if eid == "other": seen["?" + hint].append(e); continue
            seen[eid].append(e)
    created, filled, not_held = [], [], []
    for eid, reports in seen.items():
        if eid.startswith("?"): continue
        held = any(x.get("held") for x in reports)
        best = max(reports, key=lambda x: (bool(x.get("dates")), bool(x.get("location")), bool(x.get("name"))))
        ev = events.get(eid)
        if not ev: continue
        if eid in new_events:
            if not held:
                not_held.append(eid); del events[eid]; new_events.remove(eid); continue
            created.append(eid)
        # only name events we just created, or resolver-made placeholders like "Thotcon 2024"; shared folders such as "BSides 2025" keep their names
        if best.get("name") and (eid in created or ev.get("name", "").startswith("Thotcon ")): ev["name"] = best["name"]; ev["short"] = best["name"]
        for f in ("dates", "location"):
            v = (best.get(f) or "").strip()
            if v and not ev.get(f): ev[f] = v; filled.append((eid, f))
        if not ev.get("year") and best.get("year"): ev["year"] = int(best["year"])
    # keep the file's key order: existing first, new ones appended
    if not a.dry_run:
        yaml.add_representer(OrderedDict, lambda d, x: d.represent_mapping("tag:yaml.org,2002:map", x.items()))
        open(EVENTS_PATH, "w", encoding="utf-8").write("# Events that badges and SAOs are catalogued under. Key = event id.\n" + yaml.dump(events, allow_unicode=True, sort_keys=False, width=1000))
        json.dump({k: v for k, v in seen.items()}, open(os.path.join(ROOT, "data", f"sweep_{a.name}_events.json"), "w"), indent=1, ensure_ascii=False)
    print(f"events created: {len(created)} {created}")
    print(f"fields filled on existing events: {len(filled)}")
    print(f"reported not held (not created): {not_held}")
    print(f"unresolved hints: {[k[1:] for k in seen if k.startswith('?')]}")

if __name__ == "__main__":
    main()
