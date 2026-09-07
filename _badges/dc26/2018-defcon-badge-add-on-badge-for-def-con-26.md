---
title: 2018_defcon_badge — Add-on badge for DEF CON 26
id: dc26-2018-defcon-badge-add-on-badge-for-def-con-26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: HexaKhan
  url: https://github.com/HexaKhan
  role: firmware
- name: BK
  role: PCB design and electronics
summary: A DEF CON 26 Shitty Add-On nicknamed "hacker roulette" — five LEDs chase around a ring, slowing down after a button press until they land on a winning light.
functions: 'Roulette-style LED chase game: holding/releasing the button starts a light spinning around five LEDs; the spin gradually slows and stops on one LED as the "winner," with a flash sequence and an optional bonus "fun mode."'
look:
  colors: []
  shape: null
  themes:
  - game
  - ctf
tech:
  mcu: ATtiny25
  leds:
    count: 5
    type: discrete
    note: Five discrete LEDs driven directly from ATtiny I/O pins (PB0-PB4), wired to VCC so the firmware drives them active-low.
  display: none
  connectivity: []
  battery: null
  sao_version: v1
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
  firmware_url: https://github.com/HexaKhan/2018_defcon_badge/blob/master/badgeCode.c
  eda_tool: null
links:
- label: github.com/HexaKhan/2018_defcon_badge
  url: https://github.com/HexaKhan/2018_defcon_badge
  kind: repo
- label: 'DEF CON 26 Shitty Add-Ons (Hackaday.io project)'
  url: https://hackaday.io/project/52950-defcon-26-shitty-add-ons
  kind: hackaday
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/HexaKhan/2018_defcon_badge
  title: 2018_defcon_badge — Add-on badge for DEF CON 26
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 26''.'
- kind: url
  url: https://raw.githubusercontent.com/HexaKhan/2018_defcon_badge/master/README.md
  title: 'HexaKhan/2018_defcon_badge README'
  accessed: '2026-09-07'
  note: 'Confirms it is a DEF CON 26 Shitty Add-On, "hacker roulette", made by HexaKhan (code) and BK (board + electronics); ATtiny25-20SSU running at 1MHz/3.3V; links to the DEF CON 26 SAO Hackaday.io project.'
- kind: url
  url: https://raw.githubusercontent.com/HexaKhan/2018_defcon_badge/master/badgeCode.c
  title: 'HexaKhan/2018_defcon_badge badgeCode.c'
  accessed: '2026-09-07'
  note: 'Confirms 5 LEDs on PB0-PB4 (active-low, wired to VCC), a button on PB5, and the roulette/spin-and-slow-down game logic including a "fun mode."'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Repo publishes only firmware source (badgeCode.c), a precompiled .hex, and a wiring/programming diagram (ATTINY25_Programming.png, not a photo of the finished board or PCB files) — no schematic/Gerbers/EDA source, so open_source is "partial" and hardware_url/gerbers_url are left empty. No price, quantity, or distribution details found anywhere in the repo. No photo of the assembled badge was found, so images is empty. Could not run additional web searches (session search budget exhausted) to check for press coverage or a maker profile beyond the linked DEF CON 26 SAO Hackaday.io project page.'
last_modified_date: '2026-09-07'
---

This is a DEF CON 26 (2018) Shitty Add-On built as a two-person effort: BK designed the PCB and electronics, and HexaKhan wrote the firmware. The badge is a small "hacker roulette" game — five LEDs are arranged so a light appears to spin around them, and pressing and releasing the button starts and stops the spin. The light gradually slows after release until it settles on one LED as the winner, complete with a short flash sequence, and the firmware includes an optional "fun mode" variant of the game.

Under the hood it runs on an ATtiny25-20SSU clocked at 1 MHz (also tested on an ATtiny85-20PU), with the five LEDs driven directly from I/O pins PB0-PB4 and the button read on PB5. The reset pin is disabled via fuse bits so it can double as the button input, which means reflashing it later requires a high-voltage serial programmer (the maker recommends the HV Rescue Shield) rather than a standard ISP.

## Make your own

The GitHub repo publishes the firmware source (`badgeCode.c`), a Makefile, and a precompiled `2018_defcon_badge.hex`, along with a README walking through flashing both the program and the fuse bits with avrdude via an Arduino-as-ISP. No PCB schematic, layout, or Gerber files are included, so the hardware side of the project is not reproducible from the repo alone — only the firmware is open.
