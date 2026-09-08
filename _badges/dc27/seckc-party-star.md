---
title: DefCon 27 SecKC Party Star
id: dc27-seckc-party-star
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: other
event: dc27
year: 2019
makers:
- name: BadgePirates
  url: https://github.com/BadgePiratesLLC
summary: A star-shaped LED party badge BadgePirates made for the SecKC party at DEF CON 27; the units later resold on Tindie were leftover stock in various broken states.
functions: 'Intended to blink LED "bling" patterns; the badge''s repo describes it as a Party Star variant alongside the main SecKC DC27 badge.'
look:
  colors: []
  shape: star
  themes:
  - party
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $4.99
  price_usd: 4.99
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: 'Originally distributed at the SecKC party at DEF CON 27 (2019); a small leftover stock (9 "broken" soldered units, 8 bare PCBs) was later resold by BadgePirates on Tindie in 2021.'
make_your_own:
  open_source: null
  hardware_url: https://github.com/BadgePiratesLLC/DefCon_SecKCPartyStar_27
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/badgepirates/defcon-27-seckc-party-star
  url: https://www.tindie.com/products/badgepirates/defcon-27-seckc-party-star/
  kind: store
- label: github.com/BadgePiratesLLC/DefCon_SecKCPartyStar_27
  url: https://github.com/BadgePiratesLLC/DefCon_SecKCPartyStar_27
  kind: repo
images:
- file: assets/images/badges/dc27/seckc-party-star/a9dbac7151.jpg
  source: "https://www.tindie.com/products/badgepirates/defcon-27-seckc-party-star/"
  credit: "BadgePirates"
  caption: "SecKC Party Star badges, non-functional leftover units offered for resale"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 4).
- 'Tindie listing does not name a functional MCU/LED spec; the badge''s own GitHub repo (BadgePiratesLLC/DefCon_SecKCPartyStar_27, archived 2023-10-17) has minimal README content and no schematics/BOM visible via the page fetch, so tech.* fields are left empty.'
- 'This is a distinct item from dc27-seckc-badge-dc27 (the 645-LED "LED Wars" main SecKC DC27 badge) and from dc27-seckc-defcon-party-badge-sao; BadgePirates'' own catalog page (docs.badgepirates.com/catalog) lists the Party Star as "a Party Star variant" alongside the main DC27 badge, so it appears to be a companion item from the same event rather than a duplicate.'
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/badgepirates/defcon-27-seckc-party-star/
  title: DefCon 27 SecKC Party Star
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run4-spotted); event read as ''dc27''.'
- kind: url
  url: https://github.com/BadgePiratesLLC/DefCon_SecKCPartyStar_27
  title: 'BadgePiratesLLC/DefCon_SecKCPartyStar_27 - GitHub'
  accessed: '2026-09-08'
  note: 'Maker''s own repo for the badge; confirms it as a Party Star badge for the DEF CON 27 SecKC party, archived Oct 2023. No technical specs or gerbers visible in README.'
- kind: url
  url: https://docs.badgepirates.com/catalog/
  title: 'Catalog - BadgePirates Documents'
  accessed: '2026-09-08'
  note: 'Confirms the Party Star as a distinct variant alongside the main DC27 SecKC badge; no further detail given.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, maker-made item (not just a search snippet): BadgePirates'' Tindie listing and their own GitHub repo both describe it. Could not confirm MCU, LED count/type, display, connectivity, battery, quantity originally made, or whether hardware/firmware files are actually published (the repo exists but its README gave no technical detail via the page fetch used). Left those fields empty rather than guess. Two photos of the physical item were attempted from the Tindie gallery; only one (a small 114x76 thumbnail, the largest reachable without a valid Tindie image-proxy signature) downloaded successfully — the other returned HTTP 400.'
last_modified_date: '2026-09-08'
---

BadgePirates, the Kansas City-based badge collective behind SecKC's DEF CON presence, made the Party Star as a companion piece to their main "LED Wars" SecKC badge for DEF CON 27 (2019) — a star-shaped board meant to light up at the SecKC party. It's referenced in BadgePirates' own project catalog as "a Party Star variant" alongside that year's flagship 645-LED badge, with its own now-archived GitHub repository.

In 2021, BadgePirates resold a small stash of leftover stock on Tindie: nine "broken" units with components still soldered on and eight bare PCBs with parts removed, priced at $4.99 each and pitched more as add-on novelty/repair items than working badges, since the listing states the LEDs no longer blink on the units sold. No technical specifications (MCU, LED count/type, power) could be confirmed from the sources checked.
