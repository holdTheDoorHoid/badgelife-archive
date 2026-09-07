---
title: UberBox Badge
id: dc32-uberbox-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Uberfoo Heavy Industries
  url: https://github.com/Uberfoo-Heavy-Industries
summary: A DEF CON 32 badge from Uberfoo Heavy Industries built on Espressif's ESP32-S3-BOX-3 reference hardware, with a color screen for text messaging, retro demoscene-style graphics, and a configurable name display.
functions: Broadcast text messaging, retro demo scene like graphics, and of course configurable name display
look:
  colors:
  - white
  - black
  shape: rectangle
  themes:
  - retro computer
  - text
tech:
  mcu: ESP32-S3
  leds: null
  display: color LCD (ESP32-S3-BOX-3 hardware)
  connectivity:
  - wifi
  - bluetooth
  battery: null
  sao_version: null
get_one:
  price: $70.00
  price_usd: 70.0
  quantity: ''
  availability: sold_out
  availability_note: Storefront no longer lists the item as of an Oct 2025 archive snapshot, and shop.uberfoo.net itself returns "This store is unavailable" as of 2026-09-07.
  distribution:
  - purchase
  where: Sold directly through the maker's Shopify storefront (shop.uberfoo.net/products/boxy-badge) under the internal name "boxy-badge."
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/Uberfoo-Heavy-Industries/esp-s3-box-badge
  eda_tool: null
links:
- label: shop.uberfoo.net/products/boxy-badge
  url: https://shop.uberfoo.net/products/boxy-badge
  kind: store
- label: esp-s3-box-badge firmware (GitHub)
  url: https://github.com/Uberfoo-Heavy-Industries/esp-s3-box-badge
  kind: repo
- label: Uberfoo Heavy Industries (GitHub org)
  url: https://github.com/Uberfoo-Heavy-Industries
  kind: repo
  archived: https://web.archive.org/web/20260615181704/https://github.com/Uberfoo-Heavy-Industries
images:
- file: assets/images/badges/dc32/uberbox-badge/a31698c9b4.jpg
  source: https://web.archive.org/web/20240725093826/https://shop.uberfoo.net/
  credit: Uberfoo Heavy Industries
  caption: UberBox Badge product photo from the Uberfoo storefront (archived July 2024)
contact:
  emails:
  - shop@uberfoo.net
notes: []
status: released
sources:
- kind: sheet
  event: dc32
  row: 110
  updated: '2024-07-24'
- kind: url
  url: https://web.archive.org/web/20240725093826/https://shop.uberfoo.net/
  title: Uberfoo Heavy Industries storefront (Wayback Machine, 2024-07-25)
  accessed: '2026-09-07'
  note: Confirms product title "UberBox Badge," internal slug "boxy-badge," price $70.00, and product photo; the live shop.uberfoo.net/products/boxy-badge page was never itself archived and returns 404/503.
- kind: url
  url: https://github.com/Uberfoo-Heavy-Industries
  title: Uberfoo Heavy Industries (GitHub organization)
  accessed: '2026-09-07'
  note: Maker's GitHub org, hosting badge firmware repos including esp-s3-box-badge, Z80-Retro-Badge, and shitty-kitty.
  archived: https://web.archive.org/web/20260615181704/https://github.com/Uberfoo-Heavy-Industries
- kind: url
  url: https://github.com/Uberfoo-Heavy-Industries/esp-s3-box-badge
  title: esp-s3-box-badge (GitHub repo)
  accessed: '2026-09-07'
  note: Firmware repo (ESP-IDF, C/C++) targeting Espressif's ESP32-S3-BOX-3 dev hardware (sdkconfig.ci.box-3), with source files named message.h, demo/, and ui/ matching the badge's text-messaging and demoscene-graphics functions. Created 2024-07-08, last pushed 2024-09-26, shortly around DEF CON 32 (Aug 2024).
- kind: url
  url: https://shop.uberfoo.net
  title: shop.uberfoo.net (checked live)
  accessed: '2026-09-07'
  note: The storefront domain now returns a Shopify "This store is unavailable" error page; the maker's shop appears closed.
  archived: https://web.archive.org/web/20251020014350/https://shop.uberfoo.net/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The live product page (shop.uberfoo.net/products/boxy-badge) was never captured by the Wayback Machine and the storefront itself is now offline, so price/title/photo come from an archived homepage listing rather than the product page itself. No hardware files (schematics/Gerbers) were found, only the firmware repo, which is built on Espressif's ESP32-S3-BOX-3 reference design rather than a fully custom PCB — it is unclear whether Uberfoo designed original hardware or repurposed/enclosed the stock Espressif dev board. LED info, battery/power details, and exact display size could not be confirmed from any source read.
last_modified_date: '2026-09-07'
---

The UberBox Badge was Uberfoo Heavy Industries' entry for DEF CON 32 (2024), sold for $70 through the maker's own Shopify storefront under the product slug "boxy-badge." It pairs a color screen with buttons in a boxy, wearable enclosure (worn on a lanyard, per the maker's own product photo), and its advertised functions — broadcast text messaging, retro demoscene-style graphics, and a configurable name display — line up with the file layout of the maker's public firmware repository, which includes a `message.h`, a `demo/` directory, and a `ui/` directory.

The firmware repo, `esp-s3-box-badge`, targets Espressif's ESP32-S3-BOX-3 reference hardware (an ESP32-S3 based Wi-Fi/Bluetooth platform with a built-in color LCD), and was created in early July 2024, just ahead of that year's DEF CON, with commits continuing into late September. This strongly suggests the badge is built on or adapted from that Espressif dev-kit design rather than a badge PCB laid out from scratch, though no hardware files were published alongside the firmware to confirm the exact relationship.

By late 2025 the badge had disappeared from the storefront's product listing, and as of this research the shop.uberfoo.net domain itself returns a Shopify "store unavailable" page, indicating the maker's shop has since closed. Uberfoo Heavy Industries also produced the Z80 Retro Badge (DC30/DC31) and the Shitty Kitty badges (DC33/DC34).

## Make your own

Firmware source is public at [esp-s3-box-badge](https://github.com/Uberfoo-Heavy-Industries/esp-s3-box-badge) (ESP-IDF project in C/C++, built against Espressif's ESP32-S3-BOX-3 SDK configuration). No hardware design files (schematics, PCB, enclosure) were found published by the maker.
