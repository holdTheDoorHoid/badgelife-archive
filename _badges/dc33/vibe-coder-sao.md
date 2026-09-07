---
title: Vibe Coder SAO
id: dc33-vibe-coder-sao
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: coryallegory
  url: https://www.tindie.com/stores/coryallegory/
summary: A #badgelife SAO depicting a confident "coder dog" (a riff on the "I don't know what I'm doing" science-dog meme) working at a keyboard lit by cycling multicolor LEDs.
functions: 4 multicolor LEDs cycle randomly, illuminating a keyboard graphic on the board
look:
  colors: []
  shape: null
  themes:
  - dog
  - meme
  - pop culture
tech:
  mcu: null
  leds:
    count: 4
    type: multicolor
    note: LEDs cycle randomly to light up the keyboard artwork
  display: null
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: $15
  price_usd: 15.0
  quantity: ''
  availability: sold_out
  availability_note: 'Listed out of stock on Tindie since 2025-09-13; checked 2026-09-06. Maker is taking pre-orders for DEF CON 34 (August 2026) pickup.'
  distribution:
  - purchase
  - preorder
  where: Sold on Tindie and in person at DEF CON 33; pre-orders for DEF CON 34 pickup, with Canada Post shipping to Canada (US shipping paused due to customs costs).
make_your_own:
  open_source: partial
  hardware_url: https://github.com/coryallegory/vibecoder
  firmware_url: null
  eda_tool: null
  notes: 'Repo holds design assets including a 3D-printable cover STL (vibecoderdog-cover.stl); no schematic/firmware source seen.'
links:
- label: github.com/coryallegory/vibecoder
  url: https://github.com/coryallegory/vibecoder
  kind: repo
- label: Vibe Coder SAO on Tindie
  url: https://www.tindie.com/products/coryallegory/vibe-coder-sao-badgelife-addon/
  kind: store
  title: 'Vibe Coder SAO #badgelife addon - coryallegory - Tindie'
  accessed: '2026-09-06'
  note: Confirms price ($15), out-of-stock status, LED count/behavior, and DEF CON 34 pre-order note.
images:
- file: assets/images/badges/dc33/vibe-coder-sao/5099fde60f.jpg
  source: "https://www.tindie.com/products/coryallegory/vibe-coder-sao-badgelife-addon/"
  credit: "coryallegory"
  caption: "Vibe Coder SAO product photo showing the coder-dog artwork and keyboard LEDs"
contact:
  emails:
  - corymetcalfe@gmail.com
notes:
- most excellent vibes for all
status: released
sources:
- kind: sheet
  event: dc33
  row: 36
  updated: 7/30/2025 19:39:39
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'MCU and exact LED part number are not published by the maker anywhere found; left null rather than guessed. This was the maker''s first PCB design/manufacturing project, per their own GitHub README.'
last_modified_date: '2026-09-06'
---

The Vibe Coder SAO is a #badgelife add-on that coryallegory made for DEF CON 33, their first PCB design and manufacturing project. It riffs on the "I don't know what I'm doing" science-dog meme, reimagining the dog as a confident coder hammering away at a keyboard. Four multicolor LEDs cycle randomly to light up the keyboard artwork on the board, and it connects through a standard 2x3 SAO header.

The SAO sold fully assembled for $15 through Tindie and in person at DEF CON 33, but has been listed out of stock since mid-September 2025. As of this check, the maker is taking pre-orders for pickup at DEF CON 34 in August 2026, with Canada Post shipping available within Canada (US shipping is paused due to customs costs). The GitHub repo for the project includes a 3D-printable cover STL, but no schematic or firmware source was found, so hardware openness is marked partial.

## Make your own

No public schematic, PCB source, or firmware was located. The repository at github.com/coryallegory/vibecoder currently offers only a 3D-printable enclosure/cover file (`vibecoderdog-cover.stl`).
