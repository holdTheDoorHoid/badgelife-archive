---
title: DC33 Mini Badge
id: dc33-hackerboxes-listed-for-def-con-33-no-details
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc33
year: 2025
series: HackerBoxes Mini Badge
makers:
- name: HackerBoxes
  url: https://hackerboxes.com/
summary: A "learn to solder" kit and collectable badge that HackerBoxes gave out at DEF CON 33, with a satellite-dish/antenna-tower PCB, three LEDs, and an embedded NFC tag for tap-to-share contact info.
functions: Blinks three through-hole LEDs (red on the antenna tower, blue on the ground dish, RGB/clear on the satellite); the embedded NTAG215 NFC tag can be written with contact info (e.g. a vCard) via a phone NFC app and tapped to share it.
look:
  colors:
  - green
  - red
  - blue
  shape: satellite dish
  themes:
  - space
  - learn to solder
  - radio
  form_factor: pcb badge
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: red, blue, and one RGB/clear LED; through-hole, oriented long-pin-to-"+"
  display: none
  connectivity:
  - nfc
  inputs: []
  power: coin cell
  battery: coin cell, controlled by a 6-pin slide-switch
  sao_version: none
get_one:
  price: $20
  price_usd: 20
  quantity: unknown
  availability: available
  availability_note: Listed as in-stock with a limited number of remaining units as of 2026-09-06; Shopify inventory showed 19 units.
  distribution:
  - purchase
  where: Given out as an exclusive at DEF CON 33 (Aug 2025); leftover units are now sold online at hackerboxes.com.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: No Gerbers, schematics, or open-source hardware files found; HackerBoxes has not published design files for this badge.
links:
- kind: store
  label: DC33 Mini Badge — HackerBoxes store
  url: https://hackerboxes.com/products/dc33-mini-badge
  archived: https://web.archive.org/web/20260224115508/https://hackerboxes.com/products/dc33-mini-badge
- kind: video
  label: Soldering demo (shared with the DC31 Mini Badge)
  url: https://youtu.be/Z-F3ssX81bQ
images:
- file: assets/images/badges/dc33/hackerboxes-listed-for-def-con-33-no-details/3e2848f82a.png
  source: https://hackerboxes.com/products/dc33-mini-badge
  credit: HackerBoxes
  caption: DC33 Mini Badge PCB, showing satellite dish and antenna tower theme with red, blue, and RGB LEDs
  archived: https://web.archive.org/web/20260224115508/https://hackerboxes.com/products/dc33-mini-badge
contact: {}
notes:
- Sheet listed only the maker ("HackerBoxes"), no item title; the item was identified as the DC33 Mini Badge from HackerBoxes' own storefront.
status: released
sources:
- kind: sheet
  event: dc33
  row: 49
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://hackerboxes.com/products/dc33-mini-badge
  title: DC33 Mini Badge – HackerBoxes
  accessed: '2026-09-06'
  note: Primary source for title, price, description, LED layout, NFC chip (NTAG215), power (coin cell + slide switch), inventory count, and product image.
  archived: https://web.archive.org/web/20260224115508/https://hackerboxes.com/products/dc33-mini-badge
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: The community sheet listed HackerBoxes with no item details for DC33. HackerBoxes' own storefront confirms the item was the "DC33 Mini Badge," a learn-to-solder kit in the same annual Mini Badge / Badge Buddy series as their DC30-DC32 offerings, distributed at DEF CON 33 with leftover units later sold online. No Hackaday.io project, GitHub repo, or design files were found for this specific badge; HackerBoxes' product page is the only source used.
last_modified_date: '2026-09-06'
---

HackerBoxes' entry on the DC33 community sheet listed only the maker name with no further details. Their own storefront resolves this to the **DC33 Mini Badge**, the latest in an annual line of "learn to solder" kits (also called Badge Buddies) that HackerBoxes has handed out at DEF CON for roughly a decade, following earlier years' Amulet of Entropy, BananaJr, and Alien Robot Badge. The DC33 edition uses a space/satellite theme: a themed PCB shaped like a ground station, with a red LED on the antenna tower, a blue LED on the ground dish, and an RGB (clear) LED standing in for a satellite in the sky.

The badge is powered by a coin cell behind a 6-pin slide switch and carries no microcontroller — it's a simple through-hole soldering exercise rather than a programmable badge. Its one added feature is a 13.56 MHz NTAG215 NFC tag, which buyers can write with contact details (a vCard, for example) using a phone NFC app and then tap to share with others, similar to prior years' Mini Badges. HackerBoxes points buyers to its DC31 Mini Badge soldering video, since assembly is identical across years.

It was distributed as an exclusive at DEF CON 33 (August 2025); HackerBoxes has since continued selling leftover units through its own store at $20 each. No open-source hardware files, schematics, or a Hackaday.io/GitHub project were found for this badge.
