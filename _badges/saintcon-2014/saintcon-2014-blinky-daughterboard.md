---
title: SAINTCON 2014 Blinky Daughterboard
id: saintcon-2014-saintcon-2014-blinky-daughterboard
layout: badge
parent: SAINTCON 2014
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: saintcon-2014
year: 2014
makers:
- name: Matt Lorimer
summary: An optional $15 expansion board for the SAINTCON 2014 badge, adding eight tri-color LEDs driven by two TI PWM (TLC5940) chips with cycling blinky patterns.
functions: Runs button-selectable LED animation patterns (color scan from outside to middle, sequential color changes, solid random colors) with adjustable brightness; four extra LEDs light an acrylic panel.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 8
    type: RGB
    note: Ten RGB LED positions wired to two TLC5940 PWM driver chips (30 channels used of a possible 32), plus four single-color LEDs for backlighting an acrylic panel.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: $15
  price_usd: 15
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold as an optional add-on kit at SAINTCON 2014, attaching to the main SAINTCON 2014 badge via female headers.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://gist.github.com/jbdatko/069f03a02415d5adef2a
  eda_tool: null
links:
- label: gist.github.com/jbdatko/069f03a02415d5adef2a
  url: https://gist.github.com/jbdatko/069f03a02415d5adef2a
  kind: repo
- label: 'Josh Datko: "Hacking the SAINTCON Badge"'
  url: https://datko.net/2014/10/24/hacking_saintcon_badge/
  kind: article
images:
  - file: assets/images/badges/saintcon-2014/saintcon-2014-blinky-daughterboard/83363e66b8.jpg
    source: "https://datko.net/2014/10/24/hacking_saintcon_badge/"
    credit: "Josh Datko"
    caption: "The blinky daughterboard"
contact: {}
notes:
- 'Sweep''s original wording: "An optional $15 expansion/daughterboard for the SAINTCON 2014 badge with two TI PWM drivers and eight tri-color LEDs, driven by TLC5940-based blinky firmware written by Matt Lorimer." Confirmed by Josh Datko''s conference recap (datko.net) and Matt Lorimer''s firmware gist; title kept as-is since no source gives it a different name.'
status: listed
sources:
- kind: url
  url: https://gist.github.com/jbdatko/069f03a02415d5adef2a
  title: SAINTCON 2014 Blinky Daughterboard
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2014); event read as ''saintcon-2014''.'
- kind: url
  url: https://gist.github.com/jbdatko/069f03a02415d5adef2a
  title: Cylon SAINTCON Blinky (gist)
  accessed: '2026-09-10'
  note: Matt Lorimer's blinky firmware itself; confirms TLC5940 driver, 10 RGB positions (30 of 32 channels used), button-cycled patterns, four extra LEDs.
- kind: url
  url: https://datko.net/2014/10/24/hacking_saintcon_badge/
  title: 'Hacking the SAINTCON Badge - fortune datko'
  accessed: '2026-09-10'
  note: Josh Datko's SAINTCON 2014 recap; confirms the $15 daughterboard with two TI PWM drivers and eight tri-color LEDs, attached via female headers to the free ATmega-based badge by Luke Jenkins and Klint Holmes; source of the "blinkies.jpg" photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: No storefront, quantity, or PCB/design-file source was found beyond the firmware gist, so get_one.quantity, get_one.availability, and make_your_own.hardware_url stay empty/unknown. The firmware gist is public (partial open source; no hardware files located).
last_modified_date: '2026-09-10'
---

Sold as a $15 optional add-on at SAINTCON 2014, this daughterboard plugged into the conference's free Arduino-compatible badge (designed by Luke Jenkins and Klint Holmes) via female headers. It added eight tri-color LEDs driven by two Texas Instruments TLC5940 PWM chips, plus four single-color LEDs used to backlight an acrylic panel.

The blinky patterns were written by Matt Lorimer, whose firmware cycles through several modes via a push button: a color scan from the outside LEDs inward, sequential per-LED color changes, and a solid-color mode with randomized color and adjustable brightness. Attendees who assembled both the badge and the daughterboard were seen experimenting with further pattern hacks (e.g., a "Cylon" scanning effect) during the conference's hardware hacking village.

## Make your own

Matt Lorimer's original blinky firmware (Arduino .ino, using a TLC5940 library) is published as a public gist. No schematic, PCB layout, or bill of materials for the daughterboard itself has been located.
