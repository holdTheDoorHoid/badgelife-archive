---
title: Kernelcon 2026 Off Grid Badge
id: kernelcon-2026-kernelcon-2026-off-grid-badge
layout: badge
parent: Kernelcon 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: kernelcon-2026
year: 2026
makers:
- name: ZonkSec / Kernelcon Badge Team
summary: A crank-powered, off-grid electronic badge for Kernelcon 2026 that reads temperature, humidity, and pressure and drives an interactive BLE beacon-hunting quest.
functions: Hand-crank generator charges the badge and unlocks a multi-level crank-spinning boost-multiplier game; BME280 sensor measures temperature/humidity/pressure for weather prediction; BLE scanning detects nearby beacons to progress an on-badge quest; 20 addressable RGB LEDs run multiple animation patterns.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - measurement
  - radio
tech:
  mcu: ESP32-WROOM-32E
  leds:
    count: 20
    type: SK6812
    note: addressable RGB, multiple animation patterns
  display: none
  connectivity:
  - ble
  battery: crank generator with battery management
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
  hardware_url: https://github.com/ZonkSec/kernelcon-2026-badge/tree/main/pcb
  firmware_url: https://github.com/ZonkSec/kernelcon-2026-badge/tree/main/firmware
  gerbers_url: https://github.com/ZonkSec/kernelcon-2026-badge/tree/main/pcb
  eda_tool: KiCad
  license: Released for educational purposes; see individual files for specific licenses.
  notes: Repo also includes a BOM, STL files for the 3D-printed crank arm/knob, and multiple badge variants (hacker, crew, speaker, etc.).
links:
- label: github.com/ZonkSec/kernelcon-2026-badge
  url: https://github.com/ZonkSec/kernelcon-2026-badge
  kind: repo
- label: badge.gallery/events/kernelcon-2026
  url: https://badge.gallery/events/kernelcon-2026
  kind: website
- label: badge.kernelcon.org
  url: https://badge.kernelcon.org/
  kind: website
images:
- file: assets/images/badges/kernelcon-2026/kernelcon-2026-off-grid-badge/a96f538471.png
  source: https://badge.kernelcon.org/
  credit: ZonkSec / Kernelcon Badge Team
  caption: Kernelcon 2026 Off Grid crank-powered badge
contact: {}
notes:
- ESP32-WROOM-32E crank-powered weather-sensing and BLE quest badge (BME280, 20 addressable RGB LEDs) for Kernelcon 2026. Found by the event-year sweep, task con-kernelcon.
- Title confirmed against the maker's own site (badge.kernelcon.org), which calls it the "Off Grid" badge, matching the sweep's title.
status: released
sources:
- kind: url
  url: https://github.com/ZonkSec/kernelcon-2026-badge
  title: Kernelcon 2026 Off Grid Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kernelcon); event read as ''Kernelcon 2026''.'
- kind: url
  url: https://github.com/ZonkSec/kernelcon-2026-badge
  title: ZonkSec/kernelcon-2026-badge README
  accessed: '2026-09-08'
  note: Confirmed maker, event, MCU (ESP32-WROOM-32E), LEDs (20x SK6812), sensor (BME280), BLE, crank-powered charging, KiCad hardware, MicroPython firmware, repo structure (firmware/pcb/3dmodels/flyers), license note.
- kind: url
  url: https://badge.kernelcon.org/
  title: Kernelcon 2026 Off Grid Badge site
  accessed: '2026-09-08'
  note: Confirmed badge description, crank-powered weather device framing, interactive quest, and provided the badge photo (badge.png); no price/quantity/availability stated.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Price, quantity made, and availability were not stated on the repo or the badge site, so those fields are left empty/unknown. No storefront listing was found. Distribution mechanism (given at registration vs. sold) is unspecified in sources, so get_one.distribution is left empty.
last_modified_date: '2026-09-10'
model:
  file: assets/models/kernelcon-2026/kernelcon-2026-off-grid-badge.glb
  method: kicad
  source_file: pcb/weatherV3-kernelcon2026/weatherV3-kernelcon2026.kicad_pcb
  generated: '2026-09-10'
  bytes: 439340
---

The Off Grid Badge is Kernelcon 2026's official electronic badge, built around an ESP32-WROOM-32E and designed to work without wall power: a hand crank charges it through a small generator, gated by a multi-level spinning "boost multiplier" puzzle. Once powered, the badge reads ambient temperature, humidity, and pressure from a BME280 sensor and frames the readings as informal weather prediction, while 20 addressable SK6812 RGB LEDs run a set of animation patterns. A Bluetooth Low Energy scanner lets the badge detect nearby beacons, driving an interactive quest for attendees to work through over the con.

The badge was designed by ZonkSec and the Kernelcon Badge Team, continuing ZonkSec's run of Kernelcon badges going back to 2019. Firmware is written in MicroPython and the PCB was designed in KiCad 8.x, with the project's GitHub repository publishing schematics, PCB layout, custom footprints, production Gerbers, a BOM, and STL files for the printed crank arm and knob, alongside several badge variants (hacker, crew, speaker, etc.). The repo and companion site (badge.kernelcon.org) do not state price, quantity produced, or how it was distributed to attendees.

## Make your own

Hardware and firmware are both published. The `pcb/` directory of the repo holds the KiCad 8.x project (schematics, layout, footprints, Gerbers, BOM) and `3dmodels/` holds STL files for the crank arm and knob (recommended print settings: 0.25mm layer height, 6 walls, 30% infill). Firmware lives in `firmware/` as MicroPython; flashing instructions are in `firmware/FLASH_README.md`.
