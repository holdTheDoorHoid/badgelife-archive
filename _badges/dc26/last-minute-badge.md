---
title: DC26 Last Minute Badge
id: dc26-last-minute-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: xres0nance
  url: https://hackaday.io/xres0nance
summary: 'A hybrid analog-digital badge built from a 1" CRT camcorder viewfinder wired to an analog CCTV camera board, made in three days for DEF CON 26''s "1983: On the Edge of Dystopia" theme.'
functions: 'Displays a live analog video feed from a small CCTV camera on a miniature CRT screen; a separate ATtiny13-based module ("Secret Signaller") blinks a message in Morse code, either as a hard on/off or a smooth PWM fade.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
  - security
tech:
  mcu: ATtiny13
  leds: null
  display: 1" CRT (camcorder viewfinder)
  connectivity: []
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
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/aaronkondziela/DC26
  eda_tool: null
  license: CC0
  notes: 'The GitHub repo (by aaronkondziela) holds only the Morse-code "Secret Signaller" ATtiny13 firmware, described as "one component of several" of the full badge; no PCB/hardware files for the CRT/camera assembly were found.'
links:
- label: hackaday.io/project/160191-dc26-last-minute-badge
  url: https://hackaday.io/project/160191-dc26-last-minute-badge
  kind: hackaday
- label: github.com/aaronkondziela/DC26
  url: https://github.com/aaronkondziela/DC26
  kind: repo
images:
- file: assets/images/badges/dc26/last-minute-badge/31ffdac879.jpg
  source: "https://hackaday.io/project/160191-dc26-last-minute-badge"
  credit: "xres0nance"
  caption: "The DC26 Last Minute Badge, a hybrid analog CRT viewfinder camera badge"
- file: assets/images/badges/dc26/last-minute-badge/98628ee772.jpg
  source: "https://hackaday.io/project/160191-dc26-last-minute-badge"
  credit: "xres0nance"
  caption: "Assembled badge showing the CRT viewfinder and PCB"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/160191-dc26-last-minute-badge
  title: DC26 Last Minute Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''DEF CON 26''.'
- kind: url
  url: https://hackaday.io/project/160191-dc26-last-minute-badge
  title: DC26 Last-Minute Badge project log
  accessed: '2026-09-07'
  note: 'Confirmed maker (xres0nance), event/date (DEF CON 26, Aug 2018, "1983" theme), CRT/CCTV camera hardware, ATtiny13 Morse module, and GitHub link.'
- kind: url
  url: https://github.com/aaronkondziela/DC26
  title: aaronkondziela/DC26 - Secret Signaller
  accessed: '2026-09-07'
  note: 'Confirms ATtiny13 Arduino-ISP firmware for a Morse-code blinker, CC0 license, and that it is only one component of the full badge (no hardware files present).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Built for DEF CON 26 (Aug 2018) as a fast, improvised project ("Why build badges in a year, when you can do it in three days?"). No price, quantity made, or distribution details were found anywhere in the project logs or repo. No PCB/hardware design files were located; only the small Morse-code firmware module is open source. Maker''s real name may be Aaron Kondziela per the GitHub account, but this was not independently confirmed on the Hackaday profile, so makers.name is kept as the Hackaday handle xres0nance.'
last_modified_date: '2026-09-07'
---

The DC26 Last Minute Badge is a scrappy, hybrid analog-digital badge built by Hackaday.io user xres0nance for DEF CON 26 in August 2018, whose theme that year was "1983: On the Edge of Dystopia." True to its name, the maker describes building it in about three days rather than the usual year-long badge development cycle. Rather than a typical microcontroller-driven PCB badge, it centers on a 1" CRT viewfinder salvaged from a vintage camcorder, wired to a small analog CCTV camera board so the wearer displays a live grainy black-and-white video feed on a tiny glowing tube.

A separate, simpler module rounds out the badge: an ATtiny13 microcontroller (programmed via Arduino-as-ISP with the MicroCore bootloader) blinks out a message in Morse code, either as sharp on/off flashes or a smoother PWM fade. That firmware, released under CC0 and titled "Secret Signaller" on GitHub, is described by the maker as just one component of the larger badge system, and no hardware files, PCB designs, or Gerbers for the CRT/camera portion were found published anywhere. No information turned up on price, quantity made, or how (or whether) it was distributed beyond the maker's own use.
