---
title: 39C3 Cyberwatch Badge
id: 39c3-2025-39c3-cyberwatch-badge-2
layout: badge
parent: 39C3
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: 39c3-2025
year: 2025
makers:
- name: Cyberwatch project contributors
  url: https://codeberg.org/cyberwatch
summary: A solderable, modular "cyberpunk smartwatch" badge for 39C3 whose motherboard uses SD-card-shaped edge connectors to accept swappable daughterboards called "shards."
functions: 'Base kit is a wearable ESP-based board with a status LED and a display soldered on last; an optional LoRa/Meshtastic "shard" plugs into the SD-card-style slot to add mesh-radio messaging.'
look:
  colors:
  - green
  shape: smartwatch
  themes:
  - cyberpunk
  - wearable
  - radio
tech:
  mcu: ESP
  leds:
    count: 1
    type: null
    note: Single LED on the back; maker recommends soldering it sideways, facing the USB connector, for an edge-lit effect.
  display: Present, soldered on last per assembly instructions; exact panel type/size not stated in sources.
  connectivity:
  - lora
  - meshtastic
  - i2c
  - uart
  battery: Rechargeable LiPo charged via USB(-C); board includes a charging controller IC and a battery-disconnect transistor.
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - kit
  where: Distributed as a DIY solder-it-yourself kit through the "Fachschaft GAF∧Friends - LMU München" assembly at 39C3; day-one kits ran short on components, with replacements handed out on site during the congress.
make_your_own:
  open_source: yes
  hardware_url: https://codeberg.org/cyberwatch/39C3-release_board
  firmware_url: https://codeberg.org/cyberwatch/cyberwatch-meshtastic
  eda_tool: KiCad
links:
- label: codeberg.org/cyberwatch/39C3-release_board
  url: https://codeberg.org/cyberwatch/39C3-release_board
  kind: website
- label: Cyberwatch homepage & docs
  url: https://cyberwatch.codeberg.page/
  kind: website
- label: 39C3 congress hub - assembly page
  url: https://events.ccc.de/congress/2025/hub/en/project/detail/assembly/cyberwatch-badge-96/
  kind: doc
images:
- file: assets/images/badges/39c3-2025/39c3-cyberwatch-badge-2/76841c0a89.jpg
  source: "https://cyberwatch.codeberg.page/"
  credit: "Cyberwatch team"
  caption: "KiCad 3D render of the assembled front of the Cyberwatch motherboard and a shard daughterboard, showing the SD-card-style edge connectors"
- file: assets/images/badges/39c3-2025/39c3-cyberwatch-badge-2/3dc9fd3c83.jpg
  source: "https://cyberwatch.codeberg.page/"
  credit: "Cyberwatch team"
  caption: "Back-side PCB layout with the 39C3 'Power Cycles' congress art and pinout labels"
contact: {}
notes:
- Modular, solderable smartwatch-shaped badge for 39C3 with an SD-card interface for swappable daughterboard 'shards'. Found by the event-year sweep, task general-2025.
- 'Duplicate: an earlier sweep independently created 39c3-2025-39c3-cyberwatch-badge for the same item under the 39c3-2025 event id; this entry''s event was corrected from ccc-congress-2025 to 39c3-2025 to match.'
status: released
sources:
- kind: url
  url: https://codeberg.org/cyberwatch/39C3-release_board
  title: 39C3 Cyberwatch Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2025); event read as ''39C3 (Chaos Communication Congress 2025)''.'
- kind: url
  url: https://cyberwatch.codeberg.page/
  title: Cyberwatch homepage
  accessed: '2026-09-08'
  note: Confirmed features (shards, LoRa/Meshtastic shard, LED, display), on-site kit component shortage, and image URLs (front render, layout render).
- kind: url
  url: https://events.ccc.de/congress/2025/hub/en/project/detail/assembly/cyberwatch-badge-96/
  title: 39th Chaos Communications Congress - Project Cyberwatch Badge
  accessed: '2026-09-08'
  note: Confirmed the hosting assembly ("Fachschaft GAF∧Friends - LMU München") and topic tags (badge, lora, solder, meshtastic, modular, kit).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (modular shard design, LoRa/Meshtastic option, kit distribution at 39C3) confirmed on the maker''s own Codeberg org and homepage, and cross-confirmed by the official 39C3 congress hub assembly page. No price or production-quantity figures were published anywhere found. Exact MCU part number, display panel spec, and LED part number are not stated in any source, only the family/role ("ESP", "a display", "the LED"). The two saved images are KiCad 3D-render mockups from the project homepage, not photos of a physically assembled unit - no assembled-badge photo was found. Event corrected from ccc-congress-2025 to 39c3-2025 (the events.yml id specific to 39C3); note this duplicates entry 39c3-2025-39c3-cyberwatch-badge, which an earlier sweep created independently for the same badge.'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/ccc-congress-2025/39c3-cyberwatch-badge/
---

The Cyberwatch is a solderable, wrist-worn "cyberpunk smartwatch" badge built for 39C3 (Chaos Communication Congress 2025) by a team distributing it through the Fachschaft GAF∧Friends (LMU München) assembly. Its defining feature is a set of SD-card-shaped edge connectors on the motherboard: because a PCB happens to be close to the thickness of a standard SD card, the team designed the badge so that add-on "shard" daughterboards - fabricated on the same production run as the motherboard - can be plugged into these slots the way a memory card would be. The base kit centers on an ESP-family microcontroller, a rear status LED, and a display that the build instructions say to solder on last, with USB-based LiPo charging handled by an onboard charge controller and battery-disconnect transistor.

An optional LoRa shard running a Meshtastic-based firmware fork lets the badge join mesh-radio messaging networks, alongside I2C and UART headers exposed on the motherboard for other shard designs. The project was handed out as a DIY solder-yourself kit on site at 39C3; the maker's homepage notes that day-one kits ran into component shortages, with replacements provided during the congress. Hardware (KiCad source and Gerbers) and firmware (including the Meshtastic fork and a RIOT OS variant) are published on the project's Codeberg organization.

No assembled-unit photo, price, or production quantity was found in any source consulted; the images attached here are KiCad 3D-render mockups from the project's own homepage rather than photographs. This entry duplicates `39c3-2025-39c3-cyberwatch-badge`, created independently by an earlier sweep for the same badge under the correct `39c3-2025` event id.
