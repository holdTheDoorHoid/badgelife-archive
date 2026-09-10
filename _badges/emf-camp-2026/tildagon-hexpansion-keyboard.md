---
title: Keebdexpansion (Tildagon Hexpansion Keyboard)
id: emf-camp-2026-tildagon-hexpansion-keyboard
layout: badge
parent: EMF Camp 2026
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: emf-camp-2026
year: 2026
makers:
- name: davedarko
  url: https://github.com/davedarko
  role: hardware design
- name: sodoku
  role: firmware/software
- name: kliment
  role: contributor
- name: Arturo182 (solder.party)
  role: rubber keypad / dome-sticker parts, KeebDeck base component
summary: A full-layout, RGB-backlit keyboard Hexpansion for the 2026 EMF Camp "Spaceagon" (Tildagon) badge, built around the solder.party KeebDeck keyboard.
functions: Adds a full keyboard for typing text into the badge's apps, with RGB-backlit keys.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: null
  leds:
    count: null
    type: RGB
    note: RGB-backlit keycaps, count not stated by sources.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: £8.50
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - purchase
  where: Sold to EMF Camp 2026 ticket holders through the official badge store; a shipping issue meant a batch of functional parts did not arrive in time, so many attendees on site did not receive a working keyboard.
make_your_own:
  open_source: true
  hardware_url: https://github.com/davedarko/KeebDeckHexpansion
  firmware_url: https://github.com/davedarko/KeebDeckHexpansion
  eda_tool: null
links:
- label: hackaday.com/2026/06/02/the-2026-emf-badge-arrives-with-an-add-on-as-expected-its-familiar
  url: https://hackaday.com/2026/06/02/the-2026-emf-badge-arrives-with-an-add-on-as-expected-its-familiar/
  kind: article
- label: tildagon.badge.emfcamp.org/hexpansions/creating-hexpansions
  url: https://tildagon.badge.emfcamp.org/hexpansions/creating-hexpansions/
  kind: website
- label: github.com/davedarko/KeebDeckHexpansion
  url: https://github.com/davedarko/KeebDeckHexpansion
  kind: repo
images:
- file: assets/images/badges/emf-camp-2026/tildagon-hexpansion-keyboard/e0282ad449.jpg
  source: https://github.com/davedarko/KeebDeckHexpansion
  credit: davedarko
  caption: Keebdexpansion keyboard hexpansion attached to a Tildagon badge
- file: assets/images/badges/emf-camp-2026/tildagon-hexpansion-keyboard/dbfaf05854.jpg
  source: https://tildagon.badge.emfcamp.org/hexpansions/creating-hexpansions/
  credit: EMF Camp
  caption: Prototype KeebDeck keyboard hexpansion
contact: {}
notes:
- 'First official Hexpansion for the Tildagon/Spaceagon badge platform: a plug-in keyboard add-on sold to EMF 2026 ticket holders (~£8.50), using edge-connector hexpansion slots. Found by the event-year sweep, task emf-badges.'
- The sweep's title (''Tildagon Hexpansion Keyboard'') was descriptive rather than the maker's name; the project itself is called ''Keebdexpansion'' (repo tildagon-keebdexpansion / KeebDeckHexpansion) by davedarko, sodoku and kliment, built on Arturo182's solder.party KeebDeck keyboard.
status: released
sources:
- kind: url
  url: https://hackaday.com/2026/06/02/the-2026-emf-badge-arrives-with-an-add-on-as-expected-its-familiar/
  title: Tildagon Hexpansion Keyboard
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-badges); event read as ''emf-camp-2026''.'
- kind: url
  url: https://tildagon.badge.emfcamp.org/hexpansions/creating-hexpansions/
  title: Creating Hexpansions - Tildagon badge docs
  accessed: '2026-09-08'
  note: Names the project "Keebdexpansion", credits sodoku/davedarko/kliment, links the KeebDeck base and a purchase link.
- kind: url
  url: https://github.com/davedarko/KeebDeckHexpansion
  title: davedarko/KeebDeckHexpansion
  accessed: '2026-09-08'
  note: Hardware repo, MIT licensed; confirms open-source hardware, credits, and provided the product photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Core facts (maker, name, price, open-source status) confirmed via the maker's own repo and the badge team's docs page, so treated as reliable, but the MCU/LED count/quantity made were not stated by any source and are left empty. Hackaday comments also report that most attendees on site did not receive a working unit due to a shipping failure of functional parts (noted under get_one.where); this could not be cross-checked against a maker statement, hence confidence medium rather than high.
last_modified_date: '2026-09-10'
model:
  file: assets/models/emf-camp-2026/tildagon-hexpansion-keyboard.glb
  method: kicad
  source_file: KiCad/main/main.kicad_pcb
  generated: '2026-09-10'
  bytes: 548092
---

The Keebdexpansion is the first official Hexpansion for EMF Camp's 2026 "Spaceagon" (Tildagon-family) conference badge: a full-layout, RGB-backlit keyboard that plugs into one of the badge's edge-connector Hexpansion slots so wearers can type text into on-badge apps. It was designed by davedarko, with software from sodoku and contributions from kliment, and it builds on Arturo182's (solder.party) KeebDeck keyboard hardware and rubber dome-sticker keypad. According to Hackaday's coverage, the EMF badge team originally approached Arturo182 directly, but he was tied up with another project, so davedarko took on adapting KeebDeck into a Hexpansion-format add-on; using an edge connector rather than pogo pins raised manufacturing cost but was chosen for durability.

The Hexpansion was sold to EMF Camp 2026 ticket holders through the official badge store for about £8.50. Coverage from the event notes a shipping problem meant a batch of functional keyboard parts didn't arrive in time, so a number of attendees on site ended up without a working unit despite having bought one.

The hardware design is published under an MIT license on GitHub (davedarko/KeebDeckHexpansion), with a companion firmware/software project maintained separately by sodoku.
