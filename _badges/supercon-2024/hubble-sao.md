---
title: Hubble SAO
id: supercon-2024-hubble-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: pdulab
  url: https://github.com/pdulab
summary: A Hubble Space Telescope themed SAO built for Supercon 2024 with an ATmega328PB, a VEML3328 1x1-pixel RGB+IR optical sensor, an LSM6DSO IMU, four BPW34 photodiodes standing in for the solar panels, an IR LED for wireless data, a yellow LED and a button, released under CC BY-NC-SA 4.0.
functions: 'Reads ambient light/color via the VEML3328 optical sensor, tracks orientation with the LSM6DSO IMU (accel + gyro), senses IR via four BPW34 photodiodes wired to the microcontroller''s ADC, and can send wireless data over its IR LED. A yellow LED and a button round out the blinky/interactive side.'
look:
  colors: []
  shape: null
  themes:
  - space
  - sci-fi
tech:
  mcu: ATmega328PB
  leds:
    count: 1
    type: discrete
    note: One yellow indicator LED, plus a separate IR LED used for wireless data transmission.
  display: none
  connectivity:
  - ir
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
  open_source: partial
  hardware_url: https://github.com/pdulab/hubble_sao/tree/main/KiCAD_files
  firmware_url: null
  eda_tool: KiCad
  license: CC BY-NC-SA 4.0
  notes: 'Repo also includes 3D models (FreeCAD/STEP/STL/WRL) for the optical sensor and photodiode components under 3d_models/. No firmware source was found in the repository at the time of review.'
links:
- label: github.com/pdulab/hubble_sao
  url: https://github.com/pdulab/hubble_sao
  kind: repo
- label: raw.githubusercontent.com/pdulab/hubble_sao/HEAD/README.md
  url: https://raw.githubusercontent.com/pdulab/hubble_sao/HEAD/README.md
  kind: website
- label: github.com/pdulab
  url: https://github.com/pdulab
  kind: repo
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/pdulab/hubble_sao
  title: pdulab/hubble_sao - Hubble SAO for Supercon 2024
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://raw.githubusercontent.com/pdulab/hubble_sao/HEAD/README.md
  title: 'hubble_sao README: Features, License, Disclaimer'
  accessed: '2026-09-07'
  note: 'Primary source for feature list (VEML3328, LSM6DSO, 4x BPW34 photodiodes, IR LED, ATmega328PB, yellow LED, button) and the CC BY-NC-SA 4.0 license.'
- kind: url
  url: https://github.com/pdulab
  title: pdulab (GitHub profile)
  accessed: '2026-09-07'
  note: 'Confirmed maker identity and cross-referenced other Supercon-era projects (2025 Hackaday Communicator Badge clock app, a fork of the official Supercon RF Communicator Badge repo), supporting that pdulab is an active Supercon/Hackaday badge community participant.'
- kind: url
  url: https://api.github.com/repos/pdulab/hubble_sao/contents/
  title: pdulab/hubble_sao repository file listing
  accessed: '2026-09-07'
  note: 'Confirmed repo contains only KiCAD_files/ and 3d_models/ design files plus README/LICENSE; no photos of an assembled unit and no firmware source are present in the repository.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, event, MCU, sensors, license) confirmed directly from the maker''s own repo README. No pricing, quantity made, or distribution/availability details were found anywhere - this appears to be a personal/open-source SAO design rather than one that was sold, so those fields are left empty rather than guessed. No photos of the assembled SAO were found in the repo or elsewhere reachable; only KiCad/CAD design files exist, so no images could be saved. No firmware repository was found (README implies a microcontroller-driven design but only hardware files are published), so make_your_own.open_source is set to partial (hardware published, firmware not found).'
last_modified_date: '2026-09-07'
---

The Hubble SAO is a Hubble Space Telescope themed add-on badge (SAO) that pdulab built for Supercon 2024. It runs on an ATmega328PB and pairs a VEML3328 optical sensor (used as a 1x1-pixel RGB+IR camera) with an LSM6DSO IMU for orientation sensing - a nod to the real Hubble telescope's stabilization gyros. The maker notes wryly that only one of Hubble's gyroscopes still works correctly, and the SAO ships with exactly one gyro to match.

Four BPW34 infrared photodiodes, wired into the microcontroller's ADC, stand in for Hubble's solar panels, and an IR LED gives the board a way to send data wirelessly. A standard yellow LED and a push button round out the interactive features. The design files (KiCad schematic/PCB, plus 3D models for the optical sensor and photodiode footprints) are published on GitHub under a CC BY-NC-SA 4.0 license, making the hardware buildable by others for non-commercial use, though no firmware source is included in the repository.

No information was found on how many were made, whether it was sold or given away, or its price - the project reads as a personal/community build rather than a commercial release, and the guide's "never invent" rule means those fields are left blank rather than guessed.
