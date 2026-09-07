---
title: Badge Crown SAO
id: dc34-badge-crown-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: 000000widow (Brooke's Bytes)
summary: 'A small crown-shaped SAO with three flashing red LEDs standing in for the crown''s jewels; arrives fully soldered and assembled, no soldering or programming required.'
functions: 'Three flashing red LEDs blink when the SAO is powered from a host badge; no other interactivity.'
look:
  colors: [red]
  shape: crown
  themes: [jewelry, minimalist]
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: 'Flashing red LEDs (self-flashing type), driven directly with 3 resistors, no controller chip.'
  display: none
  connectivity: []
  battery: 'powered by host badge'
  sao_version: null
get_one:
  price: '$10'
  price_usd: 10
  quantity: '30'
  availability: sold_out
  availability_note: 'Uberflux listing showed 0 remaining / OUT as of 2026-09-07.'
  distribution: [purchase]
  where: 'Sold via Brooke''s Bytes'' storefront on Uberflux, distributed at the DEF CON 34 Badge Life Village (August 7-8, 2026).'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: uberflux.com/product/WIDOW-badge_crown_SAO
  url: https://uberflux.com/product/WIDOW-badge_crown_SAO
  kind: store
images:
  - file: assets/images/badges/dc34/badge-crown-sao/efb08c5d98.jpg
    source: "https://uberflux.com/product/WIDOW-badge_crown_SAO"
    credit: "Brooke's Bytes (000000widow)"
    caption: "Badge Crown SAO, front view showing three red LEDs"
  - file: assets/images/badges/dc34/badge-crown-sao/018f722bb3.jpg
    source: "https://uberflux.com/product/WIDOW-badge_crown_SAO"
    credit: "Brooke's Bytes (000000widow)"
    caption: "Badge Crown SAO, alternate view"
contact: {}
notes:
- 'Uberflux. $10, status: sold out.'
status: released
sources:
- kind: url
  url: https://uberflux.com/product/WIDOW-badge_crown_SAO
  title: Badge Crown SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://uberflux.com/product/WIDOW-badge_crown_SAO
  title: Badge Crown SAO
  accessed: '2026-09-07'
  note: 'Confirmed product description, event/date (DEF CON 34 Badge Life Village, Aug 7-8, 2026), 30 units sold, $10 price, out of stock, contents (SAO connector, 3 flashing red LEDs, 3 resistors), and pulled product photos.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'No open-source hardware/firmware files found for this item; likely a simple passive/discrete-LED design (no MCU) so there may be no firmware to publish. SAO pin count (v1 vs v2) not stated on the listing. No maker Hackaday/GitHub page found linking back to this specific SAO.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/badge-crown-sao/
---

The Badge Crown SAO is a small conference add-on shaped like a crown, made by Brooke's Bytes (Uberflux storefront handle 000000widow) for the DEF CON 34 Badge Life Village, held August 7-8, 2026. Three flashing red LEDs sit where the crown's jewels would be, lighting up when the SAO is plugged into and powered by a host badge. The board contains just an SAO connector, the three self-flashing LEDs, and three current-limiting resistors — no microcontroller — and it ships fully soldered and assembled, so no soldering or programming is required from the buyer.

The maker sold 30 units through their Uberflux storefront at $10 each; the listing shows the run sold out completely, with zero remaining. No hardware or firmware files were found published for this design, and it is unclear which SAO header/pin standard the connector follows, since the listing does not specify a version.
