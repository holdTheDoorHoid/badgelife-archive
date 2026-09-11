---
title: SuperXBit192
id: supercon-2024-superxbit192
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Kevin Juszczyk
  url: https://hackaday.io/kevin-juszczyk
summary: 'A Supercon SAO built as a miniature handheld gaming system: a 16x12 grid of 192 addressable WS2812 LEDs driven by an RP2040, with a buzzer and 6-axis IMU for motion-controlled games.'
functions: Runs small games rendered on the 16x12 LED matrix, using the onboard 6-axis IMU for motion input and a passive buzzer for sound. Supports I2C host/device roles for multiplayer between two units.
look:
  colors:
  - black
  shape: rectangle
  themes:
  - console
  - arcade
  - learn to solder
tech:
  mcu: RP2040
  leds:
    count: 192
    type: WS2812B
    note: arranged as a 16x12 addressable matrix acting as the display
  display: LED matrix 16x12
  connectivity:
  - i2c
  - usb
  inputs:
  - accelerometer
  battery: 2x AAA or SAO/USB-C power (1.8V-5V input)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/kevinjuszczyk/SuperXBit192
  firmware_url: https://github.com/kevinjuszczyk/SuperXBit192
  eda_tool: KiCad
links:
- label: hackaday.io/project/197883-superxbit192
  url: https://hackaday.io/project/197883-superxbit192
  kind: hackaday
- label: github.com/kevinjuszczyk/SuperXBit192
  url: https://github.com/kevinjuszczyk/SuperXBit192
  kind: repo
images:
- file: assets/images/badges/supercon-2024/superxbit192/ae1e3b9a12.jpg
  source: https://hackaday.io/project/197883-superxbit192
  credit: Kevin Juszczyk
  caption: SuperXBit192 SAO, 16x12 WS2812 LED matrix
- file: assets/images/badges/supercon-2024/superxbit192/9b16f08cc6.jpg
  source: https://github.com/kevinjuszczyk/SuperXBit192
  credit: Kevin Juszczyk
  caption: SuperXBit192 running an LED animation
contact: {}
notes:
- A miniature handheld gaming SAO with 192 addressable LEDs, submitted to both the Tiny Games Challenge and the Supercon 8 SAO Contest. Found by the event-year sweep, task supercon-2024.
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/197883-superxbit192
  title: SuperXBit192
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2024); event read as ''supercon-2024''.'
- kind: url
  url: https://hackaday.io/project/197883-superxbit192
  title: SuperXBit192 - Hackaday.io project page
  accessed: '2026-09-08'
  note: 'Primary source: MCU (RP2040 w/32MB flash), 192 WS2812 LEDs in a 16x12 grid, buzzer, 6-axis IMU, I2C multiplayer, power options, KiCad design files, and contest entries (Tiny Games Challenge, Supercon 8 SAO Contest).'
- kind: url
  url: https://github.com/kevinjuszczyk/SuperXBit192
  title: kevinjuszczyk/SuperXBit192 on GitHub
  accessed: '2026-09-08'
  note: Confirms open-source hardware and firmware repo (KiCad project, gerbers, BOM, source code); source of the second saved image.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Maker's Hackaday.io project page and linked GitHub repo confirm the badge exists and its design. No price, production quantity, or public availability/distribution details were found beyond the two contest entries, so get_one fields are left mostly empty. SAO pin version (4-pin vs 6-pin) is not stated on the pages checked.
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2024/superxbit192.glb
  method: kicad
  source_file: kicad/badgesao.kicad_pcb
  generated: '2026-09-10'
  bytes: 1159916
---

SuperXBit192 is a Simple Add-on (SAO) built by Kevin Juszczyk for Hackaday Supercon 8 (2024), entered in both the Tiny Games Challenge and the Supercon 8 SAO Contest. Rather than a conventional small display, the badge uses a 16x12 grid of 192 addressable WS2812 LEDs as its screen, driven by an RP2040 microcontroller with 32MB of flash. A passive buzzer (tuned for 4-5kHz) provides sound, and an onboard 6-axis IMU lets games respond to motion and tilt.

The board is designed for easy assembly, with components placed on a single side apart from the through-hole SAO connector, and it can be powered from USB-C, the SAO connector (1.8V-5V), or two AAA batteries, drawing roughly 160mA at 3V at idle. It supports I2C in either host or device mode, which the project uses for two-player interaction between units. The maker targeted a novice-programmer-friendly build, supporting both CircuitPython and the RP2040 SDK, and designed the board around JLCPCB's 6-layer prototyping service while noting it could be adapted to a cheaper 4-layer layout for larger runs, with a target unit cost under $10 at 1,000 quantity.

All design files are published on GitHub, including the KiCad project, schematics, bill of materials, production Gerbers, and firmware source, making it a fully open-source build. No information was found on an actual sale price, production run size, or how (or whether) units were distributed beyond the contest entries.
