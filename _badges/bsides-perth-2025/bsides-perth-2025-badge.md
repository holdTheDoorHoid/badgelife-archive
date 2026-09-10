---
title: BSides Perth 2025 badge
id: bsides-perth-2025-bsides-perth-2025-badge
layout: badge
parent: BSides Perth 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-perth-2025
year: 2025
makers:
- name: badges4dotcom
  url: https://github.com/badges4dotcom
summary: An attendee-assembled BSides Perth 2025 badge built around an ESP32 DOIT DevKit and a 1.8-inch LCD, paired with a matching web-based virtual badge for those who don't build the hardware.
functions: Runs a button-driven sequence/puzzle game with offline challenge sequences and (from Nov 2025) online challenges via a companion API; the virtual badge mirrors the game in a browser with keyboard controls and extra hidden content.
look:
  colors: []
  shape: rectangle
  themes:
  - security
  - kit
  - puzzle
tech:
  mcu: ESP32 DOIT DevKit v1 (30-pin)
  leds: null
  display: 1.8" LCD TFT
  connectivity:
  - wifi
  inputs:
  - buttons
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed as a self-assembled component kit to BSides Perth 2025 attendees; parts sourced from AliExpress per the repo's parts list.
make_your_own:
  open_source: true
  hardware_url: https://github.com/badges4dotcom/bsidesperth2025badge
  firmware_url: https://github.com/badges4dotcom/bsidesperth2025badge/tree/main/Template
  eda_tool: null
links:
- label: github.com/badges4dotcom/bsidesperth2025badge
  url: https://github.com/badges4dotcom/bsidesperth2025badge
  kind: repo
- label: Virtual badge (badge.bsidesperth.com.au)
  url: https://badge.bsidesperth.com.au/
  kind: website
images:
- file: assets/images/badges/bsides-perth-2025/bsides-perth-2025-badge/76fb819cc5.png
  source: https://github.com/badges4dotcom/bsidesperth2025badge
  credit: badges4dotcom
  caption: The assembled BSides Perth 2025 physical badge on an ESP32 DevKit with 1.8-inch LCD
- file: assets/images/badges/bsides-perth-2025/bsides-perth-2025-badge/c17c1d5a4f.jpg
  source: https://github.com/badges4dotcom/bsidesperth2025badge
  credit: badges4dotcom
  caption: Front view of the assembled BSides Perth 2025 physical badge
contact: {}
notes:
- Sweep's line called it an attendee-assembled badge with a companion virtual badge and 3D-printable holder; confirmed against the maker's own GitHub repo. Found by the event-year sweep, task bsides-canberra.
status: released
sources:
- kind: url
  url: https://github.com/badges4dotcom/bsidesperth2025badge
  title: BSides Perth 2025 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-canberra); event read as ''BSides Perth 2025''.'
- kind: url
  url: https://github.com/badges4dotcom/bsidesperth2025badge
  title: badges4dotcom/bsidesperth2025badge README
  accessed: '2026-09-10'
  note: Parts list, assembly, virtual badge, code template, open-source status, and images.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Price and quantity made are not stated anywhere in the repo; distribution details beyond "kit built by attendees" are not documented. LED presence/count is not mentioned in the repo (no LEDs appear to be part of the BOM). Could not find a separate storefront, press coverage, or social posts about the badge.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsides-perth-2025/bsides-perth-2025-badge.glb
  method: kicad
  source_file: PCBDesign/bsides_perth_2025/bsides_perth_2025.kicad_pcb
  generated: '2026-09-10'
  bytes: 155044
---

The BSides Perth 2025 badge is a self-assembly electronics kit built by badges4dotcom for the 2025 BSides Perth conference. It centers on an ESP32 DOIT DevKit v1 paired with a 1.8-inch LCD TFT display and four tactile push buttons, and attendees solder the header pins, buttons, and resistors themselves following the maker's assembly instructions. Once built, the badge runs a button-sequence puzzle game with offline challenges, plus online challenges added via a companion API from November 2025 onward.

For anyone who doesn't build the hardware, badges4dotcom also published a virtual badge at badge.bsidesperth.com.au that mirrors the game in a browser, complete with WASD keyboard controls and bonus content (a second episode, cheats, and an easter egg) not present on the physical unit. A 3D-printable badge holder design is also provided.

## Make your own

The hardware, an Arduino code template, and the virtual badge's source are all published in the maker's GitHub repository (github.com/badges4dotcom/bsidesperth2025badge). The repo includes a full parts list with AliExpress sourcing links, step-by-step assembly and firmware re-download instructions, and a customisation guide covering both the physical and virtual badge.
