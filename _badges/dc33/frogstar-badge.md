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
  - black
  shape: skull
  themes:
  - animal
  - frog
  - skull
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
  inputs:
  - buttons
  battery: null
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: $80
  price_usd: 80.0
  quantity: null
  availability: available
  availability_note: Checked 2026-09-06; in stock on UberFlux (19 remaining, 11 sold) and listed on Tindie at the same price.
  distribution:
  - purchase
  where: Sold online through the maker's Tindie and UberFlux stores (unofficial badge; the maker notes it does not grant entry to the con).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://bigtaro.net/frogstar25/FrogStarFirmware1.0.uf2
  eda_tool: null
links:
- label: bigtaro.net/frogstar25
  url: https://bigtaro.net/frogstar25
  kind: website
  archived: https://web.archive.org/web/20260507095715/https://bigtaro.net/frogstar25/
- label: Tindie listing
  url: https://www.tindie.com/products/bigtaro/frogstar-badge/
  kind: store
  archived: https://web.archive.org/web/20260503113524/https://www.tindie.com/products/bigtaro/frogstar-badge/
- label: UberFlux listing
  url: https://uberflux.com/product/BT-frogstar
  kind: store
- label: Bluesky (@bigtaro.bsky.social)
  url: https://bigtaro.bsky.social
  kind: social
images:
- file: assets/images/badges/dc33/frogstar-badge/b38eb78a61.jpg
  source: https://bigtaro.net/frogstar25
  credit: BigTaro's Badges
  caption: FrogStar 2025 hardware badge with round LCD display
  archived: https://web.archive.org/web/20260507095715/https://bigtaro.net/frogstar25/
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
  title: BigTaro's FrogStar 2025 Badge
  accessed: '2026-09-06'
  note: Maker's own project page; features, specs, firmware download, store links.
  archived: https://web.archive.org/web/20260507095715/https://bigtaro.net/frogstar25/
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
  archived: https://web.archive.org/web/20260503113524/https://www.tindie.com/products/bigtaro/frogstar-badge/
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: Price differs from the community sheet ($120) vs. the maker's own stores (Tindie and UberFlux both list $80); used the maker's stores as the more authoritative current price. LED count not stated anywhere found. No hardware design files (schematics/Gerbers) found published, only compiled firmware (.uf2); open_source set to partial on that basis. Total run size not stated by the maker; UberFlux stock snapshot kept in availability_note only. Colors/shape taken from the maker's own photo (black PCB, frog skull-and-crossbones), no text source states them. Verified 2026-09-07 against all three cited pages.
last_modified_date: '2026-09-06'
---

The FrogStar Badge is BigTaro's Badges' unofficial DEF CON 33 entry, built around a Raspberry Pi RP2350 driving a 1.28" round LCD (GC9A01, 240x240). It leans fully into a frog theme: a frog-themed Capture the Flag unlocks GIFs and "bling," and the badge also runs a built-in Frogger-like game. Six onboard buttons handle input, it has an IR receiver, and addressable WS2812B RGB LEDs provide the light show. The PCB is black, shaped as a frog skull over crossbones with the round display as the face. Two SAO v1.69bis ports let it host add-ons, and units ship with stickers.

The maker's pages carry an explicit disclaimer that it is unofficial and does not grant DEF CON entry. It is listed on both Tindie and UberFlux at $80 (the community sheet's $120 figure could not be confirmed on either storefront). As of the research date, UberFlux showed 19 units remaining against 11 already sold. Firmware (v1.0, as a .uf2 file) is published for anyone to flash, but no hardware design files were found, so it is only partially open source.

## Make your own

Only the compiled firmware is available, at `https://bigtaro.net/frogstar25/FrogStarFirmware1.0.uf2`. Per the maker's instructions, flashing is done by copying the firmware file onto the badge (RP2350 UF2 bootloader drag-and-drop). No schematics, PCB files, or source code repository were found.
