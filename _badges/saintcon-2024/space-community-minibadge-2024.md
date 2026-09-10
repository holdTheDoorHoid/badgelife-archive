---
title: Space Community minibadge (2024)
id: saintcon-2024-space-community-minibadge-2024
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: SHIFTY
summary: A space-themed SAINTCON 2024 community minibadge, a small lit PCB pin with a space/spacecraft graphic.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - space
tech:
  mcu: 'none'
  leds:
    count: 2
    type: SMD
    note: Two 1206 SMD LEDs plus a series resistor on the board; no microcontroller (passive/battery-driven lighting).
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
  open_source: partial
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Space%20Community%20-%20SHIFTY
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/Space%20Community%20-%20SHIFTY
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Space%20Community%20-%20SHIFTY
  kind: repo
images:
  - file: assets/images/badges/saintcon-2024/space-community-minibadge-2024/e294abfa46.jpg
    source: "https://github.com/utahsaint-org/MiniBadges2024/tree/main/Space%20Community%20-%20SHIFTY"
    credit: "SHIFTY"
    caption: "Front copper/render of the Space Community minibadge PCB art"
contact: {}
notes:
- 2024 Space Community minibadge credited to SHIFTY (distinct from the 2023 Space Community Cube Sat badge, made by Jup1t3r, already in the archive). Found by the event-year sweep, task saintcon-2024.
- The community sheet listed the maker as "unconfirmed"; the repo folder name and the wider MiniBadges2024 repo (all other SAINTCON 2024 minibadges are credited the same way) attribute it to SHIFTY, a recurring SAINTCON badge designer.
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Space%20Community%20-%20SHIFTY
  title: Space Community minibadge (2024)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/README.md
  title: utahsaint-org/MiniBadges2024 README
  accessed: '2026-09-10'
  note: 'Confirms the repo is the SAINTCON 2024 minibadge set, supporting the event/year.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/Space%20Community%20-%20SHIFTY/Space%20Community%20-%20SHIFTY.kicad_pcb
  title: Space Community - SHIFTY.kicad_pcb
  accessed: '2026-09-10'
  note: 'KiCad PCB source; shows two 1206 SMD LED footprints, a resistor, and a "MiniBadge_Simple" footprint, and no MCU footprint.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: >
    Only source found is the maker's own GitHub repo folder (KiCad project, PSD/SVG
    art, and PNG fab-layer exports); no separate write-up, storefront, or photo of an
    assembled/lit badge was located, and no press or social coverage turned up in two
    searches. Price, quantity, and availability are not stated anywhere found, so those
    fields are left empty. The board layout supports two LEDs on a coin-cell-style
    "MiniBadge_Simple" footprint with no MCU, consistent with SAINTCON's simple passive
    community minibadges, but this is inferred from the PCB file rather than stated by
    the maker in prose.
last_modified_date: '2026-09-10'
---

The Space Community minibadge is one of the SAINTCON 2024 community minibadges, credited to the recurring SAINTCON badge designer SHIFTY. It carries a space/spacecraft graphic and is built as a simple lit PCB pin: the KiCad source shows two 1206 SMD LEDs and a resistor on a small board using a common "MiniBadge_Simple" footprint, with no microcontroller, so any lighting is passive rather than driven by firmware.

It is part of the wider `utahsaint-org/MiniBadges2024` GitHub repository, which collects the KiCad design files, vector artwork, and Photoshop source for the full set of SAINTCON 2024 community and event minibadges (Blue Team, Education Security, Women In Cybersecurity, Tamper Evident, and others), all attributed to SHIFTY. It is a separate design from the 2023 "Space Community Cube Sat" badge, which was made by a different SAINTCON designer, Jup1t3r.

No storefront listing, price, production quantity, or press coverage was found for this specific minibadge; the KiCad hardware files are published in the repo, but no matching firmware repo exists since the board has no MCU.

## Make your own

The KiCad project (schematic, PCB layout, and custom footprints) and the source artwork (SVG and PSD layers used for the silkscreen/soldermask art) are published in the `Space Community - SHIFTY` folder of the repo linked above. Someone wanting to reproduce it would open the `.kicad_pro` project in KiCad, order the two-layer board from a standard PCB fab, and hand-solder the two 1206 LEDs and the resistor onto the "MiniBadge_Simple" footprint.
