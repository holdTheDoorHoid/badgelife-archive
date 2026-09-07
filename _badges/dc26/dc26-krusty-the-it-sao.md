---
title: Krusty the It
id: dc26-dc26-krusty-the-it-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: Twinkle Twinkie
  url: https://hackaday.io/TwinkleTwinkie
summary: Twinkle Twinkie's first Shitty Add-on, a creepy Pennywise-style clown PCB made for the DEF CON 26 indie badges, with two reverse-mount OSRAM LEDs shining through the board as glowing yellow eyes, a 2x2 SAO header and a 51-ohm resistor; KiCad files and Gerbers are posted and it was sold on Tindie.
functions: 'Decorative only: the two LED eyes light up bright yellow when the SAO is powered from a host badge''s 3.3V SAO header.'
look:
  colors: []
  shape: null
  themes:
  - horror
  - meme
tech:
  mcu: none
  leds:
    count: 2
    type: reverse-mount
    note: Two OSRAM TOPLED SMD LEDs (LY T776-Q2T1-26-Z), wired through a single 51-ohm 0805 resistor, mounted to shine through the PCB as the clown's eyes.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: $20 (1-4 units), $18 each for 5+
  price_usd: 20
  quantity: '140'
  availability: sold_out
  availability_note: Tindie listing shows "Product Retired" / sold out as of 2026-09-07.
  distribution:
  - purchase
  where: Sold assembled on Tindie by Twinkle Twinkie.
make_your_own:
  open_source: true
  hardware_url: https://hackaday.io/project/158664-krusty-the-it
  firmware_url: null
  eda_tool: KiCad
  notes: Raw KiCad project and Gerbers posted on the Hackaday.io project page. A second PCB revision removed an unneeded resistor footprint; about 45 of the 140 units made used a zero-ohm jumper there instead of the 51-ohm resistor.
links:
- label: hackaday.io/project/158664-krusty-the-it
  url: https://hackaday.io/project/158664-krusty-the-it
  kind: hackaday
  archived: https://web.archive.org/web/20260512165639/https://hackaday.io/project/158664-krusty-the-it
- label: www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1/
  kind: store
  archived: https://web.archive.org/web/20260510025610/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1/
images:
- file: assets/images/badges/dc26/dc26-krusty-the-it-sao/efe5ca898f.jpg
  source: https://hackaday.io/project/158664-krusty-the-it
  credit: Twinkle Twinkie
  caption: Krusty the It SAO, a clown-face PCB with two LED eyes
  archived: https://web.archive.org/web/20260512165639/https://hackaday.io/project/158664-krusty-the-it
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/158664-krusty-the-it
  title: Krusty The It
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260512165639/https://hackaday.io/project/158664-krusty-the-it
- kind: url
  url: https://hackaday.io/project/158664-krusty-the-it
  title: Krusty The It
  accessed: '2026-09-07'
  note: Maker's own project page; confirmed DEF CON 26 origin, LED/resistor/header parts, quantity (140, ~45 with a zero-ohm jumper on a second revision), and KiCad/Gerber files.
  archived: https://web.archive.org/web/20260512165639/https://hackaday.io/project/158664-krusty-the-it
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1/
  title: TwinkleTwinkie's Badgelife SAO Add-on
  accessed: '2026-09-07'
  note: Tindie storefront; confirmed price ($20, $18 for 5+), sold-out/retired status, and pre-assembled sale.
  archived: https://web.archive.org/web/20260510025610/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Event and year were already correct (DC26 = DEF CON 26, 2018). No PCB color/shape info found on either source, so look.colors and look.shape are left empty. No maker duplicate found in existing_titles.txt (other Twinkle Twinkie SAOs there are Avocado, Black Cat, Daft Helmet, Mando Kitty, all DC30).
last_modified_date: '2026-09-07'
---

Krusty the It was Twinkle Twinkie's first Shitty Add-on (SAO), made for the DEF CON 26 (2018) indie badge scene. The board is a creepy, Pennywise-style clown face: two reverse-mount OSRAM TOPLED SMD LEDs sit behind the PCB and shine through it as the clown's eyes, glowing bright yellow once the SAO gets 3.3V from a host badge's SAO header. A single 51-ohm 0805 resistor limits current to the LEDs, and the board connects via a standard 2x2 vertical SAO header.

About 140 units were made. A second PCB revision dropped an unnecessary resistor footprint from the original design; roughly 45 of the 140 units carry a zero-ohm jumper there instead of the 51-ohm resistor. Twinkle Twinkie sold finished, pre-assembled units on Tindie for $20 each (or $18 each in quantities of five or more); the listing is now marked retired/sold out.

The hardware is open source: raw KiCad project files and Gerbers are posted on the Hackaday.io project page, so the design can be reproduced by anyone willing to source the same OSRAM LEDs and SAO header.
