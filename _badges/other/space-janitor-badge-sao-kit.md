---
title: Space Janitor Badge SAO Kit
id: other-space-janitor-badge-sao-kit
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: blinkingthing
  url: https://www.tindie.com/stores/blinkingthing/
summary: 'A minimal, do-it-yourself SAO kit shaped as a nod to Roger Wilco, the janitor-turned-hero of the Sierra adventure game Space Quest, sold assembled-by-you on Tindie.'
functions: 'No animation or blink patterns; the four LEDs simply light up steadily once the SAO gets 3.3V and ground from the host badge ("no fancy blinkies, just constant power").'
look:
  colors: [red]
  shape: null
  themes: [space, sci-fi, kit]
tech:
  mcu: none
  leds:
    count: 4
    type: reverse-mount gullwing
    note: red LEDs, driven directly (no microcontroller), with a single 1206 resistor
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: "$10.00"
  price_usd: 10
  quantity: ''
  availability: unknown
  distribution: [purchase, kit]
  where: Sold as a kit on the maker's Tindie store (blinkingthing); listing was marked on break until November 25, 2019 as of the last check.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: Assembly instructions were posted as an image (blinkingthing.github.io/kit_instructions_thing_0x03.png); no schematic, Gerbers or firmware repo were found.
links:
- label: www.tindie.com/products/blinkingthing/space-janitor-badge-sao-kit
  url: https://www.tindie.com/products/blinkingthing/space-janitor-badge-sao-kit/
  kind: store
- label: blinkingthing.github.io
  url: https://blinkingthing.github.io/
  kind: website
images:
- file: assets/images/badges/other/space-janitor-badge-sao-kit/478b80057f.jpg
  source: "https://www.tindie.com/products/blinkingthing/space-janitor-badge-sao-kit/"
  credit: "blinkingthing"
  caption: "Space Janitor Badge SAO Kit, assembled"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: listed
sources:
- kind: url
  url: https://www.tindie.com/products/blinkingthing/space-janitor-badge-sao-kit/
  title: Space Janitor Badge SAO Kit
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''unknown''.'
- kind: url
  url: https://www.tindie.com/products/blinkingthing/space-janitor-badge-sao-kit/
  title: Space Janitor Badge SAO Kit (Tindie listing)
  accessed: '2026-09-07'
  note: Confirmed maker, price ($10), kit contents (PCB, 4 reverse-mount gullwing red LEDs, 1206 resistor, SAO header), SAO v1.69bis form factor, "on break until November 25, 2019" listing status, and a link to assembly instructions.
- kind: url
  url: https://blinkingthing.github.io/
  title: blinkingthing project page
  accessed: '2026-09-07'
  note: Checked for a mention of this kit; the page only lists two other projects (Shitty Pixel, Robot Banker), so no additional detail on Space Janitor was found there.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a general-purpose SAO sold on the maker's Tindie store rather than one made for a specific convention, so no event correction could be made (left as "other"). No quantity-made figure, current availability, or open-source hardware files were found; the listing's own image dates to August 2019, and the store copy at last check said sales were paused until November 25, 2019, so current live availability is unconfirmed.
last_modified_date: '2026-09-07'
---

The Space Janitor Badge SAO Kit is a simple do-it-yourself SAO (Simple Add-On) made by the hobbyist maker blinkingthing and sold through their Tindie store. Its name and design reference Roger Wilco, the put-upon janitor-turned-spacefaring hero of Sierra On-Line's Space Quest adventure game series. Unlike many SAOs built around blinking patterns or a microcontroller, this one is intentionally bare: it takes only 3.3V and ground from a host badge's SAO header and lights four reverse-mount gullwing red LEDs at constant brightness, with no animation logic at all.

The kit ships unassembled for $10 and includes the PCB, the four LEDs, a single 1206 resistor, and an SAO header (v1.69bis, 6-pin), with assembly instructions posted separately as an image on the maker's GitHub Pages site. It does not appear to have been produced for a particular convention; it reads as one of several small SAO kits blinkingthing has sold on Tindie alongside other "Thing 0x0N"-numbered projects. As of the last check the listing's sales were paused, and no information on total quantity made or current restocking was found.
