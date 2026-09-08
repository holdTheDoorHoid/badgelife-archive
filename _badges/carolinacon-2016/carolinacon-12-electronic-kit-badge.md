---
title: CarolinaCon 12 Electronic Kit Badge
id: carolinacon-2016-carolinacon-12-electronic-kit-badge
layout: badge
parent: CarolinaCon 12
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: carolinacon-2016
year: 2016
makers:
- name: CarolinaCon Group / Hardware Village
summary: 'An easy-to-assemble 555-timer kit badge included with admission to CarolinaCon 12, with a photoresistor-controlled blinking LED and open protoboard space for expansion.'
functions: 'Light-reactive blinker: a 555-timer astable circuit with a photoresistor in the timing network changes the LED''s blink rate with ambient light. A large protoboard area fits an Arduino Micro- or Nano-compatible board; a boost converter (given as a $20 donation reward, alongside a clone Arduino Micro) let that board run from the kit''s two AAA batteries.'
look:
  colors: []
  shape: null
  themes:
  - kit
  - learn to solder
  - hardware tool
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single LED whose blink rate is set by a 555-timer astable circuit with a photoresistor in the timing network.
  display: null
  connectivity: []
  battery: 2x AAA
  sao_version: null
get_one:
  price: included with $40 CarolinaCon 12 admission
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - kit
  - village
  where: Included with admission (CarolinaCon 12, March 4-6 2016, Hilton North Raleigh/Midtown); attendees assembled it themselves at the on-site Hardware Village.
make_your_own:
  open_source: 'yes'
  hardware_url: https://carolinacon.org/archive/cc2016/badge.trim.png
  firmware_url: null
  eda_tool: null
  notes: No PCB/gerbers — a protoboard kit. The con published a partial schematic (linked) and a full PDF assembly manual.
links:
- label: badge.gallery/events/carolinacon-12
  url: https://badge.gallery/events/carolinacon-12
  kind: website
- label: CarolinaCon 12 official archive page
  url: https://carolinacon.org/archive/cc2016/
  kind: website
- label: Badge instruction manual (PDF)
  url: https://carolinacon.org/archive/cc2016/badge.pdf
  kind: doc
- label: Partial badge schematic
  url: https://carolinacon.org/archive/cc2016/badge.trim.png
  kind: doc
images: []
contact: {}
notes:
- Sweep found this via badge.gallery, which read the event as "CarolinaCon 2016"; confirmed against the con's own archived 2016 page.
status: released
sources:
- kind: url
  url: https://badge.gallery/events/carolinacon-12
  title: CarolinaCon 12 Electronic Kit Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:carolinacon); event read as ''CarolinaCon 2016''.'
- kind: url
  url: https://carolinacon.org/archive/cc2016/
  title: CarolinaCon 12 (official archived event page)
  accessed: '2026-09-08'
  note: Primary source confirming the badge description, admission price ($40), Arduino Micro/Nano protoboard expansion, boost-converter donation reward, and links to the schematic and instruction PDF.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: No photo of an assembled badge was found; only the con's partial schematic image and PDF instruction manual are available, so images were left empty rather than using a schematic in place of a photo. Maker is credited as "CarolinaCon Group / Hardware Village" per the con's own site language ("Hardware Hacking Village" per badge.gallery); exact quantity made and a fixed BOM cost are not published anywhere found.
last_modified_date: '2026-09-08'
---

CarolinaCon 12 (March 4-6, 2016, Hilton North Raleigh/Midtown, Raleigh NC) gave every attendee a small analog electronics kit as part of the $40 admission price, meant to be soldered together on-site at the con's Hardware Village. The kit built a 555-timer astable circuit whose LED blink rate shifts with the photoresistor's light exposure, using basic through-hole parts (555 timer, LED, photoresistor, resistors, a capacitor, wire) and running off two included AAA batteries.

Beyond the core circuit, the badge left a generous protoboard area sized to accept an Arduino Micro- or Nano-compatible board, for attendees who wanted to extend it. CarolinaCon sold clone Arduino Micros with headers already attached, and offered one of those boards plus a boost converter (to step the AAA batteries up to a voltage the Arduino could run on) as a thank-you for a $20 donation to the con.

The con published a partial schematic and a full PDF assembly manual on its own site, but no photo of an assembled badge has turned up in the sources checked for this entry.
