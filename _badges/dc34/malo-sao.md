---
title: MalO SAO
id: dc34-malo-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: ParallelLogic
  url: https://github.com/parallellogic-/
summary: An SAO themed after the SCP Foundation's SCP-1471-A, packed with an OLED display, dozens of LEDs, and a grab-bag of sensors for puzzles and IR messaging between badges.
functions: IR Chat; puzzles, games, and custom LED animations; capacitive touch buttons; battery/thermal monitoring; NFC/RFID tag support
look:
  colors: []
  shape: null
  themes:
  - horror
  - sci-fi
  - security
tech:
  mcu: RP2350B
  leds:
    count: 50
    type: null
    note: 'Maker''s GitHub repo describes a red-green LED plus IR transmit/receive; the storefront listing advertises "over 50 LEDs" — sources disagree, see notes.'
  display: 1.5" 128x128 grayscale OLED (SSD1327)
  connectivity:
  - ir
  - nfc
  - rfid
  - usb
  battery: null
  sao_version: null
get_one:
  price: $50
  price_usd: 50.0
  quantity: 64
  availability: sold_out
  availability_note: 'Uberflux listing showed 0 remaining, 64 sold, checked 2026-09-06.'
  distribution:
  - purchase
  where: Sold online via Uberflux (uberflux.com/product/PL-1471) and in person at DEF CON 34.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/parallellogic-/MalO_SAO
  firmware_url: https://github.com/parallellogic-/MalO_SAO
  eda_tool: null
  license: Creative Commons Attribution-ShareAlike 3.0 Unported License
  fab_url: null
  notes: Schematics, PCB layout, and firmware source are published together in the GitHub repo per the maker's own description.
links:
- label: www.youtube.com/watch?v=lrK-HDk0pKE
  url: https://www.youtube.com/watch?v=lrK-HDk0pKE
  kind: video
- label: uberflux.com/product/PL-1471
  url: https://uberflux.com/product/PL-1471
  kind: store
- label: github.com/parallellogic-/MalO_SAO
  url: https://github.com/parallellogic-/MalO_SAO
  kind: repo
- label: github.com/parallellogic-
  url: https://github.com/parallellogic-/
  kind: repo
images:
- file: assets/images/badges/dc34/malo-sao/ed18f94345.jpg
  source: "https://uberflux.com/product/PL-1471"
  credit: "ParallelLogic"
  caption: "MalO SAO board, front view"
- file: assets/images/badges/dc34/malo-sao/2e25200ad1.jpg
  source: "https://uberflux.com/product/PL-1471"
  credit: "ParallelLogic"
  caption: "MalO SAO board, back view"
contact:
  discord: ParallelLogic
  emails:
  - parallellogic@gmail.com
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 58
  updated: 8/4/2026 21:44:59
  listing: Update to Existing
- kind: url
  url: https://uberflux.com/product/PL-1471
  title: "MalO SAO (ver1.0.0 Themed Artisan Electronics Circuit Board) - Uberflux"
  accessed: '2026-09-06'
  note: Price, quantity sold/remaining, features list, and images.
- kind: url
  url: https://github.com/parallellogic-/MalO_SAO
  title: "parallellogic-/MalO_SAO - GitHub"
  accessed: '2026-09-06'
  note: MCU, display, connectivity, sensor list, license, and confirmation that hardware and firmware files are both published.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    This entry duplicates dc34-malo (same maker ParallelLogic, same GitHub repo
    MalO_SAO, same product); the sheet appears to have two rows for one item
    (row 21 "New" vs row 58 "Update to Existing"). Filled in independently per
    instructions. LED count/type is uncertain: the GitHub repo's own text
    describes only a red-green LED plus IR transmit/receive, while the Uberflux
    storefront advertises "over 50 LEDs" and customizable animations; could not
    resolve which is accurate without opening the repo's schematic/BOM files,
    so tech.leds.type is left null. tech.battery, tech.sao_version, and
    look.colors/look.shape could not be confirmed from the sources checked.
last_modified_date: '2026-09-06'
---

The MalO SAO is a shitty add-on from ParallelLogic themed on the SCP Foundation's SCP-1471-A, made for DEF CON 34. It centers on an RP2350B dual-core microcontroller driving a 1.5" 128x128 grayscale OLED, and layers on capacitive touch buttons, an IMU, a light sensor, a hall-effect sensor, a microphone, a buzzer, a vibration motor, and NFC/RFID support. A standout feature is infrared transmit/receive hardware used for an "IR Chat" mode, letting badges holding a MalO SAO exchange messages with each other over IR. The board is USB-C hackable and reprogrammable through the Arduino IDE.

It sold through Uberflux for $50 (all 64 units sold out) alongside in-person sales at DEF CON 34, and came with a wrist lanyard and stickers. ParallelLogic has published both the hardware design files and firmware source on GitHub under a Creative Commons Attribution-ShareAlike 3.0 license.

This entry appears to duplicate `dc34-malo`, which was imported from an earlier sheet row for the same maker and the same GitHub repo; see `research.notes`.

## Make your own

Schematics, PCB layout files, and firmware source are all published in the [MalO_SAO GitHub repo](https://github.com/parallellogic-/MalO_SAO) under a Creative Commons Attribution-ShareAlike 3.0 license, with documentation describing the build in the repo itself.
