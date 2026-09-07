---
title: Shitty Kitty V2
id: dc34-shitty-kitty-v2
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Uberfoo Heavy Industries
  url: https://shop.uberfoo.net/
  role: designed by "@lipo"
summary: A cat-shaped electronic badge with two 0.96" color IPS screens and two SAO ports, built around an RP2040 and running the maker's own "SkittyOS" firmware.
functions: Dual color IPS displays running SkittyOS (graphics demos, scrolling text, customizable fonts), a five-button interface for menu navigation, two fully-featured SAO 1.69bis ports, and USB-C charging/firmware updates via mass storage.
look:
  colors:
  - green
  shape: cat
  themes:
  - cat
  - animal
  - wearable
  - sao
tech:
  mcu: RP2040
  leds: null
  display: two 0.96" 80x160 color IPS
  connectivity:
  - usb
  - i2c
  - uart
  battery: LiPo 2000 mAh
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: '75'
  price_usd: 75.0
  quantity: '15'
  availability: sold_out
  availability_note: Uberflux storefront showed out of stock as of 2026-09-06, noting 15 sold at the DEF CON 34 drop.
  distribution:
  - purchase
  where: Sold through the maker's Uberflux storefront (uberflux.com) at a DEF CON 34 drop.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/Uberfoo-Heavy-Industries/shitty-kitty
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: Firmware ("SkittyOS") is public on GitHub; no hardware/Gerbers repo was found for the V2 board specifically.
links:
- label: uberflux.com/product/UF-SK2
  url: https://uberflux.com/product/UF-SK2
  kind: store
- label: Uberfoo-Heavy-Industries/shitty-kitty (firmware)
  url: https://github.com/Uberfoo-Heavy-Industries/shitty-kitty
  kind: repo
  archived: false
- label: The Sh*%$ty Kitty Badge - DEF CON Forums
  url: https://forum.defcon.org/node/237378
  kind: article
  archived: false
images:
- file: assets/images/badges/dc34/shitty-kitty-v2/008a5e9b25.jpg
  source: https://www.uberflux.com/product/UF-SK2
  credit: Uberfoo Heavy Industries
  caption: Shitty Kitty V2 badge product photo
contact:
  discord: lipo
  emails:
  - James@uberfoo.net
notes:
- The community sheet also lists an identically-titled "Shitty Kitty V2" entry under dc33 (2025); see research.notes.
status: released
sources:
- kind: sheet
  event: dc34
  row: 18
  updated: 6/16/2026 12:51:03
  listing: New
- kind: url
  url: https://uberflux.com/product/UF-SK2
  title: Shitty Kitty V2 - Uberflux storefront listing
  accessed: '2026-09-06'
  note: Confirmed price ($75), RP2040 MCU, dual 0.96in IPS screens, dual SAO 1.69bis ports, LiPo battery, five buttons, out-of-stock status, and that 15 units were sold at the DEF CON 34 drop.
- kind: url
  url: https://github.com/Uberfoo-Heavy-Industries/shitty-kitty
  title: Uberfoo-Heavy-Industries/shitty-kitty (GitHub)
  accessed: '2026-09-06'
  note: Firmware repo for "Shitty OS" / SkittyOS; confirms it is reprogrammable over USB (appears as a serial port / mass storage device).
- kind: url
  url: https://forum.defcon.org/node/237378
  title: The Sh*%$ty Kitty Badge - DEF CON Forums
  accessed: '2026-09-06'
  note: Community forum thread discussing the Shitty Kitty badge line and its reprogrammable USB-serial interface.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: |
    Core specs (RP2040, dual IPS screens, dual SAO ports, $75, 15 sold, sold out) are confirmed by the maker's own storefront listing, which explicitly attributes the sell-out to "the DEF CON 34 drop" - supporting this entry's dc34 placement. However, an identical title ("Shitty Kitty V2", same maker) also appears on the dc33 (2025) community sheet as row 7; a web search noted "more units...released for pick-up at DEF CON 33" for the same product, suggesting Shitty Kitty V2 may have first shipped at DC33 and continued selling/being distributed at DC34, with the sheet capturing it in both years. Could not find hardware Gerbers/BOM, LED specifics (the board appears to have no addressable LEDs, only the two IPS displays and a status LED near the audio jack, unconfirmed), or a maker-published photo beyond the single storefront product shot. eda_tool and license not stated anywhere found.
last_modified_date: '2026-09-06'
related:
- dc33-shitty-kitty-v2
---

Shitty Kitty V2 is a cat-shaped badge from Uberfoo Heavy Industries, designed by the maker known as "@lipo." It replaces the original 2021 Shitty Kitty's STM32 board with a Raspberry Pi RP2040, and adds a second screen: two 0.96" 80x160 color IPS displays sit where the original cat's eyes would be, driven by the maker's own "SkittyOS" firmware, which ships with graphics demos, scrolling text, and customizable fonts. A row of five buttons handles menu navigation, and the board carries two fully-featured SAO 1.69bis ports so it can host other badges' add-ons. Power comes from a 2000 mAh LiPo battery charged over USB-C, and the same port doubles as a mass-storage interface for firmware updates.

The badge sold for $75 through the maker's Uberflux storefront, where the listing notes 15 units sold at "the DEF CON 34 drop" before going out of stock. An identically-named listing also exists on the DEF CON 33 (2025) community sheet from the same maker, and outside reporting mentions further Shitty Kitty V2 units being released for pickup at DEF CON 33, so this may be a badge that first appeared at DC33 and continued to be sold/distributed into DC34 rather than two distinct designs; see the research notes on the DC33 entry for the parallel listing.

## Make your own

Hardware files (schematic/Gerbers/BOM) were not found published anywhere searched, but the firmware, "SkittyOS," is open source on GitHub at Uberfoo-Heavy-Industries/shitty-kitty. The badge enumerates as a USB serial device and can be controlled with a terminal program (e.g. PuTTY or `screen`); the repo's README documents reflashing it via USB DFU/mass-storage mode.
