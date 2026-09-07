---
title: AND!XOR DC29 Badge
id: dc29-and-xor-dc29-badge
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc29
year: 2021
makers:
- name: AND!XOR
  url: https://andnxor.com
  role: Zapp and Hyr0n
summary: 'A pure hardware-and-analog badge with no integrated circuits, made in response to the 2021 chip shortage: it ships unpopulated, and solving a glyph cipher printed on the back is required to identify which passive components go where before it can be soldered together.'
functions: 'Ships as a self-contained challenge, not a working badge out of the box. Wearers must use a multimeter and/or magnifying glass to identify unmarked SMD resistors, capacitors and transistors and a through-hole trimpot, crack a 16-symbol glyph cipher on the back that encodes component identifiers and placement, trace continuity to reverse-engineer the circuit (no schematic or BOM was published), and hand-solder the main PCB and four daughter PCBs together. Can simply be worn unsoldered as a badge, or completed as a functional analog circuit usable in another hardware project.'
look:
  colors: [black, gold, white, clear]
  shape: rectangle
  themes: [puzzle, ctf, learn to solder, minimalist]
  form_factor: pcb badge
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: 2x coin cell
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '800 kits'
  availability: sold_out
  availability_note: 'About 400 sold through the AND!XOR online store, per the Aug 2021 Hackaday coverage; the rest distributed in person at DEF CON 29 and via local drops. Checked 2026-09-07 via secondary coverage; store page not directly verified.'
  distribution: [purchase, free_drop]
  where: 'AND!XOR online store (roughly half the run) plus in-person distribution at DEF CON 29 and "local drops" in other cities.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/180738-andxor-dc29-badge
  url: https://hackaday.io/project/180738-andxor-dc29-badge
  kind: hackaday
- label: 'Hackaday: AND!XOR''s DEF CON 29 Electronic Badge Is An Assembly Puzzle'
  url: https://hackaday.com/2021/08/02/andxors-def-con-29-electronic-badge-is-an-assembly-puzzle/
  kind: article
- label: 'OSH Park blog: AND!XOR''s DEF CON 29 Electronic Badge is an Assembly Puzzle'
  url: https://blog.oshpark.com/2021/08/06/andxors-def-con-29-electronic-badge-is-an-assembly-puzzle/
  kind: article
- label: 'DEF CON Forums: AND!XOR DC29 thread'
  url: https://forum.defcon.org/node/237411
  kind: social
images:
  - file: assets/images/badges/dc29/and-xor-dc29-badge/ac3c9f45bf.jpg
    source: "https://hackaday.com/2021/08/02/andxors-def-con-29-electronic-badge-is-an-assembly-puzzle/"
    credit: "AND!XOR / Hackaday"
    caption: "Front of the AND!XOR DC29 badge, unpopulated"
  - file: assets/images/badges/dc29/and-xor-dc29-badge/3e825105bb.jpg
    source: "https://hackaday.com/2021/08/02/andxors-def-con-29-electronic-badge-is-an-assembly-puzzle/"
    credit: "AND!XOR / Hackaday"
    caption: "Rear of the AND!XOR DC29 badge showing the glyph cipher component markings"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/180738-andxor-dc29-badge
  title: AND!XOR DC29 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 29''.'
- kind: url
  url: https://hackaday.com/2021/08/02/andxors-def-con-29-electronic-badge-is-an-assembly-puzzle/
  title: "AND!XOR's DEF CON 29 Electronic Badge Is An Assembly Puzzle"
  accessed: '2026-09-07'
  note: 'Primary source for maker names (Zapp and Hyr0n), shape/finish details, quantity (800 kits, ~400 sold via store), OSH Park "After Dark" treatment, and the image files used.'
- kind: url
  url: https://blog.oshpark.com/2021/08/06/andxors-def-con-29-electronic-badge-is-an-assembly-puzzle/
  title: "AND!XOR's DEF CON 29 Electronic Badge is an Assembly Puzzle"
  accessed: '2026-09-07'
  note: 'Confirmed the OSH Park "After Dark" fab treatment (black substrate, clear solder mask, ENIG gold pads, white solder mask) and the badge-as-puzzle framing.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own Hackaday.io project page has little written detail beyond the gallery; most concrete facts (maker names, kit contents, quantity, sales split) come from the contemporaneous Hackaday.com article and were not independently re-confirmed on an AND!XOR-run page. No price, schematic, BOM, or gerber/firmware links were published by the maker as of these sources -- the whole point of the badge is that a schematic/BOM is withheld as part of the puzzle. Price not found; left empty. Could not verify whether the AND!XOR store still lists it (checked via secondary source only).'
last_modified_date: '2026-09-07'
---

The AND!XOR DC29 badge, created by team members Zapp and Hyr0n, was AND!XOR's response to the global chip shortage during the pandemic-affected DEF CON 29 (August 2021, Las Vegas). Rather than a microcontroller-driven electronic badge, it is a purely analog, passive-component hardware puzzle: no ICs, no schematic, and no bill of materials were provided. A kit consists of a main PCB, four daughter PCBs, a small bag of taped SMD resistors, capacitors and transistors plus a through-hole trimpot, two coin cells, a battery holder, and a lanyard.

To assemble it, a solver has to use a multimeter and magnifying glass to identify each unmarked component, crack a 16-symbol glyph cipher printed on the back of the board (icons including an apple, a rocket ship, a poker chip, and others) that encodes which component goes where, and trace continuity across the board to reverse-engineer the circuit before soldering it all together. The board is sized to resemble a CDC COVID-19 vaccination card and carries square lanyard holes and rounded, 1980s-style corners. It was fabricated by OSH Park using their "After Dark" process: a black substrate, clear solder mask that lets the copper traces show through, ENIG gold-plated pads, and white solder-mask lettering.

AND!XOR made 800 kits total. Roughly half were sold through their online store, with the rest handed out in person at DEF CON 29 and through informal "local drops" elsewhere. Because the puzzle depends on the components and wiring staying secret, no hardware files, firmware, or documentation were published for this badge.
