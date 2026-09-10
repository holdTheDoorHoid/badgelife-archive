---
title: LayerOne 2024 POV Spinner Badge
id: layerone-2024-layerone-2024-pov-spinner-badge
layout: badge
parent: LayerOne 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: layerone-2024
year: 2024
makers:
- name: charliex
  url: https://github.com/charlie-x
summary: A spinner-style electronic badge for LayerOne 2024 that uses a 12-LED strip and a hall-effect sensor to draw persistence-of-vision text and patterns as it spins.
functions: Persistence-of-vision display of text and visual effects while spinning, with a power button to wake the CPU and a slider switch for programmer mode; a hall-effect sensor drives interrupt-based timing and RPM calculation for the display loop; sleeps to save battery when idle.
look:
  colors: []
  shape: circle
  themes:
  - hardware tool
tech:
  mcu: ATtiny4313
  leds:
    count: 12
    type: discrete
    note: 12 LEDs arranged along the spinner arm for the POV effect; visible LED count around the circle varies with spin speed.
  display: none
  connectivity: []
  battery: battery-powered (cell, exact type not stated)
  sao_version: null
make_your_own:
  open_source: true
  hardware_url: https://github.com/charlie-x/LayerOne_2024
  firmware_url: https://github.com/charlie-x/LayerOne_2024
  eda_tool: KiCad
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed as part of the LayerOne 2024 conference badge package.
links:
- label: badge.gallery/badges/layerone-2024-pov-spinner-badge
  url: https://badge.gallery/badges/layerone-2024-pov-spinner-badge
  kind: website
- label: charlie-x/LayerOne_2024 (GitHub)
  url: https://github.com/charlie-x/LayerOne_2024
  kind: repo
images:
- file: assets/images/badges/layerone-2024/layerone-2024-pov-spinner-badge/3a00061d75.jpg
  source: https://github.com/charlie-x/LayerOne_2024
  credit: charlie-x
  caption: POV spinner badge PCB with 12-LED strip
contact: {}
notes:
- Persistence-of-vision spinning-display badge for LayerOne 2024. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task con-layerone.
- Confirmed via badge.gallery and the maker's GitHub repo (charlie-x/LayerOne_2024). Title matches the sweep's wording.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/layerone-2024-pov-spinner-badge
  title: LayerOne 2024 POV Spinner Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''LayerOne 2024''.'
- kind: url
  url: https://badge.gallery/badges/layerone-2024-pov-spinner-badge
  title: LayerOne 2024 POV Spinner Badge
  accessed: '2026-09-10'
  note: Confirmed maker (charliex), event/year, ATtiny4313 MCU, 12-LED POV strip, hall-effect sensor.
- kind: url
  url: https://github.com/charlie-x/LayerOne_2024
  title: charlie-x/LayerOne_2024
  accessed: '2026-09-10'
  note: Maker's repo with schematics/board files (KiCad), firmware, MIT license, and photos; used for hardware details and image.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Price, quantity made, and exact battery type were not stated in either source. Note discrepancy - badge.gallery's summary said "Eagle board/schematic files" but the actual repo uses KiCad files (spin_pov_LDO.sch/.brd); the repo is treated as authoritative.
last_modified_date: '2026-09-10'
model:
  file: assets/models/layerone-2024/layerone-2024-pov-spinner-badge.glb
  method: kicad
  source_file: spin_pov_LDO.brd
  generated: '2026-09-10'
  bytes: 136628
---

The LayerOne 2024 POV Spinner Badge is a fidget-spinner-style electronic badge made by charliex (of null space labs, a longtime LayerOne badge contributor) for LayerOne 2024, held May 25-26, 2024 in Pasadena, California. Instead of a static display, the badge uses a 12-LED strip mounted along one arm of the spinner; as the badge is spun by hand, the LEDs blink in a timed sequence to draw text and patterns in the air via persistence of vision.

Timing for the POV effect comes from a hall-effect sensor that triggers on each rotation, letting the ATtiny4313 firmware calculate RPM and schedule LED updates via interrupts. A power button wakes the CPU from sleep (used to conserve battery when the badge isn't spinning), and a slider switch selects programmer mode for reflashing the firmware.

The hardware (KiCad schematic and board files) and firmware are published on GitHub under the MIT license at charlie-x/LayerOne_2024, making this a fully open-source badge. Pricing, production quantity, and exact battery specifications were not published alongside the design files.

## Make your own

Firmware can be built with avr-gcc or Microchip Studio and flashed to the ATtiny4313 via the board's programming pads. The KiCad project (`spin_pov_LDO.sch` / `spin_pov_LDO.brd`) in the repo provides the schematic and PCB layout needed to fabricate the board.
