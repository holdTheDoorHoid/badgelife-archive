---
title: DC404 Training Badge
id: dc30-dc404-training-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: Enterprise Badge
summary: A learn-to-solder practice board for DC404's DEF CON badge-making workshop, teaching through-hole and SMD soldering with a working LED chaser circuit as the payoff.
functions: Practice board for soldering resistors, diodes and an LED chase; once built correctly, a 555 timer clocks a 4520 binary counter to light 8 LEDs in a running/chase pattern.
look:
  colors:
  - green
  shape: rectangle
  themes:
  - learn to solder
  - kit
tech:
  mcu: none (555 timer + CD4520 binary counter, no microcontroller)
  leds:
    count: 8
    type: SMD
    note: 1206 SMD LEDs (D1-D8), driven in sequence by the counter circuit; board also has a separate practice area with extra through-hole solder points not wired to LEDs
  display: none
  connectivity: []
  battery: 2x 3V coin cell (nominal 1000mAh cells, e.g. CR2477-class), footprint marked "3039"
  sao_version: none
get_one:
  price: $25
  price_usd: 25.0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: sold via drops at the con; given away free while supplies lasted at the Hardware Hacking Village (HHV)
make_your_own:
  open_source: true
  hardware_url: https://github.com/seeigecannon/DC404TrainingBadge
  firmware_url: null
  eda_tool: KiCad
notes:
- They are being sold via drops at the con. If you are quick, there will be some for free at the HHV
- GitHub repo README calls it the "DC404 Learn to Solder Badge"; the community sheet listed it as "DC404 Training Badge". Repo history goes back to 2020 (Rev A) with a Rev B update in 2021, so this design predates and was reused for DC30 (2022) rather than being drawn fresh that year.
status: released
sources:
- kind: sheet
  event: dc30
  row: 37
  updated: '2022-07-19'
- kind: url
  url: https://github.com/seeigecannon/DC404TrainingBadge
  title: seeigecannon/DC404TrainingBadge
  accessed: '2026-09-06'
  note: Repo README, file listing, KiCad schematic/XML netlist and PCB renders; confirms it is a learn-to-solder practice board, not a badge with an MCU, and gives the LED/component details and Unlicense license.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Could not confirm exact quantity made/distributed, exact coin-cell part number beyond the "3V 1000mAh" schematic label, or find independent (non-repo) coverage of the DC30 distribution. GitHub repo's own commit history (2020-2021) predates the DC30 (2022) sheet listing, suggesting this training board design was reused across multiple DEF CON years rather than made new for DC30; left event as dc30 per the sheet since that is the year it was reported distributed.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc30/dc404-training-badge.glb
  method: kicad
  source_file: Learn404.kicad_pcb
  generated: '2026-09-07'
  bytes: 361492
---

The DC404 Training Badge is a learn-to-solder practice board made by Enterprise Badge (the crew behind the DC404 community's badge projects) and handed out at DEF CON, including free drops at the Hardware Hacking Village. Unlike most badges in this archive it carries no microcontroller: the circuit is built from a 555 timer driving a CD4520 dual binary up-counter, which steps through eight 1206 SMD LEDs (D1-D8) in a chase/running-light pattern once assembled correctly. A silkscreen "PRACTICE AREA" with extra unconnected through-hole and SMD footprints gives beginners somewhere to try their first joints before soldering the parts that actually matter, and clear polarity markings guide first-time solderers through orienting the LEDs and ICs. Power comes from two coin cells in large through-hole holders.

The hardware is fully open source under the Unlicense and published on GitHub as KiCad schematic, PCB and Gerber files, along with printable schematics and an assembly instructions document. The repository's commit history shows an initial 2020 upload followed by a "Rev B" update in 2021, both predating the DC30 (2022) community sheet listing used for this entry — indicating the board is a recurring teaching tool reused across multiple DEF CON years rather than a one-off design for DC30 specifically.

## Make your own

The GitHub repo (https://github.com/seeigecannon/DC404TrainingBadge) includes the KiCad project (`Learn404.sch`, `Learn404.kicad_pcb`), a `GERBERs` folder ready to send to a fab, a printable reference schematic, and an `Instructions.odt` assembly guide. Bill of materials, per the schematic: one LM555 timer, one CD74HCT4520 dual binary counter, eight 1206 SMD LEDs, associated 1206 resistors, and two coin cells in "3039"-footprint holders.
