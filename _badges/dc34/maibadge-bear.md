---
title: maibadge-bear
id: dc34-maibadge-bear
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Hackin7 (HCKBADGES)
  url: https://github.com/maibadge
summary: A bear-shaped electronic badge themed after the maimai arcade rhythm game, sold by Hackin7 for DEF CON 34 in kit, partially-soldered, and fully-soldered variants.
functions: Addressable LED animations (rainbow, chase, comet, pulse); the fully-soldered variant adds a round display that plays back custom images/video; simpler variants play tones and LED animations.
look:
  colors: []
  shape: bear
  themes:
  - animal
  - arcade
  - retro computer
  - mascot
tech:
  mcu: ESP32-S3
  leds:
    count: null
    type: addressable
    note: 'GPIO15 drives the LED chain on the bear_v1 board; firmware supports rainbow, chase, comet and pulse animations.'
  display: 1.28" round LCD (GC9A01A controller)
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: '$20 (no display) / $35 (kit, MCU + display unsoldered) / $40 (fully soldered)'
  price_usd: 20
  quantity: ''
  availability: available
  availability_note: 'Uberflux listing checked 2026-09-07: 22 of the $20 tier remaining (7 sold), 4 remaining of the $35 tier (2 sold), 9 remaining of the $40 tier (4 sold).'
  distribution:
  - purchase
  where: Sold via Hackin7's Uberflux storefront.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/maibadge/maibadge
  firmware_url: https://github.com/maibadge/maibadge/tree/main/code/circuitpython-full-slop-port
  eda_tool: null
  notes: 'The maibadge GitHub repo covers two PCB shapes (bear_v1 and machine_v2) with a shared CircuitPython firmware port; the bear board uses GPIO15 for its LED chain.'
links:
- label: uberflux.com/product/HCK-maibadge-bear
  url: https://uberflux.com/product/HCK-maibadge-bear
  kind: store
- label: maibadge/maibadge (GitHub)
  url: https://github.com/maibadge/maibadge
  kind: repo
images:
  - file: assets/images/badges/dc34/maibadge-bear/2ee07fd76d.jpg
    source: "https://uberflux.com/product/HCK-maibadge-bear"
    credit: "Hackin7 / Uberflux"
    caption: "maibadge-bear product photo"
  - file: assets/images/badges/dc34/maibadge-bear/fccf82a7e3.jpg
    source: "https://uberflux.com/product/HCK-maibadge-bear"
    credit: "Hackin7 / Uberflux"
    caption: "maibadge-bear, alternate view"
contact: {}
notes:
- 'Uberflux. $20, status: upcoming drop.'
status: announced
sources:
- kind: url
  url: https://uberflux.com/product/HCK-maibadge-bear
  title: maibadge-bear
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://uberflux.com/product/HCK-maibadge-bear
  title: maibadge-bear product page
  accessed: '2026-09-07'
  note: 'Confirmed maker (Hackin7), event (DEF CON 34), pricing tiers and stock counts, and gathered product photos.'
- kind: url
  url: https://github.com/maibadge/maibadge
  title: maibadge/maibadge
  accessed: '2026-09-07'
  note: 'Open-source hardware/firmware repo; confirms two PCB shapes (bear_v1, machine_v2) and CircuitPython firmware.'
- kind: url
  url: https://github.com/maibadge/maibadge/tree/main/code/circuitpython-full-slop-port
  title: circuitpython-full-slop-port
  accessed: '2026-09-07'
  note: 'Confirms ESP32-S3 MCU, GC9A01A display controller, GPIO15 LED pin on the bear board, and supported LED animation modes.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Bear-shaped badge themed after the maimai arcade rhythm game, part of a maibadge line (bear + machine shapes) by Hackin7/HCKBADGES for DEF CON 34 (2026). Uberflux listing describes the fully-soldered variant loosely as "OLED"; the maibadge firmware repo instead documents a GC9A01A-driven round LCD, so the display line follows the repo. LED count is not stated anywhere found; only the driving GPIO and animation modes are documented. Quantity made overall is not stated, only per-tier remaining/sold counts on the storefront at time of check.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/maibadge-bear/
---

The maibadge-bear is a bear-shaped electronic badge from Hackin7 (HCKBADGES), themed after maimai, the touch-panel arcade rhythm game, and sold for DEF CON 34 (2026) through Hackin7's Uberflux storefront. It ships in three tiers: a $20 board with no display that still runs LED animations and simple tone playback, a $35 kit with the ESP32-S3 and round display left for the buyer to solder, and a $40 fully-assembled version.

Hardware and firmware are open source under the `maibadge/maibadge` GitHub organization, which covers both this bear-shaped PCB (`bear_v1`) and a companion machine-shaped board (`machine_v2`) themed after the maimai cabinet itself, sharing a CircuitPython firmware port. The bear board is built around an ESP32-S3, drives its addressable LEDs from GPIO15 with rainbow, chase, comet, and pulse animation modes, and drives a round GC9A01A-controller LCD capable of showing custom images and video on the fully-soldered variant.

## Make your own

Both PCB designs and a shared CircuitPython firmware port live in the `maibadge/maibadge` repository, with the bear firmware under `code/circuitpython-full-slop-port`. The firmware notes call out checking the fitted ESP32-S3's flash/PSRAM memory suffix before selecting or flashing a CircuitPython build.
