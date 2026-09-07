---
title: SAINTCON 2024 badge (compukidmike)
id: saintcon-2024-saintcon-2024-badge-compukidmike
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: saintcon-2024
year: 2024
makers:
- name: compukidmike
  url: https://github.com/compukidmike
summary: The official SAINTCON 2024 conference badge, worn wrist-mounted rather than on a lanyard, with a touch LCD and screw-mounted "Klip-on" expansion boards.
functions: Runs a WiFi-connected badge OS on the conference network; supports IR, a touchscreen UI, and two official I2C minibadge slots on the included two-slot Klip-on. A separate 8-slot lanyard-mounted minibadge expansion board (powered over USB-C) holds additional minibadges without I2C game connectivity.
look:
  colors: []
  shape: null
  themes:
  - wearable
tech:
  mcu: ESP32-S3
  leds: null
  display: LCD with capacitive touch (parallel/I80 interface; exact size not stated)
  connectivity:
  - wifi
  - i2c
  - ir
  - usb
  battery: USB-C rechargeable with onboard charger IC (chemistry not stated)
  sao_version: null
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/compukidmike/Saintcon2024/tree/main/Hardware
  firmware_url: https://github.com/compukidmike/Saintcon2024/tree/main/Firmware
  eda_tool: KiCad
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed as the official badge to SAINTCON 2024 attendees; not sold separately as far as sources state.
links:
- label: github.com/compukidmike/Saintcon2024
  url: https://github.com/compukidmike/Saintcon2024
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/Saintcon2024
  title: SAINTCON 2024 badge (compukidmike)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''saintcon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2024/main/README.md
  title: 'Saintcon2024 README'
  accessed: '2026-09-07'
  note: Maker's own description of the wrist-mount design, Klip-on expansion boards, minibadge slots, and minibadge expansion board over USB-C power.
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2024/main/Firmware/sdkconfig.defaults
  title: Saintcon2024 firmware sdkconfig.defaults
  accessed: '2026-09-07'
  note: Confirms ESP32-S3 target, parallel-interface LCD with capacitive touch, USB-C Type-C ID/charger GPIOs, IR TX/RX, I2C peripheral bus, and conference WiFi config.
- kind: url
  url: https://github.com/compukidmike/Saintcon2024/tree/main/Hardware/Saintcon2024MainBoard
  title: Saintcon2024MainBoard hardware files
  accessed: '2026-09-07'
  note: Confirms full open-source hardware release (schematic PDF, BOM, gerbers, KiCad project) for the main badge board.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Repo is the maker''s own project page but does not state price, quantity made, LED count/type, exact display size, or battery chemistry; these are left empty rather than guessed. The two repository "images" (an engineering-drawing prop and a fake press release) are in-character joke assets for the badge''s fictional "MK Factor / Klippy-Net" theme, not photos of the real hardware, so none were saved to images:. No other photos of the finished badge were found in the repo.'
last_modified_date: '2026-09-07'
---

The SAINTCON 2024 badge, built by compukidmike for the SAINTCON badge team, departed from the usual lanyard format: it's worn wrist-mounted on a velcro sweatband (a lanyard mount was also offered), with a touchscreen LCD and a USB-C port. Under the hood it runs an ESP32-S3 with a parallel-interface capacitive-touch LCD, WiFi onto the conference network, IR, and an I2C bus for minibadges.

The badge's headline feature is a screw-mounted "Klip-on" expansion system: two 3V3/GND screws double as mounting points and a power tap for community-made add-on boards. Every badge shipped with a two-slot minibadge Klip-on (limited to two official, I2C-connected game minibadges at a time) plus a separate 8-slot minibadge expansion board that clips onto a lanyard and draws power from the badge's USB-C port, for attendees who wanted to display more minibadges than the official game supported. The badge team leaned into an in-universe joke framing the design notes as a "leaked" engineering drawing and press release from a fictional "MK Factor" wrist-communicator, rather than releasing real specs ahead of the conference.

## Make your own

The full hardware and firmware are published in the maker's GitHub repo. The `Hardware/Saintcon2024MainBoard` folder has the schematic PDF, BOM, gerbers, and KiCad project for the badge itself, and the `Klip-ons` folder has KiCad libraries, schematic symbols, and example footprints (Left/Right/Upper/Lower Klip-on outlines, plus a minibadge Klip-on example) for building compatible add-on boards. Firmware is an ESP-IDF 5.3.1 project targeting the ESP32-S3.
