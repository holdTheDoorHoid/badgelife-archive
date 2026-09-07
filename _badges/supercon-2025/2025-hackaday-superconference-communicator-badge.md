---
title: 2025 Hackaday Superconference Communicator Badge
id: supercon-2025-2025-hackaday-superconference-communicator-badge
layout: badge
parent: Supercon 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2025
year: 2025
makers:
- name: 'Hackaday / Supplyframe Design Lab (keyboard: Arturo182/solder.party; software: Spaceben; design: Bogdan Rosu)'
summary: 'A mesh-networking "communicator" badge built for Hackaday Supercon 9 (2025): an ESP32-S3 with a custom IPS display, a LoRa radio, and a retro dome-switch keyboard, run in MicroPython.'
functions: 'Runs a LoRa mesh chat client ("IRC, but LoRa") where attendees pick a topic on the numpad to join a channel; also supports WiFi/BLE and user-written MicroPython apps.'
look:
  colors: [black]
  shape: rectangle
  themes: [radio, retro computer, hardware tool]
tech:
  mcu: ESP32-S3
  leds: null
  display: 2.79in IPS LCD (168x428, NV3007 controller)
  connectivity: [lora, wifi, bluetooth]
  battery: LiPo
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '~500'
  availability: free
  distribution: [free_drop]
  where: 'Given to attendees of Hackaday Supercon 9, held in Pasadena, CA, in 2025.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  firmware_url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  eda_tool: null
  license: MIT
  fab_url: null
  notes: 'Repo includes hardware, firmware, docs, and front-panel design files (STEP/DXF/SVG) for custom badge shells.'
links:
- label: github.com/Hack-a-Day/2025-Communicator_Badge
  url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  kind: repo
- label: hackaday.com/2025/10/23/announcing-the-2025-hackaday-superconference-communicator-badge
  url: https://hackaday.com/2025/10/23/announcing-the-2025-hackaday-superconference-communicator-badge/
  kind: article
- label: hackaday.com/2025/10/27/the-supercon-2025-badge-is-built-to-be-customized
  url: https://hackaday.com/2025/10/27/the-supercon-2025-badge-is-built-to-be-customized/
  kind: article
images:
  - file: assets/images/badges/supercon-2025/2025-hackaday-superconference-communicator-badge/79db150746.png
    source: "https://github.com/Hack-a-Day/2025-Communicator_Badge"
    credit: "Hackaday / Supplyframe Design Lab"
    caption: "Front of the 2025 Hackaday Supercon Communicator Badge"
  - file: assets/images/badges/supercon-2025/2025-hackaday-superconference-communicator-badge/3598d44e59.png
    source: "https://github.com/Hack-a-Day/2025-Communicator_Badge"
    credit: "Hackaday / Supplyframe Design Lab"
    caption: "Close-up of the rear PCB and keyboard mechanism"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  title: 2025 Hackaday Superconference Communicator Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Official 2025 Supercon 9 badge; ESP32-S3, SX1262 LoRa mesh chat, 2.79in IPS LCD, retro keyboard''.'
- kind: url
  url: https://hackaday.com/2025/10/23/announcing-the-2025-hackaday-superconference-communicator-badge/
  title: 'Announcing the 2025 Hackaday Superconference Communicator Badge'
  accessed: '2026-09-07'
  note: 'MCU, display, radio, keyboard, quantity (~500 units), open-source hardware confirmation, sponsors.'
- kind: url
  url: https://hackaday.com/2025/10/27/the-supercon-2025-badge-is-built-to-be-customized/
  title: 'The Supercon 2025 Badge Is Built To Be Customized'
  accessed: '2026-09-07'
  note: 'Two-PCB stack-up, expansion port, MicroPython firmware, customizable front panel files (STEP/DXF/SVG).'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Event corrected from supercon-2026 to supercon-2025: the badge was made for and distributed at Hackaday Supercon 9, held in 2025, per both the GitHub repo and the Hackaday.com announcement articles. LED count/type and SAO header presence are not stated in the sources checked and are left empty. Price is not applicable since it was given free to attendees rather than sold; quantity (~500) is stated as approximate in the Hackaday article.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2026/2025-hackaday-superconference-communicator-badge/
---

The 2025 Hackaday Superconference Communicator Badge was the official badge given to attendees of Hackaday Supercon 9, held in Pasadena, CA in 2025. Rather than a typical single-purpose blinky badge, it was built as a small mesh-networking communicator: an ESP32-S3 drives a custom 2.79" IPS LCD (168x428, NV3007 controller) and an SX1262 LoRa radio, letting attendees join LoRa mesh chat channels by picking a topic on a built-in numpad — described by its creators as "IRC, but LoRa." It also carries WiFi and Bluetooth, and runs its interface in MicroPython with LVGL, so attendees could read and modify the running code on the badge itself.

The badge's most distinctive hardware feature is its keyboard: a custom dome-switch keypad with a silicone membrane, designed by Arturo182 of Solder Party, married to a retro-computer-styled two-PCB stack-up (a cosmetic front board over the working rear board). The front panel was deliberately designed to be swapped out, with STEP, DXF, and SVG files provided so attendees could mill, laser-cut, or 3D-print their own replacements. Software lead was Spaceben, with design work from Bogdan Rosu, and Hackaday credits Espressif, Seeed, and DigiKey as component sponsors. Around 500 units were made for the 2025 event, and both hardware and firmware are published under an MIT license on GitHub.

## Make your own

Full hardware (schematics/board files) and firmware are in the [GitHub repo](https://github.com/Hack-a-Day/2025-Communicator_Badge), including a `hardware/` directory, `firmware/` in MicroPython, and front-panel replacement files in STEP, DXF, and SVG formats for custom fabrication. The custom dome-switch keyboard tooling makes small-scale reproduction of an exact clone costly, but the front panel and firmware are readily hackable on their own.
