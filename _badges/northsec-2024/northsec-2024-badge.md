---
title: NorthSec 2024 Badge
id: northsec-2024-northsec-2024-badge
layout: badge
parent: NorthSec 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: northsec-2024
year: 2024
makers:
- name: NorthSec
  url: https://github.com/nsec/nsec-badge
summary: The official electronic badge for NorthSec 2024 (Montreal), an ESP32-S3 board with 16 NeoPixels, six buttons, and four SAO ports, built by NorthSec's Team Badge and used both as the conference badge and a CTF platform.
functions: Conference badge with separate "conference", "CTF", and "addon" firmware targets; the CTF firmware ties the badge into NorthSec's on-site capture-the-flag competition, and NeoPixels/buttons support badge-to-badge interaction via the two pairing connectors.
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
  - hardware tool
tech:
  mcu: ESP32-S3-WROOM-1-N8R8
  leds:
    count: 16
    type: NeoPixel
    note: Addressable RGB LEDs
  display: null
  connectivity:
  - wifi
  - ble
  battery: 3xAAA or USB-C
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/nsec/nsec-badge/tree/2024/hw/2024
  firmware_url: https://github.com/nsec/nsec-badge/tree/2024
  eda_tool: Eagle
links:
- label: badge.gallery/events/northsec-2024
  url: https://badge.gallery/events/northsec-2024
  kind: website
- label: nsec/nsec-badge (2024 branch, hardware)
  url: https://github.com/nsec/nsec-badge/tree/2024/hw/2024
  kind: repo
- label: nsec/nsec-badge (2024 branch, README)
  url: https://github.com/nsec/nsec-badge/blob/2024/README.md
  kind: repo
images:
- file: assets/images/badges/northsec-2024/northsec-2024-badge/456e706759.jpg
  source: https://github.com/nsec/nsec-badge/tree/2024/hw/2024
  credit: NorthSec / nsec-badge repo
  caption: Animated badge cell from the official nsec-badge 2024 repository (MIT licensed)
contact: {}
notes:
- Official NorthSec 2024 badge supporting SAO v1.69bis connectors; source on the 2024 branch of nsec/nsec-badge. Found by the event-year sweep, task northsec.
status: released
sources:
- kind: url
  url: https://badge.gallery/events/northsec-2024
  title: NorthSec 2024 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:northsec); event read as ''northsec-2024''.'
- kind: url
  url: https://github.com/nsec/nsec-badge/tree/2024/hw/2024
  title: nsec/nsec-badge 2024 hardware directory
  accessed: '2026-09-08'
  note: Confirmed hardware source files present (Eagle .brd/.sch, gerbers, sao and sao-ctf subfolders); no distribution or pricing details on this page.
- kind: url
  url: https://github.com/nsec/nsec-badge/blob/2024/README.md
  title: nsec/nsec-badge README (2024 branch)
  accessed: '2026-09-08'
  note: Confirmed MCU, LED count, buttons, SAO ports, power options, firmware targets (conference/CTF/addon), and MIT license.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Maker's own repo and README confirm all core specs. Price, quantity made, and exact attendee-distribution details (e.g. whether it was included with registration or sold separately) were not stated anywhere found; left empty rather than guessed.
last_modified_date: '2026-09-10'
model:
  file: assets/models/northsec-2024/northsec-2024-badge.glb
  method: kicad
  source_file: hw/2024/sao/sponsor/sponsor_v1.0.kicad_pcb
  generated: '2026-09-10'
  bytes: 106664
---

The NorthSec 2024 badge is the official electronic badge for NorthSec, the applied security conference held annually in Montreal, built by the event's volunteer Team Badge. It is based on an ESP32-S3-WROOM-1-N8R8 module and carries sixteen addressable NeoPixel RGB LEDs, six input buttons, two pairing connectors for badge-to-badge interaction, and four SAO v1.69bis expansion headers. It can run on USB-C power or three AAA batteries.

Hardware and firmware are both fully open source under the MIT license, published on the `2024` branch of the `nsec/nsec-badge` GitHub repository. The hardware was designed in Eagle (schematic, board, and gerber files are included alongside a CTF-specific SAO subfolder), and firmware is built with Espressif's ESP-IDF via PlatformIO. Three firmware targets exist — "conference," "CTF," and "addon" — reflecting the badge's dual role as a general attendee device and as a platform for NorthSec's on-site capture-the-flag competition.

Pricing, production quantity, and the exact mechanics of how the badge was distributed to attendees (bundled with registration, sold separately, etc.) were not documented on the sources checked, and are left blank rather than guessed.
