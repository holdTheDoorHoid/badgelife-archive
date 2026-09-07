---
title: Llama SAO
id: dc26-llama-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: compukidmike
  url: https://github.com/compukidmike
summary: 'A last-minute, just-for-fun SAO shaped like a llama, built from two LEDs and a resistor.'
functions: 'Lights two LEDs; no microcontroller or other logic.'
look:
  colors:
  - white
  - black
  shape: llama
  themes:
  - animal
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 'Two LEDs and a resistor; no driver IC or MCU.'
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/compukidmike/DC26/tree/master/Llama%20SAO
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/compukidmike/DC26/tree/master/Llama%20SAO
  url: https://github.com/compukidmike/DC26/tree/master/Llama%20SAO
  kind: repo
- label: compukidmike on GitHub
  url: https://github.com/compukidmike
  kind: repo
images:
- file: assets/images/badges/dc26/llama-sao/dba86438dc.jpg
  source: "https://github.com/compukidmike/DC26/tree/master/Llama%20SAO"
  credit: "compukidmike"
  caption: "Llama SAO PCB, white soldermask with black silkscreen"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/DC26/tree/master/Llama%20SAO
  title: Llama SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc26''.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/DC26/master/Llama%20SAO/Readme.md
  title: 'Llama SAO Readme.md'
  accessed: '2026-09-07'
  note: 'Maker''s own readme: describes it as a last-minute for-fun SAO with 2 LEDs and a resistor, white soldermask/black silkscreen, and a note about boardhouses stripping silkscreen over bare copper.'
- kind: url
  url: https://github.com/compukidmike/DC26
  title: 'compukidmike/DC26: DEFCON 26 Projects'
  accessed: '2026-09-07'
  note: 'Confirms repo is compukidmike''s DEF CON 26 project collection, GPL-3.0 licensed, includes Gerbers/KiCad files/BOM for the Llama SAO.'
- kind: url
  url: https://www.tindie.com/stores/compukidmike/
  title: 'MKFactor (compukidmike) on Tindie'
  accessed: '2026-09-07'
  note: 'compukidmike runs MKFactor with his wife; general context on the maker, no Llama SAO listing found there.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own readme and repo confirm what it is, that it is a DIY-only 2-LED-and-resistor SAO with full KiCad/Gerber/BOM files, and that it predates any commercial listing. No price, quantity, or distribution details were found anywhere (Tindie store search turned up no Llama SAO listing) -- it reads as a one-off the maker made and shared as open hardware rather than something sold or handed out at DEF CON 26, but no source states that explicitly, so availability is left unknown rather than guessed.'
last_modified_date: '2026-09-07'
---

The Llama SAO is a small, deliberately simple add-on that compukidmike (of MKFactor) built for DEF CON 26 in 2018. By the maker's own description it was "a last minute SAO that was just for fun" -- just two LEDs and a resistor, with no microcontroller or other logic. The board uses white soldermask with black silkscreen, and the readme calls out a fabrication quirk worth knowing for anyone reproducing it: some board houses strip silkscreen that overlaps bare copper, which would spoil the look of the design.

The project is fully open: the GitHub repository (compukidmike/DC26, under GPL-3.0) includes the KiCad schematic and layout files, Gerber manufacturing files, and a bill of materials spreadsheet, alongside a single photo of the finished board. No information was found on price, quantity produced, or how (or whether) it was distributed at the con -- it may simply have been a personal project the maker shared as open hardware rather than a badge that was sold or given away.

## Make your own

The repository (linked above) has everything needed to reproduce the board: KiCad Files/ for the schematic and layout, Gerbers/ ready to send to a fab, and Llama SAO BOM.xlsx listing the two LEDs and resistor. Order boards with white soldermask and black silkscreen, and confirm with the board house that they won't strip silkscreen overlapping bare copper, per the maker's note.
