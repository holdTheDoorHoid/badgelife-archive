---
title: '"fuck" note offensive SAO'
id: dc32-fuck-note-offensive-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: BigFuckingBadge
  url: https://hackaday.io/hexum064
summary: A pocket-sized SAO from BigFuckingBadge (maker hexum064) that lights up one of 13 profanity-laced phrases at a touch, built to be worn on a badge or on its own.
functions: It displays a lit up LED next to a phrase that starts with FUCK. You can select between 13 of them with a touch sensitive pad in the same of a meme guy. Includes SAO connector to solder on, and cr2032 clip, switch, and magnetic lapel stickon clip if the owner wants to wear it separately from a host badge. https://hackaday.io/project/194808-fuck-note-sao
look:
  colors: []
  shape: null
  themes:
  - meme
  - text
tech:
  mcu: ATtiny1616
  leds: null
  display: null
  connectivity: []
  battery: CR2032
  sao_version: null
get_one:
  price: ~$20
  price_usd: 20.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: sold only at the con
make_your_own:
  open_source: true
  hardware_url: https://github.com/BigFuckingBadge/fuck-sao
  firmware_url: https://github.com/BigFuckingBadge/fuck-sao
  eda_tool: KiCad
links:
- label: hackaday.io/project/194808-fuck-note-sao
  url: https://hackaday.io/project/194808-fuck-note-sao
  kind: hackaday
- label: github.com/BigFuckingBadge/fuck-sao
  url: https://github.com/BigFuckingBadge/fuck-sao
  kind: repo
images:
- file: assets/images/badges/dc32/fuck-note-offensive-sao/f10467c610.jpg
  source: https://github.com/BigFuckingBadge/fuck-sao
  credit: BigFuckingBadge
  caption: The fuck note SAO board
- file: assets/images/badges/dc32/fuck-note-offensive-sao/5b44deaf1c.jpg
  source: https://github.com/BigFuckingBadge/fuck-sao
  credit: BigFuckingBadge
  caption: Fuck note SAO prototype, lit up
contact:
  emails:
  - bfb.team.public@gmail.com
notes: []
status: released
sources:
- kind: sheet
  event: dc32
  row: 21
  updated: '2024-06-18'
- kind: url
  url: https://hackaday.io/project/194808-fuck-note-sao
  title: '"Fuck" note SAO - Hackaday.io'
  accessed: '2026-09-06'
  note: Maker (hexum064), concept, touch interface, mounting options, project status
- kind: url
  url: https://github.com/BigFuckingBadge/fuck-sao
  title: BigFuckingBadge/fuck-sao
  accessed: '2026-09-06'
  note: Open KiCad hardware source, gerbers, BOM, and photos; folder names (fuck-sao-t416.X, fuck-sao-touch-t1616.X) show the MCU moved from an ATtiny416 prototype to an ATtiny1616 in the touch-based final revision
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Hardware and firmware are open source on GitHub (KiCad files, gerbers, BOM). Could not confirm LED type/count, exact price paid, or quantity made from the sources read; get_one.price/price_usd carry the sheet's original estimate rather than a maker-confirmed figure. Hackaday project log entries were not individually reachable to pin down a full build history beyond the v1 (button, ATtiny416) to v3 (touch, ATtiny1616) progression visible in the repo's folder names.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc32/fuck-note-offensive-sao.glb
  method: kicad
  source_file: fuck-sao.kicad_pcb
  generated: '2026-09-07'
  bytes: 116972
---

The "fuck" note SAO is a small add-on board from BigFuckingBadge (Hackaday handle hexum064) sold at DEF CON 32. A touch pad shaped like a meme figure lets the wearer cycle through 13 short phrases, each beginning with "FUCK," lighting an LED next to the selected line. It ships with an SAO connector for plugging into a host badge, plus a CR2032 battery clip, a power switch, and a magnetic lapel clip so it can also be worn as a standalone pin independent of any badge.

The project went through several revisions visible in its GitHub repository: an early button-driven prototype built around an ATtiny416, and a later touch-based version on an ATtiny1616 that the maker's Hackaday log and repo folder names identify as the final ("v3.0") build. All KiCad schematics, PCB layout, gerbers, and a bill of materials are published openly, along with build photos and a demo video, making the design fully reproducible.

Pricing and exact production numbers were not confirmed by any source read for this entry; the badge sheet's estimate of roughly $20, sold only at the convention, is carried over unverified.
