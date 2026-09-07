---
title: DEF CON 25 Retro Badge
id: dc25-retro-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: xres0nance
  url: https://hackaday.io/xres0nance
summary: 'A hand-built badge made entirely from authentic late-1980s/early-1990s components, with no microcontroller, built to fit DEF CON 25''s retro theme.'
functions: 'A diode-matrix logic circuit drives a seven-segment display salvaged from a Motorola MicroTAC cell phone, cycling through digits and indicator lights as a conversation piece rather than performing a game or CTF.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
tech:
  mcu: 'none'
  leds: null
  display: '7-segment (salvaged Motorola MicroTAC module)'
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: 'One-off personal project; not sold or distributed.'
make_your_own:
  open_source: yes
  hardware_url: https://hackaday.io/project/26256-def-con-25-retro-badge
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/26256-def-con-25-retro-badge
  url: https://hackaday.io/project/26256-def-con-25-retro-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260907113659/https://hackaday.io/project/26256-def-con-25-retro-badge
images:
- file: assets/images/badges/dc25/retro-badge/b6e0caa2c8.jpg
  source: "https://hackaday.io/project/26256-def-con-25-retro-badge"
  credit: "xres0nance"
  caption: "The DEF CON 25 Retro Badge, front view"
- file: assets/images/badges/dc25/retro-badge/97b2b39f33.jpg
  source: "https://hackaday.io/project/26256-def-con-25-retro-badge"
  credit: "xres0nance"
  caption: "Close-up of the seven-segment display module and perfboard construction"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/26256-def-con-25-retro-badge
  title: DEF CON 25 Retro Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''DEF CON 25''.'
  archived: https://web.archive.org/web/20260907113659/https://hackaday.io/project/26256-def-con-25-retro-badge
- kind: url
  url: https://hackaday.io/project/26256-def-con-25-retro-badge
  title: DEF CON 25 Retro Badge (project page detail)
  accessed: '2026-09-07'
  note: 'Confirmed maker (xres0nance), no-microcontroller design, discrete-logic parts (SN74HC595N shift register, 74F00N NAND gates, CD4066 analog switch, NE555P timer, 27x 1N4148 diodes), salvaged Motorola MicroTAC 7-segment display, KiCad files and schematic published on the page, and gallery images.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own Hackaday.io project page is the only source found; no press coverage, storefront, or social posts were located. Price and quantity are not stated anywhere on the page since it was a one-off build, not a distributed badge. Exact LED count on the salvaged display module is not specified by the maker.'
last_modified_date: '2026-09-07'
---

The DEF CON 25 Retro Badge is a one-off badge built by hacker xres0nance for DEF CON 25's 1980s/90s retro theme in 2017, under the tagline "Hack like it's 1989!" Rather than using a microcontroller, it is built entirely from discrete logic components of that era: a 74HC595 shift register, 74F00 NAND gates, a CD4066 analog switch, an NE555 timer, and a diode matrix of 27 1N4148 diodes, hand-soldered on perfboard.

Its centerpiece is a seven-segment display module salvaged from a Motorola MicroTAC cellular phone, showing green digits and indicator lights driven by the diode-matrix logic. The badge was built as a personal conversation-starter rather than a product — it was never sold, given away, or produced in quantity.

The maker published the full KiCad design files and a schematic on the Hackaday.io project page, making the design open source, though no firmware is applicable given the microcontroller-free design.
