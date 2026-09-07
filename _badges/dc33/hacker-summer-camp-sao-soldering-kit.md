---
title: Hacker Summer Camp SAO Soldering Kit
id: dc33-hacker-summer-camp-sao-soldering-kit
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc33
year: 2025
makers:
- name: Make it Hackin
  url: https://github.com/MakeItHackin
summary: A beginner through-hole soldering kit from Make it Hackin that builds into a small SAO with four RGB LEDs that slowly cycle color when plugged into a badge.
functions: It slowly changes color. The four RGB LEDs cycle through colors once the assembled SAO is powered by a host badge's SAO header.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 4
    type: RGB
    note: Through-hole RGB LEDs, one current-limiting resistor, assembled by the buyer.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: $5
  price_usd: 5.0
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/MakeItHackin/SummerCampSAO
  firmware_url: null
  eda_tool: null
links:
- label: github.com/MakeItHackin/SummerCampSAO
  url: https://github.com/MakeItHackin/SummerCampSAO
  kind: repo
- label: Assembly tutorial (YouTube)
  url: https://youtu.be/E3vtrzXdGKo
  kind: video
images:
- file: assets/images/badges/dc33/hacker-summer-camp-sao-soldering-kit/9bb538c890.jpg
  source: "https://github.com/MakeItHackin/SummerCampSAO"
  credit: "Make it Hackin"
  caption: "Assembled Hacker Summer Camp SAO with RGB LEDs lit"
- file: assets/images/badges/dc33/hacker-summer-camp-sao-soldering-kit/0684ca08c0.jpg
  source: "https://github.com/MakeItHackin/SummerCampSAO"
  credit: "Make it Hackin"
  caption: "Kit contents laid out before assembly"
contact:
  emails:
  - andrew@makeithackin.com
notes:
- Teaches you how to solder through-hole components
status: listed
sources:
- kind: sheet
  event: dc33
  row: 43
  updated: 8/3/2025 10:50:24
- kind: url
  url: https://github.com/MakeItHackin/SummerCampSAO
  title: "MakeItHackin/SummerCampSAO"
  accessed: '2026-09-06'
  note: "README describes the kit's contents (4 RGB LEDs, 1 resistor, 1 SAO connector), assembly steps, and confirms it lights up with slow-changing colors once plugged into a badge's SAO port; no price, quantity, or MCU is stated in the repo."
research:
  status: researched
  confidence: low
  last_checked: '2026-09-06'
  notes: 'Confirmed via the maker''s own GitHub repo (README + assembly photos): this is a passive, MCU-less through-hole soldering kit with 4 RGB LEDs and 1 resistor, distributed as a beginner kit (likely bundled with a badge or sold alongside one, per the community sheet). The repo README also mentions "DC32 Engage" and "DC32 Flipboard" stickers included in the kit bag, which may mean some kit stock or stickers were left over from a prior year, but the sheet lists this item for DC33 (2025) so that is kept as the event. No storefront, price confirmation beyond the sheet''s $5, quantity made, or availability status was found; web search was unavailable for this task (session search budget exhausted) so only the repo itself and its linked YouTube tutorial were checked.'
last_modified_date: '2026-09-06'
---

The Hacker Summer Camp SAO is a beginner-friendly soldering kit by Make it Hackin, distributed around DEF CON 33 (2025) for $5. It is a simple, MCU-less SAO circuit board: builders solder in one resistor, four through-hole RGB LEDs, and a 4-pin SAO connector, then plug the finished board into a badge's SAO header to see the LEDs slowly cycle color, powered entirely by the host badge. The kit ships with a small bag of stickers and googly eyes alongside the board and components.

Make it Hackin published a step-by-step README and a companion YouTube video walking through the resistor, LED, and connector soldering steps and how to test the finished board on a badge simulator. Beyond the maker's own GitHub repo, no separate storefront listing, price confirmation, or production quantity could be found for this specific kit.
