---
title: Haunting Specter Expansion Board (2023)
id: saintcon-2023-haunting-specter-expansion-board-2023
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: distinctm1nd
  url: https://github.com/distinctm1nd
summary: 'A minibadge expansion board shaped like a ghost/jack-o-lantern face that powers and lights up to 8 SAINTCON minibadges at once, run either from the main conference badge or standalone on AA batteries.'
functions: 'Powers and displays up to 8 minibadges via 20-pin connectors; can be run standalone on 2x AA batteries or powered through the main SAINTCON badge; additional expansion boards can be daisy-chained and powered from it; LED colors and resistor values are swappable so builders can practice designing series LED/resistor circuits.'
look:
  colors:
  - green
  shape: other
  themes:
  - halloween
  - horror
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 16
    type: discrete
    note: 'Multi-color version: 14 SMD 1206 LEDs (mixed colors) + 2 through-hole LEDs. Red/Yellow version: 12 SMD 1206 LEDs (red/yellow) + 2 through-hole LEDs. Both use series resistors per LED, sized for swapping colors.'
  display: none
  connectivity: []
  battery: 2x AA
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed at SAINTCON 2023 in Utah; came in two component variants (multi-color and red/yellow). Optional 3D-printed backs were offered separately by a community member ("lavaman") on Discord, not by the maker.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/distinctm1nd/haunting_specter_expansion_board_2023
  firmware_url: null
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: 'Repo has a schematic PDF, PCB renderings, full build/assembly instructions, and a component list for both LED-color variants, but no Gerbers, BOM file, or stated license, and no indication of the EDA tool used.'
links:
- label: github.com/distinctm1nd/haunting_specter_expansion_board_2023
  url: https://github.com/distinctm1nd/haunting_specter_expansion_board_2023
  kind: repo
images:
  - file: assets/images/badges/saintcon-2023/haunting-specter-expansion-board-2023/f012b2fca4.jpg
    source: "https://github.com/distinctm1nd/haunting_specter_expansion_board_2023"
    credit: "distinctm1nd"
    caption: "Assembled multi-color version of the Haunting Specter Expansion Board"
  - file: assets/images/badges/saintcon-2023/haunting-specter-expansion-board-2023/218c973956.jpg
    source: "https://github.com/distinctm1nd/haunting_specter_expansion_board_2023"
    credit: "distinctm1nd"
    caption: "Assembled red/yellow version of the Haunting Specter Expansion Board"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://github.com/distinctm1nd/haunting_specter_expansion_board_2023
  title: Haunting Specter Expansion Board (2023)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''saintcon-2023''.'
- kind: url
  url: https://raw.githubusercontent.com/distinctm1nd/haunting_specter_expansion_board_2023/main/README.md
  title: haunting_specter_expansion_board_2023 README
  accessed: '2026-09-07'
  note: 'Full build description, components list for both LED-color variants, assembly instructions, and use with the SAINTCON badge or standalone on AA batteries.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'No price, quantity made, or maker''s own name (beyond the "distinctm1nd" handle) were stated anywhere in the repo. No MCU is used - this is a passive LED expansion board, not a microcontroller-driven badge. No SAO header is present; it connects to the SAINTCON main badge and other expansion boards via 20-pin 2.54mm connectors, not a standard SAO port, so sao_version/sao_ports are left as none/empty rather than guessed. Shape is a ghost/jack-o-lantern-style face (eyes, nose, mouth laid out as LED positions) - recorded as "other" since no closer vocabulary term fit. 3D-printed backs were a separate community offering (from "lavaman"), not part of the maker''s own kit.'
last_modified_date: '2026-09-07'
---

The Haunting Specter Expansion Board is a SAINTCON 2023 minibadge accessory built to power and display up to eight minibadges at once. It can run standalone on two AA batteries or draw power from the main SAINTCON conference badge, and additional expansion boards can be daisy-chained off of it. The board's face-shaped LED layout (eyes, nose, and mouth positions) gives it a ghost or jack-o'-lantern look in keeping with SAINTCON's Halloween-season timing.

It shipped in two component variants: a multi-color version using 14 SMD 1206 LEDs in assorted colors plus 2 through-hole LEDs, and a red/yellow version using 12 SMD 1206 LEDs plus 2 through-hole LEDs. The maker, distinctm1nd, designed every LED position with its own series resistor specifically so builders could swap in different colored LEDs and recalculate the resistor value themselves - the GitHub repo includes a full LED/resistor swap table and points builders to an online LED resistor calculator, framing the board partly as a soldering and circuit-design exercise. A separate community member ("lavaman") offered 3D-printed backs for the board over Discord, though these were not part of the maker's own kit.

## Make your own

The repository (github.com/distinctm1nd/haunting_specter_expansion_board_2023) includes a schematic PDF, front/back PCB renderings, assembly photos, and step-by-step soldering instructions for both the multi-color and red/yellow variants, including LED orientation diagrams and the per-LED resistor value table. No Gerbers, bill of materials file, or license are published, and the design tool used is not stated, so it is recorded here as partially open source (documentation and schematic only).
