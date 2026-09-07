---
title: Samurai CTF Badge
id: dc26-samurai-ctf-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Silas Cutler
  url: https://hackaday.io/silas-cutler
summary: A circular independent badge made for DEF CON 26 (2018), cut with the Japanese kanji for "samurai" (侍) and built on RGB-LED electronics reused from an earlier MassHackers badge design.
functions: Programmable RGB LED color rotation and fade effects along two LED strips, with a button to switch between lighting modes. No CTF/game logic of its own beyond the "CTF" in its name; the electronics were adapted from a Massachusetts hacker meetup badge.
look:
  colors:
  - black
  - white
  shape: circle
  themes:
  - ctf
  - text
  - security
tech:
  mcu: Teensy 2.0
  leds:
    count: 6
    type: RGB
    note: Two strips of surface-mount RGB LEDs along the badge edge, driven with the SoftPWM library for smooth color fades; inherited from the MassHackers 2015 badge base design.
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Made by Silas Cutler ("Team Samurai") as a personal DEF CON 26 badge build; no evidence it was sold or widely distributed.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/TheDukeZip/MassHackersBadge2015
  firmware_url: https://github.com/TheDukeZip/MassHackersBadge2015
  eda_tool: Eagle
links:
- label: hackaday.io/project/160469-samurai-ctf-badge
  url: https://hackaday.io/project/160469-samurai-ctf-badge
  kind: hackaday
- label: TheDukeZip/MassHackersBadge2015 (base electronics)
  url: https://github.com/TheDukeZip/MassHackersBadge2015
  kind: repo
images:
- file: assets/images/badges/dc26/samurai-ctf-badge/644fb006a1.jpg
  source: https://hackaday.io/project/160469-samurai-ctf-badge
  credit: Silas Cutler
  caption: Samurai CTF Badge - circular PCB with Japanese kanji for samurai (侍), LED strips, and carabiner clip
- file: assets/images/badges/dc26/samurai-ctf-badge/686cb38043.jpg
  source: https://hackaday.io/project/160469-samurai-ctf-badge
  credit: Silas Cutler
  caption: Underside of the Samurai CTF Badge showing component placement and LED strips
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/160469-samurai-ctf-badge
  title: Samurai CTF Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/160469-samurai-ctf-badge
  title: Samurai CTF Badge - project page
  accessed: '2026-09-07'
  note: Confirmed maker Silas Cutler, event DEF CON 26 (2018), that it reuses TheDukeZip/MassHackers electronics, and pulled the two gallery photos of the badge.
- kind: url
  url: https://github.com/TheDukeZip/MassHackersBadge2015
  title: TheDukeZip/MassHackersBadge2015
  accessed: '2026-09-07'
  note: 'Source repo for the underlying electronics: Teensy 2.0 modified to 3.3V/8MHz, 6 RGB LEDs with SoftPWM fades, Eagle CAD design files and Gerbers.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The Hackaday.io project page (created Aug 2018) is Silas Cutler''s own write-up describing it as his "first proper DEFCON badge build," made by "Team Samurai," and states the badge electronics were derived from TheDukeZip''s MassHackers badge on GitHub (confirmed: Teensy 2.0-based, 6 RGB LEDs). No price, quantity, or distribution details were found; this reads as a personal/one-off build rather than a sold product, so get_one fields are left mostly empty. No design files specific to the Samurai badge itself (as opposed to the reused MassHackers base) were found.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/samurai-ctf-badge/
model:
  file: assets/models/dc26/samurai-ctf-badge.glb
  method: kicad
  source_file: MassHackersBadge2015.brd
  generated: '2026-09-07'
  bytes: 116100
---

The Samurai CTF Badge is an independent hardware badge made by Silas Cutler for DEF CON 26 in 2018, under the name "Team Samurai." It is a circular black PCB cut through with the Japanese kanji for "samurai" (侍) in white silkscreen, worn on a carabiner clip. Cutler describes it on Hackaday.io as his first full DEF CON badge build.

Rather than designing the electronics from scratch, the badge reuses the circuit from TheDukeZip's 2015 MassHackers badge: a Teensy 2.0 microcontroller modified to run at 3.3V and 8MHz for power efficiency, driving two edge-mounted strips of RGB LEDs (six total) through the SoftPWM library for smooth color-fade effects, with a button to cycle lighting modes. The MassHackers design was published in Eagle CAD with full schematics, PCB layout, and Gerber files, though those files describe the donor electronics rather than the samurai-shaped board itself.

No pricing, production quantity, or distribution information was found; the project appears to have been a personal build rather than a badge sold or given away at scale.
