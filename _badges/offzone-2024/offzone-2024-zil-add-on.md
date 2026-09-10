---
title: OFFZONE 2024 ZIL add-on
id: offzone-2024-offzone-2024-zil-add-on
layout: badge
parent: OFFZONE 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2024
year: 2024
makers:
- name: BI.ZONE / Craft.Zone
  url: https://github.com/bi-zone/offzone-hw
summary: A small ZIL-truck-shaped (Soviet automaker) LED add-on board for the OFFZONE 2024 badge, part of a set of collectible add-ons released for the conference.
functions: 'Passive LED indicator board: four LEDs (two white, two orange) light up when the add-on is plugged into power via its connector; no logic or MCU.'
look:
  colors:
  - green
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: 2x white 1206 LEDs and 2x orange 0805 LEDs, each with a 220 ohm 1206 series resistor.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2024/zil_addon
  firmware_url: null
  eda_tool: KiCad
  gerbers_url: https://github.com/bi-zone/offzone-hw/tree/master/2024/zil_addon/zil_addon_gbr
  bom_url: https://github.com/bi-zone/offzone-hw/blob/master/2024/zil_addon/zil_addon_BOM.html
  notes: Two-layer FR4 PCB, 1.5mm thick, immersion silver finish, green solder mask, black silkscreen. Connects via a PLD-4 connector (a 4-pin header, matching the other 2024 OFFZONE add-ons).
links:
- label: github.com/bi-zone/offzone-hw/tree/master/2024/zil_addon
  url: https://github.com/bi-zone/offzone-hw/tree/master/2024/zil_addon
  kind: repo
images:
- file: assets/images/badges/offzone-2024/offzone-2024-zil-add-on/a01b2587dc.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2024/zil_addon
  credit: BI.ZONE / Craft.Zone
  caption: ZIL add-on, front view
- file: assets/images/badges/offzone-2024/offzone-2024-zil-add-on/b09618911c.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2024/zil_addon
  credit: BI.ZONE / Craft.Zone
  caption: ZIL add-on, back view
contact: {}
notes:
- ZIL-themed (Soviet truck brand) add-on board for the OFFZONE 2024 badge. Found by the event-year sweep, task con-phdays.
- The sweep's link used the branch name 'main', which 404s; the repo's actual default branch is 'master'. Corrected link kept below.
status: released
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2024/zil_addon
  title: OFFZONE 2024 ZIL add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2024''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/master/2024/zil_addon
  title: bi-zone/offzone-hw - 2024/zil_addon
  accessed: '2026-09-08'
  note: Corrected repo path (master branch); directory listing, README.md and BOM confirm construction, connector, and design files.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed via BI.ZONE's own GitHub repo (design files, README, BOM). No storefront, price, quantity, or distribution details found anywhere; this appears to be a design/build repo rather than a sales listing, so it was likely given out at the conference rather than sold. SAO connector type is a PLD-4 header, which could not be confidently mapped to the standard sao_version vocabulary (v1/v1.69bis), so left null. No maker photo of it worn on a badge was found, only the isolated board photos in the repo.
last_modified_date: '2026-09-10'
model:
  file: assets/models/offzone-2024/offzone-2024-zil-add-on.glb
  method: kicad
  source_file: 2024/zil_addon/zil_addon.kicad_pcb
  generated: '2026-09-10'
  bytes: 52724
---

The ZIL add-on is one of a set of small LED add-on boards BI.ZONE and Craft.Zone released alongside the main OFFZONE 2024 badge, named for ZIL, the Soviet-era Moscow truck and limousine manufacturer. It is a simple, MCU-free board: four surface-mount LEDs (two white 1206s, two orange 0805s), each behind its own 220 ohm current-limiting resistor, wired to light up when the add-on is powered through its PLD-4 connector.

The board is a two-layer FR4 PCB, 1.5mm thick, with immersion silver-finished pads, a green solder mask, and black silkscreen markings. BI.ZONE published the full KiCad source (schematic, PCB, and project files), Gerbers, and an HTML bill of materials in their `offzone-hw` GitHub repository, along with build instructions and photos of the front and back of the assembled board. No pricing, production quantity, or separate distribution details were published; it reads as a giveaway/collectible add-on for OFFZONE 2024 attendees rather than an item that was sold.

## Make your own

BI.ZONE's repo has everything needed to build one: the KiCad schematic/PCB/project files, Gerber files ready to send to a fab, and an HTML BOM. Per their README, the resistors go on first (non-polarized), then the LEDs lens-side down with the two larger (white) LEDs oriented one way and the two smaller (orange) LEDs the opposite way per the polarity marks, and finally the PLD-4 connector.
