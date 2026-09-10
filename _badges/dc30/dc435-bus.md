---
title: DC435 BUS
id: dc30-dc435-bus
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: dc30
year: 2022
makers:
- name: Sh33pr0ck
  role: builder/submitter
- name: ay.aitch
  role: designer
summary: 'A DEF CON group (DC435) minibadge with a single LED that blinks or stays solid depending on which side of a solder-jumper pad is bridged.'
functions: 'Single LED with a bistable solder jumper: bridge one side for a blinking LED, the other for solid-on.'
look:
  colors: []
  shape: null
  themes:
  - security
  - village badge
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: 'Single-pad hand-soldered LED; behavior (blink vs. solid) set by a solder jumper.'
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution: []
  where: 'Given out informally by DC435 (the Salt Lake City DEF CON group) at their monthly meetups.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/data
  url: https://minibadge.wiki/data/
  kind: website
- label: 'MiniBadge Wiki 2022 data export (JSON)'
  url: https://minibadge.wiki/2022.json
  kind: doc
images:
  - file: assets/images/badges/dc30/dc435-bus/e83caadbe8.jpg
    source: "https://minibadge.wiki/data/"
    credit: "Sh33pr0ck / ay.aitch"
    caption: "DC435 BUS minibadge, front"
  - file: assets/images/badges/dc30/dc435-bus/a1df5d675e.jpg
    source: "https://minibadge.wiki/data/"
    credit: "Sh33pr0ck / ay.aitch"
    caption: "DC435 BUS minibadge, back"
contact: {}
notes:
- 'The MiniBadge Wiki data export lists this as a "Personal" category minibadge, conference year 2022, rarity "Rare", quantity made unrecorded (0/unknown).'
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/data/
  title: DC435 BUS
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://minibadge.wiki/2022.json
  title: 'MiniBadge Wiki 2022 data export'
  accessed: '2026-09-10'
  note: 'Full record for "DC435 BUS": author Sh33pr0ck, design credited to ay.aitch, category Personal, conference year 2022, soldering difficulty Beginner, rarity Rare, how to acquire "Find someone from DC435 and talk to them about our monthly meetups," build instructions describing a single LED and one solder jumper for blink vs. solid modes. Also supplied the front/back photos.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'This is a DC435 (a DEF CON group based in Salt Lake City, UT) minibadge, not a SAINTcon badge -- the sweep''s source page (minibadge.wiki) tracks DEF CON-family minibadges by conference year, and the 2022 data export lists this item under conferenceYear 2022 with no SAINTcon connection. Moved event from saintcon-2022 to dc30 (DEF CON 30, 2022) accordingly. No maker storefront, repo, or independent press coverage found beyond the MiniBadge Wiki record; price, quantity made, and hardware files are not stated anywhere found.'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/saintcon-2022/dc435-bus/
---

The DC435 BUS is a minibadge made for DC435, the DEF CON group based in Salt Lake City, Utah, for the 2022 conference season. It was built by Sh33pr0ck to a design by ay.aitch and handed out informally to people who connected with the group at its monthly meetups, rather than sold through any storefront.

Electronically it is simple: a single hand-soldered LED plus a resistor, both attached with the single-pad technique aimed at beginner solderers. A solder jumper pad lets the builder choose the LED's behavior at assembly time -- bridging one side makes it blink, the other makes it stay solid on -- so no two assemblies need behave identically.

The MiniBadge Wiki community archive, which catalogs DEF CON-family minibadges by conference year, lists it as a "Personal" category badge with a "Rare" rarity rating and no recorded quantity made. No independent coverage, repository, or purchase listing for it was found elsewhere.
