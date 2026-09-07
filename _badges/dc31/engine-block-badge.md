---
title: Engine block badge
id: dc31-engine-block-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Car Hacking Village
- name: Linted
  url: https://github.com/linted
  role: hardware and firmware design
summary: The DEF CON 31 Car Hacking Village badge, an RP2040 board shaped and silkscreened like an engine block, built around a full CAN bus stack instead of the usual I2C SAO bus.
functions: Speaks CAN 2.0B over four onboard MCP2558FD transceivers (one per SAO port plus one for the badge's own bus), runs MicroPython with a REPL over USB-C, and exposes an slcan interface so it can be used as a USB-to-CAN adapter for socketcan tools like cansniffer.
look:
  colors:
  - red
  - black
  shape: engine block
  themes:
  - automotive
  - security
  - radio
tech:
  mcu: RP2040
  leds:
    count: 13
    type: mixed (1206 + reverse-mount)
    note: 4 standard 1206 LEDs plus 9 reverse-mount LEDs (P2-1206RTCS2) laid out inside the engine-cylinder silkscreen art.
  display: none
  connectivity:
  - usb
  inputs:
  - buttons
  battery: 2x AA
  sao_version: v1.69bis
  sao_ports: 3
get_one:
  price: $70.00
  price_usd: 70.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold in person at DEF CON 31 by the Car Hacking Village ($69.42 if paying by credit card per the community sheet).
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/linted/CHV_badge_board
  firmware_url: https://github.com/linted/CHV_Badge_Firmware
  gerbers_url: https://github.com/linted/CHV_badge_board/tree/main/plot
  eda_tool: KiCad
  license: null
  notes: No explicit license file in either repo; both were public on GitHub as of the 2026-09-07 check.
links:
- label: www.carhackingvillage.com
  url: https://www.carhackingvillage.com
  kind: website
  archived: https://web.archive.org/web/20260810193641/https://www.carhackingvillage.com/
- label: CHV_badge_board (hardware, KiCad + Gerbers)
  url: https://github.com/linted/CHV_badge_board
  kind: repo
- label: CHV_Badge_Firmware
  url: https://github.com/linted/CHV_Badge_Firmware
  kind: repo
- label: CHV SAO Specification (CAN-over-SAO pinout used by this badge)
  url: https://github.com/linted/CHV_SAO_Specification
  kind: doc
- label: DC31 Car Hacking Village Badge and SAO (maker walkthrough video)
  url: https://www.youtube.com/watch?v=yvvOl6LfodQ
  kind: video
images:
- file: assets/images/badges/dc31/engine-block-badge/9b02db17f6.jpg
  source: https://www.youtube.com/watch?v=yvvOl6LfodQ
  credit: Car Hacking Village / Linted
  caption: Presentation slide showing the front and back of the DC31 CHV badge (from the maker's video walkthrough)
contact: {}
notes:
- $69.42 if using credit card
status: released
sources:
- kind: sheet
  event: dc31
  row: 21
  updated: '2023-06-08'
- kind: url
  url: https://www.carhackingvillage.com
  title: Car Hacking Village
  accessed: '2026-09-07'
  note: 2023 Badge Overview section links to the SAO spec and the maker's badge walkthrough video; confirms the CAN-over-SAO change.
  archived: https://web.archive.org/web/20260810193641/https://www.carhackingvillage.com/
- kind: url
  url: https://www.youtube.com/watch?v=yvvOl6LfodQ
  title: DC31 Car Hacking Village Badge and SAO
  accessed: '2026-09-07'
  note: Maker (Linted) walkthrough video, published 2023-08-10; slide lists full CAN bus, SAO connectors, MicroPython REPL, slcan interface. Thumbnail shows front/back photos of the physical badge.
- kind: url
  url: https://github.com/linted/CHV_badge_board
  title: linted/CHV_badge_board
  accessed: '2026-09-07'
  note: KiCad source + Gerbers for CHV_DC31 board; BOM (CHV_DC31.csv) gives MCU (RP2040), LED count/types, 3x SAO headers (v1.69bis 2x3 footprint), 4x MCP2558FD CAN transceivers, 2xAA battery holder, USB-C, W25Q16 NOR flash.
- kind: url
  url: https://github.com/linted/CHV_Badge_Firmware
  title: linted/CHV_Badge_Firmware
  accessed: '2026-09-07'
  note: README describes firmware for "emulating a car on a single PCB"; C and MicroPython implementations; slcan/cansniffer setup instructions.
- kind: url
  url: https://github.com/linted/CHV_SAO_Specification
  title: linted/CHV_SAO_Specification
  accessed: '2026-09-07'
  note: Documents the badge's non-standard SAO pinout, replacing I2C with CAN TX/RX on the 2x3 v1.69bis connector.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts (MCU, LED count/types, SAO/CAN design, battery, connectors) come straight from the maker's own KiCad BOM and firmware README, corroborated by the maker's own walkthrough video. Could not find a storefront listing, so quantity made and post-con availability are unknown - it appears to have been sold only in person at DC31. No independent press coverage (hackaday.com, hackster.io) turned up; web search was unavailable for part of this research (session search quota exhausted, DuckDuckGo/Bing gave no usable results), so it is possible some coverage exists that was not found.
last_modified_date: '2026-09-07'
---

The DEF CON 31 Car Hacking Village badge is shaped and silkscreened like an engine block, with reverse-mount LEDs standing in for cylinders. Designed by CHV volunteer "Linted," it runs on an RP2040 and is built around CAN bus rather than the usual badge I2C bus: three SAO headers use the standard 2x3, 1.69bis footprint but swap the I2C pins for CAN TX/RX, each backed by its own MCP2558FD CAN FD transceiver, so the badge (and any attached SAO) can be addressed as CAN nodes. It runs MicroPython with a REPL over USB-C and also exposes an slcan interface, letting it double as a USB-to-CAN adapter for tools like `cansniffer`. Power comes from either USB-C or an onboard 2x AA holder.

It was sold in person at DEF CON 31 in the Car Hacking Village for $70 ($69.42 by credit card, per the community sheet). No online storefront listing was found, so it isn't clear how many were made or whether any were left over after the con.

## Make your own

The hardware (KiCad schematic, PCB, BOM, and Gerbers) is on GitHub at `linted/CHV_badge_board`, and the firmware — C and MicroPython implementations that "emulate a car on a single PCB" plus the slcan/cansniffer tooling — is at `linted/CHV_Badge_Firmware`. The modified CAN-over-SAO pinout is documented separately in `linted/CHV_SAO_Specification`. Neither repo carries an explicit license file.
