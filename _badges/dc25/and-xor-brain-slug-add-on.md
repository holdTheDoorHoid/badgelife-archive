---
title: AND!XOR Brain Slug Add-on
id: dc25-and-xor-brain-slug-add-on
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc25
year: 2017
makers:
- name: AND!XOR
summary: A tiny Futurama-style "brain slug" (Hunter S. Rodriguez) add-on board that plugged into AND!XOR's DEF CON 25 badge, later cited as the direct precedent for the Shitty Add-On (SAO) standard.
functions: Lights up a handful of WS2812B LEDs, driven by an onboard ATtiny85; the host badge only supplied it power.
look:
  colors:
  - green
  shape: null
  themes:
  - sci-fi
  - meme
  - pop culture
tech:
  mcu: ATtiny85
  leds:
    count: null
    type: WS2812B
    note: "A small handful of WS2812B LEDs; exact count not stated in sources."
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '~10'
  availability: unknown
  distribution: []
  where: 'Given out/attached with a handful of AND!XOR DC25 badges in 2017; not sold separately as far as sources show.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/ANDnXOR/ANDnXOR_DC25_Badge/tree/master/Brain%20Slug
  url: https://github.com/ANDnXOR/ANDnXOR_DC25_Badge/tree/master/Brain%20Slug
  kind: repo
- label: 'Hackaday: Introducing The Shitty Add-On V1.69bis Standard'
  url: https://hackaday.com/2019/03/20/introducing-the-shitty-add-on-v1-69bis-standard/
  kind: article
- label: 'Hackaday.io: An Oral History of the Shitty Add-On Standard'
  url: https://hackaday.io/project/52950-shitty-add-ons/log/151626-an-oral-history-of-the-shitty-add-on-standard
  kind: hackaday
images:
  - file: assets/images/badges/dc25/and-xor-brain-slug-add-on/3d6a424955.jpg
    source: "https://hackaday.com/2019/03/20/introducing-the-shitty-add-on-v1-69bis-standard/"
    credit: "Hackaday / AND!XOR"
    caption: "The DC25 AND!XOR badge with Brain Slug SAO attached, the design that inspired the Shitty Add-On standard"
contact: {}
notes:
- Futurama-style Brain Slug add-on board (ATtiny85 + WS2812B LEDs) for the AND!XOR DC25 badge, only ~10 made, later cited as the precedent for the Shitty Add-On standard. Found by the event-year sweep, task dc25-saos.
- The GitHub repo link from the original sweep (github.com/ANDnXOR/ANDnXOR_DC25_Badge/tree/master/Brain%20Slug) now 404s; the current AND!XOR GitHub org (created 2026) has no DC25 badge repo. Kept the link for reference but it could not be verified live.
status: listed
sources:
- kind: url
  url: https://github.com/ANDnXOR/ANDnXOR_DC25_Badge/tree/master/Brain%20Slug
  title: AND!XOR Brain Slug Add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc25-saos); event read as ''dc25''.'
- kind: url
  url: https://hackaday.com/2019/03/20/introducing-the-shitty-add-on-v1-69bis-standard/
  title: Introducing The Shitty Add-On V1.69bis Standard
  accessed: '2026-09-08'
  note: 'Confirms the Brain Slug existed on the DC25 (2017) AND!XOR badge, ATtiny85 + WS2812B LEDs, ~10 made, host badge only supplied power, and its role as the direct precedent for the SAO standard.'
- kind: url
  url: https://hackaday.io/project/52950-shitty-add-ons/log/151626-an-oral-history-of-the-shitty-add-on-standard
  title: An Oral History of the Shitty Add-On Standard
  accessed: '2026-09-08'
  note: 'Same account of the Brain Slug (Hunter S. Rodriguez / Futurama reference), corroborating the Hackaday article.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Existence and core facts (chip, LEDs, ~10 made, power-only connection, role as SAO precedent) are confirmed by two independent Hackaday sources, but the maker''s own repo link from the sweep is now dead and no working AND!XOR GitHub org holds a DC25 repo, so hardware/firmware files could not be verified directly. No maker storefront, price, or exact LED count found. Confidence kept at medium rather than high because the primary source (the repo) is unreachable.'
last_modified_date: '2026-09-08'
---

The Brain Slug is a small Futurama-themed add-on board — a nod to the show's mind-control parasite worn by Hunter S. Rodriguez — that AND!XOR built to go with their DEF CON 25 (2017) badge. It is a simple design: an ATtiny85 microcontroller driving a handful of WS2812B addressable LEDs, with the host badge doing nothing more than supplying power over the connector.

Only about ten of them were ever made, making it one of the rarer AND!XOR add-ons, but its influence outran its production run. When the wider badgelife community formalized the Shitty Add-On (SAO) connector standard in 2018–2019, the Brain Slug was cited by name as the precedent that showed a small, blinky, badge-hosted accessory board was worth standardizing around.

The original discovery sweep's GitHub link (`ANDnXOR/ANDnXOR_DC25_Badge`) no longer resolves, and the AND!XOR GitHub organization as it exists today carries no DC25-era repository, so the design files referenced by early write-ups could not be independently confirmed as still available.
