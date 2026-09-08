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
functions: 'Wears as a smartwatch-style badge; reconfigurable via swappable "shard" add-on boards inserted through an SD-card-reader-style slot; a Meshtastic/LoRa shard adds mesh radio functionality; back-mounted RGB LED for effects.'
look:
  colors: []
  shape: null
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
  availability: unknown
  distribution:
  - kit
  where: 'Distributed as a self-solder kit at 39C3 (39th Chaos Communication Congress), Hamburg, Dec 2025; no storefront or price found.'
make_your_own:
  open_source: yes
  hardware_url: https://codeberg.org/cyberwatch/39C3-release_board
  firmware_url: null
  eda_tool: KiCad
links:
- label: codeberg.org/cyberwatch/39C3-release_board
  url: https://codeberg.org/cyberwatch/39C3-release_board
  kind: repo
- label: 'events.ccc.de: Cyberwatch Badge project page'
  url: https://events.ccc.de/congress/2025/hub/en/project/detail/assembly/cyberwatch-badge-96/
  kind: doc
images: []
contact: {}
notes:
- Modular solderable smartwatch-style badge with swappable SD-card-form-factor 'shard' add-on boards and optional LoRa/Meshtastic radio, built for 39C3. Found by the event-year sweep, task ccc-adjacent.
- 'Sweep imported maker as "Cyberwatch project contributors"; the project''s own 39C3 hub listing names the team as "Fachschaft GAF∧Friends - LMU München" (a Munich student-union-adjacent group), which is used here instead.'
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
  note: 'Maker''s own description of the badge concept, the SD-card "shard" mechanism, and solder-order guidance (ESP soldered on the back, display soldered last, LED orientation).'
- kind: url
  url: https://events.ccc.de/congress/2025/hub/en/project/detail/assembly/cyberwatch-badge-96/
  title: 'Conference 39th Chaos Communications Congress - Project Cyberwatch Badge'
  accessed: '2026-09-08'
  note: Confirms the maker/team name (Fachschaft GAF∧Friends - LMU München) and that the project carries LoRa/Meshtastic tags on the official 39C3 hub.
- kind: url
  url: https://codeberg.org/api/v1/repos/cyberwatch/39C3-release_board/contents/Resources
  title: Repository Resources directory listing
  accessed: '2026-09-08'
  note: 'Identifies the exact MCU part (ESP32-C6-WROOM-1, both -N8 and -1U-N8 variants present as KiCad symbol/footprint archives) and the LoRa radio options included in the design (RFM95W_868S2 and a Wio-SX1262 module library), confirming the 868 MHz LoRa/Meshtastic shard.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, maker-documented badge (not just a sweep snippet): the Codeberg repo and the official 39C3 congress hub project page both describe it. Could not find price, quantity made, availability/sold-out status, a firmware repo, display part/size, or any photo of the assembled hardware — the repository''s Resources folder holds only design-guide assets (fonts, logos, style-guide files) and component datasheet images, not photos of the finished badge. Duplicates entry ccc-congress-2025-39c3-cyberwatch-badge, which covers the same badge under a different event-id folder for the same congress.'
last_modified_date: '2026-09-08'
---

The Cyberwatch is a solder-it-yourself badge built by Fachschaft GAF∧Friends, a Munich (LMU München) student group, for 39C3 (the 39th Chaos Communication Congress) in Hamburg, December 2025. It is shaped and worn like a smartwatch, built around an ESP32-C6-WROOM-1 module. Its distinguishing feature is a motherboard with an SD-card-reader-style slot: because a PCB and a standard SD card are roughly the same thickness, the team designed small daughterboards ("shards") that plug into that slot to swap in different functionality, panelized alongside the mainboard for single-run manufacturing. One documented shard adds a LoRa radio (the design includes both an RFM95W 868 MHz module and a Wio-SX1262 module option) for Meshtastic-style mesh networking.

The badge also carries a small display (the maker's assembly notes say to solder it last, with tape underneath to avoid shorts) and a single back-mounted RGB LED, plus onboard LiPo charging and battery-disconnect circuitry. The hardware is fully open: KiCad schematics, PCB layout, and a print-ready assembly PDF are published on the team's Codeberg repository, alongside the 39C3 congress style-guide assets used for the board art. No firmware repository, price, production quantity, or post-congress availability information was found.
