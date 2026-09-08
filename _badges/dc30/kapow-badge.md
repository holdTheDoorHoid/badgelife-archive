---
title: KAPOW! Badge
id: dc30-kapow-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: SE Community (Social Engineering Community)
summary: 'A beginner soldering-kit badge shaped like a comic-book "KAPOW!" burst, with 11 color-changing LEDs.'
functions: 'Solder-your-own kit: 11 through-hole color-changing LEDs light up when the on/off switch is closed, powered by a 3xAA pack. No resistors needed, aimed at first-time solderers.'
look:
  colors:
  - gold
  - red
  shape: comic burst
  themes:
  - pop culture
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 11
    type: discrete
    note: 'Color-changing LEDs with built-in controllers; no current-limiting resistors required.'
  display: none
  connectivity: []
  battery: 3x AA (4.5V)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Listed as retired on Tindie, checked 2026-09-08; maker states no plans for future production.'
  distribution:
  - purchase
  - kit
  where: 'Sold on Tindie by SE Community as "extras from our village," with proceeds funding the Social Engineering Community''s operations.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/secommunity/kapow-badge-from-secdef-con-30-limited-supply
  url: https://www.tindie.com/products/secommunity/kapow-badge-from-secdef-con-30-limited-supply/
  kind: store
- label: 'KAPOW badge soldering instructions | SEC @ DEF CON 30'
  url: https://www.youtube.com/watch?v=VyGbYZsfJvg
  kind: video
images:
- file: assets/images/badges/dc30/kapow-badge/63d6e50ca2.jpg
  source: "https://www.tindie.com/products/secommunity/kapow-badge-from-secdef-con-30-limited-supply/"
  credit: "SE Community"
  caption: "Assembled KAPOW! Badge with LEDs illuminated"
contact: {}
notes:
- Beginner soldering-kit badge with 11 color-changing LEDs, made for the Heroes vs. Villains youth challenge at DEF CON 30's Social Engineering Community village. Found by the event-year sweep, task dc30-saos.
- 'Sheet listed no title variant; Tindie calls it "KAPOW! Badge from SEC@DEF CON 30."'
status: listed
sources:
- kind: url
  url: https://www.tindie.com/products/secommunity/kapow-badge-from-secdef-con-30-limited-supply/
  title: KAPOW! Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc30-saos); event read as ''dc30''.'
- kind: url
  url: https://www.tindie.com/products/secommunity/kapow-badge-from-secdef-con-30-limited-supply/
  title: KAPOW! Badge from SEC@DEF CON 30 - LIMITED SUPPLY - Tindie
  accessed: '2026-09-08'
  note: 'Primary source: description, BOM (11 LEDs, 3xAA battery pack, switch, no resistors), event/year, retired/sold-out status, and product photos.'
- kind: url
  url: https://www.youtube.com/watch?v=VyGbYZsfJvg
  title: KAPOW badge soldering instructions | SEC @ DEF CON 30
  accessed: '2026-09-08'
  note: 'Confirms the badge as the SE Community Youth Challenge KAPOW badge; assembly walkthrough, no new technical specs beyond the Tindie listing.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'No MCU, no maker page beyond the Tindie storefront and a YouTube assembly video were found. Exact quantity made and unit price are not stated anywhere found; PCB shape and colors are read from the product photo, not stated in text. No design files (KiCad/Gerbers) were located, so make_your_own is left null rather than guessed.'
last_modified_date: '2026-09-08'
---

The KAPOW! Badge is a beginner-friendly soldering kit made by the Social Engineering Community (SEC) for the "Heroes vs. Villains" youth challenge in their village at DEF CON 30 (2022). The PCB is cut into the shape of a comic-book "KAPOW!" explosion burst, finished in gold with a red starburst graphic, and comes with 11 through-hole LEDs that change color on their own, a 3xAA battery pack, and a slide switch — deliberately simple, with no resistors to solder, so kids aged 10-17 could assemble it themselves. SEC posted a YouTube walkthrough of the build alongside the kit.

Leftover kits from the village were later sold on Tindie as a fundraiser for the community's ongoing costs. As of this check the Tindie listing is marked retired with no plans for another run, so it is effectively sold out; no price, print quantity, or design files were published anywhere found.


