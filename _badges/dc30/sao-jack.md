---
title: Jack SAO
id: dc30-sao-jack
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: hamster
  url: https://twitter.com/hamster
summary: A simple learn-to-solder SAO shaped like a smiley skull and crossbones, with four through-hole LEDs and two resistors.
functions: 'No electronics beyond the LEDs themselves: once assembled, the two white/yellow LEDs at the "eyes" of the crossbones and two red LEDs lower on the board light up whenever the SAO is plugged into a powered badge header. There is no microcontroller or animation logic.'
look:
  colors:
  - black
  - white
  shape: skull
  themes:
  - skull
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: Two white/yellow-green LEDs and two red LEDs, through-hole, wired directly to the SAO power pins (no driver or MCU).
  display: none
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
  hardware_url: https://github.com/hamster/defcon30/tree/main/jack
  firmware_url: null
  eda_tool: KiCad
  notes: Repo includes KiCad schematic/PCB/project files and a BOM spreadsheet (jack-BOM.xlsx); no firmware since the board has no MCU.
links:
- label: github.com/hamster/defcon30/tree/main/jack
  url: https://github.com/hamster/defcon30/tree/main/jack
  kind: repo
images:
- file: assets/images/badges/dc30/sao-jack/b91b96a1df.jpg
  source: https://github.com/hamster/defcon30/tree/main/jack
  credit: hamster
  caption: Assembled Jack SAO, LEDs lit
- file: assets/images/badges/dc30/sao-jack/c196110585.jpg
  source: https://github.com/hamster/defcon30/tree/main/jack
  credit: hamster
  caption: Jack SAO kit parts before assembly
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://github.com/hamster/defcon30/tree/main/jack
  title: SAO Jack
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc30''.'
- kind: url
  url: https://raw.githubusercontent.com/hamster/defcon30/main/jack/README.md
  title: 'hamster/defcon30: jack/README.md'
  accessed: '2026-09-07'
  note: Maker's own step-by-step README confirming it is a learn-to-solder SAO kit (4 LEDs in two colors, 2 resistors, SAO connector), made for DEF CON 30, with build photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Repo README (the maker''s own page) confirms what the kit is, its parts, and that it was made for DEF CON 30 (repo description: "defcon 30 SAOs"). No storefront, price, or quantity information was found anywhere; a web search for the item by name and maker turned up nothing beyond the repo itself, so get_one fields are left empty. Shape/colors were read directly off the maker''s own build photos in the repo.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc30/sao-jack.glb
  method: kicad
  source_file: jack/jack.kicad_pcb
  generated: '2026-09-07'
  bytes: 110300
---

Jack is a beginner-friendly SAO kit made by hamster for DEF CON 30 (2022), designed purely to teach soldering rather than to show off complex electronics. The board is a black PCB silkscreened in white as a smiley-face skull and crossbones with "D3F C0N" lettering, and the whole build is four through-hole LEDs (two white/yellow-green at the "eyes," two red lower on the crossbones) plus two resistors and a SAO connector — no microcontroller, so once soldered the LEDs simply light whenever the badge supplies power through the header.

The maker's GitHub repository walks through the entire assembly in photos, calling out easy soldering pitfalls (the small LEDs have their cathode on the *shorter* leg rather than the usual flat-spot marking) step by step, and includes the full KiCad source, PCB Gerbers-ready project files, and a bill-of-materials spreadsheet for anyone who wants to reproduce it. No price, production quantity, or distribution channel is documented anywhere the archive could find, so those fields are left blank; it is presumed to have been a DEF CON 30 giveaway or soldering-village kit rather than a storefront item, but that is not confirmed by any source.
