---
title: Tanmatsu
id: why-2025-tanmatsu-why2025-badge-pcb-design
layout: badge
parent: Why 2025
grand_parent: Badge Archive
nav_exclude: true
type: other
event: why-2025
year: 2025
makers:
- name: Renze Nicolai and Paul Honig / badge.team / Nicolai Electronics
  url: https://nicolaielectronics.nl/tanmatsu/
summary: A handheld ESP32-P4 "pocket terminal" with a QWERTY keyboard, MIPI DSI
  display, and LoRa radio, originally designed by badge.team as the planned
  WHY2025 conference badge before a dispute split it off into a standalone
  commercial product sold by Nicolai Electronics.
functions: General-purpose hacking/development terminal; runs a launcher firmware
  with OTA updates; supports hot-swappable "personality" expansion modules,
  QWIIC/PMOD/SAO expansion ports, and LoRa-based wireless communication.
look:
  colors:
  - black
  - white
  - blue
  shape: rectangle
  themes:
  - retro computer
  - hardware tool
  - radio
tech:
  mcu: ESP32-P4 (+ ESP32-C6 radio co-processor)
  leds: null
  display: 800x480 MIPI DSI LCD, 16-bit color
  connectivity:
  - wifi
  - ble
  - lora
  - zigbee
  - i2c
  battery: null
  sao_version: null
get_one:
  price: "€120 (€99 excl. VAT)"
  price_usd: null
  quantity: ''
  availability: available
  distribution:
  - purchase
  where: Sold directly by Nicolai Electronics' web shop (shop.nicolaielectronics.nl),
    originating from the badge.team/Konsool hardware lineage.
make_your_own:
  open_source: null
  hardware_url: https://github.com/Nicolai-Electronics/tanmatsu-documentation
  firmware_url: https://github.com/badgeteam/esp32-component-badge-bsp
  eda_tool: null
links:
- label: media.ccc.de/v/2025-188-tanmatsu-why2025-badge-pcb-design
  url: https://media.ccc.de/v/2025-188-tanmatsu-why2025-badge-pcb-design
  kind: video
- label: Tanmatsu — Nicolai Electronics
  url: https://nicolaielectronics.nl/tanmatsu/
  kind: website
- label: Tanmatsu documentation — specifications
  url: https://docs.tanmatsu.cloud/hardware/specifications/
  kind: doc
- label: A Closer Look At The Tanmatsu — Hackaday
  url: https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/
  kind: article
images:
  - file: assets/images/badges/why-2025/tanmatsu-why2025-badge-pcb-design/77501b01e4.jpg
    source: "https://nicolaielectronics.nl/tanmatsu/"
    credit: "Nicolai Electronics"
    caption: "Tanmatsu handheld terminal device"
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'Sweep''s title was "Tanmatsu (WHY2025 badge PCB design)", taken from the
  media.ccc.de talk title; the maker calls the device simply "Tanmatsu".'
- 'DUPLICATE: this is the same device already covered at
  other/konsool-tanmatsu.md ("Konsool / Tanmatsu"). See duplicate_of in the
  research report.'
status: released
sources:
- kind: url
  url: https://media.ccc.de/v/2025-188-tanmatsu-why2025-badge-pcb-design
  title: Tanmatsu (WHY2025 badge PCB design)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://nicolaielectronics.nl/tanmatsu/
  title: Tanmatsu — Nicolai Electronics
  accessed: '2026-09-10'
  note: Maker's product page; MCU, display, connectivity, price, inputs.
- kind: url
  url: https://hackaday.com/2025/02/04/a-closer-look-at-the-tanmatsu/
  title: A Closer Look At The Tanmatsu
  accessed: '2026-09-10'
  note: Confirms Tanmatsu was destined to be the WHY2025 badge before badge.team
    split from the WHY2025 organizers, becoming a standalone product.
- kind: url
  url: https://badge.team/docs/badges/why2025/
  title: badge.team's resignation letter from WHY2025 Team:Badge
  accessed: '2026-09-10'
  note: Primary-source confirmation that badge.team resigned from the official
    WHY2025 badge project.
- kind: url
  url: https://hackaday.com/2025/08/12/when-a-badge-misses-the-mark-why-2025/
  title: The WHY 2025 Badge And Its 18650s
  accessed: '2026-09-10'
  note: Confirms a different team ultimately built the actual WHY2025 badge
    after badge.team's exit.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: The linked media.ccc.de page is a conference talk about the PCB design,
    not the item's own page; the underlying device (Tanmatsu) is well documented
    on the maker's site. Important context, not a badgelife item confusion but
    a lineage split - Tanmatsu was designed to become the official WHY2025
    badge, but badge.team resigned from the WHY2025 Team:Badge project in
    early 2025 over a dispute with organizers, and Tanmatsu continued as an
    independent commercial product instead. The actual badge handed out at
    WHY2025 was built by a different team and is a separate item (not covered
    here). This entry duplicates other/konsool-tanmatsu.md, which already
    documents the same device under the "Konsool / Tanmatsu" title with the
    fuller maker credit list (Renze Nicolai, Paul Honig, Julian Scheffers, et
    al.). LED info and exact battery/mAh spec were not found on the pages
    checked. Event kept as why-2025 per the design lineage; it was never
    actually distributed as the WHY2025 attendee badge.
last_modified_date: '2026-09-10'
---

Tanmatsu is a handheld "pocket terminal" built around Espressif's ESP32-P4 application processor (dual-core RISC-V, 768 KB SRAM, 32 MB PSRAM) paired with an ESP32-C6 radio co-processor for Wi-Fi 6, Bluetooth LE 5, and Thread/Zigbee. It has an 800x480 MIPI DSI color LCD, a metal-dome QWERTY keyboard, a LoRa radio (868/915 MHz or 433 MHz variants), and expansion via QWIIC, PMOD, and SAO connectors plus swappable internal "personality modules."

The device traces back to badge.team, the Dutch collective behind many European congress badges, and was originally being developed as the badge for WHY2025 ("What Hackers Yearn"). In early 2025, badge.team's core team publicly resigned from the WHY2025 Team:Badge project over a dispute with the event organizers and IFCAT, splitting Tanmatsu off from the WHY2025 badge program. Renze Nicolai continued the hardware independently through Nicolai Electronics, which now sells assembled Tanmatsu units directly (around €120) with an ESP-IDF-based launcher firmware and OTA update support. The badge that WHY2025 attendees actually received in August 2025 was a separate device built by a different team, and drew its own coverage for battery-safety issues with its 18650 cells.

This entry was created from a media.ccc.de recording of a HackerHotel 2025 talk by Renze Nicolai and Paul Honig about the Tanmatsu PCB design process. The device itself is already documented in this archive under `other/konsool-tanmatsu.md`.
