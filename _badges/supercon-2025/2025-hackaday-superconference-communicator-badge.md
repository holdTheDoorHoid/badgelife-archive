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
functions: Runs a LoRa mesh chat client ("IRC, but LoRa") where attendees pick a topic on the numpad to join a channel; also supports WiFi/BLE and user-written MicroPython apps.
look:
  colors:
  - black
  shape: rectangle
  themes:
  - radio
  - retro computer
  - hardware tool
tech:
  mcu: ESP32-S3
  leds: null
  display: 2.79in IPS LCD (168x428, NV3007 controller)
  connectivity:
  - lora
  - wifi
  - bluetooth
  battery: LiPo
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ~500
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of Hackaday Supercon 9, held in Pasadena, CA, in 2025.
make_your_own:
  open_source: true
  hardware_url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  firmware_url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  eda_tool: KiCad
  license: MIT
  fab_url: null
  notes: Repo includes hardware, firmware, docs, and front-panel design files (STEP/DXF/SVG) for custom badge shells.
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
- label: Source files (GitHub)
  url: https://github.com/eosti/2025-Communicator_Badge
  kind: hardware
images:
- file: assets/images/badges/supercon-2025/2025-hackaday-superconference-communicator-badge/79db150746.png
  source: https://github.com/Hack-a-Day/2025-Communicator_Badge
  credit: Hackaday / Supplyframe Design Lab
  caption: Front of the 2025 Hackaday Supercon Communicator Badge
- file: assets/images/badges/supercon-2025/2025-hackaday-superconference-communicator-badge/3598d44e59.png
  source: https://github.com/Hack-a-Day/2025-Communicator_Badge
  credit: Hackaday / Supplyframe Design Lab
  caption: Close-up of the rear PCB and keyboard mechanism
- file: assets/images/badges/supercon-2025/2025-hackaday-superconference-communicator-badge/6884e0ba30.jpg
  source: https://hackaday.com/2025/10/23/announcing-the-2025-hackaday-superconference-communicator-badge/
  credit: Hackaday
  caption: Front of the 2025 Supercon Communicator Badge, showing the display and dome-switch keyboard
- file: assets/images/badges/supercon-2025/2025-hackaday-superconference-communicator-badge/413f64c959.png
  source: https://hackaday.com/2025/10/23/announcing-the-2025-hackaday-superconference-communicator-badge/
  credit: Hackaday
  caption: Close-up of the back of the badge showing the LoRa radio module and SMA antenna connector
- file: assets/images/badges/supercon-2025/2025-hackaday-superconference-communicator-badge/f1745ddb89.jpg
  source: https://github.com/Hack-a-Day/2025-Communicator_Badge
  credit: Hackaday
  caption: Front render of the Communicator Badge with customizable front panel
- file: assets/images/badges/supercon-2025/2025-hackaday-superconference-communicator-badge/3598d44e59.png
  source: https://github.com/Hack-a-Day/2025-Communicator_Badge
  credit: Hackaday
  caption: Close-up of the rear PCB showing the keyboard dome switches and electronics
contact: {}
notes:
- Hardware is a custom dome-switch keyboard (silicone matrix, driven through a TC8418 I2C multiplexer) inspired by vintage portable communicator devices; the radio is a Seeed SX1262 LoRa module with an SMA antenna connector. Firmware is written in MicroPython with the LVGL graphics framework.
- The Hackaday article mentions volunteers Brandon, Dave, Will, and Mike, and says future European editions of the badge are planned; not enough detail was found to add a separate maker/series entry for those.
- LED count/type not stated in the sources checked; tech.leds left empty rather than guessed.
- Two-PCB design; purely decorative front board holds keyboard membrane, made for customization
- Firmware repo also carries a "2026_hackaday_europe_image.bin", suggesting the same platform was reused for Hackaday Europe 2026; not confirmed as a separate release and not researched here.
status: released
sources:
- kind: url
  url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  title: 2025 Hackaday Superconference Communicator Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Official 2025 Supercon 9 badge; ESP32-S3, SX1262 LoRa mesh chat, 2.79in IPS LCD, retro keyboard''.'
- kind: url
  url: https://hackaday.com/2025/10/23/announcing-the-2025-hackaday-superconference-communicator-badge/
  title: Announcing the 2025 Hackaday Superconference Communicator Badge
  accessed: '2026-09-07'
  note: MCU, display, radio, keyboard, quantity (~500 units), open-source hardware confirmation, sponsors.
- kind: url
  url: https://hackaday.com/2025/10/27/the-supercon-2025-badge-is-built-to-be-customized/
  title: The Supercon 2025 Badge Is Built To Be Customized
  accessed: '2026-09-07'
  note: Two-PCB stack-up, expansion port, MicroPython firmware, customizable front panel files (STEP/DXF/SVG).
- kind: url
  url: https://raw.githubusercontent.com/Hack-a-Day/2025-Communicator_Badge/main/firmware/README.md
  title: Communicator Badge firmware README
  accessed: '2026-09-07'
  note: MicroPython + LVGL + asyncio firmware architecture; LoRa network stack with TTL-based message repeating; SAO I2C bus and onboard keyboard/display API mentioned.
