---
title: Supercomputer Cluster SAOAO
id: supercon-2024-yo-dawg-saoao-supercomputer-cluster
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://hackaday.io/davedarko
summary: A 19x19 mm supercomputer-cluster themed Simple Add-on Add-on (SAOAO) built entirely from 0805 LEDs and resistors, made for davedarko's Yo Dawg SAO project at the Supercon 2024 add-on contest.
functions: 'Self-blinking LEDs meant to mimic the flickering status lights of a rack of computers; no microcontroller, driven directly off the SAOAO connector.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: none
  leds:
    count: 32
    type: discrete
    note: 0805 package LEDs (self-blinking type per the maker's log), arranged with 4 series resistors; no driver IC.
  display: null
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: free
  price_usd: null
  quantity: '10'
  availability: free
  distribution:
  - free_drop
  - contest
  where: Handed out/traded at Supercon 2024 alongside the rest of the Yo Dawg SAOAO batch; the maker brought extras and encouraged attendees to make their own from the published files.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/davedarko/YoDawgSAO/tree/main/badges/super_computer_custer_0805
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/YoDawgSAO
  url: https://github.com/davedarko/YoDawgSAO
  kind: repo
- label: hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  kind: hackaday
images:
- file: assets/images/badges/supercon-2024/yo-dawg-saoao-supercomputer-cluster/79e728088a.png
  source: "https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao/log/233282-i-dont-think"
  credit: "davedarko"
  caption: "Bare, unpopulated SAOAO PCBs fresh from fabrication, including the supercomputer-cluster design"
- file: assets/images/badges/supercon-2024/yo-dawg-saoao-supercomputer-cluster/9c82b683d8.jpg
  source: "https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao/log/233282-i-dont-think"
  credit: "davedarko"
  caption: "Assembled, working Simple Add-on Add-ons from the same batch, LEDs lit"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/YoDawgSAO
  title: davedarko/YoDawgSAO - Simple Add-on Add-ons
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/davedarko/YoDawgSAO/tree/main/badges/super_computer_custer_0805
  title: badges/super_computer_custer_0805 folder
  accessed: '2026-09-07'
  note: Confirmed the KiCad files for this specific themed SAOAO; sole commit is by davedarko.
- kind: url
  url: https://raw.githubusercontent.com/davedarko/YoDawgSAO/main/badges/super_computer_custer_0805/super_computer_custer_0805.kicad_sch
  title: super_computer_custer_0805.kicad_sch (raw)
  accessed: '2026-09-07'
  note: "Schematic symbol count gives parts: 32x Device:LED, 4x Device:R, one 3-pin SAOAO connector, no MCU."
- kind: url
  url: https://raw.githubusercontent.com/davedarko/YoDawgSAO/main/README.md
  title: YoDawgSAO README
  accessed: '2026-09-07'
  note: Project background - 19x19mm size, 1.27mm 3-pin GND-VCC-GND header, made for the Supercon 2024 (Supercon 8) add-on contest.
- kind: url
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao/log/233282-i-dont-think
  title: "Yo Dawg SAO project log: \"I don't think\" (09/30/2024)"
  accessed: '2026-09-07'
  note: Maker's own account that 10 "supercomputer" boards were made using self-blinking LEDs, alongside 100 baseplates, hackaday-logo, Iron Man, and hackspace-logo variants; source of both saved photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The repo folder (super_computer_custer_0805) and commit history confirm davedarko as the sole author of the design files, and the schematic confirms the 32-LED/4-resistor, no-MCU part count. However, no page individually names or photographs this specific themed board apart from the general project photos of the whole SAOAO batch (bare PCBs and assembled/lit boards), so the two saved images show the batch rather than a confirmed close-up of this exact design. Price is listed as free/contest giveaway per the project's general distribution model; no separate storefront listing was found for this specific SAO.
last_modified_date: '2026-09-07'
---

Part of davedarko's "Yo Dawg SAO" project for the Supercon 2024 (Supercon 8) add-on contest, the Supercomputer Cluster SAOAO is one of several small themed boards (alongside an Iron Man design, a Hackaday logo, and a hackspace logo) built to the project's "SAOAO" standard: a 19x19 mm add-on for an add-on, connecting to a host SAO baseplate through a 1.27 mm, 3-pin GND-VCC-GND header rather than I2C. Its schematic is entirely passive - 32 LEDs and 4 resistors in 0805 packages, with no microcontroller - using LEDs the maker described as "self blinking" to suggest the flickering status lights of a rack of servers without needing any driving logic.

Davedarko had roughly ten of these fabricated in a batch that also included 100 Yo Dawg baseplates and a mix of the other themed SAOAOs, and brought them to Supercon 2024 to hand out, while publishing the KiCad source so other attendees could fabricate their own from the same files. No dedicated storefront listing, price, or individual photo of this specific board (separate from the general project batch) was found; the two images saved here show the wider SAOAO batch arriving from fabrication and later assembled and lit.

## Make your own

The KiCad schematic, PCB layout, and a pre-generated production/fabrication folder (including a JLCPCB-style netlist and a Gerber zip) are in the `badges/super_computer_custer_0805` folder of the [YoDawgSAO GitHub repo](https://github.com/davedarko/YoDawgSAO/tree/main/badges/super_computer_custer_0805). It follows the same 19x19 mm / 3-pin SAOAO header spec documented in the repo's main README.
