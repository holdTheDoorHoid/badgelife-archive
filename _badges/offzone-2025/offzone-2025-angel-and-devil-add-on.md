---
title: OFFZONE 2025 Angel and Devil add-on
id: offzone-2025-offzone-2025-angel-and-devil-add-on
layout: badge
parent: OFFZONE 2025
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2025
year: 2025
makers:
- name: BI.ZONE / Craft.Zone
summary: A small passive SAO add-on for the OFFZONE 2025 badge, styled as an angel and a devil, that lights red and white LEDs.
functions: 'No microcontroller or interactivity: two BC807-25 transistors drive two white and two red 1206 LEDs in a simple analog blinking/flashing circuit, powered off the host badge''s SAO connector.'
look:
  colors:
  - white
  - red
  shape: null
  themes:
  - fantasy
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: 2x white and 2x red 1206 LEDs, driven by 2x BC807-25 transistors (analog, no MCU)
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2025/angelanddevil_addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bi-zone/offzone-hw/tree/main/2025/angelanddevil_addon
  url: https://github.com/bi-zone/offzone-hw/tree/main/2025/angelanddevil_addon
  kind: repo
- label: 2025.offzone.moscow/badge-and-offcoins
  url: https://2025.offzone.moscow/badge-and-offcoins/
  kind: website
images:
  - file: assets/images/badges/offzone-2025/offzone-2025-angel-and-devil-add-on/0265a86183.jpg
    source: "https://github.com/bi-zone/offzone-hw/tree/master/2025/angelanddevil_addon"
    credit: "BI.ZONE / Craft.Zone"
    caption: "Angel-and-devil add-on board, front"
  - file: assets/images/badges/offzone-2025/offzone-2025-angel-and-devil-add-on/5a7b84ad56.jpg
    source: "https://github.com/bi-zone/offzone-hw/tree/master/2025/angelanddevil_addon"
    credit: "BI.ZONE / Craft.Zone"
    caption: "Angel-and-devil add-on board, back"
contact: {}
notes:
- Angel-and-devil-themed add-on board for the OFFZONE 2025 badge. Found by the event-year sweep, task con-phdays.
status: listed
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2025/angelanddevil_addon
  title: OFFZONE 2025 Angel and Devil add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2025''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/master/2025/angelanddevil_addon
  title: angelanddevil_addon README and KiCad files
  accessed: '2026-09-08'
  note: 'Confirmed the repo''s default branch is master (not main, which 404s); README describes parts list, assembly steps, and links front/back photos; KiCad schematic/PCB/gerbers/BOM present.'
- kind: url
  url: https://2025.offzone.moscow/badge-and-offcoins/
  title: OFFZONE 2025 badge and offcoins page
  accessed: '2026-09-08'
  note: 'Describes the 2025 main badge and its SAO add-on slots in general (new connector, backward compatible with prior years'' add-ons, distributed via activities/Craft.Zone); does not mention this add-on by name, price, or quantity.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, open-source SAO from BI.ZONE/Craft.Zone''s own offzone-hw repo (2025/angelanddevil_addon), with README, KiCad source, gerbers, BOM, and front/back photos. It is a passive add-on: no MCU, just two transistors switching four LEDs (2 white, 2 red) in an angel/devil motif, connecting via a PLD-6 header to the badge''s SAO port. Could not find price, quantity made, or distribution method (free drop vs. earned via offcoins) on the event''s badge page, which discusses add-ons generically but does not name this one specifically; left those fields empty. The existing repo link in the entry (branch "main") 404s; the repo''s actual default branch is "master". Kept the original link as-is per instructions and added a working master-branch link as an additional source.'
last_modified_date: '2026-09-08'
---

The Angel and Devil add-on is a small SAO-style accessory built by BI.ZONE / Craft.Zone for the OFFZONE 2025 conference badge, part of a set of themed add-ons released alongside that year's main badge (others in the same 2025 batch include Bear, Boombox, Terminal, and Anonymous add-ons). It has no microcontroller: two BC807-25 transistors switch two white and two red 1206 LEDs, arranged so the board reads as a tiny angel-and-devil pairing, with power drawn straight from the host badge over a PLD-6 connector.

The hardware is fully open source. BI.ZONE published the KiCad schematic, PCB layout, project file, gerbers, and an HTML bill of materials in their `offzone-hw` GitHub repository, along with a short assembly guide covering resistor values, LED orientation, and solder order for anyone who wants to build their own copy. The board is a standard 2-layer FR4 PCB with white soldermask, black silkscreen, and HASL finish.

Specifics on how it was distributed at the conference -- price, quantity produced, or whether it was a free drop versus something earned through the event's "offcoins" activity system -- were not found on the event's own badge page or elsewhere; those fields are left blank pending better sourcing.
