---
title: OFFZONE 2024 Lamp add-on
id: offzone-2024-offzone-2024-lamp-add-on
layout: badge
parent: OFFZONE 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2024
year: 2024
makers:
- name: BI.ZONE / Craft.Zone
summary: A lantern-shaped SAO add-on for the OFFZONE 2024 badge, with a red and yellow LED "flame" whose glow is set by turning a 3D-printed knob on a potentiometer.
functions: Turning the knob (mounted on a potentiometer) adjusts the lantern's LED "flame" glow; no other interactivity.
look:
  colors:
  - red
  - white
  - black
  shape: lantern
  themes: []
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: One 5730-package red LED and one 5730-package yellow LED behind a lens, forming a "flame."
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2024/lamp_addon
  firmware_url: null
  gerbers_url: https://github.com/bi-zone/offzone-hw/tree/master/2024/lamp_addon/lamp_addon_gbr
  bom_url: https://github.com/bi-zone/offzone-hw/blob/master/2024/lamp_addon/lamp_addon_BOM.html
  eda_tool: KiCad
  license: null
links:
- label: github.com/bi-zone/offzone-hw/tree/main/2024/lamp_addon
  url: https://github.com/bi-zone/offzone-hw/tree/main/2024/lamp_addon
  kind: repo
- label: lamp_addon README (BI.ZONE / Craft.Zone)
  url: https://github.com/bi-zone/offzone-hw/blob/master/2024/lamp_addon/README.md
  kind: doc
images:
- file: assets/images/badges/offzone-2024/offzone-2024-lamp-add-on/ebbeba18ee.jpg
  source: "https://github.com/bi-zone/offzone-hw/blob/master/2024/lamp_addon/README.md"
  credit: "BI.ZONE / Craft.Zone"
  caption: "Front of the lamp add-on SAO, showing the potentiometer knob and LEDs"
- file: assets/images/badges/offzone-2024/offzone-2024-lamp-add-on/9b6ac9abfc.jpg
  source: "https://github.com/bi-zone/offzone-hw/blob/master/2024/lamp_addon/README.md"
  credit: "BI.ZONE / Craft.Zone"
  caption: "Back of the lamp add-on SAO"
contact: {}
notes:
- Lamp-themed add-on board for the OFFZONE 2024 badge. Found by the event-year sweep, task con-phdays.
status: released
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2024/lamp_addon
  title: OFFZONE 2024 Lamp add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2024''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/blob/master/2024/lamp_addon/README.md
  title: "lamp_addon README, bi-zone/offzone-hw"
  accessed: '2026-09-08'
  note: "Maker's assembly README (Russian): PCB spec (2-layer FR4, red soldermask, black silkscreen), BOM (red + yellow 5730 LEDs, two 100-ohm resistors, a 2M-ohm potentiometer, a PLD-4 connector), assembly steps, and a 3D-printed knob (lamp_addon_knob.stl) for the potentiometer. Confirms front/back photos."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'One of six OFFZONE 2024 add-ons in the same repo (cube_blue, cube_green, seal, thisisfine, zil - each likely deserving its own entry, see report). No price, quantity, or distribution details found on the repo; OFFZONE add-ons are typically given out rather than sold, but this was not confirmed anywhere. PLD-4 is a 4-pin SAO connector, so sao_version is recorded as v1. No dedicated theme tag fit the vocabulary list (closest would be a new "lantern"/"fire" tag), so themes was left empty rather than guessed. License for the hardware files was not stated in the repo.'
last_modified_date: '2026-09-08'
---

The Lamp add-on is one of a set of SAO-style plug-in boards BI.ZONE / Craft.Zone made for the OFFZONE 2024 conference badge. The PCB itself is cut into the silhouette of an oil lantern: a red top and base, a white/silver body, and a black knob housing, with a red and a yellow 5730-package LED glowing behind a teardrop-shaped cutout to suggest a flame. A 3D-printed knob, mounted on a 2 MΩ potentiometer, lets the wearer turn the flame's glow up or down; the board connects to the host badge through a 4-pin PLD-4 (SAO v1) header.

The hardware is openly published on BI.ZONE's `offzone-hw` GitHub repository as KiCad source files, Gerbers, a BOM, and an assembly guide, alongside five other 2024 add-ons (cube_blue, cube_green, seal, thisisfine, and zil). No firmware is involved since the board is a passive LED/potentiometer circuit with no microcontroller.

## Make your own

Files are in the `2024/lamp_addon` folder of [bi-zone/offzone-hw](https://github.com/bi-zone/offzone-hw/tree/master/2024/lamp_addon): KiCad schematic/PCB source, Gerbers, a BOM (`lamp_addon_BOM.html`), and an STL for the printed knob (`lamp_addon_knob.stl`). Per the maker's README: solder the two 1206 100-ohm resistors first (no polarity), then the two 5730 LEDs lens-down (observing polarity), then the potentiometer, then the PLD-4 connector, and finally print and fit the knob onto the potentiometer's shaft.
