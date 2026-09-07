---
title: EgDah ala HaDge
id: other-egdah-ala-hadge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2015
makers:
- name: Antti Lukats
  url: https://hackaday.io/Antti
summary: 'An open, MCU-agnostic alternative badge concept from Antti Lukats, built around stacked banana-jack/magnetic I/O connectors instead of a fixed brain chip.'
functions: 'POV (persistence of vision) display, capacitive sense pads, and a modular I/O scheme (banana jacks plus magnetic contacts) meant to let add-on boards plug in for radio (WiFi/BLE/FM), a secondary MCU (Atmel SAM/AVR), or SD storage up to 128GB.'
look:
  colors:
  - green
  - gold
  shape: rectangle
  themes:
  - hardware tool
  - radio
tech:
  mcu: none
  leds: null
  display: POV
  connectivity: []
  battery: 2x CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/7467-egdah-ala-hadge
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/7467-egdah-ala-hadge
  url: https://hackaday.io/project/7467-egdah-ala-hadge
  kind: hackaday
images:
  - file: assets/images/badges/other/egdah-ala-hadge/5db868a174.jpg
    source: "https://hackaday.io/project/7467-egdah-ala-hadge"
    credit: "Antti Lukats"
    caption: "Assembled prototype PCB, corner view showing pogo-pin/banana I/O contacts and an onboard MCU package"
  - file: assets/images/badges/other/egdah-ala-hadge/8e5b042084.jpg
    source: "https://hackaday.io/project/7467-egdah-ala-hadge"
    credit: "Antti Lukats"
    caption: "Two stacked prototype boards showing the ball-contact interboard connectors"
contact: {}
notes: []
status: unknown
sources:
- kind: url
  url: https://hackaday.io/project/7467-egdah-ala-hadge
  title: Egdah ala Hadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/7467-egdah-ala-hadge
  title: EgDah ala HaDge | Hackaday.io
  accessed: '2026-09-07'
  note: 'Project page: description, spec list (POV display, capacitive pads, UD Card Type III / CRUVI slots, magnetic and banana I/O, 2x CR2032 power, no fixed MCU, BOM target under $20), creator Antti Lukats, created 2015-08-28.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    This is a 2015 Hackaday.io project by Antti Lukats (creator of the DIPSY
    tiny-SoC project), pitched as an "Alternative Hackaday Badge: Inspired by
    DIPSY.COOL" — a riff on the official Hackaday.io "HaDge" badge project
    (hackaday.io/project/3009). It is a modular, brain-agnostic badge design:
    the spec explicitly lists "Main MCU: None," leaving the builder to add
    their own microcontroller or FPGA via the banana-jack/magnetic I/O slots.
    Prototype PCB photos exist on the project page, so at least one physical
    board was built, but there is no evidence it was manufactured in
    quantity, sold, or distributed at any specific convention — it reads as
    a design exploration/proof of concept rather than an event badge. No
    con or year of distribution is stated anywhere on the page, so `event`
    is left as `other` and `status` as `unknown`. Price, quantity, and
    availability are not stated beyond a rough sub-$20 BOM target. No
    separate firmware or hardware-files repo link was found on the project
    page itself.
last_modified_date: '2026-09-07'
---

EgDah ala HaDge is a 2015 Hackaday.io project by Antti Lukats, presented as an "Alternative Hackaday Badge" inspired by his earlier DIPSY tiny system-on-chip project and playing off the name of the official Hackaday.io community badge ("HaDge"). Rather than shipping with a fixed microcontroller, the design deliberately leaves "Main MCU: None," expecting a builder to bring their own MCU or FPGA and plug it in through a bank of banana-jack and magnetic I/O connectors, alongside UD Card Type III and CRUVI expansion slots. Listed features include a POV (persistence of vision) display mode, capacitive touch pads, and support for add-on radio modules (WiFi, BLE, FM) or SD storage up to 128GB, all targeted at a bill of materials under $20.

Photos on the project page show an assembled prototype PCB — a populated board with a QFN/TSSOP-class chip, ball-style pogo contacts along its edges, and a second board stacked beneath it via the same contacts — confirming physical hardware was built and tested. There is no indication in the available sources that it was produced in numbers, sold, or handed out at any specific convention; it appears to be a personal open-hardware exploration rather than an event badge with a confirmed release history.
