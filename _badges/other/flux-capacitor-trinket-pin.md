---
title: FLUX capacitor trinket
id: other-flux-capacitor-trinket-pin
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 2017
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A Back to the Future-style flux capacitor pin with a flowing LED animation, built around an ATtiny13/ATtiny45. Not sold for a specific event; it's a standalone hobby pin, not an SAO.
functions: 'Flowing/blinking LED animation across the three "stages" of the flux capacitor graphic, driven by an ATtiny13a or ATtiny45.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - movie
  - pin
tech:
  mcu: ATtiny13a / ATtiny45
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/FluxCapacitor
  firmware_url: null
  eda_tool: Eagle
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: hackaday.io/project/25898-flux-capacitor-trinket
  url: https://hackaday.io/project/25898-flux-capacitor-trinket
  kind: hackaday
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/FluxCapacitor
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/FluxCapacitor
  kind: repo
images:
- file: assets/images/badges/other/flux-capacitor-trinket-pin/90bae5750f.png
  source: "https://hackaday.io/project/25898-flux-capacitor-trinket"
  credit: "davedarko"
  caption: "The FLUX capacitor trinket pin"
- file: assets/images/badges/other/flux-capacitor-trinket-pin/6ebec089d5.jpg
  source: "https://hackaday.io/project/25898-flux-capacitor-trinket/gallery"
  credit: "davedarko"
  caption: "Gallery photo of the flux capacitor trinket"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/25898-flux-capacitor-trinket
  title: FLUX capacitor trinket | Hackaday.io
  accessed: '2026-09-07'
  note: "Project page: created July 13, 2017 by davedarko, description \"emancipating this project from my blinking stuff project\"; no event named; Eagle schematic/board files (attiny45.sch/.brd) attached, chip variants ATtiny13a/25/45/85 discussed. Gallery images used for photos."
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO
  title: davedarko/Simple-Add-ons-SAO
  accessed: '2026-09-07'
  note: "Repo's project table lists FluxCapacitor as a pin (not an SAO): \"animations thanks to an Attiny13, the flux is flowing.\" No license stated for the repo."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No event/con was ever named for this item on Hackaday.io or GitHub — it reads as a personal hobby project, not something made for or sold at a specific convention, so event is left as "other". Exact LED count, battery/power source, price, quantity made, and license are not stated anywhere found; the FluxCapacitor subfolder''s readme.md is an empty placeholder file. The hardware files (Eagle .sch/.brd) are published but no firmware source was found in the repo, so make_your_own.open_source is "partial" rather than "yes". A project log on the same Hackaday.io page describes a later, seemingly unrelated pivot to an AVR fuse/high-voltage-programming "fixer" board built to recover bad ATtiny13a chips; that log is about salvaging chips for this project, not a different product, so it was not treated as a separate item.'
last_modified_date: '2026-09-07'
---

The FLUX capacitor trinket is a small blinky pin by Hackaday.io user davedarko (GitHub: davedarko), posted July 13, 2017 as a spin-off of his earlier "blinking stuff" project. It's built around an 8-pin AVR — the writeup discusses both ATtiny13a and ATtiny45 builds — driving an LED animation meant to mimic the three glowing stages of the flux capacitor from *Back to the Future*. It is explicitly listed as a pin rather than an SAO in the maker's own SAO repository index, and no specific convention or year of distribution is named anywhere in the sources found.

Design files (Eagle schematic and board layout for the ATtiny45 version) are published in davedarko's `Simple-Add-ons-SAO` GitHub repository, but the project's own readme file in that folder is empty and no firmware source could be located, so build instructions beyond the bare hardware files aren't available. A companion Hackaday.io log describes the maker running into a bad batch of ATtiny13a chips (only 2 of 15 worked) and building a separate high-voltage fuse-reset tool to recover them — a supply-chain side note on this project rather than a different product.

No price, quantity, or distribution details were found; this appears to have been a one-off/hobbyist build rather than something sold or handed out at an event.
