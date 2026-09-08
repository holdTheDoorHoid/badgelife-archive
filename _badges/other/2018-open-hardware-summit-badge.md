---
title: 2018 Open Hardware Summit Badge
id: other-2018-open-hardware-summit-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: OSH Park
  url: https://oshpark.com/
  role: fabrication / project lead
- name: Alex Camilo
  url: https://hackaday.io/alex-camilo
  role: designer
- name: Mike Rankin
  role: concept
summary: An ESP32-based e-paper name badge made for the 2018 Open Hardware Summit (MIT, September 27, 2018), letting wearers update the displayed name wirelessly from a phone or laptop.
functions: Displays the wearer's name on an e-paper screen; the name text can be updated wirelessly over WiFi/BLE from an Android or iOS device, or over a serial console; includes a tilt-triggered accelerometer feature and capacitive touch buttons.
look:
  colors: []
  shape: rectangle
  themes:
  - open source
  - hardware tool
tech:
  mcu: ESP32
  leds: null
  display: E-Paper (GDEH0213B1)
  connectivity:
  - wifi
  - bluetooth
  - uart
  battery: 2x AA
  sao_version: none
get_one:
  price: ''
  price_usd: 25
  quantity: '300'
  availability: unknown
  distribution:
  - conference
  where: Distributed to attendees of the 2018 Open Hardware Summit at MIT
make_your_own:
  open_source: true
  hardware_url: https://github.com/OSHPark/ohs18badge
  firmware_url: https://github.com/acamilo/ohs2018-badge-firmware
  eda_tool: KiCad
links:
- label: hackaday.io/project/112222-2018-open-hardware-summit-badge
  url: https://hackaday.io/project/112222-2018-open-hardware-summit-badge
  kind: hackaday
- label: 'GitHub: OSHPark/ohs18badge (hardware design files)'
  url: https://github.com/OSHPark/ohs18badge
  kind: repo
- label: 'GitHub: acamilo/ohs2018-badge-firmware'
  url: https://github.com/acamilo/ohs2018-badge-firmware
  kind: repo
- label: Official badge documentation site
  url: http://oshwabadge2018.github.io/
  kind: website
images:
- file: assets/images/badges/other/2018-open-hardware-summit-badge/0937766332.jpg
  source: https://hackaday.io/project/112222-2018-open-hardware-summit-badge
  credit: OSH Park / Open Hardware Summit 2018 team
  caption: The 2018 Open Hardware Summit badge
- file: assets/images/badges/other/2018-open-hardware-summit-badge/a8da5ef495.png
  source: http://oshwabadge2018.github.io/
  credit: Open Hardware Summit 2018 team
  caption: Badge board render/illustration
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/112222-2018-open-hardware-summit-badge
  title: 2018 Open Hardware Summit Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''Open Hardware Summit 2018''.'
- kind: url
  url: https://github.com/OSHPark/ohs18badge
  title: OSHPark/ohs18badge on GitHub
  accessed: '2026-09-07'
  note: Hardware design files, license (CERN OHL v1.2), event details, budget/quantity, OSHWA UID US000133.
- kind: url
  url: http://oshwabadge2018.github.io/
  title: OSHWA 2018 Badge documentation site
  accessed: '2026-09-07'
  note: Confirms event name, links to GitHub/Twitter/Hackaday; source of badge.png image.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Made for the Open Hardware Summit (MIT, Sept 27 2018) — no matching event id exists in _data/events.yml (the archive''s vocabulary is oriented toward hacker cons like DEF CON/Supercon, not the OSHWA summit), so event is left as "other". LED count/type not stated by any source; leaving tech.leds empty. Current availability (whether any remain, or if it was a one-time con giveaway) not stated. Fact-check pass (2026-09-07): re-fetched all three cited sources (Hackaday project page, OSHPark/ohs18badge repo, oshwabadge2018.github.io) plus the firmware repo; confirmed maker roles, ESP32/GDEH0213B1/2xAA/wifi/bluetooth/uart, $25 budget, 300-unit quantity, CERN OHL v1.2, OSHWA UID US000133, KiCad, and KX122-1037 accelerometer. Removed one unsupported editorial claim from the body ("or anyone nearby" push-updates by strangers) that no source stated. Both saved images verified by eye to show this badge (purple PCB, OHS logo, ESP32-WROOM, e-paper window) and match their cited source pages.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/other/2018-open-hardware-summit-badge.glb
  method: kicad
  source_file: oshw2018badgeprototype.kicad_pcb
  generated: '2026-09-07'
  bytes: 412132
---

The 2018 Open Hardware Summit Badge was built for attendees of the Open Hardware Summit, held at MIT on September 27, 2018. OSH Park led the project, with PCB design by Alex Camilo and concept work by Mike Rankin; roughly 300 units were made to a $25-per-badge budget. Each badge centers on an ESP32 driving a GDEH0213B1 e-paper display that shows the wearer's name, runs on two AA batteries, and includes a KX122-1037 accelerometer and capacitive touch buttons alongside a serial console header for debugging.

What made the badge notable was its wireless name-update feature: attendees could push new text to the display from an Android or iOS device, rather than the name being fixed at flashing time. Firmware ran MicroPython, with both a serial REPL and a browser-based WebREPL over WiFi for interacting with the badge.

The hardware is fully open sourced under the CERN Open Hardware Licence v1.2 and holds OSHWA certification UID US000133, fitting for a badge made for the Open Hardware Summit itself. KiCad schematic and PCB files, along with a bill of materials, are published in OSH Park's `ohs18badge` GitHub repository, with firmware maintained separately by Alex Camilo.

## Make your own

Hardware design files (KiCad schematic, PCB layout, and BOM) are in [OSHPark/ohs18badge](https://github.com/OSHPark/ohs18badge); firmware (MicroPython) is in [acamilo/ohs2018-badge-firmware](https://github.com/acamilo/ohs2018-badge-firmware). The badge is OSHWA-certified (UID US000133) and licensed under CERN OHL v1.2, so both hardware and firmware are free to build from.
