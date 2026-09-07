---
title: Hubble SAO
id: supercon-2024-hubble-sao-2
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: pdulab
  url: https://hackaday.io/pdulab
summary: A Simple Add-On shaped like the Hubble Space Telescope, entered in the Supercon 8 (2024) SAO Contest, carrying a VEML3328 one-pixel RGB+IR camera, an LSM6DSO IMU, four BPW34 photodiodes as solar panels, an IR LED for wireless data, a yellow LED, a button and an ATmega328PB; the maker notes the published revision still has hardware bugs (reversed IR LED driver FET, wrong SAO connector footprint, ATmega328PB SPI pin assumption).
functions: 'Uses the VEML3328 as a one-pixel RGB+IR "camera"; the LSM6DSO IMU senses orientation/motion (the maker notes only one gyroscope axis works, a nod to the real Hubble telescope''s own gyro failures); four BPW34 photodiodes stand in for solar panels and read out via the ADC; an IR LED sends data wirelessly; a yellow LED and button provide basic UI.'
look:
  colors: []
  shape: spaceship
  themes:
  - space
  - sci-fi
tech:
  mcu: ATmega328PB
  leds:
    count: 1
    type: discrete
    note: single yellow LED
  display: none
  connectivity:
  - ir
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '3 PCBs assembled'
  availability: not_released
  distribution: []
  where: 'Not sold; shared as an open-source project. Only three boards were built and the design was archived before Supercon due to hardware bugs found too late to fix.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/pdulab/hubble_sao
  firmware_url: https://github.com/pdulab/hubble_sao
  eda_tool: KiCad
  license: CC BY-NC-SA 4.0
  notes: 'Repo includes KiCad design files and 3D model files; maker documents known bugs in the published revision (see summary).'
links:
- label: hackaday.io/project/198447-hubble-sao
  url: https://hackaday.io/project/198447-hubble-sao
  kind: hackaday
- label: github.com/pdulab/hubble_sao
  url: https://github.com/pdulab/hubble_sao
  kind: repo
images:
- file: assets/images/badges/supercon-2024/hubble-sao-2/029e8ece88.jpg
  source: "https://hackaday.io/project/198447-hubble-sao"
  credit: "pdulab"
  caption: "Hubble SAO assembled board"
contact: {}
notes: []
status: cancelled
sources:
- kind: url
  url: https://hackaday.io/project/198447-hubble-sao
  title: Hubble SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/198447-hubble-sao
  title: Hubble SAO - Hackaday.io
  accessed: '2026-09-07'
  note: Maker's project page; confirmed event (Supercon 8/2024), features, chip, sensors, quantity built (3 PCBs), and that it was archived before the con due to hardware bugs.
- kind: url
  url: https://github.com/pdulab/hubble_sao
  title: pdulab/hubble_sao
  accessed: '2026-09-07'
  note: Confirmed hardware/firmware are open source (KiCad files, 3D models), CC BY-NC-SA 4.0 license, and functional details (IMU quirk, photodiodes as solar panels).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own Hackaday.io page and GitHub repo both confirm the core facts. No storefront exists; only 3 PCBs were assembled and the project was never sold or completed for the con floor, so price/quantity-sold/availability fields beyond "not_released" are left empty. LED count/type is inferred as a single generic yellow LED per the maker''s description; no addressable LED type is mentioned. sao_version (pin count) is not stated anywhere, despite the maker noting the SAO connector footprint on the board was wrong.'
last_modified_date: '2026-09-07'
---

The Hubble SAO is a Simple Add-On shaped like the Hubble Space Telescope, built by pdulab for the Supercon 8 (2024) SAO Contest. Rather than just looking the part, it plays with the telescope's real quirks: a VEML3328 sensor acts as a one-pixel RGB+IR "camera," an LSM6DSO IMU stands in for the telescope's gyroscopes (the maker notes that, fittingly, only one axis works on their board, echoing the real Hubble's history of gyro failures), and four BPW34 photodiodes wired to the microcontroller's ADC represent its solar panels. An IR LED provides a simple wireless data link, backed by an ATmega328PB, a yellow status LED, and a button.

The board was ambitious on the soldering front too, mixing 1206 and 0805 passives with SOIC-8, 32-pin TQFP, and even LGA packages. Only three PCBs were built and partially assembled, and the maker found several hardware bugs too late to fix before Supercon: a reversed MOSFET on the IR LED driver, an incorrect SAO connector footprint, and a conflict between the ATmega328PB's SPI programming pins. As a result the project was archived rather than brought to the con or sold, and shared purely for reference. Hardware (KiCad files and 3D models) and firmware are published on GitHub under CC BY-NC-SA 4.0.

## Make your own

The GitHub repo (github.com/pdulab/hubble_sao) has the KiCad schematic/PCB files and 3D model files needed to reproduce the board, along with the firmware source. Anyone building from it should be aware of the documented bugs above before fabricating a board.
