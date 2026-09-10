---
title: BSides Vancouver 2025 Badge
id: bsides-vancouver-2025-bsides-vancouver-2025-badge
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
summary: An ESP32-C3 wearable badge for BSides Vancouver 2025 that reads NFC tags handed out at the con to change team colour, log session attendance, and unlock achievement LEDs, and doubles as the platform for the con's badge-building workshop.
functions: Reads NFC tags to change the badge's team colour, record session attendance, or trigger achievement LEDs; detects a magnet via a bipolar-latching Hall sensor; uses an ambient-light sensor to auto-sleep when pocketed; optionally hosts an open WiFi access point (long-press BTN2) with a phone-friendly control panel and a deliberately-vulnerable mini capture-the-flag at 192.168.4.1; persists progress across power cycles in NVS.
look:
  colors: []
  shape: rectangle
  themes:
  - security
  - ctf
  - puzzle
  - wearable
  form_factor: pcb badge
tech:
  mcu: ESP32-C3
  leds:
    count: 5
    type: SK6812MINI-HS
    note: 5 addressable RGB "NeoPixel"-style LEDs plus 6 charlieplexed monochrome indicator LEDs (D3-D9)
  display: none
  connectivity:
  - wifi
  - nfc
  inputs:
  - buttons
  power: USB Type-A (edge connector)
  battery: 2x CR2032 (parallel, optional)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/maltchev/bsides-vancouver-badge/blob/main/docs/BSides_Badge_2025_r2.0_Schematics.PDF
  firmware_url: https://github.com/maltchev/bsides-vancouver-badge
  gerbers_url: null
  eda_tool: null
  license: MIT
links:
- label: github.com/maltchev/bsides-vancouver-badge
  url: https://github.com/maltchev/bsides-vancouver-badge
  kind: repo
- label: www.bsidesvancouver.com/archive/2025/2025-badge
  url: https://www.bsidesvancouver.com/archive/2025/2025-badge
  kind: website
- label: docs/HARDWARE.md (pinout & component reference)
  url: https://github.com/maltchev/bsides-vancouver-badge/blob/main/docs/HARDWARE.md
  kind: doc
images: []
contact: {}
notes:
- 'Original sweep line: "Official BSides Vancouver 2025 conference badge: an ESP32-C3 wearable with NFC reader, addressable RGB LEDs, charlieplexed indicator LEDs, and a hall-effect sensor; firmware and schematics published on GitHub." Found by the event-year sweep, task bsides-detroit. Confirmed on maker''s GitHub repo and the event''s own archive page; title matches the maker''s own naming.'
status: released
sources:
- kind: url
  url: https://github.com/maltchev/bsides-vancouver-badge
  title: BSides Vancouver 2025 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-detroit); event read as ''BSides Vancouver 2025''.'
- kind: url
  url: https://github.com/maltchev/bsides-vancouver-badge
  title: 'maltchev/bsides-vancouver-badge: README, docs/HARDWARE.md'
  accessed: '2026-09-10'
  note: Confirmed maker, MCU (ESP32-C3), LED count/type, sensors (NFC ST25R3911B, Hall MGH201A1T3, ALS-PT19), buttons, power rails (USB or 2x CR2032), MIT firmware license, and schematic PDF location.
- kind: url
  url: https://www.bsidesvancouver.com/archive/2025/2025-badge
  title: BSides Vancouver 2025 Badge archive page
  accessed: '2026-09-10'
  note: Confirms the badge is the official BSides Vancouver 2025 badge, used with flashing/programming instructions for the badge workshop; only page image found was the BSides Vancouver site logo, not a badge photo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'No price, production quantity, or formal distribution channel is disclosed by either source; get_one fields left empty. No photo of the physical board was found (only a schematic PDF and the event''s logo image), so images could not be saved. Duplicate entry: bsides-vancouver-2025-b-sides-vancouver-2025-badge covers the same badge (found by a different sweep angle, credited generically to "BSides Vancouver community" with no maker name) and should likely be merged into this one, which has the maker-attributed source.'
last_modified_date: '2026-09-10'
---

The BSides Vancouver 2025 badge is an ESP32-C3-based wearable built by Nick Maltchev (GitHub: maltchev) as both the official conference badge and the teaching platform for the con's badge-building workshop. It carries an ST25R3911B NFC reader that scans tags handed out around the venue to shift the badge's team colour, log session attendance, or light up achievement LEDs, alongside five SK6812MINI-HS addressable RGB LEDs and six charlieplexed indicator LEDs. A bipolar-latching Hall-effect sensor and an ambient-light sensor round out the sensing package, the latter used to drop the badge into light sleep when it's pocketed.

Long-pressing one of its two buttons opens an on-badge WiFi access point hosting a phone-friendly control panel and a small, intentionally-vulnerable capture-the-flag challenge at 192.168.4.1. The 100 mm x 100 mm single-sided FR-4 board runs off USB power or two CR2032 cells wired in parallel (the coin cells can't sustain the NFC front-end's inrush current, so the firmware exposes a low-power mode that skips NFC init for off-USB testing). Progress persists across power cycles via NVS.

## Make your own

Both hardware and firmware are published under the MIT license in the `maltchev/bsides-vancouver-badge` GitHub repository. The five-page schematic PDF (`docs/BSides_Badge_2025_r2.0_Schematics.PDF`) is the authoritative hardware reference; `docs/HARDWARE.md` summarizes the components and GPIO pinout for firmware purposes. The repo builds with ESP-IDF v5.4.1 (`idf.py set-target esp32c3 && idf.py build && idf.py -p <PORT> flash monitor`), and also ships a `starter-template/` blank project and pre-built binaries under `prebuilt/2025-production/` for flashing without a full toolchain install.
