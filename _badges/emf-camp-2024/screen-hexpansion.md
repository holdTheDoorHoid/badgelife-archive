---
title: Screen Hexpansion
id: emf-camp-2024-screen-hexpansion
layout: badge
parent: EMF Camp 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: emf-camp-2024
year: 2024
makers:
- name: Mat Booth
  url: https://matbooth.co.uk/projects/emf/
summary: A hexpansion module that adds a small round auxiliary display to the Tildagon, EMF Camp 2024's badge.
functions: 'Plugs into a Tildagon hexpansion port to drive an additional round LCD, letting an app show extra data on a second screen; the maker''s own description: "plug-in an auxialliary screen or two to maximise the amount of data you can display at a time."'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: round LCD (GC9A01A driver)
  connectivity:
  - i2c
  battery: powered by host badge
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
  hardware_url: https://github.com/mbooth101/emf-screen-hexpansion/tree/main/hardware
  firmware_url: https://github.com/mbooth101/emf-screen-hexpansion
  eda_tool: KiCad
links:
- label: matbooth.co.uk/projects/emf
  url: https://matbooth.co.uk/projects/emf/
  kind: website
- label: mbooth101/emf-screen-hexpansion
  url: https://github.com/mbooth101/emf-screen-hexpansion
  kind: repo
images: []
contact: {}
notes:
- Auxiliary-screen hexpansion for the Tildagon badge documented alongside the author's other EMF badge projects. Found by the event-year sweep, task emf-addons.
status: released
sources:
- kind: url
  url: https://matbooth.co.uk/projects/emf/
  title: Screen Hexpansion
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-addons); event read as ''EMF Camp 2024''.'
- kind: url
  url: https://github.com/mbooth101/emf-screen-hexpansion
  title: mbooth101/emf-screen-hexpansion
  accessed: '2026-09-08'
  note: Repo README confirms it is a Tildagon hexpansion, MIT + CERN-OHL licensed, with firmware install steps via the badge's Hexpansions app.
- kind: url
  url: https://raw.githubusercontent.com/mbooth101/emf-screen-hexpansion/main/hardware/production/bom.csv
  title: hardware/production/bom.csv
  accessed: '2026-09-08'
  note: Board BOM (resistors, AT24C256C EEPROM for hexpansion identification); datasheets folder in the repo also includes GC9A01A, the round-LCD display driver used.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Maker's page and repo confirm what the hexpansion is and that it is open source (KiCad hardware + MicroPython/firmware files under MIT/CERN-OHL-P), but neither source states price, quantity made, or sale/distribution channel, so get_one fields are left empty. No MCU is on the board itself -- it is driven by the host Tildagon over I2C, per the EEPROM-based hexpansion identification scheme. No photos of the assembled board were found on either the maker's page or the GitHub repo (only a generic GitHub social-preview image), so no images were saved. Set status to released since the repo and firmware exist and are documented as installable, though no explicit "for sale" or unit-count statement was found.
last_modified_date: '2026-09-10'
model:
  file: assets/models/emf-camp-2024/screen-hexpansion.glb
  method: kicad
  source_file: hardware/screen-hexpansion.kicad_pcb
  generated: '2026-09-10'
  bytes: 136800
---

The Screen Hexpansion is a small expansion board for the Tildagon, the badge used at EMF Camp 2024 (and planned to continue at EMF Camp 2026). It plugs into one of the Tildagon's hexpansion ports and adds a round LCD (driven by a GC9A01A display controller) so that badge apps can show information on a second screen in addition to the badge's main display. Mat Booth, who also made the Tildagon's GPS Hexpansion and its speedometer app, describes it as his first hardware add-on design for an EMF Camp badge, joking that plugging in several at once could turn a Tildagon into a "multiocular" badge covered in eyes.

The hardware is fully open: KiCad schematics and PCB files, fabrication outputs, and a bill of materials are published in the project's GitHub repository under the CERN Open Hardware license, alongside MIT-licensed firmware. Like other Tildagon hexpansions, the board carries an onboard EEPROM (an AT24C256C) that the badge's built-in Hexpansions app reads to identify the module and fetch or update its firmware over the air; the same firmware can also be flashed manually with `mpremote`.

No pricing, production quantity, or sales channel is documented on the maker's page or in the repository, so it is unclear whether the Screen Hexpansion was sold, given away at EMF Camp, or built only for the maker's own use and shared as an open design.

## Make your own

The full KiCad hardware design and MIT/CERN-OHL-licensed firmware are in [mbooth101/emf-screen-hexpansion](https://github.com/mbooth101/emf-screen-hexpansion). To bring up firmware on an assembled board: insert the hexpansion into port 2 of a Tildagon, then run `mpremote mount EEPROM + run EEPROM/prepare_eeprom.py + cp EEPROM/app.py :/hexpansion/app.py` from the repo directory; afterward it can be moved to any port, or updated over the air using the Tildagon's Hexpansions app with VID `0x4D42` / PID `0x5EE5`.
