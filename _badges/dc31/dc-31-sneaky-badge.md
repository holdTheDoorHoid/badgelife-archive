---
title: Sneaky Badge
id: dc31-dc-31-sneaky-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Gigs (@gigstaggart)
  url: https://gigsbadge.com/
summary: A DEF CON 31 badge with movable, hand-soldered letter tiles that play a built-in Wordle-style word game, made as an homage to the film Sneakers.
functions: 'Includes a Wordle-style word-guessing game with a dictionary of tens of thousands of words, played by arranging passive plug-in letter tiles that each encode a hard-coded Baudot code via connected/disconnected PCB traces.'
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - movie
  - retro computer
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: gigsbadge.com/product/sneakybadge
  url: https://gigsbadge.com/product/sneakybadge/
  kind: website
- label: gigsbadge.com (portfolio page)
  url: https://gigsbadge.com/
  kind: website
images:
- file: assets/images/badges/dc31/dc-31-sneaky-badge/fb1a219b59.jpg
  source: "https://gigsbadge.com/"
  credit: "Gigs (@gigstaggart)"
  caption: "Sneaky Badge with movable letter tiles"
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- The original sweep's title, "DC 31 Sneaky Badge", differs from the maker's own naming, "Sneaky Badge"; title corrected to match the maker's portfolio page.
status: released
sources:
- kind: url
  url: https://gigsbadge.com/product/sneakybadge/
  title: DC 31 Sneaky Badge
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://gigsbadge.com/
  title: Gigs Badge and PCB Design
  accessed: '2026-09-10'
  note: 'Maker''s own portfolio page confirms the badge, event/year (DEF CON 31), theme, letter-tile mechanic, and manufacturing details (~100 hand-soldered joints, 50,000 letter-tile PCBs sorted and bagged by hand). The product-page URL in the original link (gigsbadge.com/product/sneakybadge/) returns a 404; this portfolio page is the surviving source.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'The original product page (gigsbadge.com/product/sneakybadge/) 404s; all information comes from the maker''s portfolio page instead, which does not give price, quantity, availability, MCU/electronics details, or design-file links. The letter tiles are described as "completely passive" (no MCU), so tech.mcu/leds/display are left empty rather than guessed at for the badge body itself. Likely a duplicate of existing entry dc31-sneakers-badge (same maker, same badge, "Sneaky Badge" title) - flagged for de-duplication.'
last_modified_date: '2026-09-10'
---

The Sneaky Badge was Gigs's (@gigstaggart) DEF CON 31 entry, an homage to the film *Sneakers*. Rather than a single fixed PCB, it shipped with a large set of movable, passive letter tiles that plug into sockets on the badge; each tile is completely passive, encoding a hard-coded Baudot code through which traces are connected or cut. Arranging the tiles lets the wearer play a built-in Wordle-style word-guessing game backed by a dictionary of tens of thousands of words.

The letter-tile approach came at a heavy manufacturing cost: because the tile sockets use through-hole connections, each badge required nearly 100 hand-soldered joints, and the PCB manufacturer shipped the 50,000 letter-tile boards mixed together, requiring them to be sorted by hand and divided into statistically weighted bags before being packed with each badge. Gigs describes weeks of manual labor going into the project as a result.

No pricing, production-quantity, or availability information was found, and the maker's original product page for the badge (gigsbadge.com/product/sneakybadge/) is no longer live; the maker's portfolio page is the only surviving first-party source. No hardware or firmware files were found published for this project.
