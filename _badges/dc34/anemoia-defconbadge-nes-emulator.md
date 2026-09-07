---
title: Anemoia-DefconBadge (NES emulator)
id: dc34-anemoia-defconbadge-nes-emulator
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: other
event: dc34
year: 2026
makers:
- name: Retia LLC / Shim06
summary: ''
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
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
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/RetiaLLC/Anemoia-DefconBadge
  url: https://github.com/RetiaLLC/Anemoia-DefconBadge
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: not_an_item
sources:
- kind: url
  url: https://github.com/RetiaLLC/Anemoia-DefconBadge
  title: Anemoia-DefconBadge (NES emulator)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc34''.'
- kind: url
  url: https://github.com/RetiaLLC/DefconBadge2026
  title: 'RetiaLLC/DefconBadge2026 — DEF CON Badge (2026), ESP32-S3'
  accessed: '2026-09-07'
  note: The actual hardware badge this firmware runs on; confirms it is a third-party firmware port, not a standalone badge/SAO product.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    This repo is a firmware port, not a badge or SAO in its own right. Its README
    says it is "a standalone port of the Anemoia-ESP32 NES emulator for the Retia
    2024 DEF CON badge (ESP32-S3, ILI9341 TFT, micro-SD, piezo)" (upstream emulator:
    Shim06/Anemoia-ESP32, GPL-3.0). The actual badge hardware, made by Retia LLC,
    lives in a separate repo, RetiaLLC/DefconBadge2026, which documents an
    ESP32-S3-WROOM-1 badge with a 2.4" ILI9341 touch TFT, RFM95W LoRa radio, 10x
    WS2812B NeoPixels, SAO v2 + QWIIC + UART/SPI expansion, and 2xAA/USB-C power
    (GitHub, accessed 2026-09-07); despite the README's "2024" wording, the repo
    was created and pushed in July 2026 and is explicitly the 2026 badge (repo
    named DefconBadge2026), consistent with the dc34 (DEF CON 34, 2026) event
    already on this entry. Recommend replacing this entry with one for the actual
    RetiaLLC DC34 badge (see other_items_found); this Anemoia repo is one of
    several alternate-firmware projects for it (alongside DOOM, Meshtastic,
    MeshCore, Reticulum, and the "Badge Launcher" menu system) and does not merit
    its own catalog entry as a distinct hardware item.
last_modified_date: '2026-09-07'
---

This GitHub repository is a software port, not a hardware badge or SAO. It adapts the open-source [Anemoia-ESP32](https://github.com/Shim06/Anemoia-ESP32) NES emulator (by Shim06, GPL-3.0) to run on the Retia LLC DEF CON 34 badge, an ESP32-S3 badge with an ILI9341 color TFT, micro-SD slot, and piezo buzzer. Players load `.nes` ROMs from an SD card, browse and launch them from an on-badge menu, and hear chiptune audio through the badge's unamplified piezo via a custom sigma-delta modulation driver clocked at 44.1 kHz.

The bulk of the project's documented work is badge-specific bring-up rather than emulator design: the badge shares one SPI bus between its display, SD card, and LoRa radio, and the port had to add strict bus-transaction discipline to avoid deadlocks, switch to a flash-mapped ROM backend so gameplay never touches the SD card mid-frame, enlarge a stack that overflowed during the ROM-to-flash copy, patch a vendored TFT_eSPI display driver for an ESP-IDF 5 regression, fix bank-mirroring bugs in two NES mapper types, and design a one-button START/SELECT/pause scheme around the badge's limited controls.

The badge hardware itself, along with its other alternate firmware (DOOM, Meshtastic, MeshCore, Reticulum, and a "Badge Launcher" menu), is documented in the separate RetiaLLC/DefconBadge2026 repository; that project, not this emulator port, is the actual DEF CON 34 badge and is a candidate for its own archive entry.
