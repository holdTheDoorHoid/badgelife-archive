---
title: OFFZONE 2025 Anonymous add-on
id: offzone-2025-offzone-2025-anonymous-add-on
layout: badge
parent: OFFZONE 2025
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2025
year: 2025
makers:
- name: BI.ZONE / Craft.Zone
summary: A small self-solder SAO shaped like an Anonymous (Guy Fawkes) mask, made as one of the OFFZONE 2025 badge add-ons.
functions: 'No electronics beyond the three LEDs and their current-limiting resistors: it lights up when plugged into a badge that powers its SAO header. No microcontroller, no animation logic.'
look:
  colors:
  - white
  - black
  shape: mask
  themes:
  - security
  - privacy
  - pop culture
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: 3x red 1206 LEDs, each in series with a 220 ohm 1206 resistor; no driver IC.
  display: none
  connectivity: []
  battery: null
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2025/anonymous_addon
  firmware_url: null
  eda_tool: KiCad
  notes: KiCad project, Gerbers, and BOM are published; there is no firmware because the board has no MCU.
links:
- label: github.com/bi-zone/offzone-hw/tree/main/2025/anonymous_addon
  url: https://github.com/bi-zone/offzone-hw/tree/main/2025/anonymous_addon
  kind: repo
- label: github.com/bi-zone/offzone-hw/tree/master/2025/anonymous_addon
  url: https://github.com/bi-zone/offzone-hw/tree/master/2025/anonymous_addon
  kind: repo
  note: Working link; the repo default branch is master, not main.
images:
- file: assets/images/badges/offzone-2025/offzone-2025-anonymous-add-on/ee00291060.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2025/anonymous_addon
  credit: BI.ZONE / Craft.Zone
  caption: Front of the assembled Anonymous add-on SAO, showing the mask silhouette and three red LEDs
- file: assets/images/badges/offzone-2025/offzone-2025-anonymous-add-on/830c92c315.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2025/anonymous_addon
  credit: BI.ZONE / Craft.Zone
  caption: Back of the Anonymous add-on board with the 6-pin SAO connector
notes:
- Anonymous-mask-themed add-on board for the OFFZONE 2025 badge. Found by the event-year sweep, task con-phdays.
contact: {}
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2025/anonymous_addon
  title: OFFZONE 2025 Anonymous add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2025''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/master/2025/anonymous_addon
  title: 'offzone-hw: 2025/anonymous_addon (README, BOM, KiCad files)'
  accessed: '2026-09-08'
  note: Confirmed the item exists; original main-branch link 404s because the repo default branch is master. README (Russian) gives PCB spec, BOM, and assembly instructions.
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/2025/anonymous_addon/README.md
  title: anonymous_addon README.md
  accessed: '2026-09-08'
  note: PCB fab spec (2-layer FR4, 1.5mm, white soldermask, black silkscreen), BOM (3x red 1206 LED, 3x 220 ohm 1206 resistor, PLD-6 connector), and solder assembly steps.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Only source is the maker''s own GitHub repo (design files + README); no press coverage, storefront, or photo of it in use at the event was found, so price/quantity/availability are unknown. The README is in Russian; translated for this entry. The PLD-6 connector matches a 6-pin SAO header, hence sao_version: v2. Title matches the sweep''s wording; no correction needed.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/offzone-2025/offzone-2025-anonymous-add-on.glb
  method: kicad
  source_file: 2025/anonymous_addon/anonymous_addon.kicad_pcb
  generated: '2026-09-10'
  bytes: 45888
---

The Anonymous add-on is one of a set of small SAOs BI.ZONE and Craft.Zone designed for the OFFZONE 2025 conference badge, alongside companion add-ons shaped like a bear, a boombox, a terminal, and an angel-and-devil pair. It is a passive board with no microcontroller: three red 1206 LEDs, each behind its own 220 ohm current-limiting resistor, wired straight to a 6-pin SAO connector, so it simply lights up when seated on a badge that supplies power through its SAO header.

The board is sold/distributed as a self-solder kit rather than pre-assembled: the repository's README walks through soldering the resistors (no polarity), then the LEDs lens-down with their polarity arrows all pointing the same direction, then the connector. The hardware is openly published as a KiCad project (schematic, PCB, BOM, and Gerbers); there is no firmware repository because the board has no programmable chip.

No press write-up, storefront listing, or in-the-wild photo turned up beyond the maker's own repository, so price, production quantity, and how it was distributed at OFFZONE 2025 (e.g. included with badge registration vs. a separate give-away) remain unknown.
