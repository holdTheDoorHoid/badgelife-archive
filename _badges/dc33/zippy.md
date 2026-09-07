---
title: Zippy
id: dc33-zippy
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: DCZia
  url: https://github.com/dczia
summary: A wearable badge shaped and colored like a classic Zip disk, with a 6x7 NeoPixel matrix that shines through a translucent shell in sound- and motion-reactive light shows.
functions: A four-way joystick cycles between modes and adjusts brightness; modes include a rainbow display, an accelerometer-reactive mode that shifts color with tilt, and a microphone-driven sound-reactive "party mode."
look:
  colors:
  - clear
  - multicolor
  shape: rectangle
  themes:
  - retro computer
  - wearable
tech:
  mcu: RP2040
  leds:
    count: 42
    type: WS2812B
    note: Described by the maker as "NeoPixels," arranged in a 6x7 matrix behind the translucent shell.
  display: none
  connectivity:
  - usb
  inputs:
  - joystick
  - accelerometer
  - microphone
  power: USB-C or 3x AAA batteries (included)
  battery: 3x AAA
  sao_version: null
  sao_ports: 1
get_one:
  price: '80'
  price_usd: 80.0
  quantity: ''
  availability: limited
  availability_note: Tindie listing showed "Only 8 units remaining in stock" as of 2026-09-06.
  distribution:
  - purchase
  where: Tindie storefront (snurkle engineering)
make_your_own:
  open_source: true
  hardware_url: https://github.com/dczia/zippy-badge
  firmware_url: https://github.com/dczia/zippy-badge
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: Repo has Hardware, Software (CircuitPython), and Shells (3D-printable case) folders. No LICENSE file found.
links:
- label: www.tindie.com/products/hamster/2025-dczia-badge-zippy
  url: https://www.tindie.com/products/hamster/2025-dczia-badge-zippy/
  kind: store
- label: github.com/dczia/zippy-badge
  url: https://github.com/dczia/zippy-badge
  kind: repo
- label: Source files (GitHub)
  url: https://github.com/hamster/zippy-badge
  kind: hardware
images:
- file: assets/images/badges/dc33/zippy/8a5c3f4dee.jpg
  source: https://www.tindie.com/products/hamster/2025-dczia-badge-zippy/
  credit: snurkle engineering
  caption: The Zippy badge glowing through its translucent Zip-disk-style shell
contact: {}
notes: []
status: released
sources:
- kind: sheet
  event: dc33
  row: 48
  updated: 7/28/2025
- kind: url
  url: https://www.tindie.com/products/hamster/2025-dczia-badge-zippy/
  title: 2025 DCZia Badge - Zippy from snurkle engineering on Tindie
  accessed: '2026-09-06'
  note: Maker's storefront listing; price, specs, contents, sound/motion-reactive modes, translucent shell, stock count.
- kind: url
  url: https://github.com/dczia/zippy-badge
  title: GitHub - dczia/zippy-badge
  accessed: '2026-09-06'
  note: Confirms open-source hardware and CircuitPython firmware repo with Hardware/Software/Shells folders; no license file found.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Sold by "snurkle engineering" on Tindie under the DCZia name; unclear whether this is a solo maker or a Tindie storefront for the DCZia team, so kept the sheet's maker attribution (DCZia). SAO header version, exact quantity made, and EDA tool/license were not stated in any source found. Merged with duplicate entry 'Zippy Badge' (dc33-dczia-zippy-badge).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc33/dczia-zippy-badge/
model:
  file: assets/models/dc33/zippy.glb
  method: kicad
  source_file: Hardware/final/zippy-badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 404400
---

Zippy is DCZia's 2025 DEF CON badge (DEF CON 33), styled after a classic Iomega Zip disk. Each unit has a randomly colored translucent plastic shell over the PCB, so the 42-NeoPixel, 6x7 LED matrix inside shows through as a diffuse glow rather than bare LEDs. A Raspberry Pi RP2040 running CircuitPython drives the display, reading a built-in digital microphone and 3-axis accelerometer to switch between a rainbow mode, a tilt-reactive color mode, and a sound-reactive "party mode," all selected and adjusted with a four-way joystick.

The badge ships fully assembled except for an optional SAO header and battery box that the owner solders on themselves; it can run on USB-C power or three included AAA batteries, and has a microSD slot for expansion. It sold for $80 through DCZia's Tindie storefront (run under the name "snurkle engineering"), with a small remaining stock as of this writing. Both the hardware and the CircuitPython firmware are published on GitHub, continuing DCZia's yearly tradition of open-source DEF CON badges (their 2018 keyboard badge, 2022 "30-in-One," and 2024/2025 lines among them).

## Make your own

Hardware and firmware live in the [zippy-badge](https://github.com/dczia/zippy-badge) repository, split into `Hardware` (board design files), `Software` (CircuitPython code and libraries), and `Shells` (3D-printable case files for the translucent housing). To reflash a unit, connect it over USB-C so it mounts as a `CIRCUITPY` drive, then copy the contents of the `Software` folder onto it.

## Notes merged from the duplicate entry "Zippy Badge"

Zippy is DCZia's badge for DEF CON 33 (2025), styled after a classic Zip disk with a translucent plastic shell over the PCB. A Raspberry Pi RP2040 running CircuitPython drives a 42-LED NeoPixel matrix visible through the shell, with a four-way joystick for cycling between a rainbow mode, an accelerometer-reactive tilt mode, and a microphone-driven sound-reactive "party mode." It runs on USB-C power or an AA battery pack, and the case is held together with four M2x4 screws; the maker also publishes custom 3D-printable shell designs.

Hardware and firmware are open source on GitHub, continuing DCZia's series of DEF CON badges. This entry duplicates the archive's `dc33-zippy` entry, which was researched from DCZia's Tindie storefront ("snurkle engineering") and carries pricing ($80) and stock details not confirmed from the GitHub repo alone.

## Make your own

Hardware and firmware live in the [zippy-badge](https://github.com/dczia/zippy-badge) repository, with Hardware, Software (CircuitPython), and Shells (3D-printable case) folders. Connect the badge over USB-C so it mounts as a CircuitPython drive, then copy the firmware onto it to reflash.
