---
title: DC-34-Countdown-To-Singularity
id: dc34-countdown-to-singularity
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: eggsactly
  url: https://github.com/eggsactly
summary: A DEF CON 34 badge with eight 7-segment displays showing a running estimate of when the AI singularity will occur; front buttons let the wearer adjust the guess.
functions: Displays and lets the wearer adjust a personal estimate for the date of the AI singularity on an eight-digit 7-segment display, backed by an onboard real-time clock; has three pushbuttons for input.
look:
  colors: []
  shape: null
  themes:
  - sci-fi
  - text
tech:
  mcu: ATmega328P
  leds:
    count: 2
    type: discrete
    note: Two red LEDs (Wurth 151031SS06000)
  display: 8-digit 7-segment display
  connectivity: []
  battery: 9V battery (plus CR1220 RTC backup)
  sao_version: v1
  sao_ports: 7
  inputs:
  - buttons
get_one:
  price: ~$22 in parts (BOM cost per board)
  price_usd: 22.29
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/eggsactly/DC-34-Countdown-To-Singularity/tree/master/DC-34-Countdown-To-Singularity-Board
  firmware_url: https://github.com/eggsactly/DC-34-Countdown-To-Singularity/tree/master/DC-34-Countdown-To-Singularity-Firmware
  eda_tool: KiCad
links:
- label: github.com/eggsactly/DC-34-Countdown-To-Singularity
  url: https://github.com/eggsactly/DC-34-Countdown-To-Singularity
  kind: repo
images: []
contact: {}
notes:
- Repo is a KiCad 6 design + Arduino-based firmware project for a DEF CON 34 (2026) badge; the maker also has an unrelated DC32-Badge repo. No storefront, press coverage, or assembled-badge photos were found.
status: listed
sources:
- kind: url
  url: https://github.com/eggsactly/DC-34-Countdown-To-Singularity
  title: DC-34-Countdown-To-Singularity
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 34''.'
- kind: url
  url: https://raw.githubusercontent.com/eggsactly/DC-34-Countdown-To-Singularity/master/README.md
  title: DC-34-Countdown-To-Singularity README
  accessed: '2026-09-07'
  note: 'README and BOM: describes badge function, ATmega328P MCU, PCF8523T RTC, 7-segment displays, red LEDs, SAO connectors, 9V power, KiCad 6 design files, BOM part costs.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Only source is the maker's own GitHub repo; no storefront, press, Hackaday page, or social posts found confirming distribution, quantity, or pricing beyond raw parts cost. No photos of an assembled unit exist in the repo (only KiCad source files and a board-art SVG), so no images were saved. Price/quantity/availability for the finished badge are unknown; the $22.29 figure is the BOM parts cost, not a sale price.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc34/countdown-to-singularity.glb
  method: kicad
  source_file: DC-34-Countdown-To-Singularity-Board/DC-34-Countdown-To-Singularity-Board.kicad_pcb
  generated: '2026-09-07'
  bytes: 374136
---

The DC-34-Countdown-To-Singularity badge, made by GitHub user eggsactly for DEF CON 34 (2026), is a novelty countdown display: an eight-digit 7-segment readout shows the wearer's personal estimate for when the AI singularity will happen, and three front-mounted pushbuttons let them adjust that guess. The board is built around an ATmega328P (programmed like a stock Arduino via bootloader and an FTDI cable) and keeps time with a PCF8523T real-time clock backed by its own CR1220 coin cell, so the countdown persists between power-ups. It runs from a 9V battery through onboard 5V and 3.3V regulators, and carries two red LEDs plus seven SAO connectors for other badges to plug into.

The project is fully open source: the GitHub repository includes KiCad 6 schematics and PCB layout, an Arduino-IDE firmware sketch, and a bill of materials pricing the parts at roughly $22.29 per board. No storefront listing, press coverage, or photos of an assembled unit turned up, so it is unclear whether the badge was actually produced and distributed at DEF CON 34 or remains a published design.

## Make your own

Hardware files (KiCad 6.0.11+) and firmware (Arduino 1.8.5-compatible) are in the GitHub repo linked above, along with a full BOM with Digikey part links. The bootloader must be burned once with a USBasp-style programmer before the chip can be flashed like a normal Arduino over FTDI.
