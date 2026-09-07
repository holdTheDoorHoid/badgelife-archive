---
title: SmartAO SAO
id: dc33-sao-for-above-smartao
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: Coruscant Ventures
  url: https://coruscantventures.com/defcon-badges
summary: A DEF CON 33 companion SAO from Coruscant Ventures that drives the addressable RGB edge lighting on the maker's own "SAO Many SAOs Badge."
functions: Plugs into the host badge's top-left SAO slot to power and drive its ARGB edge LEDs; without it the badge's edge lights do not animate.
look:
  colors: []
  shape: null
  themes:
  - sao
tech:
  mcu: null
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: "$30 (sale, was $40)"
  price_usd: 30.0
  quantity: ''
  availability: available
  availability_note: 'Listed "IN STOCK," delivery at DEF CON 33, as of 2026-09-07; maker''s PayPal checkout is broken, so buyers are asked to contact them directly via Discord or Reddit to arrange payment.'
  distribution:
  - purchase
  where: Sold directly from the maker's Coruscant Ventures storefront; since the site's checkout is broken, buyers message the maker (Discord vor_t3x1 or Reddit u/MorningMother8622) to arrange payment and shipping.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: coruscantventures.com/defcon-badges/p/smartao-sao
  url: https://coruscantventures.com/defcon-badges/p/smartao-sao
  kind: store
- label: coruscantventures.com/defcon-badges
  url: https://coruscantventures.com/defcon-badges
  kind: website
images:
- file: assets/images/badges/dc33/sao-for-above-smartao/34dee4d759.jpg
  source: "https://coruscantventures.com/defcon-badges/p/smartao-sao"
  credit: "Coruscant Ventures"
  caption: "SmartAO SAO product photo"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- 'This SmartAO SAO is a separate, companion product to Coruscant Ventures'' "SAO Many SAOs Badge" (catalogued as dc33-sao-and-many-sao-badge and dc33-sao-many-saos-already-catalogued-as-dc33-sao-many-saos); it is required to light that badge''s edge LEDs but is sold and listed on its own product page.'
- 'An eBay resale listing title read "SmartAO DEF CON SAO, Rp2040 SAO" (chip not confirmed on the maker''s own product page, so tech.mcu was left blank).'
status: released
sources:
- kind: url
  url: https://coruscantventures.com/defcon-badges
  title: SAO for above / SmartAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc33''.'
- kind: url
  url: https://coruscantventures.com/defcon-badges/p/smartao-sao
  title: SmartAO SAO — Coruscant Ventures
  accessed: '2026-09-07'
  note: Maker's own product page; confirmed name, price ($30 sale / $40 list), in-stock status, that it powers the ARGB LEDs on the SaO MANY SAOs badge, and broken checkout / contact-to-buy details. Product photo saved from this page's og:image.
- kind: url
  url: https://coruscantventures.com/defcon-badges/p/sao-many-saos
  title: SAO Many SAOs Badge DEFCON 33 — Coruscant Ventures
  accessed: '2026-09-07'
  note: Confirms the SmartAO is the companion module for the host badge's edge LEDs.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The sheet-derived title conflated the host badge ("SAO for above") with this companion module ("SmartAO"); retitled to the maker''s own product name for this specific listing, "SmartAO SAO." Chip/MCU, LED count/type, battery, and connector version were not stated on the maker''s product page; a third-party eBay resale listing titled it "SmartAO DEF CON SAO, Rp2040 SAO" but this was not confirmed by the maker, so tech.mcu was left empty rather than guessed. No dedicated hardware/firmware repo or design files were found for the SmartAO itself (the GitHub repo linked from the host badge''s entry covers that badge, not this module). Quantity made was not stated anywhere found.'
last_modified_date: '2026-09-07'
---

Coruscant Ventures' SmartAO is a companion SAO sold alongside the maker's DEF CON 33 "SAO Many SAOs Badge," a 25-slot SAO carrier board. Plugged into the host badge's top-left slot, the SmartAO is what actually drives the addressable RGB LEDs running around that badge's edge; without it, those edge lights stay dark even though the rest of the badge and its other 24 SAO slots work normally.

As of this check the SmartAO is listed in stock at $30 (marked down from $40), with delivery promised at DEF CON 33. Like the host badge's own listing, the storefront's PayPal checkout is broken, so the maker asks interested buyers to message them on Discord or Reddit to arrange payment and shipping directly. No chip, LED, or battery specifications were published on the maker's own product page; a resale listing on eBay described it as an "Rp2040 SAO," but since that detail could not be confirmed from Coruscant Ventures' own materials, it was not carried into the record. No hardware or firmware files specific to the SmartAO were found.
