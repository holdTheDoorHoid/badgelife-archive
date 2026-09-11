---
title: reDOT_RGB
id: supercon-2024-redot-rgb
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Alex
  url: https://hackaday.io/tinyledmatrix
summary: A miniature SAO with a 5x7 RGB LED matrix in an 8x11mm PCB, driven by a single ATtiny816.
functions: Drives 35 individually addressable RGB LEDs as a tiny scrolling/animated pixel display; plugs into a badge's SAO header.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
tech:
  mcu: ATtiny816
  leds:
    count: 35
    type: WS2812B
    note: 1010-size RGB LEDs arranged as a 5x7 matrix
  display: LED matrix 5x7
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: Submitted to the Supercon 8 SAO Contest; no separate storefront found.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/tinyledmatrix/reDOT_RGB
  firmware_url: https://github.com/tinyledmatrix/reDOT_RGB
  eda_tool: KiCad
images:
- file: assets/images/badges/supercon-2024/redot-rgb/61edaf4c17.jpg
  source: https://hackaday.io/project/197898-redotrgb
  credit: Alex (tinyledmatrix)
  caption: reDOT_RGB assembled SAO PCB, 5x7 RGB LED matrix
- file: assets/images/badges/supercon-2024/redot-rgb/93d6fb97ac.jpg
  source: https://github.com/tinyledmatrix/reDOT_RGB
  credit: Alex (tinyledmatrix)
  caption: reDOT_RGB PCB shown for scale
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/197898-redotrgb
  title: reDOT_RGB
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 8 Add-On Contest — honorable mention; 5x7 RGB LED matrix with ATtiny816, 8x11mm''.'
- kind: url
  url: https://hackaday.io/project/197898-redotrgb
  title: reDOT_RGB (hackaday.io project page)
  accessed: '2026-09-07'
  note: Confirmed maker handle (tinyledmatrix), event (Supercon 8 SAO Contest, submitted 2024), chip (ATtiny816-M), 35 WS2812-style LEDs, 8x11mm PCB, GitHub repo link, and gallery photos.
- kind: url
  url: https://github.com/tinyledmatrix/reDOT_RGB
  title: tinyledmatrix/reDOT_RGB
  accessed: '2026-09-07'
  note: Confirmed KiCad hardware files and firmware are published in-repo; README description and PCB photo. No explicit license or BOM/gerbers file found in fetched content.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No contest placement (win/honorable mention) could be confirmed from the fetched Hackaday page content, despite the sheet import note claiming "honorable mention" — left status generic pending a source that states it. No pricing, quantity, or license information found; no evidence of a separate storefront, so availability left unknown. Sheet originally filed this under Supercon 2025, but the project was built for the Supercon 8 (2024) SAO Contest, so event corrected to supercon-2024.
last_modified_date: '2026-09-10'
redirect_from:
- /badges/supercon-2025/redot-rgb/
model:
  file: assets/models/supercon-2024/redot-rgb.glb
  method: kicad
  source_file: reDOT_RGB.kicad_pcb
  generated: '2026-09-10'
  bytes: 112536
---

reDOT_RGB is a tiny SAO (Simple Add-on) built by Alex, who goes by tinyledmatrix, for the Supercon 8 SAO Contest in 2024. The board packs a 5x7 grid of 35 individually addressable RGB LEDs into an 8x11mm PCB, driven by a single ATtiny816 microcontroller, and connects to a host badge through a standard 4-pin SAO header. It follows on from an earlier project, reDOT_smart, keeping the same size and LED pitch.

Hardware design files (KiCad) and firmware are published on GitHub at tinyledmatrix/reDOT_RGB, alongside build photos; the Hackaday.io project page carries the fuller writeup and gallery. No license file, bill of materials, or storefront listing was found, so open-source status is marked partial and pricing/availability are left unknown.
