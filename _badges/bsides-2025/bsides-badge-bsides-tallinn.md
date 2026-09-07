---
title: BSides 25 Badge
id: bsides-2025-bsides-badge-bsides-tallinn
layout: badge
parent: BSides 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-2025
year: 2025
makers:
- name: BSides Tallinn
  url: https://github.com/BSides-Tallinn
summary: 'The official conference badge for BSides Tallinn 2025: an ESP32-C3 board with an OLED display and 16 addressable RGB LEDs, running MicroPython.'
functions: 'Runs MicroPython firmware loaded over USB-C; drives a 128x64 OLED display and 16 WS2812B addressable LEDs. Specific badge software/game features are not documented in the repository.'
look:
  colors: []
  shape: null
  themes:
  - security
tech:
  mcu: ESP32-C3FH4
  leds:
    count: 16
    type: WS2812B
    note: Neopixel-compatible
  display: 0.96" OLED (SSD1306, 128x64)
  connectivity:
  - wifi
  - bluetooth
  - usb
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
  open_source: yes
  hardware_url: https://github.com/BSides-Tallinn/bsides_badge/tree/main/hardware
  firmware_url: https://github.com/BSides-Tallinn/bsides_badge/tree/main/software
  eda_tool: null
links:
- label: github.com/BSides-Tallinn/bsides_badge
  url: https://github.com/BSides-Tallinn/bsides_badge
  kind: repo
- label: BSides 2025 badge schematics (PDF)
  url: https://github.com/BSides-Tallinn/bsides_badge/blob/main/hardware/BSides_2025_badge_v1.1_schematics.pdf
  kind: doc
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/BSides-Tallinn/bsides_badge
  title: bsides_badge (BSides-Tallinn)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://raw.githubusercontent.com/BSides-Tallinn/bsides_badge/main/README.md
  title: 'BSides 25 badge - README'
  accessed: '2026-09-07'
  note: Confirmed MCU, display, LED, connectivity, firmware language, and that it was made for BSides 2025.
- kind: url
  url: https://api.github.com/repos/BSides-Tallinn/bsides_badge/contents/hardware
  title: bsides_badge hardware directory listing
  accessed: '2026-09-07'
  note: Confirmed schematics PDF is the only hardware file present; no photos of the physical badge are in the repo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Repo README titles the project "BSides 25 badge" and confirms it was made for BSides 2025, but does not name a city. The GitHub org name "BSides-Tallinn" strongly implies BSides Tallinn 2025; matched to the generic bsides-2025 event id in events.yml since no location-specific "bsides-tallinn-2025" entry exists there. No price, quantity, availability, or distribution info is published in the repo. No photos of the assembled badge were found (repo contains only a schematics PDF, no image files); could not search further because this session''s web search budget was exhausted after the first search.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/bsides-badge-bsides-tallinn/
---

The BSides 25 badge is the official conference badge produced by BSides Tallinn for BSides 2025, built around an ESP32-C3FH4 microcontroller with Wi-Fi and Bluetooth. It carries a 128x64 SSD1306 OLED display and 16 WS2812B addressable RGB LEDs, and charges and flashes over USB-C.

The badge's firmware is written in MicroPython and is fully open source, published in the `BSides-Tallinn/bsides_badge` GitHub repository alongside the hardware schematics. The README documents the exact MicroPython build used for the 2025 event and gives step-by-step instructions for reflashing the badge and copying the software over with `mpremote`, making it straightforward for owners to inspect or modify the code themselves.

Beyond the technical build, no information about pricing, quantity produced, or how attendees obtained the badge could be found in the source material, and no photos of the assembled hardware are available in the repository.

## Make your own

Hardware schematics are published as a PDF in the repo's `hardware` directory. To flash the software: install `esptool` and `mpremote`, flash the MicroPython build named in the README (v1.26.1, 2025-09-11) to the ESP32-C3 with `esptool`, then copy the contents of the `software` directory to the badge with `mpremote fs cp -r software/* :/`.
