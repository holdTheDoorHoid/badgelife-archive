---
title: 39C3 Cyberwatch Badge
id: 39c3-2025-39c3-cyberwatch-badge
layout: badge
parent: 39C3
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: 39c3-2025
year: 2025
makers:
- name: Fachschaft GAF∧Friends (LMU München)
  url: https://events.ccc.de/congress/2025/hub/en/project/detail/assembly/cyberwatch-badge-96/
summary: A solder-yourself, smartwatch-shaped badge for 39C3 whose motherboard accepts swappable "shard" daughterboards through an SD-card-reader slot, with an optional LoRa/Meshtastic radio shard.
functions: Wears as a smartwatch-style badge; reconfigurable via swappable "shard" add-on boards inserted through an SD-card-reader-style slot; a Meshtastic/LoRa shard adds mesh radio functionality; back-mounted RGB LED for effects.
look:
  colors:
  - green
  shape: smartwatch
  themes:
  - wearable
  - cyberpunk
  - radio
  - kit
tech:
  mcu: ESP32-C6-WROOM-1
  leds:
    count: 1
    type: RGB
    note: Back-mounted single RGB LED; maker recommends soldering it sideways facing the USB connector.
  display: unspecified small display (soldered last per assembly instructions)
  connectivity:
  - lora
  - meshtastic
  - usb
  battery: LiPo (has a battery disconnect transistor and charge controller on-board)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - kit
  where: Distributed as a self-solder kit at 39C3 (39th Chaos Communication Congress), Hamburg, Dec 2025; no storefront or price found.
make_your_own:
  open_source: true
  hardware_url: https://codeberg.org/cyberwatch/39C3-release_board
  firmware_url: https://codeberg.org/cyberwatch/cyberwatch-meshtastic
  eda_tool: KiCad
links:
- label: codeberg.org/cyberwatch/39C3-release_board
  url: https://codeberg.org/cyberwatch/39C3-release_board
  kind: repo
- label: 'events.ccc.de: Cyberwatch Badge project page'
  url: https://events.ccc.de/congress/2025/hub/en/project/detail/assembly/cyberwatch-badge-96/
  kind: doc
- label: Cyberwatch homepage & docs
  url: https://cyberwatch.codeberg.page/
  kind: website
images:
- file: assets/images/badges/39c3-2025/39c3-cyberwatch-badge/76841c0a89.jpg
  source: https://cyberwatch.codeberg.page/
  credit: Cyberwatch team
  caption: KiCad 3D render of the assembled front of the Cyberwatch motherboard and a shard daughterboard, showing the SD-card-style edge connectors
- file: assets/images/badges/39c3-2025/39c3-cyberwatch-badge/3dc9fd3c83.jpg
  source: https://cyberwatch.codeberg.page/
  credit: Cyberwatch team
  caption: Back-side PCB layout with the 39C3 'Power Cycles' congress art and pinout labels
contact: {}
notes:
- Modular solderable smartwatch-style badge with swappable SD-card-form-factor 'shard' add-on boards and optional LoRa/Meshtastic radio, built for 39C3. Found by the event-year sweep, task ccc-adjacent.
- Sweep imported maker as "Cyberwatch project contributors"; the project's own 39C3 hub listing names the team as "Fachschaft GAF∧Friends - LMU München" (a Munich student-union-adjacent group), which is used here instead.
- Modular, solderable smartwatch-shaped badge for 39C3 with an SD-card interface for swappable daughterboard 'shards'. Found by the event-year sweep, task general-2025.
- 'Duplicate: an earlier sweep independently created 39c3-2025-39c3-cyberwatch-badge for the same item under the 39c3-2025 event id; this entry''s event was corrected from ccc-congress-2025 to 39c3-2025 to match.'
status: listed
sources:
- kind: url
  url: https://codeberg.org/cyberwatch/39C3-release_board
  title: 39C3 Cyberwatch Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:ccc-adjacent); event read as ''39C3 2025''.'
- kind: url
  url: https://codeberg.org/cyberwatch/39C3-release_board/raw/branch/main/README.md
  title: Cyberwatch Base README
  accessed: '2026-09-08'
  note: Maker's own description of the badge concept, the SD-card "shard" mechanism, and solder-order guidance (ESP soldered on the back, display soldered last, LED orientation).
