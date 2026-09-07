---
title: Chakra Badge
id: dc32-chakra-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: DC540
summary: A round-TFT, RP2040-powered badge shaped like a meditating figure with laser-cut acrylic wings, tracing chakra points down its spine with a coiled gold "kundalini" trace; built around seven on-badge challenges for a trophy competition.
functions: Seven built-in badge challenges/puzzles for a competition with physical trophies (three in-person winners plus one virtual winner); touch-pad-driven animations on the round display. Final challenge firmware was withheld until DEF CON 32 day one; presale units shipped with demo animations instead.
look:
  colors:
  - black
  - gold
  - white
  shape: meditating figure with wings
  themes:
  - art
  - wearable
  - fantasy
  - ctf
  form_factor: pcb badge
tech:
  mcu: RP2040
  leds: null
  display: round TFT (GC9A01 driver, non-touch)
  connectivity:
  - usb
  inputs:
  - touch
  battery: LiPo
  power: USB-C
  sao_version: none
get_one:
  price: $100.00
  price_usd: 100.0
  quantity: 'Limited presale batch, planned around 25 (35 shown in stock during presale); total production run not stated'
  availability: sold_out
  availability_note: 'No longer listed in the DC540 shop as of 2026-09-06/07 (product page returns 404); last confirmed available during the 2024 presale.'
  distribution:
  - purchase
  - preorder
  where: DC540's own WooCommerce shop (dc540.org), as a limited presale ahead of DEF CON 32, then direct sales at the con with final challenge firmware.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: dc540.org/xxx/shop
  url: https://dc540.org/xxx/shop/
  kind: store
- label: 'Chakra Badge – 2024 (product page, via Wayback Machine)'
  url: http://web.archive.org/web/20240528213848/https://dc540.org/xxx/product/chakra-badge-2024/
  kind: store
- label: DC540 Badge Announcement (2024-04-18)
  url: https://dc540.org/xxx/2024/04/badge-announcement/
  kind: article
images:
- file: assets/images/badges/dc32/chakra-badge/7030ebdf86.jpg
  source: "https://dc540.org/xxx/product/chakra-badge-2024/"
  credit: "DC540"
  caption: "The DC540 Chakra Badge, a round RP2040-powered badge with laser-cut acrylic wings"
contact:
  handles:
  - '@dc540_nova'
notes:
- The current price is $100 with $10 for shipping
- 'Assembled in the USA by Bradan Lane Studio (per the maker''s product listing).'
- 'The badge was originally planned for DEF CON 31 (2023) but slipped a year, per the maker.'
status: released
sources:
- kind: sheet
  event: dc32
  row: 49
  updated: '2024-06-01'
- kind: url
  url: http://web.archive.org/web/20240528213848/https://dc540.org/xxx/product/chakra-badge-2024/
  title: 'Chakra Badge – 2024 – DC540 Defcon Group'
  accessed: '2026-09-06'
  note: 'Product description, spec list, price ($100), stock count (35) at presale time, and product photos; live page now 404s.'
- kind: url
  url: https://dc540.org/xxx/2024/04/badge-announcement/
  title: Badge Announcement – DC540
  accessed: '2026-09-06'
  note: 'Design story: single-board RP2040 (custom, not a Pico devboard), EEPROM+flash, USB-C, LiPo, 3D-printed battery cover, laser-engraved acrylic wings with sidelighting, seven badge challenges with trophies, presale vs. DEF CON day-one firmware plan.'
- kind: url
  url: https://dc540.org/xxx/wp-content/uploads/2024/04/chakrabadge.jpg
  title: Chakra Badge product photo
  accessed: '2026-09-06'
  note: 'Saved as the entry image; shows the meditating-figure PCB shape, chakra points, acrylic wings, and lanyard.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Core facts confirmed on DC540''s own product listing (archived, since 404) and their badge-announcement post. LED count/type for the acrylic-wing "sidelights" is not specified anywhere found, so tech.leds is left empty. No public hardware/firmware repo was found for this badge (DC540''s GitHub org has no matching project), so make_your_own fields are left null rather than guessed. Display size (likely ~1.28" round, common for GC9A01) is not stated by the maker, so it was left out of tech.display rather than assumed.'
last_modified_date: '2026-09-06'
---

The Chakra Badge is DC540's DEF CON 32 badge: a single circuit board cut into the silhouette of a seated, meditating figure with a pair of laser-engraved, backlit acrylic wings bolted on at the shoulders. A round TFT sits where the figure's head would be, and a coiled gold trace runs down the board like a spine, passing through chakra icons rendered in the silkscreen. It replaces the "sandwich board" construction of DC540's earlier badges with a single RP2040-based board — built from scratch rather than around a Raspberry Pi Pico module — with its own EEPROM, flash, USB-C port, and LiPo battery under a 3D-printed cover. Touch pads along the "snake" segments serve as the only input, since the round display is not a touchscreen.

The badge was built around a set of seven on-badge challenges with laser-cut trophies for the first three in-person finishers and one virtual finisher. DC540 shipped a limited presale run (advertised as around 25 units, with roughly 35 shown in stock on the store) carrying only demo animations, holding back the actual challenge firmware until the morning of DEF CON 32's first day so that presale buyers and con-goers could compete on equal footing; reflashing over USB-C required no special tools. The badges were assembled in the US by Bradan Lane Studio. DC540 originally intended the design for DEF CON 31 but pushed it back a year to finish it properly. As of this research, the product page has been taken down and the badge does not appear in DC540's current shop, indicating the run has sold out.
