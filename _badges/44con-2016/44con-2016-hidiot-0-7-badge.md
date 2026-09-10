---
title: 44CON 2016 HIDIOT 0.7 Badge
id: 44con-2016-44con-2016-hidiot-0-7-badge
layout: badge
parent: 44CON 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: 44con-2016
year: 2016
makers:
- name: Raw Hex
  url: https://github.com/rawhex
summary: The official 44CON 2016 badge, a build-it-yourself USB HID toolkit board handed to attendees and soldered together in an on-site workshop.
functions: 'Acts as a Digispark-compatible USB HID device: programmed through the Arduino IDE to emulate keyboards/mice and run USB HID payload experiments (keystroke injection, automation demos).'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - security
  - learn to solder
tech:
  mcu: Digispark-compatible AVR (ATtiny85 architecture, via the Digistump/Trinket Arduino core)
  leds:
    count: 1
    type: discrete
    note: single user-programmable LED on pin PB1
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: about 500 boards distributed; fewer than 150 fully assembled via the on-site soldering workshop
  availability: free
  distribution:
  - free_drop
  - kit
  where: Given to 44CON 2016 attendees; unsoldered/partially-soldered boards were built at an on-site badge soldering workshop.
make_your_own:
  open_source: true
  hardware_url: https://github.com/rawhex/hidiot_hardware
  firmware_url: https://github.com/rawhex/hidiot
  eda_tool: Eagle
  license: GPL-3.0
links:
- label: badge.gallery/badges/44con-2016-hidiot-0-7-badge
  url: https://badge.gallery/badges/44con-2016-hidiot-0-7-badge
  kind: website
- label: Getting Started With Your HIDIOT Badge (44CON blog)
  url: https://44con.com/2016/09/19/getting-started-with-your-hidiot-badge/
  kind: article
- label: rawhex/hidiot_hardware (schematics/board, Eagle)
  url: https://github.com/rawhex/hidiot_hardware
  kind: repo
- label: rawhex/hidiot (Arduino software stack)
  url: https://github.com/rawhex/hidiot
  kind: repo
images: []
contact: {}
notes:
- Official 44CON 2016 badge, an unreleased HIDIOT 0.7 USB HID toolkit board built and programmed via Arduino IDE, given to attendees. Found by the event-year sweep, task con-44con.
- The discovery sweep listed the maker as "HIDIOT" - that is the project/product name; the team behind it is Raw Hex (44CON's own blog post and the hidiot_hardware/hidiot GitHub repos are published under the rawhex org).
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/44con-2016-hidiot-0-7-badge
  title: 44CON 2016 HIDIOT 0.7 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-44con); event read as ''44CON 2016''.'
- kind: url
  url: https://44con.com/2016/09/19/getting-started-with-your-hidiot-badge/
  title: Getting Started With Your HIDIOT Badge
  accessed: '2026-09-08'
  note: Maker's own (44CON) blog post confirming ~500 boards distributed, <150 fully assembled at the soldering workshop, Digispark-compatible programming via Arduino IDE, and HID payload/keystroke-injection use.
- kind: url
  url: https://github.com/rawhex/hidiot_hardware
  title: 'rawhex/hidiot_hardware: Schematics etc. for HIDIOT Hardware'
  accessed: '2026-09-08'
  note: Confirms Raw Hex as the maker org, GPL-licensed Eagle schematics/board files, and Digispark/Trinket (ATtiny85-family) compatibility; repo currently only hosts 1.0-revision files, not 0.7.
- kind: url
  url: https://github.com/rawhex/hidiot
  title: 'rawhex/hidiot: HID I/O Toolkit software stack for arduino integration'
  accessed: '2026-09-08'
  note: Firmware/software stack repo, same rawhex org.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, event, function, distribution numbers, open-source status) confirmed on 44CON''s own blog and the rawhex GitHub org. No confirmed photo of the 0.7 revision specifically could be found: badge.gallery notes none has been cleared, and the hidiot_hardware repo only contains board files/renders for the later 1.0 revision, so no image was saved to avoid misrepresenting this entry with the wrong hardware revision. Exact chip part number (ATtiny85) is inferred from the maker''s statement that the board is Digispark/Trinket-compatible (both of which are ATtiny85-based platforms) rather than stated verbatim for this board; flagged here for transparency. PCB color/shape and precise price (it was free/included with entry) are not documented beyond "free".'
last_modified_date: '2026-09-10'
model:
  file: assets/models/44con-2016/44con-2016-hidiot-0-7-badge.glb
  method: kicad
  source_file: hidiot_1.0_final.brd
  generated: '2026-09-10'
  bytes: 191596
---

The 44CON 2016 badge was not a finished gadget but a kit: the HIDIOT (Human Interface Device Input/Output Toolkit) 0.7, a small Digispark-compatible USB board designed by Raw Hex for experimenting with USB HID devices. Around 500 boards went out to attendees, and 44CON ran an on-site soldering workshop where fewer than 150 were actually finished into working units that year - the rest went home as unassembled kits.

Once built, a HIDIOT could be flashed from the Arduino IDE (via the Digistump/Micronucleus bootloader) to act as a USB keyboard or mouse, making it a hands-on platform for HID payload experiments such as keystroke injection and input-device automation. It carried a single user-programmable LED and no display; all of its capability came from the USB HID stack running on its Digispark-compatible microcontroller.

Raw Hex published both the hardware (Eagle schematics and board files) and the accompanying Arduino software stack on GitHub under GPL-3.0, and continued developing the platform into a HIDIOT 1.0 revision that appeared as the 44CON 2017 badge. No verified photograph of the specific 0.7 hardware revision handed out in 2016 has surfaced; the GitHub hardware repo currently only documents the later 1.0 board.

## Make your own

- Get the schematics and Eagle board files from [rawhex/hidiot_hardware](https://github.com/rawhex/hidiot_hardware) (note: currently the 1.0 revision, not 0.7).
- Get the companion Arduino software stack from [rawhex/hidiot](https://github.com/rawhex/hidiot).
- Program it through the Arduino IDE configured for Digispark/Trinket boards, using the Digistump Micronucleus bootloader.
