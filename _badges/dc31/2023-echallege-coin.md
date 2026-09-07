---
title: 2023 eChallengeCoin
id: dc31-2023-echallege-coin
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
series: eChallengeCoin
makers:
- name: Bradán Lane
  url: https://aosc.cc/
  role: designer (site published under Adventures of Sara Cladlow / T.E.C. - Tod Troche, Lory Ester, Sara Cladlow)
summary: A 47mm round electronic puzzle coin with four RGB-backlit touch pads, sold at DEF CON 31, that plays a SIMON-like game and other touch challenges tied to a story called "Sara and the Saint."
functions: Three interactive touch-pad challenges - a SIMON-like color-sequence game, an adaptive tap-cadence challenge, and a color-position encoding puzzle - plus story content ("Sara and the Saint") read via serial or online. An IR transceiver lets two coins interact when held edge to edge.
look:
  colors:
  - black
  - white
  - green
  - blue
  - yellow
  - red
  shape: circle
  themes:
  - coin
  - puzzle
  - ctf
  form_factor: coin
tech:
  mcu: null
  leds:
    count: 4
    type: RGB
    note: Visible through the translucent backshell.
  display: none
  connectivity:
  - uart
  - ir
  inputs:
  - touch
  battery: coin cell (tolerates up to 3.3V)
  sao_version: none
get_one:
  price: $60.00
  price_usd: 60.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold at the Hacker Warehouse booth at DEF CON 31.
make_your_own:
  open_source: partial
  hardware_url: https://aosc.cc/eccn2023
  firmware_url: null
  eda_tool: KiCad
  notes: Hardware viewable as KiCanvas files on the project page; a Python script for Knight's Tour decoding is also provided. No firmware repo found.
links:
- label: aosc.cc/eccn2023
  url: https://aosc.cc/eccn2023
  kind: website
images:
- file: assets/images/badges/dc31/2023-echallege-coin/2c4caa9b3e.jpg
  source: "https://aosc.cc/eccn2023"
  credit: "Bradán Lane / T.E.C."
  caption: "Face of the 2023 eChallengeCoin showing the four touch pads"
- file: assets/images/badges/dc31/2023-echallege-coin/e78f8d5ae0.jpg
  source: "https://aosc.cc/eccn2023"
  credit: "Bradán Lane / T.E.C."
  caption: "The 2023 eChallengeCoin in its acrylic case"
contact: {}
notes:
- It will be for sale at the Hacker Warehouse booth
status: released
sources:
- kind: sheet
  event: dc31
  row: 17
  updated: '2023-07-14'
- kind: url
  url: https://aosc.cc/eccn2023
  title: "AoSC - 2023 eChallengeCoin"
  accessed: '2026-09-06'
  note: "Primary project page: full feature description, photos, KiCanvas hardware files, and story content."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'The project page is published under "Adventures of Sara Cladlow" (site aosc.cc, hosted under bradanlane.com) and credits the fictional team "T.E.C." (Tod Troche, Lory Ester, Sara Cladlow) as the in-universe makers; the community sheet lists the real maker as Bradán Lane, consistent with the 2024 and 2026 eChallengeCoin entries in this archive, so the maker field was kept as-is. No MCU part number, firmware repository, quantity made, or current availability was stated on the source page.'
last_modified_date: '2026-09-06'
---

The 2023 eChallengeCoin is a 47mm-diameter, 6mm-thick round electronic puzzle sold at the Hacker Warehouse booth during DEF CON 31, the fourth or fifth year of Bradán Lane's eChallengeCoin series (published under the "Adventures of Sara Cladlow" project). Where earlier years leaned on single-color PCBs, the 2023 board is built from six colors of soldermask (black, white, green, blue, yellow, and red) and adds four RGB LEDs that shine through a translucent 3D-printed backshell, replacing the single-color LEDs of prior coins.

Four oversized touch pads drive three onboard challenges: a SIMON-style color-memory game, a new adaptive tap-cadence puzzle that learns the player's timing, and a color-position encoding challenge. A new piezo buzzer adds audio feedback, a top-edge push button handles wake/sleep, and a flanking IR transceiver lets two coins "talk" when held edge to edge for a bonus interaction. A staggered 0.1"-pitch pin header exposes a 9600-8N1 serial interface (GND/3V/TX/RX) that both powers the coin (up to 3.3V) and can be used to read an in-fiction short story, "Sara and the Saint," which is also posted on the project site for owners and non-owners alike. Hardware files are viewable via KiCanvas on the project page, along with a Python script for decoding one of the puzzle's Knight's Tour-based ciphers; no firmware repository was found.
