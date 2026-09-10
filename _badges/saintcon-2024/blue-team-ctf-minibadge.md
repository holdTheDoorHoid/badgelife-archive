---
title: Blue Team CTF minibadge
id: saintcon-2024-blue-team-ctf-minibadge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: SHIFTY
summary: A passive SAINTCON 2024 minibadge for the Blue Team CTF track, carrying two SMD LEDs powered through the standard minibadge connector.
functions: 'Lights two onboard LEDs when plugged into a host badge''s minibadge header; no other electronics or logic.'
look:
  colors: []
  shape: null
  themes:
  - ctf
  - security
tech:
  mcu: none
  leds:
    count: 2
    type: SMD
    note: Two 1206 SMD LEDs, each with a series resistor; no microcontroller or other logic on the board.
  display: none
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
  open_source: partial
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Blue%20TEAM%20CTF%20-%20SHIFTY
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/Blue%20TEAM%20CTF%20-%20SHIFTY
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Blue%20TEAM%20CTF%20-%20SHIFTY
  kind: repo
- label: utahsaint-org/MiniBadges2024
  url: https://github.com/utahsaint-org/MiniBadges2024
  kind: repo
images: []
contact: {}
notes:
- Blue Team CTF-themed minibadge for SAINTCON 2024, credited to SHIFTY in the folder name. Found by the event-year sweep, task saintcon-2024.
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Blue%20TEAM%20CTF%20-%20SHIFTY
  title: Blue Team CTF minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024
  title: 'utahsaint-org/MiniBadges2024: Minibadges for SAINTCON 2024'
  accessed: '2026-09-10'
  note: 'Repo description confirms the collection was made for SAINTCON 2024; root README has no per-badge detail.'
- kind: url
  url: https://api.github.com/repos/utahsaint-org/MiniBadges2024/contents/Blue%20TEAM%20CTF%20-%20SHIFTY
  title: Directory listing, Blue TEAM CTF - SHIFTY
  accessed: '2026-09-10'
  note: 'File listing (KiCad schematic/PCB/project files, .psd, .svg, PNG export folder) used to confirm the design is a 20mm KiCad minibadge with no README of its own.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/Blue%20TEAM%20CTF%20-%20SHIFTY/Blue%20TEAM%20CTF%20-%20SHIFTY.kicad_pcb
  title: Blue TEAM CTF - SHIFTY.kicad_pcb
  accessed: '2026-09-10'
  note: 'PCB file inspected for footprints: two LED_SMD 1206 LEDs, two matching resistors, and a MiniBadge:MiniBadge_Simple connector footprint; no MCU footprint present.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/Blue%20TEAM%20CTF%20-%20SHIFTY/Blue%20Team%20CTF.svg
  title: Blue Team CTF.svg
  accessed: '2026-09-10'
  note: 'Confirms board outline is a 20mm x 20mm square, the standard SAINTCON minibadge size.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'The GitHub repo (utahsaint-org/MiniBadges2024, described by its owner as "Minibadges for SAINTCON 2024") confirms this is a real, designed minibadge for that event, matching the entry''s existing event/year. Only KiCad source files, a .psd, and gerber-style PNG layer exports (front copper/mask/silk, black-and-white) are in the repo -- no photograph of an assembled unit and no README for this specific badge, so solder-mask color, exact shape/theme beyond "CTF"/"security", price, quantity made, and distribution method could not be confirmed and are left empty. PCB inspection shows 2 SMD LEDs and a resistor per LED wired to a standard MiniBadge_Simple connector, with no microcontroller -- consistent with SAINTCON''s many purely decorative, host-powered minibadges. Did not find the badge on any storefront, Hackaday, or press coverage; open_source is "partial" because hardware (KiCad) files are public but no firmware exists to publish (board appears to have no logic to drive the LEDs beyond passive resistor limiting, so "firmware" is likely not applicable). Did not save images: the only visual files in the repo are individual PCB gerber-layer exports (front copper, mask, silk) in black-and-white, not photos or a full-color rendering of the finished piece, so none clearly show what the actual minibadge looks like.'
last_modified_date: '2026-09-10'
---

The Blue Team CTF minibadge is one of dozens of minibadges SHIFTY designed for SAINTCON 2024's minibadge program, themed after the con's Blue Team CTF track. Like other SAINTCON minibadges, it is a small (20mm square) PCB meant to plug into a host badge's minibadge connector rather than carry its own battery or logic; two surface-mount LEDs, each behind its own current-limiting resistor, light up once it is seated in a badge that provides power. No microcontroller is present on the board.

The design files -- KiCad schematic and PCB, a Photoshop source, and vector/PNG artwork exports -- are published in the utahsaint-org/MiniBadges2024 GitHub repository alongside dozens of the con's other 2024 minibadges, but the repository carries no per-badge README, storefront listing, or photo of an assembled unit, so details like the actual solder-mask color, how many were made, and how attendees obtained it (contest, giveaway, trade) are not confirmed by any source found.
