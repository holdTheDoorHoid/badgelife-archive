---
title: 2x2 Minibadge Display
id: saintcon-2025-2x2-minibadge-display
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2025
year: 2025
makers:
- name: Pips
summary: A compact 2x2 display board for holding four SAINTCON minibadges, sharing its clock/driver circuit with Pips' larger 10x10 minibadge grid.
functions: Holds and displays 2x2 (four) minibadges using the same clock module design as the 10x10 minibadge grid; the design is meant to scale up to a 3x3 grid without changing components.
look:
  colors: []
  shape: null
  themes:
  - minibadge
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Purchase directly from the maker, Pips, at SAINTCON 2025.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=2x2%20Minibadge%20Display&year=2025
  url: https://minibadge.wiki/?search=2x2%20Minibadge%20Display&year=2025
  kind: website
images:
- file: assets/images/badges/saintcon-2025/2x2-minibadge-display/f9beb45289.jpg
  source: https://minibadge.wiki/?search=2x2%20Minibadge%20Display&year=2025
  credit: Pips
  caption: Front of the 2x2 Minibadge Display board
- file: assets/images/badges/saintcon-2025/2x2-minibadge-display/916631c204.jpg
  source: https://minibadge.wiki/?search=2x2%20Minibadge%20Display&year=2025
  credit: Pips
  caption: Back of the 2x2 Minibadge Display board
contact: {}
notes:
- 'category: Other; rarity: Super Rare'
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=2x2%20Minibadge%20Display&year=2025
  title: 2x2 Minibadge Display
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2025''.'
- kind: url
  url: https://minibadge.wiki/2025.json
  title: minibadge.wiki 2025 data feed
  accessed: '2026-09-07'
  note: JSON record backing the wiki listing page; source of description, soldering instructions, quantity made, category, rarity, acquisition method, and the front/back image filenames.
  archived: https://web.archive.org/web/20260611102155/http://minibadge.wiki/2025.json
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No maker profile, storefront, repo, or price could be found beyond the minibadge.wiki listing itself; MCU, LED, and quantity details are not stated there ("quantityMade" field is 0/blank on the source data). Availability, MCU, LEDs, and price left empty per the never-invent rule.
last_modified_date: '2026-09-07'
---

The 2x2 Minibadge Display is a small display board by the maker Pips, made for SAINTCON 2025, that holds and lights up four minibadges at once in a 2x2 layout. It reuses the same clock/driver circuit as Pips' larger 10x10 minibadge grid display, and the design is built so it could scale up to a 3x3 arrangement without swapping any components or changing the circuit.

Power comes in over USB-C, but the port is charge-only: it is wired with a 5.1k pulldown resistor to request 5V from the host, and the onboard DC-DC converter limits the board to roughly 500 mA. Assembly is rated beginner-level soldering, consisting of soldering pin sockets to mount the minibadges.

Pips listed it as sold directly from themself at the con, with a "Super Rare" community rarity rating and no quantity-made figure recorded. No separate storefront, repository, or price was found for it beyond the minibadge.wiki community listing.
