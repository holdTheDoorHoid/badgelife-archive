#!/usr/bin/env python3
"""Create badges/<event>/index.md for every event in _data/events.yml that lacks one.

Each event page lists its entries with Liquid at build time, so it never needs regenerating
after entries change. Existing event pages are left untouched (they may carry hand-written
history), unless --update is given, in which case only the generated block is refreshed.
"""
import os, re, sys, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVENTS = yaml.safe_load(open(os.path.join(ROOT, "_data", "events.yml")))
MARK_START, MARK_END = "<!-- archive:entries:start -->", "<!-- archive:entries:end -->"

def block(ev):
    return f"""{MARK_START}
{{% include event_entries.html event="{ev}" %}}
{MARK_END}"""

def entry_count(ev):
    import glob
    return len(glob.glob(os.path.join(ROOT, "_badges", ev, "*.md")))

def front_matter(ev, meta):
    # Newest events first in the sidebar; events with no entries yet stay out of the nav.
    return {
        "title": meta.get("short", ev.upper()),
        "layout": "default",
        "parent": "Badge Archive",
        "has_children": True,
        "has_toc": False,
        "nav_order": 10000 - int(meta.get("year") or 0),
        "nav_exclude": entry_count(ev) == 0,
        "event": ev,
    }

def page(ev, meta):
    fm = front_matter(ev, meta)
    body = f"# {meta.get('name', ev)}\n\n"
    details = []
    if meta.get("dates"): details.append(meta["dates"])
    if meta.get("location"): details.append(meta["location"])
    if details: body += " · ".join(details) + "\n\n"
    if meta.get("notes"): body += meta["notes"] + "\n\n"
    if meta.get("sheet"): body += f"Community badge sheet for this event: [open the sheet]({meta['sheet']})\n\n"
    body += block(ev) + "\n"
    return "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + "---\n" + body

def main():
    update = "--update" in sys.argv
    made = refreshed = 0
    for ev, meta in EVENTS.items():
        path = os.path.join(ROOT, "badges", ev, "index.md")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(path):
            open(path, "w", encoding="utf-8").write(page(ev, meta)); made += 1; continue
        text = open(path, encoding="utf-8").read()
        # always refresh the front matter (nav order / exclusion depend on entry counts); keep the body
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
        if m:
            old = yaml.safe_load(m.group(1)) or {}
            new = front_matter(ev, meta)
            for k in old:
                if k not in new: new[k] = old[k]
            text = "---\n" + yaml.safe_dump(new, sort_keys=False, allow_unicode=True) + "---\n" + m.group(2)
            open(path, "w", encoding="utf-8").write(text); refreshed += 1
        if MARK_START not in text:
            text = text.rstrip("\n") + "\n\n" + block(ev) + "\n"
            open(path, "w", encoding="utf-8").write(text); refreshed += 1
        elif update:
            pre, rest = text.split(MARK_START, 1)
            _, post = rest.split(MARK_END, 1)
            open(path, "w", encoding="utf-8").write(pre + block(ev) + post); refreshed += 1
    print(f"event pages: created={made} refreshed={refreshed}")

if __name__ == "__main__":
    main()
