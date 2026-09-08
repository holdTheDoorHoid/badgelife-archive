---
title: 'Anesidora Mk1'
id: hackerhotel-2023-hackerhotel-2023-badge
layout: badge
parent: HackerHotel 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hackerhotel-2023
year: 2023
makers:
- name: badge.team (Pim, Sake, Nikolett S.)
summary: 'A puzzle badge built around an RP2040, artwork-first: the copper and soldermask draw a cracked stone tablet in lapis blue and gold, in the style of an ancient grave marker.'
functions: 'Served as the key to the event puzzle hunt: a text adventure accessible over the badge''s USB serial port, with binary clues hidden on lanyards and location markers around the hotel. Solvers received a physical amulet.'
look:
  colors: [blue, gold, copper]
  shape: null
  themes: [puzzle, ctf]
tech:
  mcu: RP2040
  leds: null
  display: 'none'
  connectivity: [usb]
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: 'Distributed to attendees at HackerHotel 2023.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/AnesidoraCorporation/hh2023hardware
  firmware_url: https://github.com/AnesidoraCorporation/hh2023firmware
  eda_tool: KiCad
links:
- label: badge.team/docs/badges/hackerhotel-2023
  url: https://badge.team/docs/badges/hackerhotel-2023/
  kind: website
- label: 'AnesidoraCorporation/hh2023hardware (GitHub)'
  url: https://github.com/AnesidoraCorporation/hh2023hardware
  kind: repo
- label: 'AnesidoraCorporation/hh2023firmware (GitHub)'
  url: https://github.com/AnesidoraCorporation/hh2023firmware
  kind: repo
- label: 'AnesidoraCorporation/hh2023documentation (GitHub)'
  url: https://github.com/AnesidoraCorporation/hh2023documentation
  kind: doc
images: []
contact: {}
notes:
- 'The event-year sweep''s snippet called this the "HackerHotel 2023 Badge"; badge.team names it the Anesidora Mk1. No usable photo of the badge itself was found on badge.team or in the AnesidoraCorporation GitHub repos (hardware repo has design files but no image assets); price and quantity made were not stated anywhere found.'
status: released
sources:
- kind: url
  url: https://badge.team/docs/badges/hackerhotel-2023/
  title: HackerHotel 2023 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:hackerhotel); event read as ''hackerhotel-2023''.'
- kind: url
  url: https://github.com/AnesidoraCorporation/hh2023hardware
  title: 'AnesidoraCorporation/hh2023hardware'
  accessed: '2026-09-08'
  note: 'Confirms RP2040 hardware design files in KiCad for the Anesidora Mk1.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, RP2040, puzzle-hunt function, USB serial, CR2032, open hardware/firmware) confirmed on badge.team, which is the maker''s own documentation site. Price and quantity made not found anywhere. No image of the badge was locatable within budget. This entry appears to duplicate hackerhotel-2023-hacker-hotel-2023-hardware-hh2023hardware, which covers the same hardware repo.'
last_modified_date: '2026-09-08'
---

The Hackerhotel 2023 badge, the Anesidora Mk1, was built by badge.team (credited to Pim on hardware/software, Sake on challenges, and Nikolett S. on artwork) around an RP2040 microcontroller. The board treats its copper and soldermask as artwork first: together they draw a cracked stone tablet in lapis blue and gold, styled after an ancient grave marker, with the electronics laid into and around the design. A row of buttons and LEDs along the bottom stands in for data and address lines. It runs on USB-C for power, serial, and firmware updates, backed by a CR2032 coin cell with a BAT/USB switch, and its firmware is MicroPython distributed as `.uf2` files.

The badge served as the key to the event's puzzle hunt: attendees interacted with a text adventure over the badge's USB serial port, hunting for binary clues hidden on lanyards and physical markers placed around the hotel. Solvers who worked through the puzzle received a physical amulet as a prize.

## Make your own

Hardware (KiCad design files, schematic, and Gerbers) is published at [AnesidoraCorporation/hh2023hardware](https://github.com/AnesidoraCorporation/hh2023hardware), firmware at [AnesidoraCorporation/hh2023firmware](https://github.com/AnesidoraCorporation/hh2023firmware), and puzzle documentation at [AnesidoraCorporation/hh2023documentation](https://github.com/AnesidoraCorporation/hh2023documentation).
