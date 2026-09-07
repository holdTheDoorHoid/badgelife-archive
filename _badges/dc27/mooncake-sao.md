---
title: Mooncake SAO
id: dc27-mooncake-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: cybr1d (Jeremy Ward)
  url: https://github.com/cybr1d-cybr1d
summary: A simple LED-only Shitty Add-On shaped like the character Mooncake from the cartoon Final Space, built on the SAO v1.69bis 6-pin connector as the maker's first KiCad PCB for DEF CON 27.
functions: 'LED-only; no microcontroller or blink logic, LEDs light directly off the SAO header power.'
look:
  colors: [green, black]
  shape: null
  themes: [tv, cartoon, mascot]
tech:
  mcu: none
  leds:
    count: 8
    type: discrete
    note: Eight discrete LEDs (D1-D8), generic KiCad Device:LED symbols; no driver IC or microcontroller.
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
  open_source: yes
  hardware_url: https://github.com/cybr1d-cybr1d/Mooncake-SAO
  firmware_url: null
  eda_tool: KiCad
  gerbers_url: https://github.com/cybr1d-cybr1d/Mooncake-SAO
  fab_url: https://www.pcbway.com/project/shareproject/DEF_CON_27_Mooncake_Shitty_Add_On.html
  license: CC BY-SA 3.0
  notes: Repo contains full KiCad schematic and Gerber/drill files; PCBWay shared-project page mirrors the same design for reordering.
links:
- label: github.com/cybr1d-cybr1d/Mooncake-SAO
  url: https://github.com/cybr1d-cybr1d/Mooncake-SAO
  kind: repo
- label: www.pcbway.com/project/shareproject/DEF_CON_27_Mooncake_Shitty_Add_On.html
  url: https://www.pcbway.com/project/shareproject/DEF_CON_27_Mooncake_Shitty_Add_On.html
  kind: fab
images:
  - file: assets/images/badges/dc27/mooncake-sao/65ef83b1de.png
    source: "https://github.com/cybr1d-cybr1d/Mooncake-SAO"
    credit: "Jeremy Ward (cybr1d)"
    caption: "Front of the Mooncake SAO PCB"
  - file: assets/images/badges/dc27/mooncake-sao/a9ee6e01c6.png
    source: "https://github.com/cybr1d-cybr1d/Mooncake-SAO"
    credit: "Jeremy Ward (cybr1d)"
    caption: "Back of the Mooncake SAO PCB showing the SAO header and LEDs"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/cybr1d-cybr1d/Mooncake-SAO
  title: 'cybr1d-cybr1d/Mooncake-SAO: A shitt addon of the character Mooncake from Final Space'
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://www.pcbway.com/project/shareproject/DEF_CON_27_Mooncake_Shitty_Add_On.html
  title: DEF CON 27 Mooncake Shitty Add-On - Share Project - PCBWay
  accessed: '2026-09-07'
  note: Confirmed maker Jeremy Ward (UK), DEF CON 27 (2019), v1.69bis SAO standard, 2-layer 50x55mm PCB with green solder mask/black silkscreen, CC BY-SA 3.0 license, and that it was the maker's first KiCad PCB.
- kind: url
  url: https://raw.githubusercontent.com/cybr1d-cybr1d/Mooncake-SAO/master/Mooncake.sch
  title: Mooncake.sch (KiCad schematic)
  accessed: '2026-09-07'
  note: Schematic lists 8 discrete LEDs (D1-D8) as generic Device:LED symbols with no microcontroller or driver IC.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No price, quantity made, or distribution method (free drop vs. sale) found in any source; availability is unknown. No separate maker post (Twitter/Hackaday) beyond the repo and PCBWay page was located.
last_modified_date: '2026-09-07'
---

The Mooncake SAO is a Shitty Add-On shaped like Mooncake, the round blue-and-white companion creature from the animated series Final Space. Maker Jeremy Ward, who posts as cybr1d, built it for DEF CON 27 in 2019 and describes it on the project's PCBWay page as his first attempt at designing a PCB and learning KiCad, put together with help from instructional videos.

The board is a straightforward two-layer, 50 x 55 mm PCB with a green solder mask and black silkscreen, connecting to a host badge through the SAO v1.69bis 6-pin header. It carries eight discrete LEDs (D1 through D8) directly wired to the header power with no microcontroller, driver chip, or blink logic — the character's design shows through the silkscreen and LED placement rather than any animated effect.

Ward published the full KiCad schematic and manufacturing files (Gerbers and drill files) on GitHub under a CC BY-SA 3.0 license, and mirrored the same design as a shared project on PCBWay so others could reorder the boards. No information was found on how many were made, whether they were sold or given away, or their price.
