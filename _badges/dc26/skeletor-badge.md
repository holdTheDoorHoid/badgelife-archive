---
title: Skeletor Badge
id: dc26-skeletor-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Dr.n0psl3d
  url: https://github.com/DrN0psl3d
summary: A hand-built pixel-art skull badge with an ATtiny85, 8 addressable RGB LEDs, and 20 more discrete red/green LEDs, made by Dr.n0psl3d for DEF CON 26 (2018).
functions: Cycles at random through several LED animation modes — a rainbow chase, a bidirectional "chaser" effect, blink patterns, and a Morse-code message spelling out "DEFCON" (the firmware also defines "RTG"/RedTeamGriffin and "DR" Morse patterns, but a bug in the code means only the DEFCON pattern ever actually plays).
look:
  colors:
  - black
  - white
  shape: skull
  themes:
  - skull
  - pop culture
  - tv
tech:
  mcu: ATtiny85
  leds:
    count: 28
    type: WS2812B
    note: 8x WS2812B addressable RGB LEDs (LED1-8) plus 10 discrete red LEDs (LTST-C170KRKT) and 10 discrete green 0805 LEDs, driven directly off two GPIO pins.
  display: none
  connectivity: []
  battery: 2-pin header for a battery (cell type not specified in sources)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/DrN0psl3d/Skeletor
  firmware_url: https://github.com/DrN0psl3d/Skeletor/blob/master/skeletor.ino
  eda_tool: null
  bom_url: https://github.com/DrN0psl3d/Skeletor/blob/master/LCSC_Exported_20180818_063906.xlsx
  license: MIT
  notes: Firmware is Arduino (.ino) code using the Adafruit_NeoPixel library; an LCSC-exported BOM spreadsheet is included in the repo. No PCB design files (Gerbers/schematic source) are published, only the firmware and BOM.
links:
- label: github.com/DrN0psl3d/Skeletor
  url: https://github.com/DrN0psl3d/Skeletor
  kind: repo
images:
- file: assets/images/badges/dc26/skeletor-badge/af6f15b14b.jpg
  source: "https://github.com/DrN0psl3d/Skeletor"
  credit: "Dr.n0psl3d"
  caption: "Skeletor badge PCB, silkscreened with 'skeletor v1.0' and 'Crafted by: Dr.n0psl3d #RedTeamGriffin'"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/DrN0psl3d/Skeletor
  title: Skeletor Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''unknown''.'
- kind: url
  url: https://raw.githubusercontent.com/DrN0psl3d/Skeletor/master/skeletor.ino
  title: skeletor.ino
  accessed: '2026-09-07'
  note: 'Firmware source: 8x WS2812B (Adafruit_NeoPixel, pin 3), 2 discrete LEDs on pins 1/4, Morse-code and animation routines; code header dated 2018-07-27, version 1.0, shortly before DEF CON 26 (Aug 9-12 2018).'
- kind: url
  url: https://raw.githubusercontent.com/DrN0psl3d/Skeletor/master/LCSC_Exported_20180818_063906.xlsx
  title: LCSC BOM export
  accessed: '2026-09-07'
  note: 'Bill of materials: ATTINY85-20SU MCU, 8x WS2812B, 10x LTST-C170KRKT red LEDs, 10x 0805 green LEDs, USBASP ISP header, battery header.'
- kind: url
  url: https://i.imgur.com/SMuqEMv.jpg
  title: Skeletor badge photo (linked from README)
  accessed: '2026-09-07'
  note: 'Photo confirms a black PCB with white silkscreen in an 8-bit pixel-art skull shape, text "skeletor v1.0" and "Crafted by: Dr.n0psl3d #RedTeamGriffin".'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched github.com/DrN0psl3d/Skeletor, its README, skeletor.ino, and the LCSC BOM xlsx directly. All tech fields, the license, the image, and the DC26/2018 dating (firmware dated 2018-07-27, one week before DEF CON 26, Aug 9-12 2018) check out. One factual correction made: the entry originally said the Morse routine spells out "DEFCON", "RTG", and "DR" as three distinct working messages. Reading skeletor.ino shows the morse() function takes a pattern argument but its body is hardcoded to always read from the module-level defcon_morse_pattern array, ignoring the argument — so calling morse(rtg_morse_pattern) or morse(dr_morse_pattern) actually plays the DEFCON pattern too. The RTG and DR arrays are defined in source but never actually rendered; functions and body text were corrected to say so. (Separately, the loop()''s switch statement also has no break statements, so a chosen case falls through into every case after it — a further quirk of the animation cycling not covered above since it does not contradict any specific claim in the entry.) Event corrected from "other" to dc26 by the prior researcher on the strength of the firmware''s defcon_morse_pattern name and the July 2018 code date; no independent third-party coverage (press, forums, storefront) was found beyond the maker''s own GitHub repo, so confidence stays medium rather than high. Price, quantity made, and distribution method remain unknown/empty because no source states them. No PCB design files (Gerbers/schematic) are published, only firmware and BOM.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/skeletor-badge/
---

Skeletor Badge is a self-built electronic badge made by the hardware hacker known as Dr.n0psl3d, shaped as an 8-bit pixel-art skull (visually referencing the Masters of the Universe villain Skeletor) on a black PCB with white silkscreen. It was built for DEF CON 26 in August 2018: the firmware is dated one week before Aug 9, and one of its built-in Morse-code messages is literally named for DEF CON in the source code.

Under the hood it runs on an ATtiny85 microcontroller flashed via a USBASP header, driving eight WS2812B addressable RGB LEDs plus twenty more discrete red and green LEDs (ten of each) directly from two GPIO pins. On power-up it randomly picks between several light shows: a NeoPixel rainbow fade, a bidirectional LED chaser, simple blink patterns at varying speed, and a Morse-code message. The source code defines three Morse patterns — one for "DEFCON", one for "RTG" (apparently short for "RedTeamGriffin," the handle silkscreened onto the board alongside the maker's name), and one for "DR" — but the `morse()` function has a bug that makes it always play the DEFCON pattern regardless of which one is selected, so in practice the badge never actually spells out "RTG" or "DR". The maker's own README is characteristically self-deprecating ("This is some code for a badge I made? It's horrible, please don't copy this shit lol").

The GitHub repository (MIT-licensed) publishes the Arduino firmware and an LCSC-exported bill of materials, but no schematic or Gerber files, so the badge's electrical design can be inferred from the BOM and code but not fully reproduced from what's public. No information was found on how many were made, whether it was sold or given away, or who besides the maker wore one.
