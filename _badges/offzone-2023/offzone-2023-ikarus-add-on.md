---
title: OFFZONE 2023 Ikarus add-on
id: offzone-2023-offzone-2023-ikarus-add-on
layout: badge
parent: OFFZONE 2023
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2023
year: 2023
makers:
- name: BI.ZONE / Craft.Zone
summary: A small DIY LED add-on board shaped after the Ikarus theme, published as an open-hardware build for the OFFZONE 2023 conference badge.
functions: Lights two white and two orange LEDs; no other electronics or logic.
look:
  colors:
  - red
  shape: null
  themes:
  - security
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: 2x white 1206 LEDs and 2x orange 0805 LEDs, each behind a 220 ohm 1206 resistor.
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
  where: 'Not sold as a finished item: published as a DIY build (order the PCB yourself, solder the BOM).'
make_your_own:
  open_source: true
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2023/ikarus_addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bi-zone/offzone-hw/tree/master/2023/ikarus_addon
  url: https://github.com/bi-zone/offzone-hw/tree/master/2023/ikarus_addon
  kind: repo
images:
- file: assets/images/badges/offzone-2023/offzone-2023-ikarus-add-on/1f5a9f7d61.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2023/ikarus_addon
  credit: BI.ZONE / Craft.Zone
  caption: Ikarus add-on PCB, front side
- file: assets/images/badges/offzone-2023/offzone-2023-ikarus-add-on/2137fc16a1.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2023/ikarus_addon
  credit: BI.ZONE / Craft.Zone
  caption: Ikarus add-on PCB, back side with LEDs
- file: assets/images/badges/offzone-2023/offzone-2023-ikarus-add-on/1f5a9f7d61.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2023/ikarus_addon
  credit: BI.ZONE / Craft.Zone
  caption: Front of the ikarus_addon board with LEDs and PLD-4 connector
- file: assets/images/badges/offzone-2023/offzone-2023-ikarus-add-on/2137fc16a1.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2023/ikarus_addon
  credit: BI.ZONE / Craft.Zone
  caption: Back of the ikarus_addon board
contact: {}
notes:
- Ikarus-themed add-on board for the OFFZONE 2023 badge. Found by the event-year sweep, task con-phdays.
- The sweep's source link used branch 'main'; the repo's actual default branch is 'master' (corrected in links/sources above).
- Sweep-era title kept as "ikarus_addon" (the repo folder/README name); the community sheet elsewhere lists the same item as "OFFZONE 2023 Ikarus add-on".
status: released
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2023/ikarus_addon
  title: OFFZONE 2023 Ikarus add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2023''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/master/2023/ikarus_addon
  title: ikarus_addon README, BI.ZONE offzone-hw repo
  accessed: '2026-09-08'
  note: Confirmed the item exists, its BOM (LEDs, resistors, PLD-4 connector), red solder mask, KiCad source files and gerbers, and pulled front/back photos.
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/README.md
  title: offzone-hw repo README
  accessed: '2026-09-08'
  note: Confirms these add-ons are published as self-build projects (order your own PCB, buy your own BOM) rather than distributed as finished items at the con.
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/2023/ikarus_addon/README.md
  title: ikarus_addon README (Russian assembly instructions)
  accessed: '2026-09-10'
  note: Source for BOM, LED counts/colors, PCB spec (2-layer FR4, red mask, PLD-4 connector), and front/back photo URLs.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed on the maker's own GitHub repo (BI.ZONE org). The repo README frames all these add-ons as DIY builds for people to fabricate and solder themselves, so price/quantity/availability as a finished product are genuinely unknown and left blank. No firmware exists since the board is a passive LED add-on (no MCU). Could not determine the exact color/theme rendering of "Ikarus" beyond the red PCB and LED placement shown in the photos; no separate coverage of the add-on set was found beyond the repo itself. Merged with duplicate entry 'ikarus_addon' (offzone-2023-ikarus-addon).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/offzone-2023/ikarus-addon/
model:
  file: assets/models/offzone-2023/offzone-2023-ikarus-add-on.glb
  method: kicad
  source_file: 2023/ikarus_addon/ikarus_addon.kicad_pcb
  generated: '2026-09-10'
  bytes: 50204
---

The Ikarus add-on is one of four small companion boards BI.ZONE and Craft.Zone published for the OFFZONE 2023 conference badge (alongside cat, iron, and lighthouse add-ons from the same year). It is a simple, unpowered PCB: two white 1206 LEDs and two orange 0805 LEDs, each fed through its own 220 ohm resistor, wired through a PLD-4 connector so it draws power from the host badge rather than carrying its own microcontroller or battery.

Rather than selling a finished, assembled unit, BI.ZONE published the add-on as an open-hardware DIY project: KiCad schematic and PCB source files, ready-to-send gerbers, and a BOM/README walking a builder through ordering the two-layer, red-solder-mask board and hand-soldering the four LEDs and four resistors. This matches how the rest of the `offzone-hw` repository is organized — one folder per year, each with build instructions aimed at letting even a soldering novice reproduce the add-on themselves.

Because it was released as source files rather than a finished product, there is no listed price, production quantity, or storefront to check for availability — those fields are left blank rather than guessed.

## Notes merged from the duplicate entry "ikarus_addon"

The ikarus_addon is a small plug-in LED accessory that BI.ZONE and Craft.Zone produced for OFFZONE 2023, part of a family of similarly-built add-ons released that year (alongside cat_addon, iron_addon, and lighthouse_addon). It is a simple, MCU-less 2-layer PCB finished in red solder mask with black silkscreen, carrying two white 1206 LEDs and two orange 0805 LEDs, each fed through its own 220-ohm current-limiting resistor, and a PLD-4 connector for attaching to a host badge.

BI.ZONE published the full hardware design for the addon on their `offzone-hw` GitHub repository, including KiCad schematic and PCB files, a BOM, and Russian-language assembly instructions with front and back photos. The instructions call for soldering the resistors first, then the LEDs lens-down (observing polarity, small 0805 parts on the front and larger 1206 parts on the back), and finally the connector.

No pricing, quantity, or distribution details were found; the GitHub repository is a hardware-design archive rather than a storefront, so how the addon was distributed at the event (e.g. free giveaway, badge add-on kit, contest prize) is unconfirmed.
