---
title: RVAsec 2019 Badge
id: rvasec-2019-rvasec-2019-badge
layout: badge
parent: RVAsec 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rvasec-2019
year: 2019
makers:
- name: HackRVA
  url: https://www.hackrva.org/
summary: The eighth RVAsec conference badge, hand-built by HackRVA members from bare copper boards, running laser tag, a procedurally generated dungeon-crawler maze game, a badge-collecting social game, and a small onboard C interpreter used during the CTF.
functions: 'Laser Tag (infrared emitters/receivers report hits and timing to a base station), Maze (procedurally generated dungeon crawler with monsters and loot), Badge Monsters (a social exchange game where attendees collect monsters by interacting with other badges), and a C interpreter used for CTF challenges. A scoreboard feature was planned but cut for time.'
look:
  colors: []
  shape: null
  themes:
  - ctf
  - security
  - puzzle
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
  distribution:
  - free_drop
  where: Given to RVAsec 2019 attendees; not sold.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/HackRVA/badge2019interp
  eda_tool: null
  notes: 'Badge/laser-tag/maze firmware (with the C interpreter) is in HackRVA/badge2019interp; the laser-tag base station firmware is in HackRVA/master-base-2019. No hardware (schematic/Gerbers/BOM) repo was found.'
links:
- label: badge.gallery/badges/rvasec-2019-badge
  url: https://badge.gallery/badges/rvasec-2019-badge
  kind: website
- label: hackrva.org - 2019 HackRVA RVASec Badge
  url: https://www.hackrva.org/2019/07/2019-hackrva-rvasec-badge/
  kind: article
- label: 'GitHub: HackRVA/badge2019interp'
  url: https://github.com/HackRVA/badge2019interp
  kind: repo
- label: 'GitHub: HackRVA/master-base-2019'
  url: https://github.com/HackRVA/master-base-2019
  kind: repo
images:
  - file: assets/images/badges/rvasec-2019/rvasec-2019-badge/c08dd852ec.jpg
    source: "https://www.hackrva.org/2019/07/2019-hackrva-rvasec-badge/"
    credit: "HackRVA"
    caption: "The finished 2019 RVAsec badge"
  - file: assets/images/badges/rvasec-2019/rvasec-2019-badge/eb23720012.jpg
    source: "https://www.hackrva.org/2019/07/2019-hackrva-rvasec-badge/"
    credit: "HackRVA"
    caption: "RVAsec 2019 badge assembly / build day"
contact: {}
notes:
- HackRVA electronic badge for RVAsec 2019. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task con-rvasec.
- 'Confirmed by HackRVA''s own blog post and badge.gallery. Sweep''s one-line description matches; no title correction needed.'
- 'Hardware specifics (MCU, LED count/type, display, power) were not stated on the maker''s blog or in the firmware README beyond mentioning RGB LED, audio, IR, and a D-pad in the interpreter repo; left null/empty rather than guessed.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/rvasec-2019-badge
  title: RVAsec 2019 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-rvasec); event read as ''RVAsec 2019''.'
- kind: url
  url: https://www.hackrva.org/2019/07/2019-hackrva-rvasec-badge/
  title: 2019 HackRVA RVASec Badge - hack.RVA
  accessed: '2026-09-10'
  note: "Maker's own writeup: badge functions (laser tag, maze, badge monsters, C interpreter), in-house build process, and source photos."
- kind: url
  url: https://github.com/HackRVA/badge2019interp
  title: 'GitHub: HackRVA/badge2019interp'
  accessed: '2026-09-10'
  note: 'Firmware repo README; describes onboard C interpreter, LCD/framebuffer, USB, RGB LED, IR, buttons/D-pad, audio, ADC, and limited (~8KB) RAM, but not a specific MCU part number.'
- kind: url
  url: https://github.com/HackRVA/master-base-2019
  title: 'GitHub: HackRVA/master-base-2019'
  accessed: '2026-09-10'
  note: 'Base station firmware repo for the laser-tag game, linked from the maker blog post.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Core facts (maker, event, functions, distribution, firmware repos, photos) confirmed on HackRVA''s own blog. Hardware details (exact MCU, LED type/count, display, battery) were not stated anywhere found and are left empty rather than guessed. No price/quantity found since the badge was given to attendees, not sold; no dedicated hardware/Gerbers repo was located.'
last_modified_date: '2026-09-10'
---

The 2019 RVAsec badge was the eighth in HackRVA's annual run of conference badges, built the way the group builds all of them: designed, etched from bare copper, populated, and programmed entirely in-house by HackRVA members over several months of planning and build days. It shipped free to RVAsec 2019 attendees rather than being sold.

Functionally it centered on infrared-based laser tag, where the badge's IR emitters and receivers reported hits and timing back to a base station (firmware in `HackRVA/master-base-2019`). Alongside that it ran Maze, a procedurally generated dungeon crawler with monsters and loot, and Badge Monsters, a social game where attendees collected monsters by interacting with other people's badges. A small onboard C interpreter, written by Dustin Firebaugh, doubled as a CTF challenge platform; a planned scoreboard feature didn't make it in due to time constraints. HackRVA and attendees reportedly called it their best badge year yet.

## Make your own

The badge and game firmware (including the C interpreter, LCD/framebuffer handling, IR, RGB LED, D-pad input, audio, and ADC support) is public at `HackRVA/badge2019interp`; the interpreter's own README notes it's "no where near a full C implementation" and that the badge has only about 8KB of usable RAM. The laser-tag base station firmware is separately public at `HackRVA/master-base-2019`. No hardware files (schematic, Gerbers, or BOM) were found published for this specific badge.
