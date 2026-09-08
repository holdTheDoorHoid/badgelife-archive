---
title: Air Jewel
id: fri3d-2018-fri3d-2018-air-jewel
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
- name: Wim Van Gool
  url: null
- name: Bert Outtier
  url: null
summary: The Air jewel is an add-on expansion board for the Fri3d Camp 2018 Ph0xx badge that interfaces a dust particle sensor and a GPS module to the badge; two revisions (Air.00 and Air.01) of the Altium design live in the repo's design/jewels folder.
functions: Adds air-quality sensing (dust particle sensor) and GPS positioning to the Ph0xx badge.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - measurement
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - gps
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
  hardware_url: https://github.com/Fri3dCamp/badge/tree/master/design/jewels/Air.01
  firmware_url: https://github.com/Fri3dCamp/badge
  eda_tool: Altium
links:
- label: github.com/Fri3dCamp/badge
  url: https://github.com/Fri3dCamp/badge
  kind: repo
  archived: https://web.archive.org/web/20260312123042/https://github.com/Fri3dCamp/badge
- label: github.com/Fri3dCamp/badge/tree/master/design/jewels/Air.01
  url: https://github.com/Fri3dCamp/badge/tree/master/design/jewels/Air.01
  kind: repo
- label: hackaday.io/project/160451-ph0xx
  url: https://hackaday.io/project/160451-ph0xx
  kind: hackaday
  archived: https://web.archive.org/web/20260904220754/https://hackaday.io/project/160451-ph0xx
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Fri3dCamp/badge
  title: Fri3dCamp/badge - Elk hacker/maker/DIY Kamp heeft zijn eigen badge nodig...
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260312123042/https://github.com/Fri3dCamp/badge
- kind: url
  url: https://hackaday.io/project/160451-ph0xx
  title: 'Ph0xx: Fri3d Camp 2018 badge project page'
  accessed: '2026-09-07'
  note: Confirms the Ph0xx badge is ESP32-WROOM-32 based, credits Wim Van Gool and Bert Outtier alongside Fri3d Camp, ~600 badges made, and lists the Air jewel (dust sensor + GPS) and Bot jewel (servo power for a bipedal robot build) as the two expansion jewels.
  archived: https://web.archive.org/web/20260904220754/https://hackaday.io/project/160451-ph0xx
- kind: url
  url: https://github.com/Fri3dCamp/badge/tree/master/design/jewels/Air.01
  title: badge/design/jewels/Air.01 at master - Fri3dCamp/badge
  accessed: '2026-09-07'
  note: Confirms open Altium design files (SchDoc/PcbDoc) exist for the Air jewel, revision 01; a separate Air.00 folder holds the first revision. No README or photos of the jewel itself found in the repo (media/ only has main-badge photos).
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: Fact-check pass (2026-09-07) re-fetched all three cited sources and confirmed every non-empty field and body sentence. github.com/Fri3dCamp/badge's own README confirms it is the Fri3d Camp Badge 2018 repo; the GitHub API confirms both design/jewels/Air.00 and design/jewels/Air.01 folders exist with Altium SchDoc/PcbDoc files, and a code/ folder with firmware for the host badge. hackaday.io/project/160451-ph0xx (the makers' own project page) confirms the ESP32-WROOM-32 Ph0xx badge, credits Wim Van Gool and Bert Outtier alongside Fri3d Camp, documents ~600-650 units assembled, and confirms the Air jewel interfaces a dust particle sensor and GPS (and was used on a weather-balloon flight, per that page - not added to this entry since it's a detail about Ph0xx's project log rather than the jewel entry itself, noted here for a future pass). The Air jewel itself has no README, BOM, part numbers, price, quantity, or photos in any cited source, so those fields remain correctly empty. No
    contradictions found between sources. Confidence held at medium because all Air-jewel-specific detail (as opposed to the parent Ph0xx badge) rests on the Hackaday project log's prose rather than a dedicated jewel document.
last_modified_date: '2026-09-07'
model:
  file: assets/models/fri3d-2018/fri3d-2018-air-jewel.glb
  method: gerber
  source_file: design/jewels/Air.01/OUTPUT/Gerber
  generated: '2026-09-07'
  bytes: 49572
  size_mm:
  - 420.0
  - 297.0
  note: The published files have no board outline, so the model is shown on a rectangular board.
---

The Air jewel is one of two expansion "jewels" built for Fri3d Camp's 2018 Ph0xx conference badge, alongside the servo-driving Bot jewel for a bipedal robot build. It plugs into the ESP32-WROOM-32-based Ph0xx badge and adds a dust particle sensor and a GPS module, letting badge wearers log air quality and location data during the camp. Fri3d Camp is a Belgian family hacker/maker event, and the Ph0xx badge (around 600 units) was designed by Wim Van Gool and Bert Outtier together with the Fri3d Camp team for the August 2018 event.

The jewel went through at least two hardware revisions, Air.00 and Air.01, both published as Altium schematic and PCB files in the Fri3dCamp/badge GitHub repository under `design/jewels/`. The repository does not include a dedicated README, bill of materials, or photos for the Air jewel itself, so exact sensor part numbers and how it was distributed (e.g., whether every attendee received one or it was a separate build) could not be confirmed from available sources.
