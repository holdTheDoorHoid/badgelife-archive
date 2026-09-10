#!/usr/bin/env python3
"""Download the PCB design files (KiCad boards, Eagle boards, Gerber sets) that entries link to, so 3D models can be built.

Sources handled: GitHub repos (root, /tree/<ref>/<path>, /blob/...), GitLab repos, Hackaday.io project file lists.
Files land in data/hw/<entry id>/ (git-ignored); data/hw_manifest.json records what was found, the commit, and the licence.
Idempotent: entries already in the manifest are skipped unless --refresh. Polite: ~2 GitHub API calls per repo via `gh api`.

  scripts/fetch_hardware.py            # every entry with make_your_own.hardware_url / gerbers_url / hardware links
  scripts/fetch_hardware.py --only dc27 --limit 20
"""
import argparse, glob, json, os, re, subprocess, sys, time, urllib.parse, urllib.request, zipfile
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HW = os.path.join(ROOT, "data", "hw"); MANIFEST = os.path.join(ROOT, "data", "hw_manifest.json")
UA = {"User-Agent": "badgelife-archive-hw-fetch/0.1 (+https://github.com/holdTheDoorHoid/badgelife-archive)"}
KICAD = (".kicad_pcb",); EAGLE = (".brd",)
GERBER_LOOSE = (".gbr", ".gtl", ".gbl", ".gko", ".gm1", ".gm2", ".gbs", ".gts", ".gbo", ".gto", ".gbp", ".gtp", ".drl", ".xln", ".txt", ".gml", ".gd1", ".gpi", ".g2", ".g3")
ZIP_HINT = re.compile(r"gerb|gbr|fab|production|jlc|pcbway|oshpark|elecrow|cam|manufactur|output", re.I)
MAX_FILE = 30 * 1024 * 1024; MAX_TOTAL = 80 * 1024 * 1024

def log(*a): print(*a, flush=True)

def gh(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=60)
    if r.returncode != 0: return None
    try: return json.loads(r.stdout)
    except Exception: return None

