---
title: Prismatic Shard SAO for DC XXXI badge
id: dc31-prismatic-shard-sao-for-dc-xxxi-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: Cyber Circuitry
  url: https://www.cybercircuitry.com
summary: An unofficial, DEF CON 31-themed electronic "shard" from Cyber Circuitry with onboard games/puzzles, an IR communicator for interacting with other units, and LED lighting effects.
functions: Onboard games and puzzles, a social/interactive IR communicator for talking to other Prismatic Shards, and LED lighting effects.
look:
  colors:
  - white
  - gold
  - black
  shape: shard
  themes:
  - fantasy
  - art
  - puzzle
  form_factor: pcb sao
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - ir
  battery: LIR2032 (included), USB-C charging
  sao_version: null
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: Listed as "Sold Out" on cybercircuitry.com as of 2026-09-07.
  distribution:
  - purchase
  where: Sold directly through the maker's own website, cybercircuitry.com; shipped to DEF CON 31 buyers in July 2023.
links:
- label: www.cybercircuitry.com
  url: https://www.cybercircuitry.com
  kind: website
  archived: https://web.archive.org/web/20260213122552/https://www.cybercircuitry.com
- label: darthdebugger (GitHub)
  url: https://github.com/darthdebugger
  kind: repo
- label: darthdebugger (Twitter/X)
  url: https://twitter.com/darthdebugger
  kind: social
images:
- file: assets/images/badges/dc31/prismatic-shard-sao-for-dc-xxxi-badge/d080ab705c.jpg
  source: https://www.cybercircuitry.com
  credit: Cyber Circuitry
  caption: Prismatic Shard PCB, showing the shard-shaped outline, illustrated artwork, and UPDI programming header
  archived: https://web.archive.org/web/20260213122552/https://www.cybercircuitry.com
contact: {}
notes:
- This one got under my radar. There are still some for sale on the website.
- The sheet note about ongoing sales is now out of date; the maker's site lists the item as "Sold Out."
status: released
sources:
- kind: sheet
  event: dc31
  row: 24
  updated: '2023-06-25'
- kind: url
  url: https://www.cybercircuitry.com
  title: Cyber Circuitry
  accessed: '2026-09-07'
  note: Maker's own product page; confirmed name, description, features (games, puzzles, IR communicator, LED effects, USB-C charging, LIR2032 cell), "Sold Out" status, and two product photos. Also links to the maker's GitHub (darthdebugger) and Twitter/X account.
  archived: https://web.archive.org/web/20260213122552/https://www.cybercircuitry.com
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Only source found is the maker's own single-page website; no Hackaday.io, press, or storefront listing turned up (web search budget for this session was exhausted before a second round of searches could run, so coverage may be thin). Price, quantity made, exact microcontroller, LED type/count, and open-source status are not stated anywhere found. The saved product photo shows a UPDI programming header, which points to a Microchip AVR part (e.g. ATtiny/megaAVR 0- or 1-series), but this is an inference from the board photo, not a maker statement, so tech.mcu is left null. A second product image (lh3.googleusercontent.com ...9sVixOAxPVvoD...) returned HTTP 403 and could not be saved. The maker's GitHub profile shows 2 repositories but its listing is not publicly browsable, so no firmware/hardware repo could be confirmed.
last_modified_date: '2026-09-07'
---

The Prismatic Shard is an unofficial, DEF CON 31–themed electronic badge/SAO made by Cyber Circuitry, styled as a crystalline shard rather than a traditional rectangular board. The maker describes it as built "to give back to that community" of badgelife enthusiasts, and it packs onboard games and puzzles, an infrared communicator meant for interacting with other Shards, and LED lighting effects, all powered by a USB-C-rechargeable LIR2032 cell.

The board's silkscreen carries an original illustration of a woman's face worked into the shard's crystalline facets, picked out in white, gold, and black against the PCB substrate. A visible UPDI programming header on the board suggests a Microchip AVR microcontroller, though the maker's page does not name the specific part, and no exact LED type or count could be confirmed.

Cyber Circuitry sold the Shard directly from its own website with a planned July 2023 shipping window for DEF CON 31 attendees; by the time of this research pass the listing showed "Sold Out." No open-source hardware or firmware files, Hackaday.io project, or third-party press coverage were found to corroborate further technical details.
