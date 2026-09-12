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
functions: TV-B-Gone mode (cycles ~135 common TV "off" codes one at a time) and an MQ303 breathalyzer mode (heats the sensor for ~5 seconds, then displays a raw sensor-resistance value rather than a BAC reading); modes are selected with the left/right d-pad buttons.
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
  - hardware tool
tech:
  mcu: Cypress PSoC
  leds: null
  display: 0.96" 128x64 LCD (dual-color)
  connectivity:
  - ir
  battery: 2x AA
  sao_version: null
get_one:
  price: $80
  price_usd: 80
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold assembled on Tindie by phelgon; also distributed at DEF CON 26 and 27. Tindie listing shows out of stock since 2022-10-21.
make_your_own:
  open_source: true
  hardware_url: https://github.com/ellwoodthewood/DC858_619_Badge
  firmware_url: https://github.com/ellwoodthewood/DC858_619_Badge/blob/master/BeachDay%20Clean%20FW%20Project.7z
  gerbers_url: https://github.com/ellwoodthewood/DC858_619_Badge/blob/master/BEACHDAY-XB%20Gerbers.pdf
  bom_url: https://github.com/ellwoodthewood/DC858_619_Badge/blob/master/BEACHDAY-XB.xlsx
  eda_tool: null
  license: null
  fab_url: null
  notes: Repo also includes BEACHDAY-XB.pdf, the schematic/layout PDF, named for the board "BEACHDAY-XB."
links:
- label: hackaday.io/project/160782-dc858619-beach-day-unofficial-def-con-26-badge
  url: https://hackaday.io/project/160782-dc858619-beach-day-unofficial-def-con-26-badge
  kind: hackaday
- label: github.com/ellwoodthewood/DC858_619_Badge
  url: https://github.com/ellwoodthewood/DC858_619_Badge
  kind: repo
  archived: https://web.archive.org/web/20260504131605/https://github.com/ellwoodthewood/DC858_619_Badge
- label: www.tindie.com/products/phelgon/dc858619-unofficial-def-con-badge
  url: https://www.tindie.com/products/phelgon/dc858619-unofficial-def-con-badge/
  kind: store
  archived: https://web.archive.org/web/20260503104231/https://www.tindie.com/products/phelgon/dc858619-unofficial-def-con-badge/
images:
- file: assets/images/badges/dc26/dc858-619-beach-day-badge/e9b1e98644.jpg
  source: https://hackaday.io/project/160782-dc858619-beach-day-unofficial-def-con-26-badge
  credit: DC858/619 / ellwood
  caption: DC858/619 'Beach Day' unofficial DEF CON 26 badge
- file: assets/images/badges/dc26/dc858-619-beach-day-badge/178f498788.jpg
  source: https://www.tindie.com/products/phelgon/dc858619-unofficial-def-con-badge/
  credit: phelgon
  caption: The DC858/619 Beach Day Badge, fully assembled
  archived: https://web.archive.org/web/20260503104231/https://www.tindie.com/products/phelgon/dc858619-unofficial-def-con-badge/
contact: {}
notes:
- Fully assembled unofficial electronic badge for DEF CON attendees from the DC858/619 (San Diego) DEF CON group, with RGB LEDs, MQ303 breathalyzer, IR TV-B-Gone, 128x64 LCD, and SAO support; design files on GitHub (ellwoodthewood/DC858_619_Badge). Found by the event-year sweep, task con-dc404.
- The community sheet read the event as "DC858 2018"; the maker's Tindie listing confirms it was made for DEF CON 26 (2018), and also sold at DEF CON 27 (2019).
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
  note: Confirmed maker (DC858/619, San Diego DEF CON group), event/year (DEF CON 26, 2018), the two operating modes (TV-B-Gone and MQ303 breathalyzer), and pulled the project photo used above.
