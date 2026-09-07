---
title: The Blockchain Badge
id: dc29-the-blockchain-badge
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc29
year: 2021
makers:
- name: Hackerware.io
  url: https://www.hackster.io/HacksFromPanda
  role: design and firmware (Abhinav SP)
summary: A wrist-wearable OLED badge made for DEF CON's Blockchain Village, built around a crypto puzzle players solve by entering a binary code on its two side buttons.
functions: 'Boots to a Blockchain-village logo animation and event details (special badge holders also see their name/designation flashed on screen). Holding S1 for 4 seconds opens an "Insert Code" puzzle mode where S1/S2 enter and clear a binary code; the badge auto-checks the code as soon as it is fully entered, unlocking further clues (part of a Blockchain CTF). Reprogrammable over exposed ISP header pins.'
look:
  colors:
  - white
  - blue
  shape: rectangle
  themes:
  - crypto
  - ctf
  - wearable
tech:
  mcu: ATmega32A
  leds: null
  display: 0.96" I2C OLED
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Given to attendees/badge holders of the Blockchain Village at DEF CON 29 (2021); not sold at retail as far as sources show.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://www.hackster.io/HacksFromPanda/the-blockchain-badge-93f659
  eda_tool: null
links:
- label: www.hackster.io/HacksFromPanda/the-blockchain-badge-93f659
  url: https://www.hackster.io/HacksFromPanda/the-blockchain-badge-93f659
  kind: article
images:
- file: assets/images/badges/dc29/the-blockchain-badge/9d65c53535.jpg
  source: "https://www.hackster.io/HacksFromPanda/the-blockchain-badge-93f659"
  credit: "Abhinav SP / HacksFromPanda"
  caption: "The Blockchain Badge, cover image"
- file: assets/images/badges/dc29/the-blockchain-badge/c5836497b2.jpg
  source: "https://www.hackster.io/HacksFromPanda/the-blockchain-badge-93f659"
  credit: "Abhinav SP / HacksFromPanda"
  caption: "Badge photo from the project gallery"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-blockchain-badge-93f659
  title: The Blockchain Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''unclear''.'
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-blockchain-badge-93f659
  title: The Blockchain Badge - Hackster.io project page
  accessed: '2026-09-07'
  note: 'Primary source for maker, story, hardware BOM (ATmega32A, 0.96in I2C OLED, CR2032, 4 tactile switches, DPDT slide switch), function description, and cover/gallery photos. Published August 6, 2021 (mid DEF CON 29, Aug 5-8 2021, Las Vegas).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker Abhinav SP (Hackerware.io, credited in the code header as "Hackerwares.in") built this for "Blockchain Village founder Ajit." The project page never says "DEF CON" outright, but the publish date (Aug 6, 2021) falls squarely inside DEF CON 29 (Aug 5-8, 2021) and Blockchain Village is a long-running DEF CON village, so event was set to dc29 at medium confidence rather than left as other -- flag for a human check if a different con with its own Blockchain Village turns up. Firmware source (C code for the ATmega32A) is published on the page with the CTF puzzle logic deliberately stripped out; no PCB/Gerber files were found, so open_source is partial rather than yes. Price, quantity made, and current availability are not stated anywhere in the source.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/the-blockchain-badge/
---

The Blockchain Badge is a wrist-worn, OLED-equipped conference badge designed by Abhinav SP of Hackerware.io for the Blockchain Village at DEF CON 29 (August 2021), commissioned by village founder Ajit to represent the community and add a puzzle element to the con. Built around a single-sided PCB with an ATmega32A microcontroller and a 0.96" I2C OLED display, it boots into a Blockchain-village logo animation and event details, and flashes the wearer's name and designation on screen for selected badge holders. Lanyard cutouts at the top and bottom let it be worn around the wrist.

The badge's signature feature is a crypto puzzle: holding one side button for four seconds opens an "Insert Code" screen where the two side buttons enter and clear a binary string, which the badge checks automatically once a full code is entered, unlocking further clues in a Blockchain Village CTF. Every badge also exposes ISP header pins so holders can reprogram the ATmega32A themselves; Hackerware.io published a version of the firmware with the CTF puzzle logic removed so people could safely experiment without spoiling the challenge for others still playing it live.

## Make your own

The Hackster.io project page provides the C source for the ATmega32A (written from scratch, including OLED font/animation routines and a serial-communication stub), which can be built and flashed with Microchip Studio and an ISP programmer. No PCB design files (schematic/Gerbers) were found in the sources reviewed, so full hardware reproduction is not currently possible from public files alone.
