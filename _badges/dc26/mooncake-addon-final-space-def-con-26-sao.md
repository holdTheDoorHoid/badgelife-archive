---
title: mooncake-addon (Final Space) — DEF CON 26 SAO
id: dc26-mooncake-addon-final-space-def-con-26-sao
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
summary: A
functions: Lights up its 10 addressable LEDs; no other stated interactive function.
look:
  colors: []
  shape: null
  themes:
  - pop culture
  - tv
  form_factor: pcb sao
tech:
  mcu: none
  leds:
    count: 10
    type: discrete
    note: 10x 1206-package LEDs, each with its own 220-ohm resistor, driven via an MCP23017 I/O expander (SOIC28) rather than a microcontroller.
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
  open_source: 'yes'
  hardware_url: https://github.com/d4rkwyng/mooncake-addon
  firmware_url: null
  eda_tool: KiCad
  license: MIT
  notes: Repo includes KiCad schematic/PCB/netlist files, component libraries, manufacturing gerbers for Rev B, Rev C, and a Rev C "ESO" variant, and a bill of materials.
links:
- label: github.com/d4rkwyng/mooncake-addon
  url: https://github.com/d4rkwyng/mooncake-addon
  kind: repo
images:
- file: assets/images/badges/dc26/mooncake-addon-final-space-def-con-26-sao/b48515385e.png
  source: https://github.com/d4rkwyng/mooncake-addon
  credit: d4rkwyng
  caption: Front of the Mooncake SAO PCB
- file: assets/images/badges/dc26/mooncake-addon-final-space-def-con-26-sao/1c1d99100d.png
  source: https://github.com/d4rkwyng/mooncake-addon
  credit: d4rkwyng
  caption: Back of the Mooncake SAO PCB
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/d4rkwyng/mooncake-addon
  title: mooncake-addon (Final Space) — DEF CON 26 SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 26''.'
- kind: url
  url: https://github.com/d4rkwyng/mooncake-addon
  title: 'GitHub repo README: mooncake-addon'
  accessed: '2026-09-07'
  note: Confirms it is a
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: The maker's own repo/README supplied every fact used here (type, event, year, maker, LEDs, BOM, open-source status). No price, quantity made, or distribution method is stated anywhere in the repo, and no secondary coverage (Hackaday, forums, storefronts) was found to fill those in, so get_one fields are left empty/unknown rather than guessed. No firmware is mentioned — the board is driven by an I/O expander, not a programmable MCU, so tech.mcu is set to none and make_your_own.firmware_url left null.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc26/mooncake-addon-final-space-def-con-26-sao.glb
  method: kicad
  source_file: mooncake_RevC.kicad_pcb
  generated: '2026-09-07'
  bytes: 93512
---

The Mooncake Addon is a #badgelife "shitty addon" (SAO) made for DEF CON 26 (2018) by d4rkwyng, with help from AND!XOR and SparX. It takes the shape of Mooncake, the small floating companion character from the animated series Final Space, and plugs into a badge's SAO header via a standard 2x2 shitty connector.

Rather than a microcontroller, the board is built around an MCP23017 I/O expander that drives 10 individually addressable 1206-package LEDs (each with its own 220-ohm current-limiting resistor) plus a 0.1uF decoupling capacitor. The maker released three PCB revisions — an initial Rev A prototype, an updated Rev B, and a final Rev C with an additional "ESO" variant — with gerbers for the later revisions included in the repository.

The full design is open-source under the MIT License: KiCad schematic, PCB layout, netlist, component libraries, manufacturing gerbers, and a bill of materials are all published in the GitHub repo. No pricing, production quantity, or distribution details (sold, given away, contest prize, etc.) were found in the repo or elsewhere, so that information is left blank here.

## Make your own

The repository (https://github.com/d4rkwyng/mooncake-addon) contains everything needed to fabricate the board: KiCad source files under `design/`, ready-to-order gerbers under `gerbers/` for Rev B, Rev C, and the Rev C ESO variant, and a BOM listing the MCP23017, 10 LEDs and resistors, one capacitor, and a shitty connector.
