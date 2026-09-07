---
title: Charlie Badge
id: other-charlie-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: xBeau
  url: https://hackaday.io/xbeau
summary: 'A hand-etched hobbyist wearable with six charlieplexed LEDs driven by an ATtiny85 and a coin cell, built as the maker''s "first attempt at badgelife."'
functions: 'Lights six discrete LEDs in patterns using charlieplexing (driving six LEDs from three microcontroller pins).'
look:
  colors:
  - green
  shape: null
  themes:
  - learn to solder
tech:
  mcu: ATtiny85
  leds:
    count: 6
    type: discrete
    note: Charlieplexed, individually controllable.
  display: none
  connectivity: []
  battery: coin cell
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/63066-charlie-badge
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/63066-charlie-badge
  url: https://hackaday.io/project/63066-charlie-badge
  kind: hackaday
- label: xBeau on Hackaday.io
  url: https://hackaday.io/xbeau
  kind: social
images:
  - file: assets/images/badges/other/charlie-badge/46a5581ba6.jpg
    source: "https://hackaday.io/project/63066-charlie-badge"
    credit: "xBeau"
    caption: "PCB render of the Charlie Badge showing the charlieplexed LEDs, ATtiny85, and coin cell holder"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/63066-charlie-badge
  title: Charlie Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/63066-charlie-badge
  title: Charlie Badge
  accessed: '2026-09-07'
  note: 'Confirmed maker (xBeau), MCU (ATtiny85), 6 charlieplexed LEDs, coin cell power, KiCad design files, and 2018-02-24 creation date. No pricing, quantity, or firmware source given.'
- kind: url
  url: https://hackaday.io/xbeau
  title: "xBeau's Profile | Hackaday.io"
  accessed: '2026-09-07'
  note: 'Maker is a Noisebridge (SF Bay Area) member; separately made a 2018 Hackaday Superconference badge reverse-engineering project, but that is a different project from Charlie Badge, which is described as a standalone practice piece rather than a con-specific badge.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Not made for a specific convention -- the maker''s own page calls it "a first attempt at ℔adgelife" (a practice/experiment project), dated 2018-02-24, with no event tie-in stated. Left event as "other" since no matching con was named. KiCad hardware files (schematic + PCB, badge20180223.zip) are linked on the project page, but no firmware/code repository was found, so open_source is "partial". No price, quantity made, or availability information exists anywhere on the page.'
last_modified_date: '2026-09-07'
---

The Charlie Badge is a small hobbyist wearable made by xBeau, a Noisebridge hackerspace member in the San Francisco Bay Area, and posted to Hackaday.io on February 24, 2018. It uses charlieplexing -- a technique for driving more LEDs than a microcontroller has spare pins by treating each pin as bidirectional -- to control six discrete LEDs from an ATtiny85, powered by a single coin cell battery. The maker describes it plainly as "a first attempt at badgelife," framing it as a personal exercise in the technique and in designing a badge meant to be reproduced with conductive silver ink rather than a factory PCB process.

Unlike many badgelife entries, the Charlie Badge was not built for a specific convention; the project page ties it to no particular event or year of attendance, and it appears to be a standalone practice board rather than something distributed at a con. The Hackaday.io listing includes a KiCad schematic and PCB layout (packaged as badge20180223.zip) but no firmware source, so it is only partially open source. No pricing, production quantity, or distribution details were published.
