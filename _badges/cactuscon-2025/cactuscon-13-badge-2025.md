---
title: CactusCon 13 Badge (2025)
id: cactuscon-2025-cactuscon-13-badge-2025
layout: badge
parent: CactusCon 13 (2025)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cactuscon-2025
year: 2025
makers:
- name: Badge Pirates
  url: https://www.badgepirates.com/
summary: The official electronic badge for CactusCon 13 (Feb 14-15, 2025, Mesa Convention Center, AZ), built around an ESP32-S3 with a touch SPI display.
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: ESP32-S3
  leds: null
  display: SPI TFT with touch
  connectivity:
  - wifi
  - ble
  battery: 2x 14500 with LiPo charging and fuel gauge
  sao_version: null
  inputs:
  - touch
  - buttons
  - rotary encoder
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to attendees, speakers, staff and "Mafia" role variants at CactusCon 13.
make_your_own:
  open_source: true
  hardware_url: https://github.com/BadgePiratesLLC/CactusCon13
  firmware_url: null
  eda_tool: KiCad
links:
- label: badge.gallery/badges/cactuscon-13-badge
  url: https://badge.gallery/badges/cactuscon-13-badge
  kind: website
- label: BadgePiratesLLC/CactusCon13 (GitHub)
  url: https://github.com/BadgePiratesLLC/CactusCon13
  kind: repo
- label: Badge Pirates
  url: https://www.badgepirates.com/
  kind: website
- label: BadgePirates catalog entry
  url: https://docs.badgepirates.com/catalog/
  kind: doc
- label: BadgePirates ESP32-S3 platform reference
  url: https://docs.badgepirates.com/platform/esp32-s3/
  kind: doc
images:
- file: assets/images/badges/cactuscon-2025/cactuscon-13-badge-2025/e96025a9c6.png
  source: https://www.badgepirates.com/
  credit: Badge Pirates
  caption: CactusCon 13 (2025) badge
contact: {}
notes:
- Official conference badge for CactusCon 13 (2025), made by Badge Pirates. Found by the event-year sweep, task con-layerone.
- Badge Pirates' own platform docs describe the shared ESP32-S3 hardware (used by CactusCon 13, CactusCon 14, and BSidesKC 2025/2026) as having a 320x240 SPI display and 6 NeoPixels, but did not confirm these specifics apply to the CC13 board itself, so LED count/type is left blank rather than assumed.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/cactuscon-13-badge
  title: CactusCon 13 Badge (2025)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''CactusCon 2025''.'
- kind: url
  url: https://github.com/BadgePiratesLLC/CactusCon13
  title: 'GitHub - BadgePiratesLLC/CactusCon13: CactusCon13 Badge Repo'
  accessed: '2026-09-10'
  note: Confirmed maker, MIT-licensed open hardware (KiCad CAD, Gerbers, 3D-print files, STEP exports); no README with detailed specs found.
- kind: url
  url: https://www.badgepirates.com/
  title: Badge Pirates - Making badges for fun and no profit
  accessed: '2026-09-10'
  note: Portfolio listing confirming maker and providing the badge photo used here.
- kind: url
  url: https://docs.badgepirates.com/catalog/
  title: Catalog - BadgePirates Documents
  accessed: '2026-09-10'
  note: Confirms the CactusCon 13 (2025) repo link, listed as "Project CC13".
- kind: url
  url: https://docs.badgepirates.com/platform/esp32-s3/
  title: ESP32-S3 Reference - BadgePirates Documents
  accessed: '2026-09-10'
  note: Confirms ESP32-S3 hardware platform shared across CactusCon 13/14 and BSidesKC 2025/2026 badges; gives chip, MCU, and general shared spec (display/LEDs/battery) but does not confirm all specifics for the CC13 variant specifically.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Core facts (maker, event/year, MCU, display, battery, open-source status) confirmed via badge.gallery, the maker's own GitHub repo, and BadgePirates' own site/docs. Exact LED count/type, price, and quantity produced were not found in any source and are left blank rather than assumed. No firmware repo link was found (hardware repo only contains CAD/3D-print/reference docs).
last_modified_date: '2026-09-10'
model:
  file: assets/models/cactuscon-2025/cactuscon-13-badge-2025.glb
  method: kicad
  source_file: CAD-OuterBoard/Project-CC13_outer_v2_Attendee.kicad_pcb
  generated: '2026-09-10'
  bytes: 626312
---

The CactusCon 13 Badge is the official electronic conference badge for CactusCon 13, held February 14-15, 2025 at the Mesa Convention Center in Arizona. It was designed and produced by Badge Pirates, a group known for building conference badges for numerous hacker cons since 2018. The badge is built around an ESP32-S3 (WROOM, N16-class) microcontroller and features an SPI TFT display with touch input, two push buttons, and a rotary dial, along with USB serial programming, a microSD card slot, and a buzzer. Power comes from dual 14500 cells with LiPo charging and fuel-gauge circuitry, and the design uses interchangeable outer boards to distinguish attendee, speaker, staff, and "Mafia" role variants.

The hardware is open source under the MIT license, with KiCad CAD files, Gerbers, 3D-print assets, and STEP mechanical exports published in the BadgePiratesLLC/CactusCon13 GitHub repository. Badge Pirates' own documentation site groups this badge with CactusCon 14 and the BSidesKC 2025/2026 badges as sharing a common ESP32-S3 hardware platform, though the specific LED count and firmware for the CC13 board were not confirmed in available sources.

## Make your own

Hardware design files (KiCad CAD, Gerbers, 3D-print/STEP mechanical files) are published at https://github.com/BadgePiratesLLC/CactusCon13 under the MIT license. No dedicated firmware repository was found for this badge.
