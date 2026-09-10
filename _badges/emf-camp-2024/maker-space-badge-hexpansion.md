---
title: Maker Space badge hexpansion
id: emf-camp-2024-maker-space-badge-hexpansion
layout: badge
parent: EMF Camp 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: emf-camp-2024
year: 2024
makers:
- name: DanNixon
summary: A hexpansion (plug-in expansion module) for the EMF Camp Tildagon badge, shaped like the Maker Space (makerspace.org.uk) "M" logo and outlined in red LEDs.
functions: Runs a background chasing-light effect across the 29 LEDs outlining the Maker Space M logo; the included MicroPython app is loaded automatically by the Tildagon badge from the hexpansion's onboard EEPROM and has no UI of its own.
look:
  colors:
  - red
  - black
  shape: logo
  themes:
  - logo
  - hardware tool
tech:
  mcu: none
  leds:
    count: 29
    type: discrete
    note: 0603 red LEDs, individually addressable via two AW9523BTQR I/O expanders (16 segments each, clockwise around the M shape)
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
  open_source: 'yes'
  hardware_url: https://github.com/DanNixon/hexpansions/tree/main/makerspace-badge
  firmware_url: https://github.com/DanNixon/hexpansions/tree/main/makerspace-badge/app
  eda_tool: KiCad
  license: MIT (firmware app; no separate license found for the hardware files)
links:
- label: github.com/DanNixon/hexpansions/tree/main/makerspace-badge
  url: https://github.com/DanNixon/hexpansions/tree/main/makerspace-badge
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'Sweep imported the sheet/search wording "Maker Space badge hexpansion"; the maker''s repo names it the same way, so no title correction was needed.'
status: released
sources:
- kind: url
  url: https://github.com/DanNixon/hexpansions/tree/main/makerspace-badge
  title: Maker Space badge hexpansion
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://raw.githubusercontent.com/DanNixon/hexpansions/main/makerspace-badge/README.md
  title: 'makerspace-badge/README.md at main · DanNixon/hexpansions'
  accessed: '2026-09-10'
  note: Confirmed LED count/driver, EEPROM, pinout table, and BOM; no license or price/quantity stated.
- kind: url
  url: https://github.com/DanNixon/hexpansions
  title: DanNixon/hexpansions
  accessed: '2026-09-10'
  note: Repo README and og:image description confirm this is a hexpansion for the EMF Camp Tildagon badge (used at EMF Camp 2024 and 2026).
- kind: url
  url: https://raw.githubusercontent.com/DanNixon/hexpansions/main/makerspace-badge/app/README.md
  title: makerspace-badge/app/README.md
  accessed: '2026-09-10'
  note: 'Confirmed included MicroPython firmware app (app.py, aw9523.py), EEPROM header (vid 0xCAFE, pid 0x0191, friendly_name MS-NCL), and that it runs a proof-of-concept chasing effect with no UI.'
- kind: url
  url: https://raw.githubusercontent.com/DanNixon/hexpansions/main/makerspace-badge/app/LICENSE.txt
  title: makerspace-badge/app/LICENSE.txt
  accessed: '2026-09-10'
  note: Firmware app is MIT licensed (license file copyright line names Corentin Lapeyre, likely carried over from a template repo).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Confirmed as a real, built hexpansion via the maker's own repo (schematics, PCB, BOM, README, plus a MicroPython firmware app for the EEPROM). No product photo of the assembled board was found in the repo (only the source logo artwork used to derive the LED outline, which is not a photo of the item, so no image was saved). No price, quantity made, or distribution method could be found, so those fields are left empty. Availability/status beyond "it exists and was built, with a working firmware demo" is unconfirmed; set to released on the assumption a repo with fabrication files, a finished KiCad PCB, and a working demo app was actually built, per typical Tildagon hexpansion projects, but this is not directly stated on the page. The firmware's MIT LICENSE.txt names a different person (Corentin Lapeyre) as copyright holder, likely boilerplate carried over from a hexpansion template repo rather than a separate contributor to this project; noted here rather than guessed at.
last_modified_date: '2026-09-10'
---

The Maker Space badge hexpansion is a plug-in module for the EMF Camp Tildagon badge, made by DanNixon for [Maker Space](https://www.makerspace.org.uk/), a UK makerspace/community organization. The hexagonal PCB outlines the Maker Space "M" logo with 29 individually addressable 0603 red LEDs, arranged clockwise in 16-segment groups driven by two AW9523BTQR I2C LED-driver/I/O-expander chips, with a ZD24C64A EEPROM (standard on Tildagon hexpansions) for board identification and configuration.

The project is one of several hexpansions DanNixon published in the same `hexpansions` GitHub repository (alongside a "Le Carnard de Bleu" duck, a "Rabbit," and "Flandre Scarlet" 3D-printed wings), all built for the Tildagon badge platform used at EMF Camp 2024 and 2026. No price, production quantity, or distribution details were found — the repository is a hardware design share rather than a storefront listing.

## Make your own

The GitHub repo includes full KiCad schematic and PCB files, a bill of materials (AW9523BTQR LED drivers, ZD24C64A EEPROM, 0603 red LEDs, 0805 resistors, 0603 capacitors), and fabrication output, plus an MIT-licensed MicroPython app (`app.py`, `aw9523.py`) that gets written to the hexpansion's EEPROM and demonstrates a chasing LED effect. To build one: fabricate the PCB from the KiCad files, assemble per the BOM, then flash the hexpansion EEPROM following EMF Camp's standard hexpansion documentation, using the header values given in the app's README (vid `0xCAFE`, pid `0x0191`, friendly name `MS-NCL`).