- kind: url
  url: https://events.ccc.de/congress/2025/hub/en/project/detail/assembly/cyberwatch-badge-96/
  title: Conference 39th Chaos Communications Congress - Project Cyberwatch Badge
  accessed: '2026-09-08'
  note: Confirms the maker/team name (Fachschaft GAF∧Friends - LMU München) and that the project carries LoRa/Meshtastic tags on the official 39C3 hub.
- kind: url
  url: https://codeberg.org/api/v1/repos/cyberwatch/39C3-release_board/contents/Resources
  title: Repository Resources directory listing
  accessed: '2026-09-08'
  note: Identifies the exact MCU part (ESP32-C6-WROOM-1, both -N8 and -1U-N8 variants present as KiCad symbol/footprint archives) and the LoRa radio options included in the design (RFM95W_868S2 and a Wio-SX1262 module library), confirming the 868 MHz LoRa/Meshtastic shard.
- kind: url
  url: https://cyberwatch.codeberg.page/
  title: Cyberwatch homepage
  accessed: '2026-09-08'
  note: Confirmed features (shards, LoRa/Meshtastic shard, LED, display), on-site kit component shortage, and image URLs (front render, layout render).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, maker-documented badge (not just a sweep snippet): the Codeberg repo and the official 39C3 congress hub project page both describe it. Could not find price, quantity made, availability/sold-out status, a firmware repo, display part/size, or any photo of the assembled hardware — the repository''s Resources folder holds only design-guide assets (fonts, logos, style-guide files) and component datasheet images, not photos of the finished badge. Duplicates entry ccc-congress-2025-39c3-cyberwatch-badge, which covers the same badge under a different event-id folder for the same congress. Merged with duplicate entry ''39C3 Cyberwatch Badge'' (39c3-2025-39c3-cyberwatch-badge-2).'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/39c3-2025/39c3-cyberwatch-badge-2/
---

The Cyberwatch is a solder-it-yourself badge built by Fachschaft GAF∧Friends, a Munich (LMU München) student group, for 39C3 (the 39th Chaos Communication Congress) in Hamburg, December 2025. It is shaped and worn like a smartwatch, built around an ESP32-C6-WROOM-1 module. Its distinguishing feature is a motherboard with an SD-card-reader-style slot: because a PCB and a standard SD card are roughly the same thickness, the team designed small daughterboards ("shards") that plug into that slot to swap in different functionality, panelized alongside the mainboard for single-run manufacturing. One documented shard adds a LoRa radio (the design includes both an RFM95W 868 MHz module and a Wio-SX1262 module option) for Meshtastic-style mesh networking.

The badge also carries a small display (the maker's assembly notes say to solder it last, with tape underneath to avoid shorts) and a single back-mounted RGB LED, plus onboard LiPo charging and battery-disconnect circuitry. The hardware is fully open: KiCad schematics, PCB layout, and a print-ready assembly PDF are published on the team's Codeberg repository, alongside the 39C3 congress style-guide assets used for the board art. No firmware repository, price, production quantity, or post-congress availability information was found.

## Notes merged from the duplicate entry "39C3 Cyberwatch Badge"

The Cyberwatch is a solderable, wrist-worn "cyberpunk smartwatch" badge built for 39C3 (Chaos Communication Congress 2025) by a team distributing it through the Fachschaft GAF∧Friends (LMU München) assembly. Its defining feature is a set of SD-card-shaped edge connectors on the motherboard: because a PCB happens to be close to the thickness of a standard SD card, the team designed the badge so that add-on "shard" daughterboards - fabricated on the same production run as the motherboard - can be plugged into these slots the way a memory card would be. The base kit centers on an ESP-family microcontroller, a rear status LED, and a display that the build instructions say to solder on last, with USB-based LiPo charging handled by an onboard charge controller and battery-disconnect transistor.

An optional LoRa shard running a Meshtastic-based firmware fork lets the badge join mesh-radio messaging networks, alongside I2C and UART headers exposed on the motherboard for other shard designs. The project was handed out as a DIY solder-yourself kit on site at 39C3; the maker's homepage notes that day-one kits ran into component shortages, with replacements provided during the congress. Hardware (KiCad source and Gerbers) and firmware (including the Meshtastic fork and a RIOT OS variant) are published on the project's Codeberg organization.

No assembled-unit photo, price, or production quantity was found in any source consulted; the images attached here are KiCad 3D-render mockups from the project's own homepage rather than photographs. This entry duplicates `39c3-2025-39c3-cyberwatch-badge`, created independently by an earlier sweep for the same badge under the correct `39c3-2025` event id.
