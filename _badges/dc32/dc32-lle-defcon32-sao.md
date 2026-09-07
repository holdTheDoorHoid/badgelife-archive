---
title: DEFCON32 SAO
id: dc32-dc32-lle-defcon32-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: LLE (lle)
  url: https://github.com/lle
summary: A DEF CON 32 Shitty Add-On by GitHub maker lle built around an STM32F0 driving an 8x8 LED matrix with a single button, running an animation/screensaver mode plus a new racing-game mode on firmware carried over from their DEF CON 31 blinky add-on.
functions: Single-button interface with an animation/screensaver mode and a new racing-game mode, built on firmware inherited from the maker's DEF CON 31 add-on.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: STM32F0
  leds:
    count: 64
    type: discrete
    note: 8x8 LED matrix, carried over from the DEF CON 31 design; one LED lit at a time to stay within the port current limit.
  display: LED matrix 8x8
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
  hardware_url: https://github.com/lle/defcon32-sao
  firmware_url: https://github.com/lle/defcon32-sao
  eda_tool: null
links:
- label: github.com/lle/defcon32-sao
  url: https://github.com/lle/defcon32-sao
  kind: repo
- label: github.com/lle/defcon31-addon
  url: https://github.com/lle/defcon31-addon
  kind: repo
images:
- file: assets/images/badges/dc32/dc32-lle-defcon32-sao/00e53040d8.jpg
  source: https://github.com/lle/defcon32-sao
  credit: lle
  caption: The DEF CON 32 SAO board
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/lle/defcon32-sao
  title: lle/defcon32-sao
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/lle/defcon32-sao
  title: lle/defcon32-sao (README and media folder)
  accessed: '2026-09-07'
  note: Confirmed STM32F0 MCU, racing-game mode added on top of DEF CON 31 firmware, hardware/firmware fully open in the repo, and the badge photo used above.
- kind: url
  url: https://github.com/lle/defcon31-addon
  title: lle/defcon31-addon
  accessed: '2026-09-07'
  note: Confirmed the shared foundation firmware, 8x8 LED matrix (64 LEDs), single-button interaction, and STM32F0 MCU that DEF CON 32's SAO reuses.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Both repos are the maker's personal open-source hardware/firmware releases; neither documents price, quantity made, or how/whether it was distributed to others, so those fields are left empty. No third-party coverage (Hackaday, press, storefronts) of this SAO was found.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc32/dc32-lle-defcon32-sao.glb
  method: kicad
  source_file: dc32sao.brd
  generated: '2026-09-07'
  bytes: 201656
---

LLE's DEF CON 32 SAO is a small STM32F0-based add-on built around an 8x8 LED matrix and a single push button, continuing directly from their DEF CON 31 blinky add-on. The firmware reuses that project's foundation code (in turn recycled from an earlier "Snake Business Card" design) and adds a new racing-game mode alongside the original animation/screensaver mode.

Both the hardware and firmware are published on GitHub with no restrictions noted, including PCB design files, STM32CubeIDE firmware sources, and step-by-step ST-Link flashing instructions. The maker does not state how many units were made, whether it was sold or given away, or where it was distributed — it appears to be a personal project shared openly rather than a commercial product.

## Make your own

Hardware and firmware are in the [defcon32-sao repo](https://github.com/lle/defcon32-sao). To flash it: build the firmware in STM32CubeIDE, connect an ST-Link programmer (the maker uses an STM32F0 Nucleo board) to the PCB's SWD header via the documented connector wiring, then run the debug configuration to program the board.
