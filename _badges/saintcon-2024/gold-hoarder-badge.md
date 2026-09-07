---
title: Gold Hoarder Badge
id: saintcon-2024-gold-hoarder-badge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
series: Sea of Thieves minibadge set
makers:
- name: Mister X
  url: https://minibadge.wiki/?search=Mister%20X
summary: A key-shaped SAINTCON 2024 minibadge themed after the Gold Hoarders faction from the video game Sea of Thieves, one of a personal set of Sea of Thieves-themed minibadges by the same maker.
functions: 'No interactive functions beyond two lit LEDs; it is a trade/collectible minibadge, not a game piece.'
look:
  colors:
  - black
  - gold
  shape: key
  themes:
  - pirate
  - video game
  - pop culture
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 'Two through-hole LEDs (D1, D2) each paired with a resistor (R1, R2); soldering guide calls for the "single-pad method" for hand soldering.'
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: unknown
  distribution:
  - swap
  - free_drop
  where: "Traded in person with the maker at SAINTCON 2024; given away free to anyone who didn't have a minibadge to trade."
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=Gold%20Hoarder%20Badge&year=2024
  url: https://minibadge.wiki/?search=Gold%20Hoarder%20Badge&year=2024
  kind: website
- label: minibadge.wiki 2024 data (Gold Hoarder Badge entry)
  url: https://minibadge.wiki/2024.json
  kind: doc
images:
- file: assets/images/badges/saintcon-2024/gold-hoarder-badge/5e68368f7c.png
  source: "https://minibadge.wiki/2024.json"
  credit: "Mister X (@thatonemisterx)"
  caption: "Front of the Gold Hoarder minibadge, a key-shaped PCB themed after Sea of Thieves' Gold Hoarders faction"
- file: assets/images/badges/saintcon-2024/gold-hoarder-badge/7b69587300.png
  source: "https://minibadge.wiki/2024.json"
  credit: "Mister X (@thatonemisterx)"
  caption: "Back of the Gold Hoarder minibadge, showing two LEDs (D1, D2), two resistors, and the maker's handle @thatonemisterx"
contact: {}
notes:
- 'category: Personal; rarity: Super Rare'
- 'Maker signs the board silkscreen as "@thatonemisterx".'
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=Gold%20Hoarder%20Badge&year=2024
  title: Gold Hoarder Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2024''.'
- kind: url
  url: https://minibadge.wiki/2024.json
  title: minibadge.wiki 2024 submissions data (JSON)
  accessed: '2026-09-07'
  note: 'The search page itself is JS-rendered and returns no content to a plain fetch; this is the underlying data file it loads from, containing the actual Gold Hoarder Badge record (description, soldering instructions, category, rarity, acquire method, front/back image paths).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source is the maker''s own submission on minibadge.wiki (community-run SAINTCON minibadge database); no independent maker page, repo, or press coverage found. Quantity made is recorded as 0 in the source data, which appears to mean "not tracked" rather than an actual count, so get_one.quantity is left empty. No hardware/firmware files were found, so make_your_own is left null rather than guessed. LED type is generic through-hole (silkscreen just labels them D1/D2); exact part number not given.'
last_modified_date: '2026-09-07'
---
The Gold Hoarder Badge is a SAINTCON 2024 minibadge shaped like an ornate brass key, made by a hobbyist who goes by Mister X (signed on the board as @thatonemisterx). It's one entry in a personal set of minibadges themed after the four playable factions in the pirate video game Sea of Thieves; this one represents the Gold Hoarders, the faction built around treasure-hunting and vault-looting. The board is a simple, beginner-level build: two through-hole LEDs and their paired resistors on the back, powered off the host badge rather than its own battery, with four 2-position headers connecting it in.

The badge was made and distributed informally at the con rather than sold: the maker's own instructions say to trade for it, or just ask for one for free if you don't have anything to trade. It carries a "Super Rare" rarity tag and is filed under the "Personal" category on minibadge.wiki, the community-run database of SAINTCON minibadges, which is the only source found for this entry — no separate maker page, storefront, or open-source hardware release turned up.
