---
title: Supercon II badge
id: supercon-2016-supercon-ii-badge
layout: badge
parent: Hackaday Supercon 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2016
year: 2016
makers:
- name: Voja Antonic
  url: https://hackaday.io/voja
  role: hardware design
- name: Dusan Petrovic
  url: null
  role: co-designer
summary: The official conference badge for Hackaday Superconference II (Pasadena, Nov 5-6 2016), a PIC-based follow-up to the earlier Belgrade Conference badge with a 128-LED matrix display and infrared badge-to-badge communication.
functions: Scrolling/animated LED matrix display, infrared transceiver for badge-to-badge or app interaction, onboard accelerometer, 5-bit I/O expansion port; firmware is updated by dragging a HEX file onto the badge, which enumerates over USB as a mass-storage device ("HackABadge" custom bootloader).
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
  - learn to solder
tech:
  mcu: PIC18F25K50
  leds:
    count: 128
    type: discrete
    note: 8x16 discrete LED matrix, multiplexed via a 74HC138 3-to-8 decoder driving the anodes; refresh uses about 1% of CPU time.
  display: LED matrix 8x16
  connectivity:
  - ir
  - usb
  inputs: []
  battery: battery-powered (type not specified in source)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of Hackaday Superconference II, November 5-6, 2016, Pasadena, CA.
make_your_own:
  open_source: yes
  hardware_url: https://hackaday.io/project/16401-supercon-ii-badge
  firmware_url: https://hackaday.io/project/16401-supercon-ii-badge
  eda_tool: null
  gerbers_url: https://hackaday.io/project/16401-supercon-ii-badge
  bom_url: null
  license: null
  fab_url: null
  notes: Hackaday.io project page hosts PCB files (Protel format), Gerbers (five badges per panel), firmware HEX files, and manuals (PDF and other formats).
links:
- label: hackaday.io/project/16401-supercon-ii-badge
  url: https://hackaday.io/project/16401-supercon-ii-badge
  kind: hackaday
images:
- file: assets/images/badges/supercon-2016/supercon-ii-badge/2f886a6b58.jpg
  source: "https://hackaday.io/project/16401-supercon-ii-badge"
  credit: "Voja Antonic / Dusan Petrovic"
  caption: "Supercon II badge PCB"
- file: assets/images/badges/supercon-2016/supercon-ii-badge/2d656cb9ab.jpg
  source: "https://hackaday.io/project/16401-supercon-ii-badge"
  credit: "Voja Antonic / Dusan Petrovic"
  caption: "Supercon II badge, front view"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/16401-supercon-ii-badge
  title: Supercon II badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''Supercon 2''.'
- kind: url
  url: https://hackaday.io/project/16401-supercon-ii-badge
  title: Supercon II badge
  accessed: '2026-09-07'
  note: 'Full project page fetch: confirmed maker names, event (Superconference II, Nov 5-6 2016, Pasadena), MCU, LED matrix, IR transceiver, accelerometer, USB bootloader, and availability of Gerbers/firmware/manuals.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Event corrected from supercon-2018 to supercon-2016: the project page states this badge was made for Hackaday Superconference II, held November 5-6 2016 in Pasadena, not 2018. Battery type/chemistry, exact quantity made, and price are not stated on the project page and are left empty. A hackaday.com companion article (search suggested hackaday.com/2016/11/04/hackaday-superconference-badge-part-2-hardware/) returned 404 and was not used.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2018/supercon-ii-badge/
---

The Supercon II badge was the official conference badge for Hackaday Superconference II, held November 5-6, 2016 in Pasadena, California. It was designed by Voja Antonic and Dusan Petrovic as a refinement of their earlier Belgrade Conference badge, built around a PIC18F25K50 microcontroller running at 48 MHz. Its centerpiece is a display made of 128 discrete LEDs arranged as a matrix, multiplexed by a 74HC138 decoder so that refreshing it consumes only about 1% of the processor's time.

Beyond the display, the badge adds an integrated accelerometer, a 5-bit I/O expansion connector, and an infrared transceiver (a 940 nm LED paired with a TSOP6240 receiver) for badge-to-badge or app-driven interaction. Microchip built a custom USB bootloader for the project, nicknamed "HackABadge," which makes the badge enumerate as a USB mass-storage drive so firmware updates are done by simply dragging a HEX file onto it.

The badge was distributed free to Superconference II attendees and was not sold commercially afterward. Its designers published the full PCB files (in Protel format), Gerbers laid out five-badges-per-panel, firmware HEX files, and manuals on the Hackaday.io project page, making it straightforward for anyone to build their own.
