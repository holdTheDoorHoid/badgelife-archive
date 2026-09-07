---
title: '#un1eet Shitty Add On'
id: dc26-un1eet-shitty-add-on
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: '|)3vice'
  url: https://hackaday.io/d3vice
summary: 'A beginner-friendly Shitty Add-On that |)3vice made for DEF CON 26 (2018) while learning KiCad: a small ''#un1eet'' (leet) PCB-art board assembled from a single 0805 LED and resistor plus SAO header pins, later revised as the ''un1eet x2'' with a through-hole LED behind the hash symbol and I2C/SPI pads exposed for mods.'
functions: 'Lights a single LED once the resistor and LED are hand-soldered on; the x2 revision exposes I2C and SPI pads for further mods.'
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
  - text
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single 0805 SMD LED (through-hole LED behind the hash symbol on the un1eet x2 revision).
  display: null
  connectivity:
  - i2c
  - spi
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: 'Sold as an assemble-it-yourself kit through the maker''s Tindie store (dMaker); exact price and quantity not stated on the pages checked.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/160043-un1eet-shitty-add-on
  url: https://hackaday.io/project/160043-un1eet-shitty-add-on
  kind: hackaday
- label: hackaday.io/project/160043/instructions
  url: https://hackaday.io/project/160043/instructions
  kind: hackaday
- label: www.tindie.com/stores/dMaker
  url: https://www.tindie.com/stores/dMaker/
  kind: store
images:
  - file: assets/images/badges/dc26/un1eet-shitty-add-on/6566874adb.jpg
    source: "https://hackaday.io/project/160043-un1eet-shitty-add-on"
    credit: "|)3vice"
    caption: "The #un1eet Shitty Add-On PCB"
  - file: assets/images/badges/dc26/un1eet-shitty-add-on/0e5f6fe2cb.jpg
    source: "https://hackaday.io/project/160043-un1eet-shitty-add-on"
    credit: "|)3vice"
    caption: "The #un1eet Shitty Add-On assembled on a badge"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/160043-un1eet-shitty-add-on
  title: '#un1eet Shitty Add On'
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/160043-un1eet-shitty-add-on
  title: '#un1eet Shitty Add On (project page)'
  accessed: '2026-09-07'
  note: 'Confirmed maker, event/year (DEF CON 26, 2018), that it is a learning-focused SAO with an SMD LED and 0805 resistor, KiCad/Inkscape design tools, and sale via Tindie.'
- kind: url
  url: https://hackaday.io/project/160043/instructions
  title: '#un1eet Shitty Add On - instructions'
  accessed: '2026-09-07'
  note: 'Assembly steps for the LED, 0805 resistor, and SAO headers; confirms the un1eet x2 revision has a through-hole LED behind the hash symbol and exposed I2C/SPI pads.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The Tindie store page (tindie.com/stores/dMaker) returned a Cloudflare challenge page and could not be read, so price, quantity made, and current availability are unknown. No mcu is used (the board is a passive LED+resistor circuit); tech.mcu set to none accordingly.'
last_modified_date: '2026-09-07'
---

The #un1eet Shitty Add-On is a deliberately simple, learning-focused SAO that |)3vice designed for DEF CON 26 in 2018 while first picking up KiCad. The board is a small piece of PCB art spelling out "#un1eet" (a leetspeak pun), populated with just a single 0805 SMD LED and a matching resistor soldered on by the buyer, plus the standard SAO header pins to plug into a badge. The maker's own instructions frame soldering mistakes as part of the fun, coining the phrase "Gleaming the Circuit" for parts damaged along the way, and note that replacement SMD components cost only a couple of dollars if something goes wrong.

A later revision, the "un1eet x2," swaps in a through-hole LED mounted behind the hash symbol and exposes I2C and SPI pads so more experienced builders can extend the board. The kits were sold assembled-to-order through the maker's Tindie store (dMaker); the storefront could not be checked directly during this research (it returned a Cloudflare bot-check page), so pricing, quantity produced, and whether it is still available are unknown.

## Make your own

The maker's Hackaday.io project page hosts the write-up and step-by-step instructions (soldering the resistor, then the LED, then the SAO headers), but no linked Gerbers, schematic, or firmware repository were found; design files may exist only on the maker's own systems.
