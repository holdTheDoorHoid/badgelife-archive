---
title: SAO Hat
id: dc26-sao-hat
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/hacker/308303-twinkletwinkie
summary: 'A red "MAGA"-style hat Shitty Add-on whose lettering reads "Make Add-ons Shitty Again" and lights up white, released as TwinkleTwinkie''s DC26 Shitty Add-on #5 for DEF CON 26 (2018), running at 3.3V on the SAO standard with KiCad files and Gerbers published.'
functions: Illuminates the "Make Add-ons Shitty Again" lettering in white LED light when powered.
look:
  colors:
  - red
  - white
  shape: null
  themes:
  - meme
  - pop culture
  - wearable
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing marked "Product Retired" as of 2026-09-07 check; seller noted they were taking a break.
  distribution:
  - purchase
  where: Sold assembled via TwinkleTwinkie's Tindie store; project files also shared on Hackaday.io.
make_your_own:
  open_source: true
  hardware_url: https://hackaday.io/project/159524-sao-hat
  firmware_url: null
  gerbers_url: https://cdn.hackaday.io/files/1595246825074816/SAO_Hat_hackaday.zip
  eda_tool: KiCad
links:
- label: hackaday.io/project/159524-sao-hat
  url: https://hackaday.io/project/159524-sao-hat
  kind: hackaday
  archived: https://web.archive.org/web/20260519083707/https://hackaday.io/project/159524-sao-hat
- label: www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-5
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-5/
  kind: store
  archived: https://web.archive.org/web/20260519051635/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-5/
- label: cdn.hackaday.io/files/1595246825074816/SAO_Hat_hackaday.zip
  url: https://cdn.hackaday.io/files/1595246825074816/SAO_Hat_hackaday.zip
  kind: hackaday
images:
- file: assets/images/badges/dc26/sao-hat/30f5d151bf.jpg
  source: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-5/
  credit: TwinkleTwinkie
  caption: The assembled SAO Hat, a red hat-shaped SAO with glowing white lettering
  archived: https://web.archive.org/web/20260519051635/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-5/
- file: assets/images/badges/dc26/sao-hat/50d4c4ee8d.jpg
  source: https://hackaday.io/project/159524-sao-hat
  credit: TwinkleTwinkie
  caption: The SAO Hat project photo from Hackaday.io
  archived: https://web.archive.org/web/20260519083707/https://hackaday.io/project/159524-sao-hat
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/159524-sao-hat
  title: SAO Hat
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260519083707/https://hackaday.io/project/159524-sao-hat
- kind: url
  url: https://hackaday.io/project/159524-sao-hat
  title: SAO Hat
  accessed: '2026-09-07'
  note: Confirmed maker, event/year (DC26, 2018), white LED lighting, KiCad/Gerbers file availability, and used as source of the project photo.
  archived: https://web.archive.org/web/20260519083707/https://hackaday.io/project/159524-sao-hat
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-5/
  title: 'TwinkleTwinkie''s Badgelife SAO Add-on #5'
  accessed: '2026-09-07'
  note: Confirmed it is a red hat with glowing white "Make Add-ons Shitty Again" lettering, 3.3V SAO power, assembled/pre-built sale, black hot glue over LEDs to prevent light bleed, and that the listing is now retired/no longer available.
  archived: https://web.archive.org/web/20260519051635/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-5/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price and quantity made were not stated on either source; left empty. No LED count or specific chip given (board is passive, driven by the host badge's 3.3V SAO power, no MCU).
last_modified_date: '2026-09-07'
---

TwinkleTwinkie's SAO Hat is the fifth in their "Shitty Add-on" line, released for DEF CON 26 in 2018. It is a small red, hat-shaped PCB that plugs into a badge's SAO header and draws 3.3V power from the host badge. White LEDs light up lettering that reads "Make Add-ons Shitty Again," a play on the political red-hat slogan it visually references.

The add-on was sold pre-assembled through TwinkleTwinkie's Tindie store, with black hot glue applied over the LEDs to keep the light from bleeding through the board. It could also be powered independently on a breadboard for testing. As of this research pass the Tindie listing is marked "Product Retired," with the seller noting they were taking a break from sales; no price or production quantity was published on either the Tindie or Hackaday.io pages.

The design is open source: KiCad project files and Gerbers are published on the project's Hackaday.io page as a downloadable zip, so anyone with SAO fabrication experience can reproduce the board.

## Make your own

1. Download the KiCad project and Gerber files from the Hackaday.io project page.
2. Fabricate the board (send the Gerbers to a PCB manufacturer).
3. Assemble the white LEDs and hot-glue over them to diffuse the light and prevent bleed-through, per the maker's build.
4. Plug into any badge with a standard 3.3V SAO header.
