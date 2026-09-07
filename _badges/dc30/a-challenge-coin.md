---
title: 2022 eChallengeCoin
id: dc30-a-challenge-coin
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
series: eChallengeCoin
makers:
- name: Bradán Lane STUDIO
  url: https://www.bradanlane.com/
summary: An interactive electronic challenge coin from Bradán Lane STUDIO, part of the "Adventures of Sara Cladlow" story series, solved using onboard LEDs, touch sensors, and a piezo buzzer.
functions: Three interactive LED/touch-sensor challenges, three story-based puzzles unlocked over UART, an IR transceiver for bonus device-to-device content, and demo modes including LED animations and a Craps game.
look:
  colors: []
  shape: circle
  themes:
  - coin
  - puzzle
  - ctf
tech:
  mcu: null
  leds:
    count: 7
    type: null
    note: Three LEDs for the interactive challenges, three for the story challenges, and one center bonus indicator.
  display: none
  connectivity:
  - uart
  - ir
  battery: CR2032 (included)
  sao_version: null
get_one:
  price: $40.00
  price_usd: 40.0
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing shows as retired/no longer for sale, checked 2026-09-06.
  distribution:
  - purchase
  where: Online (Tindie Store)
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: Documentation site (aosc.cc/eccn2022) shows schematic/board views via KiCanvas, but no repository link or license was found.
links:
- label: www.tindie.com/products/bradanlane/2022-echallengecoin
  url: https://www.tindie.com/products/bradanlane/2022-echallengecoin/
  kind: store
  archived: https://web.archive.org/web/20260519052558/https://www.tindie.com/products/bradanlane/2022-echallengecoin/
- label: aosc.cc/eccn2022 (documentation)
  url: https://aosc.cc/eccn2022
  kind: doc
  accessed: '2026-09-06'
  archived: https://web.archive.org/web/20260519084516/https://aosc.cc/eccn2022
images:
- file: assets/images/badges/dc30/a-challenge-coin/d8743e2491.jpg
  source: https://www.tindie.com/products/bradanlane/2022-echallengecoin/
  credit: Bradán Lane STUDIO
  caption: Front face of the 2022 eChallengeCoin
  archived: https://web.archive.org/web/20260519052558/https://www.tindie.com/products/bradanlane/2022-echallengecoin/
contact: {}
notes:
- Will also have a special SAO available in person
status: released
sources:
- kind: sheet
  event: dc30
  row: 16
  updated: '2022-07-02'
- kind: url
  url: https://www.tindie.com/products/bradanlane/2022-echallengecoin/
  title: 2022 eChallengeCoin - Tindie
  accessed: '2026-09-06'
  note: Maker identity, description, size, battery, price, retired/sold-out status
  archived: https://web.archive.org/web/20260519052558/https://www.tindie.com/products/bradanlane/2022-echallengecoin/
- kind: url
  url: https://aosc.cc/eccn2022
  title: 2022 eChallengeCoin Project documentation
  accessed: '2026-09-06'
  note: LED count/layout, touch sensor count, IR feature, UART protocol details
  archived: https://web.archive.org/web/20260519084516/https://aosc.cc/eccn2022
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: The sheet listed only a garbled title ("A Challenge Coin...", maker "2022 sChallenge Coin"); identified as Bradán Lane STUDIO's 2022 eChallengeCoin from the linked Tindie store, title corrected accordingly. MCU/chip was not disclosed on either the Tindie listing or the maker's documentation site, so tech.mcu is left null. No hardware/firmware repository link was found despite the documentation mentioning open design-file viewing via KiCanvas, so make_your_own fields are left null aside from a note. This is part of a recurring "eChallengeCoin" series with later years (see dc32-echallenge-coin-2024, dc34-2026-echallengecoin) as separate entries; not a duplicate of those since each year is a distinct product.
last_modified_date: '2026-09-06'
---

The 2022 eChallengeCoin is an electronic challenge coin made by Bradán Lane STUDIO for DEF CON 30, part of the maker's recurring eChallengeCoin series and tied into the ongoing "Adventures of Sara Cladlow" story. The 44mm, 6mm-thick coin runs on a CR2032 battery and packs seven LEDs, six capacitive touch sensors, a piezo buzzer, a UART interface, and an IR transceiver, letting a solver work through three interactive LED/touch puzzles and three story-driven puzzles, plus bonus content unlocked by holding two coins near each other over IR. It also includes lighter demo modes, such as LED animations and a Craps game, for people who just want to play with it.

It was sold through the maker's Tindie store for $40 and came with a protective coin case and an optional badge holder; the sheet notes a separate special SAO version was also available in person at the con. The Tindie listing is now marked retired, and the maker has continued the series with new eChallengeCoins in subsequent years. No MCU/chip identification or hardware/firmware repository was found in the sources checked, despite documentation referencing viewable design files.
