---
title: 'ATTENTION! SuperCon AddOn'
id: supercon-2018-attention-supercon-addon
layout: badge
parent: Supercon 2018
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2018
year: 2018
makers:
- name: Morgan
  url: https://hackaday.io/morgan
  role: creator
- name: Ben Hencke
  url: https://hackaday.io/ben-hencke
  role: collaborator
summary: An ESP32-WROOM add-on board for the 2018 Hackaday Superconference badge that runs Espressif's AT firmware, letting badges talk to each other over WiFi and Bluetooth using classic AT modem commands.
functions: Badge-to-badge communication via BLE Serial Port Profile and WiFi Station Mode, driven with retro AT-command syntax (AT, OK, AT+GMR, etc.) sent from the host badge.
look:
  colors:
  - purple
  shape: rectangle
  themes:
  - retro computer
  - radio
tech:
  mcu: ESP32-WROOM
  leds: null
  display: none
  connectivity:
  - wifi
  - ble
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: '18 PCBs ordered; parts brought for about 10'
  availability: unknown
  distribution:
  - conference badge hack
  where: Made for and distributed at Hackaday Superconference 2018; not a general retail item.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/morganrallen/SuperCon2018_Badge_Hack
  eda_tool: null
  license: Apache License 2.0
  notes: 'Firmware repository published (ESP32-firmware and badge-supercon18.X directories); no separate hardware/Gerber files were found linked from the project page.'
links:
- label: hackaday.io/project/161906-attention-supercon-addon
  url: https://hackaday.io/project/161906-attention-supercon-addon
  kind: hackaday
- label: github.com/morganrallen/SuperCon2018_Badge_Hack
  url: https://github.com/morganrallen/SuperCon2018_Badge_Hack
  kind: repo
images:
  - file: assets/images/badges/supercon-2018/attention-supercon-addon/d33a14acf7.png
    source: "https://hackaday.io/project/161906-attention-supercon-addon"
    credit: "Morgan"
    caption: "ATTENTION: SuperCon AddOn ESP32 board for the 2018 Hackaday Superconference badge"
  - file: assets/images/badges/supercon-2018/attention-supercon-addon/90e994045c.png
    source: "https://hackaday.io/project/161906-attention-supercon-addon"
    credit: "Morgan"
    caption: "PCB layout showing the ESP32-WROOM module footprint"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/161906-attention-supercon-addon
  title: Attention! Supercon Addon
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/161906-attention-supercon-addon
  title: ATTENTION! SuperCon AddOn (Hackaday.io project page)
  accessed: '2026-09-07'
  note: 'Confirmed maker (Morgan, with Ben Hencke), event/year (Hackaday Supercon 2018), ESP32-WROOM AT-firmware concept, quantity (18 PCBs ordered, parts for ~10), and image source.'
- kind: url
  url: https://github.com/morganrallen/SuperCon2018_Badge_Hack
  title: morganrallen/SuperCon2018_Badge_Hack
  accessed: '2026-09-07'
  note: 'Firmware repo under Apache 2.0; contains ESP32-firmware and badge-supercon18.X directories. No hardware/Gerber files evident.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No pricing or public sale info found; this reads as a one-off conference project rather than a sold item, so price/quantity-sold and precise LED info were left empty. No dedicated hardware repo or Gerbers found, only the firmware repo, so make_your_own.open_source is "partial" rather than "yes".'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/attention-supercon-addon/
---

The ATTENTION! SuperCon AddOn is an ESP32-WROOM add-on board that Morgan (with collaborator Ben Hencke) built for the 2018 Hackaday Superconference badge. It won the Software Category at Supercon 2018. Rather than writing custom firmware, the project loads Espressif's stock AT command firmware onto the ESP32, letting the board be driven with the same AT-command syntax used by old external modems ("AT", "OK", "AT+GMR", and so on) — a deliberate nod to early dial-up and BBS-era computing.

Functionally, the addon gives the host Supercon badge two communication paths: a BLE Serial Port Profile link and a WiFi Station Mode connection, both intended for badge-to-badge chat between attendees using the retro AT syntax as the interface. The board's PCB carries the "ATTENTION!" branding and project URL silkscreened directly on it. Morgan ordered a small run of 18 PCBs and brought assembled parts for around 10 badges, consistent with a one-off conference project rather than a commercial product.

The firmware is published on GitHub under the Apache 2.0 license, covering the ESP32 AT firmware setup and a companion badge-side codebase, but no separate hardware files (schematic, Gerbers, BOM) were found linked from the project page, so the hardware side is not confirmed open source.
