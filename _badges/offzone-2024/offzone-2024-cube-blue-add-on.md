---
title: OFFZONE 2024 Cube Blue add-on
id: offzone-2024-offzone-2024-cube-blue-add-on
layout: badge
parent: OFFZONE 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2024
year: 2024
makers:
- name: BI.ZONE / Craft.Zone
summary: A DIY solder-it-yourself SAO from OFFZONE 2024's Craft.Zone village, a small blue-soldermask PCB with four blue LEDs that plugs into a badge over a 4-pin connector.
functions: 'No MCU: the four LEDs simply light up when powered through the connector, driven by two current-limiting resistors. No games or logic, just a soldering-practice light-up add-on.'
look:
  colors:
  - blue
  shape: cube
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 4
    type: 1206
    note: Blue, through-hole-style 1206 LEDs mounted lens-down; two 100-ohm 1206 resistors for current limiting.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed as a solder-your-own kit at OFFZONE 2024's Craft.Zone soldering village; PCB and BOM are published for anyone to order and build their own.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/main/2024/cube_blue_addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bi-zone/offzone-hw/tree/main/2024/cube_blue_addon
  url: https://github.com/bi-zone/offzone-hw/tree/main/2024/cube_blue_addon
  kind: repo
images:
  - file: assets/images/badges/offzone-2024/offzone-2024-cube-blue-add-on/032a3e2bf7.png
    source: "https://github.com/bi-zone/offzone-hw/tree/main/2024/cube_blue_addon"
    credit: "BI.ZONE / Craft.Zone"
    caption: "PCB layout preview of the Cube Blue add-on"
  - file: assets/images/badges/offzone-2024/offzone-2024-cube-blue-add-on/7929c1ba93.jpg
    source: "https://github.com/bi-zone/offzone-hw/tree/main/2024/cube_blue_addon"
    credit: "BI.ZONE / Craft.Zone"
    caption: "Assembled Cube Blue add-on, front, with blue LEDs lit"
contact: {}
notes:
- Blue-cube-themed add-on board for the OFFZONE 2024 badge. Found by the event-year sweep, task con-phdays.
- The sweep's source page (a GitHub tree URL) 404s when fetched directly; the folder does exist under the bi-zone/offzone-hw repo and was confirmed via the GitHub API and raw file URLs.
status: released
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2024/cube_blue_addon
  title: OFFZONE 2024 Cube Blue add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2024''.'
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/2024/cube_blue_addon/README.md
  title: cube_blue_addon README (bi-zone/offzone-hw)
  accessed: '2026-09-08'
  note: 'Maker README (in Russian): PCB spec (2-layer FR4, blue soldermask, black silkscreen), BOM (4x blue 1206 LEDs, 2x 100-ohm 1206 resistors, PLD-4 connector), and assembly instructions.'
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/README.md
  title: offzone-hw repo README
  accessed: '2026-09-08'
  note: 'Confirms the repo collects OFFZONE add-ons by year from Craft.Zone, published as open-source solder-it-yourself kits with gerbers and BOM for anyone to order and build.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own GitHub repo (README, KiCad files, gerbers, BOM, and preview/photo images), so the design and construction are well documented. No MCU is used (LEDs are simply wired through resistors), so functions beyond lighting up are absent. Price, quantity made, and current availability are not stated anywhere in the repo; this looks like a DIY kit distributed at the con''s soldering village rather than a priced product, so those fields are left empty/unknown rather than guessed. SAO connector is a 4-pin "PLD-4" header; not confirmed whether this follows the standard SAO v1 pinout, so sao_version is left null.'
last_modified_date: '2026-09-08'
---

The Cube Blue add-on is one of several small solder-practice kits BI.ZONE's Craft.Zone village put together for OFFZONE 2024. It is a simple two-layer PCB with a blue soldermask, populated with four blue 1206 LEDs (mounted lens-down) and two 100-ohm current-limiting resistors, and it connects to a host badge through a 4-pin PLD-4 header. There is no microcontroller: power delivered through the connector lights the LEDs directly, making the board a beginner-friendly soldering exercise rather than a programmable add-on.

BI.ZONE published the full KiCad source, gerber files, and an HTML bill of materials for the add-on in their `offzone-hw` GitHub repository, alongside matching kits shaped like a green cube, a lamp, a seal, a "this is fine" scene, and a ZIL car from the same year. The repository's top-level instructions walk builders through ordering the PCB (from a Russian fab like Rezonit or from JLCPCB/PCBWay) and sourcing parts, suggesting these were meant to be built by attendees at the con's soldering village rather than sold as a finished, priced product.

## Make your own

The hardware is fully open. Grab the KiCad project and gerbers from the repo folder, order a 2-layer FR4 board (1.5 mm thick, blue soldermask, black silkscreen, HASL finish), and follow the BOM in `cube_blue_addon_BOM.html` to source four blue 1206 LEDs, two 100-ohm 1206 resistors, and a PLD-4 connector. Assembly is three steps: solder the resistors, solder the LEDs lens-down observing polarity, then solder the connector.
