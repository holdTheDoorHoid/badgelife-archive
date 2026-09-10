---
title: Etch sAo Sketch
id: supercon-2024-etch-sao-sketch
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Andy Geppert (ageppert)
  url: https://github.com/ageppert
summary: An Etch A Sketch-style SAO with a 1.5-inch 128x128 grayscale SSD1327 OLED, two potentiometer knobs with 3D-printed caps, and a LIS3DH 3-axis accelerometer, all reachable over I2C; V1.0 was shared at Hackaday Supercon 8 (2024) and entered in its SAO contest, with a V1.3 run manufactured by Elecrow for Hackaday Europe 2025.
functions: Draw on the OLED using the two analog potentiometer knobs; the accelerometer can also feed motion-based input. The maker notes the analog controls are suited to simple games like Pong or Snake when paired with a capable host MCU.
look:
  colors:
  - red
  shape: rectangle
  themes:
  - retro computer
  - art
  - learn to solder
tech:
  mcu: none
  leds: null
  display: 1.5" 128x128 grayscale OLED (SSD1327)
  connectivity:
  - i2c
  inputs:
  - accelerometer
  battery: powered by host badge
  sao_version: v1
get_one:
  price: $29
  price_usd: 29
  quantity: ''
  availability: limited
  availability_note: Tindie listing showed only 3 units remaining as of 2026-09-07
  distribution:
  - purchase
  where: Sold assembled with a protective case on Tindie (V1.0); a V1.3 run was made by Elecrow and given out at Hackaday Europe 2025
make_your_own:
  open_source: true
  hardware_url: https://github.com/ageppert/SAO_Etch_sAo_Sketch
  firmware_url: https://github.com/ageppert/SAO_Etch_sAo_Sketch
  eda_tool: null
links:
- label: github.com/ageppert/SAO_Etch_sAo_Sketch
  url: https://github.com/ageppert/SAO_Etch_sAo_Sketch
  kind: repo
- label: hackaday.io/project/197581-etch-sao-sketch
  url: https://hackaday.io/project/197581-etch-sao-sketch
  kind: hackaday
- label: www.tindie.com/products/36383
  url: https://www.tindie.com/products/36383/
  kind: store
- label: github.com/ageppert/SAO_Sketch
  url: https://github.com/ageppert/SAO_Sketch
  kind: repo
images:
- file: assets/images/badges/supercon-2024/etch-sao-sketch/0c70999b1d.jpg
  source: https://github.com/ageppert/SAO_Etch_sAo_Sketch
  credit: Andy Geppert (ageppert)
  caption: Etch sAo Sketch V1.0, shared at Hackaday Supercon 8 (2024)
- file: assets/images/badges/supercon-2024/etch-sao-sketch/10bec6ebca.jpg
  source: https://www.tindie.com/products/36383/
  credit: Andy Geppert (ageppert)
  caption: Assembled Etch sAo Sketch with protective case, sold on Tindie
- file: assets/images/badges/supercon-2024/etch-sao-sketch/fac7f899d1.jpg
  source: https://hackaday.io/project/197581-etch-sao-sketch
  credit: Andy Geppert
  caption: Etch sAo Sketch SAO with OLED display and knobs
- file: assets/images/badges/supercon-2024/etch-sao-sketch/5ca5e164b0.jpg
  source: https://www.tindie.com/products/36383/
  credit: Machine Ideas, LLC
  caption: Etch sAo Sketch assembled with case, drawing a heart on the OLED
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/ageppert/SAO_Etch_sAo_Sketch
  title: Etch sAo Sketch
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/ageppert/SAO_Etch_sAo_Sketch
  title: 'ageppert/SAO_Etch_sAo_Sketch: README'
  accessed: '2026-09-07'
  note: Confirmed version history (V1.0 through V1.3), event tie-ins, I2C pull-up resistor errata, open-source status, and image files.
- kind: url
  url: https://hackaday.io/project/197581-etch-sao-sketch
  title: Etch sAo Sketch - Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed submission to the Supercon 8 SAO contest, PCB dimensions (40x50mm, 2-layer), copper-ball alignment spheres, and October 2024 prototype status.
