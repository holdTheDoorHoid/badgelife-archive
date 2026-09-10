---
title: BSidesPDX 2018 ATtiny861 Badge
id: bsides-portland-2018-bsidespdx-2018-attiny861-badge
layout: badge
parent: BSidespdx 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-portland-2018
year: 2018
makers:
- name: PDX Badgers
  url: https://github.com/pdxbadgers
summary: An Oregon-state-shaped electronic badge for BSidesPDX 2018, built around an ATtiny861 with charlieplexed icon LEDs and RGB accent LEDs.
functions: Cycles the 12 charlieplexed icon LEDs (mountain, coffee, rain, bridge, sasquatch, book, train, beard, bike, donut, rose, beer) and drives 4 PWM-controlled RGB LEDs; two switches select modes. Public boardtest firmware exercises the charlieplex matrix and LED cycling.
look:
  colors:
  - purple
  - yellow
  - gold
  shape: oregon outline
  themes:
  - logo
  - security
tech:
  mcu: ATtiny861
  leds:
    count: 16
    type: charlieplexed, RGB
    note: 12 yellow charlieplexed icon LEDs plus 4 PWM-controlled RGB LEDs
  display: none
  connectivity:
  - usb
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/pdxbadgers/badge-2018/tree/master/HW
  firmware_url: https://github.com/pdxbadgers/badge-2018/tree/master/FW
  eda_tool: KiCad
links:
- label: badge.gallery/badges/bsidespdx-2018-attiny861-badge
  url: https://badge.gallery/badges/bsidespdx-2018-attiny861-badge
  kind: website
- label: github.com/pdxbadgers/badge-2018
  url: https://github.com/pdxbadgers/badge-2018
  kind: repo
images:
- file: assets/images/badges/bsides-portland-2018/bsidespdx-2018-attiny861-badge/51317151de.jpg
  source: "https://github.com/pdxbadgers/badge-2018"
  credit: "PDX Badgers"
  caption: "BSidesPDX 2018 ATtiny861 badge, front (Oregon-shaped purple PCB with charlieplexed icon LEDs)"
- file: assets/images/badges/bsides-portland-2018/bsidespdx-2018-attiny861-badge/cb6ed58025.jpg
  source: "https://github.com/pdxbadgers/badge-2018"
  credit: "PDX Badgers"
  caption: "BSidesPDX 2018 ATtiny861 badge, back (sponsor logo panel)"
contact: {}
notes:
- ATTiny861-based LED badge with SAO header for BSidesPDX 2018. Found by the event-year sweep, task bsides-portland.
- 'Sweep/aggregator title used "ATTiny861" (all-caps); the maker''s own repo and datasheet spell the chip "ATtiny861", used here as the title.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/bsidespdx-2018-attiny861-badge
  title: BSidesPDX 2018 ATTiny861 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-portland); event read as ''BSidesPDX 2018''.'
- kind: url
  url: https://github.com/pdxbadgers/badge-2018
  title: pdxbadgers/badge-2018
  accessed: '2026-09-10'
  note: Maker's own repo; confirms chip, LED layout, SAO header, KiCad/firmware sources, and the Oregon-shaped board art.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Price, quantity made, and how it was distributed (free with badge registration vs. sold) are not stated anywhere found; get_one fields left empty. tech.sao_version not confirmed from available sources (repo mentions a SAO connector but not which pinout revision), left null.
last_modified_date: '2026-09-10'
---

The BSidesPDX 2018 badge is an Oregon-state-shaped PCB built by the PDX Badgers, the volunteer group behind Portland's BSides hardware badges, around an Atmel ATtiny861 microcontroller. Twelve small icons cut into the silkscreen — a mountain, a coffee cup, rain, a bridge, a sasquatch, a book, a train, a beard, a bike, a donut, a rose, and a beer — are lit by charlieplexed yellow LEDs, and four additional RGB LEDs are driven with PWM for color effects. The board charges from USB Micro-B through a Micronucleus bootloader, runs off a CR2032 coin cell, has two switches for mode control, and carries a SAO connector so other badges could plug into it.

The hardware (KiCad schematics, PCB layout, BOM, and datasheets) and firmware (C source, including a public `boardtest.ino` that cycles the LEDs and exercises the charlieplex matrix) are both published in the `pdxbadgers/badge-2018` GitHub repository, alongside the source art files for the Oregon-outline board shape and the sponsor-logo back panel. No pricing, production quantity, or distribution details (e.g., whether it was included with conference registration) turned up in the sources checked.

## Make your own

The full design is open: clone `pdxbadgers/badge-2018`, and use the `HW/` folder's KiCad files, BOM, and datasheets to fabricate the board, and the `FW/` folder's C source (built for the ATtiny861 via ATTinyCore, flashed with the Micronucleus USB bootloader) to program it.
