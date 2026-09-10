---
title: LayerOne 2023 PIC HID Badge
id: layerone-2023-layerone-2023-pic-hid-badge
layout: badge
parent: LayerOne 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: layerone-2023
year: 2023
makers:
- name: charliex
  role: designer/firmware
- name: LayerOne
summary: A PIC16F1455-based USB HID keyboard badge for LayerOne 2023 with addressable LEDs and a DFU bootloader.
functions: Emulates a USB HID keyboard, typing a stored macro (default "LayerOne 2023") when its button is pressed; macros can be reprogrammed over a generic HID interface. Drives WS2812B/SK6812 addressable LED effects, and can be put into DFU mode (hold the button while plugging in USB) for firmware updates via dfu-util or a PICkit 3+. The firmware ships with a commented-out, partial RubberDucky 2.0 script interpreter that badge-competition entrants were challenged to finish for a prize.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: PIC16F1455
  leds:
    type: WS2812B/SK6812
    note: Addressable LEDs driven from the PIC's RC3 pin.
  display: null
  connectivity:
  - usb
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
  open_source: 'yes'
  hardware_url: https://github.com/charlie-x/LayerOne2023
  firmware_url: https://github.com/charlie-x/LayerOne2023
  eda_tool: null
  notes: Repo includes Eagle PCB schematics/layout, 3MF/STEP enclosure models, component datasheets, and full firmware source (built with MPLAB 6.10 + XC8 2.41). License is BSD-3-Clause per the maker's own page.
links:
- label: badge.gallery/badges/layerone-2023-pic-hid-badge
  url: https://badge.gallery/badges/layerone-2023-pic-hid-badge
  kind: website
- label: github.com/charlie-x/LayerOne2023
  url: https://github.com/charlie-x/LayerOne2023
  kind: repo
images: []
contact: {}
notes:
- 'Sweep''s wording: "Official PIC-microcontroller-based badge that functions as a USB HID device, for LayerOne 2023." Confirmed on badge.gallery, which credits the design to charliex; matches the maker''s own GitHub repo.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/layerone-2023-pic-hid-badge
  title: LayerOne 2023 PIC HID Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''LayerOne 2023''.'
- kind: url
  url: https://badge.gallery/badges/layerone-2023-pic-hid-badge
  title: LayerOne 2023 PIC HID Badge
  accessed: '2026-09-10'
  note: Confirmed the badge, credited designer (charliex), event/date (LayerOne 2023, May 27-28 2023, Hilton Pasadena), MCU, LEDs, firmware features, and RubberDucky competition detail.
- kind: url
  url: https://github.com/charlie-x/LayerOne2023
  title: charlie-x/LayerOne2023
  accessed: '2026-09-10'
  note: Maker's own repo; confirmed open-source hardware/firmware (BSD-3-Clause), Eagle PCB files, 3MF enclosure models, and toolchain (MPLAB 6.10, XC8 2.41). No badge photo found in the repo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Confirmed as a real, released badge with an open-source repo by the maker (charliex). No price, quantity made, or distribution method found in either source. No photo of the assembled badge was found (repo has no images; badge.gallery page has none either), so images list is empty.
last_modified_date: '2026-09-10'
---

The LayerOne 2023 PIC HID Badge is a small USB badge designed by charliex, a longtime LayerOne badge maker (also behind the 2014, 2015, and 2017 LayerOne badges), for the 2023 conference at the Hilton Pasadena. Built around a PIC16F1455 microcontroller, it enumerates as a USB HID keyboard and types out a stored text macro (LayerOne 2023 by default) when its button is pressed. The macro can be rewritten over a generic HID interface, and the badge also drives a run of WS2812B/SK6812 addressable LEDs for programmable lighting effects.

Firmware updates go through a built-in DFU bootloader, entered by holding the button while plugging in USB, and can be flashed with dfu-util or a PICkit 3 or later. The firmware source includes a partial, commented-out implementation of a RubberDucky 2.0 script interpreter, which was posed to attendees as a badge-hacking competition challenge with a prize for whoever completed it.

The design is fully open source, published by charliex on GitHub under a BSD-3-Clause license with Eagle schematic and board files, 3MF/STEP enclosure models, component datasheets, and the C firmware (built with Microchip MPLAB 6.10 and the XC8 2.41 compiler). No pricing, production quantity, or distribution details were found, and no photo of the assembled badge turned up in either source consulted.
