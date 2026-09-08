---
title: 2024 Christmas Ornament - Sara and the Christmas Maze
id: other-2024-christmas-ornament-sara-and-the-christmas-maze
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 2024
makers:
- name: Bradán Lane STUDIO
  url: https://bradanlane.com
summary: A coin-shaped, gold-clad Christmas ornament that doubles as a USB text-adventure game and a CircuitPython macro-pad.
functions: Runs a built-in text-adventure game ("Sara and the Christmas Maze," an adaptation of the 2024 eChallengeCoin's "Sara and the Dark Labyrinth") over a USB serial terminal; can instead be reflashed with CircuitPython and used as a 3-touch-pad USB macro-pad with LEDs and a small speaker.
look:
  colors:
  - gold
  - clear
  shape: coin
  themes:
  - holiday
  - puzzle
  - ctf
tech:
  mcu: SAMD21
  leds: null
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://circuitpython.org/board/bradanlanestudio_coin_m0/
  eda_tool: null
links:
- label: aosc.cc/bauble2024.php
  url: https://aosc.cc/bauble2024.php
  kind: website
  archived: https://web.archive.org/web/20260508141258/https://aosc.cc/bauble2024.php
- label: CircuitPython board page (bradanlanestudio_coin_m0)
  url: https://circuitpython.org/board/bradanlanestudio_coin_m0/
  kind: doc
  archived: https://web.archive.org/web/20260414215005/https://circuitpython.org/board/bradanlanestudio_coin_m0/
images:
- file: assets/images/badges/other/2024-christmas-ornament-sara-and-the-christmas-maze/279a033b3f.jpg
  source: https://aosc.cc/bauble2024.php
  credit: Bradán Lane STUDIO
  caption: Gold-clad face of the 2024 Christmas ornament coin
  archived: https://web.archive.org/web/20260508141258/https://aosc.cc/bauble2024.php
- file: assets/images/badges/other/2024-christmas-ornament-sara-and-the-christmas-maze/f41580a0e0.jpg
  source: https://aosc.cc/bauble2024.php
  credit: Bradán Lane STUDIO
  caption: Clear acrylic back of the ornament showing the electronics
  archived: https://web.archive.org/web/20260508141258/https://aosc.cc/bauble2024.php
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- Part of the "Adventures of Sara Cladlow" (AoSC) universe run by Bradán Lane STUDIO, the same maker behind the DEF CON eChallengeCoin series (see dc34-2026-echallengecoin). This ornament is a Christmas-2024 spin-off, not made for a specific convention, so it is filed under the "other" event; no matching event id exists in events.yml.
status: released
sources:
- kind: url
  url: https://aosc.cc/bauble2024.php
  title: 2024 Christmas Ornament - Sara and the Christmas Maze
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''n/a (Christmas 2024, not a con badge)''.'
  archived: https://web.archive.org/web/20260508141258/https://aosc.cc/bauble2024.php
- kind: url
  url: https://aosc.cc/bauble2024.php
  title: AoSC - 2024 Christmas Ornament
  accessed: '2026-09-07'
  note: Primary source for description, maker, MCU (SAMD21), functions, LED behavior, CircuitPython instructions, and photos. No price, quantity, or availability was published on the page.
  archived: https://web.archive.org/web/20260508141258/https://aosc.cc/bauble2024.php
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The maker's own project page confirms what the item is, how it works, and its chip, but never states price, quantity made, or whether it is still available, so get_one fields are left empty. No dedicated storefront or listing page was found in a short search; the AoSC site itself appears to be the only listing.
last_modified_date: '2026-09-07'
---

The 2024 Christmas Ornament is a coin-shaped USB gadget from Bradán Lane STUDIO, made as a holiday spin-off of their "Adventures of Sara Cladlow" (AoSC) universe — the same continuity behind DEF CON's eChallengeCoin series. The coin has a gold-clad face depicting Jolly Saint Nick, a clear acrylic back exposing the electronics, a laser-etched case, and an included hook for hanging on a tree.

Out of the box it runs a text-adventure game, "Sara and the Christmas Maze," an adaptation of the 2024 eChallengeCoin's "Sara and the Dark Labyrinth," played over a USB serial terminal on a Microchip SAMD21 microcontroller. A single red LED on the back signals its state (fast blink for normal operation, slow pulse for bootloader mode, fast pulse if the USB connection isn't recognized). The same game firmware also runs on the 2025 eChallengeCoin hardware and on generic SAMD21 boards such as the Adafruit ItsyBitsy M0 Express.

Alternatively, the ornament can be reflashed with CircuitPython (erasing the game) and repurposed as a small macro-pad: it has three touch pads, multiple LED groups, and a small speaker, and sample code is provided for a 3-key macro-pad or a mute-button. No price, production quantity, or ongoing availability is stated on the maker's page.
