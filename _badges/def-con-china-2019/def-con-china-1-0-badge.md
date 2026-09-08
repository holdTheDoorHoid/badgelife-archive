---
title: DEF CON China 1.0 Badge
id: def-con-china-2019-def-con-china-1-0-badge
layout: badge
parent: DEF CON China 1.0
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: def-con-china-2019
year: 2019
makers:
- name: Grand Idea Studio (Joe Grand)
  url: https://grandideastudio.com/portfolio/other/defcon-china-2019-badge/
summary: 'The official electronic badge for DEF CON China 1.0, built on a flexible printed circuit board shaped like a tree. Attendees light up the tree by completing tasks during the conference.'
functions: 'A game in which attendees illuminate an on-badge tree by completing conference tasks. Also has USB connectivity and motion detection via an onboard accelerometer.'
look:
  colors: []
  shape: tree
  themes:
  - security
  - hardware tool
  - puzzle
tech:
  mcu: ATmega328P (Arduino Pro Mini, 3.3V @ 8MHz)
  leds: null
  display: none
  connectivity:
  - usb
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '3300'
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to DEF CON China 1.0 (2019) attendees in Beijing; six silkscreen variants denoted attendee type (Human, Speaker, Village, Goon, Press, Sponsor).
make_your_own:
  open_source: yes
  hardware_url: https://grandideastudio.com/media/dcn1_bdg_schematic.pdf
  firmware_url: https://grandideastudio.com/media/dcn1_bdg_source.zip
  gerbers_url: https://grandideastudio.com/media/dcn1_fpc_shield_gerbers.zip
  bom_url: https://grandideastudio.com/media/dcn1_bdg_bom.pdf
  eda_tool: null
  license: CC BY 4.0
  fab_url: https://oshpark.com/shared_projects/WGHZCahO
  notes: 'Documentation on the maker''s site also includes a block diagram, assembly drawing, test procedure (with video), a Raspberry Pi programming script, and design slides/videos. Two companion boards (FPC Shield, FPC Breakout) have their own schematics, BOM, assembly drawings, Gerbers, and OSH Park shares.'
links:
- label: grandideastudio.com/portfolio/other/defcon-china-2019-badge
  url: https://grandideastudio.com/portfolio/other/defcon-china-2019-badge/
  kind: website
- label: 'FPC Shield — OSH Park shared project'
  url: https://oshpark.com/shared_projects/WGHZCahO
  kind: fab
- label: 'FPC Breakout — OSH Park shared project'
  url: https://oshpark.com/shared_projects/X4QDh3nj
  kind: fab
- label: 'Creating the DEFCON China 1.0 Badge (YouTube)'
  url: https://www.youtube.com/watch?v=Y9YJS4toHZU&list=PL9fPq3eQfaaCy4N0nLoX7MtmxQEkrWL_i&index=11
  kind: video
- label: 'A Look at the DEFCON China 1.0 Badge (YouTube)'
  url: https://www.youtube.com/watch?v=j8AlX0X2NUI
  kind: video
- label: 'Badge Demonstration (YouTube)'
  url: https://www.youtube.com/watch?v=JW9SDF1MAvQ
  kind: video
images:
- file: assets/images/badges/def-con-china-2019/def-con-china-1-0-badge/65985b0f37.jpg
  source: "https://grandideastudio.com/portfolio/other/defcon-china-2019-badge/"
  credit: "Grand Idea Studio"
  caption: "DEF CON China 1.0 badge, front, flexible PCB tree design"
- file: assets/images/badges/def-con-china-2019/def-con-china-1-0-badge/2ef7dde2ea.jpg
  source: "https://grandideastudio.com/portfolio/other/defcon-china-2019-badge/"
  credit: "Grand Idea Studio"
  caption: "DEF CON China 1.0 badge, detail view"
contact: {}
notes:
- 'Found by the event-year sweep, task con-def-con-china, which read the badge title and event correctly; no wording correction needed.'
status: released
sources:
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-china-2019-badge/
  title: DEF CON China 1.0 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-def-con-china); event read as ''DEF CON China 2019''.'
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-china-2019-badge/
  title: DEF CON China 1.0 Badge — Grand Idea Studio portfolio page
  accessed: '2026-09-08'
  note: 'Maker''s own project page: confirmed maker, event, MCU (ATmega328P / Arduino Pro Mini), power (CR2032), accelerometer, USB, tree-lighting game concept, 3,300 units across six attendee-type variants, CC BY 4.0 license, and links to schematics/BOM/gerbers/source code/videos.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'All core facts confirmed directly on the maker''s own portfolio page, which is thorough and unambiguous. LED count/type not stated anywhere on the page (only "tree-style illumination system"), so tech.leds is left null. No independent price or free/paid distribution statement was found; distribution is inferred as free_drop since DEF CON badges are given to attendees, but no source states this explicitly, so get_one.price and availability are left unset pending a source that says so. EDA tool not stated.'
last_modified_date: '2026-09-08'
---

The DEF CON China 1.0 Badge was the official electronic badge for DEF CON China 1.0, the only edition of the conference's short-lived international spinoff, held in Beijing in 2019. Designed by Joe Grand of Grand Idea Studio, it is built on a flexible printed circuit board shaped like a tree, with active electronics mounted on the flex substrate. The badge's primary function is a game: attendees illuminate the tree by completing tasks during the conference. It also carries USB connectivity and motion detection via an onboard accelerometer, and runs on an Arduino Pro Mini (ATmega328P, 3.3V @ 8MHz) powered by a single CR2032 coin cell.

Grand Idea Studio manufactured 3,300 units, each carrying unique artwork and a silkscreen color denoting one of six attendee types: Human, Speaker, Village, Goon, Press, and Sponsor.

## Make your own

All designs are released under a Creative Commons Attribution 4.0 International license. The maker's page hosts a full set of documentation for the badge itself — block diagram, schematic, bill of materials, assembly drawing, test procedure (with video), a Raspberry Pi programming script, and Arduino source code — plus design slides and several build/demo videos. Two companion boards used to program and interface with the badge, an FPC Shield and an FPC Breakout, are documented separately with their own schematics, BOMs, assembly drawings, Gerber files, and OSH Park shared projects for ordering the bare PCBs.
