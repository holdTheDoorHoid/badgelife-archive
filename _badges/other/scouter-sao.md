---
title: Scouter-SAO
id: other-scouter-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2021
makers:
- name: syn-ack-zack
  url: https://github.com/syn-ack-zack
- name: mcm3nac3
  url: https://github.com/mcm3nac3
summary: A simple passive shitty-add-on (SAO) with four LEDs, designed to plug into the 2021 Hackers Teaching Hackers "ScryptKeeper" conference badge.
functions: 'Lights four LEDs, powered from the host badge''s SAO header; no onboard microcontroller or independent logic.'
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: Four generic LEDs (D1-D4) sharing a single current-limiting resistor (R1), driven directly from the SAO header rather than an onboard MCU.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/HTHackers/ScryptKeeper/tree/main/Scouter-SAO
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/HTHackers/ScryptKeeper/tree/main/Scouter-SAO
  url: https://github.com/HTHackers/ScryptKeeper/tree/main/Scouter-SAO
  kind: repo
- label: github.com/HTHackers/ScryptKeeper
  url: https://github.com/HTHackers/ScryptKeeper
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
- 'Made for Hackers Teaching Hackers (HTH), an annual InfoSec conference in Columbus, Ohio; no matching event id exists in _data/events.yml, so event is left as "other". HTH 2021 was the "ScryptKeeper" badge year, which is where the Scouter-SAO folder lives in the HTHackers/ScryptKeeper repo.'
status: listed
sources:
- kind: url
  url: https://github.com/HTHackers/ScryptKeeper/tree/main/Scouter-SAO
  title: Scouter-SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''other''.'
- kind: url
  url: https://github.com/HTHackers/ScryptKeeper
  title: 'HTHackers/ScryptKeeper: The ScryptKeeper - 2021 Hackers Teaching Hackers Badge'
  accessed: '2026-09-07'
  note: Repo README identifies the parent badge as the 2021 Hackers Teaching Hackers (HTH) conference badge, CircuitPython-based.
- kind: url
  url: https://raw.githubusercontent.com/HTHackers/ScryptKeeper/main/Scouter-SAO/ScryptKeeper-Scouter.zip
  title: ScryptKeeper-Scouter.zip (KiCad project archive)
  accessed: '2026-09-07'
  note: 'KiCad schematic/PCB (TFTS-HTH-SAO-Scout-IS) shows a v1.69bis 6-pin SAO connector (X1), one resistor (R1), and four LEDs (D1-D4); board silkscreen reads "HACKERS TEACHING HACKERS" and credits "@syn-ack-zack" and "@mcm3nac3".'
- kind: url
  url: https://github.com/syn-ack-zack
  title: syn-ack-zack (Zack Nagaich) - GitHub
  accessed: '2026-09-07'
  note: Profile lists ScryptKeeper as the "2021 Hackers Teaching Hackers Badge," confirming the maker and year.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    No dedicated README, storefront, or announcement post exists for the Scouter-SAO
    itself; everything here comes from reading the KiCad source files (schematic,
    netlist, PCB silkscreen text) in the repo. Could not confirm price, quantity made,
    availability, distribution method, or the board's shape/colors/artwork theme (no
    photo or rendered board image was found anywhere online). The "Scouter" name
    suggests a sci-fi/wearable-device visual theme but that is not confirmed by any
    source read, so look.shape and look.themes are left empty rather than guessed.
    Hackers Teaching Hackers (HTH) is a real, ongoing Columbus, Ohio InfoSec
    conference but has no entry in _data/events.yml, so event stays "other".
last_modified_date: '2026-09-07'
---

The Scouter-SAO is a shitty add-on (SAO) built to plug into the ScryptKeeper, the 2021 Hackers Teaching Hackers (HTH) conference badge designed by syn-ack-zack (Zack Nagaich). Unlike the ScryptKeeper itself, which runs CircuitPython on a full microcontroller, the Scouter-SAO is a passive board: its schematic shows nothing more than a standard v1.69bis 6-pin SAO connector, one resistor, and four LEDs, all powered straight off the host badge's SAO header with no onboard logic of its own.

The board's KiCad files (shared as a zipped project alongside standalone Gerbers in the HTHackers/ScryptKeeper GitHub repo) carry the internal name "TFTS-HTH-SAO-Scout-IS" and silkscreen text crediting "@syn-ack-zack" and "@mcm3nac3" as the designers, alongside "HACKERS TEACHING HACKERS." No accompanying writeup, photo, or storefront listing for the SAO turned up in searches, so its intended shape, artwork, colors, price, and how (or whether) it was distributed to attendees remain unknown.

## Make your own

The repo includes a complete KiCad project (schematic, PCB layout, and netlist) plus a standalone `gerber/` folder with fabrication-ready Gerbers and drill files, so the board can be reproduced as-is. No bill of materials or firmware is included, but the schematic itself specifies the parts needed: one SAO v1.69bis connector, four LEDs, and one resistor.
