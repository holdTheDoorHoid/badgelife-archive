---
title: BSides SD 2020 Badge
id: bsides-san-diego-2020-bsides-sd-2020-badge
layout: badge
parent: BSides San Diego 2020
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-san-diego-2020
year: 2020
makers:
- name: S. Hollingsworth (community contributor)
summary: An Arduino Trinket M0-based electronic badge used at BSides San Diego 2020, customized with community-written CircuitPython LED animation routines.
functions: Runs custom CircuitPython LED "badge bling" animation routines on the Trinket M0 board.
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: Trinket M0
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/shollingsworth/bsides-sd-2020-badge-hacking
  eda_tool: null
links:
- label: github.com/shollingsworth/bsides-sd-2020-badge-hacking
  url: https://github.com/shollingsworth/bsides-sd-2020-badge-hacking
  kind: repo
images: []
contact: {}
notes:
- Confirmed via the repo itself (README, single commits history). The repo is firmware only (a code.py of custom LED routines for the Trinket M0 badge) written by GitHub user "shollingsworth"; no hardware files, photos, maker/vendor name, price, or quantity were found anywhere. It is unclear whether "shollingsworth" designed the physical badge or just wrote bling routines for a badge distributed at the con, so the maker is listed as a community contributor rather than confirmed designer.
- A separate, apparently unrelated repo (ellwoodthewood/BSidesSD, "Badge Project for BSides San Diego") also exists and may describe the same or a different year's badge; not pursued further per scope (one entry per task) — reported separately.
status: released
sources:
- kind: url
  url: https://github.com/shollingsworth/bsides-sd-2020-badge-hacking
  title: BSides SD 2020 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2020); event read as ''BSides San Diego 2020''.'
- kind: url
  url: https://github.com/shollingsworth/bsides-sd-2020-badge-hacking/blob/master/README.md
  title: 'bsides-sd-2020-badge-hacking README'
  accessed: '2026-09-10'
  note: Confirms Arduino Trinket M0 clone hardware, CircuitPython >=5.0.0 requirement, and that the code is custom "badge bling" LED routines for BSides SD 2020.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: Fact-check pass (2026-09-10) re-fetched both cited sources (repo root and README) and confirmed every populated field and body sentence against them (Trinket M0 clone, CircuitPython >=5.0.0, "badge bling" LED routines, firmware-only with no hardware files/photos/price/quantity, event id, GPL-3.0-licensed repo with 4 commits). No contradictions found; nothing to correct. The only source remains a small firmware-only GitHub repo, so LED count/type, display, connectivity, colors, and shape genuinely could not be determined and are left empty.
last_modified_date: '2026-09-10'
---

At BSides San Diego 2020, attendees carried an electronic badge built around an Arduino Trinket M0 (or compatible clone) board. GitHub user "shollingsworth" published a small CircuitPython project, `bsides-sd-2020-badge-hacking`, containing a `code.py` with a handful of borrowed and custom LED animation routines — described by the author as "badge bling" — meant to be copied onto the badge's Trinket M0 to change its lighting behavior.

No hardware design files, official vendor or organizer credit, photos, price, or production quantity could be found for the badge itself; the repository is firmware-only and the author's role (designer of the physical badge versus an attendee who wrote extra animations for it) is not stated anywhere in the source.

## Make your own

Copy `code.py` from the [GitHub repo](https://github.com/shollingsworth/bsides-sd-2020-badge-hacking) onto the root of an Arduino Trinket M0 (or clone) running CircuitPython 5.0.0 or later.
