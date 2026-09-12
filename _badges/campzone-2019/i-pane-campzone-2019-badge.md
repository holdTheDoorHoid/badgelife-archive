---
title: I-Pane (CampZone 2019 badge)
id: campzone-2019-i-pane-campzone-2019-badge
layout: badge
parent: Campzone 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: campzone-2019
year: 2019
makers:
- name: Badge.Team (Tom Clement, Roel Harbers)
  url: https://badge.team/
summary: 'The official CampZone 2019 badge: an ESP32-based multi-badge with an RGB LED matrix display, running Badge.team''s Python app-store firmware over WiFi/BLE.'
functions: Runs downloadable Python apps from the Hatchery app store over WiFi; drives an RGB LED matrix ("eye-killing" per the maker); supports USB offline development. An optional solderable "coin" add-on PCB carried an MPU-6050 accelerometer/gyro and temperature sensor.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: ESP32
  leds: null
  display: RGB LED matrix
  connectivity:
  - wifi
  - ble
  - usb
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
  open_source: true
  hardware_url: https://github.com/badgeteam/cz19-badge
  firmware_url: https://github.com/badgeteam/cz19-badge
  eda_tool: null
  license: MIT
  notes: Includes a separate hardware repo for the optional MPU-6050 "coin" add-on, jorisplusplus/MPU_Coin.
links:
- label: badge.team/docs/badges/campzone-2019
  url: https://badge.team/docs/badges/campzone-2019/
  kind: website
  archived: https://web.archive.org/web/20260610145839/https://badge.team/docs/badges/campzone-2019/
- label: badgeteam/cz19-badge (GitHub, archived repo)
  url: https://github.com/badgeteam/cz19-badge
  kind: repo
  archived: https://web.archive.org/web/20260912174814/https://github.com/badgeteam/cz19-badge
- label: jorisplusplus/MPU_Coin (optional coin add-on hardware)
  url: https://github.com/jorisplusplus/MPU_Coin
  kind: repo
  archived: https://web.archive.org/web/20260912174919/https://github.com/jorisplusplus/MPU_Coin
images: []
contact: {}
notes:
- RGB LED matrix badge, extended 8MB flash ESP32 WiFi/BLE, Hatchery Python app store, USB offline dev.
status: released
sources:
- kind: url
  url: https://badge.team/docs/badges/campzone-2019/
  title: I-Pane (CampZone 2019 badge)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''CampZone 2019''.'
  archived: https://web.archive.org/web/20260610145839/https://badge.team/docs/badges/campzone-2019/
- kind: url
  url: https://github.com/badgeteam/cz19-badge
  title: badgeteam/cz19-badge
  accessed: '2026-09-07'
  note: Confirms this is the official CampZone 2019 event badge repo (now archived/read-only on GitHub), MIT licensed, with firmware and hardware design files as submodules/subfolders.
  archived: https://web.archive.org/web/20260912174814/https://github.com/badgeteam/cz19-badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The badge.team docs page (maker''s own page) confirms ESP32 with 8MB flash, RGB LED matrix, WiFi/BLE, Python app store via Hatchery, and USB offline dev, plus an optional MPU-6050 "coin" add-on PCB. Exact LED count/type, price, quantity made, and a photo of the physical badge were not found in the sources checked. The GitHub repo (badgeteam/cz19-badge) confirms MIT license and open hardware+firmware but is now archived/read-only, so file-level detail (BOM, Gerbers, exact repo layout) was not verified beyond the top-level description. Marked status: released on the assumption CampZone 2019 attendees received it as the event badge, consistent with badge.team''s pattern for other camps.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/campzone-2019/i-pane-campzone-2019-badge.glb
  method: kicad
  source_file: cz19-badge-hardware/cz19-badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 1070396
---

The I-Pane was the official electronic badge given to attendees of CampZone 2019, designed and produced by the Dutch collective Badge.team (credited to Tom Clement for hardware, with Roel Harbers). Like other badge.team event badges of that era, it is built around an ESP32 microcontroller with extended 8MB flash and runs the team's shared multi-badge firmware platform, which lets wearers download and run small Python applications over WiFi from the group's "Hatchery" app store, alongside offline development over USB. The badge's headline feature is a bright RGB LED matrix display, which the maker's own documentation describes as "eye-killing."

CampZone attendees who wanted to extend their badge could solder on an optional add-on PCB nicknamed the "coin," which carries an MPU-6050 accelerometer/gyroscope and temperature sensor and connects to the main board; its hardware is published separately. The badge's own hardware and firmware are open source under the MIT license via the `badgeteam/cz19-badge` repository on GitHub, though that repository has since been archived and is read-only.

No pricing, production quantity, or a photo of the physical badge could be confirmed from the sources checked; the badge.team documentation page includes only a schematic-style SVG illustration of the board rather than a photograph.
