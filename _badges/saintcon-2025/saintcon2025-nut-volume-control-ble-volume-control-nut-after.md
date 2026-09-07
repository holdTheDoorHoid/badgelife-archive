---
title: Saintcon 2025 Nut Volume Control (BLE Volume Control Nut, AfterCon side project)
id: saintcon-2025-saintcon2025-nut-volume-control-ble-volume-control-nut-after
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: saintcon-2025
year: 2025
makers:
- name: compukidmike
  url: https://github.com/compukidmike
summary: 'A firmware remix that turns a leftover SAINTCON 2025 "Nut" game token into a BLE media remote: turning it sends volume up/down, pressing it sends play/pause.'
functions: 'Rotary turn sends BLE HID volume-up/volume-down key events; pressing the knob sends play/pause. Six NeoPixels chase to show the last action, one LED lighting per detent turned and all six flashing yellow on a button press.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: ESP32-C3
  leds:
    count: 6
    type: NeoPixel (WS2812-family)
    note: LOLIN C3 Mini dev board driving 6 addressable pixels via the Adafruit_NeoPixel library.
  display: none
  connectivity:
  - ble
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
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/compukidmike/Saintcon2025/tree/main/Firmware/AfterCon/Saintcon2025NutVolumeControl
  eda_tool: null
links:
- label: github.com/compukidmike/Saintcon2025/tree/main/Firmware/AfterCon/Saintcon2025NutVolumeControl
  url: https://github.com/compukidmike/Saintcon2025/tree/main/Firmware/AfterCon/Saintcon2025NutVolumeControl
  kind: repo
- label: compukidmike/Saintcon2025 (main badge repo, README)
  url: https://github.com/compukidmike/Saintcon2025
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/Saintcon2025/tree/main/Firmware/AfterCon/Saintcon2025NutVolumeControl
  title: Saintcon2025 Nut Volume Control (BLE volume-control Nut, AfterCon side project in the same repo)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''saintcon-2025''.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2025/main/Firmware/AfterCon/Saintcon2025NutVolumeControl/Saintcon2025NutVolumeControl.ino
  title: Saintcon2025NutVolumeControl.ino (source)
  accessed: '2026-09-07'
  note: 'Confirms MCU (ESP32-C3 on a LOLIN C3 Mini board), rotary-encoder + button pin wiring, 6 NeoPixels, and the BLE HID volume/play-pause behavior. Device advertises as "SC25Nut", manufacturer string "MK Factor".'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2025/main/README.md
  title: compukidmike/Saintcon2025 README
  accessed: '2026-09-07'
  note: 'Explains what a "Nut" is in this repo: the official SC25 badge (a giant wrench with an embedded NFC tag) was paired with NFC "Nut" tokens used to write one-time codes for the badge game. This volume-control project is a separate AfterCon firmware remix of that Nut hardware, not the game device itself.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The repo is the maker''s own (compukidmike / MK Factor, Michael Whiteley), so the firmware details are first-hand, but no photo of the reflashed Nut was found, and there is no separate hardware/PCB description for this AfterCon build (it reuses the existing Nut PCB from the main badge game, whose board files live in the repo''s Firmware/nut and Hardware folders but were not confirmed to be electrically identical to this side project''s target). No price, quantity, or distribution info exists because this was a personal post-con firmware hack, not a distributed item, hence get_one and status are left thin. Type is a judgment call: this is a repurposed accessory that pairs with a phone/PC over BLE, not a wearable badge or SAO.'
last_modified_date: '2026-09-07'
---

At SAINTCON 2025 the official badge was an oversized wrench with an embedded NFC tag, used together with small NFC "Nut" tokens that players turned in to unlock badge-game codes. After the con, maker compukidmike (Michael Whiteley of MK Factor) reflashed one of these Nut boards — an ESP32-C3 on a LOLIN C3 Mini — with new firmware that turns it into a Bluetooth LE media remote instead of a game token.

The rewritten firmware watches a rotary encoder's two quadrature pins and a push-button: rotating the knob sends BLE HID volume-up or volume-down key presses (one direction per pin, using interrupt handlers), and pressing the button sends play/pause. Six NeoPixel LEDs give visual feedback, lighting one pixel further around the ring per detent turned and flashing all six yellow on a button press, then fading out after about half a second of inactivity. The device advertises over BLE as "SC25Nut" with manufacturer string "MK Factor", using a modified fork of the ESP32-BLE-Keyboard library (T-vK/ESP32-BLE-Keyboard) bundled directly in the sketch.

This is a firmware-only side project built on top of existing SAINTCON 2025 game hardware rather than a standalone released product — no separate PCB, price, or distribution info was published for it. The code is open on GitHub under the same repo as the official SC25 badge and Nut game hardware.

## Make your own

The firmware (`Saintcon2025NutVolumeControl.ino`, plus a bundled `BleKeyboard.cpp/.h`) is published at the link above. Per the source comments, it targets the Arduino IDE with the `esp32` board package by Espressif Systems (v3.2.0 was used), board selection "LOLIN C3 Mini", and the Adafruit NeoPixel library (v1.12.5 was used). It requires a Nut board (or equivalent ESP32-C3 hardware wired the same way: rotary encoder on pins 0/1, button on pin 21, 6 NeoPixels on pin 10) — no separate schematic or BOM for this specific build was found in the repo.
