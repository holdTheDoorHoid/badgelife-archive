---
title: ToadSec Badge RootedCON
id: rootedcon-2025-toadsec-badge-rootedcon
layout: badge
parent: RootedCON Madrid 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rootedcon-2025
year: 2025
makers:
- name: Toad Security
  url: https://blog.toadsec.io
  role: writeup/firmware (Alejandro Torres / "Snoody")
- name: Snoody
  role: PCB design
summary: A DIY ESP32-based 2.4GHz wireless-attack badge from the Toad Security blog, built for RootedCON, using three nRF24L01+PA+LNA modules to jam and spam WiFi, Bluetooth, BLE, RC and IoT devices.
functions: 'Generates interference/jamming across 2.4GHz WiFi, Bluetooth, BLE, RC controls, IoT devices, and wireless keyboards/mice using three nRF24L01+PA+LNA modules; can run iOS notification-spam attacks against out-of-date Apple devices; scans for nearby WiFi and Bluetooth networks/devices.'
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
  - hardware tool
tech:
  mcu: ESP32-WROOM-32UE
  leds:
    count: 2
    type: WS2812B
    note: two Neopixel WS2812B indicator LEDs; optional active 3V buzzer for audio feedback
  display: 1.3" OLED
  connectivity:
  - wifi
  - ble
  - bluetooth
  battery: LiPo 3.7V, 1500 mAh+ with TP4056 charge module
  sao_version: null
  inputs:
  - buttons
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://blog.toadsec.io/assets/img/posts/badge/BadgeToad.rar
  eda_tool: null
  notes: 'The blog post is a full DIY build guide with a parts list, wiring/connection diagrams, a schematic image, and a downloadable firmware archive (BadgeToad.rar) built in Arduino IDE for the ESP32 platform. No PCB Gerbers, schematic source files, or a hardware repo are linked -- only rendered PCB images -- so hardware is not fully open-sourced even though firmware is downloadable.'
links:
- label: blog.toadsec.io/2025/05/21/Badge.html
  url: https://blog.toadsec.io/2025/05/21/Badge.html
  kind: website
- label: Toad Security (blog)
  url: https://blog.toadsec.io
  kind: website
images:
- file: assets/images/badges/rootedcon-2025/toadsec-badge-rootedcon/8eca27cae9.jpg
  source: "https://blog.toadsec.io/2025/05/21/Badge.html"
  credit: "Toad Security / Snoody"
  caption: "Front of the ToadSec Badge PCB design"
- file: assets/images/badges/rootedcon-2025/toadsec-badge-rootedcon/167c8e28df.jpg
  source: "https://blog.toadsec.io/2025/05/21/Badge.html"
  credit: "Toad Security / Snoody"
  caption: "Back of the ToadSec Badge PCB design"
contact:
  email: snoody@toadsec.io
notes:
- Fan-made ESP32 Wroom32 UE badge/wireless-pentest tool built for RootedCON, with three nRF24L01+PA+LNA modules, 1.3in OLED, LiPo/TP4056 power and optional long-range EBYTE modules, documented with firmware download on the Toad Security blog. Found by the event-year sweep, task con-navaja-negra.
status: released
sources:
- kind: url
  url: https://blog.toadsec.io/2025/05/21/Badge.html
  title: ToadSec Badge RootedCON
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-navaja-negra); event read as ''RootedCON 2025''.'
- kind: url
  url: https://blog.toadsec.io/2025/05/21/Badge.html
  title: ToadSec Badge RootedCON
  accessed: '2026-09-08'
  note: Confirmed the badge is a real DIY build (ESP32 + 3x nRF24L01+PA+LNA, 1.3in OLED, WS2812B LEDs, LiPo/TP4056 power, 5 SMD buttons); designer credited as Snoody, writeup by Alejandro Torres; firmware download (BadgeToad.rar) present; no price/quantity/store found.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'This is a DIY build-your-own guide (parts list + wiring diagrams + firmware download) rather than a badge that was sold or handed out at RootedCON, so get_one fields (price/quantity/availability) are left empty -- no sources state that it was distributed at the event itself. No Gerbers or hardware source files were found, only rendered PCB images, so make_your_own.open_source is "partial" (firmware only). No maker photos of an assembled physical unit were found -- images saved are the PCB layout renders. Could not confirm total units built or whether any were handed out on-site at RootedCON Madrid 2025.'
last_modified_date: '2026-09-08'
---

The ToadSec Badge is a DIY ESP32-based badge published by Toad Security (writeup by Alejandro Torres, PCB design by "Snoody") for RootedCON, built around an ESP32-WROOM-32UE paired with three nRF24L01+PA+LNA modules. It is styled as a 2.4GHz wireless-attack tool: it can jam and spam WiFi, Bluetooth, BLE, RC controls, and IoT devices, and specifically calls out spamming outdated iOS devices with notification pop-ups, alongside passive WiFi/Bluetooth scanning. A 1.3" OLED screen, two WS2812B LEDs, five SMD buttons, and an optional buzzer round out the interface, powered by a 1500 mAh+ LiPo cell through a TP4056 charge module with an optional trio of EBYTE E01-2G4M27D modules to extend range.

The blog post is written as a complete build guide rather than a product listing: it lists every component, gives wiring tables for the battery/charging circuit, shows a schematic diagram, and links a downloadable Arduino firmware archive (BadgeToad.rar) with setup notes for the ESP32 Arduino core and troubleshooting tips. No Gerber files, KiCad/Eagle sources, or a hardware repository are linked, so the hardware side is documented in pictures only rather than fully open-sourced; the firmware is the one piece that is directly downloadable.

No pricing, unit count, or distribution details (e.g., whether it was sold, given away, or built individually by attendees) are stated anywhere on the page, so those fields are left blank rather than guessed.
