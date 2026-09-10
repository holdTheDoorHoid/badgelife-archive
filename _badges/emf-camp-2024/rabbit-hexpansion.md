---
title: Rabbit hexpansion
id: emf-camp-2024-rabbit-hexpansion
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
summary: An open-source hexpansion for the EMF Camp 2024 Tildagon badge with a single RGB LED and an I2C EEPROM.
functions: Lights an onboard RGB LED (red, green, blue channels) and stores hexpansion identification data on an I2C EEPROM, following the standard Tildagon hexpansion interface.
look:
  colors: []
  shape: hexagon
  themes:
  - animal
tech:
  mcu: none
  leds:
    count: 1
    type: RGB
    note: 5mm RGBA (RGB) LED, discrete, driven directly rather than addressable
  display: none
  connectivity:
  - i2c
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
  hardware_url: https://github.com/DanNixon/hexpansions/tree/main/rabbit
  firmware_url: null
  eda_tool: KiCad
  license: CERN-OHL-P-2.0
  fab_url: null
  notes: KiCad schematic/PCB, DXF cutout files for the hexpansion shell, and SVG/PNG artwork are in the repo.
links:
- label: github.com/DanNixon/hexpansions/tree/main/rabbit
  url: https://github.com/DanNixon/hexpansions/tree/main/rabbit
  kind: repo
- label: github.com/DanNixon/hexpansions
  url: https://github.com/DanNixon/hexpansions
  kind: repo
images:
- file: assets/images/badges/emf-camp-2024/rabbit-hexpansion/7ab71485de.jpg
  source: "https://github.com/DanNixon/hexpansions/tree/main/rabbit"
  credit: "DanNixon"
  caption: "PCB render of the Rabbit hexpansion"
contact: {}
notes:
- Sheet listed this only as "Open-source Tildagon hexpansion published in DanNixon's hexpansions repo" (seen only in a search snippet); confirmed directly from the maker's GitHub repo and its README.
- No price, quantity, or public distribution details are given anywhere in the repo; this looks like a personal/one-off hexpansion Dan Nixon built for their own EMF Camp 2024 Tildagon badge rather than something sold or given away at scale.
- The repo's top-level README confirms these are hexpansions "designed for the EMF Camp Tildagon badge."
status: listed
sources:
- kind: url
  url: https://github.com/DanNixon/hexpansions/tree/main/rabbit
  title: Rabbit hexpansion
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-addons); event read as ''EMF Camp 2024''.'
- kind: url
  url: https://github.com/DanNixon/hexpansions/blob/main/rabbit/README.md
  title: hexpansions/rabbit/README.md at main
  accessed: '2026-09-10'
  note: Pinout and parts list (ZD24C64A EEPROM, 4.7k pull-up resistors, 5mm RGBA LED); confirms it is a Tildagon hexpansion.
- kind: url
  url: https://github.com/DanNixon/hexpansions
  title: DanNixon/hexpansions
  accessed: '2026-09-10'
  note: Repo-level README confirms these hexpansions are for the EMF Camp Tildagon badge and are licensed CERN-OHL-P-2.0.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Core facts (maker, event, what it is, hardware, license) confirmed on the maker's own GitHub repo, so this is more than a bare search snippet. Confidence is medium rather than high because no page states price, quantity, or how/whether it was distributed beyond the repo itself — it may simply be Dan Nixon's own badge accessory, not a general release.
last_modified_date: '2026-09-10'
---

The Rabbit hexpansion is an open-source expansion module for the Tildagon badge issued at EMF Camp 2024, built by Dan Nixon (DanNixon) as part of their personal `hexpansions` repository alongside three other modules (Flandre Scarlet wings, Le Carnard de Bleu, and a Maker Space badge). It plugs into the Tildagon's hexpansion header and carries a single 5mm RGB LED plus an I2C EEPROM for hexpansion identification, following the standard Tildagon hexpansion electrical interface.

The hardware is fully open: KiCad schematic and PCB files, DXF cutout files for the physical shell, and SVG/PNG artwork are all published in the repo under the CERN-OHL-P-2.0 open hardware license. No firmware is included or needed beyond what the host Tildagon badge already runs for hexpansions.

Nothing in the repo or README indicates a price, a production quantity, or a distribution channel (sale, giveaway, or otherwise) — it reads as a one-off or small personal build rather than a hexpansion sold to the wider EMF Camp community, though that could not be confirmed either way.

## Make your own

The `rabbit` folder in [DanNixon/hexpansions](https://github.com/DanNixon/hexpansions/tree/main/rabbit) has everything needed to reproduce it: open `rabbit.kicad_pro` in KiCad to get the schematic and PCB layout, and use `rabbit-inner.dxf` / `rabbit-outer.dxf` for the hexpansion shell cutouts. Parts are a Zetta ZD24C64A I2C EEPROM, 0805 4.7kOhm I2C pull-up resistors, and a 5mm RGBA (RGB) LED.
