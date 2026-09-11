---
title: TARS SAO
id: supercon-2024-tars-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://hackaday.io/davedarko
summary: A Simple Add-on inspired by the TARS robot from Interstellar, built around an RP2040-Tiny module with a 160x80 ST7735S colour display, six capacitive touch buttons, a small speaker, a white NeoPixel LED and a QWIIC I2C port, running a menu of apps such as a six-note piano, I2C scanner, scrolling name tag, meme display and Snake; made for the Supercon 8 SAO Contest at Hackaday Supercon 2024.
functions: Menu-driven apps including a 6-note piano keyboard, a Nokia 3310-style tone composer, an I2C terminal/scanner for QWIIC sensors, a scrolling name tag, a "MemeSaver" image display, and Snake.
look:
  colors: []
  shape: null
  themes:
  - robot
  - movie
  - sci-fi
tech:
  mcu: RP2040
  leds:
    count: 1
    type: WS2812B
    note: single white LED used as an activity/cue light, referencing TARS's status light in the film
  display: 160x80 ST7735S color LCD
  connectivity:
  - i2c
  battery: null
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
  hardware_url: https://github.com/davedarko/TARS-SAO
  firmware_url: https://github.com/davedarko/TARS-SAO
  eda_tool: KiCad
links:
- label: github.com/davedarko/TARS-SAO
  url: https://github.com/davedarko/TARS-SAO
  kind: repo
- label: hackaday.io/project/198001-tars-sao
  url: https://hackaday.io/project/198001-tars-sao
  kind: hackaday
images:
- file: assets/images/badges/supercon-2024/tars-sao/9a61d4a284.jpg
  source: https://hackaday.io/project/198001-tars-sao
  credit: davedarko
  caption: TARS SAO cover photo
- file: assets/images/badges/supercon-2024/tars-sao/0a79b10983.jpg
  source: https://hackaday.io/project/198001-tars-sao
  credit: davedarko
  caption: TARS SAO with display and touch buttons
- file: assets/images/badges/supercon-2024/tars-sao/9a61d4a284.jpg
  source: https://hackaday.io/project/198001-tars-sao
  credit: davedarko
  caption: TARS SAO project photo
- file: assets/images/badges/supercon-2024/tars-sao/0a79b10983.jpg
  source: https://hackaday.io/project/198001-tars-sao
  credit: davedarko
  caption: TARS SAO device detail
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/TARS-SAO
  title: 'davedarko/TARS-SAO: A not so simple Add-On for badges'
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/davedarko/TARS-SAO
  title: 'davedarko/TARS-SAO: A not so simple Add-On for badges'
  accessed: '2026-09-07'
  note: Confirmed open-source KiCad hardware design files (MIT license), 6 capacitive touch buttons, small speaker, LED indicator, small display.
- kind: url
  url: https://hackaday.io/project/198001-tars-sao
  title: TARS SAO project page on Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed maker, RP2040-Tiny MCU, 160x80 ST7735S display, capacitive touch buttons (1M ohm resistors), 13x18mm PWM speaker, white activity LED, two QWIIC I2C connectors, menu apps (piano, composer, I2C terminal/scanner, name tag, MemeSaver, planned Snake); made for the Supercon 8 SAO Contest at Hackaday Supercon 2024, project dated September 17, 2024.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Both the GitHub repo and Hackaday.io project page confirm the hardware and software details in the existing summary. No pricing, quantity-made, or distribution/availability details were found on either page beyond it being a Supercon 8 SAO Contest entry; get_one fields left largely empty. No standalone storefront or press coverage located (web search budget was exhausted before a broader search could be run). LED count/type is an inference from "NeoPixel" phrasing in the original sheet summary and "LED indicator" on GitHub; Hackaday.io does not give an explicit LED part number, so tech.leds.type (WS2812B) carries medium confidence only. Merged with duplicate entry 'TARS SAO' (supercon-2024-tars-sao-3).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/supercon-2024/tars-sao-3/
model:
  file: assets/models/supercon-2024/tars-sao.glb
  method: kicad
  source_file: KiCad/TARS/TARS.kicad_pcb
  generated: '2026-09-10'
  bytes: 158372
---

The TARS SAO is a Simple Add-On built by hacker davedarko for the Supercon 8 SAO Contest at Hackaday Supercon 2024, taking its name and cue-light styling from the TARS robot in the film *Interstellar*. It runs on an RP2040-Tiny module and carries a 160x80 ST7735S color LCD, six capacitive-touch buttons wired through 1M ohm resistors in place of physical switches, a small PWM-driven speaker, and a single white LED used as a status/activity indicator. Two QWIIC I2C connectors let it talk to other sensors and boards on a badge.

Rather than doing one thing, the SAO boots into a menu of small apps: a six-note piano keyboard, a Nokia 3310-style tone composer, an I2C terminal and scanner for probing QWIIC devices, a scrolling name-tag display, a "MemeSaver" image viewer, and a planned Snake game. The firmware is written for the Arduino IDE using libraries such as TFT_eSPI and RP2040_PWM.

Hardware (KiCad) and firmware are published on GitHub under an MIT license, making this an open-source build. Neither the GitHub repository nor the Hackaday.io project page states a price, production quantity, or how (or whether) units were distributed beyond the Supercon contest entry itself, so those fields are left blank pending further sources.

## Notes merged from the duplicate entry "TARS SAO"

The TARS SAO is a Simple Add-On built by hacker davedarko for the SAO badge-add-on contest at Hackaday Supercon 8 in 2024, styled after TARS, the boxy robot companion from the film *Interstellar*. It packs a surprising amount into a small board: an RP2040-Tiny microcontroller, a 160x80 color ST7735S display, six capacitive touch buttons (each using a 1M ohm resistor rather than a mechanical switch), a small speaker, a single white "cue light" LED, and a QWIIC I2C connector for hooking up other sensors. Power comes in over USB-C via a programming dongle.

Software-wise it behaves like a tiny Flipper-Zero-style menu device rather than a single-purpose add-on: onboard apps include a 6-note piano, a Nokia-ringtone-inspired tone composer, an I2C terminal and scanner for probing whatever is plugged into the QWIIC port, a name-tag display, a meme/image viewer, and a Snake game. The firmware is written for the Arduino IDE.

Hardware (KiCad) and firmware source are both published under the MIT license in davedarko's `TARS-SAO` GitHub repository, alongside the project's Hackaday.io page, which documents the build across eight project logs covering PCB layout, touch-button tuning, audio, and I2C peripheral work. Neither source states a price, production quantity, or whether units beyond the maker's own were distributed, so those fields are left unknown here.
