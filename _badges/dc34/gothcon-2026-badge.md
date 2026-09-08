---
title: Gothcon 2026 Blinky Badge
id: dc34-gothcon-2026-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Gothcon
  url: https://gothconbadge.myshopify.com/
summary: A bat-shaped LED badge sold as a fundraiser for the Gothcon party at DEF CON 34, with 44 addressable RGB LEDs and a wireless "infection" feature that spreads pattern and palette choices between nearby badges.
functions: Runs a library of color-agnostic LED patterns (twinkle, wash, chase) over selectable palettes. Directional buttons cycle patterns/palettes. Over ESP-NOW, tapping the down button lets nearby badges "infect" each other with your current pattern and palette, cascading a few hops through the room; holding down for 5 seconds opts a badge out of wireless temporarily.
look:
  colors:
  - black
  shape: bat
  themes:
  - halloween
  - horror
  - wearable
tech:
  mcu: ESP32-C3
  leds:
    count: 44
    type: WS2812B
    note: 42 LEDs animate the bat body; 2 additional LEDs form independent "bat eye" indicators.
  display: none
  connectivity:
  - wifi
  - ble
  inputs:
  - buttons
  battery: LiPo 2000 mAh
  power: USB-C
  sao_version: none
get_one:
  price: $80 at DEF CON, later reduced to $40 for leftover stock
  price_usd: 80.0
  quantity: ''
  availability: limited
  availability_note: As of 2026-09-06, the Shopify store still lists leftover post-con inventory at $40, capped at 2 per order (USPS flat-rate box); no international shipping due to the battery.
  distribution:
  - purchase
  - crowdfunding
  where: Sold directly through the Gothcon Shopify store (gothconbadge.myshopify.com) as a fundraiser for the Gothcon party at DEF CON 34; remaining stock sold post-convention.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/claviger/gothcon-firmware
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: Firmware (MicroPython) is published on GitHub; no hardware files (schematic/gerbers) were found published.
links:
- label: gothconbadge.myshopify.com
  url: https://gothconbadge.myshopify.com/
  kind: store
- label: github.com/claviger/gothcon-firmware
  url: https://github.com/claviger/gothcon-firmware
  kind: repo
- label: imgur.com/a/z90WSN9
  url: https://imgur.com/a/z90WSN9
  kind: video
  archived: https://web.archive.org/web/20260723210416/https://imgur.com/a/z90WSN9
- label: x.com/@dcgothcon
  url: https://x.com/@dcgothcon
  kind: social
- label: bsky.app/profile/dcgothcon.bsky.social
  url: https://bsky.app/profile/dcgothcon.bsky.social
  kind: social
images:
- file: assets/images/badges/dc34/gothcon-2026-badge/4ad79cbdd4.jpg
  source: https://gothconbadge.myshopify.com/
  credit: Gothcon
  caption: Gothcon 2026 bat-shaped LED badge with acrylic shield
contact:
  discord: '@vylanis'
  emails:
  - claviger@perimetergrid.com
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 49
  updated: 7/23/2026 20:48:56
  listing: New
- kind: url
  url: https://gothconbadge.myshopify.com/
  title: Gothcon 2026 Blinky Badge - Shopify store
  accessed: '2026-09-06'
  note: Maker, price/availability history, battery, LED count, MCU, product photo.
- kind: url
  url: https://github.com/claviger/gothcon-firmware
  title: claviger/gothcon-firmware
  accessed: '2026-09-06'
  note: Firmware details - ESP32-C3, WS2812B LED layout, button pinout, ESP-NOW "infection" feature.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts (maker, MCU, LEDs, battery, price, functions) confirmed directly from the maker's Shopify store and GitHub firmware repo. Could not reach the imgur album, x.com (paywalled), or bsky.app links to corroborate further or find additional photos; quantity made was not stated anywhere found. Open-source hardware files (schematic/gerbers) were not located, only firmware.
last_modified_date: '2026-09-06'
---

The Gothcon 2026 Blinky Badge is a bat-shaped LED badge sold by Gothcon, the goth-themed dance party held alongside DEF CON 34 in Las Vegas, as a fundraiser for the event. Built around an ESP32-C3 with Wi-Fi and BLE, it drives 44 individually addressable WS2812B LEDs across the bat's body plus two dedicated "eye" LEDs, running a library of patterns (twinkle, wash, chase) over selectable color palettes, cycled with four directional buttons. A 2000 mAh LiPo battery, charged over USB-C, keeps the badge running for roughly 24-36 hours, and it ships with a sublimation-printed lanyard and a removable acrylic shield.

The badge's standout feature is a wireless "infection" mechanic built on ESP-NOW: tapping the down button broadcasts a badge's current pattern and palette to nearby badges, which adopt it and can pass it on in turn, letting a chosen look cascade through a room. Holding the down button for five seconds opts a badge out of this behavior temporarily. The MicroPython firmware is published on GitHub by the maker (claviger), though no hardware design files were found published alongside it.

Originally sold at DEF CON 34 for $80, leftover units were still being sold through the Gothcon Shopify store as of this check for $40, limited to two per order due to USPS flat-rate shipping constraints, with no international shipping because of the built-in battery.
