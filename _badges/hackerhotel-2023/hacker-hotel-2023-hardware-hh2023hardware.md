---
title: Hacker Hotel 2023 Hardware (hh2023hardware)
id: hackerhotel-2023-hacker-hotel-2023-hardware-hh2023hardware
layout: badge
parent: HackerHotel 2023
grand_parent: Badge Archive
nav_exclude: true
type: other
event: hackerhotel-2023
year: 2023
makers:
- name: AnesidoraCorporation / badge.team
summary: 'A puzzle badge built around an RP2040, artwork-first: the copper and soldermask draw a cracked stone tablet in lapis blue and gold, in the style of an ancient grave marker.'
functions: 'Served as the key to the event puzzle hunt: a text adventure accessible over the badge''s USB serial port, with binary clues hidden on lanyards and location markers around the hotel. Solvers received a physical amulet.'
look:
  colors:
  - blue
  - gold
  - copper
  shape: null
  themes:
  - puzzle
  - ctf
tech:
  mcu: RP2040
  leds: null
  display: none
  connectivity:
  - usb
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Distributed to attendees at HackerHotel 2023.
make_your_own:
  open_source: true
  hardware_url: https://github.com/AnesidoraCorporation/hh2023hardware
  firmware_url: https://github.com/AnesidoraCorporation/hh2023firmware
  eda_tool: KiCad
links:
- label: github.com/AnesidoraCorporation/hh2023hardware/tree/main
  url: https://github.com/AnesidoraCorporation/hh2023hardware/tree/main
  kind: repo
- label: badge.team/docs/badges/hackerhotel-2023
  url: https://badge.team/docs/badges/hackerhotel-2023/
  kind: website
- label: AnesidoraCorporation/hh2023hardware (GitHub)
  url: https://github.com/AnesidoraCorporation/hh2023hardware
  kind: repo
- label: AnesidoraCorporation/hh2023firmware (GitHub)
  url: https://github.com/AnesidoraCorporation/hh2023firmware
  kind: repo
- label: AnesidoraCorporation/hh2023documentation (GitHub)
  url: https://github.com/AnesidoraCorporation/hh2023documentation
  kind: doc
images: []
contact: {}
notes:
- GitHub repository containing the hardware design files (PCB/schematics) for the HackerHotel 2023 badge. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task hackerhotel.
- The event-year sweep's snippet called this the "HackerHotel 2023 Badge"; badge.team names it the Anesidora Mk1. No usable photo of the badge itself was found on badge.team or in the AnesidoraCorporation GitHub repos (hardware repo has design files but no image assets); price and quantity made were not stated anywhere found.
status: listed
sources:
- kind: url
  url: https://github.com/AnesidoraCorporation/hh2023hardware/tree/main
  title: Hacker Hotel 2023 Hardware (hh2023hardware)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:hackerhotel); event read as ''hackerhotel-2023''.'
- kind: url
  url: https://badge.team/docs/badges/hackerhotel-2023/
  title: HackerHotel 2023 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:hackerhotel); event read as ''hackerhotel-2023''.'
- kind: url
  url: https://github.com/AnesidoraCorporation/hh2023hardware
  title: AnesidoraCorporation/hh2023hardware
  accessed: '2026-09-08'
  note: Confirms RP2040 hardware design files in KiCad for the Anesidora Mk1.
- kind: url
  url: https://badge.team/docs/badges/hackerhotel-2023/
  title: Hackerhotel 2023 Badge (Anesidora Mk1)
  accessed: '2026-09-10'
  note: 'Confirms MCU, power (USB-C + CR2032), MicroPython firmware, and team credits (Pim: hardware/software lead; Sake: challenges; Nikolett S.: artwork). No price, quantity, or images given.'
- kind: url
  url: https://github.com/AnesidoraCorporation/hh2023documentation
  title: AnesidoraCorporation/hh2023documentation
  accessed: '2026-09-10'
  note: Puzzle-hunt documentation (memo to visitors, location markers); contains no photos of the badge itself.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Core facts (MCU, power, firmware, purpose, team) are confirmed by both the maker''s GitHub org and badge.team''s own writeup, which agree. No price or quantity-made figure was published anywhere found. No photo of the physical badge turned up: the hardware repo has KiCad/Gerber files but no rendered images, the documentation repo has only puzzle-hunt PDFs/ODTs, and no image URLs were found on the badge.team page or via search. Left images empty rather than guess.'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/hackerhotel-2023/hackerhotel-2023-badge/
model:
  file: assets/models/hackerhotel-2023/hacker-hotel-2023-hardware-hh2023hardware.glb
  method: kicad
  source_file: anesidoraMk1.kicad_pcb
  generated: '2026-09-10'
  bytes: 739924
---


## Notes merged from the duplicate entry "Anesidora Mk1"

The Hackerhotel 2023 badge, the Anesidora Mk1, was built by badge.team (credited to Pim on hardware/software, Sake on challenges, and Nikolett S. on artwork) around an RP2040 microcontroller. The board treats its copper and soldermask as artwork first: together they draw a cracked stone tablet in lapis blue and gold, styled after an ancient grave marker, with the electronics laid into and around the design. A row of buttons and LEDs along the bottom stands in for data and address lines. It runs on USB-C for power, serial, and firmware updates, backed by a CR2032 coin cell with a BAT/USB switch, and its firmware is MicroPython distributed as `.uf2` files.

The badge served as the key to the event's puzzle hunt: attendees interacted with a text adventure over the badge's USB serial port, hunting for binary clues hidden on lanyards and physical markers placed around the hotel. Solvers who worked through the puzzle received a physical amulet as a prize.

## Make your own

Hardware (KiCad design files, schematic, and Gerbers) is published at [AnesidoraCorporation/hh2023hardware](https://github.com/AnesidoraCorporation/hh2023hardware), firmware at [AnesidoraCorporation/hh2023firmware](https://github.com/AnesidoraCorporation/hh2023firmware), and puzzle documentation at [AnesidoraCorporation/hh2023documentation](https://github.com/AnesidoraCorporation/hh2023documentation).
