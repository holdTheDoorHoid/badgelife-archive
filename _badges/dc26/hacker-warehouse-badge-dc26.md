---
title: Hacker Warehouse Badge (DC26)
id: dc26-hacker-warehouse-badge-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Hacker Warehouse
  url: https://hackerwarehouse.com
summary: 'A multitool electronic badge for DEF CON 26 (2018) combining an ESP32 and an ATmega32u4 to act as a USB Rubber Ducky-style keystroke injector, Wi-Fi scanner/access point, small webserver, and Google Authenticator TOTP generator.'
functions: 'Keyboard/mouse HID payload execution (Ducky Script-compatible), Wi-Fi scanning and monitoring, rogue access point creation, a built-in webserver, RGB LED light patterns, and TOTP codes as a Google Authenticator replacement.'
look:
  colors: []
  shape: rectangle
  themes:
  - security
  - hardware tool
  - cyberpunk
tech:
  mcu: ESP32 + ATmega32u4
  leds:
    count: 14
    type: WS2812B
    note: "Described by the maker as 14 NeoPixel RGB LEDs; Hackaday's preview called them 'mini WS2812' without giving a count."
  display: 96x64 graphic full-color OLED
  connectivity:
  - wifi
  - usb
  inputs:
  - buttons
  battery: 2x AA or USB
  sao_version: v1
  sao_ports: 2
get_one:
  price: "$40+ (approx.; Hackaday described it as 'slightly more than' a USB Rubber Ducky, no exact figure given)"
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - preorder
  - purchase
  where: 'Preordered directly through Hacker Warehouse, with delivery at DEF CON 26 and post-convention shipping for remaining orders.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/hackerwarehouse/HW-DC26-Badge
  firmware_url: https://github.com/hackerwarehouse/HW-DC26-Badge
  eda_tool: null
  license: GPL-3.0
  notes: 'Both the PCB design and firmware are published in the same GitHub repo under GPL-3.0, with build/flashing documentation.'
links:
- label: github.com/hackerwarehouse/HW-DC26-Badge
  url: https://github.com/hackerwarehouse/HW-DC26-Badge
  kind: repo
- label: hackaday.com/2018/07/06/a-sneak-preview-of-the-hacker-warehouse-badge
  url: https://hackaday.com/2018/07/06/a-sneak-preview-of-the-hacker-warehouse-badge/
  kind: article
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/hackerwarehouse/HW-DC26-Badge
  title: Hacker Warehouse Badge (DC26)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 26''.'
- kind: url
  url: https://github.com/hackerwarehouse/HW-DC26-Badge
  title: hackerwarehouse/HW-DC26-Badge (GitHub README)
  accessed: '2026-09-07'
  note: 'Maker''s own repo: hardware/firmware specs, GPL-3.0 license, feature list, image URLs (badge-r1.jpg, button-labels.jpg).'
- kind: url
  url: https://hackaday.com/2018/07/06/a-sneak-preview-of-the-hacker-warehouse-badge/
  title: 'A Sneak Preview Of The Hacker Warehouse Badge (Hackaday)'
  accessed: '2026-09-07'
  note: 'Press preview confirming DEF CON 26/2018, preorder/pricing context, and feature description.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker (Hacker Warehouse) is behind two later entries in the archive: dc31-hacker-mindset-badge and dc32-garrett-hacker-warehouse-listed-for-def-con-32-no-details, both attributed to Garrett / Hacker Warehouse; this DC26 badge appears to be an earlier entry in that same maker''s series. Exact unit price and quantity made were not stated by either source, and the two source photo URLs (files.hackerwarehouse.com) were unreachable from this environment (no route to host), so no images could be saved despite the repo README linking them directly.'
last_modified_date: '2026-09-07'
---

Hacker Warehouse built this badge for DEF CON 26 (2018) as a practical security multitool rather than a purely decorative badge. Under the hood it pairs an ESP32 (for Wi-Fi scanning, monitoring, and hosting a small webserver or rogue access point) with an ATmega32u4 (for USB HID keystroke/mouse injection, Ducky Script-compatible, in the style of a USB Rubber Ducky). A 96x64 full-color OLED display and four-button d-pad give it a simple on-device UI, and it can also generate TOTP codes as a stand-in for the Google Authenticator app. Fourteen NeoPixel-style RGB LEDs handle blinky patterns, and two "Shitty Add-On" headers let it host other badges' SAOs. Power comes from two AA batteries or USB.

The badge was sold as a preorder through Hacker Warehouse's own store, with units delivered at the con and remaining orders shipped afterward; Hackaday's contemporary preview pegged the price as a bit above a standalone USB Rubber Ducky without citing an exact figure. Both the hardware design and firmware were released on GitHub under the GPL-3.0 license, alongside build documentation.

## Make your own

The `hackerwarehouse/HW-DC26-Badge` GitHub repository has the PCB schematics/design files and the ESP32 + ATmega32u4 firmware source, GPL-3.0 licensed, with instructions in the README for compiling and flashing the firmware and for customizing or expanding the hardware.

