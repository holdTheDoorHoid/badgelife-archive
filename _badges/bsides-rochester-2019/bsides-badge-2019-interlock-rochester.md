---
title: BSides_badge_2019 (Interlock Rochester)
id: bsides-rochester-2019-bsides-badge-2019-interlock-rochester
layout: badge
parent: BSides Rochester 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-rochester-2019
year: 2019
makers:
- name: Interlock Rochester
  url: https://github.com/Interlock-Rochester
summary: A blinky attendee badge for BSides Rochester 2019, built by the local hacker/makerspace Interlock Rochester around an ATtiny85 and ten discrete red LEDs.
functions: LED blinking patterns driven by an ATtiny85 microcontroller; no other stated interactivity.
look:
  colors:
  - red
  shape: null
  themes:
  - security
  - badgelife
tech:
  mcu: ATtiny85
  leds:
    count: 10
    type: discrete
    note: Red 0805 SMD LEDs, each with its own 56-ohm current-limiting resistor.
  display: none
  connectivity:
  - none
  battery: 2x CR2032 (Keystone 3034 holders)
  sao_version: none
  sao_ports: null
get_one:
  price: ''
  price_usd: null
  quantity: 500 (per PCB order file "500sets" dated 2018-11-19)
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/Interlock-Rochester/BSides_badge_2019
  firmware_url: null
  gerbers_url: null
  bom_url: https://github.com/Interlock-Rochester/BSides_badge_2019/blob/master/BsidesRock2019.csv
  eda_tool: KiCad
  license: MIT
  fab_url: null
  notes: Repo has KiCad schematic/PCB (v4), BOM (.csv), and a supplier PCB-order spreadsheet, but no firmware source is included.
links:
- label: github.com/Interlock-Rochester/BSides_badge_2019
  url: https://github.com/Interlock-Rochester/BSides_badge_2019
  kind: repo
  archived: https://web.archive.org/web/20260907110407/https://github.com/Interlock-Rochester/BSides_badge_2019
images: []
contact: {}
notes:
- Board has a "Badgelife Shitty2x2" add-on connector, a non-standard 2-pin-by-2 header distinct from the official SAO v1/v2 pinout, so sao_version is left as none.
status: listed
sources:
- kind: url
  url: https://github.com/Interlock-Rochester/BSides_badge_2019
  title: BSides_badge_2019 (Interlock Rochester)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''BSides Rochester 2019''.'
  archived: https://web.archive.org/web/20260907110407/https://github.com/Interlock-Rochester/BSides_badge_2019
- kind: url
  url: https://github.com/Interlock-Rochester/BSides_badge_2019/blob/master/BsidesRock2019.csv
  title: BsidesRock2019.csv (bill of materials)
  accessed: '2026-09-07'
  note: 'BOM: confirms ATtiny85V-10SU MCU, 10x red 0805 LEDs each with a 56-ohm resistor, 2x CR2032 battery holders, and a Badgelife Shitty2x2 connector.'
- kind: url
  url: https://github.com/Interlock-Rochester/BSides_badge_2019/blob/master/T-S8W119900A-500sets-BsidesRock2019_202018-11-19.xls
  title: PCB order spreadsheet (500sets, 2018-11-19)
  accessed: '2026-09-07'
  note: Filename indicates a manufacturing order for 500 sets, dated November 2018, ahead of the 2019 event.
  archived: https://web.archive.org/web/20260907110418/https://github.com/Interlock-Rochester/BSides_badge_2019/blob/master/T-S8W119900A-500sets-BsidesRock2019_202018-11-19.xls
- kind: url
  url: https://github.com/Interlock-Rochester/BSides_badge_2019/blob/master/LICENSE
  title: LICENSE
  accessed: '2026-09-07'
  note: MIT License, copyright 2018 Interlock Rochester; confirms open-source hardware release.
  archived: https://web.archive.org/web/20260907110418/https://github.com/Interlock-Rochester/BSides_badge_2019/blob/master/LICENSE
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No README, no photos of the assembled badge, and no firmware source were found in the repository or via web search (web search budget was exhausted this session, so only the repo itself and its files were checked). Price, exact distribution method, and availability today are unknown; the badge was almost certainly given to BSides Rochester 2019 attendees rather than sold, but no source states this directly so get_one fields are left unknown/empty rather than guessed.
last_modified_date: '2026-09-07'
model:
  file: assets/models/bsides-rochester-2019/bsides-badge-2019-interlock-rochester.glb
  method: kicad
  source_file: BsidesRock2019.kicad_pcb
  generated: '2026-09-07'
  bytes: 141112
---

The BSides_badge_2019 is the attendee badge Interlock Rochester, the city's hacker/makerspace, built for BSides Rochester 2019. It is a simple blinky board: an ATtiny85V microcontroller drives ten discrete red 0805 LEDs, each behind its own 56-ohm resistor, powered by a pair of CR2032 coin cells in through-hole holders. The board also carries a "Badgelife Shitty2x2" add-on connector, a small non-standard header used across badgelife projects of that era for plugging in companion boards, though it is not the official SAO v1/v2 pinout.

The GitHub repository publishes the full KiCad schematic and PCB layout, a bill of materials, and a supplier spreadsheet for a PCB order of 500 sets dated November 2018 — evidence of the production run size, though not of how many were actually assembled or handed out. No firmware source, assembled-board photos, or README accompany the hardware files, so functions beyond LED blinking, price, and distribution method could not be confirmed from the repository, and a web search could not be run this session (the search budget was already exhausted) to check for supplementary coverage.

## Make your own

The repository (MIT licensed) has everything needed to reproduce the PCB: `BsidesRock2019.sch` and `BsidesRock2019.kicad_pcb` (KiCad v4), `BsidesRock2019.csv` for the bill of materials, and the custom `Badgelife-Shitty-2x2.kicad_mod` footprint/library for the add-on connector. No firmware source is included in the repo.
