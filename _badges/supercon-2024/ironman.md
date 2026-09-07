---
title: IronMan
id: supercon-2024-ironman
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: 'A small red SAOAO (SAO for an SAO) shaped like Iron Man''s helmet, with two LEDs lighting up the eyes and faceplate through a laser-cut acrylic-style silkscreen mask.'
functions: 'Passive light-up board: two SMD LEDs backlight cutouts in the Iron Man mask graphic. No microcontroller, no interactivity beyond the LEDs being powered.'
look:
  colors:
  - red
  - gold
  shape: null
  themes:
  - pop culture
  - movie
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: '1206 SMD LEDs (through-hole handsolder footprint), not addressable'
  display: none
  connectivity: []
  battery: powered by host board
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: '100'
  availability: free
  distribution:
  - free_drop
  - contest
  where: 'Handed out at Hackaday Supercon 8 (2024) as one of davedarko''s "SAOAO" add-on boards; not sold.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/IronMan
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/YoDawgSAO/tree/master/badges/IronMan
  url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/IronMan
  kind: repo
- label: 'Yo Dawg SAO - introducing SAOAO (Hackaday.io project)'
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  kind: hackaday
- label: 'Project log: Panels (JLCPCB order of 100 Iron Man boards)'
  url: https://hackaday.io/project/198060/log/233016-panels
  kind: doc
images:
  - file: assets/images/badges/supercon-2024/ironman/81423ef002.jpg
    source: "https://hackaday.io/project/198060/log/233016-panels"
    credit: "davedarko"
    caption: "JLCPCB panel photo showing a lit Iron Man SAOAO board (red, top right) alongside davedarko's other SAOAO designs"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/IronMan
  title: IronMan
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''supercon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/davedarko/YoDawgSAO/main/README.md
  title: 'YoDawgSAO README'
  accessed: '2026-09-07'
  note: 'Confirms the SAOAO concept was made for the Hackaday Supercon add-on contest in 2024; 19x19mm size, 1.27mm 3-pin GND-VCC-GND header.'
- kind: url
  url: https://raw.githubusercontent.com/davedarko/YoDawgSAO/main/badges/IronMan/IronMan.kicad_sch
  title: 'IronMan.kicad_sch'
  accessed: '2026-09-07'
  note: 'Schematic shows 2 LEDs (D1, D2), 2 resistors, and a single 3-pin connector; no microcontroller.'
- kind: url
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  title: 'Yo Dawg SAO - introducing SAOAO'
  accessed: '2026-09-07'
  note: 'Project page for the SAOAO line; confirms 100 red Iron Man boards were ordered with ENIG finish, plus quantities and Supercon 2024 distribution context.'
- kind: url
  url: https://hackaday.io/project/198060/log/233016-panels
  title: 'Project log: Panels'
  accessed: '2026-09-07'
  note: 'Log entry stating "100 SAO PCBs, 100 red Iron Man boards with ENIG and 100 hackaday logo boards" were ordered from JLCPCB; source of the saved panel photo.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'The GitHub repo folder itself carries no README or images for this specific board; quantity, distribution, and fabrication details came from davedarko''s Hackaday.io project page and log for the SAOAO line as a whole (the IronMan board is one of several SAOAO designs, alongside a Hackaday-logo board and a "Super Cluster" board). Price/price_usd left empty since it was a free giveaway, not sold. No firmware exists since the board has no MCU. sao_version left null: the connector is a nonstandard 3-pin (GND-VCC-GND) 1.27mm header specific to the SAOAO sub-standard, not a v1 or v1.69bis/v2 SAO header.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/ironman/
---

The Iron Man board is one of davedarko's "SAOAO" designs — a Simple Add-on Add-on, meaning a tiny badge-for-your-badge that plugs into his larger Yo Dawg SAO baseplate, which in turn plugs into a normal SAO header. Made for the Hackaday Supercon 8 (2024) add-on contest, each SAOAO is capped at 19mm x 19mm with a nonstandard 1.27mm 3-pin header (ground-power-ground, with the pins arranged so the board can't be plugged in backwards). The Iron Man version is a red PCB with a cutout silkscreen of Iron Man's helmet, backlit by two SMD LEDs so the eyes and faceplate glow. It carries no microcontroller or firmware; it is purely a lit-up graphic.

davedarko had 100 of these Iron Man boards fabricated in red with ENIG finish through JLCPCB, alongside 100 plain SAO baseplates and 100 Hackaday-logo SAOAO boards, and brought roughly 200 SAOAO boards total to Supercon 2024 to hand out as free add-ons alongside the contest badges. The hardware (KiCad schematic, PCB, and fabrication files) is published in the open-source YoDawgSAO GitHub repository.
