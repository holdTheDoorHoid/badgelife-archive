---
title: Wordweaving Badge
id: dc34-wordweaving-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: BigTaro's Badges
summary: A top-down adventure RPG badge with an OLED screen, styled as an ornate
  gold scroll, built around a CTF campaign against "eldritch horror-inspired" AI
  bosses.
functions: Connect with other word weaving badges, full gameboy-style adventure game, CTF and more!
look:
  colors:
  - gold
  shape: scroll
  themes:
  - fantasy
  - retro computer
  - console
  - ctf
  - puzzle
tech:
  mcu: RP2350
  leds:
    count: 16
    type: RGB
    note: 16 addressable RGB LEDs, described as "dozens of unlockable LED modes"
  display: 128x128 grayscale OLED
  connectivity: []
  battery: LiPo, rechargeable via USB-C
  sao_version: v2
get_one:
  price: $120
  price_usd: 120
  quantity: ''
  availability: limited
  distribution:
  - purchase
  where: Sold via Tindie (only 9 left in stock as of research date) and via Uberflux
    with DEF CON drop/on-site shipping; also listed for sale and giveaway at DEF
    CON 34 itself.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: bigtaro.net/wordweaving-badge
  url: https://bigtaro.net/wordweaving-badge
  kind: store
- label: Wordweaving Badge on Tindie
  url: https://www.tindie.com/products/bigtaro/wordweaving-badge-defcon-badgelife/
  kind: store
images:
- file: assets/images/badges/dc34/wordweaving-badge/180ea85cbf.png
  source: "https://www.tindie.com/products/bigtaro/wordweaving-badge-defcon-badgelife/"
  credit: "BigTaro's Badges"
  caption: "Wordweaving Badge product photo"
contact:
  discord: bigtaro
  emails:
  - bt@bigtaro.net
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 3
  updated: 5/25/2026 16:13:04
  listing: New
- kind: url
  url: https://bigtaro.net/wordweaving-badge
  title: "Wordweaving Badge — CTF Adventure Badge"
  accessed: '2026-09-06'
  note: Maker's own product page; confirmed MCU, display, LED count, battery, connectivity,
    and CTF/game concept.
- kind: url
  url: https://www.tindie.com/products/bigtaro/wordweaving-badge-defcon-badgelife/
  title: Wordweaving Badge (Defcon Badgelife) from BigTaro's Badges on Tindie
  accessed: '2026-09-06'
  note: Storefront listing; confirmed price ($120), stock level (9 left), full spec
    line (RP2350 + 4MB flash, 16 RGB LEDs, 128x128 grayscale display, SAO port,
    OpenLASIR compatible), and product photo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts confirmed on both the maker's own page and the Tindie storefront.
    Exact production quantity not stated anywhere found (only remaining Tindie stock,
    which is not the same number and changes over time, so left blank). No hardware/firmware
    repo or design files were found, so make_your_own fields are left null rather
    than guessed. tech.connectivity left empty because sources describe multiplayer
    "wordweaving" link-up and OpenLASIR compatibility (a laser-tag/badge-to-badge
    protocol) without naming an underlying physical layer (e.g. IR vs RF) precisely
    enough to place in the controlled vocabulary.
last_modified_date: '2026-09-06'
---

The Wordweaving Badge is BigTaro's Badges' entry for DEF CON 34: a gold, scroll-shaped PCB built around an RP2350 microcontroller with a 128x128 grayscale OLED and 16 addressable RGB LEDs, powered by a rechargeable LiPo battery charged over USB-C. It plays as a full top-down adventure game in the style of the original Game Boy, sending players through a pixel-art world to fight "eldritch horror-inspired" AI bosses that adapt and respond in words, while more than 30 capture-the-flag challenges and puzzles are woven through the story.

The badge is designed to talk to other Wordweaving badges nearby, letting players "wordsmith" from a shared pool of over 1,000 words as part of its multiplayer hooks, and it is built to be compatible with the OpenLASIR inter-badge standard used by other projects such as Dani's Laser Tag DS badge. It was sold at $120 through BigTaro's Tindie store (a limited run, with only a handful left in stock at last check) and through Uberflux with DEF CON drop and on-site shipping, and was also offered for sale and giveaway at the con itself per the community badge sheet.

No hardware design files, firmware repository, or exact production quantity were found on the maker's page or storefronts, so those fields are left blank rather than guessed.
