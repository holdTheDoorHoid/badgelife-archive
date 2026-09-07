---
title: SAO Adapter for DEF CON 31 Badge
id: dc31-sao-adapter-for-def-con-31-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: MakeItHackin
  url: https://github.com/MakeItHackin
summary: A drop-in adapter that slides into the chamber slot of the non-electronic official DEF CON 31 badge, giving it two powered SAO ports.
functions: 'Powers two SAO (Simple Add-On) ports at 3.3V, up to 350mA combined, from a single AA battery. Includes a DIY solder-practice SAO kit to plug into one of the ports.'
look:
  colors:
  - black
  shape: rectangle
  themes:
  - hardware tool
  - learn to solder
  - security
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: 1x AA (3 included)
  sao_version: v1
get_one:
  price: $30.00
  price_usd: 30
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold on Tindie by MakeItHackin, and in person from Hacker Warehouse at DEF CON 31.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/MakeItHackin/ChamberAdapter
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/makeithackin/sao-adapter-for-def-con-31-badge
  url: https://www.tindie.com/products/makeithackin/sao-adapter-for-def-con-31-badge/
  kind: store
- label: github.com/MakeItHackin/ChamberAdapter
  url: https://github.com/MakeItHackin/ChamberAdapter
  kind: repo
images:
  - file: assets/images/badges/dc31/sao-adapter-for-def-con-31-badge/e98959feb8.jpg
    source: "https://www.tindie.com/products/makeithackin/sao-adapter-for-def-con-31-badge/"
    credit: "MakeItHackin"
    caption: "Close-up front view of the SAO adapter board"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/makeithackin/sao-adapter-for-def-con-31-badge/
  title: SAO Adapter for DEF CON 31 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc31''.'
- kind: url
  url: https://github.com/MakeItHackin/ChamberAdapter
  title: MakeItHackin/ChamberAdapter
  accessed: '2026-09-07'
  note: Maker's open-hardware repo for the adapter; confirms it slides into the DC31 badge chamber and powers two SAO ports; no firmware/gerbers content surfaced beyond assembly instructions and a YouTube tutorial link.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The adapter itself is a passive power/breakout board (no MCU, no onboard LEDs) — tech.mcu set to none. Could not confirm exact unit quantity made or whether it is still in stock; Tindie listing did not show a clear sold-out/in-stock indicator at the time of checking. The bundled DIY SAO kit''s own chip/LED details were not researched separately.'
last_modified_date: '2026-09-07'
---

MakeItHackin's SAO Adapter is a small breakout board built for the 2023 DEF CON 31 badge, which was itself a non-electronic object with a physical "chamber" cut into it for attendees to fill with their own hardware. The adapter slides into that chamber and turns it into two powered SAO ports, running at 3.3V and rated for up to 350mA combined, drawing power from a single AA battery (three are included, each good for roughly 10 hours).

The $30 kit ships with more than just the adapter board: a DIY BadgeLife SAO kit (four surface-mount parts and one through-hole part) for attendees to practice soldering, plus stickers, googly eyes, a tamper-evident sticker, and a mini lanyard to help secure the adapter in the badge chamber. It was sold both on Tindie and in person through Hacker Warehouse at the con. The hardware design is published on GitHub under MakeItHackin's ChamberAdapter repo, with an assembly walkthrough and a linked video tutorial, though no gerbers or BOM were confirmed during this pass.

## Make your own

Hardware files and an assembly guide are published at github.com/MakeItHackin/ChamberAdapter, with a linked YouTube video walking through putting the kit together.
