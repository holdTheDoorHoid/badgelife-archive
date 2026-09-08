---
title: Fri3d Camp 2026 Badge
id: fri3d-2026-fri3d-camp-2026-badge
layout: badge
parent: Fri3d Camp 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: fri3d-2026
year: 2026
makers:
- name: Fri3d Camp
summary: Open-hardware conference badge for Fri3d Camp 2026, built around an ESP32-S3 with a 2-inch touchscreen and a secondary CH32X035 microcontroller for extra I/O.
functions: Runs MicroPythonOS (apps written in MicroPython) with a Retro-Go game partition; connects to official add-ons (Communicator, DJ Controller, ToF Add-on, LoRa Expansion) and to the 2022/2024 blaster toys via an expansion connector.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: ESP32-S3-WROOM-1-N16R8
  leds: null
  display: 2" IPS LCD touchscreen
  connectivity:
  - wifi
  - bluetooth
  - lora
  battery: LiPo 2000 mAh
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Given to every Fri3d Camp 2026 attendee; not sold separately as far as sources show.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Fri3dCamp/badge_2026_hw
  firmware_url: https://github.com/Fri3dCamp/badge_firmware_MicroPythonOS
  eda_tool: null
links:
- label: github.com/Fri3dCamp/badge_2026_hw
  url: https://github.com/Fri3dCamp/badge_2026_hw
  kind: repo
- label: github.com/Fri3dCamp/badge_firmware_MicroPythonOS
  url: https://github.com/Fri3dCamp/badge_firmware_MicroPythonOS
  kind: repo
- label: fri3dcamp.github.io/badge_2026
  url: https://fri3dcamp.github.io/badge_2026/en/
  kind: doc
- label: fri3d.be/en/badge
  url: https://fri3d.be/en/badge/
  kind: website
images:
- file: assets/images/badges/fri3d-2026/fri3d-camp-2026-badge/1d3cbea340.png
  source: "https://github.com/Fri3dCamp/badge_2026_hw"
  credit: "Fri3d Camp"
  caption: "Fri3d Camp 2026 badge, front"
- file: assets/images/badges/fri3d-2026/fri3d-camp-2026-badge/1d44a42599.png
  source: "https://github.com/Fri3dCamp/badge_2026_hw"
  credit: "Fri3d Camp"
  caption: "Fri3d Camp 2026 badge, back"
contact: {}
notes:
- Open-hardware ESP32-S3 maker badge for Fri3d Camp's sixth edition (14-16 Aug 2026) with 2-inch IPS touchscreen, 6-axis IMU, LoRa option and MicroPythonOS firmware. Found by the event-year sweep, task fri3d.
status: released
sources:
- kind: url
  url: https://github.com/Fri3dCamp/badge_2026_hw
  title: Fri3d Camp 2026 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:fri3d); event read as ''fri3d-2026''.'
- kind: url
  url: https://raw.githubusercontent.com/Fri3dCamp/badge_2026_hw/main/README.md
  title: Fri3dCamp/badge_2026_hw README
  accessed: '2026-09-08'
  note: 'Confirmed MCU (ESP32-S3-WROOM-1-N16R8), display, IMU, buttons/joystick, microSD, audio jack, secondary CH32X035 controller, optional LoRa module, 2000mAh LiPo battery, TP4056 charging, SAO header (v1.69bis), and expansion connector for 2022/2024 blaster add-ons.'
- kind: url
  url: https://github.com/Fri3dCamp/badge_firmware_MicroPythonOS
  title: Fri3d Camp Badge firmware based on MicroPythonOS
  accessed: '2026-09-08'
  note: 'Confirms firmware is MicroPythonOS with a Retro-Go gaming partition, shared with the 2024 badge.'
- kind: url
  url: https://fri3d.be/en/badge/
  title: 'Badge 2026 | Fri3d Camp 2026'
  accessed: '2026-09-08'
  note: 'Confirms every Fri3d Camp 2026 participant receives the badge; no price, quantity or non-attendee availability stated.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Price, quantity produced, and whether it is ever sold to non-attendees were not stated anywhere found; left empty. tech.leds left null — no onboard addressable LEDs mentioned in the hardware README (only buttons/buzzer/joystick). eda_tool not stated in the repo docs checked.'
last_modified_date: '2026-09-08'
---

The Fri3d Camp 2026 badge is the sixth main badge produced by Fri3d Camp, the Belgian hacker/maker camp, for its August 2026 event. It is built around an Espressif ESP32-S3-WROOM-1-N16R8 module (dual-core Xtensa LX7 at 240MHz, 16MB flash, 8MB PSRAM) with built-in Wi-Fi and Bluetooth 5, which removes the need for the separate USB-serial bridge chip earlier Fri3d badges required. A 2-inch IPS touchscreen LCD is the main display, backed by a 6-axis IMU, a joystick, multiple push buttons, a buzzer, a microSD slot, a 3.5mm TRRS audio jack, and a secondary CH32X035 microcontroller that handles extra I/O. Power comes from a 2000mAh LiPo cell charged over USB-C via a TP4056 charger, with a second regulator letting the Wi-Fi radio be power-gated separately to save battery.

The badge carries a v1.69bis (6-pin) SAO header plus a small bottom expansion connector for experimentation, and is electrically compatible with Fri3d's earlier "blaster" toys from the 2022 and 2024 camps. Hardware design files (schematics, production data, and 3D models, including a community-contributed joystick shroud) are published under an open license on GitHub. Firmware is MicroPythonOS, a MicroPython-based lightweight OS shared with the 2024 badge, bundled with a Retro-Go partition for games; applications are written in MicroPython.

Every Fri3d Camp 2026 attendee receives one of these badges as part of the event; none of the sources checked state a standalone price, total quantity produced, or whether units are ever sold outside camp attendance.

## Make your own

Hardware design files, schematics, and production data are in [Fri3dCamp/badge_2026_hw](https://github.com/Fri3dCamp/badge_2026_hw). Firmware source is in [Fri3dCamp/badge_firmware_MicroPythonOS](https://github.com/Fri3dCamp/badge_firmware_MicroPythonOS), and programming documentation (writing MicroPython apps for the badge) is at [fri3dcamp.github.io/badge_2026](https://fri3dcamp.github.io/badge_2026/en/).
