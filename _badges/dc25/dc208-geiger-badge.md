---
title: DC208 Geiger Badge
id: dc25-dc208-geiger-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
redirect_from:
- /badges/dc25/dc208/
type: badge
event: dc25
year: 2017
makers:
- name: DC208 (Boise DEF CON group)
summary: DC208's Geiger-counter-styled badge for DEF CON 25; an ATtiny1634 drives 16 charlieplexed dual-color LEDs and a piezo buzzer to mimic a Geiger counter's click and flash off an onboard optical sensor rather than an actual radiation tube.
functions: 'Simulates Geiger-counter behavior: reads ambient light/IR level on an onboard optical sensor and turns it into randomized LED flashes and piezo "clicks," faster or busier as the sensed light increases.'
look:
  colors: []
  shape: null
  themes:
  - radio
  - measurement
  - hardware tool
tech:
  mcu: ATtiny1634
  leds:
    count: 16
    type: discrete
    note: 16x dual-die SMD LEDs (APB3025EYC-F01, 3225 package) charlieplexed off the ATtiny1634.
  display: none
  connectivity: []
  battery: coin cell
  sao_version: none
  other:
  - Si1132 UV/ambient-light & IR sensor (I2C) stands in for a Geiger-Muller tube; there is no actual radiation detector on the board
  - CVS-1508 piezo buzzer for the counter "click" sound, driven through a BSS316NH6327XT MOSFET
  - LD1117S33 3.3V linear regulator; 3-position DIP switch for mode select
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/badgelife/DC208-DC25-geiger-badge
  firmware_url: https://github.com/badgelife/DC208-DC25-geiger-badge
  eda_tool: KiCad
  license: MIT
links:
- label: Schematics, firmware & KiCad repo
  url: https://github.com/badgelife/DC208-DC25-geiger-badge
  kind: repo
  archived: https://web.archive.org/web/20260907112502/https://github.com/badgelife/DC208-DC25-geiger-badge
images:
- file: assets/images/badges/dc25/dc208-geiger-badge/f23c6d4881.png
  source: https://github.com/badgelife/DC208-DC25-geiger-badge
  credit: DC208
  caption: Rendered PCB of the DC25 Geiger Badge
  archived: https://web.archive.org/web/20260907112502/https://github.com/badgelife/DC208-DC25-geiger-badge
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://badge.life/badges/dc25/dc208/
  title: Original badge.life archive page
  accessed: '2026-09-06'
  note: Migrated from the badge.life Badge Archive; the original page is preserved as the entry body.
  archived: https://web.archive.org/web/20260907112614/https://badge.life/badges/dc25/dc208/
- kind: url
  url: https://github.com/badgelife/DC208-DC25-geiger-badge
  title: badgelife/DC208-DC25-geiger-badge on GitHub
  accessed: '2026-09-07'
  note: README, MIT license, and repo layout (kicad/ and firmware/ folders).
  archived: https://web.archive.org/web/20260907112502/https://github.com/badgelife/DC208-DC25-geiger-badge
- kind: url
  url: https://raw.githubusercontent.com/badgelife/DC208-DC25-geiger-badge/master/firmware/doc/README.md
  title: Firmware build/flash instructions
  accessed: '2026-09-07'
  note: Confirms ATtiny1634 MCU, avr-g++ toolchain, and firmware source file names (charlieplex.cpp, led.cpp, switch.cpp, TWI_master.cpp, ir_sensor.cpp, clicker.cpp).
  archived: https://web.archive.org/web/20260907112740/https://raw.githubusercontent.com/badgelife/DC208-DC25-geiger-badge/master/firmware/doc/README.md
- kind: url
  url: https://raw.githubusercontent.com/badgelife/DC208-DC25-geiger-badge/master/kicad/DC25-geiger-badge.sch
  title: DC25-geiger-badge.sch (KiCad schematic, raw)
  accessed: '2026-09-07'
  note: Component list used to identify the LED count/package, Si1132 optical sensor, CVS-1508 buzzer, MOSFET driver, voltage regulator, and DIP switch; no Geiger-Muller tube or ionization component appears anywhere in the schematic.
  archived: https://web.archive.org/web/20260907112756/https://raw.githubusercontent.com/badgelife/DC208-DC25-geiger-badge/master/kicad/DC25-geiger-badge.sch
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Despite the name and theme, this badge has no actual Geiger-Muller tube or ionizing-radiation sensor: the schematic shows a Si1132 UV/ambient-light sensor used to drive the simulated click rate, plus a piezo buzzer and 16 charlieplexed dual-LEDs. No maker write-up, price, quantity, or event photos beyond the repo''s own PCB render were found; badge.life, Hackaday, and a GitHub/web search for DC208 DEF CON 25 turned up nothing beyond the repo and the original badge.life listing. Availability and distribution (free drop vs. sold) could not be confirmed.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc25/dc208-geiger-badge.glb
  method: kicad
  source_file: kicad/DC25-geiger-badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 225700
---
## Project Links
- [Schematics, Firmware, & Kicad Repo](https://github.com/badgelife/DC208-DC25-geiger-badge)

DC208, the Boise DEF CON group, brought this Geiger-counter-themed badge to DEF CON 25 in 2017. It is built around an ATtiny1634 microcontroller and, despite the name, does not contain an actual Geiger-Muller tube or other ionizing-radiation sensor: the schematic instead shows a Silicon Labs Si1132 UV/ambient-light and IR sensor read over I2C, which the firmware (`ir_sensor.cpp`, `TWI_master.cpp`) uses to drive a simulated "click rate." Those simulated hits are rendered as randomized flashes across 16 charlieplexed dual-die SMD LEDs (`charlieplex.cpp`, `led.cpp`) and as clicks from a piezo buzzer driven through a MOSFET (`clicker.cpp`), with a 3-position DIP switch for mode selection. Power comes from a coin cell regulated down to 3.3V by an onboard LD1117 linear regulator.

The hardware (KiCad schematic and PCB) and firmware source are published under the MIT license in the `badgelife` GitHub organization, but no maker blog post, price, production quantity, or distribution details (sold vs. given away) were found; the badge.life listing itself only linked to the repo with no further description.
