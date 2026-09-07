---
title: "2018 SuperCon Ⅹ-proto (RE: proto-board)"
id: supercon-2018-2018-supercon-proto-re-proto-board
layout: badge
parent: Supercon 2018
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2018
year: 2018
makers:
- name: xBeau
  url: https://hackaday.io/xbeau
summary: A hobbyist reverse-engineering of the official expansion/proto board for the 2018 Hackaday Supercon badge, rebuilt from the released gerbers with surface-mount parts substituted for the originals.
functions: 'Reproduces the stock expansion board''s function: a 9-pin edge connector plugs it into the Supercon badge and it exposes three 4-pin SAO headers, driven by a 74HC595 shift register.'
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Not sold; a DIY reproduction anyone can mill or order from the published design files.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Hack-a-Day/2018-Supercon-Badge
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/162009-2018-supercon-proto-re-proto-board
  url: https://hackaday.io/project/162009-2018-supercon-proto-re-proto-board
  kind: hackaday
- label: 'Hack-a-Day/2018-Supercon-Badge (official badge repo, gerbers used for this reproduction)'
  url: https://github.com/Hack-a-Day/2018-Supercon-Badge
  kind: repo
images:
- file: assets/images/badges/supercon-2018/2018-supercon-proto-re-proto-board/551915d365.png
  source: "https://hackaday.io/project/162009-2018-supercon-proto-re-proto-board"
  credit: "xBeau"
  caption: "Reverse-engineered proto/expansion board for the 2018 Supercon badge"
- file: assets/images/badges/supercon-2018/2018-supercon-proto-re-proto-board/7bb0af5838.jpg
  source: "https://hackaday.io/project/162009-2018-supercon-proto-re-proto-board"
  credit: "xBeau"
  caption: "Laser-cut 1:1 scale board reference used to check the reproduced outline against the original"
contact: {}
notes:
- 'Not a commercial product: a personal reverse-engineering/documentation project, not something distributed to attendees.'
status: released
sources:
- kind: url
  url: https://hackaday.io/project/162009-2018-supercon-proto-re-proto-board
  title: "2018 SuperCon Ⅹ-proto (RE: proto-board)"
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''Supercon 2018''.'
- kind: url
  url: https://hackaday.io/project/162009-2018-supercon-proto-re-proto-board
  title: "2018 SuperCon Ⅹ-proto (RE: proto-board) - project logs"
  accessed: '2026-09-07'
  note: 'Maker, description, components (595 shift register, 9-pin edge connector, 3x SAO 4-pin headers), board dimensions (125x97.5mm, 14 degree connector angle), design files (KiCad 5, DXF/SVG outlines), and source gerbers link (Hack-a-Day/2018-Supercon-Badge repo).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is xBeau''s own reverse-engineering project, not the official Hack-a-Day expansion board itself (though it uses the officially released gerbers as its source). It reproduces the stock expansion board with SMD parts substituted for the originals; project logs describe it as unfinished/in-progress (KiCad layout only partially recreated), so no evidence it was ever fabricated as a finished, distributed product. No price, quantity, or LED count stated anywhere in the project. Related upstream project referenced by the maker: hackaday.io/project/162054-shift-register-for-supercon-badge (by "Mike"), not created as a separate archive entry per instructions.'
last_modified_date: '2026-09-07'
---

xBeau's 2018 SuperCon Ⅹ-proto (RE: proto-board) is a hobbyist reverse-engineering of the expansion/proto board that plugged into the official 2018 Hackaday Supercon badge. Rather than being an original design, it reconstructs the stock board from the gerber files Hackaday released for that year's badge, substituting surface-mount versions of the 74HC595 shift register and other discrete parts for the originals, and rebuilding the front/back copper layers from Voja's released gerbers.

The board keeps the original's form factor: a 9-pin edge connector set at a 14-degree angle plugs it into the badge, and it carries three 4-pin SAO headers for daisy-chaining add-ons, plus 0805/SOT-23 footprints for the discrete components. As part of the reverse-engineering process, xBeau laser-cut a 1:1 scale outline in acrylic to sanity-check the reconstructed board shape against the real badge before committing to a milled or ordered PCB.

Project logs describe the KiCad recreation as only partially complete at the time of the last update, with no record of it being fabricated in quantity or distributed to anyone. It should be read as documentation of the process of converting Hackaday's original gerbers into an editable KiCad project (including a walkthrough of the Gerber-to-KiCad layer mapping) rather than as a badge or SAO of its own that was made or sold.

## Make your own

The source material is the official Hack-a-Day 2018 Supercon badge repository, which includes the production gerbers for both the badge and its expansion board. xBeau's project logs walk through importing those gerbers into KiCad (mapping each Gerber file extension to its KiCad layer) and note the outline (Edge.Cuts) layer needs manual cleanup, since converting it directly produced a duplicate overlapping outline.
