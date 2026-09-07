---
title: 2025 eChallengeCoin - Sara and the Jefferson Notebook
id: dc33-2025-echallengecoin-sara-and-the-jefferson-notebook
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
series: eChallengeCoin
year: 2025
makers:
- name: Bradán Lane
  url: https://bradanlane.com
summary: A limited-edition, gold-finished electronic "challenge coin" from the Adventures of Sara Cladlow (AoSC) series, given out (not sold) for confirmed charitable donations to youth STEM education.
functions: Plays a built-in USB-serial text adventure game, "Sara and the Jefferson Notebook" (about 40 rooms, fewer than 20 objects); also usable as a CircuitPython development platform with three capacitive touch pads and three groups of NeoPixels for custom projects (e.g. a mini macropad).
look:
  colors:
  - gold
  shape: coin
  themes:
  - coin
  - puzzle
  - learn to solder
  - charity
tech:
  mcu: SAMD21
  leds:
    count: null
    type: NeoPixel
    note: Three groups of NeoPixels, one aligned with each of the three touch pads.
  display: none
  connectivity:
  - usb
  battery: none
  sao_version: none
get_one:
  price: free (with a confirmed $50+ donation to a qualifying youth STEM charity)
  price_usd: null
  quantity: ''
  availability: free
  availability_note: 'Checked 2026-09-07: maker''s page describes it as a limited-edition release, given (not sold) in exchange for proof of a qualifying charitable donation.'
  distribution:
  - free_drop
  - charity
  where: Requested via an online form on the maker's site by submitting proof of a $50+ donation to a public charity supporting youth STEM education; mailed or picked up in person at DEF CON.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://aosc.cc/cn25/files/cn25_satjn.uf2
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: 'Game firmware shipped as a UF2 for the SAMD21; the board is also CircuitPython-compatible (see https://circuitpython.org/board/bradanlanestudio_coin_m0/). No hardware design files (schematic/PCB/gerbers) were published on the maker''s page.'
links:
- label: aosc.cc/eccn2025.php
  url: https://aosc.cc/eccn2025.php
  kind: website
- label: CircuitPython board page
  url: https://circuitpython.org/board/bradanlanestudio_coin_m0/
  kind: doc
- label: Bradán Lane (Bluesky)
  url: https://bsky.app/profile/bradanlane.bsky.social
  kind: social
images:
  - file: assets/images/badges/dc33/2025-echallengecoin-sara-and-the-jefferson-notebook/2e42d2ee46.jpg
    source: "https://aosc.cc/eccn2025.php"
    credit: "Bradán Lane / T.E.C."
    caption: "2025 eChallengeCoin, face"
  - file: assets/images/badges/dc33/2025-echallengecoin-sara-and-the-jefferson-notebook/5c4469a611.jpg
    source: "https://aosc.cc/eccn2025.php"
    credit: "Bradán Lane / T.E.C."
    caption: "2025 eChallengeCoin, case"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- 'The maker''s page frames this as ''T.E.C.'' (Sara Cladlow, Tod Troche, and Lory Ester), a fictional persona used for the Adventures of Sara Cladlow (AoSC) storyline; the actual designer/publisher is Bradán Lane (Bradán Lane STUDIO), who also produced the 2026 eChallengeCoin entries in this archive.'
status: listed
sources:
- kind: url
  url: https://aosc.cc/eccn2025.php
  title: 2025 eChallengeCoin - Sara and the Jefferson Notebook
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''2025 (unclear which con, if any)''.'
- kind: url
  url: https://aosc.cc/eccn2025.php
  title: AoSC - 2025 eChallengeCoin
  accessed: '2026-09-07'
  note: 'Primary source for description, materials, electronics (SAMD21, NeoPixels, touch pads, no battery, USB-C), donation-based distribution model, and firmware download link.'
- kind: url
  url: https://circuitpython.org/board/bradanlanestudio_coin_m0/
  title: bradanlanestudio_coin_m0 - CircuitPython board page
  accessed: '2026-09-07'
  note: 'Confirms CircuitPython compatibility for the coin board (referenced from the maker''s page).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The maker''s page does not name a specific DEF CON number; it says the coin is "available at in-person conferences we attend" and can be picked up "in-person at DEFCON." Since this is a 2025-dated item and DEFCON pickup is mentioned, event was set to dc33 (DEF CON 33, 2025) but this is an inference rather than an explicit statement on the source page. No hardware design files (schematic, PCB, gerbers) were found, only the game firmware UF2 and a pointer to the generic CircuitPython board build; make_your_own.open_source set to partial on that basis. LED count and exact production quantity are not stated.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/2025-echallengecoin-sara-and-the-jefferson-notebook/
---

The 2025 eChallengeCoin, "Sara and the Jefferson Notebook," is a gold-finished electronic challenge coin from Bradán Lane's long-running Adventures of Sara Cladlow (AoSC) project, presented under the in-story persona "T.E.C." (Sara Cladlow, Tod Troche, and Lory Ester). Rather than being sold, the coin is given to anyone who makes a confirmed donation of $50 or more to a public charity that provides STEM education opportunities to youth, with recipients submitting proof through an online form for mailing or in-person pickup at DEF CON.

Built around a Microchip SAMD21 microcontroller with USB-C connectivity, the coin has no battery and functions as a literal coin when disconnected from a computer. Plugged into a PC over USB, it presents as a serial device running a self-contained text adventure game of about 40 rooms and under 20 objects, playable through terminal software; the game firmware is distributed as a UF2 file and can also run on other SAMD21 boards such as the Adafruit ItsyBitsy M0 Express. Beyond the game, the board doubles as a CircuitPython development platform, with three capacitive touch pads and three matching groups of NeoPixels intended for custom projects such as a mini macropad, once the built-in adventure has been completed.

No PCB or schematic files were found published for this coin; only the game firmware and a link to its generic CircuitPython board definition are available. The coin belongs to the same eChallengeCoin series that continued into 2026 with Bradán Lane STUDIO's "2026 eChallengeCoin" and "2026 'Choose Your Own Charity' eChallengeCoin," both already cataloged elsewhere in this archive.
