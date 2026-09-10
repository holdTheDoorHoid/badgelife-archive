---
title: Hello-My-Name-Is-PCB-Badge
id: other-hello-my-name-is-pcb-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 0
makers:
- name: MitchellStride
  url: https://github.com/MitchellStride
summary: A personal
functions: Displays graphics/animations on an onboard OLED screen and drives RGB LEDs via buttons; runs MicroPython on an RP2040. No CTF or game described.
look:
  colors: []
  shape: rectangle
  themes:
  - meme
  - hardware tool
tech:
  mcu: RP2040
  leds:
    count: null
    type: RGB
    note: Maker notes the RGB LEDs were run out of spec at 3.3V and behaved unreliably in v1.
  display: OLED
  connectivity: []
  inputs:
  - buttons
  battery: 2x AA (with boost converter; v1 boost converter untested, unit used USB power instead)
  sao_version: null
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Not sold; a personal project the maker made for themself and local hardware meetups.
make_your_own:
  open_source: true
  hardware_url: https://github.com/MitchellStride/Hello-My-Name-Is-PCB-Badge/tree/main/hello_my_name_is
  firmware_url: https://github.com/MitchellStride/Hello-My-Name-Is-PCB-Badge/tree/main/hello_my_name_is/software
  gerbers_url: https://github.com/MitchellStride/Hello-My-Name-Is-PCB-Badge/tree/main/hello_my_name_is/gerbers
  bom_url: https://github.com/MitchellStride/Hello-My-Name-Is-PCB-Badge/tree/main/hello_my_name_is/bom
  eda_tool: KiCad
  license: CERN-OHL-S-2.0
  fab_url: null
  notes: Firmware is written in MicroPython.
links:
- label: github.com/MitchellStride/Hello-My-Name-Is-PCB-Badge
  url: https://github.com/MitchellStride/Hello-My-Name-Is-PCB-Badge
  kind: repo
images:
- file: assets/images/badges/other/hello-my-name-is-pcb-badge/5df7c24cbd.png
  source: https://github.com/MitchellStride/Hello-My-Name-Is-PCB-Badge
  credit: Mitchell Stride
  caption: Badge render, top and bottom
- file: assets/images/badges/other/hello-my-name-is-pcb-badge/70963587c8.png
  source: https://github.com/MitchellStride/Hello-My-Name-Is-PCB-Badge
  credit: Mitchell Stride
  caption: Assembled test PCB, missing front buttons
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/MitchellStride/Hello-My-Name-Is-PCB-Badge
  title: Hello-My-Name-Is-PCB-Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://raw.githubusercontent.com/MitchellStride/Hello-My-Name-Is-PCB-Badge/main/README.md
  title: 'README: "Hello My Name Is" PCB Badge'
  accessed: '2026-09-07'
  note: Primary source for description, features (RP2040, OLED, RGB LEDs, buttons, SAO connector, 2x AA power), v1 issues, and v2 wishlist.
- kind: url
  url: https://raw.githubusercontent.com/MitchellStride/Hello-My-Name-Is-PCB-Badge/main/LICENSE.md
  title: LICENSE.md
  accessed: '2026-09-07'
  note: Confirms CERN-OHL-S-2.0 hardware license.
- kind: url
  url: https://api.github.com/repos/MitchellStride/Hello-My-Name-Is-PCB-Badge/contents/hello_my_name_is
  title: Repository file listing
  accessed: '2026-09-07'
  note: Confirms presence of KiCad source, gerbers, and BOM directories.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This is a personal #badgelife project, not made for a specific convention — the maker describes it as a test PCB for future art-PCB circuits and something to bring to local hardware meetups. No event, price, quantity, or distribution details are given because it was never sold or distributed; it appears to be a one-off the maker built and photographed for themself. Event left as "other" since no con/year is named anywhere in the repo. LED count not stated. SAO version (v1 vs v1.69bis/v2 pinout) not specified in the README.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/hello-my-name-is-pcb-badge.glb
  method: kicad
  source_file: hello_my_name_is/hello_my_name_is.kicad_pcb
  generated: '2026-09-10'
  bytes: 277100
---

Hello-My-Name-Is is a personal #badgelife PCB badge designed by Mitchell Stride, built to try out circuit ideas ahead of future art PCBs and to bring along to local hardware meetups rather than for any particular convention. It runs on a Raspberry Pi RP2040 (dual-core Cortex-M0+) with MicroPython firmware, and combines an OLED screen, RGB LEDs, and buttons behind a SAO connector. Power comes from 2x AA batteries through a boost converter, with a USB-C fallback the maker used exclusively while testing since the AA boost circuit was unverified.

The maker is candid that this first version was rushed — the schematic took a few nights and the layout a few hours with no review — and lists several known issues: the RGB LEDs, run at an out-of-spec 3.3V after the maker tried to replicate another badgelife design online, worked only intermittently, and the AA boost converter was never tested. A test unit shown in the repo photos is also missing its front buttons. The README lays out a v2 wishlist (a dedicated power/user LED, a buzzer, USB CC resistors, better battery-terminal anchoring, a level shifter for the RGB LEDs, and a smaller SAO footprint), though the maker states no v2 spin is currently planned.

## Make your own

The GitHub repository publishes the full KiCad project (schematic, PCB, backups), manufacturing gerbers, and a bill of materials, all under the CERN-OHL-S-2.0 strongly-reciprocal open hardware license, alongside the MicroPython firmware. The maker notes the design is built around JLCPCB's basic SMT parts library for easy assembly, and partial assembly of the reviewed unit was done through JLCPCB's own SMT service.
