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
  open_source: yes
  hardware_url: https://github.com/Fri3dCamp/badge/tree/master/design/jewels/Air.01
  firmware_url: https://github.com/Fri3dCamp/badge
  eda_tool: Altium
links:
- label: github.com/Fri3dCamp/badge
  url: https://github.com/Fri3dCamp/badge
  kind: repo
- label: github.com/Fri3dCamp/badge/tree/master/design/jewels/Air.01
  url: https://github.com/Fri3dCamp/badge/tree/master/design/jewels/Air.01
  kind: repo
- label: hackaday.io/project/160451-ph0xx
  url: https://hackaday.io/project/160451-ph0xx
  kind: hackaday
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
- kind: url
  url: https://hackaday.io/project/160451-ph0xx
  title: 'Ph0xx: Fri3d Camp 2018 badge project page'
  accessed: '2026-09-07'
  note: Confirms the Ph0xx badge is ESP32-WROOM-32 based, credits Wim Van Gool and
    Bert Outtier alongside Fri3d Camp, ~600 badges made, and lists the Air jewel
    (dust sensor + GPS) and Bot jewel (servo power for a bipedal robot build) as
    the two expansion jewels.
- kind: url
  url: https://github.com/Fri3dCamp/badge/tree/master/design/jewels/Air.01
  title: badge/design/jewels/Air.01 at master - Fri3dCamp/badge
  accessed: '2026-09-07'
  note: Confirms open Altium design files (SchDoc/PcbDoc) exist for the Air jewel,
    revision 01; a separate Air.00 folder holds the first revision. No README or
    photos of the jewel itself found in the repo (media/ only has main-badge photos).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The Ph0xx badge and its two jewels (Air, Bot) are well documented on Hackaday.io
    and in the Fri3dCamp/badge GitHub repo, but the repo has no README, BOM, or
    photos specific to the Air jewel itself - only raw Altium schematic/PCB files
    for both revisions (Air.00, Air.01). Could not confirm the exact dust sensor
    or GPS module part numbers, an MCU on the jewel board itself (it likely relies
    entirely on the host badge's ESP32), price, or production quantity for the
    jewel specifically (only the ~600-unit badge run is documented). No firmware
    file specific to the Air jewel was located within the search budget for this
    pass.
last_modified_date: '2026-09-07'
---

The Air jewel is one of two expansion "jewels" built for Fri3d Camp's 2018 Ph0xx conference badge, alongside the servo-driving Bot jewel for a bipedal robot build. It plugs into the ESP32-WROOM-32-based Ph0xx badge and adds a dust particle sensor and a GPS module, letting badge wearers log air quality and location data during the camp. Fri3d Camp is a Belgian family hacker/maker event, and the Ph0xx badge (around 600 units) was designed by Wim Van Gool and Bert Outtier together with the Fri3d Camp team for the August 2018 event.

The jewel went through at least two hardware revisions, Air.00 and Air.01, both published as Altium schematic and PCB files in the Fri3dCamp/badge GitHub repository under `design/jewels/`. The repository does not include a dedicated README, bill of materials, or photos for the Air jewel itself, so exact sensor part numbers and how it was distributed (e.g., whether every attendee received one or it was a separate build) could not be confirmed from available sources.
