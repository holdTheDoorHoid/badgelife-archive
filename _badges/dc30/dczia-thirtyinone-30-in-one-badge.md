---
title: DCZia thirtyinone (30-in-One Badge)
id: dc30-dczia-thirtyinone-30-in-one-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc30
year: 2022
makers:
- name: DCZia
  url: https://dczia.net
summary: A "learn electronics" kit on a single PCB, built and sold as a wearable badge for DEF CON 30. Duplicate of the archive's existing entry for the same badge (see notes).
functions: 'End users solder up to 30 different described circuits onto one board (OLED display, RGB LED, speaker, switches, potentiometer, transformer), using it as a jumping-off point to explore analog electronics; the board includes hidden challenges/puzzles and ships with a printed instruction booklet and a wooden box that doubles as a soldering jig.'
look:
  colors: []
  shape: rectangle
  themes: [learn to solder, kit, electronics]
tech:
  mcu: none
  leds:
    count: 1
    type: RGB
    note: Single RGB LED among the 30 circuits; no microcontroller is used (a passive/analog electronics kit).
  display: 0.96" OLED
  connectivity: []
  battery: not specified (has a battery case)
  sao_version: none
get_one:
  price: $100
  price_usd: 100.0
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing shows "Out of Stock" (since February 2024) as of 2026-09-07.
  distribution: [purchase]
  where: Sold via Tindie (seller "hamster" / snurkle engineering, Sandy, UT).
make_your_own:
  open_source: yes
  hardware_url: https://github.com/dczia/thirtyinone
  firmware_url: null
  eda_tool: null
  gerbers_url: null
  bom_url: null
  license: Unlicense
  fab_url: null
  notes: OSHWA certified (UID US002134). Repo includes Hardware and Software folders plus the printed booklet (PDF and source).
links:
- label: github.com/dczia/thirtyinone
  url: https://github.com/dczia/thirtyinone
  kind: repo
- label: www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge
  url: https://www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge/
  kind: store
- label: DC Zia 30-in-One Badge (Hackaday.io)
  url: https://hackaday.io/project/188464-dc-zia-30-in-one-badge
  kind: hackaday
- label: "Nostalgic 30-in-ONE Electronics Badge For DEF CON 30 (Hackaday)"
  url: https://hackaday.com/2022/12/09/nostalgic-30-in-one-electronics-badge-for-def-con-30/
  kind: article
- label: DCZia
  url: https://dczia.net
  kind: website
- label: "DCZia 30 in 1 Electronic Project Kit Badge Overview (YouTube)"
  url: https://www.youtube.com/watch?v=AAD9OO9EeQw
  kind: video
images:
- file: assets/images/badges/dc30/dczia-thirtyinone-30-in-one-badge/1679846ba4.jpg
  source: "https://www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge/"
  credit: "snurkle engineering / DCZia"
  caption: "The DCZia 30-in-One badge kit with wooden box, OLED, and through-hole components"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/dczia/thirtyinone
  title: DCZia thirtyinone (30-in-One Badge)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 30''.'
- kind: url
  url: https://github.com/dczia/thirtyinone
  title: dczia/thirtyinone - GitHub
  accessed: '2026-09-07'
  note: "README (assembly order: OLED, RGB LED, speaker, switches, battery case, transformer, potentiometer, key cap), repo file listing (Hardware/ with BOM.xlsx, badge and circuits subfolders; booklet PDF and source zip), Unlicense confirmed via GitHub API."
- kind: url
  url: https://www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge/
  title: DCZia '30-in-One' defcon 30 Badge - Tindie
  accessed: '2026-09-07'
  note: Price ($100), seller (snurkle engineering, Sandy, UT), out-of-stock status (since Feb 2024), product photo, OSHWA mention.
- kind: url
  url: https://hackaday.io/project/188464-dc-zia-30-in-one-badge
  title: DC Zia 30-in-One Badge - Hackaday.io
  accessed: '2026-09-07'
  note: Component list (OLED, key switch/cap, slide switches, potentiometer, speaker, CdS light sensor, NPN transistor), wooden box with lanyard, OSHWA-certified open source hardware.
- kind: url
  url: https://hackaday.com/2022/12/09/nostalgic-30-in-one-electronics-badge-for-def-con-30/
  title: Nostalgic 30-in-ONE Electronics Badge For DEF CON 30 - Hackaday
  accessed: '2026-09-07'
  note: Context that the badge is a throwback to vintage "100-in-1" Radio Shack style electronics kits; component list confirmed (resistors, capacitors, LEDs, transistors, switches, transformer, speaker, OLED, battery box, jumper wires).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: This entry duplicates an already-researched entry for the same badge, _badges/dc30/30-in-1-badge.md (id dc30-30-in-1-badge), which was created from the community sheet and carries a fuller source list (including its OSHWA certification page and dczia.net). Facts here match that entry. Maker name confirmed as "DCZia" (not "dczia" the lowercase repo org name). No microcontroller is used (a passive/analog kit); quantity made and exact battery spec are not stated in any source found.
last_modified_date: '2026-09-07'
---

The thirtyinone (30-in-One) Badge is a "learn electronics" kit built by DCZia and sold as a badge for DEF CON 30 (2022) through Tindie under seller "snurkle engineering." Rather than running firmware on a microcontroller, it is a single PCB carrying 30 separate analog circuit projects — an OLED screen, an RGB LED, a speaker, switches, a potentiometer, and a transformer among them — that the owner solders together themselves, following a printed instruction booklet. A wooden box doubles as a soldering jig, and the board reportedly hides some challenges/puzzles for people who go looking. It sold for $100 and has since gone out of stock on Tindie.

The project is OSHWA-certified (UID US002134) and fully open source under the Unlicense, with hardware and software design files, the booklet, and its source available in DCZia's `thirtyinone` GitHub repository.

This entry is a duplicate of the archive's existing `30-in-1-badge` entry for the same DC30 badge; see that entry (id `dc30-30-in-1-badge`) for the canonical record.
