---
title: space_shuttle_SAO
id: dc31-space-shuttle-sao
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: Aerospace Village
  url: https://github.com/AerospaceVillage
summary: A Space Shuttle-shaped SAO from the Aerospace Village, with a single LED lit by its own coin cell so it glows independently of the host badge.
functions: Lights a single LED, switched on and off with an onboard slide switch; not powered from the badge SAO header.
look:
  colors: []
  shape: spaceship
  themes:
  - space
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single through-hole LED (SunLED XZMYK45WT-9), driven off the onboard coin cell through a 330-ohm resistor, not the SAO header.
  display: none
  connectivity: []
  battery: CR-type coin cell (Keystone 3034 holder)
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed by the Aerospace Village at DEF CON 31 (2023); exact distribution method not stated in the repo.
make_your_own:
  open_source: true
  hardware_url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/space_shuttle_SAO
  firmware_url: null
  eda_tool: KiCad
  gerbers_url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/space_shuttle_SAO/gerbers
  notes: No firmware — the SAO is a simple discrete-component circuit (battery, resistor, LED, switch), so there is nothing to program.
links:
- label: github.com/AerospaceVillage/avBadge_2023/tree/main/space_shuttle_SAO
  url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/space_shuttle_SAO
  kind: repo
- label: AerospaceVillage/avBadge_2023 (repo root)
  url: https://github.com/AerospaceVillage/avBadge_2023
  kind: repo
  note: 'Repo README: "Aerospace Village Badge(s) for Def Con 2023" — parent repo covering the Wright Flyer badge, the Wright Stuff badge, and several SAOs including this one.'
images:
- file: assets/images/badges/dc31/space-shuttle-sao/9e6b593173.jpg
  source: https://github.com/AerospaceVillage/avBadge_2023/tree/main/space_shuttle_SAO
  credit: Aerospace Village
  caption: KiCad PCB render of the Space Shuttle SAO
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 4).
- Sheet/sweep used the raw filename "space_shuttle_SAO" as the title; kept as-is since no other name appears in the repo.
status: released
sources:
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/space_shuttle_SAO
  title: space_shuttle_SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run4-spotted); event read as ''dc31''.'
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2023/blob/main/space_shuttle_SAO/space_shuttle_SAO.csv
  title: space_shuttle_SAO.csv (bill of materials)
  accessed: '2026-09-08'
  note: 'BOM confirms parts: coin-cell holder (BT1), one SunLED XZMYK45WT-9 LED (D1), SAO_1.69 connector (J1), 330 ohm resistor (R1), SPDT slide switch (SW1). No MCU present.'
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2023
  title: AerospaceVillage/avBadge_2023
  accessed: '2026-09-08'
  note: Repo root README confirms this is one of several Aerospace Village badges/SAOs made for DEF CON 2023 (DC31).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed via the maker's own GitHub repo and its bill-of-materials/KiCad files, so the hardware details are solid, but no press coverage, storefront, or distribution details (price, quantity, how it was handed out) were found, hence medium rather than high confidence. No separate README or write-up exists for this specific SAO beyond the CAD files.
last_modified_date: '2026-09-10'
model:
  file: assets/models/dc31/space-shuttle-sao.glb
  method: kicad
  source_file: space_shuttle_SAO/space_shuttle_SAO.kicad_pcb
  generated: '2026-09-10'
  bytes: 89708
---

The Space Shuttle SAO is one of several add-on boards the Aerospace Village produced for DEF CON 31 (2023), alongside its main Wright Flyer and Wright Stuff badges. It is a simple, self-contained board shaped like the shuttle orbiter: a coin-cell battery, a current-limiting resistor, a slide switch, and a single LED, wired so the LED lights from the onboard battery rather than from the host badge's SAO power pins. Flipping the switch turns the light on or off independently of whatever badge it is plugged into.

The board uses a 1.69bis (6-pin) SAO connector for mechanical attachment even though it does not draw power over it, and was designed in KiCad with full schematic, PCB, and Gerber files published in the Aerospace Village's `avBadge_2023` GitHub repository. No microcontroller or firmware is involved — it's a purely discrete-component circuit — so anyone with the repo's Gerbers could have it fabricated as-is.

No independent write-up, storefront listing, or press coverage of this specific SAO turned up in research; everything here comes from the maker's own repository and its bill of materials.

## Make your own

The full design is open in the linked repository: KiCad schematic (`space_shuttle_SAO.kicad_sch`) and PCB (`space_shuttle_SAO.kicad_pcb`) files, ready-to-order Gerbers under `gerbers/` and `gerber_zips/`, a pick-and-place position file, and a bill of materials (`space_shuttle_SAO.csv`) listing the coin-cell holder, LED, resistor, switch, and SAO connector. There is no firmware step — assembling the four passive/active parts per the BOM is all that's required.
