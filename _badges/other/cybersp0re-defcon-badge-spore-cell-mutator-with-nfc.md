---
title: CyberSp0re — DEFCON badge Spore cell mutator with NFC
id: other-cybersp0re-defcon-badge-spore-cell-mutator-with-nfc
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 0
makers:
- name: newtnewtnewt
  url: https://github.com/newtnewtnewt
summary: A self-built badge project that runs a genetic "Spore"-style cell mutation sim on an onboard TFT screen, letting the wearer mutate their virtual cell by scanning NFC cards.
functions: Displays and mutates a virtual "cell" (Spore-game-style) on a TFT screen; scanning an ISO14443A NFC/RFID card triggers a mutation; mutation state is saved to an onboard SD card.
look:
  colors: []
  shape: null
  themes:
  - sci-fi
  - nfc
tech:
  mcu: ESP32-S3 (Arduino Nano ESP32 "Nano Nora")
  leds: null
  display: TFT (via TFT_eSPI library; exact size not stated)
  connectivity:
  - nfc
  - wifi
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
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/newtnewtnewt/CyberSp0re
  eda_tool: null
links:
- label: github.com/newtnewtnewt/CyberSp0re
  url: https://github.com/newtnewtnewt/CyberSp0re
  kind: repo
images: []
contact: {}
notes:
- 'NFC reading uses an Adafruit PN532 breakout over SPI; a separate SPI SD card is used for persistence (SD/storage is not in the connectivity vocabulary, noted here instead).'
status: listed
sources:
- kind: url
  url: https://github.com/newtnewtnewt/CyberSp0re
  title: CyberSp0re — DEFCON badge Spore cell mutator with NFC
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/newtnewtnewt/CyberSp0re
  title: 'newtnewtnewt/CyberSp0re: A DEFCON Badge Project to build a genetic ''Spore'' cell mutator with NFC interaction'
  accessed: '2026-09-07'
  note: 'Repo README, source (.ino), and commit history read via GitHub web/API; confirmed MCU (Arduino Nano ESP32 / ESP32-S3), TFT_eSPI display, Adafruit PN532 NFC over SPI, SD card persistence. No images, no hardware/PCB files, no storefront, and no confirmation of which DEF CON year (or whether) it was actually brought/distributed at an event.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    This is a solo hobby/firmware project self-described as "A DEFCON Badge Project" by GitHub user
    newtnewtnewt (Noah Dunn), not a badge with confirmed distribution at any specific DEF CON. Commit
    history runs September-November 2025, after DEF CON 33 (Aug 2025), so it does not match that
    year's con; no source states a target year or confirms the badge was ever built as physical
    hardware, worn, or given out. No hardware files (schematic/PCB/Gerbers), no images, no price or
    quantity information, and no storefront were found. Left under the "other" event since no
    specific con/year could be confirmed from sources.
last_modified_date: '2026-09-07'
---

CyberSp0re is a solo badge-style project by GitHub user newtnewtnewt (Noah Dunn), self-described as "A DEFCON Badge Project to build a genetic 'Spore' cell mutator with NFC interaction." It runs on an Arduino Nano ESP32 ("Nano Nora," ESP32-S3-based) board, driving a TFT display through the TFT_eSPI library to render and mutate a virtual cell in the style of the Spore video game.

Mutation is triggered by scanning an ISO14443A-type NFC/RFID card, read through an Adafruit PN532 breakout wired over SPI; mutation state is written to an onboard SD card for persistence between sessions. The repository contains only Arduino sketch source code (no schematics, PCB files, or bill of materials), and no photos of a built unit, pricing, quantity, or distribution details were found, so it is unclear whether this ever existed as a badge someone wore at an event or remains a firmware-only project in progress. Commit activity spans September through November 2025.

