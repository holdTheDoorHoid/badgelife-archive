---
title: BalCCon Cyberdeck 0o27 (BCD-0o27)
id: balccon-2023-balccon-cyberdeck-0o27-bcd-0o27
layout: badge
parent: BalCCon2k23 - System Failure
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: balccon-2023
year: 2023
makers:
- name: Florian Euchner / CH405 Labs
  url: https://ch405-labs.com/
summary: The official badge for BalCCon2k23, built as a reusable ESP32-S3 cyberdeck and firmware-development platform rather than a single-event throwaway.
functions: Runs example firmware with a WiFi-configuration console and serial console access; designed as a development framework for writing custom firmware after the event, including later community firmware such as a 2024 Pong port.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: ESP32-S3
  leds:
    count: 6
    type: WS2812B
    note: individually addressable RGB
  display: ST7735 1.8" LCD, 160x128
  connectivity:
  - wifi
  - bluetooth
  - i2c
  - uart
  battery: internal battery with TP5000 charge circuit
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed as the official badge at BalCCon2k23 (Novi Sad, September 2023); organizers also handled distribution for attendees.
make_your_own:
  open_source: true
  hardware_url: https://gitlab.com/fschuetz/bcd-0o27/
  firmware_url: https://gitlab.com/fschuetz/bcd-0o27/
  eda_tool: null
links:
- label: hackaday.io/project/192371-balccon-cyberdeck-0o27-aka-bcd-0o27
  url: https://hackaday.io/project/192371-balccon-cyberdeck-0o27-aka-bcd-0o27
  kind: hackaday
- label: badge.gallery/badges/balccon-2023-bcd-0o27
  url: https://badge.gallery/badges/balccon-2023-bcd-0o27
  kind: website
- label: ch405-labs.com/bcd-0o26-hardware-assembly-guide
  url: https://ch405-labs.com/bcd-0o26-hardware-assembly-guide/
  kind: website
- label: gitlab.com/fschuetz/bcd-0o27
  url: https://gitlab.com/fschuetz/bcd-0o27/
  kind: repo
images:
- file: assets/images/badges/balccon-2023/balccon-cyberdeck-0o27-bcd-0o27/338d9d3019.jpg
  source: https://hackaday.io/project/192371-balccon-cyberdeck-0o27-aka-bcd-0o27
  credit: CH405 Labs
  caption: BCD-0o27 cyberdeck badge
contact: {}
notes:
- ESP32-S3-based reusable cyberdeck/firmware-development badge with display, buttons, RGB LEDs and SAO-ish I2C connector, made as the BalCCon2k23 badge. Found by the event-year sweep, task con-balccon.
- The Hackaday.io project page byline reads "florian-schuetz"; the badge's own repo and badge.gallery both credit Florian Euchner / CH405 Labs, which the entry keeps as the maker name.
- 'A follow-up board exists for BalCCon2k24: see the separate entry "BalCCon Mini Cyberdeck 0o00 (MC-0o00)".'
status: released
sources:
- kind: url
  url: https://hackaday.io/project/192371-balccon-cyberdeck-0o27-aka-bcd-0o27
  title: BalCCon Cyberdeck 0o27 (BCD-0o27)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-balccon); event read as ''BalCCon 2023''.'
- kind: url
  url: https://hackaday.io/project/192371-balccon-cyberdeck-0o27-aka-bcd-0o27
  title: BalCCon Cyberdeck 0o27 (BCD-0o27) - Hackaday.io project page
  accessed: '2026-09-08'
  note: Confirmed maker, event/year, MCU, display, LEDs, buttons, connectivity, battery, open-source repo link, and image.
- kind: url
  url: https://badge.gallery/badges/balccon-2023-bcd-0o27
  title: BalCCon Cyberdeck 0o27 - badge.gallery entry
  accessed: '2026-09-08'
  note: Corroborated maker (Florian Euchner / CH405 Labs), specs, and framing as a reusable dev platform; notes a 2024 Pong firmware port exists.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Price and quantity made are not published anywhere found; left blank. Could not reach ch405-labs.com/bcd-0o26-hardware-assembly-guide (fetch failed) to check whether it documents a distinct earlier "0o26" hardware revision versus this "0o27" one — left uninvestigated, flagged as a link to revisit.
last_modified_date: '2026-09-10'
model:
  file: assets/models/balccon-2023/balccon-cyberdeck-0o27-bcd-0o27.glb
  method: kicad
  source_file: hardware/BCD-0o27/BCD-0o27.kicad_pcb
  generated: '2026-09-10'
  bytes: 592872
---

The BalCCon Cyberdeck 0o27 (BCD-0o27) was the official badge for BalCCon2k23, the "System Failure" edition of the BalCCon security conference held in Novi Sad, Serbia in September 2023. Built by Florian Euchner of CH405 Labs, it is an ESP32-S3 board with a 1.8" ST7735 LCD (160x128), six WS2812B RGB LEDs, eight buttons plus reset/boot controls, Wi-Fi and Bluetooth, an internal battery with a TP5000 charge circuit, and a SAO-ish I2C connector.

Rather than a single-event throwaway, the badge was designed as a reusable cyberdeck and firmware-development platform: it ships with an ESP-IDF/C++ firmware framework, a Wi-Fi-configuration console, and documentation aimed at letting owners write and flash their own firmware after the con. Hardware and firmware are fully open source in the maker's GitLab repository. The platform saw continued life after the event, including a community-built Pong firmware port in 2024, and a follow-up board, the BalCCon Mini Cyberdeck 0o00 (MC-0o00), was made for BalCCon2k24.

## Make your own

Hardware design files, schematics, PCB sources, and the C++/ESP-IDF firmware framework are published at https://gitlab.com/fschuetz/bcd-0o27/, including a 3D-printable case and flashing notes via esptool.py.
