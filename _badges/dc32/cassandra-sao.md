---
title: Cassandra SAO
id: dc32-cassandra-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: GoonBoxBadge (MK Factor)
  url: https://github.com/compukidmike/Cassandra
summary: A Doctor Who-themed SAO built around a backlit flex PCB suspended on a frame.
functions: An SAO for our Whovians, Cassandra is a backlit flex PCB suspended on a frame.
look:
  colors: []
  shape: null
  themes:
  - sci-fi
  - tv
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: Kit ships with 4 LEDs and 4 resistors (one spare of each) even though only 3 are used.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: $20.00
  price_usd: 20.0
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Sold as a kit; the maker's tweet said to watch their Twitter/X account for drops during DEF CON 32.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: t.co/aGlGuf3UXy
  url: https://t.co/aGlGuf3UXy
  kind: website
- label: compukidmike/Cassandra (GitHub)
  url: https://github.com/compukidmike/Cassandra
  kind: repo
images:
- file: assets/images/badges/dc32/cassandra-sao/3867ed1208.jpg
  source: "https://github.com/compukidmike/Cassandra"
  credit: "compukidmike"
  caption: "Cassandra SAO, front view with backlit flex PCB"
- file: assets/images/badges/dc32/cassandra-sao/cf2e40ed16.jpg
  source: "https://github.com/compukidmike/Cassandra"
  credit: "compukidmike"
  caption: "Cassandra SAO, assembled back view showing LEDs and SAO connector"
contact:
  handles:
  - '@GoonBoxBadge'
  raw:
  - Watch  on Twitter for drops during DEFCON
notes:
- Provided as a kit, there may be a limited number of assembled ones available.
status: listed
sources:
- kind: sheet
  event: dc32
  row: 60
  updated: ''
- kind: url
  url: https://t.co/aGlGuf3UXy
  title: GoonBoxBadge tweet (redirects to GitHub repo)
  accessed: '2026-09-06'
  note: Short link listed on the community sheet resolves to the compukidmike/Cassandra GitHub repo.
- kind: url
  url: https://github.com/compukidmike/Cassandra
  title: "compukidmike/Cassandra: assembly instructions and photos"
  accessed: '2026-09-06'
  note: Repo README confirms the description, kit contents (PCB, flex PCB, SAO connector, 4 LEDs/resistors with one spare each, sticker, instruction card), and assembly steps. Only images and a README are published, no schematic/gerber/BOM files.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    Maker's own GitHub repo (compukidmike/Cassandra) confirms the sheet's description and kit contents,
    but the repo has no storefront, price confirmation, quantity, or availability info beyond the sheet's
    $20 price and the note to watch Twitter for drops. No schematic, gerber, or firmware files are published
    in the repo despite the assembly writeup, so make_your_own.open_source is left null rather than guessed.
    Could not confirm whether GoonBoxBadge and compukidmike are the same person/team or a duo (MK Factor);
    no separate profile for "GoonBoxBadge" or "MK Factor" was found in the time budget.
last_modified_date: '2026-09-06'
---

Cassandra is a Doctor Who-themed SAO made by GoonBoxBadge (credited on the community sheet as MK Factor) for DEF CON 32 in 2024. Rather than a rigid PCB face, it centers on a backlit flex PCB suspended on a frame, lit by three surface LEDs wired on the back of the board (the kit includes a fourth LED and resistor as spares). It has no microcontroller — it's a simple passive, host-powered SAO that draws its light through the standard SAO header.

The maker sold it as a $20 kit, assembled on the back side of the board by the buyer, and pointed people to their Twitter/X account (@GoonBoxBadge) to watch for drops during the con rather than running a persistent storefront. The maker's GitHub repository (compukidmike/Cassandra) carries assembly instructions and reference photos of the front, back, kit contents, and SAO connector, but no schematic, gerber, or firmware files, so it isn't clear whether the hardware design itself was ever published beyond the finished kit.
