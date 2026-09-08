---
title: 44CON 2025 RF Detector Badge
id: 44con-2025-44con-2025-rf-detector-badge
layout: badge
parent: 44CON 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: 44con-2025
year: 2025
makers:
- name: Electronic Cats
  url: https://github.com/ElectronicCats
summary: An open-source hardware badge for 44CON 2025 with a dual-MCU design (CH32 or ESP32) and an optional RF-detector add-on that measures wireless signal strength.
functions: Runs a built-in mini-game on its OLED display; with the ESP32 and add-ons soldered, it acts as an RF/hidden-wireless-device detector (based on the rfhunter project) with a boost converter, potentiometer, and buzzer alerts.
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
  - security
tech:
  mcu: CH32 or ESP32 Wemos D1
  leds: null
  display: OLED
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/ElectronicCats/badge-44con-2025
  firmware_url: https://github.com/ElectronicCats/badge-44con-2025
  eda_tool: null
  license: CERN Open Hardware Licence v1.2
  notes: RF-detector firmware/hardware builds on the rfhunter project by RamboRogers (https://github.com/RamboRogers/rfhunter).
links:
- label: github.com/ElectronicCats/badge-44con-2025
  url: https://github.com/ElectronicCats/badge-44con-2025
  kind: repo
images:
- file: assets/images/badges/44con-2025/44con-2025-rf-detector-badge/787dc96506.png
  source: "https://github.com/ElectronicCats/badge-44con-2025"
  credit: "Electronic Cats"
  caption: "Badge layout diagram showing ESP32 configuration with RF detector, boost converter, and buzzer add-ons"
- file: assets/images/badges/44con-2025/44con-2025-rf-detector-badge/30136c3f02.jpg
  source: "https://github.com/ElectronicCats/badge-44con-2025"
  credit: "Electronic Cats"
  caption: "Assembled badge with ESP32 Wemos D1 module soldered"
contact: {}
notes:
- Official 44CON 2025 badge, an open-source Electronic Cats OLED/RF-detector board with CH32 or ESP32 Wemos D1 build options, buzzer and MT3608/AD8317 add-ons. Found by the event-year sweep, task con-44con.
- No pricing, quantity, or distribution details were published in the repo; the README documents assembly only.
status: listed
sources:
- kind: url
  url: https://github.com/ElectronicCats/badge-44con-2025
  title: 44CON 2025 RF Detector Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-44con); event read as ''44CON 2025''.'
- kind: url
  url: https://github.com/ElectronicCats/badge-44con-2025
  title: badge-44con-2025 README (ElectronicCats)
  accessed: '2026-09-08'
  note: Confirmed maker, event, dual-MCU design, OLED mini-game, RF-detector add-on built on rfhunter, CERN OHL v1.2 open-source hardware license.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed via the maker's own GitHub repo and README (Electronic Cats). Repo carries no pricing, unit count, or distribution channel, so get_one fields are left empty. No SAO header noted; treated as a standalone badge with an add-on RF-detector board rather than a plug-in SAO. No third-party coverage (press/Hackaday/storefront) found to add or contradict maker details.
last_modified_date: '2026-09-08'
---

Electronic Cats designed this badge for 44CON 2025 as an open-source, dual-microcontroller board: it can run on a CH32 chip alone (driving just the OLED display and its built-in mini-game) or on an ESP32 Wemos D1 module for full functionality. I²C jumpers on the back of the board decide which chip controls the display.

The badge's headline feature is an optional RF-detector add-on, built on the open-source rfhunter project by RamboRogers. With the ESP32, a boost converter (raising 5V to 9V), an AD8317 RF detector, a potentiometer, and a buzzer all soldered in, the badge can sense hidden wireless devices by measuring RF signal strength and reporting it on the OLED screen, with optional audible alerts.

Hardware is released under the CERN Open Hardware Licence v1.2, and the GitHub repository includes wiring diagrams and step-by-step soldering photos for each add-on (boost circuit, potentiometer, buzzer, and RF detector module). No pricing, unit quantity, or distribution details were published alongside the design files.
