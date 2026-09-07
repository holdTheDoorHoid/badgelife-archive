---
title: DEF CON Furs Badge DC26
id: dc26-def-con-furs-badge-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: DEF CON Furs (defconfurs org)
  url: https://github.com/defconfurs
summary: An independent, fox-head-shaped electronic badge made by the DEF CON Furs community group for DEF CON 26, running MicroPython on an STM32F4 and driving a 126-pixel LED matrix.
functions: Plays scriptable LED animations (Python classes or JSON frame data) on the front matrix; two ear buttons switch modes; wakes on motion via the accelerometer and standby-sleeps when idle and off USB power; capacitive touch ("boop") detection; connects to a companion Bluetooth LE module over UART.
look:
  colors:
  - black
  - yellow
  shape: fox
  themes:
  - animal
  - mascot
  - wearable
  form_factor: pcb badge
tech:
  mcu: STM32F411RET6
  leds:
    count: 112
    type: discrete
    note: 525nm green 0603 LEDs (part 150060GS75000) arranged in an 18x7 matrix, with some corner/bridge-of-nose positions omitted to fit the fox-head outline; driven with per-pixel PWM dimming via a timer/DMA driver.
  display: LED matrix 18x8 (fox-head cutout, 112 usable pixels)
  connectivity:
  - bluetooth
  - uart
  - i2c
  - usb
  battery: 2x AA (BC12AAPC holder) or USB micro-B
  sao_version: null
make_your_own:
  open_source: yes
  hardware_url: https://github.com/defconfurs/dc26-fur-scripts
  firmware_url: https://github.com/defconfurs/micropython-dcfurs
  eda_tool: null
  license: MIT
  notes: Repo includes schematic PDF (dcfurs-schematic.pdf), a full BOM/assembly guide (ASSEMBLY.md), MicroPython firmware DFU image, and animation-scripting API docs. A separate web tool for building JSON animations was linked at dcfurs.liquidthex.com (not verified reachable at time of research).
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
links:
- label: github.com/defconfurs/dc26-fur-scripts
  url: https://github.com/defconfurs/dc26-fur-scripts
  kind: repo
- label: github.com/defconfurs/micropython-dcfurs
  url: https://github.com/defconfurs/micropython-dcfurs
  kind: repo
images:
  - file: assets/images/badges/dc26/def-con-furs-badge-dc26/7b346d1917.png
    source: "https://github.com/defconfurs/dc26-fur-scripts"
    credit: "defconfurs / oskirby"
    caption: "Front PCB render of the DC26 badge's 18x7 LED matrix, shaped like a fox head"
  - file: assets/images/badges/dc26/def-con-furs-badge-dc26/80311cb5ab.png
    source: "https://github.com/defconfurs/dc26-fur-scripts"
    credit: "defconfurs / oskirby"
    caption: "Back PCB render of the DC26 badge, fox-head shape, showing component placement and contributor handles"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/defconfurs/dc26-fur-scripts
  title: DEF CON Furs Badge DC26
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''DEF CON 26 (2018)''.'
- kind: url
  url: https://github.com/defconfurs/dc26-fur-scripts/blob/master/README.md
  title: DCFurs Badge Scripts README
  accessed: '2026-09-07'
  note: Confirms MCU (STM32F411RET6 running MicroPython), 32Mbit SPI flash, 18x7 LED matrix, two ear pushbuttons, Taiyo Yuden EYSGCNZ BLE radio, accelerometer and capacitive touch sensors, and an SAO ("shitty addon connector") header.
- kind: url
  url: https://github.com/defconfurs/dc26-fur-scripts/blob/master/ASSEMBLY.md
  title: DC26 Furs badge Assembly Guide (BOM)
  accessed: '2026-09-07'
  note: Full bill of materials confirming 112x discrete 0603 green LEDs, USB micro-B and 2xAA battery power options, boost converter, and other passives/ICs. Notes builders can substitute LED color if matching resistors accordingly.
