---
title: minibadge-dice — SaintCon D6 roller minibadge
id: saintcon-2022-minibadge-dice-saintcon-d6-roller-minibadge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Professor-plum
  url: https://github.com/Professor-plum
summary: A SAINTCON-style minibadge that simulates rolling a six-sided die using seven LEDs arranged in the standard dice-pip pattern.
functions: 'Press the button to "roll": the LEDs cycle rapidly through the six pip patterns, slow down, and settle on a random final result (1-6). When idle for a while it cycles through a simple attract pattern.'
look:
  colors: []
  shape: null
  themes:
  - game
  - puzzle
tech:
  mcu: ATtiny40
  leds:
    count: 7
    type: discrete
    note: Seven discrete LEDs wired to form the standard six-sided-die pip layout (PORTA drives the pips directly).
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
  hardware_url: https://github.com/Professor-plum/minibadge-dice/tree/main/hardware
  firmware_url: https://github.com/Professor-plum/minibadge-dice/tree/main/firmware
  eda_tool: KiCad
  license: CC0-1.0
  fab_url: null
  notes: Repo includes KiCad schematic/PCB/project files (plus a fab zip and schematic PDF) and C firmware (Microchip XC8-style, built with a Makefile/NetBeans project) targeting the ATtiny40.
links:
- label: github.com/Professor-plum/minibadge-dice
  url: https://github.com/Professor-plum/minibadge-dice
  kind: repo
images:
- file: assets/images/badges/saintcon-2022/minibadge-dice-saintcon-d6-roller-minibadge/2672411341.jpg
  source: https://github.com/Professor-plum/minibadge-dice
  credit: Professor-plum
  caption: The SaintCon D6 roller minibadge, an ATtiny40-based PCB with LED dice pips
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Professor-plum/minibadge-dice
  title: minibadge-dice — SaintCon D6 roller minibadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://raw.githubusercontent.com/Professor-plum/minibadge-dice/main/firmware/main.c
  title: minibadge-dice firmware source (main.c)
  accessed: '2026-09-07'
  note: Confirms the dice-roll behavior (button press triggers a decelerating random LED sequence) and shows the firmware file was created May 14, 2022, the basis for dating it to SaintCon 2022.
- kind: url
  url: https://github.com/Professor-plum/minibadge-dice/blob/main/hardware/dice-minibadge.kicad_sch
  title: minibadge-dice KiCad schematic
  accessed: '2026-09-07'
  note: Schematic lib_id confirms the MCU is a Microchip ATtiny40-S, plus a Device:LED array, an 8-pin connector (host badge interface), and a button.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The repo itself never states an event or year. The firmware source file's header comment is dated "May 14, 2022," which is the only dating evidence found; on that basis this entry was moved from "other" to saintcon-2022, but that is an inference rather than an explicit statement by the maker. No SaintCon minibadge-guide page, storefront listing, price, quantity, or distribution details for this specific board turned up in web searches (SAINTCON minibadges are traditionally traded/given away in person rather than sold, which fits the empty get_one fields but was not confirmed for this board specifically). No additional photos beyond the one in the repo's image/ folder were found.
last_modified_date: '2026-09-10'
redirect_from:
- /badges/other/minibadge-dice-saintcon-d6-roller-minibadge/
model:
  file: assets/models/saintcon-2022/minibadge-dice-saintcon-d6-roller-minibadge.glb
  method: kicad
  source_file: hardware/dice-minibadge.kicad_pcb
  generated: '2026-09-10'
  bytes: 91944
---

The minibadge-dice is a SAINTCON-style minibadge by the maker Professor-plum: a small PCB that acts as an electronic six-sided die. Seven LEDs are arranged in the standard dice-pip layout and driven directly by an ATtiny40 microcontroller. Pressing the badge's button starts a "roll" — the LEDs flicker rapidly through the six pip patterns, gradually slow down, and land on a random final face, with a brief blink to confirm the result. Left idle, it cycles through a simple attract pattern rather than sitting dark.

Like other SAINTCON minibadges, it appears designed to plug into a larger host badge (the schematic shows an 8-pin connector rather than its own battery), fitting the con's minibadge tradition of small add-on boards that attendees collect, trade, or receive for completing challenges. The GitHub repository does not state which year's SAINTCON it was made for, but the firmware's source-file date (May 14, 2022) points to SaintCon 2022.

## Make your own

The repository (CC0-1.0 licensed) includes the full KiCad project (schematic, PCB, and a fabrication zip) under `hardware/`, plus the C firmware and a Makefile-based build under `firmware/`. Building the firmware requires Microchip's XC8 toolchain for the ATtiny40; the PCB can be fabricated directly from the included KiCad files or the schematic PDF.
