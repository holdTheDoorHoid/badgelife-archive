---
title: H2HC 2018 Badge
id: h2hc-2018-h2hc-2018-badge
layout: badge
parent: H2HC 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: h2hc-2018
year: 2018
makers:
- name: security-bits.de (Brian)
  url: https://security-bits.de/
summary: A small-batch, bottle-shaped PCB badge made for H2HC 2018 in São Paulo, with ENIG gold-plated contacts, an ESP32 WROOM brain, an OLED display, six controllable LEDs, and BLE control from a custom Android app.
functions: 'Six GPIO-driven LEDs and a 0.96" OLED display, controllable over BLE from a companion Android app built in Thunkable; otherwise a general-purpose ESP32 dev platform for attendees.'
look:
  colors:
  - black
  - gold
  shape: bottle
  themes:
  - security
  - hardware tool
tech:
  mcu: ESP32 WROOM
  leds:
    count: 6
    type: discrete
    note: Six LEDs wired to GPIO pins, individually controllable.
  display: 0.96" I2C OLED
  connectivity:
  - wifi
  - ble
  - i2c
  battery: 3x AAA or USB power
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
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'The maker''s page discusses the Arduino IDE / ESP32 toolchain and a Thunkable BLE control app, and covers the ENIG PCB finish and component choices in prose, but does not link a public repo, Gerbers, or firmware download on the page as fetched.'
links:
- label: security-bits.de/electronics/badges/h2hc_18
  url: https://security-bits.de/electronics/badges/h2hc_18/
  kind: website
images:
- file: assets/images/badges/h2hc-2018/h2hc-2018-badge/b541b8b034.jpg
  source: "https://security-bits.de/electronics/badges/h2hc_18/"
  credit: "security-bits.de (Brian)"
  caption: "Front of the H2HC 2018 badge, bottle-shaped PCB with ENIG gold contacts"
- file: assets/images/badges/h2hc-2018/h2hc-2018-badge/9355d10a25.jpg
  source: "https://security-bits.de/electronics/badges/h2hc_18/"
  credit: "security-bits.de (Brian)"
  caption: "Back of the H2HC 2018 badge showing ESP32 WROOM module"
contact: {}
notes:
- Small-batch gold-plated (ENIG) bottle-shaped PCB badge with ESP32 WROOM, OLED display, six LEDs and BLE, made for H2HC 2018. Found by the event-year sweep, task con-ekoparty.
status: listed
sources:
- kind: url
  url: https://security-bits.de/electronics/badges/h2hc_18/
  title: H2HC 2018 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-ekoparty); event read as ''H2HC 2018''.'
- kind: url
  url: https://security-bits.de/electronics/badges/h2hc_18/
  title: H2HC 2018 Badge - security-bits.de
  accessed: '2026-09-08'
  note: 'Maker''s own project page: confirmed bottle-shaped ENIG-gold PCB, ESP32 WROOM, 0.96" I2C OLED, six GPIO LEDs, BLE via Thunkable Android app, AAA/USB power, Arduino IDE toolchain; provided front/back photos.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts confirmed on the maker''s own page (security-bits.de), which is authoritative but does not state price, quantity made, availability/distribution method, or link a public repo/Gerbers/firmware download. A third-party badge index (badge.gallery) independently corroborates the same specs, so confidence is medium rather than low, but get_one and make_your_own fields are left empty/partial since the source itself does not say.'
last_modified_date: '2026-09-08'
---

The H2HC 2018 Badge is a small-batch, bottle-shaped PCB badge made by Brian of security-bits.de for H2HC (Hackers 2 Hackers Conference) 2018 in São Paulo, Brazil. Its defining visual feature is an ENIG (Electroless Nickel Immersion Gold) finish on the contacts, giving the badge real gold-plated pads that stand out against the black PCB.

Electronically, the badge is built around an Espressif ESP32 WROOM module, giving it WiFi and Bluetooth LE. It carries a 0.96" I2C OLED display and six LEDs wired to GPIO pins for simple lighting effects, and can be controlled wirelessly over BLE using a companion Android app the maker built with Thunkable. It runs on either three AAA batteries or USB power, and can be reprogrammed through the Arduino IDE with the ESP32 board extensions (a USB-to-serial adapter is needed to flash it). The maker's write-up notes that attendees found the BLE functionality to be a notable drain on battery life when left running continuously.

The maker's page does not state the price, exact production quantity, or how the badge was distributed at the conference, and does not link a public hardware or firmware repository, so those fields are left blank rather than guessed.
