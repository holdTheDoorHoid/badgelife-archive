---
title: Bot Jewel
id: fri3d-2018-fri3d-2018-bot-jewel
layout: badge
parent: Fri3d 2018
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: fri3d-2018
year: 2018
makers:
- name: Fri3d Camp
  url: https://github.com/Fri3dCamp
summary: The Bot jewel is an add-on board for the Fri3d Camp 2018 Ph0xx badge that boosts the badge's power output to drive four large servos and serves as the building block of a bipedal robot; its Altium design (Bot.00) lives in the repo's design/jewels folder.
functions: Boosts the Ph0xx badge power output to drive four large servos; used as the building block of a bipedal robot built from multiple badges/jewels.
look:
  colors: []
  shape: null
  themes:
  - robot
tech:
  mcu: null
  leds: null
  display: null
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
  hardware_url: https://github.com/Fri3dCamp/badge/tree/master/design/jewels/Bot.00
  firmware_url: null
  eda_tool: Altium
links:
- label: github.com/Fri3dCamp/badge
  url: https://github.com/Fri3dCamp/badge
  kind: repo
  archived: https://web.archive.org/web/20260312123042/https://github.com/Fri3dCamp/badge
- label: github.com/Fri3dCamp/badge/tree/master/design/jewels/Bot.00
  url: https://github.com/Fri3dCamp/badge/tree/master/design/jewels/Bot.00
  kind: repo
- label: hackaday.io/project/160451-ph0xx
  url: https://hackaday.io/project/160451-ph0xx
  kind: hackaday
  archived: https://web.archive.org/web/20260904220754/https://hackaday.io/project/160451-ph0xx
images: []
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/Fri3dCamp/badge
  title: Fri3dCamp/badge - Elk hacker/maker/DIY Kamp heeft zijn eigen badge nodig...
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260312123042/https://github.com/Fri3dCamp/badge
- kind: url
  url: https://hackaday.io/project/160451-ph0xx
  title: Ph0xx | Hackaday.io
  accessed: '2026-09-07'
  note: 'Project description confirms the Bot jewel''s function: ''boosts the power to drive 4 large servos and is used as building block of the bi-pedal robot.'' Also gives Ph0xx badge specs (ESP32-WROOM-32, two 5x7 LED arrays, ADXL345 accelerometer, 18650 battery, Lego Technic-compatible holes) and credits Wim Van Gool (Hackaday.io user Brubacker) as project lead for Fri3d Camp.'
  archived: https://web.archive.org/web/20260904220754/https://hackaday.io/project/160451-ph0xx
- kind: url
  url: https://github.com/Fri3dCamp/badge/tree/master/design/jewels/Bot.00
  title: badge/design/jewels/Bot.00 at master - Fri3dCamp/badge
  accessed: '2026-09-07'
  note: Confirms design files are Altium (Fri3D_Bot_2018_00.SchDoc/.PcbDoc), and that the OUTPUT subfolder holds Gerbers, a BOM, and a PDF - i.e. hardware is openly published.
- kind: url
  url: https://github.com/Fri3dCamp/badge/tree/master/design/jewels
  title: badge/design/jewels at master - Fri3dCamp/badge
  accessed: '2026-09-07'
  note: 'Lists the jewels made for this badge: Air.00, Air.01, and Bot.00 (this item).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Could not find any photograph of the assembled Bot jewel itself (only Altium schematic/PCB source files and a PDF export in the repo's OUTPUT folder, plus general badge photos of the Ph0xx badge itself with no jewel visible/labeled) - no images saved. No pricing, quantity-made, or distribution details found; this was a maker-community add-on, not something sold separately, so those fields are likely not applicable rather than unknown. MCU/LED/display fields left empty because the jewel is a passive power-boost board for servos, not documented with its own chip - the badge's main ESP32-WROOM-32 module or a header pin apparently drives the servos through the boosted rail, but exact tech (motor driver IC, connector pinout) is in the Altium files, not the pages read here.
last_modified_date: '2026-09-07'
model:
  file: assets/models/fri3d-2018/fri3d-2018-bot-jewel.glb
  method: gerber
  source_file: design/jewels/Bot.00/OUTPUT/Gerber
  generated: '2026-09-07'
  bytes: 50396
  size_mm:
  - 420.0
  - 297.0
  note: The published files have no board outline, so the model is shown on a rectangular board.
---

The Bot jewel is a small expansion board for Fri3d Camp's 2018 "Ph0xx" badge (an ESP32-based badge given to the roughly 600 attendees of the Belgian family hacker/maker camp Fri3d Camp). Fri3d Camp badges have expansion connectors that accept plug-in "jewels," and two were designed alongside the 2018 badge: an Air jewel for dust-particle and GPS sensing, and this Bot jewel, which steps up the badge's power output enough to drive four large servos. According to the project's Hackaday.io page, the Bot jewel was built as "the building block of the bi-pedal robot" - i.e. attendees could combine badges and Bot jewels to actuate a walking robot.

The badge and its jewels were a community project credited to Fri3d Camp (Hackaday.io user Brubacker/Wim Van Gool led the writeup) and released as open hardware on GitHub. No separate sale, price, or production-quantity information was found; it does not appear to have been distributed or sold independently of the badge project.

## Make your own

The Bot jewel's hardware is published in the `Fri3dCamp/badge` repository under `design/jewels/Bot.00`, as an Altium project (`Fri3D_Bot_2018_00.PrjPcb`/`.SchDoc`/`.PcbDoc`). The `OUTPUT` subfolder there includes a rendered PDF, a bill of materials, and Gerber files ready for fabrication.
