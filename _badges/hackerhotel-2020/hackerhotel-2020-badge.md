---
title: Hackerhotel 2020 Badge
id: hackerhotel-2020-hackerhotel-2020-badge
layout: badge
parent: Hackerhotel 2020
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hackerhotel-2020
year: 2020
makers:
- name: Badge.Team (Renze Nicolai, Nikolett S., Sake, Glu)
summary: 'A mixed-reality escape-room badge with an Egyptian cat-goddess storyline, played through a serial text adventure and four front buttons.'
functions: 'Puzzle/escape-room gameplay driven over a USB-serial text interface (115200 8n1); four front buttons for game input; LED matrix for feedback/effects.'
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - egyptian
  - text
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - uart
  battery: batteries included
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: 'Distributed to attendees at Hackerhotel 2020.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/badgeteam/hackerhotel-2020-hardware
  firmware_url: https://github.com/badgeteam/hackerhotel-2020-software
  eda_tool: KiCad
links:
- label: badge.team/docs/badges/hackerhotel-2020
  url: https://badge.team/docs/badges/hackerhotel-2020/
  kind: website
- label: hackerhotel-2020-hardware (GitHub)
  url: https://github.com/badgeteam/hackerhotel-2020-hardware
  kind: repo
- label: hackerhotel-2020-software (GitHub)
  url: https://github.com/badgeteam/hackerhotel-2020-software
  kind: repo
images:
- file: assets/images/badges/hackerhotel-2020/hackerhotel-2020-badge/35e987f4ba.gif
  source: "https://badge.team/docs/badges/hackerhotel-2020/"
  credit: "Badge.Team"
  caption: "Hackerhotel 2020 badge showing LED matrix and buttons"
contact: {}
notes:
- Mixed-reality escape-room badge with Egyptian cat-goddess lore, USB-serial text adventure at 115200 baud, four front buttons, bottom-mounted SAO connector, LED matrix.
status: listed
sources:
- kind: url
  url: https://badge.team/docs/badges/hackerhotel-2020/
  title: Hackerhotel 2020 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''Hackerhotel 2020''.'
- kind: url
  url: https://badge.team/docs/badges/hackerhotel-2020/
  title: Hackerhotel 2020 Badge (docs)
  accessed: '2026-09-07'
  note: 'Confirmed badge type, gameplay (mixed-reality escape room), maker credits, four front buttons, LED matrix, USB-serial 115200 8n1, SAO connector, battery-powered; noted a known production issue with mirrored SAO pinout/inverted LED matrix that Badge.Team offered rework for at events.'
- kind: url
  url: https://github.com/badgeteam/hackerhotel-2020-hardware
  title: badgeteam/hackerhotel-2020-hardware
  accessed: '2026-09-07'
  note: 'Hardware repo: KiCad design files, CERN-OHL-P license; README notes the LED footprints are reversed on the produced boards, making the badge suitable for manual assembly only.'
- kind: url
  url: https://github.com/badgeteam/hackerhotel-2020-software
  title: badgeteam/hackerhotel-2020-software
  accessed: '2026-09-07'
  note: 'Software repo: MIT license; game prototype in Python, embedded firmware in C built with gcc-avr and flashed via pyupdi (indicates an AVR microcontroller programmed over UPDI, exact part number not stated in the repo).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own docs and both GitHub repos (hardware + software) confirm the badge concept, gameplay, credits, and that it is open source (KiCad hardware under CERN-OHL-P, firmware under MIT). Exact MCU part number, LED count/type, display type, SAO header version, price, and quantity made are not stated anywhere found and are left empty rather than guessed. The firmware toolchain (gcc-avr + pyupdi) indicates an AVR chip programmed over UPDI, noted here but not filled into tech.mcu since the specific part is unconfirmed.'
last_modified_date: '2026-09-07'
---

The Hackerhotel 2020 badge was Badge.Team's contribution to the 2020 edition of Hackerhotel, a small Dutch hacker gathering. Rather than a general-purpose platform badge, it was built as a single-purpose game piece: a mixed-reality escape room wrapped in Egyptian cat-goddess lore, played by connecting to the badge over USB-serial (115200 8n1) and working through a text adventure, with four front-panel buttons and an LED matrix providing in-badge feedback. Design credits split across the usual Badge.Team roles — Renze Nicolai on circuit/PCB design, Nikolett S. on artwork, Sake on the challenges, and Glu on audio.

A production quirk is documented on the maker's own badge.team page: the boards as manufactured have the SAO connector mounted on the bottom with a mirrored pinout, and the LED matrix polarity inverted from the original design intent, which the hardware repo's README also flags by noting the LED footprints are reversed, making the badge suitable for manual assembly only. Badge.Team offered on-site rework help at the event to correct this.

## Make your own

Hardware (KiCad schematic and PCB, CERN-OHL-P licensed) is published at github.com/badgeteam/hackerhotel-2020-hardware, and firmware/game software (MIT licensed) at github.com/badgeteam/hackerhotel-2020-software. The firmware is C compiled with gcc-avr and flashed to the badge over UPDI using pyupdi, indicating an AVR-family microcontroller, though the specific part number is not stated in either repository. The software repo also includes a Python game prototype used to develop the escape-room logic before it was ported to the embedded target.
