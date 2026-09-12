---
title: CactusCon 14 Badge (2026)
id: cactuscon-2026-cactuscon-14-badge-2026
layout: badge
parent: CactusCon 14 (2026)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cactuscon-2026
year: 2026
makers:
- name: Badge Pirates
  url: https://www.badgepirates.com/
summary: The official electronic badge for CactusCon 14 (Feb 2026), an ESP32-S3 handheld with a MicroPython/LVGL UI built around a turn-based creature-battle game with BLE badge-to-badge battles and chat.
functions: Turn-based creature-battle game (15 creatures, 5 evolution lines, 42 moves), BLE badge-to-badge battles and encrypted chat, a 14-item achievement system, and OTA firmware updates.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - wearable
tech:
  mcu: ESP32-S3
  leds:
    count: 6
    type: WS2812B
    note: Plus a separate single-color status LED on GPIO 21.
  display: null
  connectivity:
  - wifi
  - ble
  - usb
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
  open_source: 'yes'
  hardware_url: https://github.com/BadgePiratesLLC/CactusCon14
  firmware_url: https://github.com/cactuscon/cactuscon14
  eda_tool: KiCad
  notes: Hardware under CERN-OHL-S v2; firmware under MIT. Hardware repo includes schematics, KiCad project, gerbers, an interactive BOM, and STL/3MF files for 3D-printed enclosure parts.
links:
- label: github.com/jordanlanham52/CactusCon-14-Badge-Writeup-Walkthrough
  url: https://github.com/jordanlanham52/CactusCon-14-Badge-Writeup-Walkthrough
  kind: repo
  archived: https://web.archive.org/web/20260912174545/https://github.com/jordanlanham52/CactusCon-14-Badge-Writeup-Walkthrough
- label: badgepirates.com (maker site)
  url: https://www.badgepirates.com/
  kind: website
  archived: https://web.archive.org/web/20260810184033/https://badgepirates.com/
- label: BadgePiratesLLC/CactusCon14 (hardware design files)
  url: https://github.com/BadgePiratesLLC/CactusCon14
  kind: repo
  archived: https://web.archive.org/web/20260523082533/https://github.com/BadgePiratesLLC/CactusCon14
- label: cactuscon/cactuscon14 (badge game firmware)
  url: https://github.com/cactuscon/cactuscon14
  kind: repo
  archived: https://web.archive.org/web/20260912174730/https://github.com/cactuscon/cactuscon14
- label: CC14 resources hub (docs.badgepirates.com)
  url: https://docs.badgepirates.com/resources/cc14/
  kind: doc
  archived: https://web.archive.org/web/20260910225913/https://docs.badgepirates.com/resources/cc14/
- label: 'CC14 resources: schematics, STLs, gerbers, and more'
  url: https://blog.badgepirates.com/cc14-resources/
  kind: article
  archived: https://web.archive.org/web/20260310210845/https://blog.badgepirates.com/cc14-resources/
images:
- file: assets/images/badges/cactuscon-2026/cactuscon-14-badge-2026/6c17b35678.jpg
  source: https://www.badgepirates.com/
  credit: Badge Pirates
  caption: CactusCon 14 badge, hero shot from the maker's site
  archived: https://web.archive.org/web/20260810184033/https://badgepirates.com/
contact: {}
notes:
- ESP32-S3 badge with an LVGL/MicroPython UI, a Pokemon-style creature-battle game with BLE badge-to-badge battles/chat, NeoPixel LEDs, achievements and OTA updates. Found by the event-year sweep, task con-layerone.
- The sweep's only link was a third-party attendee write-up/security-teardown (jordanlanham52's repo), not the maker's own page; the maker (Badge Pirates) and their hardware/firmware repos were confirmed separately.
status: released
sources:
- kind: url
  url: https://github.com/jordanlanham52/CactusCon-14-Badge-Writeup-Walkthrough
  title: CactusCon 14 Badge (2026)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''CactusCon 2026''.'
  archived: https://web.archive.org/web/20260912174545/https://github.com/jordanlanham52/CactusCon-14-Badge-Writeup-Walkthrough
- kind: url
  url: https://www.badgepirates.com/
  title: Badge Pirates
  accessed: '2026-09-08'
  note: Confirms Badge Pirates as maker, hero image, open-source hardware link.
  archived: https://web.archive.org/web/20260810184033/https://badgepirates.com/
- kind: url
  url: https://blog.badgepirates.com/cc14-resources/
  title: 'CC14 Resources: schematics, STLs, gerbers, and more'
  accessed: '2026-09-08'
  note: Points to the BadgePiratesLLC/CactusCon14 hardware repo as the canonical design-files location.
  archived: https://web.archive.org/web/20260310210845/https://blog.badgepirates.com/cc14-resources/
- kind: url
  url: https://github.com/BadgePiratesLLC/CactusCon14
  title: BadgePiratesLLC/CactusCon14
  accessed: '2026-09-08'
  note: 'Hardware repo: KiCad files, schematics, gerbers, STL/3MF enclosure files; CERN-OHL-S v2 hardware / MIT software license.'
  archived: https://web.archive.org/web/20260523082533/https://github.com/BadgePiratesLLC/CactusCon14
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Maker, MCU, LED count/type, connectivity, game features, and open-source repos confirmed from Badge Pirates'' own site and GitHub orgs. Could not confirm: display (if any), battery/power, SAO header presence/version, price, quantity made, or distribution/availability -- the maker''s site and repo READMEs do not state these, and no storefront listing was found. The attendee write-up (jordanlanham52) is a third-party security teardown, not an official source, but its technical findings (ESP32-S3, WS2812B count, MicroPython+LVGL, BLE chat) line up with the maker''s own description and were used for tech.* fields since the maker''s pages don''t give that level of detail themselves.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/cactuscon-2026/cactuscon-14-badge-2026.glb
  method: kicad
  source_file: CAD/CC14_Outer.kicad_pcb
  generated: '2026-09-10'
  bytes: 85100
---

The CactusCon 14 badge (CC14) is the official electronic badge for CactusCon 14, held February 20, 2026 in the Phoenix, Arizona area, made by Badge Pirates. It's an ESP32-S3 handheld running MicroPython with an LVGL touch/button UI, built around a turn-based creature-battle game in the style of Pokemon: fifteen creatures across five evolution lines, forty-two battle moves, and badge-to-badge battles and chat carried over BLE with AES-128-CBC encryption. A fourteen-item achievement system and over-the-air firmware updates round out the software side; six NeoPixel (WS2812B) LEDs plus a separate status LED handle the badge's lighting.

Badge Pirates published the hardware as open source (CERN-OHL-S v2) with schematics, KiCad source, gerbers, an interactive BOM, and 3D-printable enclosure files in a dedicated GitHub repository, and a separate firmware repository under the CactusCon GitHub org carries the game code (MIT licensed). Neither the maker's site nor the repositories state price, production quantity, or how the badge was distributed to attendees.

This entry was originally created from an automated sweep that only surfaced a third-party attendee write-up -- a detailed reverse-engineering teardown by Jordan Lanham documenting the badge's firmware, unlock codes, and a predictable RNG in the battle engine, rather than any official page. Cross-checking against Badge Pirates' own site and GitHub orgs confirmed the badge is real and filled in the maker and technical details; the teardown itself remains linked as a secondary source.
