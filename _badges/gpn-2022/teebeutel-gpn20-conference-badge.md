---
title: Teebeutel
id: gpn-2022-teebeutel-gpn20-conference-badge
layout: badge
parent: GPN 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: gpn-2022
year: 2022
makers:
- name: Entropia e.V.
  url: https://entropia.de
summary: An ESP32-based, MicroPython-driven conference badge shaped like Entropia's teabag logo, made for GPN20 (Gulaschprogrammiernacht 20) and OSHWA-certified.
functions: Runs custom MicroPython apps and animations on its 128x128 OLED; onboard sensors (including a gas/air-quality sensor and a heart-rate sensor) and an expansion connector let attendees build their own add-ons.
look:
  colors:
  - orange
  - white
  shape: teabag
  themes:
  - logo
  - mascot
  - food
  - drink
tech:
  mcu: ESP32
  leds: null
  display: 128x128 OLED
  connectivity:
  - wifi
  - bluetooth
  battery: LiPo 3.7V
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/entropia/Teebeutel-Hardware
  firmware_url: https://github.com/entropia/Teebeutel-Firmware
  eda_tool: KiCad
  notes: Hardware licensed CERN-OHL-S-2.0, firmware GPL, documentation CC BY-SA. A separate Teebeutel-Expansion repo covers add-on boards for the expansion connector.
links:
- label: github.com/entropia/Teebeutel-Hardware
  url: https://github.com/entropia/Teebeutel-Hardware
  kind: repo
- label: github.com/entropia/Teebeutel-Firmware
  url: https://github.com/entropia/Teebeutel-Firmware
  kind: repo
- label: github.com/entropia/Teebeutel-Expansion
  url: https://github.com/entropia/Teebeutel-Expansion
  kind: repo
- label: OSHWA certification DE000119
  url: https://certification.oshwa.org/de000119.html
  kind: doc
- label: teebeutel.entropia.de (documentation site, offline as of 2026-09-08)
  url: https://teebeutel.entropia.de
  kind: doc
images:
- file: assets/images/badges/gpn-2022/teebeutel-gpn20-conference-badge/9892165a0f.png
  source: https://github.com/entropia/Teebeutel-Hardware
  credit: Entropia e.V.
  caption: 3D render of the Teebeutel badge, front
- file: assets/images/badges/gpn-2022/teebeutel-gpn20-conference-badge/39f448cfd2.png
  source: https://github.com/entropia/Teebeutel-Hardware
  credit: Entropia e.V.
  caption: 3D render of the Teebeutel badge, back
contact: {}
notes:
- OSHWA-certified ESP32/MicroPython electronic conference badge for GPN20 (Gulaschprogrammiernacht), with sensors and expansion capability. Found by the event-year sweep, task ccc-adjacent.
- The sweep's sources list titled the entry "Teebeutel (GPN20 conference badge)"; the maker's own repos and OSHWA listing give the name simply as "Teebeutel" (German for "teabag"), with an English gloss of "Teabag" in the repo description.
status: released
sources:
- kind: url
  url: https://github.com/entropia/Teebeutel-Hardware
  title: Teebeutel (GPN20 conference badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:ccc-adjacent); event read as ''GPN20 2022''.'
- kind: url
  url: https://github.com/entropia/Teebeutel-Hardware
  title: 'entropia/Teebeutel-Hardware: GitHub repo'
  accessed: '2026-09-08'
  note: Confirmed ESP32/MicroPython badge for GPN20 with 128x128 OLED, KiCad hardware, sensors, and expansion header. Front/back render images used for this entry (from tag release-v0.1, path DOCS/3D-Front.png and 3D-Back.png).
- kind: url
  url: https://github.com/entropia/Teebeutel-Firmware
  title: 'entropia/Teebeutel-Firmware: GitHub repo'
  accessed: '2026-09-08'
  note: MicroPython firmware repo; confirms ESP32 + 128x128 OLED, GPL license. No distribution/quantity details found.
- kind: url
  url: https://certification.oshwa.org/de000119.html
  title: DE000119 - OSHWA Certification
  accessed: '2026-09-08'
  note: Confirms OSHWA certification (DE000119, certified 2022-01-09), responsible party Entropia e.V., hardware license CERN-OHL-S-2.0, software GPL, docs CC BY-SA.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Maker's GitHub repos and the OSHWA certification confirm the core facts (ESP32, MicroPython, 128x128 OLED, sensors, expansion header, LiPo 3.7V battery, open hardware/firmware). LED count/type not confirmed and left empty. Price, quantity made, and exact distribution method (free vs. paid) at GPN20 could not be confirmed; the badge's own documentation site (teebeutel.entropia.de) returned connection-refused on every attempt and could not be checked. Front/back board photos (KiCad 3D renders) show the LiPo connector, an SD-card-sized socket, and silkscreened wifi/bluetooth/heart-rate/gas-sensor icons, which is where connectivity and battery were confirmed since the repo text alone did not spell them out.
last_modified_date: '2026-09-10'
model:
  file: assets/models/gpn-2022/teebeutel-gpn20-conference-badge.glb
  method: kicad
  source_file: Teebeutel.kicad_pcb
  generated: '2026-09-10'
  bytes: 778800
---

Teebeutel ("teabag" in German) is Entropia e.V.'s electronic conference badge for GPN20, the 20th Gulaschprogrammiernacht, held in 2022. Named and shaped after the hackerspace's own teabag mascot/logo, the badge runs MicroPython on an ESP32 and drives a 128x128 pixel OLED display for custom apps and animations. It ships with onboard sensors — including a gas/air-quality sensor and a heart-rate sensor, per the maker's documentation pages — and exposes an expansion connector so attendees can build and attach their own add-on boards, with a companion Teebeutel-Expansion repository dedicated to that.

The project is OSHWA-certified (DE000119, certified January 2022), with the hardware (KiCad schematics and PCB) released under CERN-OHL-S-2.0, the firmware under GPL, and the documentation under CC BY-SA. Board renders show an orange PCB with white silkscreen, a 3.7V LiPo battery connector, and icons for wifi and Bluetooth alongside the sensor markings, though the specifics of pricing, production quantity, and how the badge was actually distributed to GPN20 attendees were not found in the sources checked — the project's own documentation site was unreachable at time of research.

## Make your own

Hardware (KiCad project and PCB files) and firmware (MicroPython) are both published on GitHub under entropia/Teebeutel-Hardware and entropia/Teebeutel-Firmware, with a separate entropia/Teebeutel-Expansion repo for building add-on boards for the badge's expansion header.
