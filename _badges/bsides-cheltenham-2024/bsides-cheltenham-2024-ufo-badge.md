---
title: BSides Cheltenham 2024 UFO Badge
id: bsides-cheltenham-2024-bsides-cheltenham-2024-ufo-badge
layout: badge
parent: BSides Cheltenham 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-cheltenham-2024
year: 2024
makers:
- name: Punk Security
  url: https://github.com/punk-security
summary: A UFO-shaped electronic badge made by Punk Security for BSides Cheltenham 2024, with a single addressable RGB LED, a button, and a Morse-code game explained in a printed instructional booklet handed out on the day.
functions: 'Button-driven Morse code interaction (an instructional booklet with the codes was distributed at the event); runs open Arduino firmware that attendees can modify and reflash over the SAO connector.'
look:
  colors: []
  shape: spaceship
  themes:
  - sci-fi
  - space
  - security
  - learn to solder
tech:
  mcu: ATtiny402
  leds:
    count: 1
    type: WS2812B
    note: Neopixel 5050 addressable RGB LED
  display: none
  connectivity:
  - uart
  battery: CR2032 (surface-mount clip)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given out to attendees at BSides Cheltenham 2024.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/punk-security/bsides-cheltenham-2024-badge/tree/main/eagle-files
  firmware_url: https://github.com/punk-security/bsides-cheltenham-2024-badge/blob/main/bsides-cheltenham-2024-badge.ino
  gerbers_url: https://github.com/punk-security/bsides-cheltenham-2024-badge/blob/main/gerber_files.zip
  bom_url: https://www.digikey.co.uk/en/mylists/list/Z9CH9C1GM3
  eda_tool: Eagle
  fab_url: null
  license: null
  notes: A 3D-printable push-fit case (STL) and the original UFO vector artwork (SVG) are also in the repo. Firmware is built with MegaTinyCore and flashed via UPDI through the SAO connector.
links:
- label: github.com/punk-security/bsides-cheltenham-2024-badge
  url: https://github.com/punk-security/bsides-cheltenham-2024-badge
  kind: repo
images: []
contact: {}
notes:
- UFO-shaped electronic badge made for BSides Cheltenham 2024, with EasyEDA/JLCPCB gerbers provided. Found by the event-year sweep, task bsides-any.
- 'Correction: the sweep''s note said the design files were EasyEDA; the maker''s repo actually provides Autodesk EAGLE schematics/board files (plus ready-made Gerbers for JLCPCB).'
status: released
sources:
- kind: url
  url: https://github.com/punk-security/bsides-cheltenham-2024-badge
  title: BSides Cheltenham 2024 UFO Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-any); event read as ''BSides Cheltenham 2024''.'
- kind: url
  url: https://github.com/punk-security/bsides-cheltenham-2024-badge
  title: punk-security/bsides-cheltenham-2024-badge README
  accessed: '2026-09-10'
  note: 'Confirmed maker, event, MCU (ATtiny402), single Neopixel 5050 LED, CR2032 power, SAO-connector UPDI flashing, Eagle design files, gerbers, BOM link, and the Morse-code instructional booklet.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: No photos of the assembled badge were found in the repo (only the ufo.svg vector artwork and a generic GitHub social-card image, which is not a photo of the item, so no images were saved). Price and quantity made are not stated anywhere; distribution assumed free_drop since it was handed out at the con with an included handout booklet, but this is not explicitly confirmed by the maker.
last_modified_date: '2026-09-10'
---

The BSides Cheltenham 2024 UFO Badge is an open-hardware electronic badge made by the UK security consultancy Punk Security for attendees of BSides Cheltenham in 2024. It is built around an ATtiny402 microcontroller, a single Neopixel 5050 addressable RGB LED, a push button, and a CR2032 coin cell, all shaped into a flying-saucer PCB outline. Attendees received a printed Morse code instructional booklet on the day, pairing the badge's button/LED interaction with a simple code-learning game.

The badge's firmware is open Arduino code (built with MegaTinyCore) that attendees can modify and reflash themselves over UPDI through the badge's SAO-style connector, using a cheap USB-UPDI adapter. Punk Security also published the full Autodesk EAGLE schematic and board files, ready-made Gerbers for ordering exact copies from JLCPCB, a DigiKey bill of materials, a push-fit 3D-printable case (STL), and the original UFO vector artwork, making the whole design straightforward to reproduce or remix.

No price, production quantity, or photos of the assembled badge were located; the repository's images are limited to the vector artwork file and GitHub's auto-generated social preview card.
