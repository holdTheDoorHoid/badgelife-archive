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
  - measurement
  - hardware tool
  - minimalist
tech:
  mcu: ATtiny85
  leds: null
  display: none
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
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched the README, the GitHub repo page/metadata, and the schematic/PCB/assembly images directly from then3rd/rad-badge and confirmed maker, event/year (repo description literally reads "Saintcon 2022 Minibadge"), ATtiny85 MCU at 16MHz via custom fuses, the MIDI-conversion (xxd) and USBasp/PlatformIO programming workflow, and open-source hardware+firmware in one repo. The two saved images are byte-identical in content to images/assembly.jpeg and images/pcb.jpeg in the repo (only re-encoded), confirming they show this item. Corrected tech.connectivity from [usb] to [] (empty): the README''s "USB" reference is to the USBasp programmer tool used to flash the chip over ICSP/SPI, not a USB port on the badge itself; the schematic shows only SPI programming test points (MOSI/MISO/SCK/RST) and SDA/SCL/VBATT lines to the host badge connector, no USB. Corrected look.themes: replaced "radio" (radio-communications theme) with "measurement", since the badge simulates a Geiger counter / radiation-measurement device, not a radio; "radio" was likely a radiation/radio mix-up. Confidence raised to high per the guide''s definition (the maker''s own repo/README/schematic directly confirmed the core facts) even though only one source exists; no press coverage, storefront, or Hackaday post was found for this prototype, so price, quantity, and distribution/availability correctly remain empty and LED count/type remains null (not itemized as a spec in the README).'
last_modified_date: '2026-09-07'
---

**rad-badge** is a SAINTCON 2022 minibadge made by GitHub user **then3rd**, built around an ATtiny85 microcontroller overclocked to 16MHz via custom fuse settings. The maker describes it as a "fake light-reactive Geiger counter & MIDI player" — a playful prototype rather than a real radiation sensor, built and documented in a hurry ("cobbled together at the last minute") as a learning project.

The badge plays MIDI songs that are converted to C byte arrays with the `xxd` utility and compiled into the firmware; the README points to musicboxmaniacs.com as a source of compatible MIDI files. Programming and fuse-setting are done over USB with a USBasp programmer using PlatformIO in VSCode.

## Make your own

The full hardware (PCB, schematic) and firmware are published in the GitHub repo at https://github.com/then3rd/rad-badge. To build one: install VSCode with the PlatformIO extension, connect a USBasp ICSP programmer to the ATtiny85, run the `Set Fuses` target once to enable 16MHz operation, then build and upload the firmware. Custom MIDI songs can be added by converting a `.midi` file with `xxd -i yoursong.midi > midi/yoursong.h` and including it in `midiplay.h` before reflashing.
