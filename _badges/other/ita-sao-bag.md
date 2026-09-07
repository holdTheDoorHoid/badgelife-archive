---
title: ITA SAO BAG
id: other-ita-sao-bag
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: other
year: 2024
makers:
- name: davedarko
  url: https://hackaday.io/davedarko
summary: A hand-sewn canvas display bag for carrying and showing off SAOs, built as an SAO-focused alternative to the pin/plushie-collecting "ITA bag" style popular in fandom circles.
functions: Holds SAOs in 5x5 cm compartments behind a clear protective overlay; two built-in power distribution boards with a Raspberry Pi Pico drive I2C to the mounted SAOs so they can light up while worn.
look:
  colors: []
  shape: null
  themes:
  - wearable
  - hardware tool
tech:
  mcu: RP2040 (Raspberry Pi Pico)
  leds: null
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/197959-ita-sao-bag
  url: https://hackaday.io/project/197959-ita-sao-bag
  kind: hackaday
images:
- file: assets/images/badges/other/ita-sao-bag/df9046fdba.jpg
  source: "https://hackaday.io/project/197959-ita-sao-bag"
  credit: "davedarko"
  caption: "ITA SAO BAG project cover image"
- file: assets/images/badges/other/ita-sao-bag/a9dced87c0.jpg
  source: "https://hackaday.io/project/197959-ita-sao-bag"
  credit: "davedarko"
  caption: "ITA SAO BAG construction detail"
contact: {}
notes:
- Bag/carrier accessory for badges and SAOs, not a badge itself
status: announced
sources:
- kind: url
  url: https://hackaday.io/project/197959-ita-sao-bag
  title: ITA SAO BAG
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/197959-ita-sao-bag
  title: ITA SAO BAG (project page, refetched)
  accessed: '2026-09-07'
  note: Confirms maker (davedarko), build concept, RP2040-based power/I2C distribution boards, welt-pocket-sewn canvas inlay with 44 connector openings for 5x5cm SAO compartments, and clear protective overlay. Project created September 13, 2024; logged as an ongoing build with no completion, price, or distribution announced.
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO
  title: davedarko/Simple-Add-ons-SAO (GitHub)
  accessed: '2026-09-07'
  note: davedarko's SAO repository does not include the ITA SAO BAG design files; the bag itself is not published there.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a personal, ongoing maker project by davedarko (also known for the SAOAO/Supercon Add-On Add-On standard), not a badge produced for a specific convention -- no source names a con it was built for or distributed at, so event is left as "other". No price, quantity, availability, or open-source hardware/firmware files were found; the Hackaday.io log describes work in progress (sewing the inlay, designing power boards) with no stated completion date. tech.mcu and connectivity reflect the Raspberry Pi Pico / I2C distribution boards described for driving the mounted SAOs, not a badge MCU. get_one and make_your_own fields are left empty; nothing on the project page addresses release or file availability.
last_modified_date: '2026-09-07'
---

The ITA SAO BAG is a personal project by Hackaday.io maker davedarko, who is also known in the badgelife scene for creating the SAOAO (Supercon Add-On Add-On) standard. It reimagines the "ITA bag" -- a style of clear-windowed bag popular in fandom communities for displaying pins and plushies -- as a carrier for SAOs (Simple Add-Ons) instead.

The build uses a canvas inlay with 44 hand-sewn, welt-pocket-style openings arranged in 5x5 cm compartments, each meant to hold an SAO behind a clear protective overlay, echoing the modular layout of MOLLE/PALS webbing. Two custom power distribution boards built around a Raspberry Pi Pico route I2C to the mounted SAOs so they can be lit up while worn on the bag.

As of the most recent log update, the project was documented as an ongoing build -- the inlay sewing and power-board design were complete, but no finished bag, price, quantity, or distribution plan had been announced. No repository, gerbers, or firmware for the project were found; it is not listed in davedarko's public SAO GitHub repository.
