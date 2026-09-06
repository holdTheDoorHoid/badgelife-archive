#!/usr/bin/env python3
"""Download a photo for an entry into assets/images/badges/<event>/<slug>/ and print the YAML
block to add under `images:`.

  scripts/fetch_image.py URL --event dc30 --slug jollybadge --source PAGE_URL --credit "Maker" --caption "Front"

Images are resized to fit 1400px on the long side and saved as JPEG (or PNG/GIF kept as-is when
they are small and have transparency/animation). Refuses files that are not images. Prints the
relative path plus a ready-to-paste YAML snippet. Exit code 0 on success.
"""
import argparse, hashlib, io, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) badgelife-archive/0.1 (+https://github.com/holdTheDoorHoid/badgelife-archive)"}

def fullsize(url):
    # hackaday.io serves thumbnails via /images/resize/WxH/<id>.jpg; the original lives at /images/<id>.jpg
    m = re.match(r"(https?://cdn\.hackaday\.io/images/)resize/\d+x\d+/(.+)$", url)
    if m: return m.group(1) + m.group(2)
    # GitHub blob URLs -> raw
    m = re.match(r"https?://github\.com/([^/]+)/([^/]+)/blob/(.+)$", url)
    if m: return f"https://raw.githubusercontent.com/{m.group(1)}/{m.group(2)}/{m.group(3)}"
    return url

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url"); ap.add_argument("--event", required=True); ap.add_argument("--slug", required=True)
    ap.add_argument("--source", default=""); ap.add_argument("--credit", default=""); ap.add_argument("--caption", default="")
    ap.add_argument("--name", default=None, help="file stem (default: short hash of the URL)")
    ap.add_argument("--max", type=int, default=1400)
    a = ap.parse_args()
    if not re.fullmatch(r"[a-z0-9-]+", a.event) or not re.fullmatch(r"[a-z0-9-]+", a.slug):
        sys.exit("event/slug must be lowercase slugs")
    url = fullsize(a.url)
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            ctype = r.headers.get("Content-Type", "")
            data = r.read(25 * 1024 * 1024)
    except Exception as e:
        if url != a.url:
            try:
                with urllib.request.urlopen(urllib.request.Request(a.url, headers=UA), timeout=60) as r:
                    ctype = r.headers.get("Content-Type", ""); data = r.read(25 * 1024 * 1024)
            except Exception as e2:
                sys.exit(f"download failed: {e2}")
        else:
            sys.exit(f"download failed: {e}")
    if not data or (not ctype.startswith("image/") and not data[:4] in (b"\x89PNG", b"\xff\xd8\xff\xe0", b"\xff\xd8\xff\xe1", b"GIF8", b"RIFF")):
        if not data[:3] in (b"\xff\xd8\xff",):
            sys.exit(f"not an image (content-type {ctype!r})")
    stem = a.name or hashlib.sha1(url.encode()).hexdigest()[:10]
    outdir = os.path.join(ROOT, "assets", "images", "badges", a.event, a.slug)
    os.makedirs(outdir, exist_ok=True)
    try:
        from PIL import Image
        im = Image.open(io.BytesIO(data))
        animated = getattr(im, "is_animated", False)
        if animated and im.format == "GIF" and len(data) < 4 * 1024 * 1024:
            path = os.path.join(outdir, stem + ".gif"); open(path, "wb").write(data)
        else:
            im.load()
            has_alpha = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
            im.thumbnail((a.max, a.max))
            if has_alpha and im.width * im.height < 1_200_000:
                path = os.path.join(outdir, stem + ".png"); im.convert("RGBA").save(path, optimize=True)
            else:
                path = os.path.join(outdir, stem + ".jpg"); im.convert("RGB").save(path, quality=84, optimize=True, progressive=True)
    except ImportError:
        ext = ".png" if data[:4] == b"\x89PNG" else ".gif" if data[:4] == b"GIF8" else ".jpg"
        path = os.path.join(outdir, stem + ext); open(path, "wb").write(data)
    except Exception as e:
        sys.exit(f"image decode failed: {e}")
    rel = os.path.relpath(path, ROOT)
    def q(s): return '"' + s.replace('"', '\\"') + '"'
    print(rel)
    print("  - file: " + rel)
    print("    source: " + q(a.source or a.url))
    if a.credit: print("    credit: " + q(a.credit))
    if a.caption: print("    caption: " + q(a.caption))
    print(f"# saved {os.path.getsize(path)//1024} KB", file=sys.stderr)

if __name__ == "__main__":
    main()
