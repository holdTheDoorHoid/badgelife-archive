---
title: OFFZONE 2024 Cube Green add-on
id: offzone-2024-offzone-2024-cube-green-add-on
layout: badge
parent: OFFZONE 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2024
year: 2024
makers:
- name: BI.ZONE / Craft.Zone
summary: A small green-solder-mask SAO add-on shaped as a cube, one of several add-on designs made for OFFZONE 2024.
functions: Three green LEDs light up; no other interactive functions documented.
look:
  colors:
  - green
  - black
  shape: null
  themes:
  - minimalist
tech:
  mcu: none
  leds:
    count: 3
    type: '1206'
    note: Three 1206 green LEDs plus one 1206 100-ohm resistor; no microcontroller.
  display: none
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
  open_source: true
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/main/2024/cube_green_addon
  firmware_url: null
  eda_tool: KiCad
  gerbers_url: https://github.com/bi-zone/offzone-hw/tree/master/2024/cube_green_addon/cube_green_addon_gbr
  bom_url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/2024/cube_green_addon/cube_green_addon_BOM.html
  notes: 'Repo includes KiCad schematic/PCB/project files, a BOM, and Gerbers. Fab spec from the README: 2-layer FR4, 1.5mm thick board, 18 or 35 micron copper, HASL finish, green soldermask, black silkscreen.'
links:
- label: github.com/bi-zone/offzone-hw/tree/main/2024/cube_green_addon
  url: https://github.com/bi-zone/offzone-hw/tree/main/2024/cube_green_addon
  kind: repo
images:
- file: assets/images/badges/offzone-2024/offzone-2024-cube-green-add-on/1375d63381.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/main/2024/cube_green_addon
  credit: BI.ZONE / Craft.Zone
  caption: Cube Green add-on, front
- file: assets/images/badges/offzone-2024/offzone-2024-cube-green-add-on/cb017f6952.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/main/2024/cube_green_addon
  credit: BI.ZONE / Craft.Zone
  caption: Cube Green add-on, back
contact: {}
notes:
- Green-cube-themed add-on board for the OFFZONE 2024 badge. Found by the event-year sweep, task con-phdays.
status: released
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2024/cube_green_addon
  title: OFFZONE 2024 Cube Green add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2024''.'
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/2024/cube_green_addon/README.md
  title: cube_green_addon README
  accessed: '2026-09-08'
  note: 'Maker README: fab spec (2-layer FR4, green soldermask, black silkscreen), BOM (3x 1206 green LEDs, 1x 1206 100-ohm resistor, PLD-4 connector), assembly instructions, and front/back photo links.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed via the maker's own GitHub repo (bi-zone/offzone-hw), which is the primary and only source found. No press coverage, storefront, price, quantity, or distribution details turned up in a couple of targeted searches, so those fields are left empty. The board carries no MCU; it is a passive SAO with three LEDs wired through a single resistor, powered/lit presumably by the host badge's SAO header (exact SAO pinout/version not stated in the repo). One of at least six 2024 OFFZONE add-ons (Cube Blue, Lamp, Seal, This Is Fine, ZIL are the sibling entries already in the archive).
last_modified_date: '2026-09-10'
model:
  file: assets/models/offzone-2024/offzone-2024-cube-green-add-on.glb
  method: gerber
  source_file: 2024/cube_green_addon/cube_green_addon_gbr
  generated: '2026-09-10'
  bytes: 128872
  size_mm:
  - 40.5
  - 38.5
---

The Cube Green add-on is one of a set of small SAO-style add-ons that BI.ZONE and Craft.Zone produced for OFFZONE 2024, sold or distributed alongside the main conference badge. It is a simple, passive PCB accessory shaped like a cube: a 2-layer FR4 board with green soldermask and black silkscreen, populated with three 1206-package green LEDs run through a single 100-ohm resistor and connected to the host badge through a PLD-4 connector. There is no microcontroller, display, or onboard power — the LEDs simply light when connected to a powered SAO header.

The design is fully open: the maker's GitHub repository (bi-zone/offzone-hw) includes the KiCad schematic and PCB files, a generated BOM, Gerbers, and a short build guide covering resistor and LED placement (LEDs mounted lens-down, observing polarity) and connector soldering. No pricing, production quantity, or distribution details were found; the item is documented only through the maker's repo, with no press coverage or storefront listing turned up.
