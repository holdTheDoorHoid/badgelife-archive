---
title: Shift Register for Supercon Badge
id: supercon-2018-shift-register-for-supercon-badge
layout: badge
parent: Supercon 2018
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2018
year: 2018
makers:
- name: Mike Szczys
  url: https://hackaday.io/mike-szczys
summary: A small 74HC595 shift-register expansion board that plugs into the 2018 Hackaday Superconference badge's expansion port to drive 8 extra LEDs from the badge's BASIC interpreter.
functions: 'Demo/tutorial board: the shift register''s 8 outputs each drive an LED, and example BASIC code on the badge plays the tune "Chopsticks" with the LEDs lighting like piano keys in time with tones from the badge speaker.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: none
  leds:
    count: 8
    type: discrete
    note: Driven from the outputs of a 74HC595 shift register, not individually addressable RGB.
  display: none
  connectivity:
  - none
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/162054-shift-register-for-supercon-badge
  url: https://hackaday.io/project/162054-shift-register-for-supercon-badge
  kind: hackaday
images:
- file: assets/images/badges/supercon-2018/shift-register-for-supercon-badge/e521e1c8ad.jpg
  source: "https://hackaday.io/project/162054-shift-register-for-supercon-badge"
  credit: "Mike Szczys"
  caption: "The shift register expansion board plugged into the 2018 Supercon badge"
- file: assets/images/badges/supercon-2018/shift-register-for-supercon-badge/f0985cb974.jpg
  source: "https://hackaday.io/project/162054-shift-register-for-supercon-badge"
  credit: "Mike Szczys"
  caption: "Close-up of the 74HC595 shift register board and LEDs"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/162054-shift-register-for-supercon-badge
  title: Shift Register for Supercon Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/162054-shift-register-for-supercon-badge
  title: Shift Register for Supercon Badge
  accessed: '2026-09-07'
  note: 'WebFetch of the project page: identified maker (Mike Szczys), event/year (2018 Hackaday Superconference badge), function (74HC595-driven LED demo playing "Chopsticks"), and pulled og:image and gallery image URLs.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a demo/tutorial expansion board Mike Szczys (a Hackaday editor) built to show off the 2018 Supercon badge's expansion port and BASIC interpreter, not a mass-produced or sold badge/SAO. No price, quantity, or design-file links were found on the project page; it references "the Supercon Badge project page" for context but does not link it directly. No repo or Gerbers were located, so make_your_own fields are left empty rather than guessed.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/shift-register-for-supercon-badge/
---

This is a small demonstration board built by Hackaday editor Mike Szczys for the 2018 Hackaday Superconference badge. It plugs into the badge's expansion port and adds a 74HC595 shift register driving 8 discrete LEDs, using three of the badge's GPIO pins for data, latch, and clock signals.

The board isn't a standalone badge or a distributed SAO; it's a tutorial/example project showing what the 2018 Supercon badge's expansion header and onboard BASIC interpreter could do. The example program plays "Chopsticks," lighting the 8 LEDs like piano keys in sync with tones from the badge's speaker. No information on price, quantity built, or public design files was found on the project page.
