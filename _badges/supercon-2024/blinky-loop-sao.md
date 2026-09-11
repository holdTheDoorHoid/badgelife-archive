---
title: Blinky Loop SAO
id: supercon-2024-blinky-loop-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Thomas Flummer
  url: https://hackaday.io/thomas-flummer
summary: A circular SAO with a ring of 12 addressable RGB LEDs and an accelerometer, made for the Supercon 8 (2024) SAO Contest.
functions: Displays LED animations around the ring; the onboard accelerometer senses orientation and movement so animations can stay correctly oriented regardless of how the SAO is mounted, or support gesture/tilt-based effects like a digital level.
look:
  colors:
  - pink
  shape: circle
  themes:
  - minimalist
tech:
  mcu: none
  leds:
    count: 12
    type: WS2812b-2020
    note: Driven over one GPIO from the host badge; no onboard microcontroller.
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: about 35 (test batch)
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/flummer/blinky-loop-sao
  firmware_url: null
  eda_tool: KiCad
notes: []
links:
- label: hackaday.io/project/198163-blinky-loop-sao
  url: https://hackaday.io/project/198163-blinky-loop-sao
  kind: hackaday
- label: github.com/flummer/blinky-loop-sao
  url: https://github.com/flummer/blinky-loop-sao
  kind: repo
images:
- file: assets/images/badges/supercon-2024/blinky-loop-sao/7eeb060d20.jpg
  source: https://hackaday.io/project/198163-blinky-loop-sao
  credit: Thomas Flummer
  caption: Blinky Loop SAO, assembled, pink PCB
- file: assets/images/badges/supercon-2024/blinky-loop-sao/8f4ebebbb1.jpg
  source: https://hackaday.io/project/198163-blinky-loop-sao
  credit: Thomas Flummer
  caption: Blinky Loop SAO project photo
contact: {}
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198163-blinky-loop-sao
  title: Blinky Loop SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 8 SAO Contest entry''.'
- kind: url
  url: https://hackaday.io/project/198163-blinky-loop-sao
  title: Blinky Loop SAO
  accessed: '2026-09-07'
  note: Maker (Thomas Flummer), event/year (Supercon 8, 2024), LED count/type (12x WS2812b-2020), accelerometer (LIS2DH12), no onboard MCU, approx. 35 units made, source files link, images.
- kind: url
  url: https://github.com/flummer/blinky-loop-sao
  title: flummer/blinky-loop-sao
  accessed: '2026-09-07'
  note: Confirms KiCad (v8.99 nightly/v9+) design files, Gerbers, CC BY-SA 4.0 license, LIS2DH12 accelerometer and WS2812b-2020 LEDs.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Made for the Supercon 8 (2024) SAO Contest, so event corrected from supercon-2025 to supercon-2024. Price, exact SAO connector pin count (4-pin vs 6-pin), and firmware/example code location were not stated by either source.
last_modified_date: '2026-09-10'
redirect_from:
- /badges/supercon-2025/blinky-loop-sao/
model:
  file: assets/models/supercon-2024/blinky-loop-sao.glb
  method: kicad
  source_file: BlinkyLoopSAO_2x2_panel.kicad_pcb
  generated: '2026-09-10'
  bytes: 410124
---

The Blinky Loop SAO is a circular add-on badge by Thomas Flummer, built for the Supercon 8 (2024) SAO Contest. It carries a ring of 12 WS2812b-2020 addressable RGB LEDs around a central SAO connector, plus an LIS2DH12 3-axis accelerometer wired over I2C. The board has no microcontroller of its own — the LEDs and accelerometer are driven directly by the host badge's GPIO and I2C lines — so the SAO's animations depend on whatever code the host badge runs for it.

The accelerometer lets animations track the SAO's physical orientation, so a light pattern can stay right-side-up no matter how the loop is mounted, or be used for simple movement/tilt-based effects such as a digital level or gesture-triggered animation. About 35 units were made as a test batch. Hardware design files (KiCad, Gerbers) are published on GitHub under a CC BY-SA 4.0 license.

## Make your own

The hardware — KiCad schematics, PCB layout, and Gerber files — is published at github.com/flummer/blinky-loop-sao under CC BY-SA 4.0. Building one requires 12x WS2812b-2020 LEDs, an LIS2DH12 accelerometer, and a host badge capable of driving the LED ring and reading the accelerometer over I2C; no separate firmware repository for the SAO itself was found.
