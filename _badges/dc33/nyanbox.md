---
title: nyanBOX
id: dc33-nyanbox
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: jbohack & zr_crackiin
  url: https://github.com/jbohack/nyanBOX
summary: 'A handheld ESP32-based wireless security toolkit from Nyan Devices, worn/carried around DEF CON 33 and tagged by its makers as part of #BadgeLife.'
functions: WiFi Deauther, WLAN Jammer, Beacon Spam, BLE Jammer, BLE Spammer, BLE Scan, Flipper Scan, WiFi Scan, BLE Spoofer, Scanner, Analyzer, Proto Kill Mode, Sour Apple
look:
  colors: [multicolor, black]
  shape: rectangle
  themes: [radio, security, hardware tool]
tech:
  mcu: ESP32-WROOM-32U
  leds: null
  display: 0.96" OLED
  connectivity: [wifi, ble, bluetooth]
  battery: LiPo 2500 mAh
  sao_version: none
get_one:
  price: '$220 assembled / $330 complete kit'
  price_usd: null
  quantity: ''
  availability: available
  availability_note: 'Listed for sale on shop.nyandevices.com as of 2026-09-06.'
  distribution: [purchase]
  where: 'Purchased directly from shop.nyandevices.com (Nyan Devices).'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/jbohack/nyanBOX
  eda_tool: null
links:
- label: github.com/jbohack/nyanBOX
  url: https://github.com/jbohack/nyanBOX/
  kind: repo
- label: nyandevices.com
  url: https://nyandevices.com
  kind: website
- label: shop.nyandevices.com
  url: https://shop.nyandevices.com
  kind: store
images:
  - file: assets/images/badges/dc33/nyanbox/fce017f6ce.jpg
    source: "https://shop.nyandevices.com"
    credit: "Nyan Devices"
    caption: "nyanBOX device, multicolor edition"
  - file: assets/images/badges/dc33/nyanbox/8b1188153a.jpg
    source: "https://shop.nyandevices.com"
    credit: "Nyan Devices"
    caption: "nyanBOX device, black edition"
contact:
  emails:
  - jbohack@lullaby.cafe
notes:
- made by jbohack and zr_crackiin
status: released
sources:
- kind: sheet
  event: dc33
  row: 8
  updated: 6/14/2025 0:36:16
- kind: url
  url: https://github.com/jbohack/nyanBOX/
  title: 'jbohack/nyanBOX: GitHub repository'
  accessed: '2026-09-06'
  note: 'Confirmed maker names, MCU (ESP32-WROOM-32U), display, feature list, and #badgelife/defcon33 topic tags on the repo.'
- kind: url
  url: https://nyandevices.com
  title: 'Nyan Devices'
  accessed: '2026-09-06'
  note: 'Confirmed battery (2500 mAh, full-day runtime), USB-C charging, $220 price, and availability.'
- kind: url
  url: https://shop.nyandevices.com
  title: 'Nyan Devices shop'
  accessed: '2026-09-06'
  note: 'Confirmed $330.03 price for the "Complete Kit" listing, in-stock status, and product photos (multicolor and black editions).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    The maker's own site and GitHub repo confirm the device and its specs, but neither
    explicitly documents its role at DEF CON 33 beyond the GitHub topic tags "badge",
    "badgelife", and "defcon33" — no photo or post was found showing it worn or sold
    on-site. Two different prices are advertised ($220 for an assembled unit on the
    main site vs $330.03 for a "Complete Kit" on the storefront); both are recorded
    rather than picking one. LED count/type, hardware open-source status (gerbers/BOM),
    EDA tool, license, and quantity made were not stated anywhere found and are left
    empty. The three onboard NRF24 modules mentioned by the maker are not captured
    under tech.connectivity because they don't map cleanly to the controlled vocabulary
    (they're 2.4GHz RF, not sub-ghz).
last_modified_date: '2026-09-06'
---

nyanBOX is a handheld wireless-security toolkit built by jbohack and zr_crackiin under the name Nyan Devices. It's built around an ESP32-WROOM-32U with a 0.96" OLED display and three onboard NRF24 modules, and runs a menu-driven firmware with more than a dozen built-in tools — WiFi and BLE scanning, deauthentication, beacon spam, BLE jamming/spoofing, a "Sour Apple" mode, and a Flipper Zero scan mode — aimed at letting people explore RF/WiFi/BLE security without writing code. It's powered by a 2500 mAh LiPo battery over USB-C for roughly a full day of use.

The project's GitHub repository tags it with "badge," "badgelife," and "defcon33," placing it in DEF CON 33's badge scene, though no source found documents exactly how it circulated on-site (worn, sold, or given away at the con) versus through the maker's own storefront. It is sold directly by Nyan Devices at shop.nyandevices.com, currently listed at $220 for an assembled unit on the main site and $330.03 for a "Complete Kit" bundle on the store, in multicolor and black color options. Firmware is open source on GitHub; the hardware design files (PCB/gerbers/BOM) are not published there, so the project counts as only partially open source.

## Make your own

Firmware is available from the GitHub repository (github.com/jbohack/nyanBOX), which also documents the ESP Web Tools-based flashing process. No hardware files (schematic, PCB, or BOM) were found published, so building your own board from scratch is not currently documented by the maker.