- kind: url
  url: https://github.com/ellwoodthewood/DC858_619_Badge
  title: ellwoodthewood/DC858_619_Badge
  accessed: '2026-09-07'
  note: README confirms the two d-pad-selected modes; repo file listing confirms published gerbers (PDF), schematic/layout (PDF), BoM (xlsx), and firmware (7z archive) — used for open_source and the make_your_own links.
  archived: https://web.archive.org/web/20260504131605/https://github.com/ellwoodthewood/DC858_619_Badge
- kind: url
  url: https://www.tindie.com/products/phelgon/dc858619-unofficial-def-con-badge/
  title: DC858/619 Unofficial DEF CON Badge ("Beach Day Badge")
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-dc404); event read as ''DC858 2018''.'
  archived: https://web.archive.org/web/20260503104231/https://www.tindie.com/products/phelgon/dc858619-unofficial-def-con-badge/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own Hackaday project page and GitHub repo confirm what the badge is, who made it, and that hardware+firmware are open source, but neither names the MCU, LED count/type, display, battery, price, quantity made, or how/whether it was distributed beyond the DC858/619 group at DEF CON 26 — left empty rather than guessed. No press coverage (Hackaday.com, Reddit, forums) was found describing it further. Web search budget for this session was exhausted before additional searches (title+event, maker+badge) could be run, so this should be treated as a partial pass if deeper distribution/hardware detail is needed later. Merged with duplicate entry 'DC858/619 Unofficial DEF CON Badge ("Beach Day Badge")' (dc26-dc858-619-unofficial-def-con-badge-beach-day-badge).
last_modified_date: '2026-09-08'
redirect_from:
- /badges/dc26/dc858-619-unofficial-def-con-badge-beach-day-badge/
---

The "Beach Day" badge was an unofficial DEF CON 26 (2018) badge made by DC858/619, the DEF CON group covering the 858 and 619 area codes around San Diego, designed by a member going by "ellwood." Rather than blinky LEDs, its headline features are two novelty modes selected with the badge's d-pad: a TV-B-Gone mode that fires through roughly 135 of the most common television "off" infrared codes one after another, and an MQ303 gas-sensor "breathalyzer" mode. The breathalyzer heats the sensor for about five seconds and then reports the raw sensor resistance rather than a calibrated blood-alcohol estimate — a deliberate choice the maker described as avoiding any claim that the badge told someone they weren't drunk.

The project is fully open source: the GitHub repository (board name "BEACHDAY-XB") includes the Gerber files, a schematic/layout PDF, a bill of materials spreadsheet, and a firmware archive, so the design can be reproduced by anyone willing to source the MQ303 sensor and an IR emitter. Neither the Hackaday.io project page nor the repository documents the specific MCU, LED hardware, display, battery, price, or production quantity, and no secondary coverage of the badge (press, forums, storefronts) turned up in this pass, so those fields are left blank rather than guessed.

## Notes merged from the duplicate entry "DC858/619 Unofficial DEF CON Badge ("Beach Day Badge")"

The DC858/619 "Beach Day Badge" is an unofficial electronic badge made by phelgon for the DC858/619 DEF CON group (San Diego) and sold assembled through Tindie starting around DEF CON 26 in 2018, with continued sales through DEF CON 27. It leans into novelty features rather than pure blinky aesthetics: a d-pad cycles between a TV-B-Gone mode that runs through roughly 135 common television power-off codes, and a tongue-in-cheek "breathalyzer" mode built around an MQ303 gas sensor that displays a raw resistance reading after a five-second heat-up rather than a calibrated blood-alcohol figure. The badge also carries RGB LEDs, a 0.96" 128x64 dual-color LCD, runs on 2x AA batteries, and ships with a lanyard.

The badge is built around a Cypress PSoC microcontroller per the maker's own store listing. Hardware and firmware are fully open, with schematics, Gerbers, a bill of materials, and firmware source published on GitHub. The Tindie listing shows the badge sold for $80 and has been marked out of stock since October 2022.

## Make your own

Design files — PCB schematic (PDF), Gerbers, bill of materials (XLSX), and firmware (as a 7z archive) — are published at github.com/ellwoodthewood/DC858_619_Badge.
