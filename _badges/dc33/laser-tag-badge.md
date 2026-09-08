---
title: Laser* Tag Badge
id: dc33-laser-tag-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: dani.pink
  url: https://www.dani.pink/lasertag
summary: An independent DEF CON 33 badge that turns wearers into infrared laser-tag players, tallying hits on an unofficial online leaderboard.
functions: Multiplayer laser* tag game during defcon, with online** scoring. Also rechargeable power for two SAO ports.
look:
  colors:
  - black
  shape: circle
  themes:
  - ctf
  - wearable
  - game
tech:
  mcu: RP2350
  leds:
    count: 30
    type: RGB
    note: Drives the ring around the 1.28" round LCD.
  display: 1.28" round LCD (240x240, GC9A01 driver)
  connectivity:
  - ir
  battery: 18650 rechargeable
  sao_version: v1
  sao_ports: 2
get_one:
  price: '45'
  price_usd: 45.0
  quantity: ''
  availability: unknown
  distribution:
  - preorder
  where: Sold directly by the maker via a Google Form on the badge's landing page (dani.pink/lasertag).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: The maker documents the badge's IR tagging protocol as "OpenLASIR" at github.com/danielweidman/OpenLASIR (hardware/firmware for the badge itself is not published; a third-party Rust reimplementation of the protocol exists at github.com/rjzak/openlasir-rs).
links:
- label: www.dani.pink/lasertag
  url: https://www.dani.pink/lasertag
  kind: website
- label: 2025 (DC33) archive page
  url: https://www.dani.pink/lasertag/archive-2025/about
  kind: website
  archived: https://web.archive.org/web/20260430093235/https://www.dani.pink/lasertag/archive-2025/about
- label: OpenLASIR protocol (GitHub)
  url: https://github.com/danielweidman/OpenLASIR
  kind: repo
images:
- file: assets/images/badges/dc33/laser-tag-badge/281e39ccfc.jpg
  source: https://www.dani.pink/lasertag/archive-2025
  credit: Dani Weidman
  caption: Laser* Tag Badge, front view
- file: assets/images/badges/dc33/laser-tag-badge/c3e6183951.jpg
  source: https://www.dani.pink/lasertag/archive-2025
  credit: Dani Weidman
  caption: Laser* Tag Badge, angled view
contact:
  emails:
  - palm12341@gmail.com
notes:
- Landing page has a Google Form to register interest/reserve!
status: released
sources:
- kind: sheet
  event: dc33
  row: 10
  updated: 6/18/2025 10:06:42
- kind: url
  url: https://www.dani.pink/lasertag
  title: Laser* Tag Badge DS - dani.pink
  accessed: '2026-09-06'
  note: Current landing page (now describes the DC34/2026 successor, "Laser* Tag Badge DS"); confirms maker and general concept.
- kind: url
  url: https://www.dani.pink/lasertag/archive-2025/about
  title: Laser* Tag Badge - About (archived 2025 / DC33 page)
  accessed: '2026-09-06'
  note: 'Primary source for the DC33 (2025) badge specifically: hardware list (RP2350 on a Waveshare RP2350-Zero daughterboard, VSLY5940 IR emitter + IR receiver, 30 RGB LEDs, 1.28" round GC9A01 LCD, 5-way switch + SYNC button, 18650 battery, vibration motor, piezo buzzer, 2 power-only SAO ports), gameplay rules, and confirmation that 2025 scoring was manual QR-code sync only (no LoRa auto-sync, which was added for the 2026/DC34 successor). No price, quantity, or color options were stated on this page.'
  archived: https://web.archive.org/web/20260430093235/https://www.dani.pink/lasertag/archive-2025/about
- kind: url
  url: https://github.com/danielweidman/OpenLASIR
  title: danielweidman/OpenLASIR
  accessed: '2026-09-06'
  note: Maker's GitHub repo documenting the IR "OpenLASIR" tagging protocol used by the badge.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Core hardware and gameplay confirmed from the maker's own archived 2025 page. Price ($45) and the "reserve via Google Form" note come from the original community sheet and could not be independently re-verified (the live site no longer shows 2025 pricing/ordering, and no storefront/press coverage of the 2025 sale was found). Quantity made, exact PCB colors beyond the visible black solder mask, and open hardware/firmware files for the badge itself (as opposed to the OpenLASIR protocol docs) were not found. A 2026/DC34 successor, "Laser* Tag Badge DS," already has its own archive entry (dc34-laser-tag-ds) and is not this item.
last_modified_date: '2026-09-06'
---

The Laser* Tag Badge is an independent, non-official DEF CON 33 (2025) badge by dani.pink (Dani Weidman, with help from Zach Resmer) that turns the con floor into a casual game of infrared laser tag. Each badge carries a narrow-beam IR emitter and receiver: wearers earn points by tagging other badge wearers, with bonus value for tagging more unique people per hour. Because there's no real-time network link, players periodically pull up a QR code on the badge's round display and scan it to upload their hit record to an online leaderboard.

Hardware-wise the badge is built around an RP2350 on a Waveshare RP2350-Zero daughterboard, with a 1.28" round GC9A01 LCD as the main display, a ring of 30 RGB LEDs, a 5-way directional switch plus a dedicated SYNC button, a vibration motor and piezo buzzer for hit feedback, and a rechargeable 18650 cell. Two SAO ports on the badge supply power to accessories (I2C requires manually bridging a jumper). The maker documents the IR protocol behind the tagging system as "OpenLASIR," which has since drawn a third-party Rust reimplementation.

The badge was sold directly by the maker, advertised at $45 with interest/reservation collected through a Google Form linked from the badge's own site; the community sheet is the only source for that price, and no independent listing, quantity, or sell-out status could be confirmed. The 2025 badge's landing page has since been superseded by a 2026/DC34 successor ("Laser* Tag Badge DS," a separate archive entry) that adds automatic LoRa score-syncing; the original 2025 material is preserved at dani.pink's "archive-2025" page, which is the main source used here.
