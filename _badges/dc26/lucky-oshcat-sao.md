---
title: Lucky OSHCat SAO
id: dc26-lucky-oshcat-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: Twinkle Twinkie
  url: https://hackaday.io/twinkletwinkie
summary: A Shitty Add-On by Twinkle Twinkie (TwinkleTwinkie) that re-imagines the "Prince OSHCat" design as a Japanese lucky cat (maneki-neko), with the coin lit by 1206/PLCC2 LEDs.
functions: The cat holds a coin lit from underneath by surface-mount LEDs, in the style of a maneki-neko lucky cat figurine.
look:
  colors: []
  shape: cat
  themes:
  - cat
  - jewelry
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $24.20 (OSHPark board order, qty 3)
  price_usd: 24.2
  quantity: ''
  availability: unknown
  distribution: []
  where: Not sold directly; the gerbers are shared on OSHPark so anyone can order their own boards.
make_your_own:
  open_source: true
  hardware_url: https://hackaday.io/project/159856-lucky-oshcat-sao
  firmware_url: null
  gerbers_url: https://oshpark.com/shared_projects/JM1OnMzh
  eda_tool: KiCad
  fab_url: https://oshpark.com/shared_projects/JM1OnMzh
links:
- label: hackaday.io/project/159856-lucky-oshcat-sao
  url: https://hackaday.io/project/159856-lucky-oshcat-sao
  kind: hackaday
  archived: https://web.archive.org/web/20260514071234/https://hackaday.io/project/159856-lucky-oshcat-sao
- label: oshpark.com/shared_projects/JM1OnMzh
  url: https://oshpark.com/shared_projects/JM1OnMzh
  kind: fab
- label: cdn.hackaday.io/files/1598566839279104/Lucky_OSHCat_hackaday.zip
  url: https://cdn.hackaday.io/files/1598566839279104/Lucky_OSHCat_hackaday.zip
  kind: hackaday
images:
- file: assets/images/badges/dc26/lucky-oshcat-sao/760b9405d7.jpg
  source: https://hackaday.io/project/159856-lucky-oshcat-sao
  credit: TwinkleTwinkie
  caption: Lucky OSHCat SAO PCB
  archived: https://web.archive.org/web/20260514071234/https://hackaday.io/project/159856-lucky-oshcat-sao
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/159856-lucky-oshcat-sao
  title: Lucky OSHCat SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260514071234/https://hackaday.io/project/159856-lucky-oshcat-sao
- kind: url
  url: https://hackaday.io/project/159856-lucky-oshcat-sao
  title: Lucky OSHCat SAO - Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed maker (TwinkleTwinkie), creation date (July 19, 2018), that it re-imagines the Prince OSHCat as a maneki-neko lucky cat, 1206/PLCC2 LEDs under the coin, and that KiCad/gerber files are shared. No price, quantity, or distribution details given for the SAO itself.
  archived: https://web.archive.org/web/20260514071234/https://hackaday.io/project/159856-lucky-oshcat-sao
- kind: url
  url: https://oshpark.com/shared_projects/JM1OnMzh
  title: OSHCat_PCB_gerbers_20170711-1532 - OSH Park shared project
  accessed: '2026-09-07'
  note: Board is a 2-layer, 2.01 x 2.41 in PCB; OSHPark order price for a set of 3 boards is $24.20. This is the fab cost of ordering the bare board yourself, not a maker-set retail price for an assembled SAO.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: Fact-check pass (2026-09-07) re-fetched both cited pages. Maker (TwinkleTwinkie), creation date (2018-07-19), the "Prince OSHCat" -> maneki-neko reimagining, and "1206/PLCC2 LEDs" under the coin are all confirmed verbatim on the Hackaday.io project page, which also links the OSH Park share and a KiCad+Gerbers zip, confirming make_your_own fields. OSH Park page confirms 2-layer, ~2.01x2.41in board and $24.20 for a set of 3, matching get_one.price/price_usd (labeled as fab cost, not retail, correctly). tech.mcu "none" is an inference (no chip, IC, or driver circuit mentioned anywhere in the project description, only passive LEDs) rather than an explicit maker statement, but is consistent with the guide's convention for passive boards and the evidence read. Saved image matches the project's own board photo and shows the described cat/coin design. No source states DEF CON 26 distribution specifically, quantity made, an assembled price, or availability, so those remain unknown/empty as before; not treated as a defect since nothing claims otherwise. No contradictions found between sources.
last_modified_date: '2026-09-07'
---

The Lucky OSHCat SAO is a Shitty Add-On by Twinkle Twinkie (TwinkleTwinkie on Hackaday.io), created July 19, 2018. It takes the "Prince OSHCat" design and reworks it into a Japanese lucky cat (maneki-neko), with the coin the cat holds lit from below by surface-mount 1206/PLCC2 LEDs.

The design is fully open: KiCad schematics and Gerber files are bundled in a downloadable zip on the Hackaday.io project page, and the bare board is also shared on OSH Park as a ready-to-order project (a set of three 2-layer, roughly 2 x 2.4 inch boards runs $24.20 through OSH Park's fab service). No maker storefront, assembled-unit price, or production quantity was found, so it appears the SAO itself was not sold as a finished product — only the files to build your own.
