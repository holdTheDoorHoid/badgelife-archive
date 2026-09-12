---
title: ToorCamp 2018 Badge (electronic jar of fireflies)
id: toorcamp-2018-toorcamp-2018-badge-electronic-jar-of-fireflies
layout: badge
parent: ToorCamp 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: toorcamp-2018
year: 2018
makers:
- name: Great Scott Gadgets
  url: https://greatscottgadgets.com/toorcamp2018badge/
summary: A solder-it-yourself badge for ToorCamp 2018 that attendees built and housed inside a canning jar, six blinking green LEDs standing in for fireflies.
functions: Six LEDs blink in a randomized firefly-like pattern; no other interactivity documented.
look:
  colors:
  - green
  shape: null
  themes:
  - nature
  - learn to solder
  - kit
tech:
  mcu: MSP430G2211
  leds:
    count: 6
    type: discrete
    note: Six green 3mm round through-hole LEDs (D1-D6) simulating fireflies.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  availability_note: 'Checked 2026-09-08: Great Scott Gadgets'' page is marked archival; it offers firmware-reflash help by email for people who already own a unit, but does not sell new ones.'
  distribution:
  - kit
  where: Distributed as a self-assembly kit at ToorCamp 2018, built at soldering stations at the event and mounted inside a standard small (e.g. 4 oz Ball) canning jar.
make_your_own:
  open_source: true
  hardware_url: https://github.com/greatscottgadgets/toorcamp2018badge
  firmware_url: https://github.com/greatscottgadgets/toorcamp2018badge
  eda_tool: null
  license: BSD-3-Clause
  notes: Repository is archived (read-only) as of 2022-12-07; Great Scott Gadgets' own project page has a printable assembly walkthrough with build photos.
links:
- label: github.com/greatscottgadgets/toorcamp2018badge
  url: https://github.com/greatscottgadgets/toorcamp2018badge
  kind: repo
- label: Great Scott Gadgets - ToorCamp 2018 Badge
  url: https://greatscottgadgets.com/toorcamp2018badge/
  kind: website
images:
- file: assets/images/badges/toorcamp-2018/toorcamp-2018-badge-electronic-jar-of-fireflies/a01b809db3.jpg
  source: https://greatscottgadgets.com/toorcamp2018badge/
  credit: Great Scott Gadgets
  caption: Assembled badge installed in a canning jar, the finished 'jar of fireflies'
- file: assets/images/badges/toorcamp-2018/toorcamp-2018-badge-electronic-jar-of-fireflies/d232474e5f.jpg
  source: https://greatscottgadgets.com/toorcamp2018badge/
  credit: Great Scott Gadgets
  caption: Assembled PCB with the six green through-hole LEDs installed
contact: {}
notes:
- Official ToorCamp 2018 badge, described by its makers as an electronic jar of fireflies, with hardware and firmware released on GitHub. Found by the event-year sweep, task con-toorcon.
status: released
sources:
- kind: url
  url: https://github.com/greatscottgadgets/toorcamp2018badge
  title: ToorCamp 2018 Badge (electronic jar of fireflies)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-toorcon); event read as ''ToorCamp 2018''.'
- kind: url
  url: https://greatscottgadgets.com/toorcamp2018badge/
  title: ToorCamp 2018 Badge - Great Scott Gadgets
  accessed: '2026-09-08'
  note: Maker's own archival project page; source for MCU, LED count/type, battery, resistor values, distribution as a soldering-station kit at the event, and assembly photos.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Repository and GitHub metadata confirm license (BSD-3-Clause) and archived (read-only) status. Price and quantity made were not stated on either the repo or the maker's project page, so those fields are left empty. No storefront or resale listing found; treated as not_released rather than sold_out since it was originally a free/included con badge, not a store item.
last_modified_date: '2026-09-10'
model:
  file: assets/models/toorcamp-2018/toorcamp-2018-badge-electronic-jar-of-fireflies.glb
  method: kicad
  source_file: hardware/jig/toorcamp2018jig.kicad_pcb
  generated: '2026-09-10'
  bytes: 423640
---

The ToorCamp 2018 badge is a learn-to-solder kit made by Great Scott Gadgets for the 2018 ToorCamp gathering. Attendees assembled it themselves at soldering stations, populating an MSP430G2211 microcontroller, six green 3mm LEDs, and a CR2032 coin-cell holder onto a small PCB, then dropped the finished board into a standard canning jar (about the size of a 4 oz Ball jar). The six LEDs fire in a randomized, staggered pattern meant to mimic fireflies glowing inside the jar, giving the badge its name.

Great Scott Gadgets released both the hardware design and firmware for the badge on GitHub under a BSD-3-Clause license, and their own site preserves a full photographed build guide (collecting parts, installing the battery clip, the MCU, each resistor, the LEDs, and finally the board into the jar). The GitHub repository has since been archived (read-only, as of December 2022), and the project page is now explicitly marked as an archival resource; Great Scott Gadgets still offers help over email to owners who need to reflash an old unit's firmware, but the badge itself is not sold or reproduced as a product.

No price or production quantity for the original ToorCamp 2018 run was found in either the repository or the maker's page, so those fields are left blank rather than guessed.
