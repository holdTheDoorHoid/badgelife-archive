---
title: TARS SAO
id: supercon-2024-tars-sao-3
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://hackaday.io/hacker/3459-davedarko
summary: A Tamagotchi-sized, Interstellar-TARS-inspired Simple Add-On built for Hackaday Supercon 2024 around an RP2040-Tiny with a 160x80 ST7735S display, six capacitive touch buttons, a speaker, an LED and a QWIIC I2C port, running a Flipper-Zero-style menu with a piano, tone composer, I2C scanner/terminal, name tag and meme viewer.
functions: 'A menu of small apps: a 6-note piano keyboard, a Nokia-ringtone-style tone composer, an I2C terminal and scanner for debugging attached sensors, a name tag display, a meme/image viewer, and a Snake implementation.'
look:
  colors: []
  shape: null
  themes:
  - robot
  - sci-fi
  - movie
tech:
  mcu: RP2040-Tiny
  leds:
    count: 1
    type: discrete
    note: single white "cue light" activity LED
  display: 160x80 ST7735S TFT (RGB565)
  connectivity:
  - i2c
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
  open_source: yes
  hardware_url: https://github.com/davedarko/TARS-SAO
  firmware_url: https://github.com/davedarko/TARS-SAO
  eda_tool: KiCad
links:
- label: hackaday.io/project/198001-tars-sao
  url: https://hackaday.io/project/198001-tars-sao
  kind: hackaday
- label: github.com/davedarko/TARS-SAO
  url: https://github.com/davedarko/TARS-SAO
  kind: repo
images:
- file: assets/images/badges/supercon-2024/tars-sao-3/9a61d4a284.jpg
  source: "https://hackaday.io/project/198001-tars-sao"
  credit: "davedarko"
  caption: "TARS SAO project photo"
- file: assets/images/badges/supercon-2024/tars-sao-3/0a79b10983.jpg
  source: "https://hackaday.io/project/198001-tars-sao"
  credit: "davedarko"
  caption: "TARS SAO device detail"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/198001-tars-sao
  title: TARS SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/198001-tars-sao
  title: TARS SAO
  accessed: '2026-09-07'
  note: Confirmed maker, event (Supercon 8 SAO contest, 2024), MCU, display, buttons, speaker, LED, I2C connectors, USB-C power, and the app list (piano, composer, I2C terminal/scanner, name tag, meme viewer, snake).
- kind: url
  url: https://github.com/davedarko/TARS-SAO
  title: davedarko/TARS-SAO
  accessed: '2026-09-07'
  note: Confirmed MIT license and that KiCad hardware files and Arduino ("Sketchbook") firmware are published in the repo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Made for the Supercon 8 (2024) SAO badge-add-on contest; not confirmed whether it was sold, given away, or remained a contest/personal build, so price/quantity/availability are left unknown. SAO header version (v1 vs v1.69bis/v2) and PCB/solder-mask color are not stated on either source page. Board shape not confirmed from text alone.'
last_modified_date: '2026-09-07'
---

The TARS SAO is a Simple Add-On built by hacker davedarko for the SAO badge-add-on contest at Hackaday Supercon 8 in 2024, styled after TARS, the boxy robot companion from the film *Interstellar*. It packs a surprising amount into a small board: an RP2040-Tiny microcontroller, a 160x80 color ST7735S display, six capacitive touch buttons (each using a 1M ohm resistor rather than a mechanical switch), a small speaker, a single white "cue light" LED, and a QWIIC I2C connector for hooking up other sensors. Power comes in over USB-C via a programming dongle.

Software-wise it behaves like a tiny Flipper-Zero-style menu device rather than a single-purpose add-on: onboard apps include a 6-note piano, a Nokia-ringtone-inspired tone composer, an I2C terminal and scanner for probing whatever is plugged into the QWIIC port, a name-tag display, a meme/image viewer, and a Snake game. The firmware is written for the Arduino IDE.

Hardware (KiCad) and firmware source are both published under the MIT license in davedarko's `TARS-SAO` GitHub repository, alongside the project's Hackaday.io page, which documents the build across eight project logs covering PCB layout, touch-button tuning, audio, and I2C peripheral work. Neither source states a price, production quantity, or whether units beyond the maker's own were distributed, so those fields are left unknown here.
