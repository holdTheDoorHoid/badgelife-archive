---
title: DEFCON 27 Avocato Shitty Add-On
id: dc27-dc27-avocato-sao-2
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: Jeremy Ward
  url: https://www.pcbway.com/project/member/?bmbno=4F99C1F3-B710-4C
summary: A DEF CON 27 Shitty Add-On shaped like Avocato from the TV series Final Space, using an ATTiny48 to drive 24 LEDs with a button that cycles five blink modes and spinning eye animation, on a 75 x 74 mm blue two-layer board with the standard SAO 2x3 header.
functions: One button cycles through five LED blink/animation modes, including a spinning-eye effect.
look:
  colors:
  - blue
  shape: null
  themes:
  - tv
  - sci-fi
  - pop culture
tech:
  mcu: ATTiny48
  leds:
    count: 24
    type: null
    note: null
  display: null
  connectivity: []
  battery: null
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/cybr1d-cybr1d/Avocato-SAO
  firmware_url: null
  eda_tool: null
  gerbers_url: https://www.pcbway.com/project/shareproject/DEFCON_27_Avocato_Shitty_Add_On.html
  license: CC BY-SA
  fab_url: https://www.pcbway.com/project/shareproject/DEFCON_27_Avocato_Shitty_Add_On.html
  notes: Gerbers, schematic, and drill files are on GitHub; PCBWay project page notes the design is shared under Attribution-ShareAlike.
links:
- label: www.pcbway.com/project/shareproject/DEFCON_27_Avocato_Shitty_Add_On.html
  url: https://www.pcbway.com/project/shareproject/DEFCON_27_Avocato_Shitty_Add_On.html
  kind: fab
- label: github.com/cybr1d-cybr1d/Avocato-SAO
  url: https://github.com/cybr1d-cybr1d/Avocato-SAO
  kind: repo
  archived: https://web.archive.org/web/20250907001236/https://github.com/cybr1d-cybr1d/Avocato-SAO
- label: youtu.be/40Zf4UEdGXA
  url: https://youtu.be/40Zf4UEdGXA
  kind: video
images:
- file: assets/images/badges/dc27/dc27-avocato-sao-2/6dcd78a4f3.jpg
  source: https://www.pcbway.com/project/shareproject/DEFCON_27_Avocato_Shitty_Add_On.html
  credit: Jeremy Ward
  caption: Assembled Avocato SAO board with LED eyes
- file: assets/images/badges/dc27/dc27-avocato-sao-2/561117eeb8.png
  source: https://github.com/cybr1d-cybr1d/Avocato-SAO
  credit: cybr1d-cybr1d / Jeremy Ward
  caption: Avocato SAO PCB front, bare board render
  archived: https://web.archive.org/web/20250907001236/https://github.com/cybr1d-cybr1d/Avocato-SAO
contact: {}
notes: []
status: unknown
sources:
- kind: url
  url: https://www.pcbway.com/project/shareproject/DEFCON_27_Avocato_Shitty_Add_On.html
  title: DEFCON 27 Avocato Shitty Add-On - Share Project - PCBWay
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/cybr1d-cybr1d/Avocato-SAO
  title: cybr1d-cybr1d/Avocato-SAO on GitHub
  accessed: '2026-09-07'
  note: Confirmed hardware files (schematic, Gerbers, drill files, board images) are open source; no firmware or license file found in the repo itself, though the PCBWay page lists CC BY-SA.
  archived: https://web.archive.org/web/20250907001236/https://github.com/cybr1d-cybr1d/Avocato-SAO
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (maker, chip, LED count, button/blink-mode behavior, board size/color) confirmed on the maker's own PCBWay project page and cross-checked against the GitHub repo. Could not find price, quantity made, or a storefront listing anywhere, so get_one fields are left empty/unknown. No SAO header pin-count was stated explicitly; sao_version is inferred from context (2019-era SAOs of this complexity typically use the 6-pin v1.69bis/v2 header) and should be treated as a light inference, not confirmed. The GitHub repo itself does not state a license; CC BY-SA comes only from the PCBWay page text.
last_modified_date: '2026-09-07'
---

The DEFCON 27 Avocato Shitty Add-On is a fan-made SAO shaped like Avocato, the alien bounty hunter from the animated series Final Space. Designer Jeremy Ward, based in the UK, describes it as his first attempt at a more complex SAO: an ATTiny48 drives 24 LEDs across the board, with a single button cycling through five blink/animation modes, including a "spinning eye" effect for Avocato's eyes. The board is a 75 x 74 mm two-layer FR-4 PCB with blue solder mask, white silkscreen, and OSP surface finish, built to the standard SAO header so it plugs into a compatible host badge.

Ward shared the project on PCBWay (posted October 2019, shortly after DEF CON 27) with Gerber files available for anyone to fabricate their own copy, and the hardware design files — schematic, Gerbers, and drill files — are also published on GitHub under the handle cybr1d-cybr1d. A demo video on YouTube shows the LED animation running. No pricing, production quantity, or storefront listing for the badge itself turned up in research, so it is unclear whether it was sold, given away, or made only for the designer's own use.

## Make your own

The GitHub repository (github.com/cybr1d-cybr1d/Avocato-SAO) contains the schematic and Gerber/drill files needed to fabricate the board; the PCBWay project page hosts the same Gerbers directly and can be used to order boards through their fab service. No firmware source was found in the repo, so recreating the LED animation logic would require reverse-engineering it from the ATTiny48 or writing new firmware from scratch.
