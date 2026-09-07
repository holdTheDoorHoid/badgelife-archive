---
title: SAO_OLED — SAO Badge with I2C OLED 64x128
id: supercon-2024-sao-oled-sao-badge-with-i2c-oled-64x128
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Andy Geppert
  url: https://github.com/ageppert
summary: 'A passive SAO breakout for a generic I2C monochrome OLED, with a pass-through SAO port and a QWIIC/STEMMA QT port for chaining more I2C add-ons.'
functions: 'Drives a generic 0.96" (128x64) or 1.5" (128x128) monochrome I2C OLED (address 0x3C, alt 0x3D) from a host badge over the SAO connector; has no onboard MCU, so the host badge does the driving. Includes a second SAO pass-through port and a QWIIC connector so other I2C add-ons can be daisy-chained alongside it.'
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: 0.96" or 1.5" I2C OLED (128x64 / 128x128, socketed, not included)
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: 'Listed as available as a kit through Core64.io (Andy Geppert''s storefront); not independently confirmed by this research pass.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ageppert/SAO_OLED
  firmware_url: null
  eda_tool: KiCad
notes: []
links:
- label: github.com/ageppert/SAO_OLED
  url: https://github.com/ageppert/SAO_OLED
  kind: repo
- label: SAO OLED project log (hackaday.io)
  url: https://hackaday.io/project/194077-sao-oled
  kind: hackaday
images:
- file: assets/images/badges/supercon-2024/sao-oled-sao-badge-with-i2c-oled-64x128/ab8be252e5.jpg
  source: "https://github.com/ageppert/SAO_OLED"
  credit: "Andy Geppert"
  caption: "SAO_OLED v0.1 board render, front"
- file: assets/images/badges/supercon-2024/sao-oled-sao-badge-with-i2c-oled-64x128/40dd31e23f.jpg
  source: "https://github.com/ageppert/SAO_OLED"
  credit: "Andy Geppert"
  caption: "SAO_OLED v0.1 board render, back"
contact: {}
status: released
sources:
- kind: url
  url: https://github.com/ageppert/SAO_OLED
  title: SAO_OLED — SAO Badge with I2C OLED 64x128
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/ageppert/SAO_OLED
  title: 'ageppert/SAO_OLED repository contents'
  accessed: '2026-09-07'
  note: 'Repo has no README; confirmed KiCad 7 design files under "Electronic Design" (Schematic/Renders, Manufacturing folders) and two instruction PNGs.'
- kind: url
  url: https://raw.githubusercontent.com/ageppert/SAO_OLED/main/Electronic%20Design/SAO_OLED_V0.1%20Schematic%20and%20Renders/SAO_OLED_V0.1_Schematic.pdf
  title: 'SAO_OLED_V0.1 schematic PDF'
  accessed: '2026-09-07'
  note: 'Confirms no onboard MCU, generic I2C OLED socket (0x3C/0x3D), two SAO connectors (SFH11-NBPC-D03-ST-BK) plus a QWIIC port, dated 2023-09-17, and links to the hackaday.io project page.'
- kind: url
  url: https://hackaday.io/project/194077-sao-oled
  title: 'SAO OLED - Hackaday.io'
  accessed: '2026-09-07'
  note: 'States the project was submitted to the Supercon 8 SAO Contest and that the maker planned to bring units to Supercon 2024; mentions kit availability via Core64.io.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The GitHub repo carries no README or price/quantity info; the hackaday.io project log (linked from the schematic PDF) is the source for the Supercon 8 (2024) tie-in and Core64.io kit availability, but that availability claim was not independently verified against the storefront itself, so get_one fields are left mostly unfilled. No LED info found (board appears to have no onboard LEDs beyond the OLED itself). Event corrected from "other" to supercon-2024 per the hackaday.io project log.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/sao-oled-sao-badge-with-i2c-oled-64x128/
---

SAO_OLED is a small "Simple Add-On" board by Andy Geppert (also behind the Core64/CORE4 core-memory SAOs and other badgelife projects) that sockets a generic I2C monochrome OLED — either a 0.96" 128x64 panel or a 1.5" 128x128 panel — and exposes it to a host badge over a standard 4-pin SAO connector. It carries no microcontroller of its own; the host badge's firmware talks to the OLED directly over I2C at the usual 0x3C (or 0x3D) address, so the board is essentially a display breakout in SAO form rather than a smart add-on.

Alongside the display socket, the board includes a second pass-through SAO port and a QWIIC/STEMMA QT connector, letting other I2C SAOs or QWIIC peripherals be chained on the same bus. It was designed in KiCad 7/8 (schematic dated September 2023) and submitted to the Hackaday Supercon 8 SAO Contest, with the maker's project log noting plans to bring units to Supercon 2024 (the con this entry is filed under). The hardware files — schematic, PCB, and STEP model — are published on GitHub under the "Electronic Design" folder, along with two instructional images for assembly; no firmware is needed since the board has no MCU.

Pricing, quantities made, and current storefront availability were not confirmed independently; the project log points to Core64.io (the maker's shop) as a place kits have been offered, but this was not checked directly against a live listing.
