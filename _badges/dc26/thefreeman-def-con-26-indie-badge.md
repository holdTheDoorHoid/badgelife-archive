---
title: THEFREEMAN - DEF CON 26 Indie Badge
id: dc26-thefreeman-def-con-26-indie-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
summary: A passive, battery-powered indie badge shaped like a Vortigaunt (from Half-Life 2), with red and orange LEDs shining through the board to light up its eyes.
functions: 'No interactivity or MCU; the badge lights up via coin-cell power the moment a battery is installed, illuminating the Vortigaunt-style eyes.'
look:
  colors: [black, red, orange]
  shape: null
  themes: [video games, sci-fi]
tech:
  mcu: none
  leds:
    count: 5
    type: discrete
    note: 3 red OSRAM T776-P2S1-1-Z and 2 orange OSRAM T776-Q2T1-24-Z LEDs, placed to shine through the PCB and light the eyes.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '~40'
  availability: sold_out
  availability_note: 'Checked 2026-09-07: Tindie listing shows "this product is no longer available for sale."'
  distribution: [purchase]
  where: Sold via TwinkleTwinkie's Tindie store around DEF CON 26 (2018); included a green lobster-claw lanyard and 2 CR2032 batteries with the assembled badge.
make_your_own:
  open_source: yes
  hardware_url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  firmware_url: null
  eda_tool: KiCad
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/thefreeman-def-con-26-indie-badge/
  title: THEFREEMAN - DEF CON 26 Indie Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc26''.'
- kind: url
  url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  title: THEFREEMAN - DEF CON 26 INDIE BADGE | Hackaday.io
  accessed: '2026-09-07'
  note: 'Maker''s project page: Vortigaunt theme, LED part numbers, KiCad/Gerber files, ~40 boards made, passive/no-MCU design.'
images:
- file: assets/images/badges/dc26/thefreeman-def-con-26-indie-badge/796d295e58.jpg
  source: "https://www.tindie.com/products/twinkletwinkie/thefreeman-def-con-26-indie-badge/"
  credit: "TwinkleTwinkie"
  caption: "THEFREEMAN badge lit up, showing the Vortigaunt-inspired glowing eyes"
- file: assets/images/badges/dc26/thefreeman-def-con-26-indie-badge/60f3a6ff41.jpg
  source: "https://www.tindie.com/products/twinkletwinkie/thefreeman-def-con-26-indie-badge/"
  credit: "TwinkleTwinkie"
  caption: "THEFREEMAN badge, unlit, showing PCB artwork"
contact: {}
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, event, LED count/parts, battery, open-source status, ~40 units made) confirmed on the maker''s own Hackaday.io project page and Tindie store listing. Exact original price and precise quantity beyond "approximately 40" were not stated anywhere found.'
last_modified_date: '2026-09-07'
---

THEFREEMAN is TwinkleTwinkie's first DEF CON indie badge, made for DEF CON 26 (2018). It is a passive, single-layer PCB badge shaped after the Vortigaunt aliens from Valve's Half-Life 2, with three red and two orange OSRAM SMD LEDs mounted so their light shines through the board and out the character's eyes. There is no microcontroller; a single CR2032 coin cell powers the LEDs directly. The maker built the project partly to learn KiCad and to treat the PCB itself as an art medium, and released the KiCad schematic and Gerber files for both a full badge and a smaller SAO version.

Roughly 40 boards were made and sold through TwinkleTwinkie's Tindie store, with the assembled badge shipping alongside a green lobster-claw lanyard and two CR2032 batteries meant to last the length of the conference. The listing is now retired and no longer available for purchase.
