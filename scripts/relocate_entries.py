#!/usr/bin/env python3
"""Move entries whose `event:` no longer matches their folder into the right folder.

Research can discover that an entry filed under `other` (or the wrong con) belongs to a specific
event. The validator rejects folder/event mismatches, so this script fixes them:
  - moves _badges/<old>/<slug>.md to _badges/<new>/<slug>.md (suffixing -2 on collision),
  - rewrites `id:` to <new>-<slug> and `parent:` to the event's short name,
  - moves the photo folder assets/images/badges/<old>/<slug>/ and rewrites image paths,
  - adds a `redirect_from` for the old URL so existing links keep working,
  - refuses unknown events (add them to _data/events.yml first).
Run with --dry-run to see what would move.
"""
import glob, os, re, shutil, sys, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVENTS = yaml.safe_load(open(os.path.join(ROOT, "_data", "events.yml")))

def main():
    dry = "--dry-run" in sys.argv
    moved = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "_badges", "*", "*.md"))):
        text = open(path, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
        if not m: continue
        fm_text, body = m.group(1), m.group(2)
        ev = re.search(r"^event:\s*(\S+)\s*$", fm_text, re.M)
        if not ev: continue
        new_ev = ev.group(1).strip("'\"")
        old_ev = os.path.basename(os.path.dirname(path))
        if new_ev == old_ev: continue
        if new_ev not in EVENTS:
            print(f"!! {path}: event '{new_ev}' not in _data/events.yml; skipped"); continue
        slug = os.path.basename(path)[:-3]
        new_slug = slug
        new_path = os.path.join(ROOT, "_badges", new_ev, new_slug + ".md")
        n = 2
        while os.path.exists(new_path):
            new_slug = f"{slug}-{n}"; new_path = os.path.join(ROOT, "_badges", new_ev, new_slug + ".md"); n += 1
        old_id, new_id = f"{old_ev}-{slug}", f"{new_ev}-{new_slug}"
        fm_text = re.sub(r"^id:.*$", f"id: {new_id}", fm_text, count=1, flags=re.M)
        fm_text = re.sub(r"^parent:.*$", f"parent: {EVENTS[new_ev].get('short', new_ev.upper())}", fm_text, count=1, flags=re.M)
        old_img = f"assets/images/badges/{old_ev}/{slug}/"; new_img = f"assets/images/badges/{new_ev}/{new_slug}/"
        fm_text = fm_text.replace(old_img, new_img)
        old_url = f"/badges/{old_ev}/{slug}/"
        if "redirect_from:" in fm_text:
            fm_text = fm_text.replace("redirect_from:\n", f"redirect_from:\n- {old_url}\n", 1)
        else:
            fm_text += f"\nredirect_from:\n- {old_url}"
        print(f"{'would move' if dry else 'move'} {old_id} -> {new_id}")
        if dry: moved += 1; continue
        os.makedirs(os.path.dirname(new_path), exist_ok=True)
        open(new_path, "w", encoding="utf-8").write("---\n" + fm_text + "\n---\n" + body)
        os.remove(path)
        if os.path.isdir(os.path.join(ROOT, old_img)):
            os.makedirs(os.path.dirname(os.path.join(ROOT, new_img.rstrip("/"))), exist_ok=True)
            shutil.move(os.path.join(ROOT, old_img.rstrip("/")), os.path.join(ROOT, new_img.rstrip("/")))
        moved += 1
    print(f"{'would move' if dry else 'moved'} {moved} entries")

if __name__ == "__main__":
    main()
