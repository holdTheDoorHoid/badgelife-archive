---
title: BSides Vancouver 2025 Badge
id: bsides-vancouver-2025-b-sides-vancouver-2025-badge
layout: badge
parent: BSides Vancouver 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-vancouver-2025
year: 2025
makers:
- name: Nick Maltchev (maltchev)
  url: https://github.com/maltchev
summary: The official BSides Vancouver 2025 conference badge, an ESP32-C3 wearable with an NFC reader, addressable RGB LEDs, and a hidden mini capture-the-flag challenge.
functions: Reads NFC tags handed out at the conference to change the badge's team colour, record session attendance, and trigger achievement LEDs. Detects a magnet via a bipolar-latching Hall sensor and measures ambient light to auto-sleep when pocketed. Long-pressing a button optionally opens a WiFi access point hosting a phone-friendly control panel and a deliberately-vulnerable mini capture-the-flag at 192.168.4.1. Progress is stored persistently so power-cycling does not reset it. The badge also served as the basis for the BSides Vancouver badge-building workshop, with a starter-template firmware for attendees.
look:
  colors: []
  shape: rectangle
  themes:
  - security
  - ctf
  - puzzle
  - radio
  form_factor: pcb badge
tech:
  mcu: ESP32-C3
  leds:
    count: 11
    type: SK6812MINI-HS (5x addressable) + 6x charlieplexed indicator LEDs
    note: 5 addressable "NeoPixel"-style RGB LEDs plus 6 monochrome charlieplexed indicator LEDs
  display: none
  connectivity:
  - wifi
  - nfc
  battery: 2x CR2032 (parallel) or USB Type-A power
  sao_version: none
  inputs:
  - buttons
  power: USB Type-A (edge connector)
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to attendees of BSides Vancouver 2025; no separate storefront found.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/maltchev/bsides-vancouver-badge/blob/main/docs/HARDWARE.md
  firmware_url: https://github.com/maltchev/bsides-vancouver-badge
  eda_tool: null
  license: MIT
links:
- label: www.bsidesvancouver.com/archive/2025/2025-badge
  url: https://www.bsidesvancouver.com/archive/2025/2025-badge
  kind: website
  archived: https://web.archive.org/web/20260418095833/https://www.bsidesvancouver.com/archive/2025/2025-badge
- label: github.com/maltchev/bsides-vancouver-badge
  url: https://github.com/maltchev/bsides-vancouver-badge
  kind: repo
- label: github.com/bsidesvancouver/Bsides2025badge
  url: https://github.com/bsidesvancouver/Bsides2025badge
  kind: repo
- label: docs/HARDWARE.md (pinout & component reference)
  url: https://github.com/maltchev/bsides-vancouver-badge/blob/main/docs/HARDWARE.md
  kind: doc
images: []
contact: {}
notes:
- ESP32-C3 badge with interactive puzzles/sensors and hidden secrets, flashable via esptool. Found by the event-year sweep, task bsides-any.
- This entry is a duplicate of bsides-vancouver-2025-bsides-vancouver-2025-badge (same badge, same repo, maker Nick Maltchev). The sweep originally attributed this entry to "BSides Vancouver community"; the maker's own repo names Nick Maltchev (maltchev) as the developer.
- 'Original sweep line: "Official BSides Vancouver 2025 conference badge: an ESP32-C3 wearable with NFC reader, addressable RGB LEDs, charlieplexed indicator LEDs, and a hall-effect sensor; firmware and schematics published on GitHub." Found by the event-year sweep, task bsides-detroit. Confirmed on maker''s GitHub repo and the event''s own archive page; title matches the maker''s own naming.'
status: listed
sources:
- kind: url
  url: https://www.bsidesvancouver.com/archive/2025/2025-badge
  title: B|Sides Vancouver 2025 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-any); event read as ''BSides Vancouver 2025''.'
  archived: https://web.archive.org/web/20260418095833/https://www.bsidesvancouver.com/archive/2025/2025-badge
- kind: url
  url: https://github.com/maltchev/bsides-vancouver-badge
  title: 'maltchev/bsides-vancouver-badge: BSides Vancouver Conference Badge'
  accessed: '2026-09-10'
  note: 'Maker''s own repository: confirms maker (Nick Maltchev), ESP32-C3 MCU, LED counts/types, NFC/Hall/ALS sensors, buttons, battery/power options, WiFi AP + mini-CTF feature, MIT license and open-source hardware/firmware.'
