---
title: NolaCon 2025 Patches Badge
id: nolacon-2025-nolacon-2025-patches-badge
layout: badge
parent: NolaCon 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: nolacon-2025
year: 2025
series: Voodoo Heart
makers:
- name: Voodoo Heart series
summary: 'The official NolaCon 2025 Learn-to-Solder badge: a voodoo-doll-themed PCB named "Patches" with swappable limb modules and addressable LEDs, the second entry in the multi-year Voodoo Heart badge series.'
functions: Learn-to-Solder activity where attendees solder on customizable limb modules and LEDs; because the limbs are swappable, the maker says no two assembled badges look alike.
look:
  colors: []
  shape: null
  themes:
  - horror
  - learn to solder
  - kit
tech:
  mcu: null
  leds:
    count: null
    type: APA106
    note: LED sequence firmware in the maker's VoodooHeart repo targets APA106 (WS2812-compatible) addressable LEDs; exact count on the badge not stated.
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/CylentKnight/VoodooHeart
  eda_tool: null
links:
- label: badge.gallery/years/2025
  url: https://badge.gallery/years/2025
  kind: website
- label: nolacon.com/badge
  url: https://nolacon.com/badge/
  kind: website
- label: CylentKnight/VoodooHeart (LED firmware)
  url: https://github.com/CylentKnight/VoodooHeart
  kind: repo
images:
- file: assets/images/badges/nolacon-2025/nolacon-2025-patches-badge/40fb4d6bf7.png
  source: https://nolacon.com/badge/
  credit: CylentK / NolaCon
  caption: 'Outline art of the 2025 Patches badge (Voodoo Heart series #2)'
contact: {}
notes:
- NolaCon 2025's badge, part of an ongoing Voodoo Heart-themed badge series, per the badge.gallery compendium. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task general-2025.
- Official NolaCon 2025 Learn-to-Solder badge, a voodoo-doll-themed PCB with swappable limb modules and LEDs, second installment of the multi-year 'Voodoo Heart' series. Found by the event-year sweep, task con-nolacon.
- Sweep imported this title verbatim from the maker's own page heading; no change needed.
- 'Duplicate: this appears to be the same badge as entry nolacon-2025-nolacon-2025-patches-badge ("NolaCon 2025 Patches Badge"), which is thinner (fewer sources, no images). Left both filled in per research guide; a maintainer should merge/redirect.'
status: listed
sources:
- kind: url
  url: https://badge.gallery/years/2025
  title: NolaCon 2025 Patches Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2025); event read as ''NolaCon 2025''.'
- kind: url
  url: https://nolacon.com/badge/
  title: 'Patches (Voodoo Heart series, badge #2)'
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-nolacon); event read as ''NolaCon 2025''.'
- kind: url
  url: https://github.com/CylentKnight/VoodooHeart
  title: CylentKnight/VoodooHeart
  accessed: '2026-09-08'
  note: Maker's GitHub repo holding the badge's LED sequence firmware (apa106_string_v1.ino); confirms APA106 LEDs, no MCU or full hardware files published.
- kind: url
  url: https://nolacon.com/
  title: NolaCon home page (Badge Story)
  accessed: '2026-09-08'
  note: Confirms the "Patches" narrative framing and links back to the badge page; no additional hardware specifics.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed as the real NolaCon 2025 Learn-to-Solder badge via nolacon.com/badge/ and the maker''s VoodooHeart GitHub repo (LED firmware only). No schematic, MCU, PCB files, price, or production quantity have surfaced publicly, so tech.mcu, get_one fields, and hardware_url stay empty. Merged with duplicate entry ''Patches (Voodoo Heart series, badge #2)'' (nolacon-2025-patches-voodoo-heart-series-badge-2). Added series: Voodoo Heart to match the 2024 badge #1 entry, which already carries that field.'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/nolacon-2025/patches-voodoo-heart-series-badge-2/
---


## Notes merged from the duplicate entry "Patches (Voodoo Heart series, badge #2)"

Patches is the official NolaCon 2025 badge and the second installment in the maker's multi-year "Voodoo Heart" series (CylentK, also known as cyl3ntkn1ght). It continues NolaCon's Learn-to-Solder tradition: attendees solder on swappable limb modules and addressable LEDs themselves, so the maker notes that no two finished badges end up looking exactly alike. The badge carries a voodoo-doll theme tied to a short in-universe story on NolaCon's site about a doll named Patches "in a forgotten corner of New Orleans."

Hardware specifics are thin. The maker's public GitHub repository, VoodooHeart, publishes only the LED animation firmware (an Arduino sketch, `apa106_string_v1.ino`), which points to APA106 (WS2812-compatible) addressable LEDs; no schematic, PCB files, MCU identification, price, or production quantity have surfaced. The badge is part of a planned three-badge arc — NolaCon's own page describes combining "last year's badge" (2024) with this one and a "next year's final piece" into a connected series.

This entry appears to duplicate an existing, thinner entry for the same item (`nolacon-2025-nolacon-2025-patches-badge`); both are left in place per the research guide, with a request that a maintainer reconcile them.
