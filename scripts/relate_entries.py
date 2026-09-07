#!/usr/bin/env python3
"""Link two entries as related (each gets the other's id in `related:`). Usage: relate_entries.py ID_A ID_B [ID_C ...]
Every id given is linked to every other one. Ids may be old ids: they are resolved through redirect_from."""
import glob, os, re, sys, yaml
from collections import OrderedDict
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
yaml.add_representer(OrderedDict, lambda d, x: d.represent_mapping("tag:yaml.org,2002:map", x.items()))
yaml.add_representer(str, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s, style="|" if "\n" in s else None))
def load(path):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", open(path, encoding="utf-8").read(), re.S)
    return yaml.safe_load(m.group(1)) or {}, m.group(2)
def find(id_):
    for p in glob.glob(os.path.join(ROOT, "_badges", "*", "*.md")):
        fm, _ = load(p)
        if fm.get("id") == id_: return p, fm
    ev, slug = id_.split("-", 1)
    for p in glob.glob(os.path.join(ROOT, "_badges", "*", "*.md")):
        fm, _ = load(p)
        for r in fm.get("redirect_from") or []:
            for e in sorted({os.path.basename(os.path.dirname(x)) for x in glob.glob(os.path.join(ROOT, "_badges", "*", "*.md"))}, key=len, reverse=True):
                if id_.startswith(e + "-") and r == f"/badges/{e}/{id_[len(e)+1:]}/": return p, fm
    return None, None
def main():
    ids = sys.argv[1:]
    found = {}
    for i in ids:
        p, fm = find(i)
        if not p: print(f"!! {i}: not found"); continue
        found[fm["id"]] = p
    for a, pa in found.items():
        fm, body = load(pa)
        rel = [r for r in (fm.get("related") or []) if r]
        for b in found:
            if b != a and b not in rel: rel.append(b)
        fm["related"] = rel
        open(pa, "w", encoding="utf-8").write("---\n" + yaml.dump(fm, allow_unicode=True, sort_keys=False, width=1000) + "---\n" + body)
        print(f"{a}: related -> {rel}")
if __name__ == "__main__": main()
