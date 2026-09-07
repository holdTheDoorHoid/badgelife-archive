---
title: SAOfinity - An SAO Display solution with options
id: supercon-2025-saofinity-an-sao-display-solution-with-options
layout: badge
parent: Supercon 2025
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2025
year: 2025
makers:
- name: Andy Geppert
  url: https://github.com/ageppert
summary: An open-source RP2040-Zero-based "SAO Demo Controller" that lets makers test and demo an I2C-based SAO on the bench without a host badge.
functions: Powers and drives a single SAO via a shrouded 2x3 header or bare socket, with two QWIIC/I2C sockets for chaining sensors or other add-ons; ships as a soldering kit with reset/boot buttons and a USB-C connection for drag-and-drop RP2040 programming.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - kit
tech:
  mcu: RP2040-Zero
  leds:
    count: 1
    type: RGB
    note: Built-in RGB LED on the RP2040-Zero module.
  display: none
  connectivity:
  - i2c
  - usb
  battery: null
  sao_version: v2
get_one:
  price: $19
  price_usd: 19
  quantity: ''
  availability: limited
  distribution:
  - purchase
  - kit
  where: 'Sold as a soldering kit ("SAO Demo Controller V2") on Tindie by Machine Ideas, LLC; listing showed only 1 in stock as of 2026-09-07.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ageppert/SAOfinity
  firmware_url: https://github.com/ageppert/SAOfinity
  eda_tool: null
links:
- label: github.com/ageppert/SAOfinity
  url: https://github.com/ageppert/SAOfinity
  kind: repo
- label: SAO Demo Controller V2 (kit) on Tindie
  url: https://www.tindie.com/products/36033/
  kind: store
images:
- file: assets/images/badges/supercon-2025/saofinity-an-sao-display-solution-with-options/c9dede2126.jpg
  source: "https://github.com/ageppert/SAOfinity"
  credit: "Andy Geppert"
  caption: "SAOfinity SAO Demo Controller, front"
- file: assets/images/badges/supercon-2025/saofinity-an-sao-display-solution-with-options/21b90c6926.jpg
  source: "https://github.com/ageppert/SAOfinity"
  credit: "Andy Geppert"
  caption: "SAOfinity SAO Demo Controller, back"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- 'This is not itself a worn badge or SAO but a bench accessory (an "SAO display solution") for developing and demoing SAOs; kept under type: accessory rather than badge/sao.'
status: released
sources:
- kind: url
  url: https://github.com/ageppert/SAOfinity
  title: SAOfinity - An SAO Display solution with options
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''unknown''.'
- kind: url
  url: https://github.com/ageppert/SAOfinity
  title: ageppert/SAOfinity GitHub repository (README, Images folder)
  accessed: '2026-09-07'
  note: 'Confirms V1.0 "first draft" shared at Hackaday Supercon.9 (2025); repo folders for electronic design, firmware, mechanical, and manufacturing files; project photos.'
- kind: url
  url: https://www.tindie.com/products/36033/
  title: SAO Demo Controller V2 (kit) - Tindie listing by Machine Ideas, LLC
  accessed: '2026-09-07'
  note: 'Price ($19), RP2040-Zero MCU, built-in RGB LED, two QWIIC sockets, SAO shrouded header + socket, USB-C; only 1 in stock at time of check.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker Andy Geppert''s GitHub repo names V1.0 as a "first draft" shared at Hackaday Supercon.9 (2025); the Tindie store lists a "SAO Demo Controller V2" kit, so the hardware has since revised beyond V1 — the two are treated as the same ongoing project here. No page states total quantity made. Not confirmed whether this exact item was distributed at Supercon itself versus only shared/discussed there.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/saofinity-an-sao-display-solution-with-options/
---

SAOfinity is Andy Geppert's open-source "SAO Demo Controller," a small RP2040-Zero-powered board built to let SAO (Simple/Shiny Add-On) designers test and demo an I2C-based SAO on the bench without needing a full host badge. It exposes a shrouded 2x3 SAO header and a bare SAO socket, plus two QWIIC/I2C sockets for daisy-chaining sensors or other add-ons, and uses the RP2040-Zero's USB-C port for both power and drag-and-drop firmware flashing. Reset and boot buttons and the module's built-in RGB LED round out the board.

Geppert first shared a V1.0 "first draft" of the design at Hackaday Supercon.9 in 2025, publishing electronic design, firmware, mechanical, and manufacturing files in the `ageppert/SAOfinity` GitHub repo. A later "SAO Demo Controller V2" version is sold as a $19 soldering kit through Machine Ideas, LLC's Tindie store, which includes the PCB, RP2040-Zero, two QWIIC sockets, and the SAO header/socket hardware (a USB cable is not included).

