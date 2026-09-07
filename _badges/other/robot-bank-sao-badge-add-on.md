---
title: Robot Bank - SAO Badge Add On
id: other-robot-bank-sao-badge-add-on
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2019
series: "Blinking Things"
makers:
- name: blinkingthing
  url: https://blinkingthing.github.io/
summary: A robot-shaped SAO add-on styled after vintage 1980s robot bank toys, with three individually controllable LEDs and a default chomping/blinking animation.
functions: Plays LED animations (at least three, including a default chomping/blinking pattern); animations and LED intensity can be reprogrammed over I2C.
look:
  colors: []
  shape: robot
  themes:
  - robot
  - retro computer
  - toy
tech:
  mcu: ATtiny85
  leds:
    count: 3
    type: discrete
    note: Three individually controllable LEDs; fully-assembled version plays animations via the ATtiny85, a "prototype kit" version omits the MCU and each LED is statically lit instead.
  display: none
  connectivity:
  - i2c
  inputs: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: $20.00
  price_usd: 20
  quantity: ''
  availability: unknown
  availability_note: 'Tindie listing checked 2026-09-07: seller''s shop banner read "taking a break until Nov. 25, 2019," an old notice left over from the original listing date; current stock status could not be confirmed from the page text.'
  distribution:
  - purchase
  where: Sold on Tindie by seller "blinkingthing" (Sunland, California).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: 'Tindie listing links a documentation PDF (https://blinkingthing.github.io/docs/W220497AXS15.pdf) hosted on the maker''s GitHub Pages site (blinkingthing.github.io), which lists this board as "Thing 0x02 - Robot Banker." The PDF looks like a datasheet/reference sheet rather than a full open-hardware release; no separate Gerbers, BOM, or firmware repo link was found.'
links:
- label: www.tindie.com/products/blinkingthing/robot-bank-sao-badge-add-on
  url: https://www.tindie.com/products/blinkingthing/robot-bank-sao-badge-add-on/
  kind: store
- label: blinkingthing.github.io
  url: https://blinkingthing.github.io/
  kind: website
- label: 'Robot Banker documentation (PDF)'
  url: https://blinkingthing.github.io/docs/W220497AXS15.pdf
  kind: doc
images:
- file: assets/images/badges/other/robot-bank-sao-badge-add-on/7e6a2dc9d2.jpg
  source: "https://www.tindie.com/products/blinkingthing/robot-bank-sao-badge-add-on/"
  credit: "blinkingthing"
  caption: "Robot Bank SAO board, front view"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: listed
sources:
- kind: url
  url: https://www.tindie.com/products/blinkingthing/robot-bank-sao-badge-add-on/
  title: Robot Bank - SAO Badge Add On
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''other''.'
- kind: url
  url: https://blinkingthing.github.io/
  title: Blinking Things Projects
  accessed: '2026-09-07'
  note: "Maker's project page; confirms this board is listed as 'Thing 0x02 - Robot Banker' with a linked documentation PDF."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Tindie listing (dated 2019, product images uploaded May-Aug 2019) gives the core specs: 72mm x 50mm robot-shaped SAO, ATtiny85, 3 LEDs, SAO v1.69bis (I2C) connector, $20, with a cheaper "prototype kit" variant lacking the MCU. No specific conference or event is named anywhere in the listing or on the maker''s site -- this reads as a general-market Tindie product rather than a badge made for one particular con, so event is left as "other" and the year (2019) is inferred only from the listing''s upload/creation dates, not stated explicitly. Could not confirm current stock/availability from the fetched page text. Could not find a firmware or hardware repository, only a documentation PDF.'
last_modified_date: '2026-09-07'
---

The Robot Bank is a small SAO (Simple Add-On) badge accessory made by "blinkingthing," styled after 1980s robot bank toys. The 72mm x 50mm PCB is shaped like the robot's face and body, and plugs into a host badge's SAO header (v1.69bis, 6-pin I2C) for power. A fully assembled version carries an ATtiny85 microcontroller driving three individually controllable LEDs through several built-in animations, including a default "chomping/blinking" pattern; the animations and LED brightness can be reprogrammed over I2C. A cheaper prototype-kit version skips the microcontroller entirely, leaving each of the three LEDs lit statically instead of animated.

The maker's site (blinkingthing.github.io) lists this board as "Thing 0x02 - Robot Banker" alongside one other project, "Thing 0x01 - Shitty Pixel," each with a linked reference PDF. No specific conference or year is stated on the Tindie listing or the maker's page; the listing's photos date to mid-2019, which is the best available guess for when it was made and sold, but it reads as a general Tindie storefront item rather than a badge produced for one particular event.
