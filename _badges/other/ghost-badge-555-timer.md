---
title: Ghost Badge made from 555 Timer IC
id: other-ghost-badge-555-timer
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2021
makers:
- name: Arnov Sharma
  url: https://www.pcbway.com/project/member/?bmbno=068786DB-1EF6-44
summary: Bedsheet-ghost-shaped PCB badge (white soldermask, black silkscreen) whose two 3mm LED eyes are flashed by an astable 555 timer bi-flasher, built entirely from through-hole parts and powered by a CR2032 coin cell or 5V USB, released as a Halloween 2021 soldering-challenge kit.
functions: Two 3mm LEDs (the ghost's eyes) blink in an alternating bi-flasher pattern driven by a 555 timer in astable mode; no microcontroller or firmware involved.
look:
  colors:
  - white
  - black
  shape: ghost
  themes:
  - horror
  - halloween
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 3mm LEDs used as the ghost's eyes, driven directly by the 555 timer's output pin in an alternating bi-flasher circuit.
  display: none
  connectivity: []
  battery: CR2032 or 5V USB (micro USB)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  - kit
  where: Sold as a soldering kit on Tindie (MakerPals store, "Halloween Ghost Badge 2021"); design also shared publicly on PCBWay and documented step-by-step on Instructables and Hackster.
make_your_own:
  open_source: true
  hardware_url: https://www.instructables.com/Yet-Another-Badge-a-Ghost-Badge-Made-From-555-Time/
  firmware_url: null
  eda_tool: null
  gerbers_url: https://www.pcbway.com/project/shareproject/Ghost_Badge_made_from_555_Timer_IC.html
  license: CC BY-SA
  fab_url: https://www.pcbway.com/project/shareproject/Ghost_Badge_made_from_555_Timer_IC.html
  notes: 'PCB designed in OrCAD Cadence; Gerbers shared via PCBWay''s shared-project page under Creative Commons Attribution-ShareAlike. Bill of materials: 555 timer IC, 68K and 1K resistors, 1uF capacitor, micro USB port, SR206 diode, CR2032 coin cell holder, two 3mm LEDs — all through-hole.'
links:
- label: www.pcbway.com/project/shareproject/Ghost_Badge_made_from_555_Timer_IC.html
  url: https://www.pcbway.com/project/shareproject/Ghost_Badge_made_from_555_Timer_IC.html
  kind: fab
- label: www.instructables.com/Yet-Another-Badge-a-Ghost-Badge-Made-From-555-Time
  url: https://www.instructables.com/Yet-Another-Badge-a-Ghost-Badge-Made-From-555-Time/
  kind: website
- label: www.hackster.io/418992/yet-another-badge-a-ghost-badge-made-from-555-timer-ic-92dfbf
  url: https://www.hackster.io/418992/yet-another-badge-a-ghost-badge-made-from-555-timer-ic-92dfbf
  kind: article
  archived: https://web.archive.org/web/20260508014023/https://www.hackster.io/418992/yet-another-badge-a-ghost-badge-made-from-555-timer-ic-92dfbf
- label: www.tindie.com/products/makerpals/halloween-ghost-badge-2021
  url: https://www.tindie.com/products/makerpals/halloween-ghost-badge-2021/
  kind: store
images:
- file: assets/images/badges/other/ghost-badge-555-timer/3a8b152eee.png
  source: https://www.pcbway.com/project/shareproject/Ghost_Badge_made_from_555_Timer_IC.html
  credit: Arnov Sharma
  caption: Assembled ghost-shaped badge with white soldermask and glowing LED eyes
- file: assets/images/badges/other/ghost-badge-555-timer/729fe9e638.jpg
  source: https://www.instructables.com/Yet-Another-Badge-a-Ghost-Badge-Made-From-555-Time/
  credit: Arnov Sharma
  caption: Ghost badge PCB, front view showing bedsheet-ghost silkscreen outline
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://www.pcbway.com/project/shareproject/Ghost_Badge_made_from_555_Timer_IC.html
  title: Ghost Badge made from 555 Timer IC - Share Project - PCBWay
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://www.instructables.com/Yet-Another-Badge-a-Ghost-Badge-Made-From-555-Time/
  title: 'Yet Another Badge, a Ghost Badge Made From 555 Timer IC : 11 Steps - Instructables'
  accessed: '2026-09-07'
  note: Maker's own step-by-step build log; confirmed design process (OrCAD Cadence), BOM, assembly steps, CC BY-SA license, and provided project photos.
- kind: url
  url: https://www.hackster.io/418992/yet-another-badge-a-ghost-badge-made-from-555-timer-ic-92dfbf
  title: Yet Another Badge, a Ghost Badge Made From 555 Timer IC - Hackster.io
  accessed: '2026-09-07'
  note: Mirror of the same project; page returned HTTP 403 to automated fetch so content could not be directly reviewed, but title/URL confirm it as a duplicate listing of the same badge.
  archived: https://web.archive.org/web/20260508014023/https://www.hackster.io/418992/yet-another-badge-a-ghost-badge-made-from-555-timer-ic-92dfbf
- kind: url
  url: https://www.tindie.com/products/makerpals/halloween-ghost-badge-2021/
  title: Halloween Ghost Badge 2021 - MakerPals - Tindie
  accessed: '2026-09-07'
  note: Storefront listing for the assembled/kit version, sold under the MakerPals store name. Page is behind a Cloudflare bot check so price and stock count could not be confirmed directly; a web search snippet describes it as a soldering-challenge kit (solder it, insert a coin cell, switch on, LEDs blink in a loop) and notes the MakerPals store was, as of the search date, listed as on a break.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (maker, design, BOM, power options, license) confirmed from the maker's own Instructables build log and PCBWay share page. Price, quantity made, and current stock/availability on Tindie could not be confirmed — the Tindie listing is blocked by a Cloudflare challenge to automated fetches. This is a Halloween-season release, not tied to any specific hacker convention, so it is kept under the "other" event bucket; no event id in _data/events.yml matches a general Halloween/seasonal release.
last_modified_date: '2026-09-07'
---

Arnov Sharma designed this Ghost Badge in August 2021 as a Halloween-themed, beginner-friendly soldering kit. The PCB traces the outline of a classic bedsheet ghost, laid out in white soldermask with black silkscreen, and uses only through-hole parts: a 555 timer IC wired as an astable bi-flasher drives two 3mm LEDs mounted as the ghost's eyes, alternating them on and off with no microcontroller or firmware involved. The board can run from a CR2032 coin cell or from 5V over a micro USB connector, so it works either as a wearable badge or a small desk decoration.

The design was drawn up in OrCAD Cadence and manufactured through PCBWay, whose shared-project page hosts the Gerber files under a Creative Commons Attribution-ShareAlike license. Sharma documented the full build — schematic, PCB layout (including embedding a bitmap of the ghost artwork into the silkscreen), soldering, and a fix for a missed pin-4-to-pin-8 connection on the first prototype — in an 11-step Instructables guide, which was also mirrored on Hackster.io. The assembled badge (or a kit version of it) was later sold through the MakerPals store on Tindie as the "Halloween Ghost Badge 2021."

## Make your own

The project is fully open: Gerbers are on PCBWay's shared-project page and the Instructables guide walks through schematic design, PCB layout, and assembly. The bill of materials is small and entirely through-hole — a 555 timer IC, 68K and 1K resistors, a 1uF capacitor, an SR206 diode, a micro USB port, a CR2032 coin cell holder, and two 3mm LEDs — making it a reasonable first soldering project.
