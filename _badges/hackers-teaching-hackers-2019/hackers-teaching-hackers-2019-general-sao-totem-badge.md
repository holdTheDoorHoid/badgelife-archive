---
title: Hackers Teaching Hackers 2019 General (SAO Totem) Badge
id: hackers-teaching-hackers-2019-hackers-teaching-hackers-2019-general-sao-totem-badge
layout: badge
parent: Hackers Teaching Hackers 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hackers-teaching-hackers-2019
year: 2019
makers:
- name: mcm3nac3
summary: The general-attendee badge for Hackers Teaching Hackers (HTH) 2019, built as an "SAO Totem" that hosts up to four Shitty Add-Ons at once.
functions: Acts as a passive hub for SAOs; no onboard game or CTF of its own beyond powering and displaying attached add-ons.
look:
  colors: []
  shape: null
  themes:
  - village badge
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: v1
  sao_ports: 4
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/syn-ack-zack/HTH-General-Badge
  firmware_url: null
  eda_tool: KiCad
  license: GPL-3.0
  notes: Repo includes KiCad source, gerbers, and a BOM (hth-gen-bom.csv) with a linked DigiKey cart. README notes a trace error around the power switch requiring a manual bridge of the middle pins.
links:
- label: github.com/HTHackers/HTH-General-Badge
  url: https://github.com/HTHackers/HTH-General-Badge
  kind: repo
- label: github.com/syn-ack-zack/HTH-General-Badge
  url: https://github.com/syn-ack-zack/HTH-General-Badge
  kind: repo
images:
- file: assets/images/badges/hackers-teaching-hackers-2019/hackers-teaching-hackers-2019-general-sao-totem-badge/cff32d89b5.jpg
  source: https://github.com/syn-ack-zack/HTH-General-Badge
  credit: mcm3nac3
  caption: Assembled HTH General 2019 badge with SAO totem headers
contact: {}
notes:
- The general-attendee badge for HTH 2019, a USB/battery-powered SAO 'Totem' board that hosts up to four add-ons. Found by the event-year sweep, task con-blue-team-con.
- Sweep title read as "HTH-General-Badge" (the repo name); the maker's own README calls it "The general attendee badge for Hackers Teaching Hackers 2019," here shortened to "HTH General (SAO Totem) Badge."
status: listed
sources:
- kind: url
  url: https://github.com/HTHackers/HTH-General-Badge
  title: Hackers Teaching Hackers 2019 General (SAO Totem) Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-blue-team-con); event read as ''Hackers Teaching Hackers 2019''.'
- kind: url
  url: https://github.com/syn-ack-zack/HTH-General-Badge
  title: HTH-General-Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run4-spotted); event read as ''other''.'
- kind: url
  url: https://github.com/syn-ack-zack/HTH-General-Badge
  title: syn-ack-zack/HTH-General-Badge - GitHub
  accessed: '2026-09-08'
  note: 'README and repo contents: identifies badge as the HTH 2019 general attendee badge with 4 SAO ports, GPL-3.0, KiCad + gerber + BOM files, and a known switch-trace bug.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own GitHub repo (syn-ack-zack/HTH-General-Badge): README, KiCad source, gerbers, and BOM all check out. No pricing, quantity, or distribution details found anywhere -- no press coverage or storefront listing turned up in search. Merged with duplicate entry ''HTH General (SAO Totem) Badge'' (hackers-teaching-hackers-2019-hth-general-badge).'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/hackers-teaching-hackers-2019/hth-general-badge/
---


## Notes merged from the duplicate entry "HTH General (SAO Totem) Badge"

The HTH General Badge is the general-attendee badge given out at Hackers Teaching Hackers (HTH) 2019 in Columbus, Ohio. Rather than carrying its own game or display, it is built as an "SAO Totem" -- a passive board with four Shitty Add-On headers so an attendee could plug in and power up to four add-ons at once, switchable between USB and battery power.

The design, credited to mcm3nac3 for the art and PCB layout, is fully open source under GPL-3.0: the GitHub repository includes the KiCad project files, gerbers ready for fabrication, and a bill of materials with a linked DigiKey cart. The README flags one known hardware bug -- a bad trace around the power switch that needs a manual jumper across the switch's middle pins to work correctly.

No pricing, production quantity, or distribution details were found; the only source located was the project's own GitHub repository, with no press coverage or storefront turning up in search.
