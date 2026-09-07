---
title: CL4P-TP-Shitty-Add-On — DC26 Shitty Add-On Board
id: dc26-cl4p-tp-shitty-add-on-dc26-shitty-add-on-board
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: Sparx50
  url: https://github.com/Sparx50
summary: A DEF CON 26 Shitty Add-On shaped like Claptrap (CL4P-TP), the robot from the Borderlands games, with eight LEDs driven through an I/O expander.
functions: Lights eight onboard LEDs (D1-D8), each through its own 220-ohm resistor, driven via an MCP23017 I2C GPIO expander.
look:
  colors: []
  shape: robot
  themes:
  - robot
  - video game
  - pop culture
tech:
  mcu: none
  leds:
    count: 8
    type: discrete
    note: 1206 LEDs, each with its own 220-ohm current-limiting resistor
  display: none
  connectivity:
  - i2c
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/Sparx50/CL4P-TP-Shitty-Add-On
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/Sparx50/CL4P-TP-Shitty-Add-On
  url: https://github.com/Sparx50/CL4P-TP-Shitty-Add-On
  kind: repo
  archived: https://web.archive.org/web/20260907114901/https://github.com/Sparx50/CL4P-TP-Shitty-Add-On
images:
- file: assets/images/badges/dc26/cl4p-tp-shitty-add-on-dc26-shitty-add-on-board/ee69ec9de7.png
  source: https://github.com/Sparx50/CL4P-TP-Shitty-Add-On
  credit: Sparx50
  caption: Claptrap silkscreen artwork used on the CL4P-TP SAO PCB
  archived: https://web.archive.org/web/20260907114901/https://github.com/Sparx50/CL4P-TP-Shitty-Add-On
- file: assets/images/badges/dc26/cl4p-tp-shitty-add-on-dc26-shitty-add-on-board/46939edce0.png
  source: https://github.com/Sparx50/CL4P-TP-Shitty-Add-On
  credit: Sparx50
  caption: Claptrap solder-mask artwork for the CL4P-TP SAO PCB
  archived: https://web.archive.org/web/20260907114901/https://github.com/Sparx50/CL4P-TP-Shitty-Add-On
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Sparx50/CL4P-TP-Shitty-Add-On
  title: CL4P-TP-Shitty-Add-On — DC26 Shitty Add-On Board
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 26''.'
  archived: https://web.archive.org/web/20260907114901/https://github.com/Sparx50/CL4P-TP-Shitty-Add-On
- kind: url
  url: https://raw.githubusercontent.com/Sparx50/CL4P-TP-Shitty-Add-On/master/CL4p_TP.sch
  title: CL4p_TP.sch (KiCad schematic)
  accessed: '2026-09-07'
  note: Confirms it uses the badgelife_shitty_connector library (SAO), an MCP23017 I2C GPIO expander, and 8 LEDs (D1-D8) each with a 220-ohm series resistor, powered from +3.3V.
  archived: https://web.archive.org/web/20260907115044/https://raw.githubusercontent.com/Sparx50/CL4P-TP-Shitty-Add-On/master/CL4p_TP.sch
- kind: url
  url: https://github.com/Sparx50/CL4P-TP-Shitty-Add-On/tree/master/Design
  title: Design folder listing
  accessed: '2026-09-07'
  note: Contains Claptrap_SilkScreen.png and Claptrap_SolderMask.png, the character artwork applied to the PCB, plus KiCad footprint files.
  archived: https://web.archive.org/web/20260907115235/https://github.com/Sparx50/CL4P-TP-Shitty-Add-On/tree/master/Design
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No maker post, storefront, price, or quantity-made info was found beyond the GitHub repo itself, so those fields are left empty. Repo shows only KiCad hardware design files (schematic, PCB, footprints, drill files) with no firmware/code, so make_your_own.firmware_url is left null. Status set to released (rather than listed) on the strength of the finished schematic/PCB/artwork in the repo, though no photo of an assembled unit or in-the-wild sighting was found; confidence kept at medium for that reason.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc26/cl4p-tp-shitty-add-on-dc26-shitty-add-on-board.glb
  method: kicad
  source_file: CL4p_TP.kicad_pcb
  generated: '2026-09-07'
  bytes: 137560
---

The CL4P-TP Shitty Add-On is a DEF CON 26 (2018) SAO by GitHub user Sparx50, shaped and silkscreened after Claptrap (CL4P-TP), the wisecracking robot from the Borderlands video game series. The board carries eight 1206 LEDs (D1 through D8), each behind its own 220-ohm resistor, driven from an MCP23017 I2C GPIO expander running off 3.3V supplied by the host badge's SAO header.

The GitHub repository is a complete open-hardware release: KiCad schematic and PCB layout files, custom footprints for the Claptrap silkscreen and solder-mask artwork, a drill file folder, and a JACK library, but no firmware or microcontroller code — the LED driving logic would live on whatever host badge addresses the MCP23017 over I2C. No maker write-up, storefront listing, price, or production-quantity information turned up outside the repository itself, so those fields are left blank rather than guessed.

## Make your own

The repository (linked above) has everything needed to reproduce the board: `CL4p_TP.sch` and `CL4p_TP.kicad_pcb` for the schematic and layout, the `Design/` folder for the Claptrap silkscreen/solder-mask artwork and custom footprints, and a `DRILLFile/` folder with drill data ready to send to a fab.
