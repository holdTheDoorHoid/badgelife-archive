---
title: belgrade-shitty-addon-adapter
id: supercon-2018-belgrade-shitty-addon-adapter
layout: badge
parent: Supercon 2018
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2018
year: 2018
makers:
- name: flummer
  url: https://github.com/flummer
summary: A small passive adapter PCB that lets
functions: Breaks out the badge's 9-pin expansion header to a standard female pin header so any Shitty Add-On board can be plugged in; carries no active electronics of its own.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: available
  availability_note: OSH Park shared project page still live as of 2026-09-07 (order-your-own, made to order; not a fixed batch).
  distribution:
  - purchase
  where: Order-your-own PCB via the maker's OSH Park shared project link; not sold as an assembled product.
make_your_own:
  open_source: true
  hardware_url: https://github.com/flummer/belgrade-shitty-addon-adapter
  firmware_url: null
  gerbers_url: https://oshpark.com/shared_projects/ychlFFka
  fab_url: https://oshpark.com/shared_projects/ychlFFka
  eda_tool: KiCad
  license: CC-BY-SA-4.0
links:
- label: github.com/flummer/belgrade-shitty-addon-adapter
  url: https://github.com/flummer/belgrade-shitty-addon-adapter
  kind: repo
- label: OSH Park shared project (order a board)
  url: https://oshpark.com/shared_projects/ychlFFka
  kind: fab
- label: Badge for Hackaday Conference 2018 in Belgrade (Hackaday.io project)
  url: https://hackaday.io/project/80627-badge-for-hackaday-conference-2018-in-belgrade
  kind: hackaday
  archived: https://web.archive.org/web/20260214124318/https://hackaday.io/project/80627-badge-for-hackaday-conference-2018-in-belgrade
- label: DEF CON 26 Shitty Add-Ons (Hackaday.io project)
  url: https://hackaday.io/project/52950-defcon-26-shitty-add-ons
  kind: hackaday
images:
- file: assets/images/badges/supercon-2018/belgrade-shitty-addon-adapter/2e3f047045.jpg
  source: https://github.com/flummer/belgrade-shitty-addon-adapter
  credit: flummer
  caption: Assembled Belgrade/Supercon 2018 Shitty Addon adapter board
contact: {}
notes:
- adapter for badge to accept SAOs
status: released
sources:
- kind: url
  url: https://github.com/flummer/belgrade-shitty-addon-adapter
  title: belgrade-shitty-addon-adapter
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''Hackaday Belgrade / Supercon 2018''.'
- kind: url
  url: https://raw.githubusercontent.com/flummer/belgrade-shitty-addon-adapter/master/README.md
  title: 'README: Hackaday Belgrade Badge Shitty Addon Adapter'
  accessed: '2026-09-07'
  note: Confirms purpose, connector hardware (9-pin female + M20-7810245 2x2 header), and OSH Park order link; maker states it fits both the Hackaday Belgrade 2018 and Hackaday Superconference 2018 badges.
- kind: url
  url: https://api.github.com/repos/flummer/belgrade-shitty-addon-adapter
  title: 'GitHub API: repo metadata'
  accessed: '2026-09-07'
  note: Confirms license (CC-BY-SA-4.0), no listed topics, single-maintainer repo, created May 2018.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's own repo confirms this adapter was made for both the Hackaday Belgrade 2018 badge and the Hackaday Superconference 2018 badge, so the existing supercon-2018 event assignment is correct (no separate Hackaday Belgrade 2018 event id exists in events.yml to compare against). No price or production quantity is stated anywhere; it is an order-your-own OSH Park share rather than a batch the maker sold or gave away, so price/quantity/where are left mostly empty rather than guessed. No firmware applies (passive adapter, no MCU/LEDs).
last_modified_date: '2026-09-07'
---

The Belgrade Shitty Addon Adapter is a small passive PCB by GitHub user flummer that adapts the 9-pin expansion connector on the 2018 Hackaday conference badges to accept standard #badgelife Shitty Add-On boards. It carries no microcontroller or LEDs of its own — it is purely a connector breakout, using a right-angle 9-pin female header on one side and a low-profile 2x2 header (or direct pin-header soldering) on the other to expose the SAO-style pins.

According to the maker's README, the adapter fits both the Hackaday Belgrade 2018 conference badge and the Hackaday Superconference 2018 badge. The design (schematic, PCB layout, and footprint libraries) was published on GitHub in KiCad format and released under a CC-BY-SA-4.0 license, with a ready-to-order OSH Park shared project link so anyone could fabricate their own copy rather than buying a finished unit from the maker.

No price, production run, or giveaway details are documented; this looks to have been a one-off design shared for other Hackaday-badge owners to fab themselves rather than a product the maker sold or distributed at the event.
