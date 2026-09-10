---
title: HackGDL 2025 Minino Badge
id: other-hackgdl-2025-minino-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2025
makers:
- name: Electronic Cats
  url: https://electroniccats.com/store/badge-hackgdl/
summary: The official conference badge for Hack GDL 2025, built by Electronic Cats on their Minino platform with BLE and Wi-Fi, an OLED screen, and a pre-installed digital Tamagotchi game.
functions: Boots into a modular BLE/Wi-Fi app system with a pre-installed "Digital Tamagotchi" game (using the TamaLib emulator); four buttons and a buzzer for interaction; SAO connector for expansion.
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: ESP32-S3
  leds:
    count: 3
    type: NeoPixel
    note: ''
  display: OLED
  connectivity:
  - wifi
  - ble
  - usb
  battery: 3x AAA (also runs on USB-C power)
  sao_version: null
get_one:
  price: $20 (60% off a $50 list price)
  price_usd: 20
  quantity: ''
  availability: limited
  distribution:
  - purchase
  where: Sold on the Electronic Cats online store, listed as available on backorder.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/ElectronicCats/badge-hackgdl-2025
  firmware_url: https://github.com/ElectronicCats/badge-hackgdl-2025
  eda_tool: KiCad
links:
- label: badge.gallery/years/2025
  url: https://badge.gallery/years/2025
  kind: website
- label: Electronic Cats store - Badge HackGDL 2025
  url: https://electroniccats.com/store/badge-hackgdl/
  kind: store
- label: badge-hackgdl-2025 (GitHub)
  url: https://github.com/ElectronicCats/badge-hackgdl-2025
  kind: repo
- label: HackGDL 2025 - badge.gallery
  url: https://badge.gallery/events/hackgdl-2025
  kind: website
images:
- file: assets/images/badges/other/hackgdl-2025-minino-badge/e00d6123be.png
  source: https://electroniccats.com/store/badge-hackgdl/
  credit: Electronic Cats
  caption: The HackGDL 2025 Minino badge, product photo
contact: {}
notes:
- Electronic Cats-made 'Minino' badge for HackGDL 2025 in Guadalajara, Mexico, per the badge.gallery compendium (not independently opened beyond the aggregator listing). (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task general-2025.
- Confirmed via the maker's own store page and GitHub repo. No matching HackGDL event id exists in _data/events.yml; the badge was made for Hack GDL 2025 in Guadalajara, Mexico. Left event as 'other' pending a dedicated event entry.
status: released
sources:
- kind: url
  url: https://badge.gallery/years/2025
  title: HackGDL 2025 Minino Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2025); event read as ''HackGDL 2025''.'
- kind: url
  url: https://electroniccats.com/store/badge-hackgdl/
  title: Badge HackGDL 2025 - Official Hack GDL Event Badge
  accessed: '2026-09-10'
  note: 'Maker storefront: price, availability, chip, LEDs, display, battery, buttons, SAO, licensing.'
- kind: url
  url: https://github.com/ElectronicCats/badge-hackgdl-2025
  title: badge-hackgdl-2025 (GitHub)
  accessed: '2026-09-10'
  note: 'Maker repo: hardware/firmware confirmed open source, KiCad files, licenses (CERN-OHL v1.2 hardware, AGPL v3.0 firmware).'
- kind: url
  url: https://badge.gallery/events/hackgdl-2025
  title: HackGDL 2025 - Hacker Con Badges - badge.gallery
  accessed: '2026-09-10'
  note: Corroborating aggregator summary of features.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Fact-check pass (2026-09-10): re-fetched the store page, GitHub repo/README, and both badge.gallery pages. Corrected two unsupported claims from the prior pass: tech.display was "0.96\" OLED" but no source (store page, repo README, or the Minino platform README) states a screen size, only "Integrated OLED Screen" — trimmed to "OLED". look.themes listed cat/retro computer/security but none of the sources describe the badge''s look or mascot in those terms (the "cat" theme conflated the maker''s company name, Electronic Cats, with an actual visual theme) — cleared to empty. All other fields (mcu, LEDs, connectivity, battery, price, availability, open-source status, licenses, KiCad tooling, TamaLib-based Tamagotchi game) are directly stated on the maker''s own store page and/or GitHub README and are confirmed. sao_version and exact quantity made remain unstated anywhere found. No HackGDL event exists yet in _data/events.yml, so event stays "other"; the con is Hack GDL 2025, held in
    Guadalajara, Mexico.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/hackgdl-2025-minino-badge.glb
  method: kicad
  source_file: hardware/badge-hackgdl-2025.kicad_pcb
  generated: '2026-09-10'
  bytes: 300524
---

The Badge HackGDL 2025 is Electronic Cats' official conference badge for Hack GDL 2025, held in Guadalajara, Mexico. Built on the company's "Minino" hardware platform around an ESP32-S3, it pairs BLE and Wi-Fi with an OLED screen, three NeoPixel RGB LEDs, four buttons, and a buzzer, and ships with a case and a pre-installed "Digital Tamagotchi" game running on the TamaLib emulator. It runs on three AAA batteries or USB-C power and carries a Shitty Add-On (SAO) connector for expansion.

Electronic Cats sold the badge through their online store for $20 (discounted from a $50 list price), listed as available on backorder as of this check. Hardware and firmware are both open source: schematics and a KiCad-based design are published under the CERN Open Hardware License v1.2, and the ESP-IDF-based Minino firmware is released under the GNU AGPL v3.0, all in the `badge-hackgdl-2025` GitHub repository.

No HackGDL event entry currently exists in the archive's events list, so this entry stays filed under "other" pending one being added.
