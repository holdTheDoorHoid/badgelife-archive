---
title: CactusCon 12 Badge (2024)
id: cactuscon-2024-cactuscon-12-badge-2024
layout: badge
parent: CactusCon 12 (2024)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cactuscon-2024
year: 2024
makers:
- name: Badge Pirates
  url: https://www.badgepirates.com/
summary: The official electronic badge for CactusCon 12 (2024), an ESP32-S3 board internally called "Project NeoRogue" with dual SPI OLED displays, rotary dials, and an SAO port.
functions: Runs custom firmware (QA/demo code released; final event game/firmware not published) driving two SPI OLED displays plus an I2C OLED, WS2812B LED effects, and five buttons and two rotary dials for on-badge interaction.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: ESP32-S3
  leds:
    type: WS2812B
  display: dual SPI OLED + I2C OLED
  connectivity:
  - usb
  - i2c
  battery: 14500 cell, TP4054-class charger, MAX17048 fuel gauge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/BadgePiratesLLC/CactusCon-12
  firmware_url: https://github.com/BadgePiratesLLC/CactusCon-12/tree/main/CODE
  eda_tool: KiCad
  notes: Repo (archived by GitHub in 2026) includes KiCad CAD, Gerbers, BOM, and an interactive BOM. Only "BasicCodeForQA" firmware is present, not the final event game/firmware, and the repo carries no visible license statement.
links:
- label: badge.gallery/badges/cactuscon-12-badge
  url: https://badge.gallery/badges/cactuscon-12-badge
  kind: website
  archived: https://web.archive.org/web/20260912174042/https://badge.gallery/badges/cactuscon-12-badge
- label: BadgePiratesLLC/CactusCon-12 (GitHub)
  url: https://github.com/BadgePiratesLLC/CactusCon-12
  kind: repo
  archived: https://web.archive.org/web/20260912174114/https://github.com/BadgePiratesLLC/CactusCon-12
- label: BadgePirates badge catalog
  url: https://docs.badgepirates.com/catalog/
  kind: doc
  archived: https://web.archive.org/web/20260910225903/https://docs.badgepirates.com/catalog/#help-us-fill-the-gaps
images:
- file: assets/images/badges/cactuscon-2024/cactuscon-12-badge-2024/869d4e2520.jpg
  source: https://github.com/BadgePiratesLLC/CactusCon-12
  credit: Badge Pirates
  caption: CactusCon 12 badge (Project NeoRogue), front
  archived: https://web.archive.org/web/20260912174114/https://github.com/BadgePiratesLLC/CactusCon-12
- file: assets/images/badges/cactuscon-2024/cactuscon-12-badge-2024/6c028a83ab.jpg
  source: https://github.com/BadgePiratesLLC/CactusCon-12
  credit: Badge Pirates
  caption: CactusCon 12 badge (Project NeoRogue), back
  archived: https://web.archive.org/web/20260912174114/https://github.com/BadgePiratesLLC/CactusCon-12
contact: {}
notes:
- Sweep found the title as "CactusCon 12 Badge (2024)"; the maker's repo just calls the project "CactusCon12" internally, and the design's working name in the CAD/QA code is "Project NeoRogue."
- No price, production quantity, or distribution method found in any source checked.
status: listed
sources:
- kind: url
  url: https://badge.gallery/badges/cactuscon-12-badge
  title: CactusCon 12 Badge (2024)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''CactusCon 2024''.'
  archived: https://web.archive.org/web/20260912174042/https://badge.gallery/badges/cactuscon-12-badge
- kind: url
  url: https://github.com/BadgePiratesLLC/CactusCon-12
  title: BadgePiratesLLC/CactusCon-12
  accessed: '2026-09-10'
  note: Maker repo confirms event (CactusCon 12, cc12), design files (KiCad, Gerbers, BOM, iBOM), and photos of the assembled badge under DOCS/.
  archived: https://web.archive.org/web/20260912174114/https://github.com/BadgePiratesLLC/CactusCon-12
- kind: url
  url: https://badge.gallery/addons/cactuscon-12-badge/esp32-s3-wroom-projectneorogue-core
  title: ESP32-S3 WROOM ProjectNeoRogue core
  accessed: '2026-09-10'
  note: Confirms MCU and internal project name "ProjectNeoRogue".
  archived: https://web.archive.org/web/20260912174313/https://badge.gallery/addons/cactuscon-12-badge/esp32-s3-wroom-projectneorogue-core
- kind: url
  url: https://docs.badgepirates.com/catalog/
  title: Badge Catalog - BadgePirates Documents
  accessed: '2026-09-10'
  note: Maker catalog lists the CactusCon 12 badge and links the same GitHub repo; no price/quantity given.
  archived: https://web.archive.org/web/20260910225903/https://docs.badgepirates.com/catalog/#help-us-fill-the-gaps
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Confirmed as a real, maker-published badge (Badge Pirates, ESP32-S3, "Project NeoRogue") via the maker's own GitHub repo and catalog, so this is not just a search-snippet rumor. Could not find price, quantity made, or how it was distributed (free con badge vs. purchased) on any page checked; get_one fields left empty. Firmware repo has QA/demo code only, not the shipped event firmware, and carries no visible license, so open_source is marked partial rather than yes.
last_modified_date: '2026-09-10'
model:
  file: assets/models/cactuscon-2024/cactuscon-12-badge-2024.glb
  method: kicad
  source_file: CAD/CactusCon12.kicad_pcb
  generated: '2026-09-10'
  bytes: 510128
---

The CactusCon 12 badge, internally called "Project NeoRogue" by its designers, was the official electronic badge for CactusCon 12, held February 16-17, 2024 at the Mesa Convention Center in Arizona. It was designed by Badge Pirates, a badge-design collective that has built conference badges for numerous events since 2018.

The badge is built around an ESP32-S3 WROOM module and carries two SPI OLED displays alongside a separate I2C OLED, five buttons, and two rotary dial inputs, giving it a fairly involved on-badge interface for its era. It uses WS2812B addressable LEDs for lighting effects, charges a 14500 cell through a TP4054-class charge controller with MAX17048 fuel-gauge monitoring, and connects to a host over USB-C via a CH340N serial converter; it also includes a MicroSD slot and a v1.69bis SAO connector for add-on modules.

## Make your own

Badge Pirates published the hardware design for this badge on GitHub (archived in 2026, now read-only) with KiCad source files, Gerbers, a BOM and interactive BOM, and reference material for the ESP32-S3. Only a basic "BasicCodeForQA" firmware sketch is included in the repository; the actual game or event firmware that shipped on badges was not published, and the repository does not carry an explicit open-source license.
