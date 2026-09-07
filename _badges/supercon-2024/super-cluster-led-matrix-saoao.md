---
title: Super Cluster (LED matrix SAOAO)
id: supercon-2024-super-cluster-led-matrix-saoao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
summary: A passive SAO with 32 discrete 0805 LEDs wired in a grid, submitted to davedarko's YoDawgSAO collection for Hackaday Supercon 8's add-on contest.
functions: Lights up when plugged into a host badge's SAO header; no microcontroller, so any animation comes from how the LED strings are wired/powered rather than software.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - minimalist
tech:
  mcu: none
  leds:
    count: 32
    type: discrete
    note: 32x Device:LED footprints in LED_SMD 0805 package, arranged with 4 series resistors (R1-R4) rather than an LED driver chip.
  display: LED matrix (32 discrete LEDs)
  connectivity: []
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
  open_source: yes
  hardware_url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/super_computer_custer_0805
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/YoDawgSAO/tree/master/badges/super_computer_custer_0805
  url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/super_computer_custer_0805
  kind: repo
- label: davedarko/YoDawgSAO (repo root README)
  url: https://github.com/davedarko/YoDawgSAO
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/super_computer_custer_0805
  title: Super Cluster (LED matrix SAOAO)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''supercon-2024''.'
- kind: url
  url: https://github.com/davedarko/YoDawgSAO
  title: 'YoDawgSAO README: "Yo Dawg, I heard you like add-ons on your badges?"'
  accessed: '2026-09-07'
  note: Repo README confirms the whole YoDawgSAO collection (including this sub-badge) was made for the Hackaday Supercon 8 (2024) SAO/add-on contest, and gives the 19mm x 19mm / 1.27mm GND-VCC-GND header constraint shared by all badges in it.
- kind: url
  url: https://raw.githubusercontent.com/davedarko/YoDawgSAO/master/badges/super_computer_custer_0805/super_computer_custer_0805.kicad_sch
  title: super_computer_custer_0805.kicad_sch (raw KiCad schematic)
  accessed: '2026-09-07'
  note: Schematic lists 32 Device:LED symbols (D1-D32) in LED_SMD 0805 footprints, 4 resistors (R1-R4), and a single Conn_01x03_Socket (J1) for the GND-VCC-GND SAO header - no microcontroller or driver IC present.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The repo has no README, photo, or render specific to this sub-badge (only the KiCad source and gerber zip), so price, quantity, and availability could not be confirmed - it's unclear whether it was ever fabricated/distributed beyond the shared design files. The name "super_computer_custer_0805" is presumably a pun on "super computer cluster" built from 0805-package LEDs, matching the "Super Cluster" title on the community sheet. Event and year are inferred from the parent repo's README, which states the whole collection was made for Supercon 8's 2024 add-on contest, not from anything specific to this individual badge.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/super-cluster-led-matrix-saoao/
---

Super Cluster is one of several small add-ons in davedarko's YoDawgSAO collection, a set of simple, low-effort SAOs made for Hackaday Supercon 8's 2024 add-on contest as a counterpoint to more elaborate microcontroller-driven entries. Like the other boards in the collection, it follows the contest's 19mm x 19mm size limit and connects to a host badge through a 1.27mm-pitch three-pin GND-VCC-GND header.

The board itself, named `super_computer_custer_0805` in the repository (likely a pun on "super computer cluster" built from 0805-package parts), is a fully passive design: its schematic shows 32 discrete LEDs in 0805 SMD footprints wired through four series resistors, with no microcontroller or LED driver IC anywhere on the board. Powered from the host badge's SAO header, the LEDs simply light up in whatever pattern their wiring dictates - there is no firmware to program.

## Make your own

KiCad schematic, PCB, and project files, plus a pre-generated fabrication-toolkit gerber zip, are published in the `badges/super_computer_custer_0805` folder of the [YoDawgSAO repository](https://github.com/davedarko/YoDawgSAO/tree/master/badges/super_computer_custer_0805). No BOM or assembly instructions specific to this board were found beyond the schematic itself.
