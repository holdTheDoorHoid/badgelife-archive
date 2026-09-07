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
summary: A solder-it-yourself alien-robot badge from HackerBox
functions: Runs a demo Arduino sketch with three button-triggered display modes for the eye LEDs, one with buzzer sound effects; an expanded sketch from HackerBoxes (HB0104_Wireless_Badge.ino) adds 20 display modes and lets modes be triggered wirelessly from another badge over ESP-NOW.
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
  battery: 3x AA battery pack (batteries not included) or USB-C via the ESP32-C3 Supermini; USB/BAT switch
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
  where: Sold by HackerBoxes as a standalone kit and as the featured badge project in the HackerBox
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://www.instructables.com/HackerBox-0104-Engage/
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: The Instructables build guide (CC BY-NC-SA) includes the demo Arduino sketch and an attached expanded sketch (HB0104_Wireless_Badge.ino) with 20 display modes and ESP-NOW wireless triggering; no PCB source/Gerbers were found published.
links:
- label: hackerboxes.com/collections/past-hackerboxes/products/hackerbox-0104-engage
  url: https://hackerboxes.com/collections/past-hackerboxes/products/hackerbox-0104-engage
  kind: store
- label: www.hackerboxes.com
  url: https://www.hackerboxes.com
  kind: store
  archived: https://web.archive.org/web/20260523221904/https://hackerboxes.com/
- label: Alien Robot Badge Kit (standalone product page)
  url: https://hackerboxes.com/products/alien-robot-badge-kit
  kind: store
- label: 'HackerBox 0104: Engage — Instructables build guide'
  url: https://www.instructables.com/HackerBox-0104-Engage/
  kind: doc
  archived: https://web.archive.org/web/20260606133950/https://www.instructables.com/HackerBox-0104-Engage/
- label: Hackerbox 0104 - Engage (#badgelife) — Jamie's Hack Shack unboxing/build video
  url: https://www.youtube.com/watch?v=0bniLqir8wc
  kind: video
images:
- file: assets/images/badges/dc32/alien-robot-badge/574ab4bc5a.png
  source: https://hackerboxes.com/products/alien-robot-badge-kit
  credit: HackerBoxes
  caption: Alien Robot Badge Kit product photo
- file: assets/images/badges/dc32/alien-robot-badge/685e80b2c9.jpg
  source: https://www.instructables.com/HackerBox-0104-Engage/
  credit: HackerBoxes / Instructables
  caption: Alien Robot Badge Kit build step showing the two 4x4 WS2812B LED eye modules
  archived: https://web.archive.org/web/20260606133950/https://www.instructables.com/HackerBox-0104-Engage/
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
  note: Confirmed the badge shipped inside the $59 HackerBox 0104 monthly box alongside the Galactic Power Badge Kit, four SAOs and other parts, and links to the Instructables guide and an unboxing video.
- kind: url
  url: https://www.instructables.com/HackerBox-0104-Engage/
  title: 'HackerBox 0104: Engage : 10 Steps - Instructables'
  accessed: '2026-09-06'
  note: 'Detailed step-by-step build guide: confirmed ESP32-C3 Supermini MCU, two 4x4 WS2812B (32 total) LED eye modules, buttons, demo sketch with three display modes including sound effects, an attached 20-mode HB0104_Wireless_Badge.ino sketch with ESP-NOW wireless triggering, a 2x3 (6-pin) SAO header, a 3x AA battery pack with boost converter and USB/BAT switch (battery pack visible in the guide''s photos), and that the box shipped on the 2024 summer solstice ahead of DEF CON 32 / Hacker Summer Camp.'
  archived: https://web.archive.org/web/20260606133950/https://www.instructables.com/HackerBox-0104-Engage/
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Verified 2026-09-07 against the maker''s store pages, the Instructables guide (via its JSON API; the HTML page is JS-rendered) and the YouTube oEmbed title. Not found: PCB/Gerber source files or a units-made count. SAO header is a 2x3 (6-pin) female header per the guide; recorded as v1.69bis on that basis. Battery count (3x AA) is from the maker''s product photos; the guide text only says "battery pack". Fact-check corrections: battery was wrongly "powered by host badge"; the demo sketch has three modes (not "multiple"); the 20-mode sketch is attached by HackerBoxes, not a community sketch; the box held four SAOs, not three.'
last_modified_date: '2026-09-07'
---

The Alien Robot Badge is a solder-it-yourself electronic badge that HackerBoxes shipped as the headline build in HackerBox #0104, "Engage," a monthly subscription box that went out around the summer solstice of 2024 in the run-up to DEF CON 32 and the rest of Hacker Summer Camp in Las Vegas. Its two "eyes" are 4x4 WS2812B LED matrices (32 addressable RGB LEDs total), driven by an ESP32-C3 Supermini development board soldered to the badge along with two buttons, a buzzer, a DC/DC boost converter and a 3x AA battery pack (with a USB/BAT switch). Out of the box it runs a demo Arduino sketch with three button-triggered display modes, one with sound effects; HackerBoxes' Instructables guide also attaches an expanded sketch, HB0104_Wireless_Badge.ino, that adds 20 display modes and lets modes be triggered wirelessly from another badge over ESP-NOW. It carries a powered 2x3 SAO header so it can host an add-on board, and its ESP32-C3 base gives it both Wi-Fi and Bluetooth.

The badge was available two ways: bundled into the $59 HackerBox #0104 box (which also included the Galactic Power Badge Kit, four SAOs, and other parts), or purchased on its own as the $39 Alien Robot Badge Kit. As of this check, the standalone kit listing on hackerboxes.com shows sold out. No PCB design files (Gerbers/schematic) were found published; the Instructables guide covers assembly and firmware only.

## Make your own

1. Follow the HackerBox 0104 Instructables guide, which walks through forming 1 cm wire leads on the two 4x4 WS2812B eye modules, then soldering the modules, two buttons, power switch, buzzer, ESP32-C3 Supermini, boost converter (set to 5V), battery pack and SAO header onto the badge PCB.
2. Flash the demo Arduino sketch from the guide for the three built-in display/sound modes, or use the expanded `HB0104_Wireless_Badge.ino` sketch attached to the guide for 20 display modes and ESP-NOW wireless triggering.
3. No separate hardware/Gerber files were located; the guide covers assembly and firmware only.
