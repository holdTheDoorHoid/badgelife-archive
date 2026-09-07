---
title: Nullibadge 2.0 (DC26)
id: dc26-nullify-badge-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
series: Nullibadge
makers:
- name: Nullify (Omaha, NE)
  url: https://twitter.com/nullibadge
summary: A custom PCB badge built by the Nullify hacking community of Omaha, NE for DEF CON 26, with 16 addressable LEDs, a 4-character alphanumeric display, and an IR "shoot other badges" tag feature.
functions: 16 customizable LED animations; 4-character display that runs a slot-machine animation to pick a beverage (SHOT, BEER, VDKA, WSKY, WATR); scrolling text; a button-driven menu (A+B+Y=Menu, A=Left, B=Right, X=Back, Y=Enter); IR transmitter/receiver for badge-to-badge "tag" interaction, with the maker noting the IR transmitter is powerful enough to affect TVs at range if reprogrammed.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - meme
tech:
  mcu: PIC16LF18346
  leds:
    count: 16
    type: null
    note: 16 customizable LEDs with animations
  display: 4-character alphanumeric display
  connectivity:
  - ir
  battery: null
  sao_version: none
get_one:
  price: $60
  price_usd: 60
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold on-site at DEF CON 26, cash only, with online pre-registration open beforehand.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/nullibadge/defcon2017
  eda_tool: null
links:
- label: nu.llify.com
  url: http://nu.llify.com/
  kind: website
- label: Nullibadge firmware source (GitHub, defcon2017 repo)
  url: https://github.com/nullibadge/defcon2017
  kind: repo
- label: Nullibadge on Twitter
  url: https://twitter.com/nullibadge
  kind: social
- label: Defcon 25 Nullibadge photo album (Imgur)
  url: https://imgur.com/a/Vn8pm
  kind: article
images:
- file: assets/images/badges/dc26/nullify-badge-dc26/02f7237784.jpg
  source: "https://imgur.com/a/Vn8pm"
  credit: "Nullify hacking community"
  caption: "Nullibadge (DEF CON 25/26 era) PCB badge"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: http://nu.llify.com/
  title: Nullify Badge (DC26)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 26''.'
- kind: url
  url: http://nu.llify.com/
  title: NulliBadge 2.0
  accessed: '2026-09-07'
  note: Primary source for badge description, features, MCU, LED count, price, and distribution details.
- kind: url
  url: https://github.com/nullibadge/defcon2017
  title: nullibadge/defcon2017 firmware repository
  accessed: '2026-09-07'
  note: Firmware source for the badge line; site states DC26 badge reused this DC25 codebase. No hardware files or license found in the repo.
- kind: url
  url: https://imgur.com/a/Vn8pm
  title: Defcon 25 Nullibadge photo album
  accessed: '2026-09-07'
  note: Photo of the badge (linked from the DC26 project page as "Defcon 25 nullibadge pictures"); used for the saved image.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The maker''s own project page (nu.llify.com) is the primary source and calls this "an Unofficial Defcon 26 Badge," confirming event/year. No PCB hardware files (schematic/gerbers) were found, only the firmware repo, which is explicitly for the earlier DC25 board (the maker states DC26 reused the same codebase) -- so make_your_own.open_source is marked partial and hardware_url left empty. Quantity made, exact LED type/part number, battery type, and current availability were not stated anywhere found. The one photo saved is captioned by the maker''s own page as DC25-era Nullibadge pictures, since no DC26-specific photo was found; the hardware is stated to be the same platform/codebase.'
last_modified_date: '2026-09-07'
---

Nullibadge 2.0 was an unofficial badge built and sold by Nullify, a hacking community based in Omaha, Nebraska, for DEF CON 26 in 2018. It runs on a PIC16LF18346 microcontroller and carries 16 addressable LEDs for custom animations alongside a 4-character alphanumeric display. The display's headline gimmick is a slot-machine-style animation that lands on a randomly chosen drink (shot, beer, vodka, whiskey, or water), and it can also scroll arbitrary text through a simple four-button menu.

Beyond blinky lights, the badge includes an IR transmitter and receiver meant for badge-to-badge "tag" play at close range. The maker's page notes, half as a warning and half as a boast, that the same IR transmitter is powerful enough to be repurposed to switch off televisions at a distance with the right code. The badge sold for $60 cash-only on site at DEF CON 26, with pre-registration open ahead of the con.

## Make your own

The community published the firmware for the prior year's board on GitHub (`nullibadge/defcon2017`), built in MPLAB X with the XC8 compiler and Microchip Code Configurator, targeting the PIC16LF18346 (or its non-L predecessor on earlier boards). The DC26 project page states the 2018 badge reused this same codebase, though no separate hardware files (schematic, PCB layout, or gerbers) or an explicit license were found for either year's board. Reprogramming requires a PICkit3 programmer, which the maker notes costs around $20.
