---
title: Alien Robot Badge
id: dc32-alien-robot-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: HackerBoxes
  url: https://hackerboxes.com
summary: A solder-it-yourself alien-robot badge from HackerBox #0104 "Engage," built around an ESP32-C3 Supermini and two 4x4 WS2812B LED matrices standing in for the robot's glowing eyes.
functions: Runs an Arduino sketch with multiple triggered display modes for the eye LEDs plus a sound effect; an expanded community sketch (HB0104_Wireless_Badge.ino) adds 20 display modes and button-triggered wireless features.
look:
  colors:
  - multicolor
  shape: robot
  themes:
  - robot
  - sci-fi
  - wearable
  - learn to solder
tech:
  mcu: ESP32-C3 (Supermini dev board)
  leds:
    count: 32
    type: WS2812B
    note: Two 4x4 WS2812B ("neopixel") matrices form the robot's two eyes.
  display: none
  connectivity:
  - wifi
  - bluetooth
  inputs:
  - buttons
  battery: powered by host badge
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: $39 (badge kit alone) / $59 (full HackerBox 0104 monthly box)
  price_usd: 39
  quantity: ''
  availability: sold_out
  availability_note: 'hackerboxes.com/products/alien-robot-badge-kit checked 2026-09-06: listed as "Sold out."'
  distribution:
  - purchase
  - kit
  where: Sold by HackerBoxes as a standalone kit and as the featured badge project in the HackerBox #0104 "Engage" monthly subscription box, shipped around the summer solstice 2024 ahead of DEF CON 32 / Hacker Summer Camp.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://www.instructables.com/HackerBox-0104-Engage/
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: The Instructables build guide includes the demo Arduino sketch and links an expanded community sketch (HB0104_Wireless_Badge.ino) with 20 display modes; no PCB source/Gerbers were found published.
links:
- label: hackerboxes.com/collections/past-hackerboxes/products/hackerbox-0104-engage
  url: https://hackerboxes.com/collections/past-hackerboxes/products/hackerbox-0104-engage
  kind: store
- label: www.hackerboxes.com
  url: https://www.hackerboxes.com
  kind: store
- label: Alien Robot Badge Kit (standalone product page)
  url: https://hackerboxes.com/products/alien-robot-badge-kit
  kind: store
- label: 'HackerBox 0104: Engage — Instructables build guide'
  url: https://www.instructables.com/HackerBox-0104-Engage/
  kind: doc
- label: "Hackerbox 0104 - Engage (#badgelife) — Jamie's Hack Shack unboxing/build video"
  url: https://www.youtube.com/watch?v=0bniLqir8wc
  kind: video
images:
  - file: assets/images/badges/dc32/alien-robot-badge/574ab4bc5a.png
    source: "https://hackerboxes.com/products/alien-robot-badge-kit"
    credit: "HackerBoxes"
    caption: "Alien Robot Badge Kit product photo"
  - file: assets/images/badges/dc32/alien-robot-badge/685e80b2c9.jpg
    source: "https://www.instructables.com/HackerBox-0104-Engage/"
    credit: "HackerBoxes / Instructables"
    caption: "Alien Robot Badge Kit build step showing the two 4x4 WS2812B LED eye modules"
contact: {}
notes:
- We will also have kits and some fully assembled at the HackerBox DC32 Vendor Table (have built this one and it does have a nice challenge concerning the soldering of wires on it).
status: released
sources:
- kind: sheet
  event: dc32
  row: 64
  updated: '2024-07-24'
- kind: url
  url: https://hackerboxes.com/products/alien-robot-badge-kit
  title: Alien Robot Badge Kit – HackerBoxes
  accessed: '2026-09-06'
  note: Confirmed price ($39), sold-out status, powered SAO port, Wi-Fi/Bluetooth support, and product photo.
- kind: url
  url: https://hackerboxes.com/products/hackerbox-0104-engage
  title: 'HackerBox #0104 - Engage – HackerBoxes'
  accessed: '2026-09-06'
  note: Confirmed the badge shipped inside the $59 HackerBox 0104 monthly box alongside other kits, and links to the Instructables guide and an unboxing video.
- kind: url
  url: https://www.instructables.com/HackerBox-0104-Engage/
  title: 'HackerBox 0104: Engage : 10 Steps - Instructables'
  accessed: '2026-09-06'
  note: 'Detailed step-by-step build guide: confirmed ESP32-C3 Supermini MCU, two 4x4 WS2812B (32 total) LED eye modules, buttons, demo Arduino sketch with a sound effect, an expanded 20-mode community sketch (HB0104_Wireless_Badge.ino), and that the box shipped on the 2024 summer solstice ahead of DEF CON 32 / Hacker Summer Camp.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Core facts confirmed directly from the maker''s own store pages and build guide. Not found: PCB/Gerber source files, a specific units-made count, and the SAO pinout count beyond the default v1.69bis assumption (the badge itself hosts one powered SAO port; no source stated it explicitly as "v1.69bis" but that is the standard 6-pin SAO used across recent HackerBoxes). Left make_your_own.hardware_url and gerbers_url empty since no PCB design files were found published, only the firmware/build guide.'
last_modified_date: '2026-09-06'
---

The Alien Robot Badge is a solder-it-yourself electronic badge that HackerBoxes shipped as the headline build in HackerBox #0104, "Engage," a monthly subscription box that went out around the summer solstice of 2024 in the run-up to DEF CON 32 and the rest of Hacker Summer Camp in Las Vegas. Its two "eyes" are 4x4 WS2812B LED matrices (32 addressable RGB LEDs total), driven by an ESP32-C3 Supermini development board wired to the badge along with a couple of buttons and a small speaker. Out of the box it runs a demo Arduino sketch with a few triggered display modes and a sound effect; HackerBoxes' Instructables guide also links an expanded community sketch, HB0104_Wireless_Badge.ino, that adds 20 display modes and more elaborate wireless-triggered behavior. It carries a powered SAO port so it can host an add-on board, and its ESP32-C3 base gives it both Wi-Fi and Bluetooth.

The badge was available two ways: bundled into the $59 HackerBox #0104 box (which also included the Galactic Power Badge Kit, three full-color SAOs, and other parts), or purchased on its own as the $39 Alien Robot Badge Kit. As of this check, the standalone kit listing on hackerboxes.com shows sold out. No PCB design files (Gerbers/schematic) were found published; the Instructables guide covers assembly and firmware only.

## Make your own

1. Follow the HackerBox 0104 Instructables guide, which walks through soldering the ESP32-C3 Supermini board, the two 4x4 WS2812B eye modules, and the buttons onto the badge PCB.
2. Flash the demo Arduino sketch from the guide for the built-in triggered display/sound modes, or use the expanded `HB0104_Wireless_Badge.ino` sketch linked from the guide for 20 display modes.
3. No separate hardware/Gerber files were located; anyone reproducing the PCB itself would need to reverse it from photos or contact HackerBoxes.
