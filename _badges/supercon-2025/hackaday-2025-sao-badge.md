---
title: Vince SAO Badge
id: supercon-2025-hackaday-2025-sao-badge
layout: badge
parent: Supercon 2025
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2025
year: 2025
makers:
- name: dtwprojects
summary: A DIY SAO built around an LP5810 I2C LED driver, with a button and an analog sensor input for timing/blink-pattern experiments.
functions: 'Reads a sensor and a button; on a button press it encodes and blinks out sensor/timing values as LED pulse patterns via four LEDs on an LP5810 I2C LED driver.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: ATtiny
  leds:
    count: 4
    type: null
    note: Driven via an LP5810 I2C LED driver (I2C address 0x50, four LED outputs at registers 0x40-0x43).
  display: none
  connectivity:
  - i2c
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
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/dtwprojects/Hackaday_2025_SAO_badge
  eda_tool: null
links:
- label: github.com/dtwprojects/Hackaday_2025_SAO_badge
  url: https://github.com/dtwprojects/Hackaday_2025_SAO_badge
  kind: repo
images: []
contact: {}
notes:
- The repository ("Vince_SAO_Badge") contains only firmware (one .ino sketch) and a GPL-3.0 LICENSE; no schematic, gerbers, BOM, or photos are published, so hardware details beyond what the firmware implies are unconfirmed.
status: listed
sources:
- kind: url
  url: https://github.com/dtwprojects/Hackaday_2025_SAO_badge
  title: Hackaday_2025_SAO_badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''Hackaday 2025''.'
- kind: url
  url: https://raw.githubusercontent.com/dtwprojects/Hackaday_2025_SAO_badge/main/Vince_SAO_Badge/Vince_SAO_Badge.ino
  title: Vince_SAO_Badge.ino
  accessed: '2026-09-07'
  note: 'Firmware source: ATtiny + TinyWireM talking to an LP5810 LED driver at I2C address 0x50, pins for an LED signal output, an analog sensor (A3), and a pull-up button (pin 4); functions encode sensor/timing data as LED blink and pulse patterns.'
- kind: url
  url: https://api.github.com/repos/dtwprojects/Hackaday_2025_SAO_badge/git/trees/main?recursive=1
  title: 'GitHub API: repo file tree'
  accessed: '2026-09-07'
  note: Confirms the repo holds only .gitignore, LICENSE (GPL-3.0), a one-line README, and the single firmware sketch under Vince_SAO_Badge/ - no hardware design files or images.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'No maker profile, storefront, Hackaday.io page, or press coverage of this specific project was found, so maker''s real name, price, quantity, availability, board shape/color, and photos are unknown. The repo name "Hackaday_2025_SAO_badge" and 2025 timing point to Hackaday Supercon 2025 (the annual Hackaday Superconference), but no source explicitly confirms which event the board was built for or distributed at; treat the event assignment as inferred, not confirmed.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/hackaday-2025-sao-badge/
---

This is a small DIY SAO (Simple Add-On) whose firmware repository is named "Vince_SAO_Badge," published by the GitHub user dtwprojects under the repo `Hackaday_2025_SAO_badge`. Only firmware is published: an Arduino sketch for an ATtiny-family microcontroller that talks over I2C (via TinyWireM) to an LP5810 LED driver at address 0x50, controlling four LED channels. The board also reads an analog sensor and a push-button; pressing the button triggers routines that encode sensor and timing values as LED blink and pulse sequences, suggesting the SAO's main trick is displaying numeric data through light rather than a screen.

No schematic, PCB files, bill of materials, or photos accompany the code, and no storefront, Hackaday.io project page, or press coverage of the board turned up in research, so its real name, price, production quantity, availability, and appearance remain unconfirmed. The repository's name and its 2025 timing suggest it was built for that year's Hackaday Superconference, but no source directly states which event it was made for or handed out at.
