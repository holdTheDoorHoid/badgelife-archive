---
title: lucy-sao (Disenchanted character)
id: other-lucy-sao-disenchanted-character
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: ly7erg1c
  url: https://github.com/ly7erg1c
summary: A shaped SAO cut in the silhouette of Luci, the demon-cat sidekick from the animated series Disenchantment.
functions: ''
look:
  colors:
  - gold
  shape: cat
  themes:
  - cat
  - tv
  - pop culture
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
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
  open_source: yes
  hardware_url: https://github.com/ly7erg1c/lucy-sao
  firmware_url: null
  eda_tool: Altium
links:
- label: github.com/ly7erg1c/lucy-sao
  url: https://github.com/ly7erg1c/lucy-sao
  kind: repo
images:
  - file: assets/images/badges/other/lucy-sao-disenchanted-character/a3757e4136.jpg
    source: "https://github.com/ly7erg1c/lucy-sao"
    credit: "ly7erg1c"
    caption: "Lucy SAO, 3D PCB render, front"
  - file: assets/images/badges/other/lucy-sao-disenchanted-character/cbc852997d.jpg
    source: "https://github.com/ly7erg1c/lucy-sao"
    credit: "ly7erg1c"
    caption: "Lucy SAO, PCB layout showing the 4-pin SAO header (J1) and single resistor (R1)"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/ly7erg1c/lucy-sao
  title: lucy-sao (Disenchanted character)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/ly7erg1c/lucy-sao
  title: 'ly7erg1c/lucy-sao: A shitty add on of lucy from disenchanted'
  accessed: '2026-09-07'
  note: 'Repo readme (two renders only, no prose) and file listing confirmed the design files are Altium Designer sources (.PrjPcb/.SchDoc/.PcbDoc) for a shaped board; commit history dated 2023-04-26.'
- kind: url
  url: https://api.github.com/repos/ly7erg1c/lucy-sao/contents/Badge_Cig_Ver%202.0.4
  title: 'Badge_Cig_Ver 2.0.4 folder listing'
  accessed: '2026-09-07'
  note: 'Confirmed contents: schematic, PCB, CAM files, and a manufacturer/production files folder; PCB shows a 4-pin SAO header (J1) and a single resistor (R1), no MCU or LED footprints visible.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'No maker statement, storefront, or press coverage found beyond the bare GitHub repo (description: "a shitty add on of lucy from disenchanted"). No event, price, quantity, or distribution info exists anywhere found. The two committed images are Altium 3D/2D renders, not photos of an assembled unit, so it is unclear whether the board was ever fabricated or handed out at a con. Repo commits are dated 2023-04-26; no specific convention is named, so event is left as "other" per the research guide (no matching event id could be confirmed). LEDs: the board layout shows no LED footprints, only a 4-pin SAO connector (J1) and a single resistor (R1), consistent with a passive/decorative add-on; tech.leds left null rather than guessed as none-with-confidence.'
last_modified_date: '2026-09-07'
---

This is a small SAO (shitty add-on) cut into the silhouette of Luci, the wisecracking demon cat from the Netflix animated series *Disenchantment*. The GitHub repository, published by user ly7erg1c in April 2023, contains only the Altium Designer source files for the board (schematic, PCB layout, and CAM/manufacturing outputs) and two render images — no written description beyond the repo's one-line tagline calling it "a shitty add on of lucy from disenchanted."

The PCB layout shows a standard 4-pin SAO edge connector (labeled J1, with GND and three signal pins) and a single resistor (R1), but no microcontroller or LED footprints are visible in the renders, suggesting this is a passive, decorative SAO rather than an illuminated or interactive one. No information was found about what convention (if any) it was made for, whether it was ever fabricated and handed out, pricing, or quantity — the repository is the only trace of the project online.

Because hardware design files (schematic and PCB) are published in full, `make_your_own.open_source` is set to `yes`; there is no firmware to speak of, consistent with a board that appears to carry no active components.
