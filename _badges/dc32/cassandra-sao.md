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
  where: Sold as a kit; the community sheet says to watch @GoonBoxBadge on Twitter/X for drops during DEF CON 32.
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
  archived: https://web.archive.org/web/20260509120845/https://github.com/compukidmike/Cassandra
images:
- file: assets/images/badges/dc32/cassandra-sao/3867ed1208.jpg
  source: https://github.com/compukidmike/Cassandra
  credit: compukidmike
  caption: Cassandra SAO, front view with backlit flex PCB
  archived: https://web.archive.org/web/20260509120845/https://github.com/compukidmike/Cassandra
- file: assets/images/badges/dc32/cassandra-sao/cf2e40ed16.jpg
  source: https://github.com/compukidmike/Cassandra
  credit: compukidmike
  caption: Cassandra SAO, assembled back view showing LEDs and SAO connector
  archived: https://web.archive.org/web/20260509120845/https://github.com/compukidmike/Cassandra
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
  title: t.co short link from the community sheet (301 redirect to GitHub repo)
  accessed: '2026-09-06'
  note: Short link listed on the community sheet returns a 301 to the compukidmike/Cassandra GitHub repo (re-checked 2026-09-06).
- kind: url
  url: https://github.com/compukidmike/Cassandra
  title: 'compukidmike/Cassandra: assembly instructions and photos'
  accessed: '2026-09-06'
  note: Repo README confirms the description, kit contents (PCB, flex PCB, SAO connector, 4 LEDs/resistors with one spare each, sticker, instruction card), and assembly steps. Only images and a README are published, no schematic/gerber/BOM files.
  archived: https://web.archive.org/web/20260509120845/https://github.com/compukidmike/Cassandra
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Fact-check 2026-09-06: every non-empty field re-checked against the sheet row (dc32 row 60), the t.co redirect, the repo README and the repo Images folder; both saved images are resized copies of the repo''s Front.jpg and Back.jpg. tech.mcu "none" and battery "powered by host badge" are inferred from the kit contents (PCB, flex PCB, SAO connector, LEDs, resistors only) rather than stated outright. The repo has no storefront, price confirmation, quantity, or availability info beyond the sheet''s $20 price and the note to watch Twitter for drops; the tweet itself was not read. No schematic, gerber, or firmware files are published in the repo, so make_your_own.open_source is left null rather than guessed. Could not confirm whether GoonBoxBadge and compukidmike are the same person/team or a duo (MK Factor).'
last_modified_date: '2026-09-06'
---

Cassandra is a Doctor Who-themed SAO made by GoonBoxBadge (credited on the community sheet as MK Factor) for DEF CON 32 in 2024. Rather than a rigid PCB face, it centers on a backlit flex PCB suspended on a frame, lit by three LEDs soldered on the back of the board (the kit includes a fourth LED and resistor as spares). The kit contains no microcontroller — just the LEDs, resistors and an SAO header — so it is a passive SAO powered by whatever badge it plugs into.

The maker sold it as a $20 kit, assembled on the back side of the board by the buyer, and the community sheet directed buyers to watch the @GoonBoxBadge Twitter/X account for drops during the con. The maker's GitHub repository (compukidmike/Cassandra) carries assembly instructions and reference photos of the front, back, kit contents, and SAO connector, but no schematic, gerber, or firmware files, so it isn't clear whether the hardware design itself was ever published beyond the finished kit.
