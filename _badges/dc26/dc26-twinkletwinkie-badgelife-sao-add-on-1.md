---
title: 'TwinkleTwinkie''s Badgelife SAO Add-on #1'
id: dc26-dc26-twinkletwinkie-badgelife-sao-add-on-1
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: TwinkleTwinkie
  url: https://www.tindie.com/stores/twinkletwinkie/
summary: Shitty Add-on for DEF CON 26 badges depicting a terrifying clown whose eyes light up bright yellow, sold assembled on Tindie by TwinkleTwinkie in 2018 and since retired.
functions: Yellow LED eyes light up when the SAO is powered from a host badge or a breadboard.
look:
  colors:
  - yellow
  shape: null
  themes:
  - horror
tech:
  mcu: none
  leds:
    count: 2
    type: discrete (OSRAM TOPLED LY T776-Q2T1-26-Z)
    note: Yellow LEDs form the clown's glowing eyes.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: $20 (1-4 units), $18 each for 5+
  price_usd: 20
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing shows the product as retired, checked 2026-09-07.
  distribution:
  - purchase
  where: Sold assembled by TwinkleTwinkie on Tindie.
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/158664-krusty-the-it-def-con-26-shitty-add-on
  firmware_url: null
  eda_tool: KiCad
links:
- label: www.ebay.com/itm/145940255791
  url: https://www.ebay.com/itm/145940255791
  kind: website
- label: www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1/
  kind: store
  archived: https://web.archive.org/web/20260510025610/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1/
- label: Krusty the IT - DEF CON 26 Shitty Add-on (Hackaday.io)
  url: https://hackaday.io/project/158664-krusty-the-it-def-con-26-shitty-add-on
  kind: hackaday
images:
- file: assets/images/badges/dc26/dc26-twinkletwinkie-badgelife-sao-add-on-1/5b6e0f53fd.jpg
  source: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1/
  credit: TwinkleTwinkie
  caption: The clown SAO with yellow LED eyes
  archived: https://web.archive.org/web/20260510025610/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1/
- file: assets/images/badges/dc26/dc26-twinkletwinkie-badgelife-sao-add-on-1/643a59bf6d.jpg
  source: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1/
  credit: TwinkleTwinkie
  caption: Second product photo of the clown SAO
  archived: https://web.archive.org/web/20260510025610/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://www.ebay.com/itm/145940255791
  title: DEFCON 26 Hacking Conference - 2018 TwinkleTwinkie Badge Add-on Set | eBay
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1/
  title: 'TwinkleTwinkie''s Badgelife SAO Add-on #1 - Tindie'
  accessed: '2026-09-07'
  note: Maker's own store listing; source for description, price, SAO spec, availability (retired), and product photos.
  archived: https://web.archive.org/web/20260510025610/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-1/
- kind: url
  url: https://hackaday.io/project/158664-krusty-the-it-def-con-26-shitty-add-on
  title: Krusty the IT - DEF CON 26 Shitty Add-on - Hackaday.io
  accessed: '2026-09-07'
  note: Documentation link embedded on the Tindie listing itself (missed by the prior research pass). Confirms 2x OSRAM TOPLED LY T776-Q2T1-26-Z LEDs, a 2x2 vertical-header (4-pin/v1) SAO connector, a single 0805 resistor and no MCU, published KiCad project + Gerbers, and approximately 140 units produced. Corrects the body's prior "closed-source" claim.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: Re-verified against the maker's Tindie listing and its embedded Hackaday.io documentation link (missed by the prior pass), which confirms the LED part, SAO header type/version, absence of an MCU, and that KiCad/Gerbers are published. Corrected make_your_own (was null/closed-source, now partial with a hardware_url) and removed the unsupported eBay-resale claim from get_one.where and the body, since the eBay listing returned HTTP 403 on both WebFetch and curl and its content could not be confirmed (its link is kept only as the original intake source, not as evidence of resale details). All remaining populated fields are supported by a source actually read.
last_modified_date: '2026-09-07'
---

TwinkleTwinkie's Badgelife SAO Add-on #1 is a Shitty Add-on made for DEF CON 26 (2018), styled as a menacing clown face whose eyes glow yellow when the SAO is plugged into a compatible host badge or powered from a breadboard at the standard 3.3V SAO spec. It was sold assembled through TwinkleTwinkie's Tindie store for $20 (discounted to $18 each for orders of five or more).

The listing is now marked retired on Tindie. Its own "Documentation" link points to a Hackaday.io project page ("Krusty the IT"), which shows the board uses two OSRAM TOPLED SMD LEDs and a single resistor with no microcontroller, connects via a standard 4-pin (v1) SAO header, and has its KiCad project and Gerbers published.

## Make your own

Hardware files (KiCad project and Gerbers) for this design are published on the maker's Hackaday.io project page, linked above. No separate firmware repository applies, since the board has no MCU.
