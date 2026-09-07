---
title: Badgelife DC26 Proto Board
id: dc26-badgelife-dev-board
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc26
year: 2018
makers:
- name: zapp1337
  url: https://github.com/zapp1337
summary: A bare-bones prototyping/breakout board for the
functions: Lets a hobbyist prototype an SAO design by breaking the Shitty Add-On 2x2 connector's four pins (3.3V, GND, SCL, SDA) out onto labeled pads/through-holes for wiring or dead-bug prototyping.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - kit
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - i2c
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/zapp1337/badgelife_dev_board
  firmware_url: null
  eda_tool: KiCad
  license: Apache-2.0
  gerbers_url: null
  fab_url: null
  bom_url: null
  notes: Repo contains KiCad schematic/PCB files and custom footprints for the Shitty 2x2 (through-hole and SMT) SAO connector.
links:
- label: github.com/zapp1337/badgelife_dev_board
  url: https://github.com/zapp1337/badgelife_dev_board
  kind: repo
images:
- file: assets/images/badges/dc26/badgelife-dev-board/7c05d39756.png
  source: https://github.com/zapp1337/badgelife_dev_board
  credit: zapp1337
  caption: Silkscreen artwork reading '#badgelife DC26 Proto Board'
contact: {}
notes:
- badgelife dev board
status: released
sources:
- kind: url
  url: https://github.com/zapp1337/badgelife_dev_board
  title: badgelife_dev_board
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/zapp1337/badgelife_dev_board
  title: zapp1337/badgelife_dev_board (repo contents)
  accessed: '2026-09-07'
  note: KiCad schematic/PCB files, custom "Shitty" 2x2 SAO connector footprints (through-hole and SMT), Apache-2.0 LICENSE file, minimal README ("#badgelife dev board").
- kind: url
  url: https://raw.githubusercontent.com/zapp1337/badgelife_dev_board/master/silk.png
  title: silk.png (board silkscreen artwork)
  accessed: '2026-09-07'
  note: Silkscreen text reads "#badgelife DC26 Proto Board", identifying the event as DEF CON 26 (2018); board labels (3.3v.png, gnd.png, scl.png, sda.png) confirm the four broken-out SAO pins.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The repo itself has almost no documentation (a 2-line README); the event/year (DC26, 2018) comes from text visible in the board's own silkscreen artwork (silk.png) rather than a written project description. No price, quantity, or distribution info found anywhere -- this looks like a personal/community prototyping tool rather than a badge sold or given away, so those fields are left empty. No photo of an assembled/populated board was found, only the KiCad silkscreen graphic.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/badgelife-dev-board/
model:
  file: assets/models/dc26/badgelife-dev-board.glb
  method: kicad
  source_file: badgelife_dev_board.kicad_pcb
  generated: '2026-09-07'
  bytes: 150444
---

The Badgelife DC26 Proto Board is a small prototyping aid made by zapp1337 for the #badgelife community around DEF CON 26 (2018). Rather than being a badge or SAO in its own right, it is a breakout board for the "Shitty Add-On" (SAO) standard: it exposes the four pins of a Shitty 2x2 connector -- 3.3V, GND, SCL and SDA -- onto labeled pads, using custom KiCad footprints for both through-hole and SMT versions of the connector. The board's silkscreen reads "#badgelife DC26 Proto Board," which is the only place the event and year are stated; there is no accompanying write-up.

The project is fully open source: the GitHub repository (github.com/zapp1337/badgelife_dev_board) contains the complete KiCad schematic and PCB layout, the custom connector and label footprints, and an Apache-2.0 license, but no firmware (there is no microcontroller on the board). No information was found about price, quantity made, or how it was distributed, suggesting it was made for personal or small-scale community use rather than sold or handed out at scale.

## Make your own

The hardware files are in the repo root: `badgelife_dev_board.kicad_pcb` and the matching schematic/library files, plus the custom footprints `Badgelife-Shitty-2x2.kicad_mod` and `Badgelife-Shitty-SMT-2x2.kicad_mod`. Open the project in KiCad, and the board can be fabricated directly from the included layout; no separate Gerber export or fab-house share link was found in the repo.
