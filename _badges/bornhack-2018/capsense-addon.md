---
title: CapSense_addon
id: bornhack-2018-capsense-addon
layout: badge
parent: BornHack 2018
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: bornhack-2018
year: 2018
makers:
- name: Thomas Flummer
  url: https://github.com/flummer
summary: A capacitive-sensing breakout board designed to plug into the BornHack 2018 badge, built around a Texas Instruments FDC1004 capacitance-to-digital converter.
functions: Reads capacitive touch/proximity via the FDC1004 over I2C; six single-pin headers break out sense channels, likely for external electrodes or touch pads.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - measurement
tech:
  mcu: none
  leds: null
  display: null
  connectivity:
  - i2c
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
  open_source: partial
  hardware_url: https://github.com/bornhack/badge2018/tree/breakoutboards/CapSense_addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bornhack/badge2018/tree/breakoutboards/CapSense_addon
  url: https://github.com/bornhack/badge2018/tree/breakoutboards/CapSense_addon
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
status: listed
sources:
- kind: url
  url: https://github.com/bornhack/badge2018/tree/breakoutboards/CapSense_addon
  title: CapSense_addon
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://api.github.com/repos/bornhack/badge2018/contents/CapSense_addon?ref=breakoutboards
  title: 'GitHub API: CapSense_addon directory listing'
  accessed: '2026-09-10'
  note: Confirmed the folder holds only KiCad design files (schematic, PCB, netlist, project file) and no README or images.
- kind: url
  url: https://raw.githubusercontent.com/bornhack/badge2018/breakoutboards/CapSense_addon/CapSense_addon.sch
  title: CapSense_addon.sch (raw schematic)
  accessed: '2026-09-10'
  note: Identified the FDC1004 capacitance-to-digital IC, SDA/SCL (I2C) connections, a 2x2 header, and six single-pin sense headers.
- kind: url
  url: https://api.github.com/repos/bornhack/badge2018/commits?path=CapSense_addon&sha=breakoutboards
  title: 'GitHub API: commit history for CapSense_addon'
  accessed: '2026-09-10'
  note: Single commit, "Initial version," by Thomas Flummer (github.com/flummer), 2018-07-26 - identifies the designer.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Design files only (KiCad schematic, PCB, netlist, project file) on the `breakoutboards` branch of bornhack/badge2018; no README, no renders or photos, and no evidence found that it was ever fabricated, sold, or distributed to attendees - it may have stayed a design exercise. The schematic names the IC as a Semiconductors:FDC1004 (TI capacitance-to-digital converter) with SDA/SCL breakouts and a 2x2 connector matching the badge's breakout-board pattern seen on sibling entries (Blinky_addon, LED_addon). Maker attribution comes from the sole git commit author, not a byline on the page itself, so confidence is medium rather than high. No pricing, quantity, or availability information exists anywhere in the repo.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bornhack-2018/capsense-addon.glb
  method: kicad
  source_file: CapSense_addon/CapSense_addon.kicad_pcb
  generated: '2026-09-10'
  bytes: 63160
---

CapSense_addon is a capacitive-sensing breakout board for the BornHack 2018 badge, built around Texas Instruments' FDC1004 capacitance-to-digital converter. It communicates over I2C (SDA/SCL) and breaks out six individual sense channels via single-pin headers, presumably for wiring up external touch pads or electrodes, while a 2x2 connector ties it to the main badge - the same connector style used by the other BornHack 2018 breakout boards (Blinky_addon, LED_addon).

The board lives on the `breakoutboards` branch of the `bornhack/badge2018` GitHub repository as a single commit, "Initial version," from Thomas Flummer (BornHack's badge designer) on 2018-07-26. Only the KiCad design files are present - schematic, PCB layout, netlist, and project file - with no README, no photos or renders, and no mention on the community badge sheet of it being built, kitted, or handed out. It reads as a design exercise or one-off experiment alongside BornHack's other badge add-ons rather than a badge that saw wide distribution.

## Make your own

The KiCad source (schematic and PCB layout) is published in the repository linked above, but there is no bill of materials, firmware, or build write-up - anyone reproducing it would need to source the FDC1004 and match up the six sense-channel headers themselves.
