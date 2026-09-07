---
title: Brrr
id: dc26-dc26-brrr-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: awkward intelligence
  url: https://hackaday.io/Awkwardai
summary: Ice-cream-cone-with-lightning SAO modelled on Gucci Mane's cheek tattoo as a tribute to Atlanta; a dual-LED flasher built around a BJT transistor and white SMD LEDs to simulate lightning, sold in the maker's DEF CON 26 SAO sets.
functions: dual-LED flasher that blinks to simulate lightning
look:
  colors: []
  shape: null
  themes:
  - food
  - pop culture
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: white SMD LEDs driven by a BJT transistor flasher circuit
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given away as a freebie to people who bought the maker's DEF CON 26 shitty-add-on sets; not sold individually.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  gerbers_url: https://cdn.hackaday.io/files/1599526843386368/brrrfriFRI.zip
  eda_tool: null
links:
- label: hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  kind: hackaday
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- label: hackaday.io/project/159952/files
  url: https://hackaday.io/project/159952/files
  kind: hackaday
  archived: https://web.archive.org/web/20260907115748/https://hackaday.io/project/159952/files
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  title: The Harbinger Shitty Add-on Badges
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- kind: url
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  title: The Harbinger Shitty Add-on Badges
  accessed: '2026-09-07'
  note: Maker's own project description confirms Brrr is a DEF CON 26 (2018) SAO, its design story, the LED flasher circuit, and that it was given free with purchase of the maker's SAO sets rather than sold.
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- kind: url
  url: https://hackaday.io/project/159952/files
  title: The Harbinger Shitty Add-on Badges - Files
  accessed: '2026-09-07'
  note: Lists brrrfriFRI.zip, described as "Brrr Gerbers" (761 KB, uploaded 2018-07-25) - the board's Gerber manufacturing files.
  archived: https://web.archive.org/web/20260907115748/https://hackaday.io/project/159952/files
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's project page and files page confirm the core facts (design story, LED flasher, DEF CON 26/2018, free giveaway, Gerbers available). No schematic or firmware was found, only Gerbers, so open_source is marked partial. Could not find a photo of Brrr itself on the project page distinct from other SAOs in the same multi-item project listing, so no image was saved (guessing which gallery image was Brrr would risk misattribution). Quantity made is not stated anywhere found.
last_modified_date: '2026-09-07'
---

Brrr is a shitty add-on (SAO) by the maker awkward intelligence, made for DEF CON 26 in 2018 as part of their "Harbinger" line of add-ons. The design reworks the ice-cream-cone-with-lightning tattoo on Gucci Mane's cheek into a small PCB, as a tribute to the maker's home city of Atlanta - the project notes it "could work for Brrcon" as a pun on the rapper's association with the city.

Electrically it's simple: a dual-LED flasher built around a BJT transistor driving white SMD LEDs to simulate a lightning flicker, with no microcontroller. It wasn't sold on its own - the maker gave it away as a bonus to anyone who bought one of their DEF CON 26 SAO sets.

## Make your own

The maker shared the board's Gerber files (`brrrfriFRI.zip`) on the Hackaday.io project's files page, so the PCB can be fabricated from those directly. No schematic source or firmware was published alongside them.

