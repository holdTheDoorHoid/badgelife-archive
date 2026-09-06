---
title: Laser* Tag Badge DS
id: dc34-laser-tag-ds
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
series: Laser* Tag Badge
makers:
- name: Dani Weidman
  url: https://www.dani.pink/
  role: creator
- name: Zach Resmer
  url: https://resmer.co.za/ch
  role: special help
summary: 'A wearable infrared laser-tag badge for DEF CON 34, the sequel to 2025''s Laser* Tag Badge, adding a LoRa radio for automatic score syncing and a second rear display.'
functions: 'Wear the badge at DEF CON and earn points by "shooting" other wearers with a narrow-beam IR emitter; score more for tagging more unique people per hour. Scores sync automatically over LoRa radio to an online leaderboard, or manually via a QR code if LoRa does not work out. Also compatible with the open OpenLASIR IR protocol, so a Flipper Zero (with the right IR files) or other OpenLASIR-speaking hardware can register hits against it.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - ctf
  - game
tech:
  mcu: RP2350
  leds:
    count: 60
    type: RGB
    note: Doubled from 30 on the 2025 badge.
  display: 1.28" round LCD (240x240, GC9A01) front + SSD1306 OLED on back
  connectivity:
  - lora
  - ir
  battery: Rechargeable 18650
  sao_version: v1
  sao_ports: 1
get_one:
  price: About $90
  price_usd: 90.0
  quantity: ''
  availability: unknown
  distribution:
  - preorder
  where: Preordered directly through the maker's site (www.dani.pink/lasertag); the maker said preorders would be refunded if manufacturing wasn't finished in time.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'The badge''s own hardware/firmware files are not published, but the maker documents the OpenLASIR IR protocol it speaks (MIT licensed) at https://github.com/danielweidman/OpenLASIR, letting other makers build compatible laser-tag hardware.'
links:
- label: www.dani.pink/lasertag
  url: https://www.dani.pink/lasertag
  kind: store
- label: OpenLASIR protocol (GitHub)
  url: https://github.com/danielweidman/OpenLASIR
  kind: repo
images:
- file: assets/images/badges/dc34/laser-tag-ds/371e4dc46f.jpg
  source: "https://www.dani.pink/lasertag"
  credit: "Dani Weidman"
  caption: "Laser* Tag Badge DS, front view"
- file: assets/images/badges/dc34/laser-tag-ds/9f2fbe88ec.jpg
  source: "https://www.dani.pink/lasertag"
  credit: "Dani Weidman"
  caption: "Laser* Tag Badge DS, back view showing OLED display"
contact:
  discord: danpalm
  emails:
  - palm12341@gmail.com
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 8
  updated: 5/25/2026 22:20:26
  listing: New
- kind: url
  url: https://www.dani.pink/lasertag
  title: 'Laser* Tag Badge - About'
  accessed: '2026-09-06'
  note: Primary source for hardware spec, gameplay, pricing mention, distribution, and images.
- kind: url
  url: https://github.com/danielweidman/OpenLASIR
  title: danielweidman/OpenLASIR
  accessed: '2026-09-06'
  note: Confirms the open IR protocol the badge implements, MIT licensed, and that it is a protocol spec rather than the badge's own hardware/firmware source.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Maker''s own project page confirms all core hardware and gameplay details. No published quantity made or a firm sale price/availability date beyond the sheet''s "About $90"; the page frames it as preorder-based with refunds promised if manufacturing slipped, so availability is left unknown rather than guessed. This is the DC34 (2026) sequel to a DC33 (2025) "Laser* Tag Badge" by the same maker, already in the archive as dc33-laser-tag-badge; not a duplicate, but part of the same series.'
last_modified_date: '2026-09-06'
---

Laser* Tag Badge DS is Dani Weidman's second DEF CON laser-tag badge, built for DEF CON 34 (2026) as a follow-up to the 2025 Laser* Tag Badge. Wearers "shoot" each other with a narrow-beam infrared emitter (VSLY5940) picked up by an IR receiver, scoring points for tagging unique people each hour during the con. The badge runs an RP2350 on a Waveshare RP2350-Zero daughterboard, drives 60 RGB LEDs (double the original's 30), and adds a round 1.28" GC9A01 LCD on the front alongside a new SSD1306 OLED on the back. It also gained a 915 MHz LoRa radio with an external SMA antenna, intended to sync scores to an online leaderboard automatically; if LoRa reception in the crowded Las Vegas Convention Center doesn't hold up, scores can still be synced manually via QR code. Power comes from a rechargeable 18650 cell, and the badge includes a vibration motor, piezo buzzer, and one SAO port (power plus an unimplemented I2C).

The badge speaks OpenLASIR, an open MIT-licensed infrared protocol for badge-to-badge laser tag that Weidman documents separately on GitHub, so third-party hardware — including a stock Flipper Zero loaded with the right per-color IR files — can register hits against it. Weidman also planned a firmware update so owners of the original 2025 badge could take part, though without the new LoRa or second-screen features. The maker's page frames distribution around preorders, with a promise to refund buyers if manufacturing didn't finish in time; no firm unit count or final sale price is published beyond the sheet's "about $90" estimate.

## History

Laser* Tag Badge DS is the sequel to the 2025 DEF CON 33 "Laser* Tag Badge" (also by Dani Weidman, already catalogued in this archive as `dc33-laser-tag-badge`), and shares its lineage with a separate DEF CON Singapore 2026 official badge built on the same OpenLASIR protocol.
