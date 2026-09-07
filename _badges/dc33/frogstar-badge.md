---
title: Frogstar Badge
id: dc33-frogstar-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: BigTaro's Badges
  url: https://bigtaro.net
summary: An unofficial DEF CON 33 electronic badge with a frog theme, built around a round LCD, frog-themed CTF, and a built-in Frogger-like game.
functions: Frog-themed Capture the Flag to unlock GIFs and bling, a built-in frogger-like game, and two SAO expansion ports for add-ons
look:
  colors:
  - green
  shape: circle
  themes:
  - animal
  - frog
  - ctf
  - meme
tech:
  mcu: Raspberry Pi RP2350
  leds:
    count: null
    type: WS2812B
    note: Addressable RGB "bling" LEDs
  display: 1.28" round LCD (GC9A01, 240x240)
  connectivity:
  - ir
  battery: null
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: $80
  price_usd: 80.0
  quantity: '30+ (19 remaining, 11 sold as of 2026-09-06 on UberFlux)'
  availability: available
  availability_note: Checked 2026-09-06; in stock on UberFlux (19 remaining) and listed on Tindie.
  distribution:
  - purchase
  where: Sold online through Tindie and UberFlux stores; not distributed at the con itself (unofficial badge, does not grant entry).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://bigtaro.net/frogstar25/FrogStarFirmware1.0.uf2
  eda_tool: null
links:
- label: bigtaro.net/frogstar25
  url: https://bigtaro.net/frogstar25
  kind: website
- label: Tindie listing
  url: https://www.tindie.com/products/bigtaro/frogstar-badge/
  kind: store
- label: UberFlux listing
  url: https://uberflux.com/product/BT-frogstar
  kind: store
- label: Bluesky (@bigtaro.bsky.social)
  url: https://bigtaro.bsky.social
  kind: social
images:
- file: assets/images/badges/dc33/frogstar-badge/b38eb78a61.jpg
  source: "https://bigtaro.net/frogstar25"
  credit: "BigTaro's Badges"
  caption: "FrogStar 2025 hardware badge with round LCD display"
contact:
  emails:
  - psymastr@hotmail.com
notes:
- '*ribbit*'
status: released
sources:
- kind: sheet
  event: dc33
  row: 20
  updated: 7/10/2025 11:23:38
- kind: url
  url: https://bigtaro.net/frogstar25
  title: "BigTaro's FrogStar 2025 Badge"
  accessed: '2026-09-06'
  note: Maker's own project page; features, specs, firmware download, store links.
- kind: url
  url: https://uberflux.com/product/BT-frogstar
  title: FrogStar Badge - UberFlux
  accessed: '2026-09-06'
  note: Price ($80), stock count (19 remaining / 11 sold), shipping.
- kind: url
  url: https://www.tindie.com/products/bigtaro/frogstar-badge/
  title: FrogStar Badge - Tindie
  accessed: '2026-09-06'
  note: Confirms price ($80), seller location (Denver, CO), unofficial-badge disclaimer.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Price differs from the community sheet ($120) vs. the maker''s own stores (Tindie and UberFlux both list $80); used the maker''s stores as the more authoritative current price. LED count not stated anywhere found. No hardware design files (schematics/Gerbers) found published, only compiled firmware (.uf2); open_source set to partial on that basis. Quantity is an estimate from a single UberFlux stock snapshot (19 remaining + 11 sold), not a maker-stated total run size.'
last_modified_date: '2026-09-06'
---

The FrogStar Badge is BigTaro's Badges' unofficial DEF CON 33 entry, built around a Raspberry Pi RP2350 driving a 1.28" round LCD (GC9A01, 240x240). It leans fully into a frog theme: a frog-themed Capture the Flag unlocks GIFs and "bling," and the badge also runs a built-in Frogger-like game. Six onboard buttons handle input, an IR receiver allows wireless interaction with other badges or beacons, and addressable WS2812B RGB LEDs provide the light show. Two SAO v1.69bis ports let it host add-ons, and units ship with stickers.

The badge is sold online rather than distributed at the con — it carries an explicit disclaimer that it is unofficial and does not grant DEF CON entry. It is listed on both Tindie and UberFlux at $80 (the community sheet's $120 figure could not be confirmed on either storefront). As of the research date, UberFlux showed 19 units remaining against 11 already sold. Firmware (v1.0, as a .uf2 file) is published for anyone to flash, but no hardware design files were found, so it is only partially open source.

## Make your own

Only the compiled firmware is available, at `https://bigtaro.net/frogstar25/FrogStarFirmware1.0.uf2`. Per the maker's instructions, flashing is done by copying the firmware file onto the badge (RP2350 UF2 bootloader drag-and-drop). No schematics, PCB files, or source code repository were found.
