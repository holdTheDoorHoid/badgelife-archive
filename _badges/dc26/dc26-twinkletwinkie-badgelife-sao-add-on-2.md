---
title: 'TwinkleTwinkie''s Badgelife SAO Add-on #2'
id: dc26-dc26-twinkletwinkie-badgelife-sao-add-on-2
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
series: Shitty Add-on
makers:
- name: TwinkleTwinkie
  url: https://www.tindie.com/stores/twinkletwinkie/
summary: '"Fat Pika," a Pikachu-styled Shitty Add-on for DEF CON 26 (2018) with a yellow silkscreened PCB and red LED cheeks that light up when powered.'
functions: 'No logic or buttons: the two red LEDs simply light up ("glow") whenever the SAO is powered from the host badge''s 3.3V rail.'
look:
  colors:
  - yellow
  - black
  - red
  shape: null
  themes:
  - pop culture
  - mascot
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Red OSRAM TOPLED (LS T776-P2S1-1-Z) LEDs, salvaged surplus from earlier badge mods, form Pikachu's glowing cheeks.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: $20
  price_usd: 20.0
  quantity: 50+
  availability: sold_out
  availability_note: Tindie listing shows the item as discontinued/out of stock (checked 2026-09-07).
  distribution:
  - purchase
  where: Sold on Tindie by TwinkleTwinkie in 2018; also appeared as a since-expired eBay listing.
make_your_own:
  open_source: 'yes'
  hardware_url: https://hackaday.io/project/158665-fat-pika-def-con-26-shitty-add-on
  firmware_url: null
  eda_tool: KiCad
  gerbers_url: https://cdn.hackaday.io/files/1586656788323360/Fat_Pika_hackaday.zip
  notes: KiCad project and Gerber files are bundled in a single downloadable zip on the Hackaday.io project page.
links:
- label: www.ebay.com/itm/145940255791
  url: https://www.ebay.com/itm/145940255791
  kind: website
- label: www.tindie.com/stores/twinkletwinkie
  url: https://www.tindie.com/stores/twinkletwinkie/
  kind: store
  archived: https://web.archive.org/web/20260503111119/https://www.tindie.com/stores/twinkletwinkie/
- label: TwinkleTwinkie's Badgelife SAO Add-on
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-2/
  kind: store
  archived: https://web.archive.org/web/20260510025609/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-2/
- label: Fat Pika - DEF CON 26 Shitty Add-on (Hackaday.io)
  url: https://hackaday.io/project/158665-fat-pika-def-con-26-shitty-add-on
  kind: hackaday
images:
- file: assets/images/badges/dc26/dc26-twinkletwinkie-badgelife-sao-add-on-2/db2132b077.jpg
  source: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-2/
  credit: TwinkleTwinkie
  caption: 'TwinkleTwinkie''s Badgelife SAO Add-on #2 (Fat Pika), a Pikachu-themed SAO with glowing red LED cheeks'
  archived: https://web.archive.org/web/20260510025609/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-2/
- file: assets/images/badges/dc26/dc26-twinkletwinkie-badgelife-sao-add-on-2/b3999324c9.jpg
  source: https://hackaday.io/project/158665-fat-pika-def-con-26-shitty-add-on
  credit: TwinkleTwinkie
  caption: Fat Pika SAO on Hackaday.io, showing the yellow PCB shaped like Pikachu
contact: {}
notes:
- The Hackaday.io project nicknames the board "Fat Pika."
status: released
sources:
- kind: url
  url: https://www.ebay.com/itm/145940255791
  title: DEFCON 26 Hacking Conference - 2018 TwinkleTwinkie Badge Add-on Set | eBay
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-2/
  title: 'TwinkleTwinkie''s Badgelife SAO Add-on #2 from TwinkleTwinkie on Tindie'
  accessed: '2026-09-07'
  note: 'Maker''s own product listing: title, $20 price, "electrifying yellow rodent with glowing red cheeks" description, package contents (assembled SAO + 2x2 header), discontinued/out-of-stock status, link to Hackaday.io documentation.'
  archived: https://web.archive.org/web/20260510025609/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-2/
- kind: url
  url: https://hackaday.io/project/158665-fat-pika-def-con-26-shitty-add-on
  title: Fat Pika - DEF CON 26 Shitty Add-on | Hackaday.io
  accessed: '2026-09-07'
  note: Confirms DEF CON 26 (2018) event, red OSRAM TOPLED LEDs salvaged from earlier badge mods, 50+ units made, KiCad/Gerber files published in a downloadable zip.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: The original eBay listing (145940255791) no longer resolves (deleted/expired); the Tindie product page and the maker's own Hackaday.io project page confirmed the core facts instead. No quantity price breakdown or exact LED forward-voltage specs were published beyond what is noted above. Series name "Shitty Add-on" reflects the badgelife community term the maker uses for this product line, not a formal series name.
last_modified_date: '2026-09-07'
---

TwinkleTwinkie's "Fat Pika" is the second in their run of numbered "Badgelife SAO Add-on" boards, made for DEF CON 26 in 2018. It is a yellow PCB silkscreened and shaped to evoke Pikachu, with two red LEDs standing in for the character's glowing cheeks. The LEDs were surplus OSRAM TOPLED parts left over from earlier badge modifications, and the whole board was reportedly designed and assembled in a single night. There is no microcontroller or logic on board: the SAO standard's 3.3V supply from the host badge is all it takes to light the cheeks.

TwinkleTwinkie made more than 50 units and sold them on Tindie for $20 each, complete with a 2x2 SAO header (later revisions shipped the header unsoldered so buyers could choose their own power hookup). The Tindie listing is now discontinued/out of stock, and a related eBay listing that had been circulating a "TwinkleTwinkie Badge Add-on Set" no longer resolves. The board is hardware-open: KiCad project files and Gerbers are published together in a zip on the maker's Hackaday.io project page.

## Make your own

The Hackaday.io project page for "Fat Pika" bundles the complete KiCad design (schematic, PCB layout, and Gerber files) in a single zip download. Building one requires two red LEDs (the original used OSRAM TOPLED LS T776-P2S1-1-Z) and a 2x2 SAO-compatible header; no firmware or programming is involved.