- kind: url
  url: https://github.com/defconfurs/dc26-fur-scripts/tree/master/img
  title: DC26 badge PCB render images (repo img/ folder)
  accessed: '2026-09-07'
  note: Source of the two saved images (front LED matrix and back component/credits render); confirms fox-head PCB outline and contributor handles (@metavulp, @dranothecat, @thekayfox, foobar, @thbigtanuski, @liquidthex, loialotter).
- kind: url
  url: https://api.github.com/orgs/defconfurs/repos
  title: defconfurs GitHub org repo listing
  accessed: '2026-09-07'
  note: Used to confirm there is no separate DC26-specific hardware repo (the scripts repo is the only DC26 artifact); later years (DC27+) got dedicated dcfurs-badge-dcNN repos.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core specs confirmed directly from the maker org's own repository (README, BOM/assembly guide, schematic PDF, firmware). No price, quantity made, or distribution/availability details were found in any source (this looks like a members'-made community badge rather than a sold product, but that is not stated outright anywhere found, so get_one fields are left empty rather than guessed). SAO connector is mentioned in the README but its pinout/version is not specified, so tech.sao_version is left null. A companion Bluetooth firmware/hardware repo (micropython-dcfurs) and animation-builder web tool (dcfurs.liquidthex.com) are linked but not independently verified live. status set to released since assembled units with this firmware clearly existed and were documented in detail (schematic, BOM, firmware image) consistent with a distributed/built badge, not just a rumor.
last_modified_date: '2026-09-07'
---

The DC26 DEF CON Furs badge is a fox-head-shaped PCB badge built by the DEF CON Furs community group for DEF CON 26 (2018). It runs a MicroPython environment on an STM32F411RET6 microcontroller and drives a matrix of 112 discrete green 0603 LEDs (18 columns by 7 rows, with a few positions near the ears and nose bridge omitted to keep the fox silhouette) using a custom DMA-based driver with per-pixel PWM dimming. Two pushbuttons on the badge's ears let wearers switch between animations, an onboard accelerometer handles tap/motion wake and puts the badge into standby when idle and unplugged, and a capacitive touch controller adds a "boop the nose" interaction. A Taiyo Yuden EYSGCNZ Bluetooth LE module and an SAO-style "shitty addon connector" header round out the connectivity.

The badge can be powered over USB micro-B or from two AA batteries, and the project is fully open source under the MIT license: the GitHub repository includes a schematic PDF, a complete bill of materials and assembly guide for anyone who wants to build their own from scratch, and MicroPython firmware (with a separate `micropython-dcfurs` repo carrying the firmware source). Custom animations can be written as Python classes or supplied as JSON frame data, and a web-based JSON animation builder was linked from the project (dcfurs.liquidthex.com), though its current availability wasn't checked. The back of the board carries the credits "#badgelife @metavulp @dranothecat @thekayfox foobar" and "#defconfurs @thbigtanuski @liquidthex loialotter," along with the tongue-in-cheek warning "DC26 DEFCON FURS -- MAY HAVE FLEAS."

No price, production quantity, or distribution method (sold, given away, kit-only) turned up in the sources reviewed; this reads as a badge built by and for the DEF CON Furs group itself rather than a commercial product, but that isn't stated explicitly anywhere found, so those fields are left blank rather than assumed.

## Make your own

The `dc26-fur-scripts` repository is the full build resource: `dcfurs-schematic.pdf` for the schematic, `ASSEMBLY.md` for a complete BOM (STM32F411RET6, an AAT1217 boost converter, MMA7660 accelerometer, EYSGCNZWY BLE module, 32Mbit SPI flash, IQS231A capacitive touch controller, 112x 0603 LEDs, and passives), and a prebuilt `firmware-f411.dfu` image to flash. The LED color can be substituted for any 0603 part as long as the current-limiting resistors (R8-R25) are recalculated to match. Once flashed, badge behavior is scripted in MicroPython via `main.py`, using the `badge`, `dcfurs`, and `settings` modules documented in the repo's README, with example animations in the `animations` folder.

## History

This appears to be the earliest documented DEF CON Furs group badge in this archive; the same org went on to build dedicated hardware repos for DC27 through DC33 (`dcfurs-badge-dc27` onward), suggesting DC26 established the pattern the group repeated each following year.
