---
title: rad-badge — Saintcon 2022 Minibadge
id: saintcon-2022-rad-badge-saintcon-2022-minibadge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: then3rd
  url: https://github.com/then3rd
summary: 'A fake, light-reactive Geiger counter that also plays MIDI songs, built as a SAINTCON minibadge.'
functions: 'Simulates radiation detection (light-reactive, not a real Geiger tube) with an audible/visual counter effect; plays MIDI songs converted to bytecode and flashed onto the chip; firmware and fuses are configurable/reprogrammable over USB via a USBasp programmer.'
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
  - minimalist
tech:
  mcu: ATtiny85
  leds: null
  display: none
  connectivity:
  - usb
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
  open_source: yes
  hardware_url: https://github.com/then3rd/rad-badge
  firmware_url: https://github.com/then3rd/rad-badge
  eda_tool: null
links:
- label: github.com/then3rd/rad-badge
  url: https://github.com/then3rd/rad-badge
  kind: repo
images:
  - file: assets/images/badges/saintcon-2022/rad-badge-saintcon-2022-minibadge/c23ee280ab.jpg
    source: "https://github.com/then3rd/rad-badge"
    credit: "then3rd"
    caption: "Assembled rad-badge minibadge"
  - file: assets/images/badges/saintcon-2022/rad-badge-saintcon-2022-minibadge/b7d429ab62.jpg
    source: "https://github.com/then3rd/rad-badge"
    credit: "then3rd"
    caption: "rad-badge bare PCB"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/then3rd/rad-badge
  title: rad-badge — Saintcon 2022 Minibadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''SAINTCON 2022''.'
- kind: url
  url: https://raw.githubusercontent.com/then3rd/rad-badge/main/README.md
  title: 'rad-badge README (Radiation Minibadge 2022)'
  accessed: '2026-09-07'
  note: 'Confirmed maker, event/year, ATtiny85 MCU run at 16MHz, MIDI-playback and light-reactive "fake Geiger counter" functions, USBasp programming flow, open-source firmware/hardware in the same repo, and image files (assembly.jpeg, pcb.jpeg, schematic.jpeg).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source found is the maker''s own GitHub repo (README); no press coverage, storefront, or Hackaday post turned up. Maker describes it as "cobbled together at the last minute" as a prototype experiment, so price, quantity made, and distribution/availability are not stated anywhere and are left empty. LED count/type is not documented in the README (the "geiger counter" effect is light-reactive/sound-based per the README, and no explicit LED spec is given) so tech.leds is left null. Repo references saintcon.org''s 2021 official MINIBADGE guide and github.com/lukejenkins/minibadge as prior art, not as a joint release.'
last_modified_date: '2026-09-07'
---

**rad-badge** is a SAINTCON 2022 minibadge made by GitHub user **then3rd**, built around an ATtiny85 microcontroller overclocked to 16MHz via custom fuse settings. The maker describes it as a "fake light-reactive Geiger counter & MIDI player" — a playful prototype rather than a real radiation sensor, built and documented in a hurry ("cobbled together at the last minute") as a learning project.

The badge plays MIDI songs that are converted to C byte arrays with the `xxd` utility and compiled into the firmware; the README points to musicboxmaniacs.com as a source of compatible MIDI files. Programming and fuse-setting are done over USB with a USBasp programmer using PlatformIO in VSCode.

## Make your own

The full hardware (PCB, schematic) and firmware are published in the GitHub repo at https://github.com/then3rd/rad-badge. To build one: install VSCode with the PlatformIO extension, connect a USBasp ICSP programmer to the ATtiny85, run the `Set Fuses` target once to enable 16MHz operation, then build and upload the firmware. Custom MIDI songs can be added by converting a `.midi` file with `xxd -i yoursong.midi > midi/yoursong.h` and including it in `midiplay.h` before reflashing.
