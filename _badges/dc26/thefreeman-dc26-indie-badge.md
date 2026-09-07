---
title: THEFREEMAN - DEF CON 26 Indie Badge
id: dc26-thefreeman-dc26-indie-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Twinkle Twinkie
  url: https://hackaday.io/twinkletwinkie
summary: A single-layer PCB-art indie badge shaped like a Half-Life 2 Vortigaunt head, with 5 OSRAM reverse-mount TOPLEDs (3 red, 2 orange) shining through the board to light the eyes, powered by a CR2032; about 40 were made for DEF CON 26 and the KiCad/Gerber files are posted.
functions: Decorative wearable; LEDs illuminate the Vortigaunt eyes through the single-layer board. No interactive electronics beyond the lighting.
look:
  colors:
  - green
  shape: null
  themes:
  - video games
  - pop culture
tech:
  mcu: none
  leds:
    count: 5
    type: reverse-mount
    note: 3x OSRAM TOPLED red (LS T776-P2S1-1-Z), 2x OSRAM TOPLED orange (LO T776-Q2T1-24-Z), mounted reverse-side so light shines through the single-layer PCB to backlight the eyes.
  display: none
  connectivity:
  - none
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: about 40
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://hackaday.io/project/158663/files
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260519083607/https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
- label: hackaday.io/project/158663/log/146964-a-quick-summary
  url: https://hackaday.io/project/158663/log/146964-a-quick-summary
  kind: hackaday
- label: hackaday.io/project/158663/files
  url: https://hackaday.io/project/158663/files
  kind: hackaday
images:
- file: assets/images/badges/dc26/thefreeman-dc26-indie-badge/312168004e.jpg
  source: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  credit: Twinkle Twinkie
  caption: THEFREEMAN indie badge, Vortigaunt-head PCB with reverse-mount LED eyes
  archived: https://web.archive.org/web/20260519083607/https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  title: THEFREEMAN - DEF CON 26 INDIE BADGE
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260519083607/https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
- kind: url
  url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  title: THEFREEMAN - DEF CON 26 INDIE BADGE (overview)
  accessed: '2026-09-07'
  note: Confirmed maker, event/year, LED part numbers, battery, quantity (~40), and that design files are free downloads.
  archived: https://web.archive.org/web/20260519083607/https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
- kind: url
  url: https://hackaday.io/project/158663/log/146964-a-quick-summary
  title: A quick summary (project log)
  accessed: '2026-09-07'
  note: Confirms ~40 boards for DEF CON 26; notes it is the second board revision, added copper fill for grounding, removed an unneeded resistor to improve battery life, and mentions a misspelled Twitter handle on this run.
- kind: url
  url: https://hackaday.io/project/158663/files
  title: THEFREEMAN project files
  accessed: '2026-09-07'
  note: Lists two downloadable zips - "THE_FREEMAN_Badge_hackaday.zip" (KiCad/Gerbers for the badge) and "THE_FREEMAN_SAO_hackaday.zip" (KiCad/Gerbers for a matching SAO) - both free downloads, license not stated on the page.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own Hackaday.io project page and log confirm the core facts (design, LEDs, battery, ~40 made, free KiCad/Gerber files). Price and exact distribution method (free giveaway vs. sold) are not stated anywhere on the project page; left empty rather than guessed. A companion SAO (same theme) also has files posted under this same project - see reported "other item" below, since it appears to be a separate physical piece rather than part of this badge.
last_modified_date: '2026-09-07'
---

THEFREEMAN is an indie DEF CON 26 (2018) badge by Twinkle Twinkie, shaped like the Vortigaunt head from Half-Life 2. It's a deliberately single-layer PCB, used partly as a learning exercise in KiCad and partly as an experiment in treating a bare circuit board as an art medium - the absence of a second copper layer is what lets the board's traces and silkscreen read as the creature's face. Five reverse-mounted OSRAM TOPLED LEDs (three red, two orange) sit behind the board and shine through it to light the Vortigaunt's eyes, powered by a single CR2032 coin cell. About 40 were made for the con.

The project log describes this as the second board revision: the first prototype skipped a copper ground fill on purpose so the maker could understand the circuit before adding it back, and this run adds that fill along with removing an unnecessary resistor, which the maker says meaningfully improved battery life. The run wasn't perfect - the log notes a misspelled Twitter handle on the boards - and the maker mentions plans to share build lessons via video.

## Make your own

KiCad and Gerber files for the badge are posted as a free download on the Hackaday.io project's Files tab ("THE_FREEMAN_Badge_hackaday.zip"). A second archive on the same page, "THE_FREEMAN_SAO_hackaday.zip", holds KiCad/Gerber files for a matching SAO version of the same Vortigaunt-head design - it is not described as part of this badge and may be a separate item (see report).
