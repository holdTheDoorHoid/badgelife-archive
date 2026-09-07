---
title: AND!XOR DEFCON 24 Badge
id: dc24-andxor-defcon-24-badge
layout: badge
parent: DC24
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc24
year: 2016
makers:
- name: AND!XOR
  url: https://hackaday.io/ANDnXOR
summary: AND!XOR's first independent DEF CON badge, the Bender-shaped board for DEF CON 24 (2016), built around an STM32F103 with a 128x64 OLED, an RFM69W 433 MHz radio, eight WS2812B RGB LEDs, light and tilt sensors, and 2 MB of SPI flash, running open Arduino-compatible firmware; about 120 full badges plus 50 LED-only bling variants were hand-assembled and sold at the con.
functions: Runs 14 different LED animations, includes a command-line interface accessible over serial/USB, and supports social/gaming interaction between badges over the onboard RF link.
look:
  colors:
  - black
  - white
  shape: robot
  themes:
  - robot
  - pop culture
  - sci-fi
  - security
  - radio
tech:
  mcu: STM32F103CBT6
  leds:
    count: 8
    type: WS2812B
    note: used for eye and animation effects
  display: 0.96" 128x64 OLED (SSD1306, blue)
  connectivity:
  - sub-ghz
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: about 100 white + 20 black full badges, plus 50 LED-only "Bling" variants
  availability: sold_out
  distribution:
  - purchase
  where: Sold in person at DEF CON 24 (Paris Hotel, Las Vegas, Aug 4-7 2016); demand reportedly outstripped supply, with roughly 300 people lining up for about 70 badges at one point.
make_your_own:
  open_source: true
  hardware_url: https://github.com/ANDnXOR/ANDnXOR_DC24_Badge
  firmware_url: https://github.com/ANDnXOR/ANDnXOR_DC24_Badge
  eda_tool: KiCad
  license: Apache-2.0
links:
- label: hackaday.io/project/9064-andxor-defcon-24-badge
  url: https://hackaday.io/project/9064-andxor-defcon-24-badge
  kind: hackaday
  archived: https://web.archive.org/web/20250911173920/https://hackaday.io/project/9064-andxor-defcon-24-badge/
- label: github.com/ANDnXOR/ANDnXOR_DC24_Badge
  url: https://github.com/ANDnXOR/ANDnXOR_DC24_Badge
  kind: repo
  archived: https://web.archive.org/web/20260907111848/https://github.com/ANDnXOR/ANDnXOR_DC24_Badge
images:
- file: assets/images/badges/dc24/andxor-defcon-24-badge/079965719f.jpg
  source: https://hackaday.io/project/9064-andxor-defcon-24-badge
  credit: AND!XOR
  caption: AND!XOR DEF CON 24 badge, Bender-shaped PCB
- file: assets/images/badges/dc24/andxor-defcon-24-badge/c7c703de6a.jpg
  source: https://hackaday.io/project/9064-andxor-defcon-24-badge
  credit: AND!XOR
  caption: AND!XOR DEF CON 24 badge project photo
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/9064-andxor-defcon-24-badge
  title: AND!XOR DEFCON 24 Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20250911173920/https://hackaday.io/project/9064-andxor-defcon-24-badge/
- kind: url
  url: https://hackaday.io/project/9064-andxor-defcon-24-badge
  title: AND!XOR DEFCON 24 Badge
  accessed: '2026-09-07'
  note: Confirmed makers (Zapp, Jorge Lacoste, Andrew), MCU, LEDs, display, radio, sensors, production quantities, and sale-at-con details.
- kind: url
  url: https://github.com/ANDnXOR/ANDnXOR_DC24_Badge
  title: ANDnXOR/ANDnXOR_DC24_Badge
  accessed: '2026-09-07'
  note: Confirmed open-source hardware/firmware repo, Apache-2.0 license, DFU flashing procedure.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price paid at the con and total badge count are not stated precisely on the sources checked (hackaday.io project page and GitHub repo); production split (100 white / 20 black / 50 LED-only bling) comes from the hackaday.io page and is consistent with the sheet-derived summary's "120 full + 50 bling" figure. No open web search corroboration was possible beyond these two sources (session web-search budget was exhausted); no disagreements found between the two sources used.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc24/andxor-defcon-24-badge.glb
  method: gerber
  source_file: Gerbers
  generated: '2026-09-07'
  bytes: 205304
  size_mm:
  - 72.3
  - 99.5
---

AND!XOR's DEF CON 24 badge (2016) was the Philadelphia/California-based hacker crew's first independently produced conference badge, shaped like Bender from Futurama. Designed by Zapp, Jorge Lacoste, and Andrew, it is built around an STM32F103CBT6 microcontroller running Arduino-compatible (STM32Duino) firmware, with a 0.96" 128x64 blue OLED display, eight WS2812B RGB LEDs used for eye and animation effects, an RFM69W 433 MHz radio for badge-to-badge interaction, a light sensor, a tilt switch, and 2 MB of onboard SPI flash. The badge ran 14 different LED animations and exposed a command-line interface over serial/USB for hacking.

The team hand-assembled and sold the badges in person at DEF CON 24 (Paris Hotel, Las Vegas, August 4-7, 2016) to recoup development costs, producing roughly 100 white and 20 black full badges plus 50 LED-only "Bling" variants for people who wanted the look without the electronics. Demand exceeded supply, with reports of around 300 people lining up for about 70 badges at peak demand — a preview of the sellout crowds AND!XOR's later badges would draw.

## Make your own

Hardware (KiCad schematics and Gerbers) and firmware are published under an Apache-2.0 license in the [ANDnXOR/ANDnXOR_DC24_Badge](https://github.com/ANDnXOR/ANDnXOR_DC24_Badge) repository, organized into Gerbers, Inspiration, Provision, and Software folders. Firmware is flashed over USB via `dfu-util`, entered by holding the "Down" button while connecting; an LED near the AND!XOR DEFCON 24 silkscreen flashes rapidly to indicate DFU mode.

## History

This was the first badge in what became a recurring line of independent AND!XOR DEF CON badges, including later entries for DC25 through DC33 and beyond.
