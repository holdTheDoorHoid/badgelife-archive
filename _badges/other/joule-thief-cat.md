---
title: Joule Thief Cat
id: other-joule-thief-cat
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: other
year: 0
makers:
- name: tilde.industries
  url: https://tilde.industries
summary: 'A beginner-friendly through-hole soldering kit shaped like a mischievous cat that harvests leftover energy from "dead" AA/AAA batteries to light its eyes.'
functions: 'Acts as a joule thief circuit: draws down residual charge from a discharged battery to light two LED "eyes", working down to about 0.4V input.'
look:
  colors:
  - black
  shape: cat
  themes:
  - cat
  - animal
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: yellow/orange-glowing eye LEDs
  display: none
  connectivity: []
  battery: 1x AA (or AAA with adapter), user-supplied discharged cell
  sao_version: none
get_one:
  price: "$21"
  price_usd: 21.0
  quantity: ''
  availability: available
  availability_note: 'Listed in stock on Tindie as of 2026-09-07 (34 units of the base kit).'
  distribution:
  - purchase
  where: Sold directly from tilde.industries, and via Tindie, Lectronz, Pimoroni, and Etsy storefronts.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: tilde.industries
  url: https://tilde.industries
  kind: website
- label: Joule Thief Cat product page
  url: https://tilde.industries/joulethiefcat/
  kind: website
- label: Joule Thief Cat Kit on Tindie
  url: https://www.tindie.com/products/tilde/joule-thief-cat-kit/
  kind: store
- label: Joule Thief Cat Kit on Lectronz
  url: https://lectronz.com/products/joule-thief-cat-kit
  kind: store
images:
- file: assets/images/badges/other/joule-thief-cat/922769de7d.jpg
  source: "https://tilde.industries/joulethiefcat/"
  credit: "tilde.industries"
  caption: "Assembled Joule Thief Cat kit with glowing eye LEDs"
- file: assets/images/badges/other/joule-thief-cat/ff5289c706.jpg
  source: "https://tilde.industries/joulethiefcat/"
  credit: "tilde.industries"
  caption: "Joule Thief Cat kit components before assembly"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
- Optional themed hat add-ons (witch hat, Santa/straw hat) are sold separately by the same maker.
status: released
sources:
- kind: url
  url: https://tilde.industries
  title: Joule Thief Cat
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''other''.'
- kind: url
  url: https://tilde.industries/joulethiefcat/
  title: Joule Thief Cat product page
  accessed: '2026-09-07'
  note: 'Product description, kit contents (2 LEDs, transistor, capacitor, resistor, ferrite core, AA holder), and photos.'
- kind: url
  url: https://www.tindie.com/products/tilde/joule-thief-cat-kit/
  title: Joule Thief Cat Kit from tilde.industries on Tindie
  accessed: '2026-09-07'
  note: 'Price ($21) and current stock/availability.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a standalone electronics soldering kit sold by tilde.industries (UK), not tied to any specific convention or year of release, so it stays filed under "other." No open-source hardware/firmware files were found; the maker does not mention releasing design files. Maker also makes con-specific SAOs (e.g. an MCH2022 Butterfly SAO) but the Joule Thief Cat itself is a general-market product sold across multiple storefronts (Tindie, Lectronz, Pimoroni, Etsy).'
last_modified_date: '2026-09-07'
---

The Joule Thief Cat is a beginner-friendly soldering kit from UK maker tilde.industries, styled as a small cat whose eyes light up. Rather than running from a fresh battery, it works as a classic "joule thief" boost circuit: it draws the last residual charge out of an AA (or AAA, with an adapter) battery that other devices, like a remote control or multimeter, have already declared dead. The kit works down to roughly 0.4V input and, on a fresher 1.5V cell, draws about 120mA while its two eye LEDs glow orange.

All parts are through-hole — LEDs, an NPN transistor, a capacitor, resistor, diode, wire, a ferrite core, and a battery holder — making it a common pick as a learn-to-solder project, with instructions published in both English and Japanese. It is not tied to a particular convention; tilde.industries sells it as an ongoing general-market product for about $21 through its own site as well as Tindie, Lectronz, Pimoroni, and Etsy. The maker also sells themed hats (witch, Santa/straw) as optional add-on accessories for the cat.

No hardware or firmware files were found published as open source, and no MCU is involved — the circuit is fully discrete/analog.
