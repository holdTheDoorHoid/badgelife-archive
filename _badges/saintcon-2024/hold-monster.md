---
title: Hold Monster
id: saintcon-2024-hold-monster
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: kittysedai
summary: 'A Baldur''s Gate 3-themed SAINTCON 2024 minibadge depicting the "Hold Monster" spell: a demonic, horned face framed by a jagged scroll-like border.'
functions: 'Two SMD LEDs (no microcontroller); a simple lit minibadge rather than an interactive one.'
look:
  colors: [black, gold]
  shape: rectangle
  themes: [monster, fantasy, video game]
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Two LEDs (D1, D2) with two current-limiting resistors (R1, R2); maker's instructions specify soldering LEDs first via the single-pad method, aimed at beginners.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: [swap]
  where: 'Maker states "Trade with me" as the acquisition method; not sold.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=Hold%20Monster&year=2024
  url: https://minibadge.wiki/?search=Hold%20Monster&year=2024
  kind: website
- label: minibadge.wiki data export (2024.json)
  url: https://minibadge.wiki/data/
  kind: doc
images:
  - file: assets/images/badges/saintcon-2024/hold-monster/91e836c6f0.jpg
    source: "https://minibadge.wiki/data/"
    credit: "kittysedai"
    caption: "Front of the Hold Monster minibadge"
  - file: assets/images/badges/saintcon-2024/hold-monster/fae143b916.jpg
    source: "https://minibadge.wiki/data/"
    credit: "kittysedai"
    caption: "Back of the Hold Monster minibadge"
contact: {}
notes:
- 'category: Personal; rarity: Super Rare; quantityMade listed as 0 in the minibadge.wiki data export (not stated by the maker in prose, may mean "not tracked" rather than literally zero made).'
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=Hold%20Monster&year=2024
  title: Hold Monster
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2024''.'
- kind: url
  url: https://minibadge.wiki/data/
  title: MiniBadge | Data
  accessed: '2026-09-07'
  note: 'The live search page returned no results client-side; the underlying 2024.json data export (linked from this Data page) carries the actual record: title, author (kittysedai), description (Baldur''s Gate 3 "Hold Monster" spell theme), soldering instructions/difficulty, category (Personal), conference year, quantityMade (0), rarity (Super Rare), and howToAcquire ("Trade with me"). Also the source of the front/back board-render image URLs.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, event, theme, LED/resistor count, soldering difficulty, acquisition method) come from the maker-submitted minibadge.wiki data export, which is the primary community record for SAINTCON minibadges but is self-reported rather than an independent maker page/store. Could not find price, quantity actually made (the wiki lists 0, which likely means untracked rather than none), board house, or any open-source design files. No separate maker storefront, repo, or social profile for kittysedai was found.'
last_modified_date: '2026-09-07'
---

Hold Monster is a SAINTCON 2024 minibadge by kittysedai, themed around the "Hold Monster" spell from Baldur's Gate 3 — a level 5 enchantment that paralyzes a creature. The board's artwork carries that theme through: a horned, demonic face rendered in gold on a black board, framed by a jagged border styled like a torn page or spell scroll.

Electronically it's simple: two SMD LEDs (D1, D2) each with their own current-limiting resistor (R1, R2), and no microcontroller. The maker's build notes mark it as a beginner-level solder, calling for the LEDs and resistor to go down first using the single-pad hand-soldering method before the pin header.

The badge was not sold; the maker's listed method of acquiring one was simply "Trade with me" at the con, and it's marked "Super Rare" in the community rarity tier used by minibadge.wiki. No separate storefront, repository, or design files for it were found.
