---
title: SPIvSPI Whitehat Spy SAO
id: dc27-spivspi-whitehat-spy-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: SPIvSPI (xres0nance, steve/corelit)
  url: https://github.com/SPIvSPI
summary: Spy vs. Spy themed Shitty Add-On for DEF CON 27 in the white-hat spy design, the counterpart to the Blackhat Spy, using the same EFM8BB10 (8051-core) microcontroller and GUI-generated LED animations; the repo holds its dedicated PCB design (SPIvSPI_SAO_White), schematic, kit assembly notes, firmware and build photos.
functions: 'Blinks a small set of LED accents on the white-hat spy artwork (eyes, laptop screen glyph, keyboard) driven by custom firmware and a GUI-built animation sequence.'
look:
  colors:
  - white
  shape: spy character
  themes:
  - security
  - pop culture
  - spy vs spy
tech:
  mcu: EFM8BB10F8G-A (Silicon Labs EFM8BB10, 8051 core)
  leds:
    count: null
    type: reverse-mount
    note: Lights the eyes, a terminal-prompt glyph, and a keyboard highlight on the character artwork; exact LED count not stated by the maker.
  display: none
  connectivity: []
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
  hardware_url: https://github.com/SPIvSPI/dc27sao/tree/master/hardware
  firmware_url: https://github.com/SPIvSPI/dc27sao/tree/master/firmware
  eda_tool: null
  license: MIT
  notes: Repo also includes a custom GUI tool (by steve/corelit) for generating the LED animation sequences, plus PDF schematics and kit-assembly notes for both the white and black variants.
links:
- label: github.com/SPIvSPI/dc27sao
  url: https://github.com/SPIvSPI/dc27sao
  kind: repo
- label: hackaday.io/project/166811-spivspi-sao-dc27-badge
  url: https://hackaday.io/project/166811-spivspi-sao-dc27-badge
  kind: hackaday
  archived: https://web.archive.org/web/20251217031138/https://hackaday.io/project/166811-spivspi-sao-dc27-badge
- label: twitter.com/SPIvSPI
  url: https://twitter.com/SPIvSPI
  kind: social
images:
  - file: assets/images/badges/dc27/spivspi-whitehat-spy-sao/2c78b60a27.jpg
    source: "https://github.com/SPIvSPI/dc27sao"
    credit: "SPIvSPI (xres0nance)"
    caption: "The white-hat spy SAO, LEDs lit (eyes, terminal glyph, keyboard)"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/SPIvSPI/dc27sao
  title: SPIvSPI/dc27sao — Blackhat spy & Whitehat spy SAO from Def Con 27
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/SPIvSPI/dc27sao
  title: SPIvSPI/dc27sao README and repo contents
  accessed: '2026-09-07'
  note: "Confirmed makers (xres0nance hardware/firmware, steve/corelit GUI tool), MCU (EFM8BB10F8G-A, 8051 core), MIT license, repo layout (firmware/gui/hardware/img), and found the whitehat SAO photo (img/spivspi-whitehat.jpg)."
- kind: url
  url: https://hackaday.io/project/166811-spivspi-sao-dc27-badge
  title: SPIvSPI SAO DC27 Badge | Hackaday.io
  accessed: '2026-09-07'
  note: "Confirmed event/year (DEF CON 27, 2019), MCU, and project timeline (started June 14 2019, design files released Aug 15 2019); page does not separately describe the whitehat vs blackhat variants."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Maker's GitHub repo and Hackaday page confirm the badge's origin, chip, and open-source
    status, but neither states a price, quantity made, or sale/giveaway channel, so get_one
    fields are left unknown. Exact LED count and PCB EDA tool are not stated in the sources
    read; described qualitatively from the maker's own photo instead. The companion
    "SPIvSPI Blackhat Spy SAO" from the same repo has not been given its own archive entry
    (see other_items_found).
last_modified_date: '2026-09-07'
---

The SPIvSPI Whitehat Spy SAO is one half of a pair of Spy vs. Spy-themed Shitty Add-Ons that xres0nance and steve/corelit built for DEF CON 27 (2019), the other being the Blackhat Spy SAO. The name is a play on the SPIdriver USB-to-SPI tool the pair used, reimagined as the classic MAD magazine spy characters. Both SAOs run on a Silicon Labs EFM8BB10F8G-A (8051-core) microcontroller and light a handful of LEDs worked into the character artwork itself: on the white-hat version these pick out the eyes, a green terminal-prompt glyph on a laptop screen, and an amber keyboard highlight, per the maker's own photo. steve/corelit built a dedicated GUI tool so the pair could design the LED animation sequences without hand-coding timing tables.

The project went from a pencil sketch on June 14, 2019 to finished hardware and design files published on GitHub by August 15, 2019 — about six weeks, described by the maker as "Rush. Job. Insanity." The repository (SPIvSPI/dc27sao) is released under the MIT license and includes firmware, the GUI animation tool, schematics and kit-assembly PDFs, and build photos for both the white and black variants, but does not state how many were made, what they sold for, or how they were distributed at the con.

## Make your own

The hardware and firmware are both openly published under MIT:
- Hardware (schematics, PCB files, kit notes): https://github.com/SPIvSPI/dc27sao/tree/master/hardware
- Firmware: https://github.com/SPIvSPI/dc27sao/tree/master/firmware
- LED animation GUI tool: https://github.com/SPIvSPI/dc27sao/tree/master/gui

