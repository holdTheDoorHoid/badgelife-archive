---
title: Aerospace Village Badge 2020
id: dc28-aerospace-village-badge-2020
layout: badge
parent: DC28
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc28
year: 2020
makers:
- name: Aerospace Village
  url: https://www.aerospacevillage.org
summary: An airplane-shaped badge/antenna that receives real ADS-B and ACARS aircraft transmissions, built for DEF CON 28's Aerospace Village.
functions: Works as an SMA antenna to receive ADS-B (1090 MHz) and ACARS (131.550 MHz) transmissions from nearby aircraft for use with an external RTL-SDR dongle; also breaks out I2C for bus pirate-style device interaction and drives onboard lighting; can be worn as a lanyard.
look:
  colors: []
  shape: airplane
  themes:
  - space
  - radio
  - wearable
  - hardware tool
tech:
  mcu: ATtiny85
  leds: null
  display: none
  connectivity:
  - i2c
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed as a kit at Aerospace Village at DEF CON 28 (2020); assembly instructions reference Tindie.
make_your_own:
  open_source: true
  hardware_url: https://github.com/AerospaceVillage/avBadge_2020
  firmware_url: https://github.com/AerospaceVillage/avBadge_2020
  eda_tool: null
links:
- label: github.com/AerospaceVillage/avBadge_2020
  url: https://github.com/AerospaceVillage/avBadge_2020
  kind: repo
  archived: https://web.archive.org/web/20260503194300/https://github.com/AerospaceVillage/avBadge_2020
- label: DC28 Badge | Aerospace Village
  url: https://www.aerospacevillage.org/dc28-badge
  kind: website
  archived: https://web.archive.org/web/20260520232307/https://www.aerospacevillage.org/dc28-badge
images:
- file: assets/images/badges/dc28/aerospace-village-badge-2020/640649db6a.jpg
  source: https://github.com/AerospaceVillage/avBadge_2020
  credit: Aerospace Village
  caption: The airplane-shaped badge lit up in daytime mode
  archived: https://web.archive.org/web/20260503194300/https://github.com/AerospaceVillage/avBadge_2020
- file: assets/images/badges/dc28/aerospace-village-badge-2020/2c7ec75148.gif
  source: https://github.com/AerospaceVillage/avBadge_2020
  credit: Aerospace Village
  caption: The airplane-shaped badge lit up in night mode showing its LEDs
  archived: https://web.archive.org/web/20260503194300/https://github.com/AerospaceVillage/avBadge_2020
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2020
  title: Aerospace Village Badge 2020
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''DEF CON 28 (2020)''.'
  archived: https://web.archive.org/web/20260503194300/https://github.com/AerospaceVillage/avBadge_2020
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2020
  title: Aerospace Village Badge 2020 README
  accessed: '2026-09-07'
  note: 'Repo README: description, ATtiny85 MCU, I2C/bus pirate interaction, lighting packages, SMA antenna for ADS-B/ACARS, lanyard STL mod, Tindie kit assembly instructions, image URLs.'
  archived: https://web.archive.org/web/20260503194300/https://github.com/AerospaceVillage/avBadge_2020
- kind: url
  url: https://www.aerospacevillage.org/dc28-badge
  title: DC28 Badge | Aerospace Village
  accessed: '2026-09-07'
  note: Maker's own page confirming ADS-B (1090 MHz) and ACARS (131.550 MHz) reception via external RTL-SDR, and design credit to Richard Hansen, Zachary Klein, and Dan Allen.
  archived: https://web.archive.org/web/20260520232307/https://www.aerospacevillage.org/dc28-badge
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price, quantity made, and LED count/type are not stated on the GitHub repo or the Aerospace Village page and are left empty. The repo lists a secondary fork/contributor URL (github.com/daneallen/avBadge_2020) referenced in kit-assembly instruction links.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc28/aerospace-village-badge-2020.glb
  method: kicad
  source_file: kicad/aerospace_badge/aerospace_badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 108804
---

The Aerospace Village Badge 2020 was the village's badge for DEF CON 28, shaped like an airplane and built to double as a real receiving antenna: with an external RTL-SDR dongle, it picks up ADS-B aircraft position broadcasts at 1090 MHz and ACARS messages at 131.550 MHz, the same data commercial flight-tracking services use. It runs on an ATtiny85, breaks out an I2C connection for interacting with tools like a Bus Pirate, and drives a set of onboard LEDs for a day and a night look. The design was inspired by Richard Hansen and Zachary Klein's work on low-cost aerospace cybersecurity education, with Dan Allen leading the final build.

It was handed out as an assemble-it-yourself kit, with instructions distributed both through the project's GitHub repo and via Tindie. A 3D-printable lanyard adapter is included in the repo so the badge can be worn rather than just carried. Hardware design and firmware are openly published on GitHub.

## Make your own

Hardware files, Arduino firmware, and assembly documentation (including a Tindie instruction PDF and printable lanyard STL files) are published at github.com/AerospaceVillage/avBadge_2020. The ATtiny85 is programmed via the Arduino IDE using the ATTinyCore board package and an ISP programmer such as the SparkFun Tiny AVR Programmer with a SparkFun ISP Pogo Adapter.
