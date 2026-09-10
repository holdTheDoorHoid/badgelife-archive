---
title: OFFZONE 2024 Seal add-on
id: offzone-2024-offzone-2024-seal-add-on
layout: badge
parent: OFFZONE 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2024
year: 2024
makers:
- name: BI.ZONE / Craft.Zone
summary: A seal-shaped SAO add-on from Craft.Zone's DIY series for OFFZONE 2024, built around a two-transistor blinking circuit with a green and a yellow LED.
functions: Blinks its green and yellow LEDs via a discrete two-transistor astable circuit; no MCU or programmable logic.
look:
  colors:
  - white
  shape: null
  themes:
  - animal
  - learn to solder
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: One 1206 green LED and one 0805 yellow LED, driven by a two-transistor (BC807-25) astable multivibrator, not a microcontroller.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed as a DIY kit at Craft.Zone, the hardware village/workshop at OFFZONE 2024, for attendees to solder themselves; no separate storefront found.
make_your_own:
  open_source: true
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2024/seal_addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bi-zone/offzone-hw/tree/main/2024/seal_addon
  url: https://github.com/bi-zone/offzone-hw/tree/main/2024/seal_addon
  kind: repo
- label: github.com/bi-zone/offzone-hw/tree/master/2024/seal_addon
  url: https://github.com/bi-zone/offzone-hw/tree/master/2024/seal_addon
  kind: repo
images:
- file: assets/images/badges/offzone-2024/offzone-2024-seal-add-on/8716c823de.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2024/seal_addon
  credit: BI.ZONE / Craft.Zone
  caption: Assembled seal-shaped add-on, front, with green and yellow LEDs
- file: assets/images/badges/offzone-2024/offzone-2024-seal-add-on/13d1f9f416.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2024/seal_addon
  credit: BI.ZONE / Craft.Zone
  caption: Seal add-on, back of PCB showing component placement
contact: {}
notes:
- Seal-themed add-on board for the OFFZONE 2024 badge. Found by the event-year sweep, task con-phdays.
- The sweep's source link used branch 'main'; the repo's actual default branch is 'master' (same path otherwise). Both links are kept above.
status: listed
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2024/seal_addon
  title: OFFZONE 2024 Seal add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2024''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/master/2024/seal_addon
  title: seal_addon (2024/seal_addon README, KiCad files, gerbers, BOM)
  accessed: '2026-09-08'
  note: Confirmed the repo path (default branch is master, not main), read the assembly README and BOM for LED/transistor/connector details, and found the front/back product photos.
- kind: url
  url: https://github.com/bi-zone/offzone-hw
  title: offzone-hw (top-level README)
  accessed: '2026-09-08'
  note: Confirms the repo collects Craft.Zone add-ons for OFFZONE by year, published as DIY solder-it-yourself kits with gerbers and BOM, ordered from Russian or Chinese PCB fabs and populated by the attendee.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed via the maker's own repo (README, BOM, KiCad source, gerbers, and front/back photos). No maker statement found on price, quantity made, or whether it was free vs. sold at Craft.Zone; get_one fields left unknown. No separate storefront, Hackaday post, or press coverage located in a short search. The connector is a PLD-4 (4-pin) header per the BOM, but the entry's tech.sao_version field is left null since the maker does not call it a "SAO" by name or state pin compatibility with the SAO standard versions.
last_modified_date: '2026-09-10'
model:
  file: assets/models/offzone-2024/offzone-2024-seal-add-on.glb
  method: kicad
  source_file: 2024/seal_addon/seal_addon.kicad_pcb
  generated: '2026-09-10'
  bytes: 75136
---

The Seal add-on is one of six 2024 add-on boards Craft.Zone — the hardware workshop track at BI.ZONE's OFFZONE conference — published for attendees to build themselves. Rather than a pre-assembled giveaway, it ships as open KiCad design files, gerbers, and a bill of materials: a small two-layer PCB in the shape of a seal, populated with a green 1206 LED, a yellow 0805 LED, two BC807-25 transistors, resistors, and two electrolytic capacitors wired as a simple discrete astable (free-running) blinker circuit — no microcontroller involved. It connects to a host badge through a 4-pin PLD-4 header.

The top-level `offzone-hw` repository frames the whole 2024/2025 add-on lineup as a teaching kit: order the gerbers from a Russian fab (Rezonit) or a Chinese one (JLCPCB/PCBWay), source the BOM parts locally or via AliExpress, and solder it at the con following the README's step-by-step instructions (resistors first, then LEDs observing polarity, then transistors and capacitors, then the connector). No pricing, production quantity, or distribution mechanism (free vs. paid, con badge vs. village extra) is stated in the source material found, so those fields are left blank rather than guessed.
