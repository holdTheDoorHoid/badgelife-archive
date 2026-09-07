---
title: SPIvSPI SAO DC27 Badge
id: dc27-spivspi-sao-dc27-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: SPIvSPI (xres0nance)
  url: https://github.com/SPIvSPI
summary: A Spy vs. Spy themed Shitty Add-On for DEF CON 27 (2019), built around a Silicon Labs EFM8BB10 8051-core microcontroller driving LED animations, produced in Blackhat spy and Whitehat spy variants from a freehand pencil-sketch design started June 14, 2019 and released with open firmware, hardware files, and a GUI animation-generator tool.
functions: LED "blinkenlites" animations driven by the onboard 8051 core; a companion GUI tool (by steve/corelit) lets users author custom LED animation patterns and load them onto the badge.
look:
  colors:
  - black
  - white
  shape: rectangle
  themes:
  - spy
  - pop culture
  - security
  - hardware tool
tech:
  mcu: EFM8BB10F8G-A (8051 core, SOIC16)
  leds:
    count: null
    type: discrete
    note: Blackhat variant uses red LEDs (silkscreened backwards per the kit notes); Whitehat variant uses green LEDs. Exact count not confirmed from available schematics.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/SPIvSPI/dc27sao/tree/master/hardware
  firmware_url: https://github.com/SPIvSPI/dc27sao/tree/master/firmware
  eda_tool: null
  license: MIT
  fab_url: null
  notes: Repo also includes a GUI LED-animation generator (/gui) and build photos (/img). Kit assembly notes (PDF) for both Blackhat and Whitehat variants are in /hardware; there is also a J2 breakout/dev-board footprint as an alternative to the SAO connector.
links:
- label: hackaday.io/project/166811-spivspi-sao-dc27-badge
  url: https://hackaday.io/project/166811-spivspi-sao-dc27-badge
  kind: hackaday
  archived: https://web.archive.org/web/20251217031138/https://hackaday.io/project/166811-spivspi-sao-dc27-badge
- label: github.com/SPIvSPI/dc27sao
  url: https://github.com/SPIvSPI/dc27sao
  kind: repo
- label: twitter.com/SPIvSPI
  url: https://twitter.com/SPIvSPI
  kind: social
images:
- file: assets/images/badges/dc27/spivspi-sao-dc27-badge/860a8af82d.jpg
  source: https://github.com/SPIvSPI/dc27sao
  credit: SPIvSPI (xres0nance)
  caption: Blackhat spy variant of the SPIvSPI SAO, assembled PCB
- file: assets/images/badges/dc27/spivspi-sao-dc27-badge/01a0a835b5.jpg
  source: https://github.com/SPIvSPI/dc27sao
  credit: SPIvSPI (xres0nance)
  caption: Whitehat spy variant of the SPIvSPI SAO, assembled PCB
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/166811-spivspi-sao-dc27-badge
  title: SPIvSPI SAO DC27 Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20251217031138/https://hackaday.io/project/166811-spivspi-sao-dc27-badge
- kind: url
  url: https://hackaday.io/project/166811-spivspi-sao-dc27-badge
  title: SPIvSPI SAO DC27 Badge (Hackaday.io project page)
  accessed: '2026-09-07'
  note: Confirmed maker, DEF CON 27 / 2019 event, EFM8BB10F8G-A 8051 MCU, June 14 2019 concept-sketch start date, and open-source release.
  archived: https://web.archive.org/web/20251217031138/https://hackaday.io/project/166811-spivspi-sao-dc27-badge
- kind: url
  url: https://github.com/SPIvSPI/dc27sao
  title: SPIvSPI/dc27sao GitHub repository
  accessed: '2026-09-07'
  note: Repo structure (firmware, gui, hardware, img), MIT license, credits (xres0nance hardware/firmware, steve/corelit GUI tool).
- kind: url
  url: https://raw.githubusercontent.com/SPIvSPI/dc27sao/master/hardware/SPIvSPI-Black-Kit-Notes.pdf
  title: SPIvSPI-Black-Kit-Notes.pdf
  accessed: '2026-09-07'
  note: 'Blackhat kit assembly instructions: red LEDs installed reversed from silkscreen, SAO connector or J2 breakout (not both).'
- kind: url
  url: https://raw.githubusercontent.com/SPIvSPI/dc27sao/master/hardware/SPIvSPI-White-Kit-Notes.pdf
  title: SPIvSPI-White-Kit-Notes.pdf
  accessed: '2026-09-07'
  note: 'Whitehat kit fabrication diagram: EFM8BB10F8G-A SOIC16, green (GRN) LEDs, same SAO/J2 breakout option.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No source states a sale price, quantity made, or current availability, so those fields are left empty/unknown. Exact LED count could not be confirmed: the fabrication-diagram PDFs list several 220/330-ohm resistor markings consistent with multiple LEDs, but the schematic PDFs render as vector paths with no extractable LED reference designators. The Hackaday.io project log/gallery could not be fetched directly (404 on the dedicated log URL); the main project page was used instead.'
last_modified_date: '2026-09-07'
---

The SPIvSPI SAO is a Spy vs. Spy themed Shitty Add-On made for DEF CON 27 in 2019 by the maker known as SPIvSPI (xres0nance). It started as a pencil sketch on June 14, 2019 and came together over about six weeks, described by its creator as a "total rush job." The badge is built around a Silicon Labs EFM8BB10F8G-A, an 8051-core microcontroller in a SOIC16 package, which drives LED "blinkenlites" animations on the board. A companion GUI tool, built by steve/corelit, lets someone generate custom LED animation patterns and load them onto the badge, alongside the maker's own firmware.

The SAO was produced in two matching variants: a black-PCB "Blackhat spy" version with red LEDs, and a white-PCB "Whitehat spy" version with green LEDs, both featuring Spy vs. Spy-style artwork. Each board can be built either as a standard SAO (plugging into a host badge's add-on header) or, alternatively, as a J2 breakout/dev board — the two options are mutually exclusive per the kit notes.

All of it was released as open source on GitHub under the MIT license: firmware, PCB schematics and kit-assembly notes (as PDFs) for both color variants, the LED animation GUI tool, and build photos documenting the fabrication process (panelizing, pick-and-place, reflow). No source found states a sale price, production quantity, or whether the SAO is still available; those fields are left blank pending further information.
