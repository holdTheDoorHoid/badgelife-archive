---
title: OFFZONE 2025 Boombox add-on
id: offzone-2025-offzone-2025-boombox-add-on
layout: badge
parent: OFFZONE 2025
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2025
year: 2025
makers:
- name: BI.ZONE / Craft.Zone
summary: A two-board, boombox-shaped SAO for the OFFZONE 2025 badge that plays MP3s from an SD card through two onboard speakers.
functions: Plays .mp3 files off a microSD card through two speakers; three buttons control previous track, play/pause, and next track; 8 onboard LEDs.
look:
  colors:
  - black
  shape: null
  themes:
  - music
tech:
  mcu: null
  leds:
    count: 8
    type: null
    note: 'Firmware source folder is named "405rgt6_final", suggesting an STM32F405RGT6 MCU, but this is not stated explicitly anywhere in the repo — left unconfirmed.'
  display: null
  connectivity:
  - audio
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
  open_source: yes
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2025/boombox_addon
  firmware_url: https://github.com/bi-zone/offzone-hw/tree/master/2025/boombox_addon/405rgt6_final
  eda_tool: Altium
links:
- label: github.com/bi-zone/offzone-hw/tree/main/2025/boombox_addon
  url: https://github.com/bi-zone/offzone-hw/tree/main/2025/boombox_addon
  kind: repo
- label: github.com/bi-zone/offzone-hw/tree/master/2025/boombox_addon
  url: https://github.com/bi-zone/offzone-hw/tree/master/2025/boombox_addon
  kind: repo
  note: 'Corrected URL: the repo''s default branch is "master", not "main"; the original link 404s.'
images:
  - file: assets/images/badges/offzone-2025/offzone-2025-boombox-add-on/9819e3a927.jpg
    source: "https://github.com/bi-zone/offzone-hw/tree/master/2025/boombox_addon"
    credit: "BI.ZONE / Craft.Zone"
    caption: "Assembled boombox add-on, overview"
  - file: assets/images/badges/offzone-2025/offzone-2025-boombox-add-on/9b88681e71.jpg
    source: "https://github.com/bi-zone/offzone-hw/tree/master/2025/boombox_addon"
    credit: "BI.ZONE / Craft.Zone"
    caption: "Topplate board with buttons, LEDs and speakers, assembled"
contact: {}
notes:
- Boombox-themed add-on board for the OFFZONE 2025 badge. Found by the event-year sweep, task con-phdays.
- 'The maker''s README does not give this a distinct display title; "Boombox add-on" (as used in the sheet and repo folder name "boombox_addon") is kept as-is.'
status: released
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2025/boombox_addon
  title: OFFZONE 2025 Boombox add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2025''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/master/2025/boombox_addon
  title: 'bi-zone/offzone-hw: 2025/boombox_addon'
  accessed: '2026-09-08'
  note: 'Repo tree on the actual default branch (master); confirms this is a two-board SAO add-on for the OFFZONE 2025 badge with an SD-card MP3 player, 3 buttons, 8 LEDs, and 2 speakers.'
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/2025/boombox_addon/README.md
  title: boombox_addon README.md
  accessed: '2026-09-08'
  note: 'Primary source for functions, board layout, assembly, and firmware/order details.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: >-
    Confirmed via the maker's own repo (README + file listing) rather than a search snippet.
    The linked URL in the original entry used the "main" branch and 404s; the repo's actual
    default branch is "master" — added the working link and kept the original for reference.
    MCU could not be confirmed: the firmware source folder is named "405rgt6_final", which
    strongly suggests an STM32F405RGT6, but the README/schematics were not opened at pin
    level and nothing states the chip by name, so tech.mcu is left null rather than guessed.
    LED type (WS2812B vs discrete, etc.) is not stated. No price, quantity, or availability
    info was published — this looks like a conference-distributed add-on for OFFZONE 2025
    attendees/CTF rather than a public sale, so get_one fields are left unknown. Design files
    (Altium schematic/PCB, Gerbers, BOM, assembly PDF) and firmware binary are all present in
    the repo, so make_your_own.open_source is "yes".
last_modified_date: '2026-09-08'
---

The Boombox add-on is one of several themed SAOs BI.ZONE / Craft.Zone produced for the OFFZONE 2025 badge (alongside Bear, Anonymous, Angel and Devil, and Terminal add-ons for the same event). It is built from two stacked PCBs — a topplate carrying three buttons, eight LEDs, and two small speakers, and a bottomplate carrying the microcontroller, a microSD card slot, and the connector that plugs into the main badge — joined by a 1x10 header and held together by a 3D-printed case (STL included in the repo). Load MP3 files onto a microSD card, insert it into the slot, and the three buttons step through previous track, play/pause, and next track.

The hardware is fully open: the repo includes Altium schematic and PCB source for both boards, Gerber outputs, bills of materials, an assembly drawing for the bottomplate, and a precompiled firmware binary along with its source, flashed over an SWD header broken out on the bottomplate. No pricing, production quantity, or public sale information is published — the add-on appears to have been distributed to OFFZONE 2025 attendees or CTF participants rather than sold, consistent with BI.ZONE's other yearly OFFZONE badge add-ons.

## Make your own

Order the topplate and bottomplate to the Gerber/finish specs given in the README (2-layer FR4, 1.5 mm, black soldermask, white silkscreen; topplate uses immersion tin finish, bottomplate uses HASL). Populate parts per each board's BOM (`bom_boombox_topplate.xlsx`, `bom_boombox_bottomplate.xlsx`); the topplate has no assembly drawing, but reference photos in the README show a 1x10 connector, 3 buttons, and 8 LEDs on top with 2 speakers on the bottom (LED pin 3/GND, marked with a green dot, goes in the top-right). Follow `assembly_boombox_bottomplate.pdf` for the bottomplate. Print `boombox_case.stl` for the enclosure, then flash `boombox.bin` (source in `405rgt6_final/`) over SWD.
