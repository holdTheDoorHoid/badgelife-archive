---
title: SAO Right Angle Adapter & Extender
id: other-sao-right-angle-adapter-extender
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: other
year: 2018
makers:
- name: TI (tamperinfo)
  url: https://hackaday.io/tamperinfo
summary: A simple passive PCB that right-angles or extends a badge's SAO header so an add-on can clear space or avoid rotating into a badge's other components.
functions: 'Panel filler / mechanical adapter: reroutes an SAO connector at a right angle, or extends its reach, to solve space and orientation conflicts between a badge and its SAOs.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: v1
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
- label: hackaday.io/project/160222-sao-right-angle-adapter-extender
  url: https://hackaday.io/project/160222-sao-right-angle-adapter-extender
  kind: hackaday
- label: TI (tamperinfo) on Hackaday.io
  url: https://hackaday.io/tamperinfo
  kind: social
images:
  - file: assets/images/badges/other/sao-right-angle-adapter-extender/acab91abf3.jpg
    source: "https://hackaday.io/project/160222-sao-right-angle-adapter-extender"
    credit: "TI (tamperinfo)"
    caption: "SAO Right Angle Adapter/Extender PCB"
  - file: assets/images/badges/other/sao-right-angle-adapter-extender/c1c4cc961e.jpg
    source: "https://hackaday.io/project/160222-sao-right-angle-adapter-extender"
    credit: "TI (tamperinfo)"
    caption: "SAO Right Angle Adapter/Extender PCB, alternate view"
contact: {}
notes: []
status: unknown
sources:
- kind: url
  url: https://hackaday.io/project/160222-sao-right-angle-adapter-extender
  title: SAO Right Angle Adapter Extender
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/160222-sao-right-angle-adapter-extender
  title: "SAO Right Angle Adapter & Extender — Hackaday.io project page"
  accessed: '2026-09-07'
  note: "Confirmed maker (TI / tamperinfo), project date (created 08/07/2018), one-PCB component list, no MCU/LEDs, no published Gerbers/design files, and a 2020 comment asking for files that went unanswered. Description text and 'Details' field quoted for summary/functions."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Maker's own project page is the only real source; no press or storefront coverage found.
    The page's "Details" field reads "Panel filler for Robot 1-X" — this appears to be the name
    of a specific badge or board TI designed it to pair with, not a hacker con; no such event
    exists in this archive's events list, so `event` is left as `other` rather than guessed.
    The project is tagged under Hackaday's "Shitty Add-Ons (2018)" list, consistent with a 2018
    creation date, but no specific convention is named anywhere on the page. No price, quantity,
    or distribution info was ever published — it reads as a one-off design share rather than
    something sold or given away. No Gerbers or other design files were posted despite a 2020
    request in the comments, so `make_your_own.open_source` is left null rather than "no", since
    TI never explicitly said it was closed.
last_modified_date: '2026-09-07'
---

TI (Hackaday.io handle tamperinfo) designed this small passive PCB in August 2018 to solve a recurring badgelife annoyance: SAO add-ons and the badges they plug into are rarely sized or oriented to fit together cleanly, so add-ons end up competing for panel space or getting rotated awkwardly. The board offers a right-angle bend and an extension option for a standard 4-pin SAO connector, letting a badge maker reroute where an add-on sits relative to the badge face.

The project is a single-component PCB with no microcontroller, LEDs, or display — purely a mechanical/electrical adapter. TI's own project log notes a regret that only one pin orientation was made; a second revision with the pins flipped would have doubled how the adapter could be used. No Gerbers, schematics, or other design files were ever posted, and a 2020 comment asking for the files was left unanswered, so the project appears to exist only as this one Hackaday.io writeup and its two gallery photos.
