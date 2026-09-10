---
title: BSides Charleston Lock SAO
id: bsides-charleston-2019-bsides-charleston-lock-sao
layout: badge
parent: BSides Charleston 2019
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: bsides-charleston-2019
year: 2019
makers:
- name: Badge Pirates
  url: https://github.com/BadgePiratesLLC
summary: A lock-shaped SAO kit that BSides Charleston 2019 attendees soldered together themselves, with a single through-hole LED wired to a v1.69bis SAO header.
functions: Lights a single LED once assembled and plugged into the host badge's SAO header; no other electronics.
look:
  colors: []
  shape: lock
  themes:
  - kit
  - learn to solder
  - security
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single through-hole LED; assembly guide stresses correct polarity (long anode pin to positive, flat cathode side to negative).
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Given to BSides Charleston 2019 attendees to assemble at the event; no separate storefront found.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: blog.badgepirates.com/BsidesCHS-SOA-Assembly
  url: https://blog.badgepirates.com/BsidesCHS-SOA-Assembly/
  kind: website
- label: BadgePiratesLLC on GitHub
  url: https://github.com/BadgePiratesLLC
  kind: repo
images:
  - file: assets/images/badges/bsides-charleston-2019/bsides-charleston-lock-sao/0dae0d88f1.jpg
    source: "https://blog.badgepirates.com/BsidesCHS-SOA-Assembly/"
    credit: "Badge Pirates"
    caption: "BSides Charleston 2019 badge with the Lock SAO attached"
  - file: assets/images/badges/bsides-charleston-2019/bsides-charleston-lock-sao/ed60857f4e.jpg
    source: "https://blog.badgepirates.com/BsidesCHS-SOA-Assembly/"
    credit: "Badge Pirates"
    caption: "Lock SAO with LED and header, front view during assembly"
contact: {}
notes:
- A lock-shaped SAO kit (LED + keyed headers) that attendees assembled themselves at BSides Charleston 2019, documented in a Badge Pirates assembly guide. Found by the event-year sweep, task bsides-huntsville.
- The sweep's title matched what Badge Pirates itself calls the item ("Bsides Charleston Lock SAO" / "SAO (Standalone Add-On)"), so no rewording was needed.
status: listed
sources:
- kind: url
  url: https://blog.badgepirates.com/BsidesCHS-SOA-Assembly/
  title: BSides Charleston Lock SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-huntsville); event read as ''BSides Charleston 2019''.'
- kind: url
  url: https://blog.badgepirates.com/BsidesCHS-SOA-Assembly/
  title: BsidesCHS SAO Assembly guide
  accessed: '2026-09-10'
  note: Maker's own assembly-instructions page; confirms maker, event/year, LED assembly detail, SAO v1.69bis header, and kit distribution at the event. Also source of both saved images.
- kind: url
  url: https://github.com/BadgePiratesLLC
  title: BadgePiratesLLC GitHub org
  accessed: '2026-09-10'
  note: Linked from the assembly page's social links; no repo specific to this SAO was found there.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed on the maker''s own assembly-instructions page, which describes the kit and its LED wiring but gives no chip, price, quantity made, or design-file links, so those fields stay empty. No storefront or standalone product page was found, only the assembly guide, so quantity/availability/price could not be pinned down.'
last_modified_date: '2026-09-10'
---

The BSides Charleston Lock SAO is a simple solder-it-yourself add-on that Badge Pirates put together for BSides Charleston 2019: a lock-shaped board with a single through-hole LED that plugs into a badge's SAO header (v1.69bis, the 6-pin standard). Rather than selling it, Badge Pirates handed it out as an assembly kit, publishing a step-by-step guide on their blog that walks new solderers through getting the LED's polarity right and seating the keyed header.

No chip, no display, and no independent power source are involved — it is a learn-to-solder piece whose only "feature" is lighting up once wired correctly and plugged into the host badge. No pricing, production quantity, or surviving storefront listing turned up; the only trace of the item online is Badge Pirates' own assembly-instructions page, which is also where both saved photos come from.
