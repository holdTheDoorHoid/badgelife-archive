---
title: QT - SAO
id: supercon-2024-qt-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: JonKangas
  url: https://hackaday.io/jonkangas
summary: A passive adapter that lets Adafruit QT Stemma I2C modules plug into a badge's SAO 1.69bis header.
functions: Bridges the QT Stemma I2C connector to the SAO 1.69bis pinout, with a header that lets the builder swap the data and clock lines to match whichever QT device is attached, since Adafruit's QT modules don't all share the exact same pin order.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: v1.69bis
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
- label: hackaday.io/project/198455-qt-sao
  url: https://hackaday.io/project/198455-qt-sao
  kind: hackaday
images:
- file: assets/images/badges/supercon-2024/qt-sao/3a327a719b.png
  source: "https://hackaday.io/project/198455-qt-sao"
  credit: "JonKangas"
  caption: "QT-SAO adapter board"
- file: assets/images/badges/supercon-2024/qt-sao/c574704d24.jpg
  source: "https://hackaday.io/project/198455-qt-sao"
  credit: "JonKangas"
  caption: "QT-SAO perfboard prototype"
contact: {}
notes:
- An SAO adapter that converts the 1.69bis SAO pinout to the Adafruit QT Stemma I2C connector standard, submitted to the Supercon 8 SAO Contest. Found by the event-year sweep, task supercon-2024.
- Sweep title "QT - SAO" matches the maker's own project title on Hackaday.io.
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/198455-qt-sao
  title: QT - SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2024); event read as ''supercon-2024''.'
- kind: url
  url: https://hackaday.io/project/198455-qt-sao
  title: QT - SAO
  accessed: '2026-09-08'
  note: Confirmed maker, contest, function, pinout adapter design, and pulled prototype photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: No storefront, repo, gerbers, or BOM found for this entry as of the check date, so make_your_own, get_one, and price fields are left empty. This is a one-off proof-of-concept contest entry (deadbug/perfboard build), not a manufactured product, so it may never have design files published. No MCU, LEDs, or display are used since it is a passive signal-routing adapter.
last_modified_date: '2026-09-08'
---

The QT-SAO is a small passive adapter built by JonKangas for the Supercon 8 SAO Contest in 2024. It solves a specific compatibility problem: Adafruit's line of QT Stemma I2C breakout modules mostly share a common connector and wiring, but their pin orders don't quite line up with each other or with the SAO 1.69bis header found on badges. The adapter bridges the two standards so a builder can plug a QT Stemma device into a badge's SAO port.

Because the QT modules aren't fully consistent among themselves, the design includes a header arrangement that lets the builder manually swap the data and clock lines to match whichever specific QT device is being connected. The project was built and shown as a proof of concept on perfboard with hand soldering and jumper wires rather than as a finished PCB product, and it draws inspiration from davedarko's Schedule SAO design.

As a passive routing adapter, it has no microcontroller, LEDs, or display of its own — it relies entirely on the host badge and whatever QT module is attached. No storefront, repository, or bill of materials was found, consistent with this being a contest demo rather than a released product.