- kind: url
  url: https://www.tindie.com/products/36383/
  title: SAO Etch sAo Sketch OLED (WITH CASE AND ASSEMBLED) - Tindie
  accessed: '2026-09-07'
  note: Confirmed $29 price, low stock (3 units), assembled-with-case format, and that the host MCU is not included.
- kind: url
  url: https://github.com/ageppert/SAO_Sketch
  title: ageppert/SAO_Sketch
  accessed: '2026-09-07'
  note: Confirmed this is a companion repo used for the Hackaday Europe 2025 Elecrow production run; points back to the primary Etch sAo Sketch repo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: EDA tool and total production quantity are not stated on any of the maker's pages. The board itself has no onboard MCU — it is a passive I2C peripheral (OLED + pots + accelerometer) meant to be driven by the host badge or the maker's separate SAO Demo Controller. Multiple hardware revisions exist (V1.0 Supercon 2024/Tindie, V1.1 small Tindie batch, V1.2 unbuilt, V1.3/V1.3.1 Elecrow run for Hackaday Europe 2025); this entry covers the V1.0 Supercon 2024 version per the sheet, with later revisions noted for context. Merged with duplicate entry 'Etch sAo Sketch' (supercon-2024-etch-sao-sketch-2).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2024/etch-sao-sketch-2/
---

The Etch sAo Sketch is a Simple Add-On (SAO) that reimagines the classic Etch-A-Sketch as a small I2C peripheral board. A 1.5-inch 128x128 grayscale OLED (SSD1327) sits on the front, driven by two potentiometer knobs with custom 3D-printed caps that let a host badge draw on the screen, while an onboard LIS3DH 3-axis accelerometer adds motion-based input. The board carries no microcontroller of its own — it relies on the host badge (or the maker's separate SAO Demo Controller) to read the pots and accelerometer over I2C and push pixels to the display. A distinctive touch is the use of small copper balls as mechanical alignment spheres between the OLED and main PCB.

Andy Geppert (ageppert) first shared V1.0 at Hackaday Supercon 8 in 2024, where it was entered into that event's SAO contest, and sold a small assembled run (with a protective case) on Tindie for $29. The GitHub repo documents several follow-on hardware revisions: V1.1 tweaked the pot wiring and header height for a small Tindie batch, V1.2 was designed but never built, and V1.3/V1.3.1 was manufactured by Elecrow and distributed to attendees at Hackaday Europe 2025 in Berlin, complete with an Elecrow logo on the board. Each revision after V1.0 also removed a pair of I2C pull-up resistors to fix combined-pull-up conflicts with host badges.

Hardware design files and firmware/demo code are published on GitHub, making the project fully open source, though the specific EDA tool used is not stated on the maker's pages.

## Notes merged from the duplicate entry "Etch sAo Sketch"

The Etch sAo Sketch is Andy Geppert's entry to the Supercon 8 (2024) SAO contest, riffing on the classic Etch-A-Sketch toy as a plug-in add-on for a badge's SAO header. It has no microcontroller of its own: a 1.5-inch 128x128 grayscale SSD1327 OLED and an LIS3DH 3-axis accelerometer sit on the I2C bus, and two potentiometers (fitted with 3D-printed knob caps) feed position into the accelerometer's analog inputs, so whatever host badge is plugged in does the actual drawing logic. Because it just exposes raw I2C peripherals, hosts have run things on it beyond Etch-A-Sketch drawing, including simple games like Pong and Snake.

The design has gone through several hardware revisions: V1.0 was the original Supercon 8 board, V1.1 was a small Tindie batch with a refined potentiometer range and SAO header tweaks, and V1.3 was manufactured by Elecrow for Hackaday Europe 2025 with the I2C pull-up resistors removed to fix a compatibility issue caused by excessive combined pull-up resistance when stacked with a host badge's own pull-ups. As of this research pass it is sold pre-assembled with a case through Tindie (seller Machine Ideas, LLC) for $29, with a separate "SAO Demo Controller" add-on available so the SAO can run standalone demo firmware without a host badge.

Hardware design files and firmware are published on GitHub (ageppert/SAO_Etch_sAo_Sketch), covering the schematic/PCB source, Arduino firmware, and mechanical files for the 3D-printed knob caps and case, though the repository does not spell out a specific open-source license, BOM file, or EDA tool by name.
