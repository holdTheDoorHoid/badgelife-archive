---
title: DC503_SAO — DC503's Shitty Add-On for Defcon 26
id: dc26-dc503-sao-dc503-s-shitty-add-on-for-defcon-26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: DC503
  url: https://github.com/office-deskjet/DC503_SAO
summary: A DEF CON 26 SAO shaped like the state of Oregon, made by the DC503 (Portland, OR) DEF CON group, with 12 charlieplexed LEDs behind Portland-themed icons and a heart-shaped pushbutton.
functions: 'A single button cycles the LEDs through five modes: slow, medium, and fast round-robin blinking, then medium and fast random blinking, looping back to slow.'
look:
  colors:
  - purple
  - black
  - gold
  shape: state outline
  themes:
  - pop culture
  - beer
  - food
  - logo
tech:
  mcu: ATtiny85
  leds:
    count: 12
    type: charlieplexed
    note: 12 through-hole LEDs charlieplexed off 4 ATtiny85 I/O pins, one LED behind each icon pad
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
  hardware_url: https://github.com/office-deskjet/DC503_SAO/tree/master/HW
  firmware_url: https://github.com/office-deskjet/DC503_SAO/tree/master/FW
  gerbers_url: https://github.com/office-deskjet/DC503_SAO/tree/master/HW/GERBERS
  eda_tool: KiCad
links:
- label: github.com/office-deskjet/DC503_SAO
  url: https://github.com/office-deskjet/DC503_SAO
  kind: repo
images:
- file: assets/images/badges/dc26/dc503-sao-dc503-s-shitty-add-on-for-defcon-26/709e4299e9.jpg
  source: https://github.com/office-deskjet/DC503_SAO
  credit: DC503 (office-deskjet)
  caption: 'Assembled DC503 SAO: Oregon-shaped PCB with 12 charlieplexed LEDs behind Portland-themed icons and a center pushbutton'
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/office-deskjet/DC503_SAO
  title: DC503_SAO — DC503's Shitty Add-On for Defcon 26
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 26''.'
- kind: url
  url: https://raw.githubusercontent.com/office-deskjet/DC503_SAO/master/README.md
  title: DC503_SAO README
  accessed: '2026-09-07'
  note: Confirms project name and repo layout (ART/FW/HW folders); links the assembled-board photo SOA.png.
- kind: url
  url: https://raw.githubusercontent.com/office-deskjet/DC503_SAO/master/FW/DC503_SAO_FW/DC503_SAO_FW.ino
  title: DC503_SAO_FW.ino
  accessed: '2026-09-07'
  note: Firmware source confirms ATtiny85 target (F_CPU 8MHz), 12 charlieplexed LEDs across 4 pins, one pushbutton on a pin-change interrupt cycling five blink/random speed states.
- kind: url
  url: https://raw.githubusercontent.com/office-deskjet/DC503_SAO/master/HW/README.md
  title: DC503_SAO HW README
  accessed: '2026-09-07'
  note: Confirms KiCad (v4.07, upgraded to v5.0) as the EDA tool and links a charlieplexing tutorial, corroborating the LED wiring.
- kind: url
  url: https://raw.githubusercontent.com/office-deskjet/DC503_SAO/master/SOA.png
  title: SOA.png (assembled board photo)
  accessed: '2026-09-07'
  note: 'Source photo of the assembled SAO: Oregon-outline PCB (purple/black soldermask, gold-plated pads), Portland-themed icon set (bike, beer, donut, bridge, rain cloud, bearded hipster), heart-shaped button cutout, LiPo pouch cell visible in the background.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: DC503 is the DEF CON group for the Portland, Oregon area (area code 503); the SAO's Oregon-state outline and local-culture icon set (bike, beer, Voodoo-style donut, bridge, rain, hipster beard) reflect that. No price, quantity made, or distribution channel found anywhere in the repo; this looks like a group-made giveaway/trade SAO rather than a sold item, but that is inferred, not stated, so get_one fields are left empty. No separate storefront, Hackaday.io page, or press coverage found. Web search budget was exhausted before additional corroborating searches could run.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc26/dc503-sao-dc503-s-shitty-add-on-for-defcon-26.glb
  method: gerber
  source_file: HW/DC503_SAO.kicad_pcb
  generated: '2026-09-07'
  bytes: 186752
  size_mm:
  - 63.1
  - 45.1
---

DC503_SAO is a Shitty Add-On made for DEF CON 26 (2018) by DC503, the DEF CON group for the Portland, Oregon area (the group's name comes from the 503 area code). The PCB is cut in the outline of the state of Oregon, finished in a purple-and-black soldermask with gold-plated pads, and it carries twelve round icon pads celebrating Portland-area culture: a bicycle, a beer mug, a donut, a bridge, a rain cloud, and a bearded, glasses-wearing hipster, alongside pads reading "DC503." A pushbutton sits inside a heart-shaped cutout at the center of the board.

Each icon pad backs one of twelve LEDs, charlieplexed across just four I/O pins of an ATtiny85 running at 8 MHz. Pressing the button steps through five lighting modes in a loop: slow, medium, and fast round-robin cycling through the LEDs, followed by medium and fast random flashing, debounced in software via a pin-change interrupt.

The project is fully open: the repository publishes KiCad schematic/PCB source and Gerbers for the hardware, Arduino sketches for the firmware (including a standalone charlieplexing test sketch), and the vector art used for the icon set. No price, production quantity, or sale/giveaway channel is documented anywhere in the repo, so those fields are left blank rather than guessed.

## Make your own

The hardware is in `HW/` as KiCad 4/5 schematic and PCB files with Gerbers included, ready to send to a fab. The firmware is an Arduino sketch in `FW/DC503_SAO_FW/DC503_SAO_FW.ino`, built for an ATtiny85 programmed via an Arduino-as-ISP setup (the repo's FW notes link the standard ATtiny85-on-Arduino-IDE tutorials). A separate `FW/chariplex_test` sketch isolates the charlieplexing logic for bring-up testing.
