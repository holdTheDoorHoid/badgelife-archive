---
title: Mr. Robot
id: supercon-2019-mr-robot-sao
layout: badge
parent: Supercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2019
year: 2019
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A Simple Add-On built as an I2C soundcard, homage to Brian Benchoff's earlier Mr. Robot badge but with a completely different schematic, made to test OSH Park's "after dark" black PCB finish.
functions: 'Acts as an I2C-controlled soundcard: an ATtiny85 drives a small piezo speaker through a BC847 transistor to produce sound on command from a host badge.'
look:
  colors:
  - black
  shape: null
  themes:
  - robot
  - tv
  - music
tech:
  mcu: ATtiny85
  leds: null
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: "$12.30 (OSH Park PCB fab cost for a 3-board share)"
  price_usd: 12.3
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  firmware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  eda_tool: Eagle
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: hackaday.io/project/168037-mr-robot-shitty-addon
  url: https://hackaday.io/project/168037-mr-robot-shitty-addon
  kind: hackaday
- label: oshpark.com/shared_projects/XmKK8P7r
  url: https://oshpark.com/shared_projects/XmKK8P7r
  kind: fab
images:
  - file: assets/images/badges/supercon-2019/mr-robot-sao/fbb58473d9.jpg
    source: "https://hackaday.io/project/168037-mr-robot-shitty-addon"
    credit: "davedarko"
    caption: "Mr. Robot SAO PCB"
  - file: assets/images/badges/supercon-2019/mr-robot-sao/6df3b79535.jpg
    source: "https://hackaday.io/project/168037-mr-robot-shitty-addon"
    credit: "davedarko"
    caption: "Mr. Robot SAO project log photo"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/168037-mr-robot-shitty-addon
  title: "Mr. Robot Shitty Addon - Hackaday.io"
  accessed: '2026-09-07'
  note: "Project description, components (ATtiny85, BC847, KMTG-1002/1102 piezo speaker), Eagle/PDF design files, and project logs referencing demoing I2C functionality at Hackaday Supercon 2019."
- kind: url
  url: https://oshpark.com/shared_projects/XmKK8P7r
  title: "Mr. Robot Badge Shitty Addon - OSH Park shared project"
  accessed: '2026-09-07'
  note: "PCB is a 2-layer, 1.58 x 1.57 in board, $12.30 for an OSH Park 3-pack share, uploaded Oct 16, 2019; recommends ordering in the 'afterdark' (black) finish."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: "Event corrected from 'other' to supercon-2019: the Hackaday.io project was created Oct 16, 2019 and its logs describe demoing I2C functionality at that year's Hackaday Supercon. No listed price for the finished SAO itself (only the raw OSH Park PCB fab cost), and no quantity-made or distribution details were found — the project reads as a personal/demo build rather than a widely distributed give-away. Firmware for the I2C soundcard function is described in the Hackaday project logs as unfinished/in-progress rather than a completed product."
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/mr-robot-sao/
---

The Mr. Robot SAO is a Simple Add-On by Hackaday.io user davedarko, built as a small homage to Brian Benchoff's earlier Mr. Robot badge — davedarko's version uses a completely different schematic, centered on an ATtiny85 driving a small piezo speaker (a KMTG-1002/1102) through a BC847 transistor. The idea was to turn the SAO into an I2C-controlled soundcard that a host badge could command over the SAO header's I2C lines.

The board doubled as a test vehicle for OSH Park's "After Dark" black PCB finish; the OSH Park shared-project listing explicitly recommends ordering it in that finish. The Hackaday.io project was created in October 2019, and its project logs describe demoing the I2C sound functionality at that year's Hackaday Superconference, though the logs also describe ongoing work to improve speaker volume (via an inverted oscillator) rather than a finished, shipped product.

Design files — Eagle schematic and board files, plus a PDF schematic for those without Eagle, and firmware for both the SAO ("slave") and a test/host ("master") microcontroller — are published on both the Hackaday.io project page and in davedarko's `Simple-Add-ons-SAO` GitHub repo, which collects several of his SAO designs.
