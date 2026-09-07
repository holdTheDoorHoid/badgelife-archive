---
title: AramCon Smart Badge — Hardware Files
id: other-aramcon-hardware-badge-pcb-hardware-files
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 0
makers:
- name: AramCon Badge Team
summary: 'Hardware design files for the AramCon community conference badge, covering the 2019 and 2020 editions. Both are nRF52840-based boards with a 2.9" e-paper display, NeoPixel LEDs, and a Shitty Add-On connector.'
functions: 'Runs custom CircuitPython firmware; shows information on the e-paper display, drives NeoPixel lighting effects, reads an onboard accelerometer, and buzzes a vibration motor for haptic feedback. Supports Bluetooth Low Energy / Thread mesh networking between badges. The 2019 board additionally carried an onboard MP3/WMA audio codec (VS1003) and used three Cherry MX switches in place of pushbuttons.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - village badge
tech:
  mcu: nRF52840
  leds:
    count: 2
    type: WS2812B
    note: '2020 badge has 2 WS2812B NeoPixels plus 1 green indicator LED and 1 red LED; the 2019 badge had 4 WS2812B NeoPixels instead.'
  display: 2.9" e-paper (GDEW029T5)
  connectivity:
  - ble
  - zigbee
  battery: null
  sao_version: v1.69bis
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/aramcon-badge/aramcon-hardware
  firmware_url: https://github.com/aramcon-badge/aramcon-firmware
  eda_tool: KiCad
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
links:
- label: github.com/aramcon-badge/aramcon-hardware
  url: https://github.com/aramcon-badge/aramcon-hardware
  kind: repo
- label: github.com/aramcon-badge/aramcon-firmware
  url: https://github.com/aramcon-badge/aramcon-firmware
  kind: repo
  note: 'Firmware repo, described by the maker as "the main firmware code for the AramCon 2 Badge"; MIT licensed, CircuitPython.'
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/aramcon-badge/aramcon-hardware
  title: aramcon-hardware — Badge PCB + Hardware files
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''AramCon''.'
- kind: url
  url: https://raw.githubusercontent.com/aramcon-badge/aramcon-hardware/master/README.md
  title: 'AramCon Smart Badge - Hardware Files (README)'
  accessed: '2026-09-07'
  note: 'Full hardware README: nRF52840 chip, e-paper display, LED counts, pinouts, and the 2019 vs 2020 differences (audio codec, Cherry MX switches, SAO connector version).'
- kind: url
  url: https://github.com/aramcon-badge/aramcon-firmware
  title: aramcon-firmware
  accessed: '2026-09-07'
  note: 'Firmware repo description ("the main firmware code for the AramCon 2 Badge"), confirms MIT license and CircuitPython.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    This repo covers hardware for two badge years (2019 and 2020) rather than a single
    edition, so a single `year` could not be assigned without guessing; the firmware repo's
    description names it "the AramCon 2 Badge," suggesting the 2020 board is AramCon's second
    edition. AramCon does not have a matching entry in _data/events.yml (it appears to be a
    private/community con, likely Israel-based given the org's other repos), so `event` is
    left as `other`. No price, quantity, or distribution details were published (this is a
    hardware-files repo, not a store listing); it was presumably given to attendees rather
    than sold. Battery type/capacity is not specified beyond an analog battery-voltage sense
    pin. No raster photos of an assembled badge were found in the repo (only SVG artwork and
    KiCad files), so no images were saved. `tech.sao_version` reflects the 2020 board
    (v1.69bis, 6-pin); the 2019 board used the original v1.0 (4-pin) SAO connector instead.
    `tech.connectivity` lists ble and zigbee from the controlled vocabulary; the chip and
    README also describe Thread mesh support, which has no vocabulary entry.
last_modified_date: '2026-09-07'
---

The AramCon Smart Badge is a two-generation hardware platform built by the AramCon Badge Team for the AramCon community conference, with separate 2019 and 2020 board revisions documented in the same repository. Both are built around Nordic's nRF52840 (BLE 5 / Thread / Zigbee, ARM Cortex-M4F), and pair a 2.9" e-paper display with NeoPixel RGB LEDs, an I²C accelerometer, serial flash, a vibration motor, and a rear expansion slot. The 2020 board is the more feature-complete of the two, adding a reset button, a Shitty Add-On v1.69bis (6-pin) connector, and 5 pushbuttons; the 2019 board instead used 3 Cherry MX keyboard switches for input, carried a VS1003 MP3/WMA audio codec that the 2020 board dropped, and used the older 4-pin SAO connector.

## Make your own

All PCBs were designed in KiCad, and both the hardware (`aramcon-hardware`) and firmware (`aramcon-firmware`, CircuitPython-based, MIT licensed) repos are public under the `aramcon-badge` GitHub organization. To build one: clone `aramcon-hardware`, open the relevant KiCad project (`pcb/badge` for the 2019 board, `pcbv2` for the 2020 board), fabricate from the included KiCad PCB/schematic files, and flash the matching firmware from `aramcon-firmware` onto the nRF52840.
