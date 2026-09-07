---
title: Kupo! - DC27 SAO
id: dc27-dc27-kupo-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/twinkletwinkie
summary: A Final Fantasy Moogle-shaped Shitty Add-on made by TwinkleTwinkie for DEF CON 27 in 2019, with four upside-down-mounted 1206 LEDs (three in the wings, one in the bobble) and two resistors; Gerber files are attached to the project page.
functions: The bobble glows red and the wing glows pink/pink when powered; no other interactivity.
look:
  colors:
  - red
  - pink
  shape: null
  themes:
  - pop culture
  - video game
tech:
  mcu: none
  leds:
    count: 4
    type: 1206 (reverse-mount)
    note: 3 LEDs in the wings, 1 in the bobble; two resistors on the board
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listing checked 2026-09-07: "This product is no longer available for sale;" seller is on a break from Tindie.'
  distribution:
  - purchase
  where: Sold assembled via the maker's Tindie store (TwinkleTwinkie); no longer listed as of 2026-09-07.
make_your_own:
  open_source: partial
  hardware_url: https://cdn.hackaday.io/files/1653177072922528/Mog_20190328-0040.zip
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/165317-kupo-dc27-sao
  url: https://hackaday.io/project/165317-kupo-dc27-sao
  kind: hackaday
  archived: https://web.archive.org/web/20260119110921/https://hackaday.io/project/165317-kupo-dc27-sao
- label: cdn.hackaday.io/files/1653177072922528/Mog_20190328-0040.zip
  url: https://cdn.hackaday.io/files/1653177072922528/Mog_20190328-0040.zip
  kind: hackaday
- label: hackaday.io/project/165317/gallery
  url: https://hackaday.io/project/165317/gallery
  kind: hackaday
- label: TwinkleTwinkie's "Kupo!" Badge SAO (Tindie)
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-kupo-badge-sao/
  kind: store
  archived: https://web.archive.org/web/20260519051612/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-kupo-badge-sao/
images:
- file: assets/images/badges/dc27/dc27-kupo-sao/af0e2a77e4.jpg
  source: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-kupo-badge-sao/
  credit: TwinkleTwinkie
  caption: Assembled Kupo! SAO, moogle-shaped PCB with LEDs lit
  archived: https://web.archive.org/web/20260519051612/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-kupo-badge-sao/
- file: assets/images/badges/dc27/dc27-kupo-sao/b04da1b213.jpg
  source: https://hackaday.io/project/165317/gallery
  credit: TwinkleTwinkie
  caption: Kupo! SAO PCB, moogle shape
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/165317-kupo-dc27-sao
  title: Kupo! - DC27 SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260119110921/https://hackaday.io/project/165317-kupo-dc27-sao
- kind: url
  url: https://hackaday.io/project/165317/gallery
  title: Kupo! - DC27 SAO (gallery)
  accessed: '2026-09-07'
  note: Confirmed gallery photo URLs used for saved images.
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-kupo-badge-sao/
  title: TwinkleTwinkie's "Kupo!" Badge SAO
  accessed: '2026-09-07'
  note: Storefront listing; confirmed SAO v1.69bis compatibility, LED colors (bobble red, wing pink), and that it is sold assembled and no longer available for sale.
  archived: https://web.archive.org/web/20260519051612/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-kupo-badge-sao/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's own Hackaday project page and Tindie storefront both confirm the core facts. Price and quantity made are not stated anywhere found. The Hackaday summary calls the character a "Moggle," which is the maker's own spelling for the Final Fantasy Moogle.
last_modified_date: '2026-09-07'
---

TwinkleTwinkie's "Kupo!" is a Shitty Add-On shaped like a Moogle, the winged mascot creature from Square Enix's Final Fantasy series, made for DEF CON 27 in 2019. The board is passive: four upside-down-mounted 1206 LEDs (three set into the wings, one in the character's signature bobble) are wired through two resistors directly off the SAO's 3.3V rail, so the bobble glows red and the wings glow pink whenever the SAO is powered by a host badge — no microcontroller on board.

The maker published Gerber files for the board on the Hackaday.io project page, making the hardware design available to build from, though no firmware or BOM/schematic source files were found. TwinkleTwinkie also sold it assembled through their Tindie storefront, compatible with both the original SAO standard and the newer v1.69bis 6-pin header. As of this check the Tindie listing is no longer available for purchase; the seller's shop is marked as on a break. Price and production quantity were not stated in any source found.

## Make your own

Gerber files (`Mog_20190328-0040.zip`) are attached to the Hackaday.io project page and can be sent directly to a PCB fabricator; no firmware is needed since the board is a passive LED circuit powered from the SAO header.
