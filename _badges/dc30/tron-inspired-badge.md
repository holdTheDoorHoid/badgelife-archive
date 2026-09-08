---
title: Tron-inspired Badge
id: dc30-tron-inspired-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: Ironwood Cyber
  url: https://github.com/Ironwood-Cyber
summary: A round Tron-themed badge Ironwood Cyber gave away free at DEF CON 30, a two-board LED-ring design the maker calls the "Tron Disc."
functions: Lights 70 addressable LEDs arranged in two concentric rings; the front board is a capacitive touch interface for the rear board's electronics.
look:
  colors:
  - black
  - teal
  shape: circle
  themes:
  - tron
  - sci-fi
tech:
  mcu: ESP-series (exact part not stated)
  leds:
    count: 70
    type: RGB
    note: Two concentric rings (inner and outer), diffused through 3D-printed material between the two boards.
  display: null
  connectivity: []
  battery: LiPo, rechargeable
  sao_version: null
get_one:
  price: Free
  price_usd: 0.0
  quantity: 'about 80 (per the maker)'
  availability: free
  distribution:
  - raffle
  - free_drop
  where: Given away over several weeks via Twitter/LinkedIn raffles plus unannounced in-person drops during DEF CON 30; pickup only, not shipped.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Ironwood-Cyber/dc30-badge-hw
  firmware_url: null
  eda_tool: KiCad
links:
- label: ironwoodcyber.com
  url: https://ironwoodcyber.com/
  kind: website
- label: Ironwood Cyber - About (Tron Badge history)
  url: https://www.ironwoodcyber.com/about
  kind: website
- label: Schematics repo (Ironwood-Cyber/dc30-badge-hw)
  url: https://github.com/Ironwood-Cyber/dc30-badge-hw
  kind: repo
images: []
contact: {}
notes:
- Unofficial Tron-themed DEF CON 30 badge by Ironwood Cyber, listed in Tindie's DC30 unofficial-badges roundup. Found by the event-year sweep, task general-2020.
- 'This entry duplicates dc30-ironwood-cyber-tron-badge, which already carries fuller research (maker team credits, Reddit/Twitter sourcing, two saved photos). Left unmerged per research-guide instructions; see that entry for the maker''s own name for it, "Tron Disc."'
status: released
sources:
- kind: url
  url: https://ironwoodcyber.com/
  title: Tron-inspired Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2020); event read as ''DEF CON 30 2022''.'
- kind: url
  url: https://www.ironwoodcyber.com/about
  title: About Ironwood Cyber
  accessed: '2026-09-08'
  note: Confirms "2022 DEF CON 30 badge debut" - the Tron Badge was Ironwood Cyber's first custom hardware badge, launched at DEF CON 30.
- kind: url
  url: https://github.com/Ironwood-Cyber/dc30-badge-hw
  title: 'Ironwood-Cyber/dc30-badge-hw: Tron badge hardware schematics'
  accessed: '2026-09-08'
  note: 'README/repo describes the badge: two PCBs joined by 3D-printed diffusion material, a touch-input front board, 70 addressable LEDs in two rings, rechargeable LiPo circuit, KiCad schematics. Repo description itself says "Defcon 29 Kicad Schematics", a discrepancy also flagged on the duplicate entry.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, distributed item (not just a search snippet) via the maker''s own about page and GitHub repo. Exact MCU part number, firmware source, and price/quantity beyond the maker''s own round estimate could not be found from these sources; fuller sourcing (Reddit, Twitter reveal posts, photos) already lives on the duplicate entry dc30-ironwood-cyber-tron-badge, which this was not merged into per instructions.'
last_modified_date: '2026-09-08'
---

Ironwood Cyber, a Fort Worth, Texas cybersecurity startup, brought this round Tron-themed badge to DEF CON 30 in 2022 as its first piece of custom hardware, giving it away for free rather than selling it. The badge is a two-PCB assembly - a front board with a capacitive-touch interface and a rear board carrying the electronics - joined by 3D-printed diffusion material that spreads light from 70 addressable RGB LEDs arranged in two concentric rings.

Roughly 80 units were made and distributed over several weeks through social-media raffles and a handful of unannounced in-person drops during the conference, with pickup only and no shipping. The hardware schematics (KiCad) are published on GitHub, though no firmware source or bill of materials has been released.

## Make your own

Hardware schematics (KiCad) are available in the [dc30-badge-hw repository](https://github.com/Ironwood-Cyber/dc30-badge-hw), which documents the two-board LED-ring design and its LiPo/USB circuitry. No firmware source or Gerber files have been published alongside it.
