---
title: Frankenbadge (DC27)
id: dc27-frankenbadge-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Dr.n0psl3d
  url: https://github.com/DrN0psl3d
summary: A Frankenstein's-monster-shaped wearable badge built around four working IN-12A/B Nixie tubes, multiplexed by a K155ID1 driver and run as a real-time clock.
functions: Displays the time on four Nixie tubes via a DS3231 real-time clock; keeps time through power loss; USB-reprogrammable over its mini-USB port.
look:
  colors: []
  shape: null
  themes:
  - horror
  - retro computer
  - wearable
tech:
  mcu: ATmega32U4
  leds: null
  display: 4x IN-12A/B Nixie tube
  connectivity:
  - usb
  battery: 9V battery (not included) or 9-36V DC jack
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '50'
  availability: unknown
  distribution:
  - kit
  where: Distributed as a DIY kit at DEF CON 27; assembly (including hand-soldering 0402 parts) left to the builder, hot-air rework/reflow recommended.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/DrN0psl3d/Frankenbadge
  firmware_url: https://github.com/DrN0psl3d/Frankenbadge
  eda_tool: EAGLE
  license: MIT
images:
- file: assets/images/badges/dc27/frankenbadge-dc27/d78620280c.jpg
  source: "https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/"
  credit: "Dr.n0psl3d"
  caption: "Frankenbadge with four IN-12B Nixie tubes and Frankenstein-themed silkscreen"
contact: {}
notes:
- image URL only; Nixie tube (IN-12B) badge, 50 DIY kits
status: released
sources:
- kind: url
  url: https://hackaday.com/wp-content/uploads/2019/08/FrankenBadge-DC27.jpg
  title: Frankenbadge (DC27)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
- kind: url
  url: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
  title: 'The Badgies: Clever, Crazy, And Creative Ideas In Electronic Design'
  accessed: '2026-09-07'
  note: Confirms maker, IN-12B tubes, Frankenstein theme, high-voltage components hot-glued/3D-printed-enclosed on the back, 50 kits brought to con, DIY assembly.
- kind: url
  url: https://www.hackster.io/news/this-fantastic-frankenbadge-features-functional-nixie-tubes-c2f34742133
  title: This Fantastic Frankenbadge Features Functional Nixie Tubes
  accessed: '2026-09-07'
  note: Confirms ATmega32U4 MCU, K155ID1 driver chip, multiplexed IN-12B tubes, Frankenstein-themed component placement, first Nixie build.
- kind: url
  url: https://github.com/DrN0psl3d/Frankenbadge
  title: 'GitHub - DrN0psl3d/Frankenbadge: Code for FrankenBadge, A Nixie Tube Clock You Can Wear'
  accessed: '2026-09-07'
  note: Maker's own repo; confirms parts list (4x IN-12A/B, K155ID1, ATmega32U4, DS3231 RTC), power options (9V battery or 9-36V DC jack), USB-mini reprogramming, EAGLE hardware files, MIT license.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price and exact quantity sold vs. brought were not stated by any source beyond "enough parts for 50 badges"; treated as quantity made/brought, not confirmed sold. No LED count found (badge appears to have no addressable LEDs, only Nixie tubes). Availability set to unknown since no current storefront exists; this was a one-time DIY kit at DC27 2019.
last_modified_date: '2026-09-07'
---

Dr.n0psl3d's Frankenbadge is a Frankenstein's-monster-shaped wearable built for DEF CON 27 (2019) around four IN-12A/B Nixie tubes, giving the badge a genuinely working Nixie-tube clock display. It was his first Nixie build, adapted from a Nixie clock concept, and the layout places components to suggest the stitching on Frankenstein's monster's head. Driving four Nixie tubes from a battery-friendly badge is not trivial — Nixies need roughly 170-190V — so the design multiplexes all four tubes through a single K155ID1 BCD-to-decimal driver chip, controlled by an ATmega32U4 (the same microcontroller used on the Arduino Leonardo). A DS3231 real-time clock keeps time through power loss, and the badge is reprogrammable over its USB-mini port. Power comes from a 9V battery or a 9-36V DC jack for running it at a desk; the high-voltage circuitry on the back is enclosed in a 3D-printed housing or sealed under hot glue, with a silkscreen warning to stay out.

Dr.n0psl3d brought parts for 50 badges to DEF CON 27 and distributed it as a DIY kit, leaving assembly to the builder; the smallest parts are 0402, so hot-air rework or a reflow oven is recommended over hand soldering.

## Make your own

Hardware and firmware are both open-sourced on the maker's GitHub under an MIT license. The repository includes EAGLE CAD design files for the PCB alongside the ATmega32U4 firmware. Follow the README's build notes on part sizes (0402 minimum) and recommended assembly tools before attempting a hand build.
