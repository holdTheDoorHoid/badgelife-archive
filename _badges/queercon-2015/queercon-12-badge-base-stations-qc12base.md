---
title: Queercon 12 badge base stations (qc12base)
id: queercon-2015-queercon-12-badge-base-stations-qc12base
layout: badge
parent: Queercon 12 (2015)
grand_parent: Badge Archive
nav_exclude: true
type: other
event: queercon-2015
year: 2015
makers:
- name: George Louthan (duplico)
  url: https://github.com/duplico
summary: Fixed RF "base station" units built to accompany the Queercon 12 (2015) electronic
  badge, driving OLED animations and talking to attendees' badges over radio rather than
  being worn themselves.
functions: Runs OLED display animations, drives onboard LEDs, and communicates with nearby
  Queercon 12 badges over an RFM-style sub-GHz radio link (the same neighbor-interaction
  system used by the QC12 badge itself).
look:
  colors: []
  shape: null
  themes:
  - radio
tech:
  mcu: MSP430FR5949
  leds: null
  display: OLED
  connectivity:
  - sub-ghz
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
  hardware_url: https://github.com/duplico/qc12base
  firmware_url: https://github.com/duplico/qc12base
  eda_tool: null
links:
- label: github.com/duplico/qc12base
  url: https://github.com/duplico/qc12base
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'Sweep title matched the maker''s own repo name ("Queercon 12 badge base stations"); no rewording needed.'
- Not a worn badge/SAO — this is infrastructure hardware built to run alongside the
  Queercon 12 (QC12) attendee badge (see the separate entry for that badge). No price,
  quantity, or distribution info applies since it was never sold or given to attendees.
- No photos of the physical unit were found; the repo's images/ folder holds raw animation
  frame data (.txt), not device photos.
status: released
sources:
- kind: url
  url: https://github.com/duplico/qc12base
  title: Queercon 12 badge base stations (qc12base)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://raw.githubusercontent.com/duplico/qc12base/master/README
  title: qc12base README
  accessed: '2026-09-10'
  note: Confirms hardware/animation/software licensing (CC BY-SA 4.0 hardware and
    animations, BSD 3-clause software); no quantity, price, or distribution details given.
- kind: url
  url: https://raw.githubusercontent.com/duplico/qc12base/master/radio.h
  title: qc12base radio.h
  accessed: '2026-09-10'
  note: Radio driver uses an RFM-style register map (RFM_FIFO, RFM_OPMODE, etc.), indicating
    a HopeRF RFM-family sub-GHz radio module for badge-to-base communication.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Maker's own repo confirms the project is real, its MCU (MSP430FR5949, from the
    linker script filename), OLED display, LED control, and RFM-style sub-GHz radio
    firmware. No maker post, price, quantity built, or hardware photos were found anywhere
    online, so those fields stay empty. This is companion infrastructure for the separate
    Queercon 12 (QC12) badge entry, not a wearable itself, so get_one fields largely do
    not apply.
last_modified_date: '2026-09-10'
---

George Louthan (duplico) built a small number of "base station" units to run alongside the Queercon 12 (2015) electronic badge he designed. Rather than being worn by attendees, these units were fixed hardware — likely placed around the event space — running OLED animations and LED effects while talking to nearby attendee badges over the same RFM-style sub-GHz radio link the QC12 badge used for its neighbor-interaction features.

The base stations run on an MSP430FR5949 microcontroller, the same firmware ecosystem (grlib graphics library, custom fonts, image assets) as duplico's badge projects of that era. Hardware and animation assets are released under CC BY-SA 4.0, and the firmware under a BSD 3-clause license, but no build log, price, quantity-made, or distribution details were published, and no photos of the physical units turned up in the repository or in web searches.

## Make your own

The firmware and hardware design are published at [github.com/duplico/qc12base](https://github.com/duplico/qc12base) under CC BY-SA 4.0 (hardware/animations) and BSD 3-clause (software). The repo includes the OLED driver, LED control code, radio driver, and animation/image assets, but no separate schematic, BOM, or Gerber files were found alongside the source.
