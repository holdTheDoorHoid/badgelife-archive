---
title: Ninja Networks DEF CON 17 Party Badge
id: dc17-ninja-networks-def-con-17-party-badge
layout: badge
parent: DC17
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc17
year: 2009
makers:
- name: Ninja Networks (Amanda Wozniak "w0z", Brandon Creighton "cstone")
summary: An electronic invitation to Ninja Networks' invitation-only DEF CON 17 party, whose ten LED displays randomly cycle characters until they lock in to spell "NINJA PARTY", WarGames-style.
functions: Default mode cycles and locks in characters across the display to spell "NINJA PARTY"; includes a Simon memory game, a unique-identifier display, sponsor URL display, and an on-board debugger for reading memory and reprogramming without external hardware, via four buttons.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - text
tech:
  mcu: Freescale MC9S08QE8
  leds: null
  display: 10x 16-segment HIOX-format LED character displays (two rows of five)
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ~$20/unit to produce (initially budgeted at $12)
  price_usd: null
  quantity: 500+
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of Ninja Networks' invitation-only party at DEF CON 17, August 2009.
make_your_own:
  open_source: true
  hardware_url: https://www.ninjas.org/badges/defcon17.html
  firmware_url: https://www.ninjas.org/badges/defcon17.html
  eda_tool: null
links:
- label: www.ninjas.org/badges/defcon17.html
  url: https://www.ninjas.org/badges/defcon17.html
  kind: website
  archived: https://web.archive.org/web/20260413015400/https://ninjas.org/badges/defcon17.html
- label: hackaday.com/2009/08/10/ninja-networks-party-badge
  url: https://hackaday.com/2009/08/10/ninja-networks-party-badge/
  kind: article
  archived: https://web.archive.org/web/20260414193322/https://hackaday.com/2009/08/10/ninja-networks-party-badge/
images:
- file: assets/images/badges/dc17/ninja-networks-def-con-17-party-badge/1f26b31166.jpg
  source: https://www.ninjas.org/badges/defcon17.html
  credit: Ninja Networks
  caption: Assembled Ninja Networks DEF CON 17 party badge, top view
  archived: https://web.archive.org/web/20260413015400/https://ninjas.org/badges/defcon17.html
- file: assets/images/badges/dc17/ninja-networks-def-con-17-party-badge/35472a3aac.jpg
  source: https://www.ninjas.org/badges/defcon17.html
  credit: Ninja Networks
  caption: A batch of completed DEF CON 17 Ninja Networks party badges
  archived: https://web.archive.org/web/20260413015400/https://ninjas.org/badges/defcon17.html
contact: {}
notes:
- Unofficial party badge for Ninja Networks' DC17 event, built around a Freescale MC9S08QE8 with ten 16-segment LED displays that cycle through characters and spell 'NINJA PARTY', includes a Simon game; over 500 made. Found by the event-year sweep, task dc17-all.
status: released
sources:
- kind: url
  url: https://www.ninjas.org/badges/defcon17.html
  title: Ninja Networks DEF CON 17 Party Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc17-all); event read as ''dc17''.'
  archived: https://web.archive.org/web/20260413015400/https://ninjas.org/badges/defcon17.html
- kind: url
  url: https://www.ninjas.org/badges/defcon17.html
  title: DEFCON 17 Ninja Badge - Ninjas.org
  accessed: '2026-09-08'
  note: 'Maker''s own project page: designers, chip, display, quantity (500+), assembly process, open-source release of schematics/gerbers/BOM/source code.'
  archived: https://web.archive.org/web/20260413015400/https://ninjas.org/badges/defcon17.html
- kind: url
  url: https://hackaday.com/2009/08/10/ninja-networks-party-badge/
  title: Ninja Networks Party Badge - Hackaday
  accessed: '2026-09-08'
  note: Corroborates designers (cstone/w0z), MCU, display type, quantity, PCB fab (4PCB), and open release of design files; notes XeroBank sponsorship.
  archived: https://web.archive.org/web/20260414193322/https://hackaday.com/2009/08/10/ninja-networks-party-badge/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Both the maker's own page and Hackaday agree on the core facts. LED count/type per segment (16-segment character displays, not addressable RGB) recorded under tech.display rather than tech.leds since these are HIOX-format character/segment displays, not individually driven LED pixels. Exact unit price varies by source ($12 budgeted vs. ~$20 actual); recorded both. No price paid by attendees was found — it was given away free to party guests, not sold.
last_modified_date: '2026-09-08'
---

Ninja Networks handed out this electronic badge as the ticket to their invitation-only party at DEF CON 17 in August 2009. Designed by Amanda Wozniak ("w0z") and Brandon Creighton ("cstone"), the badge is built around a Freescale MC9S08QE8 8-bit microcontroller driving ten 16-segment HIOX-format LED character displays arranged in two rows of five. In its default mode the display randomly cycles through characters and progressively locks each one in place until it spells out "NINJA PARTY," a nod to the character-lock sequence from the film *WarGames*. It also includes a Simon-style memory game, a screen for viewing the badge's unique identifier and a sponsor URL (event sponsor XeroBank), and an on-board debugger that lets the badge be reprogrammed using only its four buttons, no external hardware required.

More than 500 badges were hand-assembled by volunteers across Boston, Los Angeles, and Las Vegas, with PCBs fabricated by 4PCB and reflow soldering done in part on a $30 Target hotplate. Each unit took roughly 45 minutes to assemble by hand, for a combined total of over 87,500 solder joints across the run. Production cost was initially budgeted at about $12 per badge but rose closer to $20 by completion.

## Make your own

Cstone released the schematics, Gerber files, bill of materials, and public-domain source code for the badge on the Ninja Networks project page, under a mix of Creative Commons Attribution and public-domain licensing, making it possible for others to build their own copy of the badge.
