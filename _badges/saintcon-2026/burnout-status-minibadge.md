---
title: Burnout Status MiniBadge
id: saintcon-2026-burnout-status-minibadge
layout: badge
parent: Saintcon 2026
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2026
year: 2026
makers:
- name: J Kuro
summary: A SAINTCON-compatible minibadge that lets the wearer broadcast their conference burnout level with a single RGB LED and one push button.
functions: 'Cycles through three status modes with a button press: green (fine), yellow (low energy), red (burned out). Holding the button 3 seconds triggers an SOS distress signal in Morse code; holding it 6 seconds triggers a rainbow animation mode.'
look:
  colors:
  - black
  shape: null
  themes:
  - minimalist
tech:
  mcu: ATtiny402
  leds:
    count: 1
    type: SK6812MINI-E
    note: reverse-mount addressable RGB LED
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Design files shared on PCBWay; order as PCB-only or assembled through PCBWay'
make_your_own:
  open_source: partial
  hardware_url: https://www.pcbway.com/project/shareproject/2026_SAINTCon_Mini_Badge_792b9677.html
  firmware_url: null
  eda_tool: null
  license: CC BY-NC 4.0
  fab_url: https://www.pcbway.com/project/shareproject/2026_SAINTCon_Mini_Badge_792b9677.html
  notes: 'Firmware described as built with Arduino IDE + megaTinyCore (state machine architecture) but no firmware repo link was found on the project page.'
links:
- label: www.pcbway.com/project/shareproject/2026_SAINTCon_Mini_Badge_792b9677.html
  url: https://www.pcbway.com/project/shareproject/2026_SAINTCon_Mini_Badge_792b9677.html
  kind: fab
images:
- file: assets/images/badges/saintcon-2026/burnout-status-minibadge/e19f523e79.png
  source: "https://www.pcbway.com/project/shareproject/2026_SAINTCon_Mini_Badge_792b9677.html"
  credit: "J Kuro"
  caption: "Burnout Status MiniBadge PCB render showing the RGB LED and button"
contact: {}
notes:
- A SAINTCON 2026 minibadge with an RGB LED and pushbutton that cycles through green/yellow/red 'burnout' states, with hidden SOS and rainbow modes, built on an ATtiny402. Found by the event-year sweep, task saintcon-2026.
status: announced
sources:
- kind: url
  url: https://www.pcbway.com/project/shareproject/2026_SAINTCon_Mini_Badge_792b9677.html
  title: Burnout Status MiniBadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2026); event read as ''saintcon-2026''.'
- kind: url
  url: https://www.pcbway.com/project/shareproject/2026_SAINTCon_Mini_Badge_792b9677.html
  title: 2026 SAINTCon Mini Badge - Share Project - PCBWay
  accessed: '2026-09-08'
  note: 'Confirmed maker (J Kuro), event/year (2026 SAINTCON), functions, ATtiny402 MCU, SK6812MINI-E LED, and CC BY-NC 4.0 license; used to pull og:image for photo.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own PCBWay project page (published July 2, 2026). No storefront, price, or quantity found — this is a PCBWay share-project page (design files + fab ordering), not a sales listing, so status is set to announced rather than listed/released and get_one fields are left empty. No separate firmware repository was found, so make_your_own.firmware_url is left empty even though the page describes the firmware toolchain. No SAINTCON minibadge-wiki or Discord confirmation was checked beyond search-result snippets.'
last_modified_date: '2026-09-08'
---

The Burnout Status MiniBadge is a SAINTCON-compatible minibadge designed by J Kuro for SAINTCON 2026, built around an ATtiny402 microcontroller and a single reverse-mount SK6812MINI-E addressable RGB LED. It lets the wearer signal their current conference burnout level to people around them: a quick press cycles the LED through green (doing fine), yellow (running low), and red (burned out).

Two hidden modes reward a longer hold on the badge's single tactile button: three seconds triggers an SOS distress signal blinked out in Morse code, and six seconds switches the LED into a rainbow animation. The firmware is described as a state machine written in the Arduino IDE using megaTinyCore, targeting the ATtiny402's UPDI programming interface.

The design — a two-layer PCB with black solder mask, white silkscreen, and ENIG finish — was published as a PCBWay shared project on July 2, 2026, offering the Gerber files for download and PCB-only or assembled ordering directly through PCBWay, under a CC BY-NC 4.0 license. No separate storefront, firmware repository, price, or production quantity was found, so this appears to be a build-it-yourself release rather than a badge distributed at the conference itself.
