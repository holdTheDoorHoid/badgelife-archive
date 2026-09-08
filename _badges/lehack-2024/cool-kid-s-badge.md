---
title: Cool Kid's Badge
id: lehack-2024-cool-kid-s-badge
layout: badge
parent: leHACK 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: lehack-2024
year: 2024
makers:
- name: Tixlegeek (cyberpunk.company)
  url: https://tixlegeek.io/coolkidsbadge/
summary: A standalone ESP32-S3 pentesting badge with an NRF24L01 radio and a programmable Mifare Classic 1K NFC tag, made by Tixlegeek for leHACK.
functions: Runs standalone as an ESP32-S3 platform; the NRF24L01 module handles 2.4GHz radio work, the onboard Mifare Classic 1K tag has a programmable UUID/Block0, and it exposes I2C/GPIO plus a Flipper Zero extension port for add-ons.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - security
tech:
  mcu: ESP32-S3
  leds: null
  display: null
  connectivity:
  - nfc
  - i2c
  - wifi
  battery: null
  sao_version: none
get_one:
  price: "~€50 fully populated (estimate)"
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - free_drop
  where: Distributed at leHACK 2024 and by mail to France/EU; the maker's page said no payment should be made to anyone in advance.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
links:
- label: tixlegeek.io/coolkidsbadge
  url: https://tixlegeek.io/coolkidsbadge/
  kind: website
images:
- file: assets/images/badges/lehack-2024/cool-kid-s-badge/47ec8d2a91.jpg
  source: "https://tixlegeek.io/coolkidsbadge/"
  credit: "Tixlegeek"
  caption: "Cool Kid's Badge, final 2024 production version"
- file: assets/images/badges/lehack-2024/cool-kid-s-badge/bbf1654ac0.png
  source: "https://tixlegeek.io/coolkidsbadge/"
  credit: "Tixlegeek"
  caption: "Cool Kid's Badge production board detail"
contact: {}
notes:
- Unofficial leHACK 2023/2024 electronic badge built as a standalone ESP32-S3 pentesting platform with NRF24L01 radio, NFC, and Flipper Zero compatibility. Found by the event-year sweep, task con-brucon.
- The sweep's one-line note matched the maker's own project page, so this is a confirmed real item, not a rumor.
status: released
sources:
- kind: url
  url: https://tixlegeek.io/coolkidsbadge/
  title: Cool Kid's Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-brucon); event read as ''leHACK 2024''.'
- kind: url
  url: https://tixlegeek.io/coolkidsbadge/
  title: Cool Kid's Badge
  accessed: '2026-09-08'
  note: 'Maker''s own project page: confirms ESP32-S3 MCU, NRF24L01 radio, Mifare Classic 1K NFC tag, Flipper Zero extension port, ~€50 estimated cost, July 1 2024 arrival, and distribution at leHACK 2024 plus mail to France/EU.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Maker''s own page is the only source found (a search for "Cool Kid''s Badge" Tixlegeek turned up nothing beyond it). No LED count, display, battery spec, exact quantity made, or hardware/firmware repo link is stated on the page, so those fields are left empty. Confidence is medium rather than high because only one source (albeit the maker''s own) was available to cross-check.'
last_modified_date: '2026-09-08'
---

Cool Kid's Badge is an unofficial electronic conference badge made by Tixlegeek (cyberpunk.company) for leHACK, spanning the 2023 and 2024 editions of the French hacking conference. It is built around an ESP32-S3 microcontroller and works as a standalone pentesting platform: an onboard NRF24L01 module handles 2.4GHz radio work, and a Mifare Classic 1K NFC tag on the board has a programmable UUID and Block0, letting the wearer reprogram its NFC identity. The board also exposes I2C/GPIO and a Flipper Zero extension port for add-on modules.

The final production run arrived July 1, 2024, and the maker distributed it in person at leHACK 2024 as well as by mail within France and the EU, estimating a fully-populated unit at around €50 while cautioning that no payment should be sent to anyone in advance. The project page shows both 2024 prototype boards and the final production version, and credits Inkscape and KiCad as the (open-source) design tools used, though no hardware or firmware repository link is published on the page itself.

## Make your own

The maker's page states the badge was designed with KiCad and Inkscape but does not link a repository, Gerbers, or BOM, so hardware/firmware files could not be confirmed as published; `make_your_own.open_source` is set to `partial` on that basis.
