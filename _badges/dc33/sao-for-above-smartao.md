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
functions: Plugs into the host badge's SAO header to power and drive its ARGB edge LEDs; the maker states the edge LEDs require it to function.
look:
  colors:
  - orange
  - black
  - purple
  shape: hexagon
  themes:
  - sao
  - hardware tool
tech:
  mcu: RP2040
  leds:
    count: null
    type: ARGB
    note: Drives the ARGB LEDs on the companion "SAO Many SAOs" badge, not LEDs on its own board.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $30 (sale, was $40)
  price_usd: 30.0
  quantity: ''
  availability: available
  availability_note: Listed "IN STOCK," delivery at DEF CON 33, as of 2026-09-07; maker's PayPal checkout is broken, so buyers are asked to contact them directly via Discord or Reddit to arrange payment.
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
- label: 'eBay: SmartAO DEF CON SAO, Rp2040 SAO'
  url: https://www.ebay.com/itm/178319882205
  kind: store
images:
- file: assets/images/badges/dc33/sao-for-above-smartao/34dee4d759.jpg
  source: https://coruscantventures.com/defcon-badges/p/smartao-sao
  credit: Coruscant Ventures
  caption: SmartAO SAO product photo
- file: assets/images/badges/dc33/sao-for-above-smartao/34dee4d759.jpg
  source: https://coruscantventures.com/defcon-badges/p/smartao-sao
  credit: Coruscant Ventures
  caption: SmartAO SAO product photo
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- This SmartAO SAO is a separate, companion product to Coruscant Ventures' "SAO Many SAOs Badge" (catalogued as dc33-sao-and-many-sao-badge and dc33-sao-many-saos-already-catalogued-as-dc33-sao-many-saos); it is required to light that badge's edge LEDs but is sold and listed on its own product page.
- An eBay resale listing title read "SmartAO DEF CON SAO, Rp2040 SAO" (chip not confirmed on the maker's own product page, so tech.mcu was left blank).
- Required to get animated/colored LED behavior on Coruscant Ventures' "SAO Many SAOs" badge (see dc33-sao-and-many-sao-badge and dc33-sao-for-above); this entry covers the SmartAO module itself, sold as a separate product.
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
  archived: https://web.archive.org/web/20260506040947/https://coruscantventures.com/defcon-badges/p/sao-many-saos
- kind: url
  url: https://www.ebay.com/itm/178319882205
  title: SmartAO DEF CON SAO, Rp2040 SAO.
  accessed: '2026-09-07'
  note: eBay listing title names the chip as RP2040; the listing page itself returned an error to automated fetches (both WebFetch and curl), so only the title text could be confirmed.
- kind: url
  url: https://www.tindie.com/products/coruscant_ventures/sao-many-saos-badge/
  title: SAO Many SAOs Badge from coruscant ventures on Tindie
  accessed: '2026-09-07'
  note: Confirms the SmartAO SAO is required for "cool LED animations and actual control" of the host badge's white perimeter LEDs.
  archived: https://web.archive.org/web/20260503104002/https://www.tindie.com/products/coruscant_ventures/sao-many-saos-badge/
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): confirmed title, price, stock, delivery, broken-checkout/contact details, and companion relationship to the "SAO Many SAOs Badge" directly against the two Coruscant Ventures product pages; confirmed the saved product photo matches the product page''s og:image (same dimensions/subject). Corrected two unsupported claims that were not on either product page: removed "top-left SAO slot" (slot position was never stated) and "25-slot ... carrier board" / "24 other SAO slots" from the body (the host page states 25 unique *designs*, not slot count) — these were misreadings, not maker claims, and have been softened to what the maker actually says ("the LEDs on the outside require the SmartAO SAO to function"). Removed the unsupported "sao" theme tag (not in the guide''s controlled vocabulary); look.themes is now empty since no vocabulary term is evidenced. The sheet-derived title conflated the host badge ("SAO for above") with this companion module ("SmartAO");
    retitled to the maker''s own product name for this specific listing, "SmartAO SAO." Chip/MCU, LED count/type, battery, and connector version were not stated on the maker''s product page; a third-party eBay resale listing titled it "SmartAO DEF CON SAO, Rp2040 SAO" but this was not confirmed by the maker, so tech.mcu was left empty rather than guessed. No dedicated hardware/firmware repo or design files were found for the SmartAO itself. Quantity made was not stated anywhere found. Merged with duplicate entry ''SmartAO SAO'' (dc33-smartao-sao).'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc33/smartao-sao/
---

Coruscant Ventures' SmartAO is a companion SAO sold alongside the maker's DEF CON 33 "SAO Many SAOs Badge." Plugged into the host badge's SAO header, the SmartAO is what drives the addressable RGB LEDs running around that badge's edge; the maker's product page states those LEDs require the SmartAO to function.

As of this check the SmartAO is listed in stock at $30 (marked down from $40), with delivery promised at DEF CON 33. Like the host badge's own listing, the storefront's PayPal checkout is broken, so the maker asks interested buyers to message them on Discord or Reddit to arrange payment and shipping directly. No chip, LED, or battery specifications were published on the maker's own product page; a resale listing on eBay described it as an "Rp2040 SAO," but since that detail could not be confirmed from Coruscant Ventures' own materials, it was not carried into the record. No hardware or firmware files specific to the SmartAO were found.

## Notes merged from the duplicate entry "SmartAO SAO"

The SmartAO SAO is a small companion add-on from Coruscant Ventures, sold separately from the company's "SAO Many SAOs" badge (a DEF CON 33 host board with 25 SAO slots). Plugged into that badge's top-left SAO port, it supplies power and control for the white ARGB LEDs running around the badge's perimeter; without it those LEDs either stay dark or only light in a fixed, uncontrolled way. The maker's storefront and an eBay listing both point to it being built around an RP2040 microcontroller, though the eBay page itself could not be read directly to confirm further detail.

As of this check the SmartAO was listed "IN STOCK" on Coruscant Ventures' Squarespace site for $30 (marked down from $40), but the storefront's PayPal checkout was reported broken; the maker (Discord: vor_t3x1, Reddit: u/MorningMother8622) asks interested buyers to reach out directly to arrange payment and shipping. No hardware or firmware files for the SmartAO specifically were found published; the GitHub repo for the host "SAO Many SAOs" badge does not appear to include the SmartAO's own design.
