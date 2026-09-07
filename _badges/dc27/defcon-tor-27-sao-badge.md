---
title: Defcon-Tor-27 SAO/Badge
id: dc27-defcon-tor-27-sao-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: seeess
  url: https://github.com/seeess
summary: 'A Tor Project fundraiser SAO/badge made by seeess for DEF CON 27 (2019): five LEDs and one button drive eleven blinking modes plus two unlockable minigames, and it can run either off a host badge''s SAO header or standalone on two CR123A batteries.'
functions: 'Cycles through 11 LED blinking patterns (very slow/slow/fast/very fast cycle, slow/fast cylon, strobe, slow/fast random, binary counter, off) via a single button. Includes a Reaction Game (press at the right moment for a low score) and a Button Mashing Game (rapid presses light more LEDs); winning each unlocks an extra mode (even/odd, heartbeat). Last mode and unlocks persist in EEPROM across power cycles; holding the button at power-up can disable or reset EEPROM.'
look:
  colors: []
  shape: null
  themes:
  - privacy
  - security
tech:
  mcu: ATtiny402
  leds:
    count: 5
    type: discrete
    note: Lumileds L1SP-PRP2002800000 LEDs, 15-ohm 0603 current-limit resistors
  display: none
  connectivity: []
  inputs:
  - buttons
  battery: 2x CR123A via 2.0mm JST connector (included), or powered by host badge
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: 500+
  availability: unknown
  distribution:
  - purchase
  where: Given to the Tor Project to sell as a fundraiser at their DEF CON 27 (2019) vendor booth; came with a lanyard, batteries, battery holder, sticker, and zip ties.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/seeess/Defcon-Tor-27
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: WTFPL
  fab_url: null
  notes: 'Repo has the ATtiny402 firmware (main.c, Makefile) and a text BOM in the README, but no schematic or PCB/gerber files.'
links:
- label: github.com/seeess/Defcon-Tor-27
  url: https://github.com/seeess/Defcon-Tor-27
  kind: repo
- label: 'Feature overview video'
  url: https://youtu.be/Rasb8VQQdyw
  kind: video
images:
- file: assets/images/badges/dc27/defcon-tor-27-sao-badge/73a45a80ba.jpg
  source: "https://github.com/seeess/Defcon-Tor-27"
  credit: "seeess"
  caption: "Tor DEF CON 27 SAO/badge, front and back"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/seeess/Defcon-Tor-27
  title: Defcon-Tor-27 SAO/Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 27''.'
- kind: url
  url: https://github.com/seeess/Defcon-Tor-27
  title: 'Defcon 27 Tor Badge / SAO Manual (README)'
  accessed: '2026-09-07'
  note: 'Full README: maker (seeess), event/year, in-the-box contents, SAO v1.69bis power scheme, LED/button functionality, games and unlocks, EEPROM behavior, ATtiny402 BOM, WTFPL license, and the badge photo.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Price and exact quantity produced are not stated (only "500+ JST battery holders" crimped, used here as a rough quantity floor). Current sold-out/availability status was not checked (2019 one-off con item, no separate storefront found). No schematic or PCB/gerber files are published, only firmware and a parts-list BOM.'
last_modified_date: '2026-09-07'
---

Seeess designed this Tor-themed SAO/badge for DEF CON 27 (2019) and gave the run to the Tor Project to sell at their vendor booth as a fundraiser, absorbing the up-front cost of a custom three-color PCB, dye-sub lanyards, and custom boxes himself. Each unit ships as a small ATtiny402-driven board with five LEDs and a single button, usable either as a standalone badge (powered by two included CR123A batteries on a JST connector) or plugged into a host badge as a v1.69bis-standard SAO, since it only draws 3V3/GND from the header.

Functionally it is a fidget toy with a scoring layer: eleven LED patterns are cycled with the button, and two hidden minigames (a reaction-time test and a button-mashing meter) unlock two additional modes on a good score. State, including the last mode and any unlocks, is saved to EEPROM so it survives power cycles, and a button-hold-at-boot sequence can reset or lock out EEPROM writes for recovery. The firmware (main.c, compiled via a Makefile for the ATtiny402/UPDI toolchain) and a full bill of materials are published on GitHub under the WTFPL, though no schematic or PCB/gerber files accompany it, so it is only partially open source.

The maker's README also doubles as a candid write-up of using Seeed Studio for the three-color fab run (as part of Seeed's 2019 badge-sponsorship discount program, in exchange for an honest review), and includes a short video overview of the badge's features.