- kind: url
  url: https://raw.githubusercontent.com/maltchev/bsides-vancouver-badge/main/docs/HARDWARE.md
  title: BSides Vancouver Badge - Hardware Reference
  accessed: '2026-09-10'
  note: Confirms board dimensions, component list (LEDs, Hall switch, ALS, NFC reader, regulators), and power rails (USB or 2x CR2032).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Confirmed via the maker's own GitHub repository (maltchev/bsides-vancouver-badge), which is authoritative and matches the event page. No photos of the assembled badge were found (only the shields.io README badges and the event's generic logo image); a schematic PDF exists in the repo but is not a photo. Price, quantity made, and public availability status were not stated anywhere found. This entry duplicates bsides-vancouver-2025-bsides-vancouver-2025-badge, which already has the maker and repo link; the two should likely be merged. Merged with duplicate entry 'BSides Vancouver 2025 Badge' (bsides-vancouver-2025-bsides-vancouver-2025-badge).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/bsides-vancouver-2025/bsides-vancouver-2025-badge/
---

The BSides Vancouver 2025 badge is an ESP32-C3-based wearable designed and built by Nick Maltchev (GitHub: maltchev) as the official conference badge. It carries five addressable SK6812MINI-HS RGB LEDs alongside six monochrome charlieplexed indicator LEDs, an ST25R3911B NFC reader, a bipolar-latching Hall-effect sensor for magnet detection, and an ambient-light sensor that lets the badge auto-sleep when pocketed. It can run off USB power or two CR2032 coin cells wired in parallel.

Beyond blinking lights, the badge doubles as an interactive conference game: scanning conference-distributed NFC tags changes the badge's team colour, logs session attendance, and unlocks achievement LEDs. Long-pressing one of its two buttons opens an optional WiFi access point with a phone-friendly control panel and a small, deliberately vulnerable capture-the-flag challenge hosted locally. Progress persists across power cycles via onboard NVS storage. The badge also anchored a hands-on badge-building workshop at the conference, with a stripped-down "starter template" firmware provided for attendees to build on.

Both firmware and hardware (including a full schematic PDF) are published under the MIT license in the maker's GitHub repository, along with prebuilt binaries for attendees who just want to reflash a stock badge.

## Make your own

Hardware and firmware are fully open source (MIT license) at [github.com/maltchev/bsides-vancouver-badge](https://github.com/maltchev/bsides-vancouver-badge). To build firmware from source: install ESP-IDF v5.4.1, clone the repository, then run `idf.py set-target esp32c3`, `idf.py build`, and `idf.py -p <PORT> flash monitor`. Prebuilt binaries (bootloader, partition table, and application image) are also provided under `prebuilt/2025-production/` for flashing with esptool.py or the Windows ESP32 Flasher tool without needing a full ESP-IDF setup. The repository's `docs/HARDWARE.md` and the accompanying schematic PDF document the full pinout and component list for anyone wanting to reproduce the board.

## Notes merged from the duplicate entry "BSides Vancouver 2025 Badge"

The BSides Vancouver 2025 badge is an ESP32-C3-based wearable built by Nick Maltchev (GitHub: maltchev) as both the official conference badge and the teaching platform for the con's badge-building workshop. It carries an ST25R3911B NFC reader that scans tags handed out around the venue to shift the badge's team colour, log session attendance, or light up achievement LEDs, alongside five SK6812MINI-HS addressable RGB LEDs and six charlieplexed indicator LEDs. A bipolar-latching Hall-effect sensor and an ambient-light sensor round out the sensing package, the latter used to drop the badge into light sleep when it's pocketed.

Long-pressing one of its two buttons opens an on-badge WiFi access point hosting a phone-friendly control panel and a small, intentionally-vulnerable capture-the-flag challenge at 192.168.4.1. The 100 mm x 100 mm single-sided FR-4 board runs off USB power or two CR2032 cells wired in parallel (the coin cells can't sustain the NFC front-end's inrush current, so the firmware exposes a low-power mode that skips NFC init for off-USB testing). Progress persists across power cycles via NVS.

## Make your own

Both hardware and firmware are published under the MIT license in the `maltchev/bsides-vancouver-badge` GitHub repository. The five-page schematic PDF (`docs/BSides_Badge_2025_r2.0_Schematics.PDF`) is the authoritative hardware reference; `docs/HARDWARE.md` summarizes the components and GPIO pinout for firmware purposes. The repo builds with ESP-IDF v5.4.1 (`idf.py set-target esp32c3 && idf.py build && idf.py -p <PORT> flash monitor`), and also ships a `starter-template/` blank project and pre-built binaries under `prebuilt/2025-production/` for flashing without a full toolchain install.
