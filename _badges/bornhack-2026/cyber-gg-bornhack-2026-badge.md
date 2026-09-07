---
title: Cyber Ægg (Bornhack 2026 badge)
id: bornhack-2026-cyber-gg-bornhack-2026-badge
layout: badge
parent: Bornhack 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bornhack-2026
year: 2026
makers:
- name: Badge.Team
  url: https://badge.team/
summary: 'An egg-shaped, low-power LoRa mesh badge for BornHack 2026 with a tri-color e-paper screen and a Tamagotchi-style virtual pet game.'
functions: 'BornPets virtual pet with mini-games; LoRa mesh chat/networking via MeshCore; NFC tag; joystick-driven menu navigation; alternative firmware (Community Edition, a DOOM port, CircuitPython).'
look:
  colors: [black, red, white]
  shape: egg
  themes: [village badge, radio, retro computer, meme]
tech:
  mcu: nRF52840
  leds:
    count: 3
    type: discrete
    note: 'Three separate RGB (blue/red/green) status LEDs, active-low GPIO, per the hardware repo pinout table.'
  display: 1.54" tri-color e-paper (152x152)
  connectivity: [ble, lora, nfc, i2c, usb]
  inputs: [joystick]
  battery: 'rechargeable via USB-C; one charge lasts a full BornHack camp (about a week)'
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://codeberg.org/Ranzbak/bornhack2026-hardware
  firmware_url: https://codeberg.org/Ranzbak/bornhack-firmware-2026
  eda_tool: KiCad
links:
- label: badge.team/docs/badges/bornhack-2026
  url: https://badge.team/docs/badges/bornhack-2026/
  kind: website
  archived: https://web.archive.org/web/20260717235018/https://badge.team/docs/badges/bornhack-2026/
- label: bornhack2026-hardware (Codeberg)
  url: https://codeberg.org/Ranzbak/bornhack2026-hardware
  kind: repo
  archived: null
- label: bornhack-firmware-2026 (Codeberg)
  url: https://codeberg.org/Ranzbak/bornhack-firmware-2026
  kind: repo
  archived: null
images:
- file: assets/images/badges/bornhack-2026/cyber-gg-bornhack-2026-badge/48934658b4.jpg
  source: "https://badge.team/docs/badges/bornhack-2026/"
  credit: "Badge.Team"
  caption: "Cyber Ægg badge, front view"
- file: assets/images/badges/bornhack-2026/cyber-gg-bornhack-2026-badge/b40f328897.jpg
  source: "https://badge.team/docs/badges/bornhack-2026/"
  credit: "Badge.Team"
  caption: "Cyber Ægg badge, back view"
contact: {}
notes:
- Egg-shaped low-power badge, nRF52840, 1.54in tri-color e-paper, SX1262 LoRa mesh, BLE app, NFC tag, virtual pet 'BornPets' game.
status: listed
sources:
- kind: url
  url: https://badge.team/docs/badges/bornhack-2026/
  title: Cyber Ægg (Bornhack 2026 badge)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''BornHack 2026''.'
  archived: https://web.archive.org/web/20260717235018/https://badge.team/docs/badges/bornhack-2026/
- kind: url
  url: https://codeberg.org/Ranzbak/bornhack2026-hardware
  title: bornhack2026-hardware (Codeberg)
  accessed: '2026-09-07'
  note: 'Hardware repo README: LoRa/BLE/NFC connectivity, joystick input, three discrete RGB LEDs, QWIIC I2C port; design marked BETA/prototype stage one.'
- kind: url
  url: https://codeberg.org/Ranzbak/bornhack-firmware-2026
  title: bornhack-firmware-2026 (Codeberg)
  accessed: '2026-09-07'
  note: 'Firmware repo (Rust/Embassy) confirming open-source firmware for the badge.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own docs and hardware/firmware repos confirm the core design. Price, quantity made, and sale/distribution status were not stated anywhere found; the hardware repo describes the design as still BETA/prototype stage one as of the pages checked, so final production numbers may not exist yet. LED note is inferred from the hardware repo''s pinout table (three separate RGB-color LEDs), not an explicit LED count statement by the maker, so recorded with medium confidence.'
last_modified_date: '2026-09-07'
---

The Cyber Ægg is BornHack 2026's official badge, designed by Badge.Team with an egg-shaped shell that nods to 1990s Tamagotchi virtual pets. It runs on a Nordic nRF52840, driving a 1.54-inch tri-color (black/red/white) e-paper display and a 5-way joystick with select/execute/cancel buttons. Onboard radios include Bluetooth Low Energy, an NFC tag, and a Semtech SX1262 LoRa chip used for mesh networking over MeshCore, letting badges talk to each other and relay messages across the camp without infrastructure. A rechargeable battery, topped up over USB-C, is meant to last a full week-long BornHack event on one charge.

The signature software feature is BornPets, a virtual-pet game with mini-games built around the egg form factor, though the badge also supports alternative firmware including a Community Edition, a DOOM port, and CircuitPython. Both the hardware (KiCad) and firmware (Rust, built on the Embassy async framework) are published on Codeberg under Ranzbak's account, and the hardware repo describes the board as still in "prototype stage one" and marked BETA, with antenna performance not yet validated at the time these sources were checked.

## Make your own

Hardware design files (KiCad) are at the `bornhack2026-hardware` repo on Codeberg, and firmware source (Rust/Embassy) is at `bornhack-firmware-2026`, also on Codeberg. No separate BOM or Gerber-only share link was found; the KiCad project itself is the hardware source.
