---
title: faceblade — Face-detecting SAO badge insert DEF CON 31
id: dc31-faceblade-face-detecting-sao-badge-insert-def-con-31
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: svenscore
  url: https://github.com/svenscore
summary: A face-detecting SAO insert for the DEF CON 31 badge that watches for people with a person sensor and reacts on the OLED and NeoPixels.
functions: A person sensor reads face bounding boxes and IDs over I2C every 0.5s and the badge tracks unique faces across the session, filtering small false-positive detections. A push button cycles five modes -- Bling (random text messages, cyan/blue NeoPixel fade), Square (skull and crossbones with blinking eyes, strobe on face detect), Face Counter (large digit count of detected faces), Angel (a weeping-angel bitmap that swaps when a face appears or disappears), and Stick (an animated stick figure that walks across the OLED, fading with position).
look:
  colors: []
  shape: null
  themes:
  - security
  - privacy
  - sci-fi
tech:
  mcu: RP2040
  leds:
    count: 4
    type: NeoPixel
    note: 4 onboard NeoPixels
  display: 0.96" OLED (SSD1306 128x64, I2C)
  connectivity:
  - i2c
  battery: LiPo (Adafruit LiPo Charger BFF)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/svenscore/faceblade
  eda_tool: null
links:
- label: github.com/svenscore/faceblade
  url: https://github.com/svenscore/faceblade
  kind: repo
images:
- file: assets/images/badges/dc31/faceblade-face-detecting-sao-badge-insert-def-con-31/baf583c237.jpg
  source: "https://github.com/svenscore/faceblade"
  credit: "svenscore"
  caption: "The faceblade SAO insert with OLED display and NeoPixels"
- file: assets/images/badges/dc31/faceblade-face-detecting-sao-badge-insert-def-con-31/82d8e1df68.jpg
  source: "https://github.com/svenscore/faceblade"
  credit: "svenscore"
  caption: "The faceblade SAO insert"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/svenscore/faceblade
  title: faceblade — Face-detecting SAO badge insert DEF CON 31
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 31''.'
- kind: url
  url: https://github.com/svenscore/faceblade
  title: 'svenscore/faceblade README'
  accessed: '2026-09-07'
  note: Primary source for hardware list, modes table, firmware details, and images; confirms built for DEF CON 31 SAO PCB.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    No coverage found beyond the maker's own GitHub repo (no Hackaday.io post, forum thread, or press
    coverage located). Repo is firmware/display-assets only -- no hardware design files (schematic/PCB)
    are published, so open_source is marked partial. Price, quantity made, and availability are not
    stated anywhere found; left empty/unknown. Maker svenscore is otherwise known in the SAO community
    for a later project (vecdec, an i2c-passthrough SAO, DEF CON 34) but no other faceblade-specific
    mentions turned up.
last_modified_date: '2026-09-07'
---

faceblade is a face-detecting SAO insert that svenscore built for the DEF CON 31 badge in 2023. It pairs an Adafruit QT Py RP2040 with a person sensor (an I2C camera module intended for on-device face detection), a small SSD1306 OLED, and four onboard NeoPixels, all running CircuitPython. The badge watches for people walking by: a state machine reads face bounding boxes and IDs from the sensor twice a second, filters out small/false detections, and only fires an animation on the transition between "no face" and "face detected," so it doesn't flicker constantly in a crowd.

A push button cycles through five display modes, each pairing a different OLED animation with a different NeoPixel behavior: an idle "Bling" mode with scrolling text and a slow color fade, a skull-and-crossbones face ("Square") that strobes on detection, a digit counter of unique faces seen, a "weeping angel" bitmap that swaps pose when someone appears or vanishes, and a walking stick-figure animation. The badge runs on a LiPo via an Adafruit charger board for portable, untethered operation at the con.

The GitHub repository ships the CircuitPython firmware, OLED bitmap assets, and a prebuilt UF2 image, released under GPL-3.0, but explicitly notes it contains "firmware and display assets only" -- no schematic, PCB layout, or enclosure files are published, so this project can be rebuilt in software but not fully reproduced in hardware from the repo alone. No storefront, press coverage, or social posts about faceblade were found; the GitHub repo appears to be the only public record of the project.
