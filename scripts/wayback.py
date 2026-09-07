#!/usr/bin/env python3
"""Make sure every external link in every entry has a Wayback Machine snapshot, and record it.

For each `links[].url`, `sources[].url` (kind url) and `images[].source` in every entry:
  1. ask the availability API for the closest snapshot; if one exists within --max-age days, use it;
  2. otherwise ask Save Page Now (https://web.archive.org/save/<url>) to capture it;
  3. write the snapshot URL back into the entry as `archived:` next to the original.

Polite by design: one SPN request every --spn-interval seconds (default 8), one availability lookup
per second, retries on 429/5xx with backoff. Idempotent: links that already have `archived` are
skipped. Entries modified in the last --quiet-minutes are skipped so we never race a research agent
that is mid-edit; the file is re-read immediately before writing.

  scripts/wayback.py                 # all entries
  scripts/wayback.py --limit 50      # first 50 links needing work
  scripts/wayback.py --only dc30     # one event folder
  scripts/wayback.py --dry-run
"""
import argparse, glob, json, os, re, sys, time, datetime, urllib.parse, urllib.request, urllib.error
from collections import OrderedDict
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "badgelife-archive-wayback/0.1 (+https://github.com/holdTheDoorHoid/badgelife-archive)"}
SKIP_HOSTS = ("web.archive.org", "archive.org", "localhost", "127.0.0.1", "docs.google.com", "forms.gle", "mailto:")

yaml.add_representer(OrderedDict, lambda d, x: d.represent_mapping("tag:yaml.org,2002:map", x.items()))
def _str(d, s): return d.represent_scalar("tag:yaml.org,2002:str", s, style="|" if "\n" in s else None)
yaml.add_representer(str, _str)

def load(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    return yaml.safe_load(m.group(1)) or {}, m.group(2)

def save(path, fm, body):
    open(path, "w", encoding="utf-8").write("---\n" + yaml.dump(fm, allow_unicode=True, sort_keys=False, width=1000) + "---\n" + body)

def http(url, timeout=60, method="GET"):
    req = urllib.request.Request(url, headers=UA, method=method)
    return urllib.request.urlopen(req, timeout=timeout)

def available(url, max_age_days):
    api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    for attempt in range(3):
        try:
            with http(api, 30) as r:
                d = json.load(r)
            snap = (d.get("archived_snapshots") or {}).get("closest")
            if snap and snap.get("available"):
                ts = snap.get("timestamp", "")
                try:
                    when = datetime.datetime.strptime(ts[:8], "%Y%m%d")
                    if (datetime.datetime.utcnow() - when).days <= max_age_days:
                        return snap["url"].replace("http://web.archive.org", "https://web.archive.org")
                except ValueError:
                    pass
            return None
        except Exception as e:
            time.sleep(3 * (attempt + 1))
    return None

def save_page_now(url):
    api = "https://web.archive.org/save/" + url
    for attempt in range(3):
        try:
            req = urllib.request.Request(api, headers=UA)
            opener = urllib.request.build_opener(NoRedirect)
            r = opener.open(req, timeout=120)
            loc = r.headers.get("Location") or r.headers.get("Content-Location")
            if loc:
                if loc.startswith("/web/"): loc = "https://web.archive.org" + loc
                return loc
            final = r.geturl()
            if "/web/" in final: return final
            return None
        except urllib.error.HTTPError as e:
            loc = e.headers.get("Location") or e.headers.get("Content-Location")
            if e.code in (301, 302) and loc:
                return ("https://web.archive.org" + loc) if loc.startswith("/web/") else loc
            if e.code in (429, 503, 520, 523):
                time.sleep(30 * (attempt + 1)); continue
            return None
        except Exception:
            time.sleep(10 * (attempt + 1))
    return None

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def targets(fm):
    for l in fm.get("links") or []:
        if isinstance(l, dict) and l.get("url"): yield l, "url", "archived"
    for s in fm.get("sources") or []:
        if isinstance(s, dict) and s.get("kind") == "url" and s.get("url"): yield s, "url", "archived"
    for i in fm.get("images") or []:
        if isinstance(i, dict) and i.get("source") and i["source"].startswith("http"): yield i, "source", "archived"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0); ap.add_argument("--only", default="")
    ap.add_argument("--max-age", type=int, default=365); ap.add_argument("--spn-interval", type=float, default=8.0)
    ap.add_argument("--quiet-minutes", type=int, default=15); ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    files = sorted(glob.glob(os.path.join(ROOT, "_badges", a.only + "*" if a.only else "*", "*.md")))
    done = skipped = failed = 0
    cache = {}
    for path in files:
        if not os.path.exists(path):
            continue  # merged or removed since we listed the folder
        if (time.time() - os.path.getmtime(path)) < a.quiet_minutes * 60:
            continue
        try:
            fm, body = load(path)
        except Exception as e:
            print(f"SKIP {path}: {e}", flush=True); continue
        todo = [(obj, k, ak) for obj, k, ak in targets(fm) if not obj.get(ak) and not any(h in obj[k] for h in SKIP_HOSTS)]
        if not todo: continue
        changed = False
        for obj, k, ak in todo:
            if a.limit and done >= a.limit: break
            url = obj[k].strip()
            if url in cache:
                snap = cache[url]
            else:
                snap = available(url, a.max_age); time.sleep(1)
                if not snap and not a.dry_run:
                    snap = save_page_now(url); time.sleep(a.spn_interval)
                cache[url] = snap
            if snap:
                if not a.dry_run: obj[ak] = snap
                changed = True; done += 1
                print(f"ok   {url} -> {snap}", flush=True)
            else:
                failed += 1; print(f"FAIL {url}", flush=True)
        if changed and not a.dry_run and os.path.exists(path):
            fm2, body2 = load(path)  # re-read right before writing to minimise clobber risk
            for (obj, k, ak) in targets(fm):
                if obj.get(ak):
                    for obj2, k2, ak2 in targets(fm2):
                        if obj2.get(k2) == obj.get(k) and not obj2.get(ak2): obj2[ak2] = obj[ak]
            save(path, fm2, body2)
        if a.limit and done >= a.limit: break
    print(f"archived={done} failed={failed}")

if __name__ == "__main__":
    main()
