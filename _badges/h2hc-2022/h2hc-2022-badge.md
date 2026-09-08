---
title: H2HC 2022 Badge
id: h2hc-2022-h2hc-2022-badge
layout: badge
parent: H2HC 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: h2hc-2022
year: 2022
makers:
- name: security-bits.de (Brian)
  url: https://security-bits.de/
summary: A homemade wooden-PCB badge built for H2HC 2022, using a NE555 timer and wrapped-wire discrete components to cycle a string of LEDs through a blink pattern.
functions: Blinks a sequence of LEDs, clocked by an NE555 timer; no other functions.
look:
  colors:
  - wood
  shape: rectangle
  themes:
  - retro computer
tech:
  mcu: none
  leds:
    type: discrete
    note: Cycled in sequence by an NE555 timer clock rather than a microcontroller.
  display: none
  connectivity: []
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
- label: security-bits.de/electronics/badges/h2hc_22
  url: https://security-bits.de/electronics/badges/h2hc_22/
  kind: website
images:
- file: assets/images/badges/h2hc-2022/h2hc-2022-badge/eb14a7adb0.jpg
  source: "https://security-bits.de/electronics/badges/h2hc_22/"
  credit: "brian, security-bits.de"
  caption: "Finished wooden-PCB H2HC 2022 badge with wrapped-wire NE555 circuit and LEDs"
- file: assets/images/badges/h2hc-2022/h2hc-2022-badge/68bf918238.jpg
  source: "https://security-bits.de/electronics/badges/h2hc_22/"
  credit: "brian, security-bits.de"
  caption: "H2HC 2022 badge, back/wiring detail showing wrapped-wire construction"
contact: {}
notes:
- Wooden-PCB badge with NE555 timer and wrapped-wire discrete components driving blinking LEDs, made for H2HC 2022. Found by the event-year sweep, task con-ekoparty.
- 'The sweep''s sources list this badge as "Unspecified" maker; the page itself is a build log by "brian" of security-bits.de, who made the same kind of badge for H2HC in other years (see h2hc-2015-h2hc-2015-badge, h2hc-2018-h2hc-2018-badge).'
status: listed
sources:
- kind: url
  url: https://security-bits.de/electronics/badges/h2hc_22/
  title: H2HC 2022 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-ekoparty); event read as ''H2HC 2022''.'
- kind: url
  url: https://security-bits.de/electronics/badges/h2hc_22/
  title: H2HC 2022 Badge - Security-Bits.de
  accessed: '2026-09-08'
  note: 'Maker''s own build-log page (author "brian"): describes the badge as a wooden PCB with large components wired point-to-point, driven by an NE555 giving a clock signal that cycles a few LEDs through a blink pattern. No price, quantity, or availability stated; no design files linked.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own build-log page (security-bits.de, author "brian"), which is also the entry''s only source, so treat details as maker-stated but single-sourced. No price, quantity made, distribution, or open-source files were mentioned anywhere on the page. Could not find any other coverage of this specific badge (press, forums, storefronts) in a couple of targeted searches; it reads as a personal one-off build rather than a distributed/sold item, consistent with this maker''s other H2HC badges in the archive (2015, 2018).'
last_modified_date: '2026-09-08'
---

The H2HC 2022 badge is a homemade wooden-PCB badge built by "brian" of security-bits.de for the H2HC 2022 conference, part of a small personal series of badges the same maker built for H2HC in other years. Rather than a printed circuit board, it uses a wooden panel with discrete components connected by point-to-point wrapped wire — described on the maker's own build log as "the easiest and most complicated approach to create a PCB at the same time."

Electrically it is simple: an NE555 timer chip generates a clock signal that steps through a row of LEDs, producing a sequential blink pattern. There is no microcontroller, display, or wireless connectivity, and no SAO header. The build log documents the assembly in a schematic plus roughly 14 step-by-step photographs, but does not say how many were made, whether it was distributed beyond the maker, or list price or availability — nothing found online suggests it was sold or given away at the con.
