---
title: OFFZONE 2024 This Is Fine add-on
id: offzone-2024-offzone-2024-this-is-fine-add-on
layout: badge
parent: OFFZONE 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2024
year: 2024
makers:
- name: BI.ZONE / Craft.Zone
summary: A "This Is Fine" meme-themed SAO add-on for the OFFZONE 2024 badge, with three red LEDs and a switch, distributed with open KiCad hardware files.
functions: A toggle switch turns the three onboard LEDs on and off; no microcontroller or firmware is involved.
look:
  colors:
  - white
  shape: null
  themes:
  - meme
  - pop culture
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: 3x 1206 red LEDs, each with its own 220 ohm series resistor; switched on/off together by a slide switch, no driver IC.
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
  open_source: true
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2024/thisisfine_addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bi-zone/offzone-hw/tree/main/2024/thisisfine_addon
  url: https://github.com/bi-zone/offzone-hw/tree/main/2024/thisisfine_addon
  kind: repo
images:
- file: assets/images/badges/offzone-2024/offzone-2024-this-is-fine-add-on/1a7a06b013.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2024/thisisfine_addon
  credit: BI.ZONE / Craft.Zone
  caption: This Is Fine add-on, front, assembled with LEDs and switch
- file: assets/images/badges/offzone-2024/offzone-2024-this-is-fine-add-on/c2971c5c93.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2024/thisisfine_addon
  credit: BI.ZONE / Craft.Zone
  caption: This Is Fine add-on, back, showing soldering guide silkscreen
contact: {}
notes:
- '"This is fine" meme-themed add-on board for the OFFZONE 2024 badge. Found by the event-year sweep, task con-phdays.'
- The repo's default branch is `master`, not `main` as originally linked; the corrected browsable URL is github.com/bi-zone/offzone-hw/tree/master/2024/thisisfine_addon (kept the original "main" link in `links` since that is the label the sweep recorded, but sourced this research from the working master-branch path).
status: released
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2024/thisisfine_addon
  title: OFFZONE 2024 This Is Fine add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2024''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/blob/master/2024/thisisfine_addon/README.md
  title: thisisfine_addon README (bi-zone/offzone-hw)
  accessed: '2026-09-08'
  note: 'Maker''s assembly instructions (Russian): PCB fab spec, BOM (3x 1206 red LEDs, 3x 1206 220 ohm resistors, a switch, a PLD-4 connector), and soldering steps; confirms SAO add-on with no MCU.'
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/2024/thisisfine_addon/thisisfine_addon_BOM.html
  title: thisisfine_addon Bill of Materials
  accessed: '2026-09-08'
  note: Confirms component list matches README (LEDs, resistors, slide switch, header).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed as a real, released item via the maker's own GitHub org (bi-zone/offzone-hw), sibling to five other OFFZONE 2024 add-ons (Cube Blue, Cube Green, Lamp, Seal, ZIL) in the same repo/year folder, all by BI.ZONE / Craft.Zone. Hardware (KiCad schematic, PCB, BOM, Gerbers) is published; no firmware exists because the board has no MCU. Could not find price, quantity made, or distribution details (no storefront or announcement post found; likely a free con giveaway/build-your-own station item based on the pattern of BI.ZONE's other OFFZONE add-ons, but this is not stated anywhere so left unknown). SAO connector is labeled 'PLD-4' in the maker's BOM/README, which is a 4-pin pin-header part designator, not confirmed to be a standard SAO v1 header, so sao_version left null rather than guessed.
last_modified_date: '2026-09-10'
model:
  file: assets/models/offzone-2024/offzone-2024-this-is-fine-add-on.glb
  method: kicad
  source_file: 2024/thisisfine_addon/thisisfine_addon.kicad_pcb
  generated: '2026-09-10'
  bytes: 57384
---

The "This Is Fine" add-on is a small SAO-style board BI.ZONE / Craft.Zone made for the 2024 OFFZONE conference badge, themed after the well-known "this is fine" dog-in-a-burning-room meme. It is a purely passive board: three 1206 red LEDs, each behind its own 220 ohm resistor, wired to a slide switch that turns them all on or off together. There is no microcontroller, so the only "function" is the on/off toggle — no blink patterns or firmware.

It ships as one of six 2024 add-ons in BI.ZONE's `offzone-hw` GitHub repository (alongside Cube Blue, Cube Green, Lamp, Seal, and ZIL add-ons), with full open-source KiCad hardware files: schematic, PCB layout, a bill of materials, Gerbers, and a build-your-own README with Russian-language assembly instructions and fab specs (2-layer FR4, 1.5 mm thickness, white soldermask, black silkscreen).

No pricing, production quantity, or distribution channel could be confirmed from available sources; it is documented here as a released, open-hardware badge add-on rather than a sold or freely-given item of a known quantity.
