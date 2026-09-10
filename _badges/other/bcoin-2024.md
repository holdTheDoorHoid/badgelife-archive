---
title: BCoin 2024
id: other-bcoin-2024
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 2024
makers:
- name: youngd24
  url: https://github.com/youngd24
summary: A free 555-timer "challenge coin" given to new attendees of the South instance of the BurbSec meetup, marking a decade of the group.
functions: A 555 timer in astable mode drives a decade counter that "chases" a ring of perimeter LEDs around the coin's edge at roughly 4.8 Hz; it carries the meetup's basic info (when/where) printed on the back.
look:
  colors: []
  shape: coin
  themes:
  - coin
  - learn to solder
  - electronics
tech:
  mcu: none
  leds:
    count: null
    type: discrete
    note: Perimeter ring of LEDs driven in sequence ("chaser") by a CD4017-style decade counter fed from a 555 astable oscillator.
  display: none
  connectivity: []
  battery: CR2016 (pads also fit CR2032)
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to new attendees who show up to a meetup of the South instance of BurbSec.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/youngd24/BCoin2024
  firmware_url: null
  eda_tool: KiCad
notes: []
links:
- label: github.com/youngd24/BCoin2024
  url: https://github.com/youngd24/BCoin2024
  kind: repo
images:
- file: assets/images/badges/other/bcoin-2024/a61fba4be5.jpg
  source: https://github.com/youngd24/BCoin2024
  credit: youngd24
  caption: BCoin 2024 front, showing the perimeter LED chaser ring
- file: assets/images/badges/other/bcoin-2024/3ad425b0f9.jpg
  source: https://github.com/youngd24/BCoin2024
  credit: youngd24
  caption: BCoin 2024 back, with meetup information
contact: {}
status: released
sources:
- kind: url
  url: https://github.com/youngd24/BCoin2024
  title: BCoin 2024
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/youngd24/BCoin2024/main/README.md
  title: 'youngd24/BCoin2024: README'
  accessed: '2026-09-07'
  note: 'Maker''s own description of the coin: purpose, circuit, dimensions, battery, and hacking/modifying instructions.'
- kind: url
  url: https://api.github.com/repos/youngd24/BCoin2024
  title: youngd24/BCoin2024 repository metadata
  accessed: '2026-09-07'
  note: Repo description ("BurbSec Challenge Coin 2024"), BSD-3-Clause license, and file listing confirming KiCad source, gerbers, and BOM are published.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a self-published meetup token, not a badge for a hacker con, so no matching id exists in events.yml and event is left as ''other''; the maker calls it the "BurbSec Challenge Coin 2024" for the South instance of the BurbSec meetup group. Dimensions per the README: 50mm diameter, ~5mm thick including the battery, with a thinner 40mm version "planned" (not found released). LED count not stated in the README; not guessed. No price beyond "free to attendees" and no production quantity was given.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/bcoin-2024.glb
  method: kicad
  source_file: BCoin2024.kicad_pcb
  generated: '2026-09-10'
  bytes: 142956
---

The BCoin 2024 is a free "challenge coin" that youngd24, longtime organizer of the South instance of the BurbSec security meetup, hands out to first-time attendees. It doubles as a small electronics-education piece: at its core is a classic 555 timer running in astable mode, driving a decade counter that lights a ring of perimeter LEDs in a chasing pattern around the coin's edge at about 4.8 Hz. It runs off a single CR2016 coin cell (footprint also accepts a CR2032) and is sized — 50mm across, about 5mm thick with the battery installed — to fit standard clear acrylic challenge-coin display cases, though the maker notes to double-check case thickness before buying one.

The project is fully open source: the KiCad schematic and PCB files, a BOM, and manufacturing gerbers are published in the GitHub repo under a BSD-3-Clause license. The README walks through how to change the flash rate by swapping the R1/R2/C1 timing components (with a DigiKey calculator link for picking new values) and how to regenerate Gerber/drill files after edits, aimed at anyone who wants to build their own or adapt the design for their own group. A thinner 40mm variant was mentioned as planned but no evidence was found that it was released.

## Make your own

Hardware is fully published at https://github.com/youngd24/BCoin2024 (KiCad schematic/PCB, BOM.xlsx, and a `gerbers` directory), licensed BSD-3-Clause. To modify the flash rate, swap the R1/R2/C1 values feeding the 555 astable timer (stock values: R1 10k, R2 10k, C1 10uF, all 0603/0805), then re-run ERC/DRC in KiCad and regenerate Gerber and drill files for fabrication.
