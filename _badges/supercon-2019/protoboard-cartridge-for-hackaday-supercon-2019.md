---
title: Protoboard Cartridge for Hackaday Supercon 2019
id: supercon-2019-protoboard-cartridge-for-hackaday-supercon-2019
layout: badge
parent: Supercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: supercon-2019
year: 2019
makers:
- name: Jeroen "Sprite_TM" Domburg (Spritetm)
  url: https://github.com/Spritetm
summary: A prototyping expansion cartridge for the 2019 Hackaday Supercon badge, designed by the badge's own creator and released as an open KiCad project.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
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
  open_source: true
  hardware_url: https://github.com/Spritetm/hadbadge2019_protoboard
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/Spritetm/hadbadge2019_protoboard
  url: https://github.com/Spritetm/hadbadge2019_protoboard
  kind: repo
images: []
contact: {}
notes:
- An official prototyping cartridge for the 2019 badge, designed by the badge's own creator. Found by the event-year sweep, task supercon-2019.
- 'Confirmed via the GitHub repo (README and repo description): "This is the design of a prototyping cart for the badge for the Hackaday Supercon 2019."'
status: released
sources:
- kind: url
  url: https://github.com/Spritetm/hadbadge2019_protoboard
  title: Protoboard Cartridge for Hackaday Supercon 2019
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2019); event read as ''supercon-2019''.'
- kind: url
  url: https://github.com/Spritetm/hadbadge2019_protoboard
  title: Spritetm/hadbadge2019_protoboard on GitHub
  accessed: '2026-09-10'
  note: Confirmed the cartridge exists, its purpose, and that it is an open KiCad hardware project (schematic, PCB layout, and PDF docs); no license file, price, or quantity info found; no photo of an assembled unit, only source files.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Only source found is the maker's own GitHub repo, which confirms the item and its purpose but gives no price, quantity, availability, or photo of an assembled board. No press coverage, storefront listing, or Hackaday.io page found. Treating as a released open-hardware design rather than a commercial product, since it appears to be shared as files only.
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2019/protoboard-cartridge-for-hackaday-supercon-2019.glb
  method: kicad
  source_file: cartprotoboard.kicad_pcb
  generated: '2026-09-10'
  bytes: 650696
---

This is a prototyping expansion cartridge for the 2019 Hackaday Supercon badge, designed by Jeroen "Sprite_TM" Domburg, the same engineer who designed the badge itself. It lets badge owners plug in a blank prototyping cart to build custom add-on circuits for the badge's cartridge slot, rather than needing to design a full custom cartridge PCB from scratch.

The project is released as an open KiCad design on GitHub, including the schematic, PCB layout, and a set of custom footprint libraries (empty headers, inverted headers, an even/odd prototyping pad pattern, and mouse-bite panelization connectors), plus PDF documentation. No pricing, production quantity, or photos of an assembled board were found; the repository appears to exist primarily as a shared hardware design for anyone with KiCad to fabricate their own.

## Make your own

The hardware files are in the GitHub repo at github.com/Spritetm/hadbadge2019_protoboard. Opening `cartprotoboard.sch` and `cartprotoboard.kicad_pcb` requires KiCad; the custom `.pretty` footprint libraries in the repo need to be added to KiCad's footprint library table before the project will resolve fully.
