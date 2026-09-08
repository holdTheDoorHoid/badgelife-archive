---
title: Ph0xx (Fri3d Camp 2018 Badge)
id: fri3d-2018-fri3d-2018-ph0xx-badge-2
layout: badge
parent: Fri3d 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: fri3d-2018
year: 2018
makers:
- name: Fri3d Camp
  url: https://github.com/Fri3dCamp
summary: Ph0xx is the ESP32-WROOM-32 attendee badge for Fri3d Camp 2018 in Belgium, with two 5x7 LED matrices, an ADXL345 accelerometer, an 18650 battery with charger, buttons and touch pads, a buzzer, Lego Technic compatible holes, and Jewel expansion headers on its ears; this repo is its official Arduino library.
functions: Blinky animations on the two 5x7 LED matrices, motion sensing via the ADXL345 accelerometer, a buzzer for sound, two buttons plus two capacitive touch pads for input, and expansion via Jewel add-on boards (an "Air Jewel" for dust/GPS sensing and a "Bot Jewel" for servo control) plugged into headers on the badge's ear-shaped tips.
look:
  colors:
  - white
  - gold
  - yellow
  - orange
  shape: fox
  themes:
  - animal
  - mascot
tech:
  mcu: ESP32-WROOM-32
  leds:
    count: 70
    type: discrete
    note: Two 5x7 LED matrices (35 LEDs each) forming the badge's eyes/display.
  display: LED matrix 5x7 x2
  connectivity:
  - wifi
  - ble
  inputs:
  - buttons
  - touch
  - accelerometer
  battery: 18650 Li-ion with TP4056 charger and DW01-P protection
  sao_version: none
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/Fri3dCamp/badge
  firmware_url: https://github.com/Fri3dCamp/Fri3dBadge
  eda_tool: null
get_one:
  price: ''
  price_usd: null
  quantity: ~650 boards manufactured
  availability: free
  distribution:
  - free_drop
  where: Given to roughly 600 attendees at Fri3d Camp 2018 in Belgium (August 2018); not sold.
links:
- label: github.com/Fri3dCamp/Fri3dBadge
  url: https://github.com/Fri3dCamp/Fri3dBadge
  kind: repo
- label: github.com/Fri3dCamp/badge
  url: https://github.com/Fri3dCamp/badge
  kind: repo
  archived: https://web.archive.org/web/20260312123042/https://github.com/Fri3dCamp/badge
- label: hackaday.io/project/160451-ph0xx
  url: https://hackaday.io/project/160451-ph0xx
  kind: hackaday
  archived: https://web.archive.org/web/20260904220754/https://hackaday.io/project/160451-ph0xx
- label: web.archive.org/web/2019/wiki2018.fri3d.be/index.php?title=Badge
  url: https://web.archive.org/web/2019/http://wiki2018.fri3d.be/index.php?title=Badge
  kind: website
images:
- file: assets/images/badges/fri3d-2018/fri3d-2018-ph0xx-badge-2/0a86bd7ee4.jpg
  source: https://hackaday.io/project/160451-ph0xx
  credit: Wim Van Gool / Fri3d Camp
  caption: Ph0xx badge, ESP32-WROOM-32 attendee badge for Fri3d Camp 2018
  archived: https://web.archive.org/web/20260904220754/https://hackaday.io/project/160451-ph0xx
- file: assets/images/badges/fri3d-2018/fri3d-2018-ph0xx-badge-2/4727e9aab7.jpg
  source: https://hackaday.io/project/160451-ph0xx
  credit: Wim Van Gool / Fri3d Camp
  caption: Ph0xx badge with two 5x7 LED matrices and touch buttons
  archived: https://web.archive.org/web/20260904220754/https://hackaday.io/project/160451-ph0xx
contact: {}
notes:
- The Fri3dCamp/badge repository (hardware/design files) shows GitHub topics including ATmega32u4/AVR/IR in web search summaries, which conflicts with the ESP32-WROOM-32 chip confirmed on the maker's Hackaday.io project page; this may reflect an early prototype revision or repo mislabeling. Not resolved from available sources.
status: released
sources:
- kind: url
  url: https://github.com/Fri3dCamp/Fri3dBadge
  title: Fri3dCamp/Fri3dBadge - Arduino library for the Fri3d Camp badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/160451-ph0xx
  title: Ph0xx - Hackaday.io
  accessed: '2026-09-07'
  note: Maker's project page; confirmed ESP32-WROOM-32 chip, makers Wim Van Gool and Bert Outtier, ~600 attendees, ~650 boards manufactured, features, and provided gallery photos.
  archived: https://web.archive.org/web/20260904220754/https://hackaday.io/project/160451-ph0xx
- kind: url
  url: https://github.com/Fri3dCamp/badge
  title: Fri3dCamp/badge - hardware design repository
  accessed: '2026-09-07'
  note: Hardware/design-files repo; description mentions Dutch tagline about needing a camp badge and prototype photos, but did not yield chip/LED/price specifics beyond what Hackaday confirmed.
  archived: https://web.archive.org/web/20260312123042/https://github.com/Fri3dCamp/badge
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts (chip, features, maker names, event, distribution as a free attendee badge, ~650 units) confirmed via the maker's own Hackaday.io project page. Price was never advertised (badge was given away, not sold), so get_one.price is left empty. Could not access the archived Fri3d wiki page (web.archive.org fetch blocked in this environment) to cross-check. EDA tool used was not stated on any source checked.
last_modified_date: '2026-09-07'
model:
  file: assets/models/fri3d-2018/fri3d-2018-ph0xx-badge-2.glb
  method: kicad
  source_file: fri3d-badge-2018.brd
  generated: '2026-09-07'
  bytes: 155540
---

Ph0xx is the attendee badge Fri3d Camp handed to roughly 600 people at its 2018 family-friendly hacker camp in Belgium, with about 650 boards manufactured (initial units built by hand, the rest run through pick-and-place and reflow at the More-at-Mere facility). Designed by Wim Van Gool and Bert Outtier for Fri3d Camp, the badge is cut into a fox-like silhouette with pointed "ear" wingtips, styled in white, gold, yellow, and orange. It's built around an ESP32-WROOM-32 module, so it has Wi-Fi and Bluetooth on top of two 5x7 LED matrices (used as blinking "eyes"), an ADXL345 accelerometer for motion sensing, a KLJ-1230 buzzer, two buttons and two capacitive touch pads, and an 18650 Li-ion cell with a TP4056 charger and DW01-P protection circuit.

Beyond the core badge, Ph0xx has Lego Technic-compatible mounting holes and a pair of expansion headers on its ear tips for "Jewel" add-on boards — an Air Jewel (dust and GPS sensing) and a Bot Jewel (servo control) were built for it. Both the hardware design files and the Arduino library that drives the badge's peripherals are published on GitHub, making it a fully open-source build.
