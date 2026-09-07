---
title: Switch Ornament Reference
id: other-switch-ornament-reference
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 0
makers:
- name: scottbez1
summary: 'A tiny, ornament-sized replica of a Nintendo Switch with a working screen that plays animated GIFs, built as a Christmas tree decoration rather than a conference badge or SAO.'
functions: 'Plays animated GIFs from an SD card on a small TFT screen; settings (wifi, time zone, debug logging) are read from a config.json file on the SD card; firmware can be updated by dropping a firmware.bin on the SD card or over wifi via ArduinoOTA from a hidden credits screen.'
look:
  colors: []
  shape: null
  themes:
  - holiday
  - pop culture
  - console
tech:
  mcu: ESP32 (esp32doit-devkit-v1)
  leds: null
  display: '1.14" ST7789 TFT LCD (135x240)'
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/scottbez1/SwitchOrnamentReference/blob/master/schematic.pdf
  firmware_url: https://github.com/scottbez1/SwitchOrnamentReference
  eda_tool: null
links:
- label: github.com/scottbez1/SwitchOrnamentReference
  url: https://github.com/scottbez1/SwitchOrnamentReference
  kind: repo
- label: 'TINY Nintendo Switch Christmas Ornament (YouTube)'
  url: https://www.youtube.com/watch?v=zJxyTgLjIB8
  kind: video
images:
- file: assets/images/badges/other/switch-ornament-reference/c0fb569e5b.jpg
  source: "https://github.com/scottbez1/SwitchOrnamentReference"
  credit: "scottbez1"
  caption: "YouTube thumbnail showing the tiny Nintendo Switch-shaped ornament with a working screen"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: not_an_item
sources:
- kind: url
  url: https://github.com/scottbez1/SwitchOrnamentReference
  title: Switch Ornament Reference
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/scottbez1/SwitchOrnamentReference/master/README.md
  title: 'SwitchOrnamentReference README'
  accessed: '2026-09-07'
  note: 'Confirms it is a homemade Nintendo Switch Christmas ornament with a screen that plays GIFs; SD card config; OTA updates.'
- kind: url
  url: https://raw.githubusercontent.com/scottbez1/SwitchOrnamentReference/master/platformio.ini
  title: 'SwitchOrnamentReference platformio.ini'
  accessed: '2026-09-07'
  note: 'Gives MCU (ESP32 esp32doit-devkit-v1) and display driver/config (ST7789, 135x240).'
- kind: url
  url: https://www.youtube.com/watch?v=zJxyTgLjIB8
  title: 'TINY Nintendo Switch Christmas Ornament (Working Screen!)'
  accessed: '2026-09-07'
  note: 'Maker''s demo video; thumbnail used as the entry photo, confirms it is a Christmas tree ornament, not a badge/SAO.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This is scottbez1''s open-source reference code/schematic for a homemade Nintendo Switch-shaped Christmas tree ornament with a tiny working screen (plays GIFs from SD card). It has no connection to any hacker conference, is not an SAO (no SAO header, not designed to plug into a badge), was never sold or distributed (no price/quantity/availability), and was not made for any specific event or year. It does not belong in a badge/SAO archive; marking status: not_an_item rather than deleting so the sweep source is on record. If the archive later adds a category for non-con hobby electronics, this could be revisited.'
last_modified_date: '2026-09-07'
---

This is not a conference badge or SAO. It's [scottbez1](https://github.com/scottbez1)'s open-source reference design for a homemade Christmas tree ornament shaped like a tiny Nintendo Switch, with a small working screen that plays animated GIFs from an SD card. The repository (`SwitchOrnamentReference`) contains the firmware (PlatformIO/Arduino, targeting an ESP32 driving a 135x240 ST7789 TFT panel via the TFT_eSPI library) and a schematic PDF, released under the Apache-2.0 license.

The device reads a `config.json` file from its SD card for settings like wifi credentials, time zone, and debug logging, and supports firmware updates either by dropping a `firmware.bin` onto the SD card or over wifi via ArduinoOTA, reachable from a hidden "credits" screen. There is no evidence it was ever sold, kitted, or distributed at any event — it appears to be a one-off holiday project that the maker shared purely as reference code, and it turned up in the archive's sweep because it was on a general "SAOs to buy" link list, not because it is actually an SAO.
