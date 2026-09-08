---
title: BALCCon 2016 Badge
id: other-balccon-2016-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2016
makers:
- name: Voja Antonic
  url: https://hackaday.io/voja-antonic
summary: A conference badge for BalCCon0x7DB (2016, Novi Sad, Serbia) with synchronized infrared LED patterns, a built-in TV-B-Gone, and a USB password manager.
functions: Runs pre-defined LED patterns that play at random; when two or more badges see each other over an infrared port they sync up and play the same pattern together. Also includes a TV-B-Gone universal remote (based on Mitch Altman's original design) and a password manager that stores up to 10 passwords (15-20 characters each) and types them out over USB as a HID keyboard.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: null
  leds:
    count: 13
    type: null
    note: 12 individual red/green/blue LEDs plus one RGB LED in the center
  display: null
  connectivity:
  - ir
  - usb
  battery: null
  sao_version: none
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
- label: hackaday.io/project/13300-balccon-2016-badge
  url: https://hackaday.io/project/13300-balccon-2016-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260616190520/https://hackaday.io/project/13300-balccon-2016-badge
images:
- file: assets/images/badges/other/balccon-2016-badge/a6089f2c48.jpg
  source: https://hackaday.io/project/13300-balccon-2016-badge
  credit: Voja Antonic
  caption: BalCCon 2016 badge PCB
  archived: https://web.archive.org/web/20260616190520/https://hackaday.io/project/13300-balccon-2016-badge
- file: assets/images/badges/other/balccon-2016-badge/59862b3dc0.jpg
  source: https://hackaday.io/project/13300-balccon-2016-badge
  credit: Voja Antonic
  caption: BalCCon 2016 badge detail
  archived: https://web.archive.org/web/20260616190520/https://hackaday.io/project/13300-balccon-2016-badge
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/13300-balccon-2016-badge
  title: BALCCon 2016 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''BalCCon 2016''.'
  archived: https://web.archive.org/web/20260616190520/https://hackaday.io/project/13300-balccon-2016-badge
- kind: url
  url: https://hackaday.io/project/13300-balccon-2016-badge
  title: BALCCon 2016 Badge
  accessed: '2026-09-07'
  note: Confirmed maker (Voja Antonic), event (BalCCon0x7DB, Novi Sad, Sept 9-11 2016), and feature set (synced IR LED patterns, TV-B-Gone, USB password manager).
  archived: https://web.archive.org/web/20260616190520/https://hackaday.io/project/13300-balccon-2016-badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Made for BalCCon0x7DB, September 9-11 2016, Novi Sad, Serbia (organized by LUGoNS and the Wau Holland Foundation). No matching event exists in _data/events.yml (only DEF CON/US-con style ids are defined), so event is left as "other". MCU, exact LED part number, price, quantity, availability, and open-source status were not stated on the Hackaday.io project page and were left empty rather than guessed. A PDF manual is referenced on the project page but was not reachable via fetch to confirm further technical details.
last_modified_date: '2026-09-07'
---

Voja Antonic designed this badge for BalCCon0x7DB, the 2016 edition of the Balkan Computer Congress held September 9-11 in Novi Sad, Serbia, organized by LUGoNS and the Wau Holland Foundation. The badge carries 12 individual red/green/blue LEDs plus a central RGB LED that run pre-programmed light patterns; when two or more badges come within range of each other's infrared port they detect one another and synchronize, playing the same pattern in unison.

Beyond the LED show, the badge doubles as a TV-B-Gone universal remote (built on Mitch Altman's original open-source design) and as a small USB password manager: it can store up to 10 passwords of 15-20 characters each and type them out to a computer by acting as a USB HID keyboard, so no client software is needed.

Details such as the MCU, exact LED part, price, production quantity, and whether hardware or firmware files were released have not been confirmed from available sources and are left blank pending further research.
