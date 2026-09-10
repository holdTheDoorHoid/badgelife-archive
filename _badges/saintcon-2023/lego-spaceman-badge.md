---
title: Lego Spaceman Badge
id: saintcon-2023-lego-spaceman-badge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: Kingbob
  url: https://github.com/JonDegn
summary: A backlit minibadge shaped like a Lego minifigure torso/spaceman shirt design, made in red, blue, and black PCB colors.
functions: A single red LED lights the design; passes through power to neighboring minibadges via pin headers, in the usual SAINTCON minibadge daisy-chain style.
look:
  colors:
  - red
  - blue
  - black
  shape: null
  themes:
  - toy
  - pop culture
  - minimalist
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: 1206 red LED, 1206 82Ω resistor
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 30 of each color (red, blue, black); ~90 total
  availability: unknown
  distribution:
  - swap
  where: Traded in person with the maker (Kingbob) at SAINTCON 2023.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  gerbers_url: null
  bom_url: null
  eda_tool: null
  fab_url: null
  notes: Repo has a build/soldering guide and parts list but no schematic, Gerbers, or BOM file.
links:
- label: minibadge.wiki/?search=Lego%20Spaceman%20Badge&year=2023
  url: https://minibadge.wiki/?search=Lego%20Spaceman%20Badge&year=2023
  kind: website
- label: Saintcon2023-minibages/lego-spaceman (GitHub)
  url: https://github.com/JonDegn/Saintcon2023-minibages/blob/main/lego-spaceman/readme.md
  kind: repo
images:
- file: assets/images/badges/saintcon-2023/lego-spaceman-badge/9a34690975.jpg
  source: https://github.com/JonDegn/Saintcon2023-minibages/blob/main/lego-spaceman/readme.md
  credit: Kingbob (JonDegn)
  caption: Lego Spaceman minibadge prototype photo
- file: assets/images/badges/saintcon-2023/lego-spaceman-badge/ba989762bc.png
  source: https://minibadge.wiki/?search=Lego%20Spaceman%20Badge&year=2023
  credit: Kingbob
  caption: Lego Spaceman minibadge, front
contact: {}
notes:
- 'category: Personal; rarity: Super Rare'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=Lego%20Spaceman%20Badge&year=2023
  title: Lego Spaceman Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2023''.'
- kind: url
  url: https://minibadge.wiki/2023.json
  title: Minibadge Wiki 2023 data export (JSON)
  accessed: '2026-09-07'
  note: 'Maker''s own submission record: description ("my first foray into minibadge design", fits Lego shirt designs, made in black/red/blue), soldering difficulty (Beginner), category (Personal), rarity (Super Rare), how to acquire ("Trade with me"), and the GitHub build-guide link.'
  archived: https://web.archive.org/web/20260611102022/http://minibadge.wiki/2023.json
- kind: url
  url: https://github.com/JonDegn/Saintcon2023-minibages/blob/main/lego-spaceman/readme.md
  title: 'Saintcon2023-minibages: lego-spaceman readme'
  accessed: '2026-09-07'
  note: 'Maker''s build guide: parts list (1x 1206 red LED, 1x 1206 82Ω resistor, 4x 2-pin header), soldering steps, and quantity produced (30 of each color: red, blue, black).'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No schematic, Gerber, or BOM files were found in the linked GitHub folder — only a readme and a photo. Price and current availability are not stated anywhere; the maker's own listing says it was distributed by trading in person at SAINTCON 2023, not sold, so price/quantity-remaining fields are left empty/unknown.
last_modified_date: '2026-09-07'
---

Lego Spaceman Badge is a SAINTCON 2023 minibadge by Kingbob (GitHub: JonDegn), his first minibadge design. It reuses the classic Lego minifigure torso/shirt graphic, sized to fit the minibadge form factor, and was produced in three PCB colors — red, blue, and black — with 30 boards made of each color. A single 1206 red LED (with an 82Ω current-limiting resistor) backlights the design; four 2-pin headers carry power through to neighboring badges in the usual SAINTCON minibadge chain, and there is no microcontroller on board.

The badge was not sold; Kingbob distributed it by trading in person at the con, which is reflected in its "Super Rare" rarity rating on the community minibadge.wiki database. A short build guide and parts list are published on GitHub alongside a prototype photo, but no schematic, Gerber files, or a formal bill of materials were included, so it is only partially open source.
