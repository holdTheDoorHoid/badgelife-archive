---
title: CompuKidMike Personal Minibadge
id: saintcon-2022-compukidmike-badge-minibadge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: CompuKidMike
  url: https://github.com/compukidmike
summary: A SAINTCON 2022 minibadge with a flexible circuit "heart" that floats above a magnet mounted on the PCB, moving slightly in and out as it's touched.
functions: 'No lights or firmware: the flex circuit and magnet form a small kinetic/tactile gimmick rather than an electronic display.'
look:
  colors: [black, gold]
  shape: circle
  themes: [minimalist]
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed as a minibadge kit at SAINTCON 2022 (Utah); no separate storefront found.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/compukidmike/saintcon2022
  firmware_url: null
  eda_tool: null
  notes: 'Assembly instructions and board photos are published; no schematic/Gerber files were found in the linked repo path.'
links:
- label: saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  kind: website
- label: 'GitHub: compukidmike/saintcon2022 (repo)'
  url: https://github.com/compukidmike/saintcon2022
  kind: repo
- label: 'Minibadge assembly instructions (README)'
  url: https://github.com/compukidmike/saintcon2022/blob/main/MinibadgeInstructions/README.md
  kind: doc
images:
- file: assets/images/badges/saintcon-2022/compukidmike-badge-minibadge/9782913e87.jpg
  source: "https://github.com/compukidmike/saintcon2022/blob/main/MinibadgeInstructions/README.md"
  credit: "CompuKidMike"
  caption: "Kit parts: flex circuit with etched heart, headers, resistor pad, and the black minibadge PCB with a magnet mounted in the center"
- file: assets/images/badges/saintcon-2022/compukidmike-badge-minibadge/aff876907b.jpg
  source: "https://github.com/compukidmike/saintcon2022/blob/main/MinibadgeInstructions/README.md"
  credit: "CompuKidMike"
  caption: "Assembled minibadge, close up, showing the flex-circuit heart floating above the mounted magnet"
contact: {}
notes:
- CompuKidMike's personal-icon minibadge (distinct from his official full SAINTCON 2022 badge already catalogued). Found by the event-year sweep, task saintcon-2022.
- 'The community sheet/sweep listed this as "COMPUKIDMIKE Badge (minibadge)"; the maker''s own repo calls it the "Compukidmike Personal Minibadge," with the assembly file also referring to it informally as a "Heart Minibadge." Title updated to match the maker''s usage.'
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: COMPUKIDMIKE Badge (minibadge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2022); event read as ''saintcon-2022''.'
- kind: url
  url: https://github.com/compukidmike/saintcon2022/blob/main/MinibadgeInstructions/README.md
  title: 'Compukidmike Personal Minibadge — Minibadge Instructions'
  accessed: '2026-09-10'
  note: 'Maker''s own assembly instructions: confirms title, parts list (flex circuit, magnet, resistors, headers), the moving-heart mechanism, and no LEDs/chip.'
- kind: url
  url: https://github.com/compukidmike/saintcon2022
  title: 'compukidmike/saintcon2022 (GitHub repo)'
  accessed: '2026-09-10'
  note: 'Confirms maker and event; repo root README links the minibadge instructions and separate badge-wing soldering instructions.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Confirmed via the maker''s own GitHub repo (compukidmike/saintcon2022), which is more authoritative than the PDF sweep source (the PDF could not be parsed as text). No price, quantity made, or separate storefront was found — this reads as a badge-included kit rather than a sold item, but that is not stated explicitly anywhere. No schematic or Gerber files were found in the repo, only assembly photos and instructions, so make_your_own.open_source is "partial." No LEDs, MCU, or display are present or mentioned; the piece is a two-resistor, magnet-and-flex-circuit mechanical gimmick.'
last_modified_date: '2026-09-10'
---

CompuKidMike's SAINTCON 2022 minibadge is a small kinetic piece rather than a blinky one: a flexible printed circuit etched with a heart shape is soldered at its ends to a black PCB base that has a magnet mounted at its center. The flex circuit arcs up and over the magnet, and because of the magnet's pull the heart "floats" just above the board and shifts slightly in and out when pressed or moved, giving it a small tactile motion instead of any light or sound. The base PCB carries a "#badgelife" mark and "SAINTCON 2022" text, and the whole thing was meant to plug into the wings of that year's official SAINTCON badge alongside other minibadges.

The kit is simple to build: two 0603 resistors, two solder jumpers, four 2-pin headers, the flex circuit, and the base board. There is no microcontroller, no LEDs, and no battery — it's a passive electromechanical trinket, and the build documentation is entirely about getting the flex circuit soldered and shaped correctly (including a warning that the iron will be drawn to the magnet while soldering).

## Make your own

CompuKidMike published assembly photos and step-by-step instructions for this minibadge in the `MinibadgeInstructions` folder of his `saintcon2022` GitHub repo. No schematic or PCB source files were found there, so someone wanting to reproduce it would have the assembly steps and reference photos but would need to redesign the board and flex circuit from scratch.
