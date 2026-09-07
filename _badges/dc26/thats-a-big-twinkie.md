---
title: That's A Big Twinkie
id: dc26-thats-a-big-twinkie
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc26
year: 2018
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/hacker/308303-twinkletwinkie
summary: A battery-powered 'Shitty Add-on Amulet' made for DEF CON 26 (2018) that runs three SAOs from 2x AA batteries, with female headers on all three SAO ports so add-ons can be swapped without soldering; KiCad and Gerber files are published on the project page.
functions: 'Distributes power from 2x AA batteries to three SAOs plugged into its female headers at once, letting attendees swap add-ons without soldering or desoldering.'
look:
  colors: []
  shape: null
  themes:
  - wearable
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: 2x AA
  sao_version: null
  sao_ports: 3
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://hackaday.io/project/159823-thats-a-big-twinkie
  firmware_url: null
  gerbers_url: https://cdn.hackaday.io/files/1598236837867232/Thats_A_Big_Twinkie_hackaday.zip
  eda_tool: KiCad
links:
- label: hackaday.io/project/159823-thats-a-big-twinkie
  url: https://hackaday.io/project/159823-thats-a-big-twinkie
  kind: hackaday
- label: cdn.hackaday.io/files/1598236837867232/Thats_A_Big_Twinkie_hackaday.zip
  url: https://cdn.hackaday.io/files/1598236837867232/Thats_A_Big_Twinkie_hackaday.zip
  kind: hackaday
images:
- file: assets/images/badges/dc26/thats-a-big-twinkie/e70a4e88d7.jpg
  source: "https://hackaday.io/project/159823-thats-a-big-twinkie"
  credit: "TwinkleTwinkie"
  caption: "That's A Big Twinkie SAO amulet, powered by 2x AA batteries with three female SAO headers"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/159823-thats-a-big-twinkie
  title: That's A Big Twinkie
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/159823-thats-a-big-twinkie
  title: That's A Big Twinkie
  accessed: '2026-09-07'
  note: Read for maker, event/year, function, power, SAO port count, and image; also confirmed open-source KiCad/Gerber files are published.
- kind: url
  url: https://cdn.hackaday.io/files/1598236837867232/Thats_A_Big_Twinkie_hackaday.zip
  title: Thats_A_Big_Twinkie_hackaday.zip
  accessed: '2026-09-07'
  note: Confirmed the archive contains Gerber manufacturing files and a KiCad library table for the board.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Hackaday.io project page and its attached design-file archive are the only sources found; no press coverage, storefront listing, or price/quantity information located. LED presence, exact colors/shape, and SAO header version (v1 vs v2) are not stated anywhere and are left empty rather than guessed.
last_modified_date: '2026-09-07'
---

That's A Big Twinkie is a DEF CON 26 (2018) accessory by TwinkleTwinkie, built to solve a problem common at badge-add-on cons: attendees often had more SAOs than header slots on their main badge. Styled as a wearable "Amulet," the board runs on 2x AA batteries and distributes power to three SAOs at once through female headers on all three ports, so add-ons can be swapped in and out without any soldering.

The project page hosts a downloadable archive of KiCad source and Gerber manufacturing files, making the hardware fully open source; no firmware is involved since the board is a passive power/breakout distributor rather than a microcontroller-driven device. No pricing, production quantity, or distribution details (sale, giveaway, etc.) were found on the Hackaday.io page or in the attached files, so those fields are left blank pending better sources.
