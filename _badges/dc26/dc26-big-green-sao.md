---
title: Big Green
id: dc26-dc26-big-green-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: Twinkle Twinkie
  url: https://hackaday.io/twinkletwinkie
summary: A simple green-LED Shitty Add-On by Twinkle Twinkie for DEF CON 26 (2018), their third SAO produced and the first made without manufacturing problems, using two OSRAM reverse-gullwing green LEDs, one 10-ohm resistor and a 2x2 SAO header, with decorative silkscreen text over exposed copper-free areas on the back.
functions: No interactive functions; LEDs simply light up when powered via the SAO header, resembling a pair of glowing green eyes.
look:
  colors:
  - green
  - black
  shape: null
  themes:
  - minimalist
tech:
  mcu: none
  leds:
    count: 2
    type: reverse-mount
    note: Two OSRAM LG T770-K1M2-1-Z reverse gullwing green LEDs with a single 10-ohm 0805 resistor; no driver IC.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Checked 2026-09-07: Tindie listing shows "This product is no longer available for sale."'
  distribution:
  - purchase
  where: Sold assembled through Twinkle Twinkie's Tindie shop.
make_your_own:
  open_source: true
  hardware_url: https://hackaday.io/project/159522-big-green
  firmware_url: null
  gerbers_url: null
  bom_url: null
  eda_tool: KiCad
  license: null
  fab_url: null
  notes: KiCad project and Gerbers distributed as a "Big_Green_hackaday.zip" download linked from the Hackaday.io project page.
links:
- label: hackaday.io/project/159522-big-green
  url: https://hackaday.io/project/159522-big-green
  kind: hackaday
  archived: https://web.archive.org/web/20260512165604/https://hackaday.io/project/159522-big-green
- label: www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-3
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-3/
  kind: store
  archived: https://web.archive.org/web/20260510025609/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-3/
images:
- file: assets/images/badges/dc26/dc26-big-green-sao/4588903345.jpg
  source: https://hackaday.io/project/159522-big-green
  credit: Twinkle Twinkie
  caption: Big Green SAO PCB
  archived: https://web.archive.org/web/20260512165604/https://hackaday.io/project/159522-big-green
- file: assets/images/badges/dc26/dc26-big-green-sao/7cf761c15c.jpg
  source: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-3/
  credit: Twinkle Twinkie
  caption: Big Green assembled SAO, green LED eyes lit
  archived: https://web.archive.org/web/20260510025609/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-3/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/159522-big-green
  title: Big Green
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260512165604/https://hackaday.io/project/159522-big-green
- kind: url
  url: https://hackaday.io/project/159522-big-green
  title: Big Green - Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed maker, event/year (DEF CON 26, 2018, created July 2018), LED/resistor/header BOM, and that it was TwinkleTwinkie's first board fabbed by JLCPCB without production issues; source of the KiCad/Gerbers download and a project photo.
  archived: https://web.archive.org/web/20260512165604/https://hackaday.io/project/159522-big-green
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-3/
  title: TwinkleTwinkie's Badgelife SAO Add-on
  accessed: '2026-09-07'
  note: Confirmed it was sold assembled, describes it as a green-eyed alien-style SAO on the 3.3V SAO standard, and that the listing is now sold out; source of a product photo.
  archived: https://web.archive.org/web/20260510025609/https://www.tindie.com/products/twinkletwinkie/twinkletwinkies-badgelife-sao-add-on-3/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No price or quantity-made figures were published on either source, so those fields are left empty. The Tindie listing's own product copy calls it a decorative "green alien" design, which fits the LED-eyes look described in the sheet-derived summary; both sources agree on maker and DEF CON 26 origin.
last_modified_date: '2026-09-07'
---

Big Green is a minimal Shitty Add-On (SAO) made by Twinkle Twinkie for DEF CON 26 in 2018. It carries just two OSRAM reverse-gullwing green LEDs and a single 10-ohm resistor wired to a 2x2 SAO header, so the whole board lights up as a pair of glowing green eyes the moment it draws power from a host badge — there is no microcontroller or driver IC involved. The back of the board uses decorative silkscreen text over the areas left free of copper.

It was the third SAO Twinkle Twinkie produced, and notable to them as the first to come back from fabrication without any production problems; the Hackaday.io project page credits JLCPCB's silkscreen quality specifically. The maker sold it assembled through their Tindie shop, where it is now listed as sold out. KiCad source files and Gerbers are available as a downloadable zip from the Hackaday.io project page, so the design remains open for anyone who wants to build their own.

## Make your own

The Hackaday.io project page (https://hackaday.io/project/159522-big-green) links to a "Big_Green_hackaday.zip" download containing the KiCad project and Gerber files. No firmware is involved since the board is a passive LED circuit powered entirely by the host badge's SAO header.
