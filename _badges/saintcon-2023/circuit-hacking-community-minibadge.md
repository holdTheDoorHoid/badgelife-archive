---
title: Circuit Hacking Community Minibadge
id: saintcon-2023-circuit-hacking-community-minibadge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: hamster
  url: https://hamster.github.io/
  role: designer
- name: Yagoth
  role: community co-lead
summary: A pre-assembled analog-circuit minibadge handed out at SAINTCON 2023's Circuit Hacking Community booth, built around an RC time-constant and transistor demo.
functions: Demonstrates basic analog circuit design (an RC time-constant circuit and a transistor stage) as a teaching aid; distributed alongside booth activities using open-source logic analyzers to inspect SPI, I2C, and CAN bus traffic.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
  - puzzle
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: SAINTCON 2023 Circuit Hacking Community booth
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/hamster/SAINTCON/tree/main/CHC/2023
  firmware_url: null
  eda_tool: KiCad
links:
- label: saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  kind: website
- label: Circuit Hacking Community - SAINTCON 2023 (saintcon.zip mirror)
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/com-circuit-hacking-community/
  kind: website
- label: hamster/SAINTCON - CHC/2023 (KiCad source)
  url: https://github.com/hamster/SAINTCON/tree/main/CHC/2023
  kind: repo
images: []
contact: {}
notes:
- 2023 Circuit Hacking Community minibadge (github.com/hamster/saintcon), advanced-difficulty digital-circuit puzzle board. Found by the event-year sweep, task saintcon-2023.
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: Circuit Hacking Community Minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2023); event read as ''saintcon-2023''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/com-circuit-hacking-community/
  title: Circuit Hacking Community - SAINTCON 2023
  accessed: '2026-09-10'
  note: Confirms the community (led by hamster and Yagoth), its booth hours, activities (logic-analyzer protocol decoding, PCB/analog-circuit teaching), and that a pre-assembled minibadge with analog components (RC time constant, transistor) was available at the booth.
- kind: url
  url: https://github.com/hamster/SAINTCON/tree/main/CHC/2023
  title: hamster/SAINTCON repo, CHC/2023 folder
  accessed: '2026-09-10'
  note: Public KiCad project (chc.kicad_sch/kicad_pcb, MIT-licensed repo) confirming hamster designed this minibadge's hardware and that source files are published; no firmware present (board appears to be a passive/analog design, no MCU).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: >-
    Confirmed via SAINTCON's own event page and hamster's public GitHub repo (hamster/SAINTCON,
    folder CHC/2023, a KiCad project) that this minibadge is real and was designed by hamster for
    the Circuit Hacking Community (co-led with Yagoth) at SAINTCON 2023. Could not find price,
    quantity made, LED/display specs, colors, or a photo of the assembled board — the repo's
    images/ folder only holds vector/PNG logo art, not a board photo, and hamster's badge-museum
    site (hamster.github.io/badges) does not list a SAINTCON entry. The sweep's note citing
    "github.com/hamster/saintcon" as a repo name was close but the actual path is
    github.com/hamster/SAINTCON/tree/main/CHC. Left tech.leds, look.colors, and get_one.price/
    quantity empty rather than guess.
last_modified_date: '2026-09-10'
---

The Circuit Hacking Community was a SAINTCON 2023 booth led by hamster and Yagoth, teaching attendees the basics of digital circuit design and protocol decoding — PCB manufacturing and component types, common device protocols, and hands-on decoding of SPI, I2C, and CAN bus traffic using open-source logic analyzers. As part of the booth's activities, they handed out a pre-assembled minibadge built around simple analog components (an RC time-constant circuit and a transistor stage), meant as a low-barrier entry point for newcomers before they moved on to the logic-analyzer exercises.

The badge's hardware design is published as a KiCad project in hamster's `SAINTCON` GitHub repository, under `CHC/2023` (schematic, PCB layout, a panelized version, and footprint/library files), alongside separate logo artwork. No firmware is present in the repo, consistent with this being a passive analog demo board rather than a microcontroller-based badge.

No pricing, quantities made, or photos of the assembled board turned up during research; the repo's own image assets are logo art rather than product photos, and it does not appear in hamster's separate badge-museum catalog site.

## Make your own

The full KiCad source (schematic and PCB) is available at github.com/hamster/SAINTCON, under `CHC/2023`, including a panelized 1.0 layout and a pre-built Gerber/output archive (`chc-panel-1.0.zip`).
