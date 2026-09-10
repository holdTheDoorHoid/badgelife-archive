---
title: 'Patches (NolaCon 2025 badge, Voodoo Heart series #2)'
id: nolacon-2025-patches-nolacon-2025-badge-voodoo-heart-series-2
layout: badge
parent: NolaCon 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: nolacon-2025
year: 2025
makers:
- name: CylentK / cyl3ntkn1ght
  url: https://github.com/CylentKnight
summary: 'Patches is the 2025 NolaCon badge and the second entry in the multi-year "Voodoo Heart" badge series, a voodoo-doll character with a light-up heart and eyes built around the con''s "Learn to Solder" activity.'
functions: 'Learn-to-solder kit: attendees solder on NeoPixel-style LEDs (an ATtiny85-driven doll, heart, and two eyes) that breathe/pulse through several lighting scenes; also chains via wired headers with the prior (Stitches, 2024) and following (Scratches, 2026) badges for a combined multi-badge light sequence.'
look:
  colors: [pink, green]
  shape: null
  themes: [horror, learn to solder, kit]
tech:
  mcu: ATtiny85
  leds:
    count: 4
    type: APA106
    note: 'Driven with the Adafruit_NeoPixel library (NEO_RGB/NEO_KHZ800); 4 LEDs in one chain: mini "Patches" doll, heart, left eye, right eye.'
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: [kit]
  where: 'Distributed at NolaCon 2025 as part of the Lockpick & Solder Village learn-to-solder activity.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/CylentKnight/VoodooHeart
  eda_tool: null
links:
- label: nolacon.com/badge
  url: https://nolacon.com/badge/
  kind: website
- label: 'VoodooHeart LED sequence firmware (GitHub)'
  url: https://github.com/CylentKnight/VoodooHeart
  kind: repo
images:
  - file: assets/images/badges/nolacon-2025/patches-nolacon-2025-badge-voodoo-heart-series-2/40fb4d6bf7.png
    source: "https://nolacon.com/badge/"
    credit: "CylentK / NolaCon"
    caption: "Patches, the NolaCon 2025 badge, outline artwork"
contact: {}
notes:
- 'The sweep''s notes said this was "spotted... not yet researched"; it is confirmed to exist on NolaCon''s own badge page and is the same badge already catalogued as nolacon-2025-nolacon-2025-patches-badge ("NolaCon 2025 Patches Badge").'
- 'The community sheet''s wording, "Patches (NolaCon 2025 badge, Voodoo Heart series #2)," matches the maker''s own name for the badge ("Patches") and NolaCon''s own description of it as the second piece of the three-badge Voodoo Heart set (after 2024''s badge, before a 2026 badge).'
- 'LED type is inferred from the firmware filename (apa106_string_v1.ino) and driver call (Adafruit_NeoPixel with NEO_RGB); NolaCon''s own pages do not spell out price, quantity, or availability, so those are left unknown.'
status: released
sources:
- kind: url
  url: https://nolacon.com/badge/
  title: 'Patches (NolaCon 2025 badge, Voodoo Heart series #2)'
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://nolacon.com/
  title: Nolacon
  accessed: '2026-09-10'
  note: 'Confirms the "Patches" name and voodoo-doll story teaser; points to the badge page for full details.'
- kind: url
  url: https://github.com/CylentKnight/VoodooHeart
  title: 'CylentKnight/VoodooHeart: NolaCon Voodoo Heart Badge LED sequence'
  accessed: '2026-09-10'
  note: 'Firmware repo; apa106_string_v1.ino confirms ATtiny85 MCU and 4-LED NeoPixel-style chain (doll, heart, left eye, right eye) for the Patches badge, alongside code for the 2024 (Stitches) and 2026 (Scratches) badges in the same series.'
- kind: url
  url: https://badge.gallery/addons/nolacon-2025-patches-badge/voodoo-heart-series-continuity
  title: 'Voodoo Heart series continuity | Hacker Con Badges'
  accessed: '2026-09-10'
  note: 'Third-party summary corroborating the Voodoo Heart multi-year continuity and Learn to Solder tradition; no new technical facts.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Maker''s own site (nolacon.com) and the maker''s GitHub firmware repo confirm the badge, its name, series position, MCU, and LED setup. Price, quantity made, and current availability are not stated anywhere found and are left unknown. This entry duplicates nolacon-2025-nolacon-2025-patches-badge, which already covers the same badge.'
last_modified_date: '2026-09-10'
---

Patches is the NolaCon 2025 badge and the second installment of the con's ongoing "Voodoo Heart" series, a set of badges designed to combine across years into one voodoo-themed collection. NolaCon frames Patches as a voodoo doll from a story set in a "forgotten corner of New Orleans," built to be customized with "more freedom than ever before" — attendees solder in the badge's own light-up parts as part of the con's Lockpick & Solder Village learn-to-solder activity, now in its third year.

Under the hood, Patches is driven by an ATtiny85 lighting a 4-LED NeoPixel-style chain (APA106-type, addressed with the Adafruit_NeoPixel library) arranged as a small doll figure, a heart, and two eyes, which idle-breathe and pulse through a heartbeat-style animation. The maker's public firmware repository, VoodooHeart, contains the LED sequence code for Patches alongside the prior year's badge (Stitches, 2024) and the following year's badge (Scratches, 2026), reflecting the series' design of wiring multiple years' badges together for a combined light show.

No source found during this pass states a price, production quantity, or ongoing availability for Patches; it was distributed at NolaCon 2025 rather than sold through an open storefront as far as could be confirmed.
