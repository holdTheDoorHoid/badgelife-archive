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
functions: An all-new text adventure game, "Sara and the Dark Labyrinth," continuing the Sara Cladlow stories; the game replaces the challenges used by earlier eChallengeCoins. Runs CircuitPython as a USB device and doubles as a learning platform (Neopixels, touch sensors, accelerometer, IR, polyphonic sound, EEPROM, ePaper).
look:
  colors: []
  shape: circle
  themes:
  - puzzle
  - coin
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
  - audio
  inputs:
  - touch
  - accelerometer
  power: USB-C
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
  notes: Ships with CircuitPython pre-installed. The maker's workshop page (aosc.cc/explorer) links a "Workshop Repository" at gitlab.com/bradanlane_cp/workshops and the Tindie listing links "Source Code" to the same workshop page, but the repository was not reachable when checked (GitLab API returns 404 and it is not among the group's public projects). No schematic/PCB release was found.
links:
- label: www.tindie.com/products/bradanlane/explorer-badge
  url: https://www.tindie.com/products/bradanlane/explorer-badge/
  kind: store
  archived: https://web.archive.org/web/20260503094857/https://www.tindie.com/products/bradanlane/explorer-badge/
- label: aosc.cc — the 2024 eChallengeCoin / Explorer Badge
  url: https://aosc.cc/eccn2024.php
  kind: website
  note: Maker's own project page with full technical details, photos, and battery/case instructions.
  archived: https://web.archive.org/web/20251014105308/https://aosc.cc/eccn2024.php
- label: aosc.cc/explorer — Python & CircuitPython workshop series
  url: https://aosc.cc/explorer
  kind: doc
  note: Companion workshop series teaching Python/CircuitPython using the badge.
  archived: https://web.archive.org/web/20260503193828/https://aosc.cc/explorer/
images:
- file: assets/images/badges/dc32/echallenge-coin-2024/29d8053f6a.jpg
  source: https://aosc.cc/eccn2024.php
  credit: Bradán Lane
  caption: Front of the 2024 Explorer Badge / eChallengeCoin, with the ePaper display
  archived: https://web.archive.org/web/20251014105308/https://aosc.cc/eccn2024.php
- file: assets/images/badges/dc32/echallenge-coin-2024/39a110993e.jpg
  source: https://aosc.cc/eccn2024.php
  credit: Bradán Lane
  caption: The Explorer Badge in its case with lanyard
  archived: https://web.archive.org/web/20251014105308/https://aosc.cc/eccn2024.php
contact:
  handles:
  - '@bradanlane'
notes:
- Sheet listed this as "eChallenge Coin 2024"; the maker renamed the 2024 entry in the series to the "Explorer Badge" (title updated here, id/filename kept unchanged).
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
  archived: https://web.archive.org/web/20260503094857/https://www.tindie.com/products/bradanlane/explorer-badge/
- kind: url
  url: https://aosc.cc/eccn2024.php
  title: AoSC - Explorer Badges (the 2024 eChallengeCoin)
  accessed: '2026-09-06'
  note: Maker's own page with full hardware description (RP2040, 8MB flash, EEPROM, neopixels, touch, accelerometer, IR, polyphonic sound, 1.54in ePaper, 84mm case size), battery details, and photos.
  archived: https://web.archive.org/web/20251014105308/https://aosc.cc/eccn2024.php
- kind: url
  url: https://aosc.cc/explorer
  title: Python & CircuitPython Workshops
  accessed: '2026-09-06'
  note: Confirms RP2040/8MB storage/CircuitPython pre-installed and links the companion workshop repo.
  archived: https://web.archive.org/web/20260503193828/https://aosc.cc/explorer/
- kind: url
  url: https://aosc.cc
  title: AoSC - eChallengeCoins with Sara Cladlow
  accessed: '2026-09-06'
  note: Confirms this is part of the annual eChallengeCoin series (2020-2026) and that the 2024 story is "Sara and the Dark Labyrinth."
  archived: https://web.archive.org/web/20260511011507/https://aosc.cc/
- kind: url
  url: https://www.bradanlane.com
  title: Bradán Lane LINKS
  accessed: '2026-09-06'
  note: Maker's link directory; led to aosc.cc (the eChallengeCoin project site) and GitLab.
  archived: https://web.archive.org/web/20260509140218/https://bradanlane.com/
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: Verification 2026-09-07 re-read aosc.cc/eccn2024.php, Tindie, aosc.cc/explorer, aosc.cc and bradanlane.com; both images match the maker's photos on aosc.cc/eccn2024.php. Removed unsupported themes (ctf, learn to solder), a claim that the series pivoted to "CircuitPython education" (the maker only says the challenges were replaced with text adventure games), and the GitLab workshops link (gitlab.com/bradanlane_cp/workshops returns 404 from the GitLab API and is not listed among the bradanlane_cp group's public projects; kept as a mention in make_your_own.notes). LED count not stated by the maker. No maker page ties the badge to DEF CON 32 by name; the 2024 date and the community sheet row are the only link to the event, and in-person sales are not documented, so get_one.where names only the Tindie channel.
last_modified_date: '2026-09-07'
---

The 2024 edition of Bradán Lane's annual eChallengeCoin series was renamed the "Explorer Badge" and represented a significant redesign from prior years. At 84mm across (versus 44-47mm for the earlier eChallengeCoins), it has a custom case with a 3D-printed back, a 1.54" ePaper display, and an RP2040 microcontroller with 8MB of flash storage and dedicated EEPROM. It also carries Neopixel LEDs, touch sensors, an accelerometer, an IR receiver and emitter, polyphonic sound with a built-in speaker and I2S output, an I2C STEMMA-QT connector, USB-C, and LiPo charging for an optional 303450 cell (not included) on a 1.25mm JST connector.

Starting with this 2024 edition, the challenges of the earlier eChallengeCoins were replaced with an all-new text adventure game, "Sara and the Dark Labyrinth," that runs on the badge. The badge ships with CircuitPython pre-installed and is described by the maker as an electronic learning platform; a companion Python and CircuitPython workshop series at aosc.cc/explorer starts with introductory Python and ends with programming the badge's LEDs, touch sensors, sound, EEPROM and ePaper display. Bradán Lane sold the badge for $75 through their Tindie store, where it has been listed as sold out since January 11, 2025, with a note that restocking would happen in increments.

## History

This is the fifth annual eChallengeCoin, following "Sara and the Deleting App" (2020), "Sara and the Brewer's Bible" (2021), "Sara and the Nightclub Riddler" (2022) and "Sara and the Saint" (2023); a 2021 "eChallengeCard" was cancelled. A Christmas Ornament edition, "Sara and the Christmas Maze," followed later in 2024, and the series has continued with "Sara and the Jefferson Notebook" (2025) and "Sara and the Missing Artifacts" (2026). From 2024 onward the challenges were replaced with text adventure games.
