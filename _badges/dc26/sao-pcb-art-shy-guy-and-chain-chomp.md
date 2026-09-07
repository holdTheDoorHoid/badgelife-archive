---
title: SAO-PCB-Art (Shy Guy and Chain Chomp)
id: dc26-sao-pcb-art-shy-guy-and-chain-chomp
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: Seamus de Cleir
  url: https://github.com/LifeOnAFarm
  role: designer (GitHub/Twitter handle PotatoNightmare)
summary: A pair of simple, passive Shitty Add-On PCBs shaped like Super Mario characters -- Shy Guy and Chain Chomp -- made for the DEF CON 26 (2018) badgelife scene.
functions: No microcontroller; each board is a passive LED circuit. Chain Chomp lights 5 series LEDs, Shy Guy lights 2, both through a single current-limiting resistor, powered off a host badge's SAO header.
look:
  colors: []
  shape: null
  themes:
  - video games
  - pop culture
  - meme
tech:
  mcu: none
  leds:
    count: null
    type: 1206 LED
    note: Chain Chomp uses 5x 1206 LEDs; Shy Guy uses 2x 1206 LEDs, each board with a single 2512 51-ohm series resistor and no driver IC.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/LifeOnAFarm/SAO-PCB-Art
  firmware_url: null
  eda_tool: KiCad
notes: []
status: released
links:
- label: github.com/LifeOnAFarm/SAO-PCB-Art
  url: https://github.com/LifeOnAFarm/SAO-PCB-Art
  kind: repo
images:
- file: assets/images/badges/dc26/sao-pcb-art-shy-guy-and-chain-chomp/260098806f.jpg
  source: https://github.com/LifeOnAFarm/SAO-PCB-Art
  credit: Seamus de Cleir (LifeOnAFarm / PotatoNightmare)
  caption: Shy Guy SAO PCB art, front
- file: assets/images/badges/dc26/sao-pcb-art-shy-guy-and-chain-chomp/07c3559730.jpg
  source: https://github.com/LifeOnAFarm/SAO-PCB-Art
  credit: Seamus de Cleir (LifeOnAFarm / PotatoNightmare)
  caption: Chain Chomp SAO PCB art, front
contact: {}
sources:
- kind: url
  url: https://github.com/LifeOnAFarm/SAO-PCB-Art
  title: SAO-PCB-Art (Shy Guy and Chain Chomp)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://raw.githubusercontent.com/LifeOnAFarm/SAO-PCB-Art/master/README.md
  title: SAO PCB Art README
  accessed: '2026-09-07'
  note: 'Confirms this is two passive Shitty Add-On designs (Chain Chomp, Shy Guy) made "in the lead up to DefCon 26 #BadgeLife" (2018) by Seamus de Cleir (@PotatoNightmare); lists BOM (headers, 1206 LEDs, 2512 51-ohm resistor) and that svg/schematic/gerber/KiCad files are included under MIT license, crediting @MrTwinkleTwink''s SAO tutorial.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a bundle of two art SAOs (Chain Chomp and Shy Guy) in one repo rather than a single badge; both are fully passive (no MCU, no driver chip) LED boards designed to plug into a DEF CON 26 (2018) badge's SAO header. No price, quantity made, or distribution details were found -- this looks like a personal/hobby release of open-source design files rather than a sold product, so get_one fields are left empty. No storefront, Hackaday.io page, or press coverage was found for it.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/sao-pcb-art-shy-guy-and-chain-chomp/
model:
  file: assets/models/dc26/sao-pcb-art-shy-guy-and-chain-chomp.glb
  method: kicad
  source_file: Shy Guy/Shy Guy PCB 3.kicad_pcb
  generated: '2026-09-07'
  bytes: 140068
---

Shy Guy and Chain Chomp are a pair of small, passive PCB "art" SAOs (Shitty Add-Ons) designed by Seamus de Cleir, who goes by PotatoNightmare, in the lead-up to DEF CON 26 in 2018. Both are simple LED boards with no microcontroller: Chain Chomp lights five 1206 LEDs and Shy Guy lights two, each board wired through a single 2512 51-ohm resistor so it draws power straight from a host badge's SAO header.

De Cleir published the full design under the MIT license on GitHub as SAO-PCB-Art, including the SVG artwork, KiCad schematic and PCB files, and gerbers, along with a short bill of materials for anyone who wants to fabricate and hand-solder their own copies. The only condition asked in return is that a maker leave the original Twitter handle (@PotatoNightmare) on the back of the board. The README credits a tutorial by @MrTwinkleTwink on turning SVG artwork into KiCad SAO boards as the starting point for the project.

No evidence was found that these were sold, given away at a specific quantity, or listed on a storefront -- the repository reads as an open release of the design files rather than a commercial product, so pricing, quantity, and distribution are left blank pending better sources.
