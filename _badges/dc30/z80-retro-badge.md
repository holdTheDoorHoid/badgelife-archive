---
title: Z80 Retro Badge
id: dc30-z80-retro-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: Uberfoo Heavy Industries
  url: https://uberfoo.net
summary: A working 8-bit Z80 microcomputer built as a two-board DEF CON 30 badge - a cat-shaped "I Can Haz Z80" front panel over a full Z80 Retro Badge motherboard with RAM, ROM, and serial I/O.
functions: Boots and runs CP/M 2.2 and other Z80 software; fully reprogrammable over its expansion bus, with a 44-pin IDE connector to a compact flash card for storage.
look:
  colors:
  - purple
  - white
  - black
  shape: cat
  themes:
  - cat
  - retro computer
tech:
  mcu: Z80
  leds:
    count: 4
    type: RGB
    note: 4x addressable RGB LEDs
  display: none
  connectivity:
  - uart
  battery: 3150mAh battery
  sao_version: null
get_one:
  price: $140
  price_usd: 140.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Hacker Warehouse booth at D3FC0N
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: twitter.com/uberfoo2000/status/1552441001641639936/photo/1
  url: https://twitter.com/uberfoo2000/status/1552441001641639936/photo/1
  kind: social
- label: uberfoo.net
  url: https://uberfoo.net
  kind: website
images:
- file: assets/images/badges/dc30/z80-retro-badge/2ec0c086fc.jpg
  source: "https://twitter.com/uberfoo2000/status/1552441001641639936/photo/1"
  credit: "Uberfoo Heavy Industries (James Bryant)"
  caption: "Maker's marketing flyer showing the Z80 Retro motherboard and the cat-shaped front badge with battery holder"
contact: {}
notes:
- Can purchase at the HW booth. Any left over may be made available...
status: listed
sources:
- kind: sheet
  event: dc30
  row: 17
  updated: '2022-07-28'
- kind: url
  url: https://twitter.com/uberfoo2000/status/1552441001641639936/photo/1
  title: "James Bryant (@uberfoo2000) tweet with Z80 Retro Badge marketing flyer"
  accessed: '2026-09-07'
  note: Maker-authored spec sheet confirming chip, RAM/ROM, LEDs, battery, CP/M, and DEF CON 30 (D3FC0N) sale at the Hacker Warehouse booth; the tweet text says manufacturing was complete but shipment was still pending as of July 2022.
- kind: url
  url: https://uberfoo.net
  title: Uberfoo Heavy Industries homepage
  accessed: '2026-09-07'
  note: Maker's site; confirms Uberfoo Heavy Industries as a badge/SAO maker, though its "latest news" only highlights an earlier "Shitty Kitty" badge launch and does not mention the Z80 Retro Badge specifically.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core specs (Z80 CPU, 8kb EEPROM, 128kb bankable SRAM, SIO/2 and CTC, 44-pin IDE connector, custom "ZBridge" logic, compact flash storage, 4x addressable RGB LEDs, 3150mAh battery, CP/M 2.2) come from the maker's own promotional flyer posted to Twitter/X, not independently corroborated elsewhere - no Hackaday.io project, GitHub repo, or storefront listing for this specific badge was found (web search tooling was unavailable this session; only WebFetch-reachable pages could be checked, and Twitter's own pages return HTTP 402 to automated fetches, so this was read via a text-extraction proxy). Quantity made and final retail availability (sold out vs. leftover stock) are not stated anywhere found. make_your_own fields left empty - no hardware/firmware repo was located.
last_modified_date: '2026-09-07'
---

The Z80 Retro Badge is a two-board DEF CON 30 (D3FC0N, 2022) badge from Uberfoo Heavy Industries (maker James Bryant, @uberfoo2000): a full 8-bit Z80 microcomputer motherboard - Z80 CPU, 8kb EEPROM, 128kb bankable SRAM, a Zilog SIO/2 and CTC, a 44-pin IDE connector feeding a compact flash card for storage, and custom "ZBridge" glue logic - paired with a separate cat-shaped front panel silkscreened "I Can Haz Z80" that holds the battery and carries four addressable RGB LEDs. It boots and runs CP/M 2.2 and other Z80 software, and the maker describes it as fully reprogrammable with a full expansion bus for further hacking.

It was sold for $140 at the Hacker Warehouse booth in the DEF CON 30 vendor area, with any leftover stock said to be made available afterward. As of the maker's July 28, 2022 promotional tweet, manufacturing was complete but the boards had not yet shipped, so renders stood in for photos of the finished product; whether it ultimately sold out, how many were made, and whether hardware/firmware files were ever published are not confirmed by any source found in this pass.
