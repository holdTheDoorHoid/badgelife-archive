---
title: Athena's Fortune Badge
id: saintcon-2024-athena-s-fortune-badge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: Mister X
summary: 'A SAINTCON 2024 minibadge from a Sea of Thieves-themed set, featuring a skull-and-crossed-swords emblem, awarded only for completing three of the set''s other faction minibadges.'
functions: 'Lights two LEDs when powered through its minibadge headers; purely decorative, no interactivity beyond that.'
look:
  colors: [black, white, copper]
  shape: hexagon
  themes: [pirate, skull, pop culture]
tech:
  mcu: none
  leds:
    count: 2
    type: null
    note: Two through-hole LEDs, single-pad hand-soldering method
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: [contest]
  where: 'Not sold; given as an exclusive reward for showing proof of completing three of the other Sea of Thieves faction minibadges (Gold Hoarder, Order of Souls, Merchant Alliance, or Reaper''s Bones).'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=Athena%27s%20Fortune%20Badge&year=2024
  url: https://minibadge.wiki/?search=Athena%27s%20Fortune%20Badge&year=2024
  kind: website
images:
- file: assets/images/badges/saintcon-2024/athena-s-fortune-badge/eff52ff32d.png
  source: "https://minibadge.wiki/?search=Athena%27s%20Fortune%20Badge&year=2024"
  credit: "Mister X / minibadge.wiki"
  caption: "Front of Athena's Fortune Badge, part of the Sea of Thieves minibadge set"
- file: assets/images/badges/saintcon-2024/athena-s-fortune-badge/f27aceb14b.png
  source: "https://minibadge.wiki/?search=Athena%27s%20Fortune%20Badge&year=2024"
  credit: "Mister X / minibadge.wiki"
  caption: "Back of Athena's Fortune Badge showing LED and resistor placement"
contact: {}
notes:
- 'category: Personal; rarity: Super Rare'
- 'Beginner-level soldering difficulty per the maker''s instructions: two LEDs and two resistors (single-pad hand-soldering method) plus 4x 2-position headers.'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=Athena%27s%20Fortune%20Badge&year=2024
  title: Athena's Fortune Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2024''.'
- kind: url
  url: https://minibadge.wiki/2024.json
  title: 'MiniBadge Wiki 2024 data (JSON): Athena''s Fortune Badge entry'
  accessed: '2026-09-07'
  note: 'Primary data record behind the search-filtered wiki page; supplied description, maker (Mister X), category (Personal), rarity (Super Rare), soldering instructions and difficulty, how-to-acquire text, and the front/back image filenames.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): verified against the raw minibadge.wiki 2024.json record and the saved front/back images. All facts sourced from the maker-submitted minibadge.wiki community database entry (a community submission form, not the maker''s own site) — treated as the best available primary source per the research guide''s ordering, since no maker storefront, repo, or social post was found. Price, quantity made, board house, and any open-source files are not stated anywhere and are left empty. "quantityMade" in the source data is literally 0, which reads as unset/not reported rather than a real production count, so get_one.quantity is left blank rather than set to 0. LED type/part number not specified beyond "LEDs"; sao_version left as none since minibadge headers are not the standard SAO connector. look.colors/shape/themes are not stated in the JSON text but are directly visible in the saved images (black board, white silkscreen, copper-filled skull, hexagon outline). Removed an unsupported claim that the artwork was "styled after the game''s Reaper''s Bones faction emblem" — the source description frames this badge as a reward for escaping the Reaper''s grasp, not as that faction''s emblem, and no source identifies the skull-and-crossed-swords art as any specific in-game faction crest; the summary/body now describe the art plainly instead. status: released and confidence: medium are carried forward as reasonable but not fully certain — the source confirms a real, distributed minibadge with soldering instructions but does not directly state units were handed out (session''s web-search budget was exhausted before independent corroboration could be sought).'
last_modified_date: '2026-09-07'
---

Athena's Fortune Badge is a SAINTCON 2024 minibadge made by Mister X (Personal category, listed as Super Rare) as part of a Sea of Thieves-themed minibadge set. Its artwork is a skull-and-crossed-swords emblem rendered in black PCB with white silkscreen outline and a copper/brown-filled skull, on a hexagonal board.

The badge is a simple beginner build: two through-hole LEDs and two resistors soldered single-pad style, plus four 2-position headers that connect it to a host badge for power. It has no microcontroller, display, or connectivity of its own — the LEDs simply light when the badge is powered through those headers.

True to its Sea of Thieves theme, the badge was not sold or freely distributed. It was an exclusive reward: to receive it, a SAINTCON attendee had to show proof of completing three of the set's other faction minibadges (Gold Hoarder, Order of Souls, Merchant Alliance, or Reaper's Bones), mirroring the in-game requirement to reach level 50 in three factions to become a Pirate Legend.