- kind: url
  url: https://api.github.com/repos/Hack-a-Day/2025-Communicator_Badge/contents/documentation/datasheets
  title: Communicator Badge datasheets folder listing
  accessed: '2026-09-07'
  note: Datasheets confirm ESP32-S3-WROOM MCU, SX1262/Wio-SX1262 LoRa module, ER-TFT2.79 TFT display (NV3007 driver), TCA8418 keypad controller, and MCP73831 LiPo charge IC.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Event corrected from supercon-2026 to supercon-2025: the badge was made for and distributed at Hackaday Supercon 9, held in 2025, per both the GitHub repo and the Hackaday.com announcement articles. LED count/type and SAO header presence are not stated in the sources checked and are left empty. Price is not applicable since it was given free to attendees rather than sold; quantity (~500) is stated as approximate in the Hackaday article. Merged with duplicate entry ''Hackaday Supercon 2025 Communicator Badge'' (supercon-2025-hackaday-supercon-2025-communicator-badge). Merged with duplicate entry ''Supercon 2025 Communicator Badge'' (supercon-2025-supercon-2025-communicator-badge).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/supercon-2026/2025-hackaday-superconference-communicator-badge/
- /badges/supercon-2025/hackaday-supercon-2025-communicator-badge/
- /badges/supercon-2025/supercon-2025-communicator-badge/
model:
  file: assets/models/supercon-2025/2025-hackaday-superconference-communicator-badge.glb
  method: kicad
  source_file: hardware/communicator_pcb/communicator_pcb.kicad_pcb
  generated: '2026-09-10'
  bytes: 804792
---

The 2025 Hackaday Superconference Communicator Badge was the official badge given to attendees of Hackaday Supercon 9, held in Pasadena, CA in 2025. Rather than a typical single-purpose blinky badge, it was built as a small mesh-networking communicator: an ESP32-S3 drives a custom 2.79" IPS LCD (168x428, NV3007 controller) and an SX1262 LoRa radio, letting attendees join LoRa mesh chat channels by picking a topic on a built-in numpad — described by its creators as "IRC, but LoRa." It also carries WiFi and Bluetooth, and runs its interface in MicroPython with LVGL, so attendees could read and modify the running code on the badge itself.

The badge's most distinctive hardware feature is its keyboard: a custom dome-switch keypad with a silicone membrane, designed by Arturo182 of Solder Party, married to a retro-computer-styled two-PCB stack-up (a cosmetic front board over the working rear board). The front panel was deliberately designed to be swapped out, with STEP, DXF, and SVG files provided so attendees could mill, laser-cut, or 3D-print their own replacements. Software lead was Spaceben, with design work from Bogdan Rosu, and Hackaday credits Espressif, Seeed, and DigiKey as component sponsors. Around 500 units were made for the 2025 event, and both hardware and firmware are published under an MIT license on GitHub.

## Make your own

Full hardware (schematics/board files) and firmware are in the [GitHub repo](https://github.com/Hack-a-Day/2025-Communicator_Badge), including a `hardware/` directory, `firmware/` in MicroPython, and front-panel replacement files in STEP, DXF, and SVG formats for custom fabrication. The custom dome-switch keyboard tooling makes small-scale reproduction of an exact clone costly, but the front panel and firmware are readily hackable on their own.

## Notes merged from the duplicate entry "Hackaday Supercon 2025 Communicator Badge"

The 2025 Hackaday Superconference Communicator Badge is a LoRa mesh-networked handheld built by the Hackaday and Supplyframe Design Lab team for that year's Supercon. Rather than the blinky SAO-hosting badges of past years, it works like a walkie-talkie for text: attendees pick a topic channel on a numpad-style keyboard and send short messages that hop across nearby badges over a LoRa mesh, with the badge team using the same channel to push out conference announcements like talk times and food arrivals. The design nods to vintage handheld communicators, right down to a custom silicone dome-switch keyboard.

Under the hood it runs an ESP32-S3 (8 MB PSRAM, 16 MB flash) paired with a Seeed SX1262 LoRa radio module and SMA antenna connector, a 2.79" IPS LCD (168x428px, NV3007 controller), and a TC8418 I2C keyboard matrix controller, powered by a rechargeable LiPo cell. The firmware is MicroPython with an LVGL-based UI. Roughly 500 units were produced and given to Supercon 2025 attendees; hardware design files and firmware are published on GitHub, and the team has said further European editions of the badge are planned.

## Make your own

Hardware and firmware are open source at github.com/Hack-a-Day/2025-Communicator_Badge, organized into `documentation`, `firmware`, `hardware`, `images`, and `user_apps` directories. The repository's README was minimal at the time of this research (just a photo of the badge), so anyone rebuilding it should expect to read the source and documentation folders directly rather than follow a written guide.

## Notes merged from the duplicate entry "Supercon 2025 Communicator Badge"

The Communicator Badge was the official hardware for Hackaday Supercon 2025, held at the Hackaday HQ in Pasadena. It is a two-board handheld: a rear PCB carries an ESP32-S3 microcontroller, a 2.79-inch color TFT display, a TCA8418-driven membrane keypad, a Semtech SX1262 LoRa radio (via a Wio-SX1262 module), and a LiPo battery with USB charging, while a front board is purely mechanical — it exists to hold the keyboard membrane against the rear board's dome switches and is deliberately left blank so attendees can redesign, laser-cut, 3D-print, or CNC their own faceplate for it.

Firmware runs MicroPython with LVGL for the UI and asyncio to keep the display and keyboard responsive while a background network stack manages the LoRa radio. That stack lets badges send, receive, and repeat short messages to each other over the air using a time-to-live counter so messages propagate hop-to-hop without flooding forever, and it exposes ports that attendees could claim (via pull request) to build their own message protocols and apps on top. The badges also expose an SAO-compatible I2C bus.

Hackaday published the full hardware (KiCad) and firmware sources under the MIT license on GitHub, along with the datasheets for its major components, at github.com/Hack-a-Day/2025-Communicator_Badge. The badge was given to Supercon attendees rather than sold, and the repository shows signs the same platform was carried forward for a subsequent Hackaday Europe event, though that has not been independently confirmed.
