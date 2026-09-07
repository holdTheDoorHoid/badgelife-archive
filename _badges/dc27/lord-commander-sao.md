---
title: Lord Commander SAO
id: dc27-lord-commander-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: cybr1d-cybr1d
  url: https://github.com/cybr1d-cybr1d
summary: A Shitty Add-On PCB depicting Lord Commander, the villain from the animated series Final Space, made by Jeremy Ward (cybr1d) as his second SAO for DEF CON 27.
functions: 'Purely decorative/passive: seven LEDs wired in series to the SAO connector''s power pins, with a current-limiting resistor. No microcontroller or independent power.'
look:
  colors:
  - purple
  shape: null
  themes:
  - sci-fi
  - tv
  - villain
tech:
  mcu: none
  leds:
    count: 7
    type: discrete
    note: Seven 1206 SMD LEDs (D1-D7) wired in series with a single resistor, driven from the SAO connector's power rail; no microcontroller.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/cybr1d-cybr1d/Lord-Commander-SAO
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/cybr1d-cybr1d/Lord-Commander-SAO
  url: https://github.com/cybr1d-cybr1d/Lord-Commander-SAO
  kind: repo
- label: 'PCBWay: Lord Commander DEFCON 27 Shitty Add-On'
  url: https://www.pcbway.com/project/shareproject/Lord_Commander_DEFCON_27_Shitty_Add_On.html
  kind: fab
images:
  - file: assets/images/badges/dc27/lord-commander-sao/921d3b9de4.png
    source: "https://github.com/cybr1d-cybr1d/Lord-Commander-SAO"
    credit: "cybr1d-cybr1d (Jeremy Ward)"
    caption: "Front of the Lord Commander SAO PCB"
  - file: assets/images/badges/dc27/lord-commander-sao/36062b6e57.jpg
    source: "https://github.com/cybr1d-cybr1d/Lord-Commander-SAO"
    credit: "cybr1d-cybr1d (Jeremy Ward)"
    caption: "Assembled Lord Commander SAO board"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/cybr1d-cybr1d/Lord-Commander-SAO
  title: 'cybr1d-cybr1d/Lord-Commander-SAO: A shitty addon of the character Lord Commander from Final Space'
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://api.github.com/repos/cybr1d-cybr1d/Lord-Commander-SAO/contents/
  title: Lord-Commander-SAO repository file listing
  accessed: '2026-09-07'
  note: Confirmed KiCad schematic, Gerber and drill files, and photo filenames.
- kind: url
  url: https://raw.githubusercontent.com/cybr1d-cybr1d/Lord-Commander-SAO/master/Lord%20Commander.sch
  title: Lord Commander.sch (KiCad schematic)
  accessed: '2026-09-07'
  note: Schematic shows a Badgelife shitty_connector_v1.69bis 2x3 header, one resistor and seven discrete LEDs (D1-D7) in series, no MCU.
- kind: url
  url: https://www.pcbway.com/project/shareproject/Lord_Commander_DEFCON_27_Shitty_Add_On.html
  title: Lord Commander DEFCON 27 Shitty Add-On - Share Project - PCBWay
  accessed: '2026-09-07'
  note: 'Identifies the maker as Jeremy Ward (UK), confirms DEF CON 27 (2019) and that this was his second SAO; gives board specs: 2-layer, 100x94mm FR-4 1.6mm, purple solder mask, white silkscreen, OSP finish, CC BY-SA 3.0 license.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Event corrected from "other" to dc27 (DEF CON 27, 2019) per the PCBWay listing title and repo creation date. Price, quantity made, and distribution method were not stated anywhere found; left empty. The GitHub repo carries no firmware because the board has none to program.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/lord-commander-sao/
---

The Lord Commander SAO is a Shitty Add-On depicting the villain Lord Commander from the Netflix animated series *Final Space*. It was designed by Jeremy Ward, who publishes as cybr1d-cybr1d on GitHub, as his second SAO for DEF CON 27 in 2019. The board is a purple-soldermask, two-layer, 100 x 94 mm FR-4 PCB with white silkscreen artwork of the character, made to plug into a badge's v1.69bis (6-pin) SAO header.

Electrically the board is passive: seven 1206 SMD LEDs are wired in series through a single current-limiting resistor straight to the SAO connector's power pins, so the LEDs light whenever the host badge supplies power — there is no microcontroller, firmware, or independent battery. The design (KiCad schematic, Gerber, and drill files) is published on GitHub under a CC BY-SA 3.0 license and was also shared on PCBWay, where the fabricator donates 10% of sales back to the designer; neither page states a price, production quantity, or how the boards were distributed at the con.

## Make your own

The GitHub repository (cybr1d-cybr1d/Lord-Commander-SAO) contains the complete KiCad schematic (`Lord Commander.sch`) along with ready-to-fab Gerber and NC drill files for both copper layers, solder mask, silkscreen, and edge cuts. The same Gerbers are mirrored as a shared project on PCBWay for direct ordering.
