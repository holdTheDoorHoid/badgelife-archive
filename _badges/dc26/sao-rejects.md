---
title: SAO Rejects
id: dc26-sao-rejects
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc26
year: 2018
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/TwinkleTwinkie
summary: 'A DIY assembly kit pairing two rejected SAO board designs from DC26 (Krusty the It and Fat Pika) with "SAO Fix" repair boards, sold as a solder-it-yourself kit.'
functions: 'No interactive functions; each SAO lights two through-hole-soldered 1206 LEDs (red or yellow) once the buyer solders the LEDs and 2x2 headers onto the boards.'
look:
  colors: []
  shape: null
  themes:
  - badgelife
  - kit
tech:
  mcu: none
  leds:
    count: 2
    type: '1206'
    note: 'Two LEDs per board (one red, one yellow set across the kit); unlabeled in the kit, buyer must identify polarity/color while assembling.'
  display: none
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  - kit
  where: 'Sold on the maker''s Tindie shop as the "SAO 1 and 2 Assembly Kit."'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/159469-sao-rejects
  url: https://hackaday.io/project/159469-sao-rejects
  kind: hackaday
- label: TwinkleTwinkie on Hackaday.io
  url: https://hackaday.io/TwinkleTwinkie
  kind: hackaday
images:
  - file: assets/images/badges/dc26/sao-rejects/3c5cf67e27.jpg
    source: "https://hackaday.io/project/159469-sao-rejects"
    credit: "TwinkleTwinkie"
    caption: "SAO Rejects assembly kit boards"
  - file: assets/images/badges/dc26/sao-rejects/dad951a553.jpg
    source: "https://hackaday.io/project/159469-sao-rejects"
    credit: "TwinkleTwinkie"
    caption: "SAO Rejects kit, main project photo"
contact: {}
notes:
- 'Sheet/sweep had listed event as unknown; the Hackaday project page and maker''s profile place "Fat Pika" as TwinkleTwinkie''s DC26 (DEF CON 26, 2018) Shitty Add-on #2, so event/year were corrected to DC26 / 2018. The origin of "Krusty the It," the other board in the kit, is not confirmed on the maker''s profile but is presented alongside Fat Pika as a same-era reject.'
- 'The kit is a build-it-yourself pack of two rejected/prototype SAO PCBs plus small "SAO Fix v1.0" repair boards, headers, resistors and LEDs -- not a single finished badge. Filed as type: kit rather than sao for that reason.'
- 'No pricing, quantity made, or current Tindie availability could be confirmed; the Hackaday project page itself carries no price and the maker''s Tindie shop page could not be fetched (403 Forbidden).'
status: released
sources:
- kind: url
  url: https://hackaday.io/project/159469-sao-rejects
  title: SAO Rejects
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/159469-sao-rejects
  title: SAO Rejects
  accessed: '2026-09-07'
  note: 'Project description and build instructions: kit contents (Krusty the It Reject, Fat Pika Reject, 2 SAO Fix boards, headers, resistors, 4 LEDs), assembly steps, project created July 2018, no price listed.'
- kind: url
  url: https://hackaday.io/TwinkleTwinkie
  title: TwinkleTwinkie - Hackaday.io profile
  accessed: '2026-09-07'
  note: 'Confirms maker TwinkleTwinkie and that "Fat Pika" is their DC26 (2018) Shitty Add-on #2, used to correct event/year.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, kit contents, DC26/2018 dating via Fat Pika) confirmed from the maker''s own Hackaday.io pages. Price, quantity produced, current availability, and the exact origin/event of "Krusty the It" specifically could not be confirmed; the Tindie storefront page returned a 403 and was not reachable.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/sao-rejects/
---

SAO Rejects is a solder-it-yourself kit from badgelife designer TwinkleTwinkie, sold through their Tindie shop. Rather than being a single badge, the kit bundles two of the maker's rejected or leftover SAO board designs -- "Krusty the It" (described as "Recovered") and "Fat Pika" (described as "Untouched") -- with two small "SAO Fix v1.0" repair boards, 2x2 pin headers, 62-ohm resistors, and red and yellow 1206 LEDs, so a buyer can assemble working SAOs out of boards that didn't make the cut for the main badge run.

Fat Pika is documented elsewhere on TwinkleTwinkie's Hackaday.io profile as their fourth-numbered DC26 (DEF CON 26, 2018) Shitty Add-on, which places this kit in the same DC26-era batch of designs; the exact provenance of "Krusty the It" was not separately confirmed. Assembly is simple: each SAO board takes two unlabeled LEDs (soldered upside-down, lens toward the board) and a 2x2 header, while the accompanying fix board takes a single resistor and its own header, wired to correct an issue with the reject boards. No MCU or other active logic is involved -- the boards are simple LED indicators once populated. Pricing, production quantity, and current Tindie availability could not be verified from the sources reached.
