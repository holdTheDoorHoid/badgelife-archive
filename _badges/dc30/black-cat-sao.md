---
title: Black Cat SAO
id: dc30-black-cat-sao
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: Twinkle Twinkie
summary: A black-and-gold cat-shaped SAO with glowing green LED eyes, made for the DEF CON 30 badge ecosystem.
functions: Lights up a pair of green LED "eyes" when powered from a host badge's SAO header.
look:
  colors:
  - black
  - gold
  - green
  shape: cat
  themes:
  - animal
  - cat
tech:
  mcu: null
  leds:
    count: 2
    type: null
    note: Glowing green LED eyes
  display: null
  connectivity: []
  battery: null
  sao_version: v2
get_one:
  price: $20
  price_usd: 20.0
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing showed out of stock and the seller marked "on a break" as of 2026-09-06
  distribution:
  - purchase
  where: Tindie
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/twinkletwinkie/twinkletwinkies-black-cat-sao
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-black-cat-sao/
  kind: store
  archived: https://web.archive.org/web/20260503105405/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-black-cat-sao/
images:
- file: assets/images/badges/dc30/black-cat-sao/eb666b30d6.jpg
  source: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-black-cat-sao/
  credit: TwinkleTwinkie
  caption: Black Cat SAO with glowing green eyes
  archived: https://web.archive.org/web/20260503105405/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-black-cat-sao/
contact: {}
notes:
- Available 18Jul2023
status: released
sources:
- kind: sheet
  event: dc30
  row: 46
  updated: '2022-07-09'
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-black-cat-sao/
  title: TwinkleTwinkie's Black Cat SAO - Tindie
  accessed: '2026-09-06'
  note: Maker's storefront listing; source for description, price, connector type, and availability
  archived: https://web.archive.org/web/20260503105405/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-black-cat-sao/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Confirmed via the maker's Tindie listing (description, price, SAOv2 connector, out-of-stock status). Could not find a Hackaday.io page, GitHub repo, or press coverage; MCU/LED part number, quantity made, and open-source status remain unknown. Web search budget was exhausted before additional queries could run.
last_modified_date: '2026-09-06'
---

Twinkle Twinkie's Black Cat SAO is a badge add-on made for the DEF CON 30 badge ecosystem in 2022. It is styled as a black-and-gold cat face with a pair of green LEDs for eyes that light up when the SAO is plugged into a compatible badge. It uses a keyed 2x3 SAO v2 female connector, runs at 3.3V (so it can also be tested on a breadboard), and the maker notes it remains backward compatible with older 2x2 SAO badges, though upgrading to a v2 header is recommended.

The SAO sold for $20 through the maker's Tindie storefront. As of this research pass the listing shows it out of stock, with the seller's shop marked as "on a break." No production quantity, MCU/driver details, or open-source design files were found; there was no Hackaday.io project, GitHub repo, or press coverage located for this specific SAO.
