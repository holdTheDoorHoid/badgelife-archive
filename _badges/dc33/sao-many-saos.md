---
title: SaO MANY SAOs
id: dc33-sao-many-saos
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Coruscant Ventures
  url: https://coruscantventures.com
  role: 'design/sale credited to vor_t3x1 (Discord) / u/MorningMother8622 (Reddit)'
summary: A large host badge with 25 SAO ports that can power and display many add-on boards at once, sold alongside a companion "SmartAO" SAO that adds LED animation control.
functions: Hosts and powers up to 25 SAOs simultaneously (about 300 mA @ 3.3V total, 30 mA if running off USB/barrel power alone); white perimeter LEDs are driven by whichever SAO is plugged into the top-left slot, with full animated control only available when the SmartAO SAO is installed there.
look:
  colors: [black, white]
  shape: rectangle
  themes: [village badge]
tech:
  mcu: null
  leds:
    count: null
    type: white SMD (perimeter)
    note: One white LED sits at the edge of each SAO slot; full color/animation control requires the separate SmartAO SAO plugged into the top-left port.
  display: none
  connectivity: []
  battery: 2x 18650 (pre-installed), charge/run via USB or barrel connector
  sao_version: null
get_one:
  price: $100
  price_usd: 100.0
  quantity: ''
  availability: unknown
  distribution: [purchase]
  where: Sold directly by Coruscant Ventures via their storefront (coruscantventures.com); at DEF CON 33 arrange payment/shipping via Discord, Reddit or email since the site's PayPal checkout was reported non-functional.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  firmware_url: null
  eda_tool: null
links:
- label: Coruscantventures.com
  url: https://Coruscantventures.com
  kind: website
- label: coruscantventures.com/defcon-badges/p/sao-many-saos
  url: https://coruscantventures.com/defcon-badges/p/sao-many-saos
  kind: website
- label: 'GitHub: DC33-SaO-MANY-SAOs'
  url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  kind: repo
images: []
contact:
  emails:
  - Ja@coruscantventures.com
notes:
- Holds and controls 25 SAOs, has already been released
- 'This entry duplicates dc33-sao-and-many-sao-badge, which was independently researched from the same maker/product and carries the full write-up plus saved images; see that entry for photos.'
status: released
sources:
- kind: sheet
  event: dc33
  row: 47
  updated: 8/13/2025 22:46:45
- kind: url
  url: https://coruscantventures.com/defcon-badges/p/sao-many-saos
  title: SaO MANY SAOs - Coruscant Ventures
  accessed: '2026-09-06'
  note: Product page confirming maker, price ($100), features, and that this is the host badge for the SmartAO add-on.
- kind: url
  url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  title: 'GitHub: vortexcodes/DC33-SaO-MANY-SAOs'
  accessed: '2026-09-06'
  note: README and schematic/BOM/photos confirming power system (2x 18650, USB/barrel charging), 25-SAO capacity, perimeter LED behavior, and that gerbers were withheld until after the con.
- kind: url
  url: https://coruscantventures.com
  title: Coruscant Ventures
  accessed: '2026-09-06'
  note: Homepage confirms the company and that it sells DEF CON badges; no product-level detail beyond the product page above.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'This row duplicates dc33-sao-and-many-sao-badge (same maker, same product, same $100 price, same GitHub repo) which was already researched in full with images saved. Filled in here from the same confirmed sources per the research guide''s duplicate-handling rule. MCU, exact LED count, quantity made, and current availability are not stated by the maker anywhere found; left empty rather than guessed.'
last_modified_date: '2026-09-06'
---

The SaO MANY SAOs badge is a large host board from Coruscant Ventures built around one gimmick: it has 25 separate SAO header slots arranged in a grid, so a badge collector can plug in nearly their entire haul of add-on boards at once. It runs off two pre-installed 18650 cells that can be charged over USB or a barrel jack, with onboard LEDs to show charging status and built-in surge protection.

A row of white LEDs runs around the board's perimeter, one near each SAO slot, but they are only driven by whatever is plugged into the top-left slot. Out of the box that just lights them; to get actual animations and color control, Coruscant Ventures sold a companion "SmartAO" SAO separately for that slot. The badge shipped assembled and tested, sold for $100 through the maker's Squarespace storefront, though at least some buyers reported the site's PayPal checkout was broken during the con and had to arrange payment directly via Discord, Reddit, or email instead.

Schematics, a bill of materials, and build photos are published on GitHub, but the maker noted gerbers "may be released after DEF CON," and no firmware or MCU details were published as of this check. This entry duplicates `dc33-sao-and-many-sao-badge`, which covers the same product and already has saved photos.
