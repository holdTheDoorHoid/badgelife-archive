---
title: Explorer Badge (2024 eChallengeCoin)
id: dc32-echallenge-coin-2024
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
series: eChallengeCoin
makers:
- name: Bradán Lane
  url: https://bradanlane.com
summary: A large USB-C, CircuitPython-powered coin badge with an ePaper display, built around an all-new text adventure game, "Sara and the Dark Labyrinth."
functions: Continuation of Sara Cladlow's adventures and an all-new text adventure game, "Sara and the Dark Labyrinth"; runs on-badge as a USB CircuitPython device rather than the interactive challenge-puzzle format used by earlier eChallengeCoins.
look:
  colors: []
  shape: circle
  themes:
  - puzzle
  - ctf
  - coin
  - learn to solder
tech:
  mcu: RP2040
  leds:
    count: null
    type: WS2812B
    note: Neopixel LEDs; exact count not stated by the maker.
  display: 1.54" ePaper
  connectivity:
  - usb
  - ir
  - i2c
  battery: LiPo (303450 cell, 1.25mm JST connector; battery not included)
  sao_version: null
get_one:
  price: $75.00
  price_usd: 75.0
  quantity: ''
  availability: sold_out
  availability_note: Listed out of stock on Tindie since January 11, 2025 (checked 2026-09-06); maker noted plans to restock in increments.
  distribution:
  - purchase
  where: Sold direct by Bradán Lane STUDIO through Tindie, under the name "Explorer Badge."
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: Runs stock CircuitPython (badge is discoverable to CircuitPython.org by searching "explorer"). The maker publishes an accompanying Python/CircuitPython workshop series and code at https://gitlab.com/bradanlane_cp/workshops, but no dedicated hardware (schematic/PCB) release was found.
links:
- label: www.tindie.com/products/bradanlane/explorer-badge
  url: https://www.tindie.com/products/bradanlane/explorer-badge/
  kind: store
- label: aosc.cc — the 2024 eChallengeCoin / Explorer Badge
  url: https://aosc.cc/eccn2024.php
  kind: website
  note: Maker's own project page with full technical details, photos, and battery/case instructions.
- label: aosc.cc/explorer — Python & CircuitPython workshop series
  url: https://aosc.cc/explorer
  kind: doc
  note: Companion workshop series teaching Python/CircuitPython using the badge.
- label: gitlab.com/bradanlane_cp/workshops
  url: https://gitlab.com/bradanlane_cp/workshops
  kind: repo
  note: Workshop repository referenced from the workshop series page (not independently verified; GitLab returned a bot-check page on fetch).
images:
- file: assets/images/badges/dc32/echallenge-coin-2024/29d8053f6a.jpg
  source: "https://aosc.cc/eccn2024.php"
  credit: "Bradán Lane"
  caption: "Front of the 2024 Explorer Badge / eChallengeCoin, showing the ePaper display"
- file: assets/images/badges/dc32/echallenge-coin-2024/39a110993e.jpg
  source: "https://aosc.cc/eccn2024.php"
  credit: "Bradán Lane"
  caption: "The Explorer Badge in its case with lanyard"
contact:
  handles:
  - '@bradanlane'
notes:
- "Sheet listed this as \"eChallenge Coin 2024\"; the maker renamed the 2024 entry in the series to the \"Explorer Badge\" (title updated here, id/filename kept unchanged)."
status: released
sources:
- kind: sheet
  event: dc32
  row: 30
  updated: '2024-03-14'
- kind: url
  url: https://www.tindie.com/products/bradanlane/explorer-badge/
  title: Explorer Badge by bradanlane - Tindie
  accessed: '2026-09-06'
  note: Confirms this is the 2024 eChallengeCoin, price ($75), CircuitPython, feature list, and out-of-stock status.
- kind: url
  url: https://aosc.cc/eccn2024.php
  title: "AoSC - Explorer Badges (the 2024 eChallengeCoin)"
  accessed: '2026-09-06'
  note: Maker's own page with full hardware description (RP2040, 8MB flash, EEPROM, neopixels, touch, accelerometer, IR, polyphonic sound, 1.54in ePaper, 84mm case size), battery details, and photos.
- kind: url
  url: https://aosc.cc/explorer
  title: "Python & CircuitPython Workshops"
  accessed: '2026-09-06'
  note: Confirms RP2040/8MB storage/CircuitPython pre-installed and links the companion workshop repo.
- kind: url
  url: https://aosc.cc
  title: "AoSC - eChallengeCoins with Sara Cladlow"
  accessed: '2026-09-06'
  note: Confirms this is part of the annual eChallengeCoin series (2020-2026) and that the 2024 story is "Sara and the Dark Labyrinth."
- kind: url
  url: https://www.bradanlane.com
  title: "Bradán Lane LINKS"
  accessed: '2026-09-06'
  note: Maker's link directory; led to aosc.cc (the eChallengeCoin project site) and GitLab.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts confirmed directly by the maker's own project page (aosc.cc) and Tindie listing. Could not confirm an exact LED count or a dedicated hardware/firmware repo (only a workshop code repo, and GitLab blocked automated fetches with a bot check). No page found explicitly ties this to "DEF CON 32" by name, but the 2024 date and community-sheet entry line up; distribution beyond Tindie retail (e.g., in-person DEF CON sales) is not documented by the maker's own pages, so get_one.where is left describing the confirmed retail channel only.
last_modified_date: '2026-09-06'
---

The 2024 edition of Bradán Lane's annual eChallengeCoin series was renamed the "Explorer Badge" and represented a significant redesign from prior years. At 84mm across (versus 44-47mm for 2020-2023), it uses a custom case to house a 1.54" ePaper display on the front and an RP2040 microcontroller on the back, backed by 8MB of flash storage and dedicated EEPROM. It also carries Neopixel LEDs, capacitive touch sensors, an accelerometer, an IR receiver/emitter, polyphonic sound, an I2C STEMMA-QT connector, and support for an optional 303450 LiPo battery (not included) charged over USB-C.

Rather than the interactive challenge puzzles and story-driven "eChallengeCoin" format used in 2020-2023, the 2024 unit replaced its central story challenge with an original text adventure game, "Sara and the Dark Labyrinth," playable directly on the badge over USB. It runs stock CircuitPython, making it fully user-programmable, and the maker paired its release with a companion Python/CircuitPython workshop series (covering basic Python, then badge-specific hardware) hosted at aosc.cc/explorer. Bradán Lane sold the badge for $75 through their Tindie store; it has been listed as out of stock there since January 2025, with the maker indicating plans to restock in batches.

## History

This is the fifth entry in the eChallengeCoin series, which began in 2020 and has continued annually (a 2021 "eChallengeCard" was cancelled, and a special 2024 Christmas Ornament edition, "Sara and the Christmas Maze," followed the same year). Starting with the 2024 edition, the series pivoted from puzzle-solving toward CircuitPython education, a format the maker has continued in subsequent years (2025's "Sara and the Jefferson Notebook" and 2026's "Sara and the Missing Artifacts").
