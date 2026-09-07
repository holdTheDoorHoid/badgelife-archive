---
title: Hacker Era
id: saintcon-2024-hacker-era
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: kittysedai
summary: A SAINTCON 2024 minibadge reading "IN MY HACKER ERA" in a bubbly retro font, playing on the "in my [x] era" slang phrase (a nod to Taylor Swift's "Swiftie Era").
functions: Lights a single LED; no interactive functions.
look:
  colors:
  - white
  - black
  - yellow
  - brown
  shape: rectangle
  themes:
  - meme
  - pop culture
  - text
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single SMD LED (D1) driven through a current-limiting resistor (R1); no microcontroller.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 0
  availability: unknown
  distribution:
  - swap
  where: 'Per the maker: "Trade with me."'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=Hacker%20Era&year=2024
  url: https://minibadge.wiki/?search=Hacker%20Era&year=2024
  kind: website
images:
- file: assets/images/badges/saintcon-2024/hacker-era/872d62dd39.jpg
  source: "https://minibadge.wiki/?search=Hacker%20Era&year=2024"
  credit: "kittysedai"
  caption: "Hacker Era minibadge, front"
- file: assets/images/badges/saintcon-2024/hacker-era/74056871c5.jpg
  source: "https://minibadge.wiki/?search=Hacker%20Era&year=2024"
  credit: "kittysedai"
  caption: "Hacker Era minibadge, back"
contact: {}
notes:
- 'category: Personal; rarity: Super Rare'
- 'Maker-listed soldering difficulty: Beginner. Soldering steps: LEDs first (single-pad
  method), then the resistor (single-pad method), then the pin headers.'
- 'Front artwork exists in both white and black board-color variants per the maker''s
  description; the saved photos show the white variant.'
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=Hacker%20Era&year=2024
  title: Hacker Era
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2024''.'
- kind: url
  url: https://minibadge.wiki/2024.json
  title: Minibadge Wiki 2024 data (Hacker Era record)
  accessed: '2026-09-07'
  note: 'Structured record backing the site listing: description, soldering instructions/difficulty,
    quantity made (0, i.e. not recorded), category, "how to acquire" (trade with maker),
    rarity, and front/back image URLs.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'All facts come from the maker''s own minibadge.wiki submission (front/back
    images and JSON record); no independent maker page, storefront, or press coverage
    was found. Quantity made is recorded as 0 on the source, which likely means "not
    stated" rather than a literal zero, so get_one.quantity is left at that raw value
    and price/price_usd are left empty since no price was ever listed (distribution
    is trade-only). No MCU is present; the board is a passive LED+resistor circuit
    per the back-of-board photo (parts D1, R1).'
last_modified_date: '2026-09-07'
---

"Hacker Era" is a SAINTCON 2024 minibadge by kittysedai, a small rectangular PCB whose front reads "IN MY HACKER ERA" in a bubbly, rounded retro typeface across black, brown, and yellow text on a light board. The name plays on the "in my [x] era" slang phrase, which the maker credits to Taylor Swift's "Swiftie Era." It exists in both white and black board-color versions.

Electrically it is a simple, beginner-level build: a single SMD LED (D1) wired through a current-limiting resistor (R1), with no microcontroller, sensors, or SAO header — it draws power from the host badge it plugs into rather than carrying its own battery. The maker's listed assembly order is LEDs first, then the resistor (both by the single-pad hand-soldering method), then the pin headers.

The maker categorizes it as a "Personal" badge with a "Super Rare" rarity rating and lists no price or public sale; it was distributed only by trading directly with kittysedai at the con. No quantity-made figure, open-source design files, or third-party coverage were found beyond the maker's own minibadge.wiki listing.
