---
title: true's RGB Addon Addon for DC31 Badge
id: dc31-true-s-rgb-addon-addon-for-dc31-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: trueControl
  url: https://shop.truecontrol.org/
summary: 'An RGB LED SAO/addon board with a GAT (v1.69bis) addon header, made to plug into the official DEF CON 31 badge and add programmable RGB lighting.'
functions: 'Drives 8 RGB LEDs (5 front firing, 2 side firing, 1 rear firing) across 3 configurable zones, with more than 6 selectable lighting programs, including accelerometer-reactive and power-saving modes. User adjusts brightness with a button press. Can pass power through to a plugged-in addon even with its own LEDs off.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: null
  leds:
    count: 8
    type: RGB
    note: '5 front firing, 2 side firing, 1 rear firing, across 3 configurable zones'
  display: none
  connectivity: []
  battery: LiPo (rechargeable, chargeable while installed)
  sao_version: v1.69bis
get_one:
  price: "$30.00 (list price shown crossed out at $60.00)"
  price_usd: 30
  quantity: ''
  availability: available
  availability_note: '13 in stock per storefront listing, checked 2026-09-08; listing states orders are for pickup only at DEF CON 33, with shipping available about a week after the con.'
  distribution:
  - purchase
  where: 'trueControl webshop (shop.truecontrol.org)'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: shop.truecontrol.org/index.php?route=product%2Fproduct&product_id=133
  url: https://shop.truecontrol.org/index.php?route=product%2Fproduct&product_id=133
  kind: store
- label: DC31 Addon Addon user manual
  url: https://dc31.truecontrol.org/yearsite/manual/addon-addon
  kind: doc
- label: dc31.whiskeypirates.com
  url: https://dc31.whiskeypirates.com/
  kind: website
images:
  - file: assets/images/badges/dc31/true-s-rgb-addon-addon-for-dc31-badge/a59c7f968a.jpg
    source: "https://shop.truecontrol.org/index.php?route=product%2Fproduct&product_id=133"
    credit: "trueControl"
    caption: "Addon Addon RGB board installed inside a DC31 badge"
  - file: assets/images/badges/dc31/true-s-rgb-addon-addon-for-dc31-badge/6d88384d7d.jpg
    source: "https://shop.truecontrol.org/index.php?route=product%2Fproduct&product_id=133"
    credit: "trueControl"
    caption: "Addon Addon RGB board, standalone"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 4).
- 'The sweep title matches the storefront''s page <title> exactly ("true''s RGB Addon Addon for DC31 Badge"); the storefront''s own product heading and breadcrumb instead read "RGB Addon Addon for DC31 Badge" (no "true''s").'
status: released
sources:
- kind: url
  url: https://shop.truecontrol.org/index.php?route=product%2Fproduct&product_id=133
  title: true's RGB Addon Addon for DC31 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run4-spotted); event read as ''dc31''.'
- kind: url
  url: https://shop.truecontrol.org/index.php?route=product%2Fproduct&product_id=133
  title: RGB Addon Addon for DC31 Badge - trueControl Webshop
  accessed: '2026-09-08'
  note: 'Confirmed the product exists; supplied summary, functions, LED count/layout, battery, price, stock count, availability, distribution, links, and product photos.'
- kind: url
  url: https://dc31.whiskeypirates.com/
  title: whiskey pirates
  accessed: '2026-09-08'
  note: 'Linked from the storefront as the DC31 badge/info site; confirms the Whiskey Pirate Crew / trueControl connection but a splash page with no addon-specific content.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Storefront description is the only source read (a manual link and a schematic link are mentioned on the page but the schematic was noted by the maker as "coming soon" and neither was independently verified). MCU/chip is not named anywhere on the page, so tech.mcu is left null. This entry duplicates dc31-rgb-addon-addon-for-dc31-badge-true-s-addon-addon ("RGB Addon Addon for DC31 Badge (true''s Addon Addon)", trueControl/true) already in the archive; that entry should be treated as the primary record and this one merged or removed by a maintainer.'
last_modified_date: '2026-09-08'
---

trueControl's "Addon Addon" is an RGB LED SAO built to plug into the official DEF CON 31 badge using a GAT (v1.69bis) addon header. It carries 8 RGB LEDs arranged across three zones (five front-firing, two side-firing, one rear-firing) and offers more than six selectable lighting programs, including accelerometer-driven and power-saving modes, all user-configurable, with brightness adjusted by a button press. It also passes power through to whatever addon is plugged into it even when its own LEDs are switched off.

The board runs on a rechargeable LiPo battery and is designed to be charged in place; the maker's listing warns that the power switch is a mechanical weak point and to avoid pressure on it during installation or handling. It was designed, assembled, and coded by "true" of the Whiskey Pirate Crew / trueControl. As of this research pass the trueControl webshop still lists it for $30 (marked down from $60) with 13 units in stock, though the listing notes orders are for pickup at DEF CON 33 with shipping available roughly a week later.

This entry is a duplicate of an existing archive record, `dc31-rgb-addon-addon-for-dc31-badge-true-s-addon-addon`, which should be treated as canonical.
