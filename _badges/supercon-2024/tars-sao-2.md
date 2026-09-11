---
title: T.A.R.S.
id: supercon-2024-tars-sao-2
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: An Interstellar TARS robot-themed SAO built around an RP2040-Tiny module with a 160x80 ST7735 TFT display, six capacitive touch buttons, a speaker and an LED, described by the maker as his most complex simple add-on design.
functions: A menu-driven interface navigated with the six touch buttons, animated scrolling text on the split-screen 160x80 display, and tone/sound playback through the onboard speaker (per the Arduino sketch names in the repo, including a menu flipper, a touch-tone test, and a "chatGPT free" mode).
look:
  colors: []
  shape: null
  themes:
  - robot
  - sci-fi
  - movie
tech:
  mcu: RP2040-Tiny
  leds:
    count: 1
    type: null
    note: Single LED; README describes the board as having "an LED" without further detail.
  display: 160x80 ST7735 TFT
  connectivity:
  - i2c
  battery: null
  sao_version: v1.69bis
  sao_ports: 1
  power: powered by host badge
  inputs:
  - touch
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/davedarko/TARS-SAO/tree/main/KiCad/TARS
  firmware_url: https://github.com/davedarko/TARS-SAO/tree/main/Sketchbook
  gerbers_url: https://github.com/davedarko/TARS-SAO/tree/main/KiCad/TARS/production
  eda_tool: KiCad
  license: MIT
  notes: Hardware (KiCad schematic/PCB/gerbers/BOM) and firmware (multiple Arduino sketches) are both published in the repo under the MIT license.
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: github.com/davedarko/TARS-SAO
  url: https://github.com/davedarko/TARS-SAO
  kind: repo
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/davedarko/TARS-SAO
  title: davedarko/TARS-SAO — "A not so simple Add-On for badges"
  accessed: '2026-09-07'
  note: 'Maker''s README, LICENSE, and repo file listing: confirms RP2040-Tiny MCU, display/6 touch buttons/speaker/LED, MIT license, KiCad hardware files, and production gerbers.'
- kind: url
  url: https://raw.githubusercontent.com/davedarko/TARS-SAO/main/Sketchbook/TARS/TARS.ino
  title: TARS.ino (main firmware sketch)
  accessed: '2026-09-07'
  note: Confirms ST7735 160x80 TFT display driven via TFT_eSPI, split into left/right 80px halves for scrolling text.
- kind: url
  url: https://raw.githubusercontent.com/davedarko/TARS-SAO/main/KiCad/TARS/TARS.kicad_sch
  title: TARS.kicad_sch (schematic source)
  accessed: '2026-09-07'
  note: Schematic connector list includes a 2x3 odd/even header matching the SAO v1.69bis 6-pin standard described on the Simple-Add-ons-SAO repo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own repo confirms the hardware/firmware details in the existing summary except the stub's claim of a "Qwiic I2C port," which could not be verified — the schematic shows an extra 4-pin connector whose exact purpose (Qwiic vs. something else) is not labeled in the text-searchable schematic, so that specific claim was dropped rather than guessed. No photo of the assembled board was found (the repo's Reference folder holds only a stock RP2040-Tiny kit photo, a SVG mockup, and an unrelated font-reference image, none of which show the actual TARS SAO). Could not independently confirm it was specifically built for/distributed at Supercon 2024 beyond the original community-sheet entry (the LICENSE year, 2024, is consistent with this). Price, quantity made, and availability are not stated anywhere in the repo. No Hackaday.io project page or social posts about this specific SAO were found (web search budget was exhausted before a broader press/social search could be done).
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2024/tars-sao-2.glb
  method: kicad
  source_file: KiCad/TARS/TARS.kicad_pcb
  generated: '2026-09-10'
  bytes: 158372
---

T.A.R.S. is a "Simple Add-on" (SAO) by GitHub user davedarko (Berlin-based web developer and hardware tinkerer, prolific SAO designer) themed around the boxy robot TARS from the film *Interstellar*. The maker describes it in his SAO collection repo as "probably my most complex design, a small TARS with display and RP2040," and it was made for Supercon 2024.

The board is built around an RP2040-Tiny module driving a 160x80 ST7735 TFT display, split in the firmware into left and right 80-pixel-wide halves that each scroll animated, typewriter-style text independently. It also carries six capacitive touch buttons, a speaker, and an LED. The Arduino sketches bundled in the repo (a menu system, touch tests, tone playback, and a "chatGPT free" mode) suggest the finished badge runs a menu-driven interface with sound and touch interaction, in keeping with TARS's on-screen personality slider gags from the movie.

Both the hardware and firmware are open-sourced under the MIT license: the KiCad project includes finished production gerbers and a bill of materials, and the SAO connects to a host badge through the standard 6-pin SAO v1.69bis header. No maker's photo of the assembled board, nor any pricing, quantity, or distribution details, were found during this pass.
