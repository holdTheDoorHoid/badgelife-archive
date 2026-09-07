---
title: Pipscat
id: saintcon-2026-pipscat
layout: badge
parent: Saintcon 2026
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2026
year: 2026
makers:
- name: Pips
  url: https://www.tindie.com/stores/pips/
summary: A cat-shaped SAINTCON minibadge with a single LED, made by Pips.
functions: ''
look:
  colors: []
  shape: cat
  themes:
  - cat
  - animal
tech:
  mcu: none
  leds: 1
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '400'
  availability: unknown
  distribution:
  - free_drop
  - swap
  where: 'Given out or traded by the maker in person; per the maker''s data listing: "Come find me and I will give you one, Come find me and trade with me, At our booth."'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=Pipscat&year=2026
  url: https://minibadge.wiki/?search=Pipscat&year=2026
  kind: website
- label: Pips on Tindie
  url: https://www.tindie.com/stores/pips/
  kind: store
images:
- file: assets/images/badges/saintcon-2026/pipscat/495c93524d.jpg
  source: "https://minibadge.wiki/?search=Pipscat&year=2026"
  credit: "Pips"
  caption: "Pipscat minibadge, front"
- file: assets/images/badges/saintcon-2026/pipscat/46d0c7ea5d.jpg
  source: "https://minibadge.wiki/?search=Pipscat&year=2026"
  credit: "Pips"
  caption: "Pipscat minibadge, back"
contact: {}
notes:
- 'category: Personal; qty made: 400'
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=Pipscat&year=2026
  title: Pipscat
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2026''.'
- kind: url
  url: https://minibadge.wiki/2026.json
  title: MiniBadge Wiki data export (2026.json)
  accessed: '2026-09-07'
  note: 'The site''s search page is a client-rendered SPA with no data baked into the HTML; the underlying JSON export (linked from minibadge.wiki/data/) carries the actual Pipscat record: maker Pips, description "Cat minibadge", soldering "Solder LED, resistor, and legs" (intermediate difficulty, one LED, no MCU), quantity made 400, category Personal, board house JLCPCB, how to acquire, and the front/back/profile image paths. Notably this record''s own conferenceYear field reads 2025, not 2026 (see research.notes).'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check (2026-09-07): re-fetched minibadge.wiki/2026.json directly and confirmed every populated field against the maker''s own JSON record verbatim -- author "Pips", description "Cat minibadge", solderingInstructions "Solder LED, resistor, and legs." (Intermediate), quantityMade 400, category "Personal", boardHouse "JLCPCB", and howToAcquire "Come find me and I will give you one, Come find me and trade with me, At our booth" (matches get_one.where and the free_drop/swap distribution tags). The two saved images were re-downloaded from minibadge.wiki/images/2026/pipscat-front.png and pipscat-back.png and match the local files pixel-dimension-for-dimension (1163x1163 and 1181x1179), confirming both show this badge, front and back. The Pips Tindie store link (tindie.com/stores/pips/) could not be loaded directly (Cloudflare blocks all fetch tools, 403), but the same 2026.json export has another Pips-authored entry ("Minibadge Display Devboard") whose own howToAcquire text states "Purchase from my Tindie store - https://www.tindie.com/stores/pips/", so the maker''s own data confirms this is genuinely their store URL. The claim that Pips is a prolific SAINTCON minibadge maker (Glitch Gallery, Crown Burger, Minibadge Chain, etc.) is confirmed: the same author field appears on 11 entries in 2026.json. The maker''s own data record for this minibadge lists conferenceYear: "2025", while the archive sweep filed it under saintcon-2026 (surfaced via a year=2026 search, sitting in the "2026.json" export). This export file is not cleanly single-year, however: sibling entries by the same maker in the identical file carry conferenceYear "2026" (e.g. Crown Burger) alongside others at "2025" (e.g. Pipscat, Glitch Gallery), so the year field looks like an unreliable/manually-typed value rather than a clean signal either way. Saintcon 2025 already exists as an event id in this archive (_data/events.yml) but there is no independent confirmation of which SAINTCON this cat minibadge was actually carried at. Left event as saintcon-2026 rather than guess; flagging for a human to resolve (possible correction to saintcon-2025). No price was found (the maker gives/trades these rather than selling), and no dedicated hardware/firmware repo, chip, or color info was found beyond "one LED" and "cat" shape/theme from the description and soldering instructions -- these remain correctly blank/unknown rather than guessed.'
last_modified_date: '2026-09-07'
---

Pipscat is a cat-shaped minibadge made by Pips, a prolific minibadge designer active in the SAINTCON minibadge scene (they also made Glitch Gallery, Crown Burger, the Minibadge Chain, and several other minibadges and accessories). It's a simple build: the maker's own instructions call for soldering a single LED, a resistor, and the badge's legs, rated "Intermediate" difficulty. 400 were made, fabricated through JLCPCB.

Pips distributes it in person rather than selling it — the maker's listing says to "come find me and I will give you one" or to trade for it at their conference booth, so it functions as a free giveaway/swap item rather than a store product.

The maker's own data record for this badge lists its conference year as 2025, which conflicts with the saintcon-2026 event this entry currently sits under (the archive's discovery sweep filed it here because it surfaced via a 2026-year search on minibadge.wiki). This should be checked against SAINTCON 2025 records before being treated as confirmed for either year.
