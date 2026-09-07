---
title: Space Girl sweet looking PCB pin
id: dc30-space-girl-sweet-looking-pcb-pin
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc30
year: 2022
makers:
- name: Steph Piper (Elkei Education)
  url: https://makerqueen.com.au
summary: A beginner soldering-project badge shaped like a cartoon space girl, with a stained-glass-style PCB and two blinking LED eyes, sold by Steph Piper's Maker Queen through Adafruit.
functions: 'Solder-it-yourself kit: two LEDs light up when the on/off switch is closed, powered by a coin cell.'
look:
  colors:
  - purple
  - blue
  - silver
  shape: null
  themes:
  - space
  - jewelry
  - pin
  - learn to solder
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Through-hole LEDs act as the character's eyes; not addressable/RGB.
  display: none
  connectivity: []
  battery: CR2032 (sold separately)
  sao_version: none
get_one:
  price: $9.95
  price_usd: 9.95
  quantity: ''
  availability: available
  availability_note: 'Listed in stock (17 units) on adafruit.com/product/5495 as of 2026-09-06.'
  distribution:
  - purchase
  where: Adafruit (adafruit.com/product/5495)
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.adafruit.com/product/5495
  url: https://www.adafruit.com/product/5495
  kind: store
- label: Maker Queen (Steph Piper)
  url: https://makerqueen.com.au
  kind: website
images:
- file: assets/images/badges/dc30/space-girl-sweet-looking-pcb-pin/b7a7201578.jpg
  source: "https://www.adafruit.com/product/5495"
  credit: "Maker Queen / Adafruit"
  caption: "Space Girl PCB soldering badge, front view"
- file: assets/images/badges/dc30/space-girl-sweet-looking-pcb-pin/0bdc2180d3.jpg
  source: "https://www.adafruit.com/product/5495"
  credit: "Maker Queen / Adafruit"
  caption: "Space Girl PCB soldering badge, lit up"
contact: {}
notes:
- Outstanding art! Even though a pin, it deserves a spot here
- 'Sister item on the same maker''s line: dc30-biology-girl-sweet-looking-pcb-pin (Biology Girl), also sold via Adafruit.'
status: released
sources:
- kind: sheet
  event: dc30
  row: 50
  updated: '2022-07-09'
- kind: url
  url: https://www.adafruit.com/product/5495
  title: "Space Girl Badge Soldering Kit by Maker Queen - PRODUCT ID: 5495 - Adafruit Industries"
  accessed: '2026-09-06'
  note: Confirmed price, in-stock quantity, PCB colors, LED/battery/switch details, product images, and that it won a 2019 ROAR! Award.
- kind: url
  url: https://makerqueen.com.au
  title: Maker Queen — Steph Piper
  accessed: '2026-09-06'
  note: Confirmed Steph Piper is the maker behind Maker Queen (no direct mention of the Space Girl badge or DEF CON on the site itself).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Storefront (Adafruit) fully describes the physical badge, price, and stock. Could not find a maker page, Hackaday.io project, or press coverage tying it specifically to DEF CON 30, nor any hardware/firmware files — treated as closed/unpublished (open_source left null rather than guessed "no"). Could not reach learn.adafruit.com guide page (404) for build-guide detail. It is a passive soldering kit, not an SAO or powered "badge" in the con-badge sense, so type is set to accessory/pin-like wearable rather than badge; look.shape left null since sources describe the art (stained-glass space girl) but not a simple named silhouette.'
last_modified_date: '2026-09-06'
---

The Space Girl badge is a beginner soldering kit designed by Steph Piper of Maker Queen (an Australian maker/edutech company also credited on the community sheet as Elkei Education). It is a small custom PCB shaped and colored like a stained-glass illustration of a cartoon girl in a space helmet, rendered in jewel-tone purple, blue, and silver soldermask. Builders solder on two LEDs (the character's eyes), an on/off switch, and a coin-cell battery holder, then wear the finished piece as a pin using an attached badge clasp — no microcontroller or SAO connector involved.

It was sold through Adafruit (product #5495) at $9.95, with a CR2032 battery available separately, and the design previously won a 2019 ROAR! Award for Best Teen/Tween Product. The community sheet lists it as brought to DEF CON 30 in 2022; no DEF CON-specific writeup or hardware/firmware release was found, so distribution and any give-away/sale details specific to the con are not confirmed beyond the general Adafruit listing.
