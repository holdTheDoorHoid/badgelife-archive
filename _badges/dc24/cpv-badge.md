---
title: Crypto & Privacy Village DC24 Badge (Blinkybadge)
id: dc24-cpv-badge
layout: badge
parent: DC24
grand_parent: Badge Archive
nav_exclude: true
redirect_from:
- /badges/dc24/cpv/
type: badge
event: dc24
year: 2016
makers:
- name: Crypto & Privacy Village
  url: https://cryptovillage.org
summary: The Crypto & Privacy Village's LED badge for DEF CON 24, nicknamed "blinkybadge," built around an ATmega32u2 with USB DFU flashing.
functions: LED lighting effects; user-reflashable firmware over USB (no external programmer needed).
look:
  colors: []
  shape: null
  themes:
  - crypto
  - privacy
  - village badge
tech:
  mcu: ATmega32u2
  leds: null
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed at the Crypto & Privacy Village at DEF CON 24 (2016); no price or quantity found.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/cryptovillage/badge2016
  firmware_url: https://github.com/cryptovillage/badge2016
  gerbers_url: https://github.com/cryptovillage/badge2016/tree/master/hardware/gerbers
  bom_url: https://github.com/cryptovillage/badge2016/blob/master/hardware/BOM.pdf
  eda_tool: KiCad
  license: null
links:
- label: Project repo (cryptovillage/badge2016)
  url: https://github.com/cryptovillage/badge2016
  kind: repo
  archived: https://web.archive.org/web/20260907112054/https://github.com/cryptovillage/badge2016
images: []
contact: {}
notes:
- Repo internally calls the project "cpvdcbadge" and the firmware/board files use the name "blinkybadge"; the flashed USB device identifies itself as "dc24:1337".
status: released
sources:
- kind: url
  url: https://badge.life/badges/dc24/cpv/
  title: Original badge.life archive page
  accessed: '2026-09-06'
  note: Migrated from the badge.life Badge Archive; the original page is preserved as the entry body.
  archived: https://web.archive.org/web/20260907112128/https://badge.life/badges/dc24/cpv/
- kind: url
  url: https://github.com/cryptovillage/badge2016
  title: cryptovillage/badge2016 GitHub repo
  accessed: '2026-09-07'
  note: Confirms it is a DEF CON 24 (2016) badge, internal name "blinkybadge"/"cpvdcbadge", ATmega32u2 MCU, USB DFU bootloader flashing via dfu-programmer, KiCad hardware source with gerbers and BOM.pdf.
  archived: https://web.archive.org/web/20260907112054/https://github.com/cryptovillage/badge2016
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Only source with real technical detail is the maker's own GitHub repo; no press coverage, storefront, Hackaday project, or maker photo of the assembled badge was found. LED count/type, display, battery, price, and quantity made are not stated anywhere found. No image of the physical badge was located, so images stays empty.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc24/cpv-badge.glb
  method: kicad
  source_file: hardware/blinkybadge.kicad_pcb
  generated: '2026-09-07'
  bytes: 171068
---
The Crypto & Privacy Village's badge for DEF CON 24 (2016) is an ATmega32u2-based LED badge that the village's own hardware repository calls the "blinkybadge" (the repo itself is named `cpvdcbadge`). It uses the ATmega32u2's built-in USB bootloader, so attendees could reflash it directly over USB with the open-source `dfu-programmer` tool and a provided `reset_badge.py` script, without needing a separate programmer. Once flashed, a badge identifies itself on USB as "dc24:1337".

Hardware and firmware are both open source in the `cryptovillage/badge2016` GitHub repository: the board (schematics for LEDs and power, a KiCad PCB layout, gerbers, and a BOM PDF) lives under `hardware/`, and firmware/build tooling under `firmware/`, alongside a pre-built test firmware hex file at the repo root.

No pricing, production quantity, storefront listing, press coverage, or photo of the finished badge could be found; the repository's README also leaves the "Building Firmware" section marked "TODO," so build instructions beyond flashing an existing hex file are incomplete even in the maker's own documentation.
