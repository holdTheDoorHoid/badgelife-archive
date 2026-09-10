---
title: Mysterio
id: other-mysterio-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2025
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A Mysterio (Marvel) themed SAO by davedarko built around a CH32V003 microcontroller, designed in January 2025 as a personal project after Hackaday Supercon 2024 to try a new chip.
functions: Blinks/animates via the CH32V003; no CTF or game function described.
look:
  colors: []
  shape: null
  themes:
  - movie
  - pop culture
tech:
  mcu: CH32V003
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MysterioSAO/mysterio
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/MysterioSAO
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MysterioSAO
  kind: repo
images:
- file: assets/images/badges/other/mysterio-sao/a1fd1e81f0.jpg
  source: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MysterioSAO
  credit: davedarko
  caption: Mysterio SAO PCB render
- file: assets/images/badges/other/mysterio-sao/1d4a47f037.jpg
  source: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MysterioSAO/mysterio
  credit: davedarko
  caption: Mysterio SAO board photo
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
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/MysterioSAO/2501_Mysterio.md
  title: MysterioSAO/2501_Mysterio.md
  accessed: '2026-09-07'
  note: 'Maker''s own project notes: origin story (post-Supercon-2024 burnout, wanted to try the CH32V003 chip), inspiration (Simen''s Marvel-hero SAOs), and a Mastodon link to Simen.'
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MysterioSAO/mysterio
  title: MysterioSAO/mysterio — KiCad project files
  accessed: '2026-09-07'
  note: Confirms KiCad EDA (mysterio.kicad_pcb/.kicad_sch/.kicad_pro) and a production/ export folder; no bill of materials or firmware source found in the repo for this design.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a personal design, not made for or sold at a specific convention — the maker''s notes say it was designed in Jan 2025 (folder prefix "2501") "to try a new chip" after Hackaday Supercon 2024, with no event named as its target; left under event: other rather than assigning a supercon-2024/2025 id. No LED count/type, price, quantity, or distribution info found — the repo has design files (KiCad PCB/schematic, a production/ export folder) but no firmware source or BOM specific to this board, so tech.leds, get_one.*, and firmware_url are left empty. Repo root README lists many of the maker''s other designs (Ghibli/Soot Sprites, Han SAOlo, Mr. Robot, Knight Rider, etc.) as separate potential entries — see other_items_found.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/mysterio-sao.glb
  method: kicad
  source_file: MysterioSAO/mysterio/mysterio.kicad_pcb
  generated: '2026-09-10'
  bytes: 105356
---

Mysterio is a small Marvel-themed SAO (simple add-on) designed by davedarko, inspired by a series of Marvel superhero SAOs created by Mastodon user Simen (@simenzhor). Rather than being made for a specific convention, davedarko built it in January 2025 as a personal project: after designing six SAOs for Hackaday Supercon 2024 and feeling some burnout watching other SAO designers get more recognition, they wanted a low-pressure design to "show off some skills" and try a chip they hadn't used before, the CH32V003 — the same low-cost RISC-V microcontroller that the Supercon 2024 badge itself can program.

The board's design files (schematic, PCB layout, and a production export folder) are published on GitHub in KiCad format as part of davedarko's larger `Simple-Add-ons-SAO` repository, which collects many of their SAO and badge designs. No firmware source specific to Mysterio was found alongside the hardware files, and the project notes do not mention LED count, price, quantity made, or how (or whether) it was distributed, so those fields are left blank pending better sources.

## Make your own

The KiCad project (schematic, PCB, and project files) is in the `MysterioSAO/mysterio` folder of the repository, alongside a `production` export folder. No separate bill of materials or firmware repository was found for this specific design.
