---
title: Hackaday Supercon 2025 Communicator Badge
id: supercon-2025-hackaday-supercon-2025-communicator-badge
layout: badge
parent: Supercon 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2025
year: 2025
makers:
- name: Hackaday / Supplyframe Design Lab
  url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  role: hardware and firmware team, with community contributors Arturo182 (keyboard design) and Spaceben (software)
summary: 'The official badge for the 2025 Hackaday Superconference: a LoRa mesh-networked handheld that lets attendees text each other on topic channels, described by its makers as "IRC, but LoRa."'
functions: 'Badge-to-badge text chat over a LoRa mesh, with numpad-style channel selection; relays nearby badge traffic; also used to broadcast conference info such as talk schedules and food arrivals.'
look:
  colors: []
  shape: null
  themes:
  - radio
  - retro computer
tech:
  mcu: ESP32-S3 (8 MB PSRAM, 16 MB flash)
  leds: null
  display: 2.79" IPS LCD, 168x428px, NV3007 controller
  connectivity:
  - lora
  battery: LiPo with onboard charging
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'approximately 500'
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of the 2025 Hackaday Superconference
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  firmware_url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  eda_tool: null
links:
- label: hackaday.com/2025/10/23/announcing-the-2025-hackaday-superconference-communicator-badge
  url: https://hackaday.com/2025/10/23/announcing-the-2025-hackaday-superconference-communicator-badge/
  kind: article
- label: github.com/Hack-a-Day/2025-Communicator_Badge
  url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  kind: repo
images:
  - file: assets/images/badges/supercon-2025/hackaday-supercon-2025-communicator-badge/6884e0ba30.jpg
    source: "https://hackaday.com/2025/10/23/announcing-the-2025-hackaday-superconference-communicator-badge/"
    credit: "Hackaday"
    caption: "Front of the 2025 Supercon Communicator Badge, showing the display and dome-switch keyboard"
  - file: assets/images/badges/supercon-2025/hackaday-supercon-2025-communicator-badge/413f64c959.png
    source: "https://hackaday.com/2025/10/23/announcing-the-2025-hackaday-superconference-communicator-badge/"
    credit: "Hackaday"
    caption: "Close-up of the back of the badge showing the LoRa radio module and SMA antenna connector"
contact: {}
notes:
- 'Hardware is a custom dome-switch keyboard (silicone matrix, driven through a TC8418 I2C multiplexer) inspired by vintage portable communicator devices; the radio is a Seeed SX1262 LoRa module with an SMA antenna connector. Firmware is written in MicroPython with the LVGL graphics framework.'
- 'The Hackaday article mentions volunteers Brandon, Dave, Will, and Mike, and says future European editions of the badge are planned; not enough detail was found to add a separate maker/series entry for those.'
- 'LED count/type not stated in the sources checked; tech.leds left empty rather than guessed.'
status: released
sources:
- kind: url
  url: https://hackaday.com/2025/10/23/announcing-the-2025-hackaday-superconference-communicator-badge/
  title: Hackaday Supercon 2025 Communicator Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: official-badges); event read as ''Hackaday Supercon 2025''.'
- kind: url
  url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  title: 'Hack-a-Day/2025-Communicator_Badge (GitHub)'
  accessed: '2026-09-07'
  note: 'Official hardware/firmware repo; confirms open-source status (documentation, firmware, hardware, images, user_apps folders) and provided the badge photo filename referenced in the README.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, event, MCU, display, radio, battery, distribution) confirmed via the Hackaday announcement article and the maker''s own GitHub repo. Price/cost not stated anywhere found (badge was given to attendees, likely bundled with conference admission rather than separately priced). LED details and a hackaday.io project page were not found.'
last_modified_date: '2026-09-07'
---

The 2025 Hackaday Superconference Communicator Badge is a LoRa mesh-networked handheld built by the Hackaday and Supplyframe Design Lab team for that year's Supercon. Rather than the blinky SAO-hosting badges of past years, it works like a walkie-talkie for text: attendees pick a topic channel on a numpad-style keyboard and send short messages that hop across nearby badges over a LoRa mesh, with the badge team using the same channel to push out conference announcements like talk times and food arrivals. The design nods to vintage handheld communicators, right down to a custom silicone dome-switch keyboard.

Under the hood it runs an ESP32-S3 (8 MB PSRAM, 16 MB flash) paired with a Seeed SX1262 LoRa radio module and SMA antenna connector, a 2.79" IPS LCD (168x428px, NV3007 controller), and a TC8418 I2C keyboard matrix controller, powered by a rechargeable LiPo cell. The firmware is MicroPython with an LVGL-based UI. Roughly 500 units were produced and given to Supercon 2025 attendees; hardware design files and firmware are published on GitHub, and the team has said further European editions of the badge are planned.

## Make your own

Hardware and firmware are open source at github.com/Hack-a-Day/2025-Communicator_Badge, organized into `documentation`, `firmware`, `hardware`, `images`, and `user_apps` directories. The repository's README was minimal at the time of this research (just a photo of the badge), so anyone rebuilding it should expect to read the source and documentation folders directly rather than follow a written guide.
