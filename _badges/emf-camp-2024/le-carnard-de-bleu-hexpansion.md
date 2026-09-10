---
title: Le Carnard de Bleu hexpansion
id: emf-camp-2024-le-carnard-de-bleu-hexpansion
layout: badge
parent: EMF Camp 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: emf-camp-2024
year: 2024
makers:
- name: DanNixon
  url: https://github.com/DanNixon
summary: A single-RGB-LED hexpansion for the EMF Camp Tildagon badge, its duck-shaped enclosure a nod to the artwork Dilbert paints in a Dilbert animated-series episode.
functions: Lights a single 5mm RGB LED (individually addressable red, green and blue channels) via the Tildagon badge's hexpansion connector.
look:
  colors: []
  shape: duck
  themes:
  - duck
  - animal
  - pop culture
tech:
  mcu: none
  leds:
    count: 1
    type: RGB
    note: 5mm through-hole RGB LED, channels driven individually (not addressable/WS2812-style)
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/DanNixon/hexpansions/tree/main/le-carnard-bleu
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/DanNixon/hexpansions/tree/main/le-carnard-bleu
  url: https://github.com/DanNixon/hexpansions/tree/main/le-carnard-bleu
  kind: repo
images: []
contact: {}
notes:
- Open-source Tildagon hexpansion published in DanNixon's hexpansions repo. Sweep's summary line has been confirmed against the maker's repo (README, KiCad/DXF files); event confirmed as EMF Camp Tildagon badge (2024). Found by the event-year sweep, task emf-addons.
status: released
sources:
- kind: url
  url: https://github.com/DanNixon/hexpansions/tree/main/le-carnard-bleu
  title: Le Carnard de Bleu hexpansion
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-addons); event read as ''EMF Camp 2024''.'
- kind: url
  url: https://raw.githubusercontent.com/DanNixon/hexpansions/main/le-carnard-bleu/README.md
  title: le-carnard-bleu README.md
  accessed: '2026-09-10'
  note: Confirms parts (ZD24C64A EEPROM, 0805 4.7k resistors, 5mm RGB LED), LED pinout, and the Dilbert-artwork reference for the name.
- kind: url
  url: https://github.com/DanNixon/hexpansions
  title: DanNixon/hexpansions repository
  accessed: '2026-09-10'
  note: Confirms the repo is a collection of hexpansions for the EMF Camp Tildagon badge, listing this project alongside Flandre Scarlet wings, Maker Space badge, and Rabbit.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Confirmed as a real, published open-source hexpansion (design files, schematic and Gerbers present in the repo) rather than a snippet-only rumor. No maker's photo of the assembled/populated board was found (repo has a reference duck.png illustration used for the enclosure artwork, plus DXF/KiCad source, but no finished-product photo), so no images were saved. Price, quantity made, and availability (was it sold, given away, or just published as DIY files?) are not stated anywhere in the repo and were left blank. EEPROM part number (ZD24C64A) recorded in notes but not modeled as a dedicated field.
last_modified_date: '2026-09-10'
---

Le Carnard de Bleu ("The Blue Duck") is a hexpansion — a small expansion module — for the Tildagon badge handed out at EMF Camp 2024, designed by DanNixon. It is a simple, single-LED project: a 5mm RGB LED with its red, green and blue channels wired to separate pins on the hexpansion connector so the host badge's firmware can drive each color independently, backed by a small ZD24C64A EEPROM (used for hexpansion identification, as is standard for the format) and a set of 0805 4.7kΩ current-limiting resistors.

The name and duck-shaped board outline are a reference to the painting Dilbert creates in an episode of the Dilbert animated series ("Le Carnard de Bleu"). DanNixon published the full open-source design — KiCad schematic and PCB files, fabrication Gerbers, and the DXF outlines used to cut the duck shape — in the same GitHub repository as several of his other EMF Camp 2024 hexpansions (Flandre Scarlet 3D-printed wings, a Maker Space badge hexpansion, and a Rabbit hexpansion).

## Make your own

The `le-carnard-bleu` folder in DanNixon's hexpansions repository contains everything needed to build one: the KiCad project (schematic, PCB layout, library tables), ready-to-send Gerbers under `fabrication/pcb`, and the `duck.dxf`/`duck-inner.dxf` outline files used for the board shape. The README lists the three parts to source (a ZD24C64A EEPROM, 0805 4.7kΩ resistors, and a 5mm RGB LED) and the LED-to-connector pinout.
