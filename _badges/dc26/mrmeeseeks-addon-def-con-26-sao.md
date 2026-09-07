---
title: Mr. MeeSeeks Shitty Addon — DEF CON 26 SAO
id: dc26-mrmeeseeks-addon-def-con-26-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: d4rkwyng
  url: https://github.com/d4rkwyng
- name: SparX
summary: A #badgelife shitty addon (SAO) built for DEF CON 26, using an MCP23017 I/O expander to drive eight LEDs through the standard 2x2 "shitty" connector.
functions: Lights eight 1206 LEDs, driven over the SAO connector by an MCP23017 I/O expander rather than direct microcontroller pins.
look:
  colors: []
  shape: null
  themes:
  - tv
  - meme
tech:
  mcu: none
  leds:
    count: 8
    type: discrete
    note: 1206 package LEDs, each with its own 220 ohm current-limiting resistor, switched via an MCP23017 I/O expander (SOIC28).
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/d4rkwyng/mrmeeseeks-addon
  firmware_url: null
  eda_tool: KiCad
  license: MIT
  fab_url: null
  notes: 'Repo includes KiCad schematic/PCB/netlist files, a BOM, and Gerbers for revisions D and E (five revisions, A-E, total). No firmware is needed or published; the addon is passive logic driven by the host badge.'
links:
- label: github.com/d4rkwyng/mrmeeseeks-addon
  url: https://github.com/d4rkwyng/mrmeeseeks-addon
  kind: repo
images:
- file: assets/images/badges/dc26/mrmeeseeks-addon-def-con-26-sao/18bd4aaca4.jpg
  source: "https://github.com/d4rkwyng/mrmeeseeks-addon"
  credit: "d4rkwyng"
  caption: "Front of the Mr. MeeSeeks shitty addon PCB"
- file: assets/images/badges/dc26/mrmeeseeks-addon-def-con-26-sao/c8f045ee35.jpg
  source: "https://github.com/d4rkwyng/mrmeeseeks-addon"
  credit: "d4rkwyng"
  caption: "Back of the Mr. MeeSeeks shitty addon PCB"
contact: {}
notes:
- 'Sheet title lacked "Shitty Addon" wording; expanded per the maker''s own README title "Mr MeeSeeks Shitty Addon".'
status: released
sources:
- kind: url
  url: https://github.com/d4rkwyng/mrmeeseeks-addon
  title: mrmeeseeks-addon — DEF CON 26 SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 26''.'
- kind: url
  url: https://raw.githubusercontent.com/d4rkwyng/mrmeeseeks-addon/master/README.md
  title: mrmeeseeks-addon README
  accessed: '2026-09-07'
  note: 'Confirmed maker credits (d4rkwyng and SparX, with a nod to AND!XOR for a schematics tutorial), BOM (MCP23017, 8x LED, 8x resistor, shitty connector), five PCB revisions A-E, KiCad/MIT open-source status, and front/back preview image paths.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own repo and README confirm all core facts. No pricing, quantity-made, or distribution details were published anywhere in the repo, and no storefront, Hackaday, or social-media presence was found for this specific project, so get_one fields are left empty. Web search budget for this session was exhausted before a broader search (e.g. for AND!XOR mentions or forum posts) could be run.'
last_modified_date: '2026-09-07'
---

The Mr. MeeSeeks Shitty Addon is a DEF CON 26 (2018) SAO made by d4rkwyng and SparX, part of the badgelife scene's tradition of small "shitty addon" boards that plug into a host badge's 2x2 SAO header. It carries eight 1206 LEDs, each behind its own 220 ohm resistor, switched through an MCP23017 I/O expander rather than driven straight from a microcontroller — the board has no MCU of its own and relies entirely on the host badge for logic and power. The maker's README credits AND!XOR's instructional video on shitty-addon schematics as a reference for the design.

The project went through five PCB revisions (A through E), with Gerbers published for the final D and E revisions. Full hardware files — KiCad schematics, PCB layout, netlists, and a bill of materials — are released under the MIT license, with a photographed front-and-back preview of the assembled board on the shitty connector.

No pricing, quantity, or distribution information was found; the GitHub repository is the maker's only public presence for this project, so it's unclear how many were made or how they were given out at DEF CON 26.
