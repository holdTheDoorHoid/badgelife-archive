---
title: Fri3d Camp 2022 Badge
id: fri3d-2022-fri3d-camp-2022-badge
layout: badge
parent: Fri3d 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: fri3d-2022
year: 2022
makers:
- name: Fri3d Camp
  url: https://fri3d.be/
summary: 'ESP32-based wearable conference badge with a 240x240 color LCD, reused (with revisions) from the 2020 badge design; supports MicroPython and Arduino firmware.'
functions: 'General-purpose badge platform running MicroPython or Arduino firmware; expandable via add-on modules including GameOn (joystick, buttons, microSD, audio amp for games) and Time Blaster.'
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: ESP32-WROVER
  leds: null
  display: 240x240 IPS LCD (ST7789v controller)
  connectivity:
  - wifi
  - ble
  - usb
  - uart
  battery: LiPo (rechargeable, optional charger circuit)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '700+'
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Fri3dCamp/badge-2020
  firmware_url: https://github.com/Fri3dCamp/Badge2020_micropython
  eda_tool: null
links:
- label: fri3d.be/badge/2022
  url: https://fri3d.be/badge/2022/
  kind: website
- label: Hackaday project - Fri3d 2022 Badge
  url: https://hackaday.io/project/169741-fri3d-2022-badge
  kind: hackaday
- label: Badge hardware (badge-2020 repo)
  url: https://github.com/Fri3dCamp/badge-2020
  kind: repo
- label: Badge firmware - MicroPython
  url: https://github.com/Fri3dCamp/Badge2020_micropython
  kind: repo
- label: Badge firmware - Arduino
  url: https://github.com/Fri3dCamp/Badge2020_arduino
  kind: repo
- label: GameOn add-on module
  url: https://github.com/Fri3dCamp/gameon-2020
  kind: repo
- label: Time Blaster add-on module
  url: https://github.com/Fri3dCamp/timeblaster-2020
  kind: repo
images:
- file: assets/images/badges/fri3d-2022/fri3d-camp-2022-badge/6243ee5140.jpg
  source: "https://fri3d.be/badge/2022/"
  credit: "Fri3d Camp"
  caption: "Fri3d Camp 2022 badge with color LCD screen"
contact: {}
notes:
- Screen-equipped wearable badge; GameOn and Time Blaster add-on modules; MicroPython/Arduino firmware, Hackaday project page for specs.
- Hardware and firmware repos are named "2020"/"badge-2020" — this badge is the 2020 design (delayed by the pandemic) carried over and issued at Fri3d Camp 2022, per the design going through revisions REV00-REV03.
status: released
sources:
- kind: url
  url: https://fri3d.be/badge/2022/
  title: Fri3d Camp 2022 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''Fri3d Camp 2022''.'
- kind: url
  url: https://hackaday.io/project/169741-fri3d-2022-badge
  title: Fri3d 2022 Badge - Hackaday.io project
  accessed: '2026-09-07'
  note: 'MCU (ESP32-WROVER, 4MB PSRAM, 16MB flash), display (240x240 ST7789v IPS LCD), LIS2DH12 accelerometer, IR receiver, CP2102N USB-UART bridge, quantity (700+ units), open-source status.'
- kind: url
  url: https://github.com/Fri3dCamp/badge-2020
  title: Fri3dCamp/badge-2020 hardware repo
  accessed: '2026-09-07'
  note: 'Hardware design repo (schematics/design docs through REV00-REV03); LiPo battery with optional charger circuit; confirms this design underlies the 2022 badge.'
- kind: url
  url: https://github.com/Fri3dCamp/gameon-2020
  title: Fri3dCamp/gameon-2020 add-on repo
  accessed: '2026-09-07'
  note: 'Describes the GameOn add-on: joystick, buttons, microSD slot, 1W audio amplifier.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Price, exact quantity beyond "700+", and current availability were not stated on any source checked. LED info not found (no addressable LEDs mentioned; badge relies on the LCD). EDA tool used for the hardware design was not confirmed from the repo page text alone.'
last_modified_date: '2026-09-07'
---

The Fri3d Camp 2022 badge is an ESP32-WROVER-based wearable badge built around a 240x240 pixel color IPS LCD (ST7789v controller), given to attendees of the Belgian family-friendly hacker camp Fri3d Camp. It includes a LIS2DH12 three-axis accelerometer (used partly to control the display backlight and for wake-on-motion power savings), an IR receiver, and a CP2102N USB-to-UART bridge for programming and serial console access. It runs either MicroPython or Arduino-compatible firmware, with over 700 units manufactured.

Notably, the hardware and firmware repositories are named for "2020" rather than 2022: the badge is the design originally built for Fri3d Camp 2020, which was reused (through hardware revisions REV00-REV03) when that badge was issued at the 2022 camp instead, likely due to the event's pandemic-era disruption. The badge supports plug-in add-on modules, including GameOn (a joystick, buttons, a microSD slot, and a small 1W audio amplifier for games) and Time Blaster, both documented in their own open hardware repositories alongside the main badge.

## Make your own

Hardware design files (schematics and design documentation across multiple revisions) are published at github.com/Fri3dCamp/badge-2020, with MicroPython firmware at github.com/Fri3dCamp/Badge2020_micropython and Arduino firmware at github.com/Fri3dCamp/Badge2020_arduino. The GameOn and Time Blaster add-on boards have their own repositories (gameon-2020, timeblaster-2020) for anyone wanting to build compatible expansion modules.
