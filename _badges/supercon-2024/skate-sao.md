---
title: Skate SAO
id: supercon-2024-skate-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://hackaday.io/davedarko
summary: A proof-of-concept SAO by davedarko that mounts real fingerboard (miniature skateboard) trucks on a skate-deck-shaped PCB carrying an Andy Anderson quote; four boards were populated for the Supercon 2024 Add-on contest and brought to Pasadena.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - skateboard
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '4'
  availability: unknown
  distribution:
  - contest
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MrAnderson
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/199181-skate-sao
  url: https://hackaday.io/project/199181-skate-sao
  kind: hackaday
  archived: https://web.archive.org/web/20251208201739/https://hackaday.io/project/199181-skate-sao
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/MrAnderson
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MrAnderson
  kind: repo
- label: www.aliexpress.com/item/1005008003174723.html
  url: https://www.aliexpress.com/item/1005008003174723.html
  kind: website
images:
- file: assets/images/badges/supercon-2024/skate-sao/4d9d7dfc93.jpg
  source: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MrAnderson
  credit: davedarko
  caption: The Skate SAO board with fingerboard trucks mounted, carrying an Andy Anderson quote
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/199181-skate-sao
  title: Skate SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20251208201739/https://hackaday.io/project/199181-skate-sao
- kind: url
  url: https://hackaday.io/project/199181-skate-sao
  title: Skate SAO - Hackaday.io
  accessed: '2026-09-07'
  note: Confirms it as a proof-of-concept for mounting fingerboard trucks on a PCB, made by davedarko for the Supercon 2024 Add-on contest (Nov 2024, Pasadena); 4 boards populated and brought to Supercon; design files on GitHub.
  archived: https://web.archive.org/web/20251208201739/https://hackaday.io/project/199181-skate-sao
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MrAnderson
  title: Simple-Add-ons-SAO/MrAnderson at main
  accessed: '2026-09-07'
  note: 'Repo folder holding the design: 2411_Skate.md writeup, AndyAndersonBoard.jpg photo, MrAnderson.svg artwork, and a fingerboard.pretty KiCad footprint library. No schematic/BOM file for active electronics was found, consistent with this being a passive (no-MCU, no-LED) board.'
- kind: url
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/MrAnderson/2411_Skate.md
  title: 2411_Skate.md
  accessed: '2026-09-07'
  note: 'Maker''s own short writeup: "this is a proof of concept for using fingerboard trucks on PCBs, with an inspirational quote by Andy Anderson"; links to the same GitHub repo for Eagle/KiCad files.'
- kind: url
  url: https://www.aliexpress.com/item/1005008003174723.html
  title: AliExpress fingerboard trucks listing
  accessed: '2026-09-07'
  note: Redirected to a regional AliExpress listing; this is the sourcing link for the fingerboard trucks used as the SAO's mechanical hardware, not a listing for the SAO itself.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No MCU, LEDs, or display are present — this is a passive board (mechanical trucks + PCB + printed quote), so tech fields other than mcu/display are left null/none rather than guessed. Price, availability, and open-source license terms are not stated anywhere found; hardware files (KiCad footprint library, board art) are public on GitHub, but firmware is not applicable (no chip) and no explicit license file was found, hence open_source: partial. Andy Anderson quote text itself was not located in the sources checked. AliExpress link is for the trucks the maker bought in bulk, not a place to buy this SAO.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2024/skate-sao.glb
  method: kicad
  source_file: MrAnderson/MrAnderson/MrAnderson.kicad_pcb
  generated: '2026-09-10'
  bytes: 34756
---

The Skate SAO is a proof-of-concept add-on by hardware maker davedarko (Simple Add-ons project), built for the Supercon 2024 Add-on contest in November 2024 in Pasadena. Rather than driving LEDs or a microcontroller, the idea is purely mechanical: a real fingerboard (miniature skateboard) truck is mounted on a skateboard-deck-shaped PCB, turning a cheap bulk-bought hobby part into the SAO's defining feature. The board also carries a printed inspirational quote attributed to professional skateboarder Andy Anderson, tying the electronics-as-object joke to a real skate reference.

Four boards were populated and brought to Supercon for the contest. The design files — including a custom KiCad footprint library for the fingerboard truck hardware and the board artwork — are published on GitHub under davedarko's Simple-Add-ons-SAO repository, though no formal open-source license was found alongside them. As a passive board with no chip, LEDs, or display, its interest is entirely as a physical-design curiosity rather than an electronic one.
