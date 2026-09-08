---
title: Disobey 2020 Badge
id: other-disobey-2020-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2020
makers:
- name: Badge.Team
  url: https://badge.team/
summary: The electronic badge given to attendees of Disobey 2020 (a Finnish hacker conference), running Badge.Team's shared ESP32 badge platform with touch buttons and a homescreen/app-launcher interface.
functions: Boots to a homescreen showing the Disobey logo; START opens an app launcher (the "Hatchery") for installing community-made MicroPython apps; other apps let you set a nickname and configure WiFi; exposes a Python shell over USB-serial.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - console
  - security
tech:
  mcu: ESP32
  leds: null
  display: null
  connectivity:
  - wifi
  - uart
  inputs:
  - touch
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to attendees of Disobey 2020 in Helsinki, Finland.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/badgeteam/ESP32-platform-firmware
  eda_tool: null
links:
- label: badge.team/docs/badges/disobey-2020
  url: https://badge.team/docs/badges/disobey-2020/
  kind: website
- label: ESP32-platform-firmware (badgeteam)
  url: https://github.com/badgeteam/ESP32-platform-firmware
  kind: repo
  archived: https://web.archive.org/web/20260508163633/https://github.com/badgeteam/ESP32-platform-firmware
images:
- file: assets/images/badges/other/disobey-2020-badge/7799eeaf08.jpg
  source: https://badge.team/docs/badges/disobey-2020/
  credit: Badge.Team
  caption: Disobey 2020 badge
contact: {}
notes:
- Gameboy-style touch button layout (Start/A/B/Select/D-pad), USB-serial at 115200 8n1, Hatchery app store, nickname/WiFi config apps.
status: listed
sources:
- kind: url
  url: https://badge.team/docs/badges/disobey-2020/
  title: Disobey 2020 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''Disobey 2020''.'
- kind: url
  url: https://badge.team/docs/badges/disobey-2020/
  title: Disobey 2020 | Badge.Team
  accessed: '2026-09-07'
  note: Confirms button layout (touch buttons styled as Gameboy Start/A/B/Select/D-pad), USB-serial 115200 8n1, Hatchery app launcher, nickname/WiFi apps, and links to the badge photo and firmware repo.
- kind: url
  url: https://github.com/badgeteam/ESP32-platform-firmware
  title: 'GitHub - badgeteam/ESP32-platform-firmware: Universal badge platform for ESP32 based devices! Runs on the event badges from SHA2017, HackerHotel 2019, Disobey 2019, CampZone 2019, Disobey 2020 and more!'
  accessed: '2026-09-07'
  note: Confirms the Disobey 2020 badge runs on this shared ESP32 firmware platform (open source firmware).
  archived: https://web.archive.org/web/20260508163633/https://github.com/badgeteam/ESP32-platform-firmware
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No event id for "Disobey" exists yet in _data/events.yml, so event is left as "other"; the con is Disobey, a hacker conference in Helsinki, Finland, held in 2020. No dedicated hardware/schematic repo for the 2020 badge specifically was found (a disobey-badge-2019 repo exists on GitHub but is not confirmed to be the same hardware as the 2020 badge, so hardware_url is left empty rather than guessed). Price, quantity made, exact LED count/type, display, and battery were not stated on the sources checked and are left empty.
last_modified_date: '2026-09-07'
---

The Disobey 2020 badge was the electronic conference badge given to attendees of Disobey, a hacker and information-security conference held annually in Helsinki, Finland. It was built and supported by Badge.Team, the Dutch collective that maintains a shared ESP32-based badge platform used across a run of European hacker camps and conferences (SHA2017, Hackerhotel, CampZone, and others), rather than being a one-off design specific to Disobey.

The badge boots to a homescreen displaying the Disobey logo and a welcome message, and is navigated with touch buttons laid out and labeled in a Game Boy-inspired style: START, A, B, SELECT, and a directional pad, though exact button behavior varies by app. Pressing START opens Badge.Team's "Hatchery" app launcher, from which attendees could install community-written MicroPython apps, including ones for setting a nickname and configuring WiFi. The badge also exposes a Python shell over USB-serial at 115200 8n1 for direct development access.

As with other Badge.Team-platform badges, the firmware (ESP32-platform-firmware) is open source and shared across multiple years and events; no hardware files specific to the 2020 Disobey badge were found during this research, so its schematic/PCB source is left unconfirmed here.
