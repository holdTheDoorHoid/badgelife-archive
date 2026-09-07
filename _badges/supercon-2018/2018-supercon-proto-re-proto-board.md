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
  hardware_url: https://hackaday.io/project/162009-2018-supercon-proto-re-proto-board
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/162009-2018-supercon-proto-re-proto-board
  url: https://hackaday.io/project/162009-2018-supercon-proto-re-proto-board
  kind: hackaday
- label: 'Hack-a-Day/2018-Supercon-Badge (official badge repo, linked by the maker as background; it holds the badge firmware, not the expansion-board gerbers)'
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
  note: 'Maker, description, components (1x 9-position edge connector, 3x 4-pin SAO headers), board dimensions (125x97.5mm) and connector angle (14 degrees) from the project''s Details/Components sections; design files (in-progress KiCad 5 zip with partial 595 shift register + LEDs, plus DXF/SVG outlines). Verified against individual project logs: "chip pad sniffn" and "cook''n with kicad" (SMD 74HC595 substitution, using Voja''s original Front/Back Copper gerbers), "reading between the gerbers" (gerber-to-KiCad layer mapping, Edge.Cuts duplicate-outline cleanup; gerbers came "from the official badge project" per Voja Antonic via hackaday.io chat, not from a named repo), and "smells like progress" (laser-cut 1:1 board reference, material not specified as acrylic in the source).'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is xBeau''s own reverse-engineering project, not the official Hack-a-Day expansion board itself. Corrected during verification: removed the unsupported "learn to solder" theme tag; removed an unsupported claim that the laser-cut reference was in acrylic (source only says "laser cut," no material given); and corrected make_your_own.hardware_url plus the github link label — the linked Hack-a-Day/2018-Supercon-Badge repo contains only firmware/README/LICENSE (confirmed via the GitHub API), not gerbers, so it was wrong to call it the gerber source. The actual design files (in-progress KiCad zip, DXF/SVG outlines) are hosted as attachments on xBeau''s own hackaday.io project page, and the underlying gerbers came from Voja Antonic via hackaday.io chat / "the official badge project," not a named public repo. Project logs describe the KiCad recreation as unfinished/in-progress, so no evidence it was ever fabricated as a finished, distributed product. No price, quantity, or LED count stated anywhere in the project. Related upstream project referenced by the maker: hackaday.io/project/162054-shift-register-for-supercon-badge (by "Mike"), not created as a separate archive entry per instructions.'
last_modified_date: '2026-09-07'
---

xBeau's 2018 SuperCon Ⅹ-proto (RE: proto-board) is a hobbyist reverse-engineering of the expansion/proto board that plugged into the official 2018 Hackaday Supercon badge. Rather than being an original design, it reconstructs the stock board from the gerber files Hackaday released for that year's badge, substituting surface-mount versions of the 74HC595 shift register and other discrete parts for the originals, and rebuilding the front/back copper layers from Voja's released gerbers.

The board keeps the original's form factor: a 9-pin edge connector set at a 14-degree angle plugs it into the badge, and it carries three 4-pin SAO headers for daisy-chaining add-ons, plus 0805/SOT-23 footprints for the discrete components. As part of the reverse-engineering process, xBeau laser-cut a 1:1 scale outline to sanity-check the reconstructed board shape against the real badge before committing to a milled or ordered PCB.

Project logs describe the KiCad recreation as only partially complete at the time of the last update, with no record of it being fabricated in quantity or distributed to anyone. It should be read as documentation of the process of converting Hackaday's original gerbers into an editable KiCad project (including a walkthrough of the Gerber-to-KiCad layer mapping) rather than as a badge or SAO of its own that was made or sold.

## Make your own

The source material was the production gerbers for the badge and its expansion board, which hardware designer Voja Antonic shared via hackaday.io chat and which were posted to the official badge project; they are not included in the official Hack-a-Day 2018-Supercon-Badge GitHub repo, which holds only the badge's firmware. xBeau's project logs walk through importing those gerbers into KiCad (mapping each Gerber file extension to its KiCad layer) and note the outline (Edge.Cuts) layer needs manual cleanup, since converting it directly produced a duplicate overlapping outline. The in-progress KiCad project and DXF/SVG outline files are attached directly to xBeau's hackaday.io project page.
