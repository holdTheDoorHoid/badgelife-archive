---
title: DEF CON Shoot 31 Badge
id: dc31-def-con-shoot-31-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: seeess
summary: 'A non-electronic, wearable badge made for the unofficial DEF CON Shoot 31 side event: a 3D-printed AR-15 trigger-crank assembly worn on a lanyard, adapted by maker seeess from an existing FOSSCAD trigger-crank design.'
functions: 'No electronic functions. The printed parts assemble into a working mechanical trigger-crank mechanism (a captive spring-loaded pusher, an adjustable paddle, and two side clamshells held together with machine screws), attached to a lanyard through a cellphone-loop fitting screwed onto one of the bolts.'
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - none
  battery: none
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/seeess/Defcon-Shoot-31-Badge
  firmware_url: null
  eda_tool: null
links:
- label: github.com/seeess/Defcon-Shoot-31-Badge
  url: https://github.com/seeess/Defcon-Shoot-31-Badge
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: listed
sources:
- kind: url
  url: https://github.com/seeess/Defcon-Shoot-31-Badge
  title: DEF CON Shoot 31 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc31''.'
- kind: url
  url: https://raw.githubusercontent.com/seeess/Defcon-Shoot-31-Badge/main/README.md
  title: 'Defcon-Shoot-31-Badge README'
  accessed: '2026-09-07'
  note: 'Maker''s own build notes confirming this is a 3D-printed, non-electronic AR-15 trigger crank adapted from a FOSSCAD design, with printed parts list, print settings, and hardware (screws/nuts) list; no price, quantity, or photos given.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is the "badge" for the unofficial DEF CON Shoot side event (a separate, unofficial shooting-range meetup held alongside DEF CON, run with help from a person the maker refers to as "deviant"), not an electronic conference badge or SAO. It is purely mechanical (a 3D-printed AR-15 trigger crank, adapted from a FOSSCAD design) worn on a lanyard; no battery, MCU, or LEDs. The maker (seeess) has made a "DEF CON Shoot" badge most years, alternating between electronic and non-electronic designs (e.g. an electronic one for DC23/DC27, and simple novelty items like a chalk-round-and-sticker badge for DC24) -- this DC31 edition is one of the non-electronic years. The GitHub repo (STL files + a build-notes README) has no price, quantity-made, availability, or photos of the assembled item, and no other page with those details could be found, so get_one fields and images are left empty rather than guessed. A DEF CON forum post titled "Defcon Shoot Badge (non-electronic)" was found but is dated 2016 and describes an unrelated earlier year''s design (a 40mm chalk round), so it was not used as a source here.'
last_modified_date: '2026-09-07'
---

The DEF CON Shoot is an unofficial side event held alongside DEF CON where attendees go shoot firearms together off-site; for several years, GitHub user and badgelife maker seeess has put together a small run of "badges" specifically for that event, separate from the main conference's badge. Unlike some of seeess's other Shoot badges, which have been electronic (buttons, a 7-segment shot counter, a tilt sensor), the DC31 (2023) edition is purely mechanical: a 3D-printed replica AR-15 trigger crank, worn on a lanyard, built from a design seeess adapted from an existing FOSSCAD trigger-crank model.

The build is documented on GitHub as a set of STL files (crank, paddle, pusher, and two side clamshells) plus a README of build notes: print the parts in PETG, assemble with M2.5 machine screws and nuts plus a self-tapping M2 screw joining the paddle to the crank, and attach a lanyard via a cellphone-loop fitting screwed onto one of the bolts. The notes are practical and print-troubleshooting-focused (recommended scale adjustments per part, where first-layer squish causes fit problems, why the pusher needs to move freely for the mechanism to reset) rather than a sales listing, and no price, production quantity, or photos of a finished/assembled badge could be found for this specific year.

## Make your own

All design files are published in the GitHub repository linked above. To build one: 3D print `crank.stl`, `paddle.stl`, `BOLT4.stl`, and the side clamshell STLs in PETG (the repo's README gives specific per-part scale adjustments the maker used to get a good fit), then assemble with 4x M2.5x30mm machine screws and nuts, a black M2 self-tapping screw to join the paddle to the crank, and washers, following the fit and reset-spring notes in the README.
