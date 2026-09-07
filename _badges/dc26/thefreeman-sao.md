---
title: THE_FREEMAN SAO
id: dc26-thefreeman-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: Twinkle Twinkie
  url: https://hackaday.io/twinkletwinkie
summary: A Shitty Add-On (SAO) version of THE_FREEMAN, TwinkleTwinkie's Vortigaunt-head (Half-Life 2) indie badge made for DEF CON 26; a smaller through-board-lit PCB with a 2x2 SAO v1 header. KiCad/Gerber files are posted on the project page.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - sci-fi
  - security
tech:
  mcu: none
  leds: null
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
  open_source: yes
  hardware_url: https://hackaday.io/project/158663/files
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  kind: hackaday
- label: hackaday.io/project/158663/files
  url: https://hackaday.io/project/158663/files
  kind: hackaday
images:
- file: assets/images/badges/dc26/thefreeman-sao/312168004e.jpg
  source: "https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge"
  credit: "Twinkle Twinkie"
  caption: "THEFREEMAN Vortigaunt badge project photo (full badge shown; SAO is the smaller version of this design)"
contact: {}
notes:
- The sheet/intake listed no year; the project page confirms DEF CON 26 (2018), matching the entry's existing event assignment.
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  title: THEFREEMAN - DEF CON 26 INDIE BADGE
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  title: THEFREEMAN - DEF CON 26 INDIE BADGE
  accessed: '2026-09-07'
  note: "Confirmed maker (TwinkleTwinkie), event/year (DEF CON 26, 2018), that the full badge uses 3 OSRAM red + 2 OSRAM orange SMD LEDs and a CR2032, and that a separate SAO KiCad/Gerber archive (THE_FREEMAN_SAO_hackaday.zip) is posted alongside the full badge files."
- kind: url
  url: https://hackaday.io/project/158663/files
  title: THEFREEMAN - DEF CON 26 INDIE BADGE - Files
  accessed: '2026-09-07'
  note: "Lists two downloads: THE_FREEMAN_Badge_hackaday.zip (badge KiCad & Gerber) and THE_FREEMAN_SAO_hackaday.zip (SAO KiCad & Gerber), both posted 2018-09-10."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    The project page documents the full THE_FREEMAN badge in detail (5 OSRAM
    LEDs shining through the board to light the Vortigaunt's eyes, CR2032
    power, ~40 units of the full badge made) but gives no separate write-up
    for the SAO variant beyond noting its existence and posting its own
    KiCad/Gerber archive. Because the LED count/type, power source, quantity
    made, price, and availability given on the page describe the full badge
    and are not confirmed to be identical for the smaller SAO board, those
    tech/get_one fields are left empty rather than assumed. No storefront,
    press coverage, or additional photos of the SAO specifically were found
    (web search quota was exhausted before broader searches for press/photos
    could be run). sao_version is set to v1 (4-pin) as stated in the sheet's
    original summary; the project page itself does not restate the header
    pin count.
last_modified_date: '2026-09-07'
---

THE_FREEMAN SAO is a Shitty Add-On companion to TwinkleTwinkie's THE_FREEMAN, an indie badge made for DEF CON 26 (2018) styled after the Vortigaunt aliens from Valve's *Half-Life 2*. The full-size badge is a single-layer PCB where the artwork itself does double duty as the circuit: OSRAM SMD LEDs mounted on the back shine through the board to light up the Vortigaunt's eyes, powered by a CR2032 cell, with around 40 units produced for the con. The SAO is a smaller version of the same board, sized to plug into a badge's 2x2 SAO v1 header rather than being worn on its own.

TwinkleTwinkie published both variants' design files together on the Hackaday.io project page: a KiCad/Gerber archive for the full badge and a separate one for the SAO. Beyond confirming that the SAO exists and sharing its own set of design files, the project page does not give a separate technical write-up, price, or production count for the SAO specifically, so those details are left blank here pending a source that documents the SAO on its own.

## Make your own

KiCad and Gerber files for the SAO are bundled as `THE_FREEMAN_SAO_hackaday.zip` on the project's Files tab (https://hackaday.io/project/158663/files), alongside the separate `THE_FREEMAN_Badge_hackaday.zip` for the full-size badge.
