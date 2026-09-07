---
title: DOOM SAO
id: dc27-doom-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: AND!XOR / LonghornEngineer
  url: https://github.com/LonghornEngineer
summary: A DEF CON 27 SAO by AND!XOR's Parker Dillmann (LonghornEngineer) that puts a full ST7789 LCD and an Arduino-compatible MCU on a SAO header, showing an animated DOOM Guy while doubling as an I2C/serial bus-sniffing tool.
functions: 'Displays an animated DOOM Guy on its LCD (auto mode, or controlled via 2 GPIO pins for look left/right/back). Also works as a passive hardware hacking tool: an I2C bus sniffer (including SAO-specific decoding), a DOOM-Guy-only I2C sniffer, and a serial UART man-in-the-middle sniffer, plus a user-defined custom application area and EEPROM persistence.'
look:
  colors:
  - black
  shape: null
  themes:
  - horror
  - video game
  - hardware tool
tech:
  mcu: ATSAMD21G18A
  leds: null
  display: 1.3" 240x240 LCD (ST7789)
  connectivity:
  - i2c
  - uart
  - usb
  battery: powered by host badge (or USB-C)
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: shop.andnxor.com/products/doom-sao returned 404 as of 2026-09-07; Hackaday (July 2019) reported remaining stock was being sold at DEF CON's Hacker Warehouse.
  distribution:
  - purchase
  where: AND!XOR's online shop (shop.andnxor.com) and in person at DEF CON 27's Hacker Warehouse.
make_your_own:
  open_source: true
  hardware_url: https://github.com/LonghornEngineer/DOOM_SAO/tree/master/Hardware
  firmware_url: https://github.com/LonghornEngineer/DOOM_SAO
  eda_tool: null
  license: Apache License 2.0
  notes: Open-sourced August 11, 2019 (previously proprietary). Follows the AND!XOR SAO Reference Design (github.com/ANDnXOR/sao-reference-designs).
links:
- label: github.com/LonghornEngineer/DOOM_SAO
  url: https://github.com/LonghornEngineer/DOOM_SAO
  kind: repo
- label: 'Hackaday.io: DC27 DOOM SAO - Hurt Me Plenty'
  url: https://hackaday.io/project/164346-andxor-dc27-badge/log/165849-dc27-doom-sao-hurt-me-plenty
  kind: hackaday
- label: 'Hackaday: Hands-On - AND!XOR DEF CON 27 Badge Ditches Bender, Adopts Light Pipes'
  url: https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
  kind: article
- label: AND!XOR SAO Reference Design
  url: https://github.com/ANDnXOR/sao-reference-designs
  kind: repo
images:
- file: assets/images/badges/dc27/doom-sao/f14497ec22.jpg
  source: https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
  credit: Hackaday
  caption: The DOOM SAO plugged into the AND!XOR DC27 badge
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/LonghornEngineer/DOOM_SAO
  title: DOOM SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc27''.'
- kind: url
  url: https://github.com/LonghornEngineer/DOOM_SAO/blob/master/README.md
  title: DOOM_SAO README
  accessed: '2026-09-07'
  note: Full feature list, MCU/display specs, I2C EEPROM protocol, SAO v1.69bis compliance, license note.
- kind: url
  url: https://hackaday.io/project/164346-andxor-dc27-badge/log/165849-dc27-doom-sao-hurt-me-plenty
  title: DC27 DOOM SAO - Hurt Me Plenty | Hackaday.io
  accessed: '2026-09-07'
  note: Confirms maker (Cr4bf04m / LonghornEngineer / Parker Dillmann), sale through AND!XOR shop and Hacker Warehouse.
- kind: url
  url: https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
  title: 'Hands-On: AND!XOR DEF CON 27 Badge Ditches Bender, Adopts Light Pipes'
  accessed: '2026-09-07'
  note: Photo of the DOOM SAO on the badge; describes it as rev 1, Parker Dillmann's creation, with a serial sniffer.
- kind: url
  url: https://shop.andnxor.com/products/doom-sao
  title: AND!XOR shop - DOOM SAO (page no longer live)
  accessed: '2026-09-07'
  note: Returned HTTP 404; product page no longer available, consistent with sold-out status.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Price and exact quantity made were not found in any source checked. The maker byline is inconsistently given as "LonghornEngineer," "Cr4bf04m," and "Parker Dillmann" across sources - same person, AND!XOR team member.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc27/doom-sao.glb
  method: kicad
  source_file: DOOM_SAO.brd
  generated: '2026-09-07'
  bytes: 259768
---

The DOOM SAO is a Superior Add-On built by Parker Dillmann (LonghornEngineer, working under the handle Cr4bf04m) for AND!XOR's DEF CON 27 badge in 2019. It pairs an Arduino-compatible ATSAMD21G18A microcontroller with a 1.3" 240x240 ST7789 LCD to show an animated DOOM Guy, whose look-left/look-right/look-back poses and "health" state can be driven either automatically or over the SAO's GPIO and I2C lines.

Beyond the DOOM Guy display, the SAO doubles as a hardware-hacking tool: it can passively sniff the I2C bus (with SAO-aware decoding), watch just its own DOOM-Guy traffic, or man-in-the-middle another device's serial UART line, all accessible through a menu over its USB-C serial console. It follows the AND!XOR SAO Reference Design and the SAO v1.69bis standard, and stores its DC-year, maker ID, and per-badge state in a simulated I2C EEPROM at address 0x50.

It was sold through AND!XOR's online shop and in person at DEF CON 27's Hacker Warehouse; the shop listing is no longer live. The hardware and firmware were released under the Apache License 2.0 on GitHub shortly after the con.

## Make your own

Full KiCad-style hardware files and Arduino-compatible firmware are published in the [DOOM_SAO GitHub repository](https://github.com/LonghornEngineer/DOOM_SAO), split into `Hardware` and `Software` folders, along with a README covering the serial menu, GPIO truth table, and I2C EEPROM map needed to build or interface with one.
