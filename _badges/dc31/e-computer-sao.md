---
title: E-Computer SAO
id: dc31-e-computer-sao
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: NilbinSec
  url: https://github.com/NilbinSec
  role: production, PCB design, giveaway
- name: 2PAC
  role: design
- name: Anxious Analyst
  role: design
summary: A free light-up SAO from NilbinSec for DEF CON 31, styled after the "E Computer" prop from the DadFeels web series, in a pink-and-blue PCB.
functions: Lights up (no MCU/logic); plugs into a badge's SAO header.
look:
  colors:
  - pink
  - blue
  shape: rectangle
  themes:
  - retro computer
  - pop culture
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: 1x blue through-hole LED, 2x white side-view SMD LEDs, driven passively through a 100-ohm resistor (no microcontroller)
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: free
  price_usd: 0.0
  quantity: 200
  availability: sold_out
  availability_note: 'checked 2026-09-06: giveaway was a one-time DEF CON 31 drop in 2023, not a standing store listing'
  distribution:
  - free_drop
  where: Given away free at DEF CON 31 (2023) drops announced over NilbinSec's Twitter/X account; 200 made.
make_your_own:
  open_source: true
  hardware_url: https://github.com/NilbinSec/E-Computer-SAO-DC31
  firmware_url: null
  gerbers_url: https://github.com/NilbinSec/E-Computer-SAO-DC31/tree/main/Gerbers
  bom_url: https://github.com/NilbinSec/E-Computer-SAO-DC31
  eda_tool: null
  license: null
  fab_url: https://www.pcbway.com/project/share/Defcon_31_E_Computer_SAO_13834c16.html
  notes: Repo has no LICENSE file; hardware files (BOM, gerbers, build files) are published but licensing terms are unstated.
links:
- label: twitter.com/NilbinSec/status/1678156364013527041
  url: https://twitter.com/NilbinSec/status/1678156364013527041
  kind: social
- label: 'GitHub: NilbinSec/E-Computer-SAO-DC31'
  url: https://github.com/NilbinSec/E-Computer-SAO-DC31
  kind: repo
- label: 'PCBWay project share: Defcon 31 E-Computer SAO'
  url: https://www.pcbway.com/project/share/Defcon_31_E_Computer_SAO_13834c16.html
  kind: fab
- label: 'Reddit: NilbinSec SAO Reveal (r/Defcon)'
  url: https://www.reddit.com/r/Defcon/comments/14vc97p/nilbinsec_sao_reveal/
  kind: social
images:
- file: assets/images/badges/dc31/e-computer-sao/3fa7365213.jpg
  source: https://github.com/NilbinSec/E-Computer-SAO-DC31
  credit: NilbinSec
  caption: The E-Computer SAO PCB, pink and blue soldermask with LED, from the GitHub repo README
- file: assets/images/badges/dc31/e-computer-sao/60a3b43de5.jpg
  source: https://twitter.com/NilbinSec/status/1678156364013527041
  credit: NilbinSec
  caption: NilbinSec's DEF CON 31 reveal tweet photo of the E-Computer SAO
contact: {}
notes: []
status: released
sources:
- kind: sheet
  event: dc31
  row: 63
  updated: '2023-03-20'
- kind: url
  url: https://twitter.com/NilbinSec/status/1678156364013527041
  title: 'NilbinSec on X: reveal of the E Computer SAO for DEF CON 31'
  accessed: '2026-09-06'
  note: Confirms the SAO is based on DadFeels' "E Computer" prop, 200 units given away free, reveal date July 9 2023.
- kind: url
  url: https://github.com/NilbinSec/E-Computer-SAO-DC31
  title: 'GitHub: NilbinSec/E-Computer-SAO-DC31'
  accessed: '2026-09-06'
  note: BOM (LEDs, resistor, SAO adapter), gerbers/build files, credits design to 2PAC and Anxious Analyst.
- kind: url
  url: https://www.pcbway.com/project/share/Defcon_31_E_Computer_SAO_13834c16.html
  title: Defcon 31 E-Computer SAO - PCBWay project share
  accessed: '2026-09-06'
  note: Confirms 200 units produced, ~3% failure rate (a via sheared during through-hole resistor trimming), pink/blue soldermask and silkscreen.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: The SAO is a fan tribute styled after the "E Computer," a prop computer from the DadFeels YouTube/web series (Bardo Industries, in-universe), not a real historical computer. It is a simple passive light-up board (no MCU) with one blue through-hole LED and two white side-view SMD LEDs, connecting via a shrouded 2x3-pin (v1.69bis/v2) SAO header. NilbinSec made 200 and gave them away free at DEF CON 31 drops announced on Twitter/X. Hardware files (BOM, gerbers) are public on GitHub, but no license is stated and there is no firmware since the board has no logic. Design credited to 2PAC and Anxious Analyst.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc31/e-computer-sao.glb
  method: kicad
  source_file: Build Files/AA Design THT Modify.kicad_pcb
  generated: '2026-09-07'
  bytes: 67608
---

NilbinSec's E-Computer SAO is a free giveaway plug-in add-on made for DEF CON 31 in 2023. Its shape and pink-and-blue color scheme are a tribute to the "E Computer," a fictional retro computer prop from Bardo Industries in the DadFeels YouTube/web series, rather than any real vintage machine. The board is entirely passive: one blue through-hole LED and two white side-view SMD LEDs are wired through a single current-limiting resistor, lit whenever the SAO is plugged into a badge's power rail, with no microcontroller or logic on board.

NilbinSec produced 200 units through PCBWay and gave them all away free at drops during the convention, announcing locations over Twitter/X rather than through a storefront. Roughly 3% of the run had a manufacturing defect (a via sheared while trimming a through-hole resistor lead), which NilbinSec repaired by hand with extra solder before the giveaway. The design is credited to team members 2PAC and Anxious Analyst.

## Make your own

NilbinSec published the full bill of materials, gerbers, and build files for the SAO on GitHub (see links). Building one from scratch means sourcing a shrouded 2x3-pin SAO adapter, a blue through-hole LED, two white side-view SMD LEDs, and a 100-ohm resistor, then having the gerbers fabricated (PCBWay's shared project page shows the exact board NilbinSec ordered). No license is stated in the repository, so reuse terms beyond personal builds are unclear.
