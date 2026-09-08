---
title: DC858/619 Unofficial DEF CON Badge ("Beach Day Badge")
id: dc26-dc858-619-unofficial-def-con-badge-beach-day-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: phelgon (El Cajon, CA)
summary: An unofficial, palm-tree-themed DEF CON badge from the DC858/619 (San Diego) DEF CON group, packed with novelty features including a faux breathalyzer and a TV-B-Gone.
functions: Cycles through modes via the d-pad's left/right buttons — a TV-B-Gone mode that steps through roughly 135 common TV "off" codes, and an MQ303-based "breathalyzer" mode that heats up for five seconds and displays a raw sensor resistance reading rather than an actual BAC value. Also has RGB LED lighting patterns and SAO expansion.
look:
  colors: []
  shape: null
  themes:
  - beach
  - drink
  - security
tech:
  mcu: Cypress PSoC
  leds: null
  display: 0.96" 128x64 LCD (dual-color)
  connectivity:
  - ir
  battery: 2x AA
  sao_version: null
get_one:
  price: $80
  price_usd: 80
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold assembled on Tindie by phelgon; also distributed at DEF CON 26 and 27. Tindie listing shows out of stock since 2022-10-21.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ellwoodthewood/DC858_619_Badge
  firmware_url: https://github.com/ellwoodthewood/DC858_619_Badge
  eda_tool: null
links:
- label: www.tindie.com/products/phelgon/dc858619-unofficial-def-con-badge
  url: https://www.tindie.com/products/phelgon/dc858619-unofficial-def-con-badge/
  kind: store
- label: github.com/ellwoodthewood/DC858_619_Badge
  url: https://github.com/ellwoodthewood/DC858_619_Badge
  kind: repo
- label: "hackaday.io/project/160782 - DC858/619 \"Beach Day\" Unofficial DEF CON 26 badge"
  url: https://hackaday.io/project/160782-dc858619-beach-day-unofficial-def-con-26-badge
  kind: hackaday
images:
- file: assets/images/badges/dc26/dc858-619-unofficial-def-con-badge-beach-day-badge/178f498788.jpg
  source: "https://www.tindie.com/products/phelgon/dc858619-unofficial-def-con-badge/"
  credit: "phelgon"
  caption: "The DC858/619 Beach Day Badge, fully assembled"
contact: {}
notes:
- Fully assembled unofficial electronic badge for DEF CON attendees from the DC858/619 (San Diego) DEF CON group, with RGB LEDs, MQ303 breathalyzer, IR TV-B-Gone, 128x64 LCD, and SAO support; design files on GitHub (ellwoodthewood/DC858_619_Badge). Found by the event-year sweep, task con-dc404.
- 'The community sheet read the event as "DC858 2018"; the maker''s Tindie listing confirms it was made for DEF CON 26 (2018), and also sold at DEF CON 27 (2019).'
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/phelgon/dc858619-unofficial-def-con-badge/
  title: DC858/619 Unofficial DEF CON Badge ("Beach Day Badge")
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-dc404); event read as ''DC858 2018''.'
- kind: url
  url: https://github.com/ellwoodthewood/DC858_619_Badge
  title: "GitHub - ellwoodthewood/DC858_619_Badge"
  accessed: '2026-09-08'
  note: Maker's repo confirming firmware/hardware source, TV-B-Gone and breathalyzer mode behavior.
- kind: url
  url: https://hackaday.io/project/160782-dc858619-beach-day-unofficial-def-con-26-badge
  title: DC858/619 "Beach Day" Unofficial DEF CON 26 badge
  accessed: '2026-09-08'
  note: Project page confirming DEF CON 26 / 2018 and listing the design-file set (gerbers, schematic, BOM, firmware archive).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, released item via the maker''s own Tindie store, GitHub repo, and Hackaday.io project page. Note: this entry duplicates dc26-dc858-619-beach-day-badge, an existing entry for the same item. LED count/type not stated anywhere found. A Hackaday.io description guessed the MCU as an ATtiny85 "based on file references," which conflicts with the maker''s own Tindie listing naming a Cypress PSoC; the Tindie (maker''s own) source was preferred and the Hackaday guess was not used. SAO header version not confirmed by any source, though SAO support is mentioned. Quantity made not stated.'
last_modified_date: '2026-09-08'
---

The DC858/619 "Beach Day Badge" is an unofficial electronic badge made by phelgon for the DC858/619 DEF CON group (San Diego) and sold assembled through Tindie starting around DEF CON 26 in 2018, with continued sales through DEF CON 27. It leans into novelty features rather than pure blinky aesthetics: a d-pad cycles between a TV-B-Gone mode that runs through roughly 135 common television power-off codes, and a tongue-in-cheek "breathalyzer" mode built around an MQ303 gas sensor that displays a raw resistance reading after a five-second heat-up rather than a calibrated blood-alcohol figure. The badge also carries RGB LEDs, a 0.96" 128x64 dual-color LCD, runs on 2x AA batteries, and ships with a lanyard.

The badge is built around a Cypress PSoC microcontroller per the maker's own store listing. Hardware and firmware are fully open, with schematics, Gerbers, a bill of materials, and firmware source published on GitHub. The Tindie listing shows the badge sold for $80 and has been marked out of stock since October 2022.

## Make your own

Design files — PCB schematic (PDF), Gerbers, bill of materials (XLSX), and firmware (as a 7z archive) — are published at github.com/ellwoodthewood/DC858_619_Badge.
