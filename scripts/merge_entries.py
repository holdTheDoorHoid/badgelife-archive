#!/usr/bin/env python3
"""Merge a duplicate entry into the entry that should survive.

  scripts/merge_entries.py KEEP_ID DROP_ID [--dry-run]

Links, url-sources, notes, images (files moved into the keeper's photo folder), contact fields and
the dropped entry's body (appended under a "Merged from ..." heading) are folded into KEEP; the
dropped entry's old URL is added to KEEP's redirect_from; the dropped file is deleted.
"""
import os, re, shutil, sys, glob, yaml
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
yaml.add_representer(OrderedDict, lambda d, x: d.represent_mapping("tag:yaml.org,2002:map", x.items()))
def _s(d, s): return d.represent_scalar("tag:yaml.org,2002:str", s, style="|" if "\n" in s else None)
yaml.add_representer(str, _s)

def find(eid):
    for f in glob.glob(os.path.join(ROOT, "_badges", "*", "*.md")):
        t = open(f, encoding="utf-8").read()
        if re.search(rf"^id: {re.escape(eid)}\s*$", t, re.M): return f
    return None

def load(path):
    t = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", t, re.S)
    return yaml.safe_load(m.group(1)) or {}, m.group(2)

def canon(u): return re.sub(r"^https?://(www\.)?", "", (u or "").strip().rstrip("/")).lower()

def merge(keep_id, drop_id, dry=False):
    kp, dp = find(keep_id), find(drop_id)
    if not kp or not dp: print(f"!! missing file for {keep_id if not kp else drop_id}"); return False
    k, kbody = load(kp); d, dbody = load(dp)
    have = {canon(l.get("url")) for l in k.get("links") or []}
    for l in d.get("links") or []:
        if canon(l.get("url")) not in have: k.setdefault("links", []).append(l); have.add(canon(l.get("url")))
    shave = {canon(s.get("url")) for s in k.get("sources") or [] if s.get("url")}
    for s in d.get("sources") or []:
        if s.get("kind") == "sheet" or canon(s.get("url")) not in shave: k.setdefault("sources", []).append(s)
    for n in d.get("notes") or []:
        if n not in (k.get("notes") or []): k.setdefault("notes", []).append(n)
    kev, kslug = k["event"], os.path.basename(kp)[:-3]
    for im in d.get("images") or []:
        src = os.path.join(ROOT, im.get("file", ""))
        if os.path.exists(src):
            dst_dir = os.path.join(ROOT, "assets", "images", "badges", kev, kslug); os.makedirs(dst_dir, exist_ok=True)
            dst = os.path.join(dst_dir, os.path.basename(src))
            if not dry: shutil.move(src, dst)
            im["file"] = os.path.relpath(dst, ROOT)
            k.setdefault("images", []).append(im)
    for key, val in (d.get("contact") or {}).items():
        kc = k.setdefault("contact", {})
        if isinstance(val, list): kc[key] = list(dict.fromkeys((kc.get(key) or []) + val))
        elif not kc.get(key): kc[key] = val
    for fld in ("summary", "functions"):
        if not k.get(fld) and d.get(fld): k[fld] = d[fld]
    for sect in ("tech", "look", "get_one", "make_your_own"):
        ks, ds = k.get(sect) or {}, d.get(sect) or {}
        for kk, vv in ds.items():
            if vv not in (None, "", []) and ks.get(kk) in (None, "", [], "unknown"): ks[kk] = vv
        k[sect] = ks
    old_url = f"/badges/{d['event']}/{os.path.basename(dp)[:-3]}/"
    rf = k.get("redirect_from") or []
    if old_url not in rf: rf.append(old_url)
    k["redirect_from"] = rf
    k.setdefault("research", {})["notes"] = ((k.get("research") or {}).get("notes") or "") + f" Merged with duplicate entry '{d.get('title')}' ({drop_id})."
    k["last_modified_date"] = d.get("last_modified_date") or k.get("last_modified_date")
    if dbody.strip() and dbody.strip() not in kbody:
        kbody = kbody.rstrip("\n") + f"\n\n## Notes merged from the duplicate entry \"{d.get('title')}\"\n\n" + dbody.strip() + "\n"
    print(f"{'would merge' if dry else 'merged'} {drop_id} -> {keep_id}")
    if dry: return True
    open(kp, "w", encoding="utf-8").write("---\n" + yaml.dump(k, allow_unicode=True, sort_keys=False, width=1000) + "---\n" + kbody)
    os.remove(dp)
    ddir = os.path.join(ROOT, "assets", "images", "badges", d["event"], os.path.basename(dp)[:-3])
    if os.path.isdir(ddir) and not os.listdir(ddir): os.rmdir(ddir)
    return True

if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    merge(a[0], a[1], "--dry-run" in sys.argv)
