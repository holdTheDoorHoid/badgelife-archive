---
title: crew SAO
id: dc31-crew-sao
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: Aerospace Village
summary: A simple, independently-powered SAO from the DEF CON 31 Aerospace Village badge set, with a single LED, a switch, and its own coin-cell battery rather than drawing power from the host badge.
functions: Toggles a single LED on and off via an on-board switch; runway-marking artwork on the silkscreen.
look:
  colors: []
  shape: null
  themes:
  - security
  - village badge
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single through-hole/generic LED, not addressable.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed at the Aerospace Village at DEF CON 31 (2023); exact method (free drop vs. build-your-own) not stated in the source repo.
make_your_own:
  open_source: true
  hardware_url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/crew%20SAO
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/AerospaceVillage/avBadge_2023/tree/main/crew%20SAO
  url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/crew%20SAO
  kind: repo
- label: Aerospace Village Badge(s) for DEF CON 2023 (repo README)
  url: https://github.com/AerospaceVillage/avBadge_2023
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 4).
- Repo folder and README title case it "crew SAO"; kept as-is.
status: listed
sources:
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/crew%20SAO
  title: crew SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run4-spotted); event read as ''dc31''.'
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2023
  title: Aerospace Village Badge(s) for Def Con 2023 (README)
  accessed: '2026-09-08'
  note: Confirms event (DEF CON 31 / 2023) and that this SAO is one of several the Village made that year.
- kind: url
  url: https://raw.githubusercontent.com/AerospaceVillage/avBadge_2023/main/crew%20SAO/crew-SAO.kicad_sch
  title: crew-SAO.kicad_sch (KiCad schematic, raw)
  accessed: '2026-09-08'
  note: Read the schematic's part library IDs to confirm a 6-pin SAO connector, one LED, one SPDT switch, one resistor, and a coin-cell battery holder (no MCU).
- kind: url
  url: https://raw.githubusercontent.com/AerospaceVillage/avBadge_2023/main/crew%20SAO/crew-SAO.kicad_pcb
  title: crew-SAO.kicad_pcb (KiCad PCB, raw)
  accessed: '2026-09-08'
  note: Battery footprint is a Keystone 3034 (20mm coin-cell holder), confirming CR2032.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed via the maker's own repo (schematic + PCB + gerbers), so this is a real, built item, not just a sheet entry. No press coverage, storefront listing, or photo of the assembled board was found, so price, quantity, exact distribution method, and colors/shape are unknown. The KiCad board outline SVG in the repo is a trace render, not a photograph, so no image was saved. PCB silkscreen art (a runway-markings graphic referencing "31") supports the DC31/2023 identification.
last_modified_date: '2026-09-10'
model:
  file: assets/models/dc31/crew-sao.glb
  method: kicad
  source_file: crew SAO/crew-SAO.kicad_pcb
  generated: '2026-09-10'
  bytes: 44080
---

The crew SAO is one of several add-on badges the Aerospace Village produced for DEF CON 31 (2023), alongside its main "Wright Flyer" and "Wright Stuff" badges. Unlike most SAOs, it does not draw power from a host badge: its schematic shows a CR2032 coin-cell holder on board, along with a single LED, a resistor, and an SPDT switch to turn the LED on and off. It connects through a standard 6-pin SAO header. The board's silkscreen carries a runway-markings graphic referencing "31" (DEF CON 31).

No microcontroller is present — this is a simple passive/discrete-component add-on rather than a programmable one. The Village published the full KiCad source (schematic, PCB layout, and gerbers) in their `avBadge_2023` GitHub repository, so the hardware is fully open, though no firmware applies since there is no MCU to program.

No press coverage, storefront listing, or photo of an assembled unit turned up in this pass, so pricing, quantity made, and the precise distribution method (e.g., handed out at the village desk vs. a solder-your-own kit) remain unconfirmed.
