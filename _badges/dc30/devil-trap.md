---
title: Devil's Trap
id: dc30-devil-trap
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: Sqearlsalazar
summary: A pre-assembled SAO shaped like a devil's trap sigil, lit by red LEDs along its pentagram and ring.
functions: Lights up its devil-trap sigil artwork with red LEDs; no other interactivity.
look:
  colors:
  - red
  - black
  shape: circle
  themes:
  - horror
  - occult
tech:
  mcu: none
  leds:
    count: 7
    type: discrete
    note: 7x red 0805 SMD LEDs with 2x 0805 resistors, no driver IC
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: $15
  price_usd: 15.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold on Tindie by Sqearlsalazar; also offered at the Hardware Hacking Village at DEF CON 30
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/sqearlsalazar/devils-trap-defcon-sao
  url: https://www.tindie.com/products/sqearlsalazar/devils-trap-defcon-sao/
  kind: store
images:
- file: assets/images/badges/dc30/devil-trap/bb4f010217.jpg
  source: https://www.tindie.com/products/sqearlsalazar/devils-trap-defcon-sao/
  credit: Sqearlsalazar
  caption: Devil's Trap SAO, red PCB with devil trap sigil in LEDs
contact: {}
notes:
- Sheet listed the title as "Devil Trap"; the maker's own Tindie listing calls it "Devil's Trap," which is used here.
- Sheet price was $20; Tindie lists it at $15.
status: listed
sources:
- kind: sheet
  event: dc30
  row: 55
  updated: '2022-07-28'
- kind: url
  url: https://www.tindie.com/products/sqearlsalazar/devils-trap-defcon-sao/
  title: Devil's Trap DefCon SAO - Red & Black / Silver by sqearlsalazar
  accessed: '2026-09-06'
  note: Maker's Tindie listing; confirms name, components (7x red 0805 LEDs, 2x3 SAO connector, pre-assembled PCB), 2.25"x2.25" size, price $15, and product photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Web searches were unavailable this session (search budget exhausted), so only the maker's own Tindie listing could be consulted; no Hackaday.io, GitHub, or press coverage was found or checked. Tindie listing shows the item marked "on a break" from an older cache date, so current live availability could not be confirmed for 2026; availability left as unknown. No MCU/firmware since the board is a passive LED SAO with no driver chip.
last_modified_date: '2026-09-06'
related:
- dc30-hailsatan-sao-s
- dc30-baphomet-sao
---

The Devil's Trap SAO is a small, pre-assembled add-on board by San Diego maker Sqearlsalazar, sold on Tindie for DEF CON 30 in 2022. The 2.25" square PCB depicts a devil's trap sigil traced out with seven red 0805 SMD LEDs, powered through the badge's SAO header (or an external supply) with no onboard microcontroller — it is a purely passive lighting accessory rather than a programmable badge. Sqearlsalazar describes it as a way to "contain your #badgelife demons," fitting the maker's recurring occult and horror-themed lineup of SAOs from that DEF CON.

The board uses the standard 2x3 DEF CON SAO connector and sold for $15 on Tindie alongside the maker's other pieces from the same year, such as the Baphomet SAO. No hardware or firmware files are published, which is expected for a design with no active electronics.
