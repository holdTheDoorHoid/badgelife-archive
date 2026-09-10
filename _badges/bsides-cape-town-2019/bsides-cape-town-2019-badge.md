---
title: BSides Cape Town 2019 badge
id: bsides-cape-town-2019-bsides-cape-town-2019-badge
layout: badge
parent: BSides Cape Town 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-cape-town-2019
year: 2019
makers:
- name: Tony Mobily
  url: https://tonym128.github.io/
  role: hardware/firmware
- name: Mike Davis (elasticninja)
  role: collaborator
summary: 'ESP32-based electronic badge made for BSides Cape Town 2019, with a color touchscreen and onboard games.'
functions: 'Runs a small game engine with several playable games (asteroids, pong, a raycaster), WiFi scanning, a Bluetooth HID gamepad mode, and QR code generation.'
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
tech:
  mcu: ESP32-WROOM-32U
  leds: null
  display: 1.3" 240x240 IPS color touchscreen
  connectivity:
  - wifi
  - bluetooth
  battery: 18650 Li-ion (~2800mAh)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: 'Given out as conference badge/swag to BSides Cape Town 2019 attendees.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/tonym128/BSidesCPT2019-Firmware
  eda_tool: null
  notes: 'Firmware repo is public under GPL-3.0 (Arduino/ESP32 + TFT_eSPI). No hardware/PCB/gerber repo was found, only photos of the board in the maker''s write-up.'
links:
- label: www.8bitresearch.co.za/re-purposed-bsides-cape-town-badge.html
  url: https://www.8bitresearch.co.za/re-purposed-bsides-cape-town-badge.html
  kind: website
- label: 'Making a Badge (tonym128.github.io)'
  url: https://tonym128.github.io/2019/12/15/making-a-badge.html
  kind: article
- label: 'BSidesCPT2019-Firmware (GitHub)'
  url: https://github.com/tonym128/BSidesCPT2019-Firmware
  kind: repo
images:
  - file: assets/images/badges/bsides-cape-town-2019/bsides-cape-town-2019-badge/1ad3c5c3b3.jpg
    source: "https://tonym128.github.io/2019/12/15/making-a-badge.html"
    credit: "Tony Mobily"
    caption: "The assembled BSides Cape Town 2019 badge"
  - file: assets/images/badges/bsides-cape-town-2019/bsides-cape-town-2019-badge/1e706451c2.jpg
    source: "https://tonym128.github.io/2019/12/15/making-a-badge.html"
    credit: "Tony Mobily"
    caption: "The badge's custom PCB"
contact: {}
notes:
- ESP32-WROOM-32U conference badge with a 1.3" 240x240 IPS colour touch display and 18650 battery, later repurposed by a hobbyist to run the C# NanoFramework. Found by the event-year sweep, task bsides-bsides-cape-town.
- The sweep's title matched the maker's own naming; no correction needed.
status: released
sources:
- kind: url
  url: https://www.8bitresearch.co.za/re-purposed-bsides-cape-town-badge.html
  title: BSides Cape Town 2019 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-cape-town); event read as ''BSides Cape Town 2019''.'
- kind: url
  url: https://tonym128.github.io/2019/12/15/making-a-badge.html
  title: 'Making a Badge'
  accessed: '2026-09-10'
  note: 'Maker''s own write-up: identifies makers, ESP32 dual-core MCU, 1.3in 240x240 IPS display, 18650 battery, custom PCB, 3D-printed case, WiFi/Bluetooth. Source of both saved photos.'
- kind: url
  url: https://github.com/tonym128/BSidesCPT2019-Firmware
  title: 'BSidesCPT2019-Firmware'
  accessed: '2026-09-10'
  note: 'Firmware repository, GPL-3.0, ESP32 Dev Module + TFT_eSPI target; confirms open firmware and lists onboard games/features.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Core facts (MCU, display, battery, open firmware) confirmed on the maker''s own site and GitHub repo. Could not find a hardware/PCB repo, price, production quantity, or LED info; no complete-badge photo beyond the two saved here. Left get_one.price/quantity and tech.leds empty rather than guess.'
last_modified_date: '2026-09-10'
---

The BSides Cape Town 2019 badge was designed and built by Tony Mobily (tonym128), with collaborator Mike Davis ("elasticninja"), as the conference badge for BSides Cape Town's 2019 event. It is built around an ESP32-WROOM-32U module driving a 1.3" 240x240 IPS colour touchscreen, powered by a single 18650 lithium cell, and housed in a custom PCB with a 3D-printed case. Onboard software includes a small platform-agnostic game engine (with games like asteroids, pong, and a raycaster), WiFi scanning, a Bluetooth HID gamepad mode, and QR code generation.

The firmware is open source (GPL-3.0) and published on GitHub, built for the Arduino IDE/ESP32 toolchain with the TFT_eSPI library; no separate hardware/PCB repository was located. In late 2026, a hobbyist wrote up repurposing a 2019 badge to run the C# .NET NanoFramework instead of its original firmware, which is how this entry was first flagged by the archive's discovery sweep.
