---
title: Defcon-SAO (AlexRojasx)
id: other-defcon-sao-alexrojasx
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: AlexRojasx
  url: https://github.com/AlexRojasx
summary: A simple pirate-themed SAO for DEF CON badges, hand-built by AlexRojasx after their dad (@ElJjefeDSecurIT) didn't get around to making one.
functions: Backlights a pirate silhouette cut into the soldermask/copper/silkscreen using three LEDs; no other electronic functions.
look:
  colors: []
  shape: null
  themes:
  - pirate
  - security
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: Right-angle/back-lighting LEDs mounted on the rear of the board, shining through clear cutouts on the front to illuminate a pirate design. Resistor values vary by LED color (calculated via Ohm's law).
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: 165 assembled
  availability: unknown
  distribution:
  - free_drop
  where: Handed out/brought to DEF CON 32 (August 2024) by the maker; no storefront listing found.
make_your_own:
  open_source: true
  hardware_url: https://github.com/AlexRojasx/Defcon-SAO
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/AlexRojasx/Defcon-SAO
  url: https://github.com/AlexRojasx/Defcon-SAO
  kind: repo
images:
- file: assets/images/badges/other/defcon-sao-alexrojasx/bff91ad8cf.jpg
  source: https://github.com/AlexRojasx/Defcon-SAO
  credit: AlexRojasx
  caption: Finished assembled Defcon SAO board with pirate artwork
- file: assets/images/badges/other/defcon-sao-alexrojasx/162e191636.png
  source: https://github.com/AlexRojasx/Defcon-SAO
  credit: AlexRojasx
  caption: 3D model render of the SAO PCB showing the pirate design
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/AlexRojasx/Defcon-SAO
  title: Defcon-SAO (AlexRojasx)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://raw.githubusercontent.com/AlexRojasx/Defcon-SAO/main/README.md
  title: AlexRojasx/Defcon-SAO README
  accessed: '2026-09-07'
  note: Confirmed maker's description, 3-LED backlighting design, KiCad open-source files, hand-assembly of 165 units by reflow oven, and assembly photos dated August 2024 pinning it to DEF CON 32.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No storefront, price, or store listing was found for this SAO; README implies it was handed out/brought by the maker rather than sold. Event corrected from "other" to dc32 based on assembly photo filenames dated August 2024, matching DEF CON 32 (Aug 8-11, 2024). Firmware N/A (passive LED board, no MCU). No press coverage or social posts found.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/defcon-sao-alexrojasx.glb
  method: kicad
  source_file: pirate.kicad_pcb
  generated: '2026-09-10'
  bytes: 89672
---

AlexRojasx built this "shitty add-on" as a fun, simple SAO for DEF CON after their dad, @ElJjefeDSecurIT, didn't get around to making one for the badgelife scene. The board is a passive design: a standard 0.1" 2x3 SAO header, three backlighting LEDs mounted on the rear of the board, and a pirate silhouette left clear of soldermask, copper, and silkscreen so the LEDs glow through it from behind. Resistor values were calculated from Ohm's law and vary depending on the LED color used.

The maker had 165 units fabricated and hand-assembled them using solder paste, a reflow oven for the SMD components, and hand soldering for the through-hole header pins — around 800 SMD parts and nearly 1,000 through-hole pins across the batch. Photos of the assembly process are dated early August 2024, placing the build for DEF CON 32. The hardware (KiCad schematic and PCB files) is published on GitHub, but no firmware is needed since the board has no MCU. No store listing, price, or distribution details beyond "brought to DEF CON" were found.

## Make your own

The repository at github.com/AlexRojasx/Defcon-SAO contains the KiCad schematic (`pirate.kicad_sch`) and PCB layout (`pirate.kicad_pcb`) files needed to reproduce the board. Building one requires ordering the PCB, sourcing three LEDs (color of choice) and matching resistors sized per Ohm's law for the chosen LEDs, and hand- or reflow-soldering the SMD and through-hole components.
