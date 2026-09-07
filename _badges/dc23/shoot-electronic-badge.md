---
title: DEF CON 23 Shoot Electronic Badge
id: dc23-shoot-electronic-badge
layout: badge
parent: DC23
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc23
year: 2015
makers:
- name: seeess
  url: https://twitter.com/see_ess
summary: 'A DIY badge made for the unofficial "DEF CON Shoot" event at DEF CON 23. It packs a six-digit 7-segment display, a microphone, two buttons, and a tilt sensor into a shot counter/shot timer with several extra modes and mini-games.'
functions: 'Default mode is a microphone-triggered shot counter; other modes include a shot timer (measures time between shots), count up/down, a random-segment display mode, a "hype" mode that just displays "Defcon Shoot", an audio debug mode for setting the mic threshold, and a games submenu (a reaction-time game, a "dodge" game, and others). Settings include display brightness, refresh speed, and a tilt-sensor display flip.'
look:
  colors: []
  shape: null
  themes:
  - security
  - measurement
tech:
  mcu: PIC
  leds: null
  display: 6-digit 7-segment display
  connectivity: []
  inputs:
  - buttons
  - microphone
  - tilt sensor
  battery: 4x AA
  sao_version: none
get_one:
  price: $25
  price_usd: 25
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold to attendees at the unofficial DEF CON Shoot event at DEF CON 23 (2015); a glow-in-the-dark lanyard was included.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/seeess/Defcon-Shoot-23-Badge
  eda_tool: null
links:
- label: forum.defcon.org/forum/defcon/dc23-official-unofficial-parties-social-gatherings-events-contests/dc23-official-and-unofficial-events/unofficial-defcon-shoot/15239-defcon-23-shoot-electronic-badge
  url: https://forum.defcon.org/forum/defcon/dc23-official-unofficial-parties-social-gatherings-events-contests/dc23-official-and-unofficial-events/unofficial-defcon-shoot/15239-defcon-23-shoot-electronic-badge
  kind: social
- label: seeess/Defcon-Shoot-23-Badge (GitHub)
  url: https://github.com/seeess/Defcon-Shoot-23-Badge
  kind: repo
- label: "Defcon Shoot 23 Badge Full Overview (YouTube)"
  url: https://www.youtube.com/watch?v=awRr_h3DX8c
  kind: video
- label: "Hackaday: All The Unofficial Electronic Badges Of DEF CON"
  url: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  kind: article
images:
- file: assets/images/badges/dc23/shoot-electronic-badge/845c30e99d.jpg
  source: "https://github.com/seeess/Defcon-Shoot-23-Badge/"
  credit: "seeess"
  caption: "DEF CON 23 Shoot badge 7-segment display, showing volunteer/normal/black badge color modes"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://forum.defcon.org/forum/defcon/dc23-official-unofficial-parties-social-gatherings-events-contests/dc23-official-and-unofficial-events/unofficial-defcon-shoot/15239-defcon-23-shoot-electronic-badge
  title: DEF CON 23 Shoot Electronic Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc23''.'
- kind: url
  url: https://github.com/seeess/Defcon-Shoot-23-Badge
  title: "seeess/Defcon-Shoot-23-Badge: code and manual for the defcon shoot 23 badge"
  accessed: '2026-09-07'
  note: "README describes all display modes/games, includes badge photo; main.c firmware confirms a PIC microcontroller (\"flashing the pic\") and a 4xAA battery estimate; only firmware is published, no board files."
- kind: url
  url: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  title: "All The Unofficial Electronic Badges Of DEF CON"
  accessed: '2026-09-07'
  note: "Confirms maker (seeess), that this was his first microcontroller project (board layout help from someone else), the feature list, and the $25 price with glow-in-the-dark lanyard."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Event corrected from "other" to dc23 (DEF CON 23, 2015) based on the forum thread title and Hackaday coverage. Total quantity made is not stated on any source read; left empty. Availability left "unknown" since no source explicitly states current sold-out status (this was a one-time 2015 con sale, so it is very likely no longer available, but that was not directly stated). Exact PIC part number not found; only "the pic" is mentioned in the firmware source comments. look.colors left empty: the only colors mentioned are the display''s green/yellow/red 7-segment digit colors denoting volunteer/normal/black-badge holders, not PCB or case colors.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/shoot-electronic-badge/
---

The DEF CON 23 Shoot Electronic Badge was made by seeess for the unofficial "DEF CON Shoot" event at DEF CON 23 (2015) — his first project working with microcontrollers, with help from someone else on the board layout. It centers on a six-digit 7-segment display, a microphone, two buttons, and a tilt sensor, and defaults to a shot counter that increments whenever the mic picks up a noise past a configurable threshold (claps work as a stand-in when a badge isn't at the range). Other modes include a shot timer that records the interval between each detected shot, a count up/down mode, a random-segment display mode, an audio-debug mode for tuning the microphone threshold, and a "hype" mode that just scrolls "Defcon Shoot" for badge-curious passersby.

Beyond the shooting-focused modes, the badge also hides a small games submenu (a reaction-time game and a "dodge" game among them) and lets the wearer adjust brightness, refresh speed, and whether the tilt sensor flips the display right-side-up when worn backwards. It sold for $25 and came with a glow-in-the-dark lanyard. The firmware (a PIC microcontroller build) is published on GitHub under GPL-2.0, though no schematic or PCB files accompany it — only the code and a short manual in the README.

Seeess went on to make several other badges for later DEF CONs (an AI 6th Finger Ring and TOR-themed badges for DC32, and Tipsy Badges for DC33/DC34 with "gigs"), suggesting the DEF CON Shoot badge was an early entry in a recurring badge-making habit rather than a one-off.
