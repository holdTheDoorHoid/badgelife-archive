---
title: Minibadge Display Devboard
id: saintcon-2026-minibadge-display-devboard
layout: badge
parent: Saintcon 2026
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: saintcon-2026
year: 2026
makers:
- name: Pips
summary: A pre-soldered power/driver board for building custom SAINTCON minibadge displays, handling USB-C and LiPo power, battery charging, and board-to-board or WAGO-terminal wiring to up to 30-50 minibadges.
functions: 'Supplies and switches power for a custom minibadge display: USB-C input, LiPo battery input and charging, and regulated 3.3V/CLK/SYS outputs that a builder wires or board-to-board mounts to their own minibadge PCBs.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity:
  - usb
  battery: LiPo (charges at 4.2V@800mA)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '50'
  availability: unknown
  distribution:
  - purchase
  where: Maker's Tindie store (https://www.tindie.com/stores/pips/); store page could not be checked directly (blocked by a bot-challenge when fetched).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=Minibadge%20Display%20Devboard&year=2026
  url: https://minibadge.wiki/?search=Minibadge%20Display%20Devboard&year=2026
  kind: website
- label: minibadge.wiki 2026 data export (JSON entry for this board)
  url: https://minibadge.wiki/2026.json
  kind: doc
  archived: https://web.archive.org/web/20260611102319/http://minibadge.wiki/2026.json
- label: Pips' Tindie store
  url: https://www.tindie.com/stores/pips/
  kind: store
  archived: https://web.archive.org/web/20251212232747/https://www.tindie.com/stores/pips/
images:
- file: assets/images/badges/saintcon-2026/minibadge-display-devboard/58a2ac87ce.jpg
  source: https://minibadge.wiki/2026.json
  credit: Pips
  caption: Minibadge Display Devboard, front
  archived: https://web.archive.org/web/20260611102319/http://minibadge.wiki/2026.json
- file: assets/images/badges/saintcon-2026/minibadge-display-devboard/5d5d897f5b.jpg
  source: https://minibadge.wiki/2026.json
  credit: Pips
  caption: Minibadge Display Devboard, back
  archived: https://web.archive.org/web/20260611102319/http://minibadge.wiki/2026.json
contact: {}
notes:
- 'category: Badge Accessory; qty made: 50'
- 'Board house: JLCPCB. Soldering difficulty listed as "Pre-soldered" (sold assembled, not a solder kit).'
- 'Electrical specs per maker: Input (USB-C) 5V@3A; Input (Battery) 4.2V@3A; Battery charging 4.2V@800mA; Output (3.3V) 3.3V@3A; Output (CLK) 3.3V@3A; Output (SYS) input voltage@amperage (whichever is higher); max total minibadges supported 30-50.'
- The maker also lists a related but separate item on the same sheet, "5x5 Stackable Minibadge Display" (also by Pips, SAINTCON 2026) — reported separately, not merged into this entry.
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=Minibadge%20Display%20Devboard&year=2026
  title: Minibadge Display Devboard
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2026''.'
- kind: url
  url: https://minibadge.wiki/2026.json
  title: Minibadge Wiki 2026 data export
  accessed: '2026-09-07'
  note: 'Raw JSON record for this board: description, specialInstructions (power specs), solderingDifficulty, quantityMade, boardHouse, howToAcquire, and image filenames. The search-results page itself renders via JS and returned no content when fetched directly; this JSON export (linked from minibadge.wiki/data/) was the actual source of the facts filled in below.'
  archived: https://web.archive.org/web/20260611102319/http://minibadge.wiki/2026.json
- kind: url
  url: https://www.tindie.com/stores/pips/
  title: Pips's Tindie store
  accessed: '2026-09-07'
  note: Named by the maker as where to buy the board ("Purchase from my Tindie store"). The store page itself returned a Cloudflare bot-challenge page when fetched, so price and current listing status could not be confirmed.
  archived: https://web.archive.org/web/20251212232747/https://www.tindie.com/stores/pips/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (maker, event, function, power specs, quantity, board house, sale channel) come from the maker's own JSON record on minibadge.wiki, which counts as a maker-provided source since minibadge.wiki data is community-submitted by the badge's own maker. Price could not be confirmed because the Tindie store page is behind a Cloudflare challenge that blocked automated fetching. No MCU/LEDs/display are listed because this is a bare power/driver board, not a display itself — it is meant to power a display the buyer builds separately. No mockup or CAD/PCB design files were found published, so make_your_own is left null/unknown rather than guessed.
last_modified_date: '2026-09-07'
---

The Minibadge Display Devboard is a power and interconnect board by the maker Pips, made for SAINTCON 2026's minibadge scene. Rather than being a display or badge itself, it is infrastructure: a pre-soldered board meant to sit behind someone else's custom minibadge display build, handling USB-C and LiPo battery power, battery charging, and clean 3.3V/CLK/SYS power rails that can drive up to roughly 30-50 minibadges at once. Builders can either mount their own PCB directly to it board-to-board, or wire it up to an existing display using push-in WAGO terminals.

Fifty units were made, fabricated through JLCPCB, and sold pre-assembled (no soldering required by the buyer) through Pips' Tindie store. No price could be confirmed, since the Tindie storefront returned a bot-challenge page rather than its contents when checked.

The same maker also listed a separate, related item for SAINTCON 2026 called the "5x5 Stackable Minibadge Display" — a display module rather than a power board — which is not part of this entry and would need its own writeup.
