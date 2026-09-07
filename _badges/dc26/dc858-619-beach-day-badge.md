---
title: DC858/619 "Beach Day" Unofficial DEF CON 26 badge
id: dc26-dc858-619-beach-day-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: DC858/619 (DEF CON Group San Diego) / ellwood
  url: https://hackaday.io/hacker/289190-ellwood
summary: Unofficial DEF CON 26 badge from the San Diego DEF CON group DC858/619, with a d-pad-selected TV-B-Gone mode (cycling roughly 135 common TV off codes) and an MQ303 breathalyzer mode that reports a deliberately fuzzy sensor-resistance reading rather than a BAC; gerbers, schematic, BoM and firmware are published.
functions: 'TV-B-Gone mode (cycles ~135 common TV "off" codes one at a time) and an MQ303 breathalyzer mode (heats the sensor for ~5 seconds, then displays a raw sensor-resistance value rather than a BAC reading); modes are selected with the left/right d-pad buttons.'
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - ir
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
  hardware_url: https://github.com/ellwoodthewood/DC858_619_Badge
  firmware_url: https://github.com/ellwoodthewood/DC858_619_Badge/blob/master/BeachDay%20Clean%20FW%20Project.7z
  gerbers_url: https://github.com/ellwoodthewood/DC858_619_Badge/blob/master/BEACHDAY-XB%20Gerbers.pdf
  bom_url: https://github.com/ellwoodthewood/DC858_619_Badge/blob/master/BEACHDAY-XB.xlsx
  eda_tool: null
  license: null
  fab_url: null
  notes: 'Repo also includes BEACHDAY-XB.pdf, the schematic/layout PDF, named for the board "BEACHDAY-XB."'
links:
- label: hackaday.io/project/160782-dc858619-beach-day-unofficial-def-con-26-badge
  url: https://hackaday.io/project/160782-dc858619-beach-day-unofficial-def-con-26-badge
  kind: hackaday
- label: github.com/ellwoodthewood/DC858_619_Badge
  url: https://github.com/ellwoodthewood/DC858_619_Badge
  kind: repo
images:
- file: assets/images/badges/dc26/dc858-619-beach-day-badge/e9b1e98644.jpg
  source: "https://hackaday.io/project/160782-dc858619-beach-day-unofficial-def-con-26-badge"
  credit: "DC858/619 / ellwood"
  caption: "DC858/619 'Beach Day' unofficial DEF CON 26 badge"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/160782-dc858619-beach-day-unofficial-def-con-26-badge
  title: DC858/619 "Beach Day" Unofficial DEF CON 26 badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/160782-dc858619-beach-day-unofficial-def-con-26-badge
  title: DC858/619 "Beach Day" Unofficial DEF CON 26 badge
  accessed: '2026-09-07'
  note: 'Confirmed maker (DC858/619, San Diego DEF CON group), event/year (DEF CON 26, 2018), the two operating modes (TV-B-Gone and MQ303 breathalyzer), and pulled the project photo used above.'
- kind: url
  url: https://github.com/ellwoodthewood/DC858_619_Badge
  title: ellwoodthewood/DC858_619_Badge
  accessed: '2026-09-07'
  note: 'README confirms the two d-pad-selected modes; repo file listing confirms published gerbers (PDF), schematic/layout (PDF), BoM (xlsx), and firmware (7z archive) — used for open_source and the make_your_own links.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own Hackaday project page and GitHub repo confirm what the badge is, who made it, and that hardware+firmware are open source, but neither names the MCU, LED count/type, display, battery, price, quantity made, or how/whether it was distributed beyond the DC858/619 group at DEF CON 26 — left empty rather than guessed. No press coverage (Hackaday.com, Reddit, forums) was found describing it further. Web search budget for this session was exhausted before additional searches (title+event, maker+badge) could be run, so this should be treated as a partial pass if deeper distribution/hardware detail is needed later.'
last_modified_date: '2026-09-07'
---

The "Beach Day" badge was an unofficial DEF CON 26 (2018) badge made by DC858/619, the DEF CON group covering the 858 and 619 area codes around San Diego, designed by a member going by "ellwood." Rather than blinky LEDs, its headline features are two novelty modes selected with the badge's d-pad: a TV-B-Gone mode that fires through roughly 135 of the most common television "off" infrared codes one after another, and an MQ303 gas-sensor "breathalyzer" mode. The breathalyzer heats the sensor for about five seconds and then reports the raw sensor resistance rather than a calibrated blood-alcohol estimate — a deliberate choice the maker described as avoiding any claim that the badge told someone they weren't drunk.

The project is fully open source: the GitHub repository (board name "BEACHDAY-XB") includes the Gerber files, a schematic/layout PDF, a bill of materials spreadsheet, and a firmware archive, so the design can be reproduced by anyone willing to source the MQ303 sensor and an IR emitter. Neither the Hackaday.io project page nor the repository documents the specific MCU, LED hardware, display, battery, price, or production quantity, and no secondary coverage of the badge (press, forums, storefronts) turned up in this pass, so those fields are left blank rather than guessed.
