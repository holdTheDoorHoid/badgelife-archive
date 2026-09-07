---
title: Fri3d Camp 2024 Badge
id: fri3d-2024-fri3d-camp-2024-badge
layout: badge
parent: Fri3D 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: fri3d-2024
year: 2024
makers:
- name: Fri3d Camp
  url: https://fri3d.be/badge/2024/
summary: The badge given to every participant at Fri3d Camp 2024, an ESP32-S3 board with a 2" IPS touchscreen, programmable in MicroPython or Arduino and expandable with SAO and custom add-ons.
functions: 'Runs the standard MicroPython firmware (an Arduino firmware is also available); supports custom apps/games via its screen, joystick and buttons; expandable with add-on boards such as the Big Flamingo Gun blaster and the Communicator.'
look:
  colors: []
  shape: rectangle
  themes:
  - village badge
  - hardware tool
tech:
  mcu: ESP32-S3-WROOM-1-N16R8
  leds: null
  display: 2" IPS LCD (QT020JA001-A0, rounded corners)
  connectivity:
  - wifi
  - bluetooth
  battery: LiPo 2000 mAh
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to every registered participant of Fri3d Camp 2024.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Fri3dCamp/badge_2024_hw
  firmware_url: https://github.com/Fri3dCamp/badge_2024_micropython
  eda_tool: null
  license: Apache-2.0
links:
- label: fri3d.be/badge/2024
  url: https://fri3d.be/badge/2024/
  kind: website
- label: Badge 2024 documentation
  url: https://fri3dcamp.github.io/badge_2024/
  kind: doc
- label: badge_2024_hw (hardware design files)
  url: https://github.com/Fri3dCamp/badge_2024_hw
  kind: repo
- label: badge_2024_micropython (standard firmware)
  url: https://github.com/Fri3dCamp/badge_2024_micropython
  kind: repo
- label: badge_2024_arduino (Arduino firmware)
  url: https://github.com/Fri3dCamp/badge_2024_arduino
  kind: repo
- label: blaster_2024 (Big Flamingo Gun add-on)
  url: https://github.com/Fri3dCamp/blaster_2024
  kind: repo
- label: communicator_2024 (Communicator add-on)
  url: https://github.com/Fri3dCamp/communicator_2024
  kind: repo
images:
- file: assets/images/badges/fri3d-2024/fri3d-camp-2024-badge/ecd4763899.jpg
  source: "https://fri3d.be/badge/2024/"
  credit: "Fri3d Camp"
  caption: "Fri3d Camp 2024 badge with 2 inch IPS display"
contact: {}
notes:
- Screen-equipped programmable badge (MicroPython/Arduino); add-ons include Big Flamingo Gun blaster and Communicator module.
status: released
sources:
- kind: url
  url: https://fri3d.be/badge/2024/
  title: Fri3d Camp 2024 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''Fri3d Camp 2024''.'
- kind: url
  url: https://fri3dcamp.github.io/badge_2024/
  title: Fri3d Camp 2024 Badge documentation
  accessed: '2026-09-07'
  note: 'Confirmed doc hub lists Badge 2024, Flamingo blaster, Noisy Cricket, and Communicator boards; did not itself carry detailed specs.'
- kind: url
  url: https://github.com/Fri3dCamp/badge_2024_hw
  title: Fri3dCamp/badge_2024_hw
  accessed: '2026-09-07'
  note: 'Hardware README: ESP32-S3-WROOM-1-N16R8 MCU, 2" IPS LCD (QT020JA001-A0), 6-axis IMU (WSEN-ISDS), joystick and push buttons, buzzer, Wi-Fi/Bluetooth 5, USB-C (no separate bridge), microSD reader, 2000 mAh LiPo with TP4056 charger, SAO header plus a custom expansion connector, Apache-2.0 license.'
- kind: url
  url: https://github.com/Fri3dCamp/badge_2024_micropython
  title: Fri3dCamp/badge_2024_micropython
  accessed: '2026-09-07'
  note: 'Standard firmware shipped on the badge, referenced from the badge page.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker-published pages (fri3d.be and the Fri3dCamp GitHub org) confirm the core hardware/firmware facts. Price and production quantity are not published anywhere found; the badge is given free to every registered camp participant rather than sold, so no price applies. LED count/type not stated in the hardware README excerpt available; left empty rather than guessed.'
last_modified_date: '2026-09-07'
---

The Fri3d Camp 2024 badge is the electronic badge every registered participant of the Belgian family-friendly hacker camp Fri3d Camp received that year. It is built around an Espressif ESP32-S3-WROOM-1-N16R8 module (16 MB flash, 8 MB PSRAM) driving a 2" rounded-corner IPS LCD, with a 6-axis IMU, joystick, push buttons and a buzzer for onboard interaction. It connects over Wi-Fi and Bluetooth 5, charges over USB-C via a TP4056 charger into a 2000 mAh LiPo cell, and carries both a standard SAO header and a custom expansion connector on the bottom edge for hardware add-ons.

Out of the box the badge runs a MicroPython firmware maintained by Fri3d Camp, with an alternative Arduino firmware also published for people who prefer that toolchain. Hardware design files, schematics and production data are open (Apache-2.0) on the Fri3dCamp GitHub organization, alongside two dedicated expansion projects released for the same event: the "Big Flamingo Gun" blaster add-on and a "Communicator" module, both with their own repositories.

Sources found during this pass did not state a retail price, a production quantity, or LED count/type, and it appears the badge was not sold separately but distributed free with camp registration; those fields are left empty rather than guessed.

## Make your own

Hardware design files and production data are in [badge_2024_hw](https://github.com/Fri3dCamp/badge_2024_hw). The standard firmware is [badge_2024_micropython](https://github.com/Fri3dCamp/badge_2024_micropython), with an [Arduino build](https://github.com/Fri3dCamp/badge_2024_arduino) also available. The two 2024 add-ons ([blaster_2024](https://github.com/Fri3dCamp/blaster_2024), [communicator_2024](https://github.com/Fri3dCamp/communicator_2024)) each have their own repositories with their own hardware/firmware.
