---
title: BerlyMIB minibadge
id: saintcon-2024-personal-berlymib-minibadge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: Berly
summary: A fire-hydrant-shaped personal minibadge for SAINTCON 2024, built to the "MiniBadge Simple" passive standard with three LEDs lit by the host badge.
functions: 'Passive lighting only: three LEDs light up when plugged into a powered host badge, no onboard logic.'
look:
  colors:
  - red
  - yellow
  - silver
  shape: fire hydrant
  themes: []
tech:
  mcu: none
  leds:
    count: 3
    type: null
    note: Through-hole LED symbols in the schematic; specific part/color not stated.
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
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Personal-BerlyMIB
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/Personal-BerlyMIB
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Personal-BerlyMIB
  kind: repo
images: []
contact: {}
notes:
- Personal minibadge by Berly (maker of the 2023 Marvin the Martian badge already in the archive) for SAINTCON 2024. Found by the event-year sweep, task saintcon-2024.
- 'The archive sheet titled this "Personal-BerlyMIB minibadge" (the repo folder name); the maker''s own artwork/schematic files are simply named "BerlyMIB", so the title was tightened to "BerlyMIB minibadge".'
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Personal-BerlyMIB
  title: Personal-BerlyMIB minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/README.md
  title: 'utahsaint-org/MiniBadges2024 README'
  accessed: '2026-09-10'
  note: Confirms the repo is "Minibadges for SAINTCON 2024".
- kind: url
  url: https://api.github.com/repos/utahsaint-org/MiniBadges2024/contents/Personal-BerlyMIB
  title: Personal-BerlyMIB directory listing
  accessed: '2026-09-10'
  note: File listing shows only KiCad PCB/schematic files, layer SVGs, and Illustrator art files - no README, no photos of the assembled badge, no BOM/price/quantity info.
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/Personal-BerlyMIB/BerlyMIB-Badge.kicad_sch
  title: BerlyMIB-Badge.kicad_sch
  accessed: '2026-09-10'
  note: 'Schematic uses the Minibadge:MiniBadge_Simple connector footprint plus three Device:LED symbols and matching resistors - a passive, MCU-less minibadge lit by the host badge''s power.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/Personal-BerlyMIB/BerlyMIB_Design%20Concept.svg
  title: BerlyMIB Design Concept artwork
  accessed: '2026-09-10'
  note: Rendered the vector artwork - it depicts a red-and-yellow-and-tan fire hydrant with two silver bolt heads on the base, giving the shape/color fields.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: >-
    Confirmed real via the maker's own GitHub repo (utahsaint-org/MiniBadges2024), which holds
    complete KiCad hardware files and vector artwork for a fire-hydrant-shaped minibadge. No
    firmware is needed or present since the schematic uses the passive "MiniBadge Simple"
    standard (three LEDs + resistors, powered by the host badge, no logic chip). Could not find
    any photo of the assembled/soldered badge, price, quantity made, or distribution details -
    searches of saintcon.org, minibadge.wiki, badge.gallery, and the SAINTCON 2024 minibadge
    trading page turned up no listing for it, suggesting this was a personal/unofficial minibadge
    the maker shared design files for rather than one that went through the official minibadge
    guide or trading program. No comparison sources disagreed since only the maker's own repo
    discusses it.
last_modified_date: '2026-09-10'
---

Berly's BerlyMIB is a personal minibadge made for SAINTCON 2024, following up on the same
maker's 2023 "Marvin the Martian" badge already in the archive. The design is a small
fire-hydrant-shaped PCB - a red dome and base bracketing a tan band with yellow vertical
stripes and two silver bolt heads - built to the SAINTCON "MiniBadge Simple" passive
standard: three LEDs and their resistors wired straight to the host badge's power pins,
with no microcontroller or onboard logic, so the LEDs simply light up while the minibadge
is plugged in.

The maker published the complete KiCad project (schematic, PCB layout, and per-layer
Gerber-equivalent SVGs) along with the original Illustrator artwork in the
`utahsaint-org/MiniBadges2024` GitHub repository, so the hardware design is fully open,
though no firmware exists to publish since the board is passive. No photos of an assembled
unit, pricing, production quantity, or distribution details turned up in this pass - the
badge doesn't appear on the official SAINTCON 2024 minibadge guide, the minibadge wiki, or
badge.gallery's trading-collection listing, suggesting it circulated informally rather than
through the official program.

## Make your own

The repository (linked above) contains the KiCad schematic and PCB files
(`BerlyMIB-Badge.kicad_sch` / `.kicad_pcb`) plus front/back copper, mask, and silkscreen
SVGs and the original artwork - enough to fabricate and populate the board (three LEDs,
matching resistors, and a MiniBadge Simple edge connector) without needing any firmware.
