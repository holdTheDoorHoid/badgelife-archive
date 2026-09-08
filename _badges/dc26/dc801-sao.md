---
title: DC801 SAO
id: dc26-dc801-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: snurkle engineering / hamster
summary: A tiny self-blinking SAO fundraiser for DC801, DEF CON 26's local hacker group, with no microcontroller at all.
functions: Fades between colors on its own with no host interaction required.
look:
  colors: []
  shape: null
  themes:
  - security
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: $10
  price_usd: 10
  quantity: ''
  availability: sold_out
  availability_note: 'Listed as out of stock on Tindie as of May 15, 2021; still out of stock as checked 2026-09-08.'
  distribution:
  - purchase
  where: Sold on Tindie by seller "hamster" (snurkle engineering); proceeds supported DC801's space and hardware development.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/hamster/dc801-sao-badgelife-addon
  url: https://www.tindie.com/products/hamster/dc801-sao-badgelife-addon/
  kind: store
images:
- file: assets/images/badges/dc26/dc801-sao/95c065b105.jpg
  source: "https://www.tindie.com/products/hamster/dc801-sao-badgelife-addon/"
  credit: "snurkle engineering"
  caption: "DC801 SAO product photo"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 4).
- 'Sheet listed event as ''unknown''; Tindie listing places it in the 2018 / DEF CON 26 badgelife community.'
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/hamster/dc801-sao-badgelife-addon/
  title: DC801 SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run4-spotted); event read as ''unknown''.'
- kind: url
  url: https://www.tindie.com/products/hamster/dc801-sao-badgelife-addon/
  title: DC801 SAO badgelife addon - Tindie
  accessed: '2026-09-08'
  note: Confirmed maker, price ($10), SAO header type, no-MCU self-blinking LED design, out-of-stock status, and that proceeds supported DC801.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Only source found is the Tindie storefront itself; no maker blog post, repo, or press coverage located. Exact LED count/type and colors are not stated on the listing, so those fields are left empty. No hardware or firmware files are published for this simple passive-LED design.'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/other/dc801-sao/
---

The DC801 SAO is a small "Shitty Add-On" sold by hamster of snurkle engineering to raise money for DC801, the Salt Lake City-based hacker group and DEF CON group behind Salt Lake City's DC801 badges. Unlike most SAOs in the badgelife scene, it carries no microcontroller and no I2C connectivity at all: it is a bare LED circuit that fades between colors on its own once power is applied through the standard 2x2 SAO header, requiring no code or programming from the badge it plugs into.

The add-on shipped partially assembled, with the buyer expected to solder on a resistor and pin header themselves, and included a small hole near pin 1 so it could be tied down with string or wire to stay secured on a badge. It sold for $10 on Tindie starting around DEF CON 26 (2018), with proceeds going toward DC801's space and hardware development, and has been listed as out of stock since May 2021.
