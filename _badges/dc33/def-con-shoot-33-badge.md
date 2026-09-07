---
title: DEF CON Shoot 33 Badge
id: dc33-def-con-shoot-33-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc33
year: 2025
makers:
- name: seeess
  url: https://github.com/seeess
summary: 'A 3D-printed, non-electronic novelty badge for the DEF CON Shoot 33 side event: a spring-loaded trigger mechanism that dispenses Tic Tacs from a rubber-banded container on top.'
functions: 'Purely mechanical. Unscrew the bolts, insert the trigger, place a Tic Tac container on top, and rubber-band it between the trigger and upper receiver. Pulling the trigger releases the spring-loaded sear to dispense candy.'
look:
  colors: []
  shape: null
  themes:
  - meme
  - hardware tool
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/seeess/Defcon-Shoot-33-Badge
  firmware_url: null
  eda_tool: null
links:
- label: github.com/seeess/Defcon-Shoot-33-Badge
  url: https://github.com/seeess/Defcon-Shoot-33-Badge
  kind: repo
images:
- file: assets/images/badges/dc33/def-con-shoot-33-badge/8ddd327de3.png
  source: "https://github.com/seeess/Defcon-Shoot-33-Badge"
  credit: "seeess"
  caption: "Assembled Defcon Shoot 33 badge: a 3D-printed spring-loaded Tic Tac dispenser"
contact: {}
status: released
sources:
- kind: url
  url: https://github.com/seeess/Defcon-Shoot-33-Badge
  title: DEF CON Shoot 33 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc33''.'
- kind: url
  url: https://raw.githubusercontent.com/seeess/Defcon-Shoot-33-Badge/master/README.md
  title: 'README: Defcon-Shoot-33-Badge'
  accessed: '2026-09-07'
  note: 'Assembly instructions, spring specs, and confirmation this is a purely mechanical (no electronics) badge; source of the badge photo.'
- kind: url
  url: https://github.com/seeess/Defcon-Shoot-23-Badge
  title: 'seeess/Defcon-Shoot-23-Badge'
  accessed: '2026-09-07'
  note: 'Confirms seeess makes a "Defcon Shoot NN Badge" each year for the unofficial DEF CON Shoot side event; earlier years (e.g. Shoot 23) were electronic with a shot counter, unlike this mechanical Shoot 33 edition.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own repo confirms the design, assembly, and that it is non-electronic. Could not find price, quantity made, or distribution details specific to the Shoot 33 edition (a DEF CON forum thread about an earlier, differently-designed "Defcon Shoot Badge (non-electronic)" mentions $10/badge and a run of 100, but that thread describes a different year''s badge design and is not cited here for Shoot 33 specifics). Made for the unofficial DEF CON Shoot 33 side event (a shooting-range meetup), not an official DEF CON badge.'
last_modified_date: '2026-09-07'
---

The DEF CON Shoot 33 Badge is a novelty item made by seeess for the unofficial DEF CON Shoot side event, a shooting-range meetup held alongside DEF CON. Unlike seeess's earlier Shoot badges (the Shoot 23 edition, for example, was a full electronic badge with a microphone-based shot counter and a seven-segment display), the Shoot 33 badge is purely mechanical: a set of 3D-printed parts (bolt, upper and lower receivers, trigger, and hardware) that assemble into a small spring-loaded gun. Instead of firing anything dangerous, it holds a Tic Tac container on top, secured with rubber bands, and pulling the trigger releases a spring-loaded sear to dispense candy.

The repository provides STL files for all the printed parts along with print-orientation notes (the bolt should be printed upside down with supports on a smooth plate) and spring specifications: a 10mm outside diameter, 50mm uncompressed length coil, with the maker noting an earlier 0.1mm-wire/11-turn spring was too strong and cracked PETG bolts, settling on a gentler 0.8mm-wire, 16-turn spring instead. Triggers were shipped uninstalled to avoid the plastic spring warping in Las Vegas heat, requiring buyers to unscrew the bolts and assemble the trigger themselves.

No price, production quantity, or sales venue specific to this edition could be confirmed from available sources.

## Make your own

Hardware files (STLs) are published in the linked GitHub repository under an open license; there is no firmware, as the badge is entirely mechanical. Print the parts per the README's orientation notes, source or wind a matching spring, then assemble per the included instructions.
