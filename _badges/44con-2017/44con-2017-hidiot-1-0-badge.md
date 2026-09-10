---
title: 44CON 2017 HIDIOT 1.0 Badge
id: 44con-2017-44con-2017-hidiot-1-0-badge
layout: badge
parent: 44CON 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: 44con-2017
year: 2017
makers:
- name: Raw Hex
  url: https://github.com/rawhex
  role: hardware/firmware (design credited to Steve Lord)
summary: A build-it-yourself USB HID exploration board handed out as the 44CON 2017 conference badge, designed by UK security firm Raw Hex around an ATtiny85 microcontroller.
functions: Programmed through the Arduino IDE in Trinket/Digispark-compatible mode to emulate USB HID devices (keyboard/mouse payloads); two buttons (S1, S2) trigger user-written payloads and one onboard LED gives status feedback. A companion "HID I/O Toolkit" software stack and tutorials support building attack/demo payloads.
look:
  colors: []
  shape: card
  themes:
  - hardware tool
  - security
  - learn to solder
tech:
  mcu: ATtiny85
  leds:
    count: 1
    type: discrete
    note: single status LED (LED1), 330-ohm current-limit resistor
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  - purchase
  where: Component kits were sold/distributed at the 44CON 2017 front desk and assembled onsite in a dedicated soldering/assembly area.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/rawhex/hidiot_hardware
  firmware_url: https://github.com/rawhex/hidiot
  eda_tool: Eagle
links:
- label: badge.gallery/badges/44con-2017-hidiot-1-0-badge
  url: https://badge.gallery/badges/44con-2017-hidiot-1-0-badge
  kind: website
- label: rawhex/hidiot_hardware (schematics, Eagle files)
  url: https://github.com/rawhex/hidiot_hardware
  kind: repo
- label: rawhex/hidiot (HID I/O Toolkit software stack)
  url: https://github.com/rawhex/hidiot
  kind: repo
- label: rawhex/hidiot-tutorials
  url: https://github.com/rawhex/hidiot-tutorials
  kind: repo
- label: Getting Started With Your HIDIOT Badge (44CON blog)
  url: https://44con.com/2016/09/19/getting-started-with-your-hidiot-badge/
  kind: article
- label: HIDIOT Community on Hackster.io
  url: https://www.hackster.io/hidiot
  kind: hackaday
images: []
contact: {}
notes:
- Official 44CON 2017 badge, a build-it-yourself Raw Hex HIDIOT 1.0 USB HID board documented in the 44CON 2017 brochure. Found by the event-year sweep, task con-44con.
- Sweep title matched the maker's own naming ("HIDIOT 1.0 Rev 1" per the Eagle schematic title block); no title change needed.
- No rights-cleared photograph of the physical assembled 44CON 2017 board was found; the hidiot_hardware repo's only linked image is a schematic drawing, not a photo, so no image was saved for this entry.
status: listed
sources:
- kind: url
  url: https://badge.gallery/badges/44con-2017-hidiot-1-0-badge
  title: 44CON 2017 HIDIOT 1.0 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-44con); event read as ''44CON 2017''.'
- kind: url
  url: https://github.com/rawhex/hidiot_hardware
  title: rawhex/hidiot_hardware
  accessed: '2026-09-08'
  note: Maker's Eagle schematic (hidiot_1.0_final.sch, dated 2017/08/10) confirms ATtiny85 MCU, one LED, two buttons, USB-only connectivity, and CC BY-SA 3.0 hardware license.
- kind: url
  url: https://44con.com/2016/09/19/getting-started-with-your-hidiot-badge/
  title: Getting Started With Your HIDIOT Badge
  accessed: '2026-09-08'
  note: Confirms Digispark/Trinket-compatible Arduino IDE programming flow and V-USB/DigiKeyboard libraries; describes the prior-year (0.7) badge that 1.0 was built to be compatible with.
- kind: url
  url: https://github.com/rawhex/hidiot
  title: rawhex/hidiot (HID I/O Toolkit)
  accessed: '2026-09-08'
  note: Confirms GPL-licensed software stack for the HIDIOT boards.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, year, MCU, USB HID function, open hardware/software) confirmed via the maker''s own GitHub repos and the 44CON blog. Not confirmed: exact price, quantity made, current availability, and board colors/exact form factor beyond "card-sized" (from a third-party review title). No photo of the assembled 44CON 2017 board was located, only the Eagle schematic.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/44con-2017/44con-2017-hidiot-1-0-badge.glb
  method: kicad
  source_file: hidiot_1.0_final.brd
  generated: '2026-09-10'
  bytes: 191592
---

The 44CON 2017 conference badge was the HIDIOT 1.0, a build-it-yourself USB Human Interface Device (HID) board designed by Raw Hex, the UK-based security research outfit run by Steve Lord. Attendees bought or received component kits at the front desk and assembled the boards themselves in a dedicated soldering area, continuing a tradition Raw Hex started with an unreleased "0.7" version of the same board at 44CON 2016.

The board is built around an ATtiny85 microcontroller wired for Digispark/Trinket-compatible programming through the Arduino IDE, using the V-USB software USB stack and the Micronucleus bootloader. It exposes two buttons and one status LED, and is meant to be programmed to emulate USB HID devices such as keyboards and mice — the same class of USB HID injection attack popularized by tools like the Rubber Ducky, but here framed as a teaching platform. Raw Hex published a companion "HID I/O Toolkit" software stack and a set of tutorials, and ran a linked project competition on Hackster.io to encourage attendees to build something with their badge after the con.

## Make your own

Raw Hex published the full Eagle CAD schematic and board files for the HIDIOT 1.0 in the `hidiot_hardware` GitHub repository (hardware licensed CC BY-SA 3.0), and the accompanying firmware/software stack in the `hidiot` and `hidiot-tutorials` repositories (GPL-licensed). Building one from scratch means fabricating the board from the Eagle files, hand-soldering an ATtiny85 in a DIP package plus the USB, LED, and button components shown on the schematic, then flashing it via the Digistump AVR board package and Micronucleus in the Arduino IDE.

## History

The HIDIOT line began as an unreleased "0.7" board handed out at 44CON 2016, explicitly designed to be forward-compatible with the 1.0 revision that became the official 44CON 2017 badge.
