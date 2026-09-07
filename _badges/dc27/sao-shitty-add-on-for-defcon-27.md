---
title: DC27-SAO — Shitty Add-on for DefCon 27
id: dc27-sao-shitty-add-on-for-defcon-27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: DC404
  url: https://github.com/DC404
summary: A DIY solder-it-yourself SAO shaped like Mr. Fang, the ninja mascot of the DC404 (metro Atlanta) DEF CON group, made for DEF CON 27.
functions: Two LEDs mounted behind the eyes of the Mr. Fang face light up when the SAO is plugged into a powered badge; no other functions.
look:
  colors: []
  shape: null
  themes:
  - mascot
  - security
  form_factor: pcb sao
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: through-hole LEDs behind the eyes of the board, no driver chip
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/DC404/DC27-SAO
  firmware_url: null
  eda_tool: null
  gerbers_url: https://github.com/DC404/DC27-SAO/tree/master/GERBERS
  notes: Repo has Gerbers and step-by-step assembly instructions with photos; no schematic/EDA source files or firmware (there is no MCU).
links:
- label: github.com/DC404/DC27-SAO
  url: https://github.com/DC404/DC27-SAO
  kind: repo
images:
  - file: assets/images/badges/dc27/sao-shitty-add-on-for-defcon-27/4a775fb5b5.jpg
    source: "https://github.com/DC404/DC27-SAO"
    credit: "DC404"
    caption: "Mr. Fang SAO powered on, LED eyes lit"
  - file: assets/images/badges/dc27/sao-shitty-add-on-for-defcon-27/c78fed5643.jpg
    source: "https://github.com/DC404/DC27-SAO"
    credit: "DC404"
    caption: "Kit contents: Mr. Fang PCB, resistor, SAO connector, two LEDs"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/DC404/DC27-SAO
  title: DC27-SAO — Shitty Add-on for DefCon 27
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 27''.'
- kind: url
  url: https://raw.githubusercontent.com/DC404/DC27-SAO/master/README.md
  title: DC27-SAO README
  accessed: '2026-09-07'
  note: One-line description confirming it is a Shitty Add-on for DEF CON 27.
- kind: url
  url: https://raw.githubusercontent.com/DC404/DC27-SAO/master/Assembly.md
  title: DC27-SAO Assembly Instructions
  accessed: '2026-09-07'
  note: Kit contents (board, resistor, SAO connector, 2 LEDs), assembly steps, and photos of the board name "Mr. Fang" and the finished, powered SAO.
- kind: url
  url: https://forum.defcon.org/node/239410
  title: DC404 - DEF CON Forums
  accessed: '2026-09-07'
  note: 'Identifies DC404 as the metro Atlanta DEF CON group (active since 2003) whose logo/mascot is "ninja" Mr. Fang, matching the SAO''s shape (via search snippet; page itself failed to load directly).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    No storefront, price, quantity, or distribution info found anywhere (repo, forum
    search); likely a members-only build/give at DC404's own DEF CON 27 meetup rather
    than a sold item, but this is not confirmed by a source, so get_one fields are left
    empty. No schematic or EDA project files in the repo, only Gerbers and an assembly
    guide with photos, so open_source is "partial". No maker's personal name found,
    only the DC404 group.
last_modified_date: '2026-09-07'
---

DC27-SAO is a simple, solder-it-yourself Shitty Add-on made by DC404, the long-running metro Atlanta DEF CON group (active since 2003), for DEF CON 27 in 2019. The board is shaped like "Mr. Fang," DC404's ninja mascot, and carries no microcontroller: two through-hole LEDs are wired behind the character's eyes so they light up whenever the SAO is plugged into a powered badge.

The GitHub repository (DC404/DC27-SAO) documents the kit rather than a finished product: it ships as five parts — the PCB, a resistor, an SAO connector, and two LEDs — with a photographed, step-by-step assembly guide covering connector orientation, LED polarity, and a note that boards for older (DC26-style) SAO headers need the connector aligned differently. Gerber files are included, but there is no schematic source, BOM, or firmware, since the design has no active electronics beyond the LEDs and their current-limiting resistor.

No source found states a price, quantity made, or how it was distributed; it reads as a group project handed out or built at DC404's own DEF CON 27 activities rather than a commercial listing.
