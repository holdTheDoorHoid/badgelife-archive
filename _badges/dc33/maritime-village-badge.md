---
title: Differential Destroyer
id: dc33-maritime-village-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Maritime Hacking Village
  url: https://maritimehackingvillage.com/
summary: An open-source badge built around a Raspberry Pi Pico 2 that doubles as a real protocol-hacking and voltage-fault-injection tool for maritime and industrial bus standards (NMEA2000, NMEA0183, Modbus RTU, CAN bus).
functions: Pre-order your MHV village badge for DEF CON 33! This year’s badge (actual pictures shown) is an open-source embedded system for maritime security research, featuring interfaces for NMEA2000, NMEA0183, Modbus RTU, and CAN bus with unprecedented symbol-level CAN fault injection capabilities. We went a little crazy with it — and it turned out incredible. We can’t wait to see it on you.
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
  - hardware tool
  - village badge
  - ctf
tech:
  mcu: Raspberry Pi Pico 2
  leds:
    count: 9
    type: WS2812B
    note: 9 addressable WS2812B NeoPixels plus 6 single-color status LEDs (battery, differential injector, CAN Tx/Rx, differential receiver)
  display: 1.9" 320x170 TFT LCD
  connectivity:
  - usb
  - i2c
  - sub-ghz
  battery: JST-PH 2-pin rechargeable battery connector, onboard charging
  sao_version: null
get_one:
  price: $300 preorder (DC33) / $225 sale, originally $250 (DC34 leftover stock)
  price_usd: 300.0
  quantity: unknown; described by the maker as "one of the very last ones ever created" when resold at DEF CON 34
  availability: sold_out
  availability_note: Checked 2026-09-06 — sold out on the MHV Squarespace shop.
  distribution:
  - preorder
  - purchase
  - village
  where: Preordered online for DEF CON 33 (2025) via the MHV shop, then remaining units sold in person at DEF CON 34 (2026) as the "Differential Destroyer Badge."
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Maritime-Hacking-Village/Badge-2025
  firmware_url: https://github.com/Maritime-Hacking-Village/Badge-2025
  eda_tool: KiCad
  notes: 'Hardware licensed CERN-OHL-W; Rust firmware dual-licensed Apache-2.0 / MIT.'
links:
- label: maritimehackingvillage.com/shop/p/badge-dc33
  url: https://maritimehackingvillage.com/shop/p/badge-dc33
  kind: store
- label: Differential Destroyer Badge (MHV shop, DC34 listing)
  url: https://maritimehackingvillage.com/shop/p/differential-destroyer-badge
  kind: store
- label: Badge-2025 hardware/firmware repo (GitHub)
  url: https://github.com/Maritime-Hacking-Village/Badge-2025
  kind: repo
images:
- file: assets/images/badges/dc33/maritime-village-badge/1d7713aaf1.jpg
  source: "https://maritimehackingvillage.com/shop/p/differential-destroyer-badge"
  credit: "Maritime Hacking Village"
  caption: "The Differential Destroyer / MHV DC33 badge, main product photo"
- file: assets/images/badges/dc33/maritime-village-badge/0738efe15a.jpg
  source: "https://maritimehackingvillage.com/shop/p/differential-destroyer-badge"
  credit: "Maritime Hacking Village"
  caption: "PCB render of the Differential Destroyer badge"
contact: {}
notes:
- 'List Makers Note: as a retired naval officer, folks have absolutely no idea just how much of the stuff you use everyday requires free sea routes. These folks went all out on this badge and hacking it will show just how much goes into making sure the stuff you want makes it to your house.'
- 'The sheet listed this maker as "Maritime Village"; their own materials use "Maritime Hacking Village" (MHV).'
- 'The maker''s shop currently lists this same design (matching functions text almost verbatim) under the name "Differential Destroyer Badge," sold at DEF CON 34 as leftover stock from the DC33 preorder run, at a discounted $225 (from $250) rather than the original $300 preorder price. The original badge-dc33 shop URL from the sheet now 404s.'
status: released
sources:
- kind: sheet
  event: dc33
  row: 57
  updated: 7/31/2025
- kind: url
  url: https://maritimehackingvillage.com/shop/p/differential-destroyer-badge
  title: Differential Destroyer Badge - MHV Shop
  accessed: '2026-09-06'
  note: Confirms this is the same design as the DC33 preorder badge (matching functions text), gives price, sold-out status, and open-source repo link.
- kind: url
  url: https://github.com/Maritime-Hacking-Village/Badge-2025
  title: Maritime-Hacking-Village/Badge-2025 (GitHub)
  accessed: '2026-09-06'
  note: Hardware/firmware repo; supplied MCU, display, LED counts, connectivity, power, and license details.
- kind: url
  url: https://maritimehackingvillage.com/shop/p/badge-dc33
  title: MHV shop - badge-dc33 (dead link)
  accessed: '2026-09-06'
  note: Original sheet URL now returns HTTP 404; superseded by the differential-destroyer-badge listing.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Original badge-dc33 shop URL from the sheet is dead (404) and not in the Wayback Machine. Identified via the MHV shop''s current "Differential Destroyer Badge" listing, whose description matches the sheet''s functions text (NMEA2000, NMEA0183, Modbus RTU, CAN bus fault injection) almost word for word, and confirmed against the maker''s Badge-2025 GitHub repo for hardware specifics. Exact production quantity was not disclosed by the maker; the DC34 listing calls remaining stock "one of the very last ones ever created." Colors, shape, and SAO header presence were not stated by any source and are left empty.'
last_modified_date: '2026-09-06'
---

The Differential Destroyer is the DEF CON 33 (2025) badge from the Maritime Hacking Village (MHV), built around a Raspberry Pi Pico 2 with a 1.9" color TFT display, a joystick, an accelerometer, and 9 WS2812B RGB LEDs alongside 6 single-color status indicators. It is not a novelty badge: it is a working protocol-analysis and fault-injection tool for the buses that run ships and industrial equipment, supporting NMEA2000, NMEA0183, Modbus RTU, and standard CAN bus (via an MCP2518FD CAN-FD transceiver), with a differential injector circuit capable of driving fault voltages onto those buses at up to 5 MHz in 0.5V steps. Badge behavior and the injection engine are scriptable through an embedded Rhai interpreter written in Rust.

MHV took preorders for the badge ahead of DEF CON 33 at $300, framed as funding the village's presence at the con. The same design resurfaced at DEF CON 34 as the "Differential Destroyer Badge," sold in person out of leftover DC33 stock at a discounted $225 and described by the maker as one of the last units left; it is now sold out on the MHV shop. The original DC33 preorder page from the community sheet no longer resolves.

## Make your own

Hardware (KiCad, CERN-OHL-W licensed) and Rust firmware (Apache-2.0 / MIT) are published at github.com/Maritime-Hacking-Village/Badge-2025.
