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
  colors:
  - pink
  - green
  shape: null
  themes:
  - horror
  - learn to solder
  - kit
tech:
  mcu: ATtiny85
  leds:
    count: null
    type: APA106
    note: LED sequence firmware in the maker's VoodooHeart repo targets APA106 (WS2812-compatible) addressable LEDs; exact count on the badge not stated.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed at NolaCon 2025 as part of the Lockpick & Solder Village learn-to-solder activity.
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
- file: assets/images/badges/nolacon-2025/nolacon-2025-patches-badge/40fb4d6bf7.png
  source: https://nolacon.com/badge/
  credit: CylentK / NolaCon
  caption: Patches, the NolaCon 2025 badge, outline artwork
contact: {}
notes:
- NolaCon 2025's badge, part of an ongoing Voodoo Heart-themed badge series, per the badge.gallery compendium. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task general-2025.
- Official NolaCon 2025 Learn-to-Solder badge, a voodoo-doll-themed PCB with swappable limb modules and LEDs, second installment of the multi-year 'Voodoo Heart' series. Found by the event-year sweep, task con-nolacon.
- Sweep imported this title verbatim from the maker's own page heading; no change needed.
- 'Duplicate: this appears to be the same badge as entry nolacon-2025-nolacon-2025-patches-badge ("NolaCon 2025 Patches Badge"), which is thinner (fewer sources, no images). Left both filled in per research guide; a maintainer should merge/redirect.'
- The sweep's notes said this was "spotted... not yet researched"; it is confirmed to exist on NolaCon's own badge page and is the same badge already catalogued as nolacon-2025-nolacon-2025-patches-badge ("NolaCon 2025 Patches Badge").
- 'The community sheet''s wording, "Patches (NolaCon 2025 badge, Voodoo Heart series #2)," matches the maker''s own name for the badge ("Patches") and NolaCon''s own description of it as the second piece of the three-badge Voodoo Heart set (after 2024''s badge, before a 2026 badge).'
- LED type is inferred from the firmware filename (apa106_string_v1.ino) and driver call (Adafruit_NeoPixel with NEO_RGB); NolaCon's own pages do not spell out price, quantity, or availability, so those are left unknown.
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
- kind: url
  url: https://badge.gallery/addons/nolacon-2025-patches-badge/voodoo-heart-series-continuity
  title: Voodoo Heart series continuity | Hacker Con Badges
  accessed: '2026-09-10'
  note: Third-party summary corroborating the Voodoo Heart multi-year continuity and Learn to Solder tradition; no new technical facts.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed as the real NolaCon 2025 Learn-to-Solder badge via nolacon.com/badge/ and the maker''s VoodooHeart GitHub repo (LED firmware only). No schematic, MCU, PCB files, price, or production quantity have surfaced publicly, so tech.mcu, get_one fields, and hardware_url stay empty. Merged with duplicate entry ''Patches (Voodoo Heart series, badge #2)'' (nolacon-2025-patches-voodoo-heart-series-badge-2). Added series: Voodoo Heart to match the 2024 badge #1 entry, which already carries that field. Merged with duplicate entry ''Patches (NolaCon 2025 badge, Voodoo Heart series #2)'' (nolacon-2025-patches-nolacon-2025-badge-voodoo-heart-series-2).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/nolacon-2025/patches-voodoo-heart-series-badge-2/
- /badges/nolacon-2025/patches-nolacon-2025-badge-voodoo-heart-series-2/
---


## Notes merged from the duplicate entry "Patches (Voodoo Heart series, badge #2)"

Patches is the official NolaCon 2025 badge and the second installment in the maker's multi-year "Voodoo Heart" series (CylentK, also known as cyl3ntkn1ght). It continues NolaCon's Learn-to-Solder tradition: attendees solder on swappable limb modules and addressable LEDs themselves, so the maker notes that no two finished badges end up looking exactly alike. The badge carries a voodoo-doll theme tied to a short in-universe story on NolaCon's site about a doll named Patches "in a forgotten corner of New Orleans."

Hardware specifics are thin. The maker's public GitHub repository, VoodooHeart, publishes only the LED animation firmware (an Arduino sketch, `apa106_string_v1.ino`), which points to APA106 (WS2812-compatible) addressable LEDs; no schematic, PCB files, MCU identification, price, or production quantity have surfaced. The badge is part of a planned three-badge arc — NolaCon's own page describes combining "last year's badge" (2024) with this one and a "next year's final piece" into a connected series.

This entry appears to duplicate an existing, thinner entry for the same item (`nolacon-2025-nolacon-2025-patches-badge`); both are left in place per the research guide, with a request that a maintainer reconcile them.

## Notes merged from the duplicate entry "Patches (NolaCon 2025 badge, Voodoo Heart series #2)"

Patches is the NolaCon 2025 badge and the second installment of the con's ongoing "Voodoo Heart" series, a set of badges designed to combine across years into one voodoo-themed collection. NolaCon frames Patches as a voodoo doll from a story set in a "forgotten corner of New Orleans," built to be customized with "more freedom than ever before" — attendees solder in the badge's own light-up parts as part of the con's Lockpick & Solder Village learn-to-solder activity, now in its third year.

Under the hood, Patches is driven by an ATtiny85 lighting a 4-LED NeoPixel-style chain (APA106-type, addressed with the Adafruit_NeoPixel library) arranged as a small doll figure, a heart, and two eyes, which idle-breathe and pulse through a heartbeat-style animation. The maker's public firmware repository, VoodooHeart, contains the LED sequence code for Patches alongside the prior year's badge (Stitches, 2024) and the following year's badge (Scratches, 2026), reflecting the series' design of wiring multiple years' badges together for a combined light show.

No source found during this pass states a price, production quantity, or ongoing availability for Patches; it was distributed at NolaCon 2025 rather than sold through an open storefront as far as could be confirmed.
