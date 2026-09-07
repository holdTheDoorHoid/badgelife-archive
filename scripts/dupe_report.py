#!/usr/bin/env python3
"""Print the duplicate pairs flagged in a run's flags JSON, resolved to current ids. Usage: dupe_report.py data/runN_flags.json"""
import json, os, re, glob, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = json.load(open(sys.argv[1]))
ids = {}; redirects = {}
for p in glob.glob(os.path.join(ROOT, "_badges", "*", "*.md")):
    t = open(p, encoding="utf-8").read(); m = re.search(r"^id:\s*(\S+)", t, re.M)
    if not m: continue
    i = t.find("\nresearch:"); st = re.search(r"\n[ \t]+status:[ \t]*(\S+)", t[i:i+600]) if i >= 0 else None
    top = re.search(r"^status:\s*(\S+)", t, re.M)
    ids[m.group(1)] = (p, os.path.getsize(p), st.group(1) if st else "?", top.group(1) if top else "")
    for r in re.findall(r"^- (/badges/[^/]+/[^/]+/)", t, re.M): redirects[r] = m.group(1)
events = sorted({os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(ROOT, "_badges", "*", "*.md"))}, key=len, reverse=True)
def resolve(x):
    x = x.strip()
    if x.startswith("_badges/"): x = x[8:-3].replace("/", "-", 1)
    x = x.split()[0].strip("(),")
    if x in ids: return x
    for e in events:
        if x.startswith(e + "-"):
            u = f"/badges/{e}/{x[len(e)+1:]}/"
            if u in redirects: return redirects[u]
    return None
for a, b in s["dupes"]:
    ra, rb = resolve(a), resolve(b)
    same = ra and rb and ids[ra][0].split("/")[-2] == ids[rb][0].split("/")[-2]
    fa = f"{ra} [{ids[ra][1]}B {ids[ra][2]} {ids[ra][3]}]" if ra else f"{a} [missing]"
    fb = f"{rb} [{ids[rb][1]}B {ids[rb][2]} {ids[rb][3]}]" if rb else f"{b.split()[0]} [missing]"
    print(f"{'SAME' if same else 'diff'} | {fa} <> {fb}  {b[len(b.split()[0]):][:70].strip()}")
