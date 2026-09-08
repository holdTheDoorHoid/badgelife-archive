---
title: SmartAO SAO
id: dc33-smartao-sao
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: Coruscant Ventures
  url: https://coruscantventures.com
  role: design/sale credited to vor_t3x1 (Discord) / u/MorningMother8622 (Reddit)
summary: A companion SAO from Coruscant Ventures that plugs into the top-left slot of their "SAO Many SAOs" host badge to power and drive its perimeter ARGB LEDs.
functions: Supplies power and animation/color control to the ARGB LEDs on the outside edge of the "SAO Many SAOs" badge; without it those LEDs light only in a fixed, uncontrolled state.
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
  price: $30 (was $40)
  price_usd: 30.0
  quantity: ''
  availability: available
  availability_note: Listed "IN STOCK" on the maker storefront as of 2026-09-07; the site's PayPal checkout is broken, so the maker asks buyers to contact them directly via Discord, Reddit, or the site contact form to arrange payment and shipping.
  distribution:
  - purchase
  where: Sold directly by Coruscant Ventures via their storefront (coruscantventures.com); also listed on eBay under the title "SmartAO DEF CON SAO, Rp2040 SAO."
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: coruscantventures.com/defcon-badges/p/smartao-sao
  url: https://coruscantventures.com/defcon-badges/p/smartao-sao
  kind: website
- label: 'eBay: SmartAO DEF CON SAO, Rp2040 SAO'
  url: https://www.ebay.com/itm/178319882205
  kind: store
images:
- file: assets/images/badges/dc33/smartao-sao/34dee4d759.jpg
  source: https://coruscantventures.com/defcon-badges/p/smartao-sao
  credit: Coruscant Ventures
  caption: SmartAO SAO product photo
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- Required to get animated/colored LED behavior on Coruscant Ventures' "SAO Many SAOs" badge (see dc33-sao-and-many-sao-badge and dc33-sao-for-above); this entry covers the SmartAO module itself, sold as a separate product.
status: released
sources:
- kind: url
  url: https://coruscantventures.com/defcon-badges/p/smartao-sao
  title: SmartAO SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc33''. Confirmed maker, price ($30, was $40), in-stock status, broken PayPal checkout, and that it powers the ARGB LEDs on the "SaO MANY SAOs" badge. og:image gave the product photo saved to this entry.'
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
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a standalone product page for the SmartAO SAO itself, distinct from Coruscant Ventures' "SAO Many SAOs" host badge, which already has entries at dc33-sao-and-many-sao-badge and dc33-sao-for-above (both cover the 25-slot carrier board, not this add-on). MCU is given as RP2040 only by the title of an eBay listing that could not otherwise be fetched (403/error on both WebFetch and curl); left as the best available evidence rather than dropped, but flagged here since it is a title-only source. LED count, battery/power draw of the SmartAO board itself, quantity made, dimensions, and open-source status were not stated on the maker's product page or any other source found. There is also an unresearched stub, dc33-sao-for-above-smartao, that appears to describe this same product; left untouched per the one-entry-per-task rule.
last_modified_date: '2026-09-07'
---

The SmartAO SAO is a small companion add-on from Coruscant Ventures, sold separately from the company's "SAO Many SAOs" badge (a DEF CON 33 host board with 25 SAO slots). Plugged into that badge's top-left SAO port, it supplies power and control for the white ARGB LEDs running around the badge's perimeter; without it those LEDs either stay dark or only light in a fixed, uncontrolled way. The maker's storefront and an eBay listing both point to it being built around an RP2040 microcontroller, though the eBay page itself could not be read directly to confirm further detail.

As of this check the SmartAO was listed "IN STOCK" on Coruscant Ventures' Squarespace site for $30 (marked down from $40), but the storefront's PayPal checkout was reported broken; the maker (Discord: vor_t3x1, Reddit: u/MorningMother8622) asks interested buyers to reach out directly to arrange payment and shipping. No hardware or firmware files for the SmartAO specifically were found published; the GitHub repo for the host "SAO Many SAOs" badge does not appear to include the SmartAO's own design.