def download(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
        n = 0
        while True:
            chunk = r.read(1 << 16)
            if not chunk: break
            f.write(chunk); n += len(chunk)
            if n > MAX_FILE: raise IOError("too large")
    return n

def parse_github(url):
    m = re.match(r"https?://(?:www\.)?github\.com/([^/]+)/([^/#?]+)(?:/(tree|blob)/([^/]+)(?:/(.*))?)?", url)
    if not m: return None
    owner, repo, kind, ref, sub = m.groups(); repo = re.sub(r"\.git$", "", repo)
    sub = urllib.parse.unquote(sub or "").strip("/")
    if kind == "blob" and sub: sub = os.path.dirname(sub)
    return owner, repo, ref, sub

def select(tree, sub):
    """tree: list of (path, size). Return list of (path, size, kind) worth downloading."""
    def under(p): return (not sub) or p == sub or p.startswith(sub + "/")
    files = [(p, s) for p, s in tree if under(p)] or tree  # fall back to the whole repo if the subfolder has nothing useful
    pick = []
    kic = [(p, s) for p, s in files if p.lower().endswith(KICAD) and s <= MAX_FILE and "backup" not in p.lower()]
    egl = [(p, s) for p, s in files if p.lower().endswith(EAGLE) and s <= MAX_FILE]
    zips = [(p, s) for p, s in files if p.lower().endswith(".zip") and ZIP_HINT.search(os.path.basename(p)) and s <= MAX_FILE]
    loose = [(p, s) for p, s in files if p.lower().endswith(GERBER_LOOSE) and s <= 3 * 1024 * 1024 and p.lower().endswith(GERBER_LOOSE[:-6]) or (p.lower().endswith((".gbr", ".gtl", ".gko", ".gm1", ".gts", ".gto")) and s <= 3 * 1024 * 1024)]
    pick += [(p, s, "kicad") for p, s in sorted(kic, key=lambda x: (x[0].count("/"), -x[1]))[:6]]
    pick += [(p, s, "eagle") for p, s in sorted(egl, key=lambda x: (x[0].count("/"), -x[1]))[:4]]
    pick += [(p, s, "gerber_zip") for p, s in sorted(zips, key=lambda x: (x[0].count("/"), -x[1]))[:3]]
    if not pick and loose:
        d = os.path.dirname(sorted(loose, key=lambda x: x[0].count("/"))[0][0])
        grp = [(p, s) for p, s in files if os.path.dirname(p) == d and s <= 3 * 1024 * 1024 and not p.lower().endswith((".png", ".jpg", ".pdf", ".md"))][:60]
        pick += [(p, s, "gerber_loose") for p, s in grp]
    total = 0; out = []
    for p, s, k in pick:
        if total + s > MAX_TOTAL: break
        out.append((p, s, k)); total += s
    return out

def fetch_github(eid, url, dest):
    parsed = parse_github(url)
    if not parsed: return {"status": "unparsed"}
    owner, repo, ref, sub = parsed
    meta = gh(f"repos/{owner}/{repo}")
    if not meta: return {"status": "repo_unavailable"}
    ref = ref or meta.get("default_branch") or "main"
    tree = gh(f"repos/{owner}/{repo}/git/trees/{urllib.parse.quote(ref, safe='')}?recursive=1")
    if not tree or "tree" not in tree: return {"status": "tree_unavailable", "ref": ref}
    entries = [(t["path"], t.get("size", 0)) for t in tree["tree"] if t.get("type") == "blob"]
    chosen = select(entries, sub)
    rec = {"status": "no_pcb_files" if not chosen else "ok", "source_url": url, "repo": f"{owner}/{repo}", "ref": ref, "subpath": sub,
           "license": ((meta.get("license") or {}).get("spdx_id") or ""), "truncated": bool(tree.get("truncated")), "files": []}
    for p, s, k in chosen:
        raw = f"https://raw.githubusercontent.com/{owner}/{repo}/{urllib.parse.quote(ref, safe='')}/{urllib.parse.quote(p)}"
        out = os.path.join(dest, p.replace("..", "_"))
        try:
            n = download(raw, out); rec["files"].append({"path": p, "size": n, "kind": k}); time.sleep(0.3)
        except Exception as e:
            rec["files"].append({"path": p, "size": s, "kind": k, "error": str(e)[:80]})
    return rec

def fetch_gitlab(eid, url, dest):
    m = re.match(r"https?://gitlab\.com/([^#?]+?)(?:/-/tree/([^/]+)(?:/(.*))?)?/?$", url)
    if not m: return {"status": "unparsed"}
    proj, ref, sub = m.group(1).strip("/"), m.group(2), (m.group(3) or "").strip("/")
    api = "https://gitlab.com/api/v4/projects/" + urllib.parse.quote(proj, safe="")
    try:
        with urllib.request.urlopen(urllib.request.Request(api, headers=UA), timeout=60) as r: meta = json.load(r)
        ref = ref or meta.get("default_branch") or "main"
        items = []; page = 1
        while page <= 10:
            with urllib.request.urlopen(urllib.request.Request(f"{api}/repository/tree?recursive=true&per_page=100&page={page}&ref={ref}", headers=UA), timeout=60) as r:
                batch = json.load(r)
            items += [(i["path"], 0) for i in batch if i.get("type") == "blob"]
            if len(batch) < 100: break
            page += 1
    except Exception as e:
        return {"status": "repo_unavailable", "error": str(e)[:80]}
    chosen = select(items, sub)
    rec = {"status": "no_pcb_files" if not chosen else "ok", "source_url": url, "repo": proj, "ref": ref, "subpath": sub, "license": "", "files": []}
    for p, s, k in chosen:
        raw = f"https://gitlab.com/{proj}/-/raw/{ref}/{urllib.parse.quote(p)}"
        try: n = download(raw, os.path.join(dest, p)); rec["files"].append({"path": p, "size": n, "kind": k})
        except Exception as e: rec["files"].append({"path": p, "size": 0, "kind": k, "error": str(e)[:80]})
    return rec

def fetch_hackaday(eid, url, dest):
    m = re.match(r"https?://hackaday\.io/project/(\d+)", url)
    if not m: return {"status": "unparsed"}
    try:
        with urllib.request.urlopen(urllib.request.Request(f"https://hackaday.io/project/{m.group(1)}/files", headers={**UA, "User-Agent": "Mozilla/5.0"}), timeout=60) as r:
            html = r.read(2_000_000).decode("utf-8", "ignore")
    except Exception as e:
        return {"status": "files_page_unavailable", "error": str(e)[:80]}
    links = re.findall(r'https://cdn\.hackaday\.io/files/[^"\'\s<>]+', html)
    seen = []; files = []
    for l in links:
        l = l.split("?")[0]
        if l in seen: continue
        seen.append(l); name = urllib.parse.unquote(os.path.basename(l))
        low = name.lower()
        if low.endswith(KICAD): kind = "kicad"
        elif low.endswith(EAGLE): kind = "eagle"
        elif low.endswith(".zip") and (ZIP_HINT.search(name) or "kicad" in low or "pcb" in low or "board" in low or "hardware" in low): kind = "gerber_zip"
        else: continue
        files.append((l, name, kind))
    rec = {"status": "no_pcb_files" if not files else "ok", "source_url": url, "repo": "hackaday.io/" + m.group(1), "ref": "", "subpath": "", "license": "", "files": []}
    for l, name, kind in files[:6]:
        try: n = download(l, os.path.join(dest, name)); rec["files"].append({"path": name, "size": n, "kind": kind}); time.sleep(0.5)
        except Exception as e: rec["files"].append({"path": name, "size": 0, "kind": kind, "error": str(e)[:80]})
    return rec

def unzip_all(dest):
    for z in glob.glob(os.path.join(dest, "**", "*.zip"), recursive=True):
        out = z[:-4] + "_unz"
        if os.path.isdir(out): continue
        try:
            with zipfile.ZipFile(z) as zf:
                members = [m for m in zf.infolist() if not m.is_dir() and m.file_size <= MAX_FILE and ".." not in m.filename]
                if sum(m.file_size for m in members) > 300 * 1024 * 1024: continue
                for m in members[:400]: zf.extract(m, out)
        except Exception: pass

def entry_urls(fm):
    my = fm.get("make_your_own") or {}
    urls = [my.get("hardware_url"), my.get("gerbers_url")]
    urls += [l.get("url") for l in (fm.get("links") or []) if isinstance(l, dict) and l.get("kind") in ("hardware", "gerbers", "design_files")]
    out = []
    for u in urls:
        if u and isinstance(u, str) and u.startswith("http") and u not in out: out.append(u)
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--only", default=""); ap.add_argument("--limit", type=int, default=0); ap.add_argument("--refresh", action="store_true")
    a = ap.parse_args()
    manifest = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
    n = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "_badges", (a.only + "*") if a.only else "*", "*.md"))):
        if not os.path.exists(path): continue  # merged or relocated since the folder was listed
        text = open(path, encoding="utf-8").read(); m = re.match(r"^---\n(.*?)\n---", text, re.S)
        try: fm = yaml.safe_load(m.group(1))
        except Exception: continue
        eid = fm.get("id")
        if not eid or fm.get("status") == "not_an_item": continue
        urls = entry_urls(fm)
        if not urls: continue
        if eid in manifest and not a.refresh: continue
        dest = os.path.join(HW, eid); recs = []
        for u in urls:
            if "github.com" in u: rec = fetch_github(eid, u, dest)
            elif "gitlab.com" in u: rec = fetch_gitlab(eid, u, dest)
            elif "hackaday.io/project/" in u: rec = fetch_hackaday(eid, u, dest)
            else: rec = {"status": "unsupported_host", "source_url": u}
            recs.append(rec)
            if rec.get("status") == "ok": break
        unzip_all(dest)
        manifest[eid] = {"sources": recs, "ok": any(r.get("status") == "ok" for r in recs)}
        json.dump(manifest, open(MANIFEST, "w"), indent=1)
        log(f"{'ok  ' if manifest[eid]['ok'] else 'none'} {eid} {[r.get('status') for r in recs]}")
        n += 1
        if a.limit and n >= a.limit: break
        time.sleep(0.5)
    ok = sum(1 for v in manifest.values() if v.get("ok")); log(f"manifest: {len(manifest)} entries, {ok} with PCB files")

if __name__ == "__main__":
    main()
