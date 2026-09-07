---
title: The Child SAO
id: other-the-child-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2021
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/hacker/308303-twinkletwinkie
summary: A Grogu (The Child from The Mandalorian) themed Simple Add-On on a four-layer PCB that uses four 0807 random-flashing RGB LEDs to light up the area behind the character.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - tv
  - pop culture
  - sci-fi
tech:
  mcu: none
  leds:
    count: 4
    type: RGB
    note: 0807 package, random-flashing (self-contained blinking RGB LEDs, no driver chip)
  display: null
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
  hardware_url: https://hackaday.io/project/186283-the-child-sao
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/186283-the-child-sao
  url: https://hackaday.io/project/186283-the-child-sao
  kind: hackaday
- label: hackaday.io/twinkletwinkie
  url: https://hackaday.io/twinkletwinkie
  kind: hackaday
images:
  - file: assets/images/badges/other/the-child-sao/43f74c0334.jpg
    source: "https://hackaday.io/project/186283-the-child-sao"
    credit: "TwinkleTwinkie"
    caption: "The Child SAO, front view"
  - file: assets/images/badges/other/the-child-sao/6521929861.jpg
    source: "https://hackaday.io/project/186283-the-child-sao"
    credit: "TwinkleTwinkie"
    caption: "The Child SAO, lit up"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/186283-the-child-sao
  title: The Child SAO | Hackaday.io
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/186283-the-child-sao
  title: The Child SAO | Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed description ("Uses 4 0807 Random Flashing RGBs to light up the area behind Grogu"), 4-layer PCB, design file TheChild_4L_2021-06-10-2138.zip, project logged 2022-07-08, and pulled gallery photos.
- kind: url
  url: https://hackaday.io/twinkletwinkie
  title: TwinkleTwinkie | Hackaday.io
  accessed: '2026-09-07'
  note: Maker profile; confirmed TwinkleTwinkie as the creator and their pattern of badgelife/SAO/shitty-add-on projects, but the profile does not separately list an event/year for this item.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    The Hackaday.io project page and the maker's profile do not name a specific
    convention this SAO was made for or sold at, so event is left as other. The
    downloadable design file is dated 2021-06-10 (matching the entry's existing
    year of 2021) but the project itself was posted/logged 2022-07-08; no price,
    quantity made, or distribution channel is stated anywhere in the sources
    found. Hardware design files (a 4-layer KiCad/Gerber-style zip) are published
    on the project page, but no firmware is applicable (LEDs are self-flashing,
    no MCU) and no separate firmware repo was found, so open_source is marked
    partial rather than yes.
last_modified_date: '2026-09-07'
---

The Child SAO is a Simple Add-On by TwinkleTwinkie depicting Grogu, the character widely known as "Baby Yoda" from The Mandalorian. The board is a four-layer PCB, and its lighting comes from four 0807-package RGB LEDs that flash in a random pattern to illuminate the area behind the character artwork — the LEDs are self-contained blinkers rather than being driven by a microcontroller, so the SAO has no onboard MCU.

TwinkleTwinkie is a prolific badgelife creator on Hackaday.io, known for a series of DEF CON "shitty add-ons" (Mad Cat, Fat Pika, Big Green) and other SAOs and badges. The Child SAO's project page does not name a specific convention it was built for or sold at, and the design files bundle (dated June 2021) predates the project's Hackaday.io posting in July 2022, so it is unclear whether it debuted at a particular event or was released independently. Hardware design files are published on the project page for anyone who wants to reproduce the board; no information on price, production quantity, or how it was distributed was found.
