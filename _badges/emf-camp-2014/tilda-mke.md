---
title: TiLDA MKe
id: emf-camp-2014-tilda-mke
layout: badge
parent: EMF Camp 2014
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: emf-camp-2014
year: 2014
makers:
- name: EMF Camp badge team
summary: The official badge of EMF Camp 2014, an Arduino Due-compatible board with a backlit LCD, wireless radio, and an accelerometer, distributed to every attendee.
functions: Runs Arduino-based sketches; used for on-camp apps and games, wireless (Ciseco SRF) communication between badges, and as a general hackable dev board with IR, accelerometer/gyro, and onboard flash storage.
look:
  colors: []
  shape: null
  themes:
  - wearable
  - hardware tool
tech:
  mcu: ARM (Arduino Due compatible)
  leds:
    count: 2
    type: RGB
    note: Two front-facing RGB LEDs, plus separate RX/TX indicator LEDs
  display: 128x64 backlit LCD (JHD12864)
  connectivity:
  - ir
  battery: Rechargeable battery, MicroUSB charging; can run on USB power alone
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to every EMF Camp 2014 attendee
make_your_own:
  open_source: true
  hardware_url: https://github.com/emfcamp/TiLDA
  firmware_url: https://github.com/emfcamp/TiLDA-source
  eda_tool: null
links:
- label: badge.emfcamp.org/TiLDA_MKe
  url: https://badge.emfcamp.org/TiLDA_MKe/
  kind: website
- label: www.wikiwand.com/en/articles/Electromagnetic_Field_(festival)
  url: https://www.wikiwand.com/en/articles/Electromagnetic_Field_(festival)
  kind: website
- label: github.com/emfcamp/TiLDA
  url: https://github.com/emfcamp/TiLDA
  kind: repo
- label: github.com/emfcamp/TiLDA-source
  url: https://github.com/emfcamp/TiLDA-source
  kind: repo
images:
- file: assets/images/badges/emf-camp-2014/tilda-mke/afcdf4c053.jpg
  source: https://badge.emfcamp.org/TiLDA_MKe/
  credit: EMF Camp badge team
  caption: TiLDA MKe badge, front view
- file: assets/images/badges/emf-camp-2014/tilda-mke/04332c09bc.jpg
  source: https://badge.emfcamp.org/TiLDA_MKe/
  credit: EMF Camp badge team
  caption: TiLDA MKe badge, back view
contact: {}
notes:
- Official EMF Camp 2014 badge, an Arduino Due-compatible board (codenamed "ElectroMagnetic Boogaloo") and the first EMF badge with an LCD screen; not yet in the archive. Found by the event-year sweep, task emf-badges.
status: released
sources:
- kind: url
  url: https://badge.emfcamp.org/TiLDA_MKe/
  title: TiLDA MKe
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-badges); event read as ''emf-camp-2014''.'
- kind: url
  url: https://github.com/emfcamp/TiLDA
  title: GitHub - emfcamp/TiLDA
  accessed: '2026-09-08'
  note: Hardware/documentation repository for TiLDA MKe; confirms open-source hardware.
- kind: url
  url: https://github.com/emfcamp/TiLDA-source
  title: Source code for TiLDA badges during EMF
  accessed: '2026-09-08'
  note: Firmware source repository for the TiLDA badge line, including MKe.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Confirmed via the maker's own documentation site (badge.emfcamp.org) and the emfcamp GitHub org. Price and quantity made were not stated anywhere found; left empty. No SAO header (this predates the SAO convention) so tech.sao_version left null. Wireless radio module (Ciseco SRF) and optional ethernet breakout are mentioned in docs but no controlled-vocabulary connectivity tag fits cleanly (not wifi/ble/lora/etc.); noted here instead of forcing a mismatch. Colors and shape not stated on the documentation pages; left empty.
last_modified_date: '2026-09-10'
model:
  file: assets/models/emf-camp-2014/tilda-mke.glb
  method: kicad
  source_file: TiLDE.brd
  generated: '2026-09-10'
  bytes: 314308
---

The TiLDA MKe was the official badge handed to every attendee of EMF Camp 2014, the UK hacker camp. Built around an Arduino Due-compatible ARM board (internally nicknamed "ElectroMagnetic Boogaloo"), it was the first EMF badge to include an LCD screen — a 128x64 backlit display — alongside two front-facing RGB LEDs, a piezo buzzer, an MPU-6050 accelerometer/gyroscope, an IR transceiver, onboard flash storage, and a Ciseco SRF wireless radio module for badge-to-badge communication. It charged over MicroUSB and could also run directly from USB power.

Like the rest of the TiLDA line, the MKe was fully open source: hardware documentation and schematics live in the `emfcamp/TiLDA` GitHub repository, with badge firmware in the separate `emfcamp/TiLDA-source` repo. The badge was designed to double as a general-purpose Arduino-compatible dev board attendees could keep hacking on after the event, and it was succeeded by the TiLDA Mk3 (EMF Camp 2016) and TiLDA Mk4 (EMF Camp 2018).

## Make your own

Hardware files and documentation are on GitHub at `github.com/emfcamp/TiLDA`; firmware source is in the companion `github.com/emfcamp/TiLDA-source` repository. See `badge.emfcamp.org/TiLDA_MKe/` for the original build documentation and setup instructions.
