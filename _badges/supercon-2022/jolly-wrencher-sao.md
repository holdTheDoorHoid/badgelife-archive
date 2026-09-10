---
title: Jolly Wrencher SAO
id: supercon-2022-jolly-wrencher-sao
layout: badge
parent: Supercon 2022
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2022
year: 2022
makers:
- name: Arya Voronova
  url: https://github.com/CRImier
summary: 'A wrench-shaped SAO from Arya Voronova that is really an SMD prototyping board: 1.27mm-pitch pads on a ground-fill-connected layout, with two LEDs behind transparent "eyes" cut into the Hackaday Jolly Wrencher logo.'
functions: 'No fixed function: it is a bare prototyping canvas. The pad grid accepts passives, SOIC-style ICs, and larger castellated modules like an ESP32-WROOM; the two eye LEDs are the only built-in indicators, wired to whatever the builder solders down.'
look:
  colors:
  - black
  shape: other
  themes:
  - hardware tool
  - logo
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 0805 LED footprints mounted behind transparent "eyes" that shine through the FR4
  display: none
  connectivity: []
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/CRImier/jolly_wrencher_sao
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.com/2022/10/11/jolly-wrencher-sao-and-how-kicad-6-made-it-easy
  url: https://hackaday.com/2022/10/11/jolly-wrencher-sao-and-how-kicad-6-made-it-easy/
  kind: article
- label: CRImier/jolly_wrencher_sao (GitHub)
  url: https://github.com/CRImier/jolly_wrencher_sao
  kind: repo
images:
- file: assets/images/badges/supercon-2022/jolly-wrencher-sao/4619276f64.jpg
  source: https://github.com/CRImier/jolly_wrencher_sao
  credit: Arya Voronova
  caption: Front of the Jolly Wrencher SAO, showing the LED eyes and prototyping pads
- file: assets/images/badges/supercon-2022/jolly-wrencher-sao/f7cb904a63.jpg
  source: https://github.com/CRImier/jolly_wrencher_sao
  credit: Arya Voronova
  caption: Back of the Jolly Wrencher SAO
contact: {}
notes:
- Found as a cross-referenced link within the 2024 contest-announcement article, not independently verified/opened
status: released
sources:
- kind: url
  url: https://hackaday.com/2022/10/11/jolly-wrencher-sao-and-how-kicad-6-made-it-easy/
  title: Jolly Wrencher SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''referenced from Supercon 2024 SAO contest announcement article''.'
- kind: url
  url: https://hackaday.com/2022/10/11/jolly-wrencher-sao-and-how-kicad-6-made-it-easy/
  title: Jolly Wrencher SAO And How KiCad 6 Made It Easy
  accessed: '2026-09-07'
  note: Confirmed maker (Arya Voronova), Supercon 2022, wrench-shaped SMD prototyping SAO with two 0805 LED "eyes", SAO v1.69bis, KiCad 6 design using native SVG import.
- kind: url
  url: https://github.com/CRImier/jolly_wrencher_sao
  title: CRImier/jolly_wrencher_sao
  accessed: '2026-09-07'
  note: Confirmed open-source hardware (KiCad files + gerbers in repo), board size ~47.93x43.85mm, SAO v1.69bis, no MCU, front/back photos used for images.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Made for Supercon 2022, not Supercon 2024 (this entry sat under the wrong event folder; event field corrected to supercon-2022, see report). No price, quantity, or distribution details found in either source -- it reads as a personal/demo project shared via Hackaday rather than a sold or mass-distributed badge, so availability is left unknown. No firmware exists since the board carries no MCU of its own.
last_modified_date: '2026-09-10'
redirect_from:
- /badges/supercon-2024/jolly-wrencher-sao/
model:
  file: assets/models/supercon-2022/jolly-wrencher-sao.glb
  method: kicad
  source_file: jolly_wrencher_pcb_^^.kicad_pcb
  generated: '2026-09-10'
  bytes: 412020
---

The Jolly Wrencher SAO is a small prototyping board shaped like Hackaday's wrench logo, designed by Arya Voronova (CRImier) and written up on Hackaday in October 2022 as a showcase for KiCad 6's then-new ability to import SVG artwork directly into a PCB footprint -- that's how the wrench outline and the negative-space "eyes" were drawn. Rather than doing anything on its own, the board offers a grid of 1.27mm-pitch, ground-fill-connected SMD pads sized for passives, SOIC-style ICs, and even larger castellated modules such as an ESP32-WROOM, so builders bodge together whatever circuit they like. Two 0805 LED footprints sit behind transparent cutouts in the eyes, lighting up if populated.

It follows the SAO v1.69bis (6-pin) standard and connects like any other add-on, with both SMD and through-hole header options. The hardware is fully open: KiCad 6 project files, schematic, PCB layout, and gerbers are published on GitHub, along with front and back photos of an assembled unit; the README notes the design is untested with no fitness guarantees. No pricing, production quantity, or distribution details were found -- the write-up reads as a personal design shared for others to fab rather than something sold or handed out at scale, so those fields are left unknown here.
