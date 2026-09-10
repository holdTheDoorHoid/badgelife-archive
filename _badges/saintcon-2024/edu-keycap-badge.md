---
title: EDU-KeyCap-Badge
id: saintcon-2024-edu-keycap-badge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: unconfirmed
summary: A simple, single-LED SAINTCON 2024 education-track minibadge; the KiCad project itself is named "KeyCapESC," suggesting a keycap-shaped board.
functions: Lights a single LED when powered through its minibadge header; no onboard logic or microcontroller.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 1
    type: SMD
    note: One 1206 SMD LED with a single current-limiting resistor; no addressable/RGB driver.
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
  open_source: true
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/EDU-KeyCap-Badge
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/EDU-KeyCap-Badge
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/EDU-KeyCap-Badge
  kind: repo
- label: EDU-KeyCap-Badge Gerbers
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/EDU-KeyCap-Badge/Gerbers
  kind: fab
images: []
contact: {}
notes:
- Keycap-shaped education minibadge submitted for SAINTCON 2024. Found by the event-year sweep, task saintcon-2024.
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/EDU-KeyCap-Badge
  title: EDU-KeyCap-Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/EDU-KeyCap-Badge/KeyCapESC.kicad_pcb
  title: KeyCapESC.kicad_pcb (raw KiCad PCB file)
  accessed: '2026-09-10'
  note: 'Confirmed board contents by inspecting footprints directly: one MiniBadge_Simple header footprint, one 1206 SMD LED, one 1206 SMD resistor, no MCU footprint.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/README.md
  title: MiniBadges2024 README
  accessed: '2026-09-10'
  note: Confirms the repo is the official "Minibadges for SAINTCON 2024" collection; no per-badge documentation or maker credits given.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed the design is real by reading the KiCad PCB directly (no README or images exist in its folder or the repo root). The board''s internal project name is "KeyCapESC" rather than "EDU-KeyCap-Badge" (the folder name); kept the folder''s title per the sweep, noted the internal name here. Design is passive: one SAO/minibadge header footprint ("MiniBadge_Simple"), one LED, one resistor -- no MCU, no battery, no display. Could not find a named maker; the most recent GitHub committer on this folder is user "tjhiker" (display name "Jup1t3r"), but nothing on the repo credits them (or anyone) as the badge''s designer, so makers stays unconfirmed rather than guessing. No photos of the assembled badge were found anywhere (repo, search, or press) to save under images. Price, quantity, and distribution/availability were not stated anywhere found; SAINTCON minibadges are typically distributed to attendees who solder them at the con, but that was not confirmed for this specific badge, so
    get_one fields and status are left as in the original stub.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2024/edu-keycap-badge.glb
  method: kicad
  source_file: EDU-KeyCap-Badge/KeyCapESC.kicad_pcb
  generated: '2026-09-10'
  bytes: 34804
---

The EDU-KeyCap-Badge is one of dozens of minibadges submitted to the official `utahsaint-org/MiniBadges2024` repository, the community collection point for SAINTCON 2024's minibadge program. Its KiCad project is internally named "KeyCapESC," which (together with the folder name) suggests it is shaped like a keyboard keycap, though no photo of the finished board was found to confirm this.

Electrically it is a deliberately simple, education-track design: reading the KiCad PCB file directly shows a single minibadge header footprint, one SMD LED, and one current-limiting resistor, with no microcontroller, battery, or display on the board. That matches a learn-to-solder style minibadge meant to be easy for a beginner to assemble at the con, though no page was found describing the intended build process or who designed it.

No storefront, price, quantity, or distribution details were found for this badge, and no maker is credited on the repository. The only attribution available is the GitHub username of the most recent contributor to the folder ("tjhiker" / "Jup1t3r"), which is not confirmed to be the badge's actual designer, so the maker field is left unconfirmed rather than guessed.
