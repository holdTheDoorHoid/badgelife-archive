---
title: Knitronics Add-on Badge for Open Sauce 2026
id: open-sauce-2026-knitronics-add-on-badge-for-open-sauce-2026
layout: badge
parent: Open Sauce 2026
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: open-sauce-2026
year: 2026
makers:
- name: knitronics
summary: 'A self-powered LED-flasher add-on for the 2026 Open Sauce event badge, built around a 555-timer circuit that pulses 16 red and blue LEDs.'
functions: 'Alternates 8 red and 8 blue LEDs via a 555-timer astable circuit; a potentiometer adjusts the flash speed.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 16
    type: discrete
    note: '8 red LEDs (2V forward) and 8 blue LEDs (2.68V forward), driven in alternating pulses by a 555 timer.'
  display: none
  connectivity: []
  battery: '2x 9V batteries in series (18V supply)'
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
- label: deveco.io/u/knitronics/project/knitronics-add-on-badge-for-open-sauce-2026
  url: https://deveco.io/u/knitronics/project/knitronics-add-on-badge-for-open-sauce-2026
  kind: website
images:
  - file: assets/images/badges/open-sauce-2026/knitronics-add-on-badge-for-open-sauce-2026/6102ee4112.jpg
    source: "https://deveco.io/u/knitronics/project/knitronics-add-on-badge-for-open-sauce-2026"
    credit: "knitronics"
    caption: "Knitronics Add-on Badge for Open Sauce 2026, cover photo"
  - file: assets/images/badges/open-sauce-2026/knitronics-add-on-badge-for-open-sauce-2026/39b084b42c.jpg
    source: "https://deveco.io/u/knitronics/project/knitronics-add-on-badge-for-open-sauce-2026"
    credit: "knitronics"
    caption: "Full-color render of the badge PCB"
contact: {}
notes:
- 'Unofficial clip-on add-on for the 2026 Open Sauce badge: a 555-timer LED flasher with 16 alternating red/blue LEDs and a speed potentiometer, fabricated via NextPCB. Found by the event-year sweep, task con-open-sauce.'
status: listed
sources:
- kind: url
  url: https://deveco.io/u/knitronics/project/knitronics-add-on-badge-for-open-sauce-2026
  title: Knitronics Add-on Badge for Open Sauce 2026
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-open-sauce); event read as ''Open Sauce 2026''.'
- kind: url
  url: https://deveco.io/u/knitronics/project/knitronics-add-on-badge-for-open-sauce-2026
  title: Knitronics Add-on Badge for Open Sauce 2026
  accessed: '2026-09-08'
  note: 'Confirmed project details: 555-timer circuit, 16 LEDs (8 red, 8 blue), potentiometer speed control, dual 9V battery holders in series for 18V, two-layer PCB, NextPCB-sponsored fabrication/assembly completed July 9 2026, corner mounting holes for attaching to the main badge.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Maker''s own project page confirms the item exists and gives full technical details, but does not state price, quantity made, or availability, and does not clearly confirm whether design files/gerbers are published (a "download file" is mentioned on the page but its contents were not confirmed). Those fields are left empty rather than guessed.'
last_modified_date: '2026-09-08'
---

The Knitronics Add-on Badge is an unofficial clip-on accessory made for the 2026 Open Sauce event badge. It is a simple, purely analog blinky: a 555-timer astable circuit alternately pulses eight red LEDs (2V forward voltage) and eight blue LEDs (2.68V forward voltage), each drawing roughly 8-10mA, with a potentiometer to adjust the flash rate. Power comes from two 9V batteries wired in series for an 18V supply.

The two-layer PCB carries knitronics's logo in silkscreen and has corner mounting holes so it can be attached to the main Open Sauce badge. NextPCB sponsored fabrication and assembly, with boards completed by July 9, 2026; most components arrived pre-soldered, leaving the battery holders and potentiometer for the builder to hand-solder themselves, mirroring the build experience of the main event badge.

No price, production quantity, or availability information was found on the project page, and it is unclear whether gerbers or other design files are published there.
