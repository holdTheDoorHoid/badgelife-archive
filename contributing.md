---
title: Contributing
layout: default
nav_order: 10
---

# Contributing

The archive lives in a public GitHub repository: [{{ site.gh_edit_repository | replace: "https://github.com/", "" }}]({{ site.gh_edit_repository }}). Everything on the site is generated from plain text files there, so any fix is a small edit.

## The easy ways

- **Report a mistake or add details:** every entry has an "Open an issue" link at the bottom that pre-fills the entry name. Tell us what is wrong or what you know, with a link if you have one.
- **Send photos or files:** attach them to an issue, or point us at where they live. Say who took the photo so it can be credited.
- **Ask for a removal:** see [Photos, links and takedowns]({{ site.baseurl }}/about/#photos-links-and-takedowns).

## Editing an entry directly

Each badge or SAO is one file at `_badges/<event>/<slug>.md`. Click "Edit this page on GitHub" at the bottom of any entry, change the text, and GitHub will walk you through opening a pull request. The file has two parts:

1. A block of fields between `---` lines (the "front matter"). This is what the search filters read.
2. Free-form text below it, which becomes the body of the page.

Every field is optional. Leave a field empty rather than guessing; the site hides empty fields.

## Entry fields

| Field | What goes there |
|:--|:--|
| `title` | The badge or SAO's name. |
| `type` | `badge`, `sao`, `minibadge`, `kit`, `accessory`, `other` or `unknown`. |
| `event` | An id from `_data/events.yml`, for example `dc31` or `supercon-2024`. Add the event there first if it is missing. |
| `year` | Year of the event. |
| `makers` | A list of `name`, optional `url` and `role`. |
| `summary` | One or two plain sentences about what it is. |
| `functions` | What it does, in the maker's words if possible. |
| `look` | `colors`, `shape`, `themes` (a list of tags such as `skull`, `retro computer`, `food`), `size_mm`, `finish`, `form_factor`. |
| `tech` | `mcu`, `leds` (`count`, `type`), `display`, `connectivity` (list: `wifi`, `ble`, `lora`, `ir`, `nfc`…), `inputs`, `power`, `battery`, `sao_version` (`v1`, `v1.69bis`, `v2`, `none`), `sao_ports`, `other`. |
| `get_one` | `price`, `price_usd`, `quantity`, `availability` (`available`, `sold_out`, `free`, `not_released`, `cancelled`, `rumored`, `limited`, `unknown`), `distribution` (list: `purchase`, `free_drop`, `contest`, `village`, `kit`, `crowdfunding`), `where`. |
| `make_your_own` | `open_source` (`yes`, `no`, `partial`), `license`, `hardware_url`, `firmware_url`, `gerbers`/`gerbers_url`, `bom`/`bom_url`, `eda_tool`, `fab_url`, `notes`. |
| `links` | A list of `label`, `url`, `kind` (`repo`, `hackaday`, `store`, `social`, `video`, `article`, `doc`, `website`) and optional `archived` (a Wayback Machine URL). |
| `images` | A list of `file` (path under `assets/images/badges/<event>/<slug>/`), `source`, `credit`, `caption`. |
| `contact` | `discord`, `handles`, `emails` — only what the maker has published themselves. |
| `sources` | Where the information came from: `kind: sheet` with `event` and `row`, or `kind: url` with `url`, `title`, `accessed`. |
| `research` | `status` (`stub`, `researched`, `verified`), `confidence`, `last_checked`, `notes`. |

**`model`** (generated, do not hand-edit): `file` (the `.glb` under `assets/models/`), `method` (`kicad` or `gerber`),
`source_file`, `generated`, `bytes`, `size_mm`. Produced by `scripts/fetch_hardware.py` followed by
`scripts/build_models.py`; delete the block and the file to remove a model.

## Adding a new entry

Copy an existing entry file in the same event folder, rename it to a short slug, and fill in what you know. The file name becomes the page address. Then run, from the repository root:

```bash
python3 scripts/build_index.py
```

It validates every entry and regenerates the search index. The GitHub build does the same, so a pull request with a broken entry will fail with a message saying which field is wrong.

## Adding a whole event

Add the event to `_data/events.yml` (id, name, year, family, dates, location), then run `python3 scripts/gen_event_pages.py` to create its listing page.

## Bulk import from a badge sheet

`scripts/normalize_sheets.py` turns the yearly Google Sheets (exported as CSV into `data/sheets/`) into stub records, and `scripts/gen_entries.py` turns those into entry files without touching entries that have already been researched.
