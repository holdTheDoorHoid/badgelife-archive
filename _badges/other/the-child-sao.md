---
title: The Child SAO
id: other-the-child-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2021
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/hacker/308303-twinkletwinkie
summary: A Grogu (The Child from The Mandalorian) themed Simple Add-On on a four-layer PCB that uses four 0807 random-flashing RGB LEDs to light up the area behind the character.
functions: Four RGB LEDs positioned around the character flash randomly; no other interactive functions.
look:
  colors:
  - green
  - white
  shape: null
  themes:
  - tv
  - pop culture
  - sci-fi
tech:
  mcu: none
  leds:
    count: 4
    type: RGB
    note: 0807 package, random-flashing (self-contained blinking RGB LEDs, no driver chip)
  display: null
  connectivity: []
  battery: null
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold on Tindie by TwinkleTwinkie; the listing was live from mid-2021 and the shop is now retired ("This seller is taking a break").
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/186283-the-child-sao
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/186283-the-child-sao
  url: https://hackaday.io/project/186283-the-child-sao
  kind: hackaday
- label: hackaday.io/twinkletwinkie
  url: https://hackaday.io/twinkletwinkie
  kind: hackaday
  archived: https://web.archive.org/web/20260523064136/https://hackaday.io/twinkletwinkie
- label: www.tindie.com/products/twinkletwinkie/twinkletwinkies-the-child-sao
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-the-child-sao/
  kind: store
  archived: https://web.archive.org/web/20260506214130/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-the-child-sao/
images:
- file: assets/images/badges/other/the-child-sao/43f74c0334.jpg
  source: https://hackaday.io/project/186283-the-child-sao
  credit: TwinkleTwinkie
  caption: The Child SAO, front view
- file: assets/images/badges/other/the-child-sao/6521929861.jpg
  source: https://hackaday.io/project/186283-the-child-sao
  credit: TwinkleTwinkie
  caption: The Child SAO, lit up
- file: assets/images/badges/other/the-child-sao/c9f9dc57ae.jpg
  source: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-the-child-sao/
  credit: TwinkleTwinkie
  caption: The Child SAO, assembled with green PCB and RGB LEDs
  archived: https://web.archive.org/web/20260506214130/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-the-child-sao/
- file: assets/images/badges/other/the-child-sao/c4a2a35c82.jpg
  source: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-the-child-sao/
  credit: TwinkleTwinkie
  caption: The Child SAO, alternate view
  archived: https://web.archive.org/web/20260506214130/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-the-child-sao/
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- No specific convention or event is named on the Tindie listing; the entry is filed under "other" pending a source that ties it to a particular con.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/186283-the-child-sao
  title: The Child SAO | Hackaday.io
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/186283-the-child-sao
  title: The Child SAO | Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed description ("Uses 4 0807 Random Flashing RGBs to light up the area behind Grogu"), 4-layer PCB, design file TheChild_4L_2021-06-10-2138.zip, project logged 2022-07-08, and pulled gallery photos.
- kind: url
  url: https://hackaday.io/twinkletwinkie
  title: TwinkleTwinkie | Hackaday.io
  accessed: '2026-09-07'
  note: Maker profile; confirmed TwinkleTwinkie as the creator and their pattern of badgelife/SAO/shitty-add-on projects, but the profile does not separately list an event/year for this item.
  archived: https://web.archive.org/web/20260523064136/https://hackaday.io/twinkletwinkie
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-the-child-sao/
  title: The Child SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''unknown (product dated 2021-06)''.'
  archived: https://web.archive.org/web/20260506214130/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-the-child-sao/
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-the-child-sao/
  title: The Child SAO product page
  accessed: '2026-09-07'
  note: Confirmed maker location (Duluth, Georgia), theme/character inspiration, 4-layer PCB with green solder mask, 4 RGB LEDs, SAO v2 compatibility, 3.3V power, and that the listing is now retired/sold out. Listing timestamps place the product images at 2021-06-29.
  archived: https://web.archive.org/web/20260506214130/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-the-child-sao/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The Hackaday.io project page and the maker's profile do not name a specific convention this SAO was made for or sold at, so event is left as other. The downloadable design file is dated 2021-06-10 (matching the entry's existing year of 2021) but the project itself was posted/logged 2022-07-08; no price, quantity made, or distribution channel is stated anywhere in the sources found. Hardware design files (a 4-layer KiCad/Gerber-style zip) are published on the project page, but no firmware is applicable (LEDs are self-flashing, no MCU) and no separate firmware repo was found, so open_source is marked partial rather than yes. Merged with duplicate entry 'The Child SAO' (other-the-child-sao-2).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/the-child-sao-2/
---

The Child SAO is a Simple Add-On by TwinkleTwinkie depicting Grogu, the character widely known as "Baby Yoda" from The Mandalorian. The board is a four-layer PCB, and its lighting comes from four 0807-package RGB LEDs that flash in a random pattern to illuminate the area behind the character artwork — the LEDs are self-contained blinkers rather than being driven by a microcontroller, so the SAO has no onboard MCU.

TwinkleTwinkie is a prolific badgelife creator on Hackaday.io, known for a series of DEF CON "shitty add-ons" (Mad Cat, Fat Pika, Big Green) and other SAOs and badges. The Child SAO's project page does not name a specific convention it was built for or sold at, and the design files bundle (dated June 2021) predates the project's Hackaday.io posting in July 2022, so it is unclear whether it debuted at a particular event or was released independently. Hardware design files are published on the project page for anyone who wants to reproduce the board; no information on price, production quantity, or how it was distributed was found.

## Notes merged from the duplicate entry "The Child SAO"

TwinkleTwinkie's "The Child SAO" is a Simple Add-On shaped as the maker's own cartoonish take on Grogu ("The Child") from The Mandalorian. It is built as a 4-layer PCB with green solder mask and white silkscreen, and carries four RGB LEDs around the character that flash in a fast, random pattern. The board is compatible with the SAO v2 standard (and backward-compatible with the original SAO standard) and runs on 3.3V.

The badge was sold individually on Tindie, with product photos dated to late June 2021. No specific convention or badge-life event is named on the listing, and no microcontroller, price, or production quantity is disclosed. The listing is now retired, with the Tindie shop noting the seller "is taking a break"; the storefront otherwise shows TwinkleTwinkie as an established SAO maker with hundreds of completed orders across other designs.
