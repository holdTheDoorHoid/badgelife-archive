---
title: Badgy
id: other-badgy
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2017
makers:
- name: w4ilun (squarofumi)
  url: https://hackaday.io/w4ilun
summary: A rechargeable, coin-cell-powered e-paper WiFi badge/name-tag built around an ESP8266, designed as an open hardware alternative to a printed name badge.
functions: Shows a name-tag or any custom e-paper content; can act as a WiFi smart-home remote, weather/news display, scoreboard, or "deauther" via its ESP8266, with OTA updates, a WYSIWYG designer GUI, and IFTTT support.
look:
  colors:
  - black
  - white
  shape: rectangle
  themes:
  - wearable
  - hardware tool
  - minimalist
tech:
  mcu: ESP8266 (ESP-12E)
  leds: null
  display: 2.9" e-paper (296x128, 2-bit 4-color grayscale on Rev 2C)
  connectivity:
  - wifi
  battery: Rechargeable LIR2450 coin cell with USB charging
  sao_version: none
get_one:
  price: $29.99
  price_usd: 29.99
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold assembled via the maker's Tindie store (squarofumi); out of stock since December 2019.
make_your_own:
  open_source: true
  hardware_url: https://github.com/sqfmi/badgy
  firmware_url: https://github.com/sqfmi/badgy
  eda_tool: KiCad
links:
- label: hackaday.io/project/28800-badgy
  url: https://hackaday.io/project/28800-badgy
  kind: hackaday
  archived: https://web.archive.org/web/20251005110119/https://hackaday.io/project/28800-badgy
- label: github.com/sqfmi/badgy
  url: https://github.com/sqfmi/badgy
  kind: repo
  archived: https://web.archive.org/web/20260616225051/https://github.com/sqfmi/badgy
- label: Tindie - Badgy IoT Badge
  url: https://www.tindie.com/products/squarofumi/badgy-iot-badge/
  kind: store
images:
- file: assets/images/badges/other/badgy/1205928af3.jpg
  source: https://www.tindie.com/products/squarofumi/badgy-iot-badge/
  credit: squarofumi (w4ilun)
  caption: Badgy IoT badge product photo, e-ink display showing badge name
- file: assets/images/badges/other/badgy/125c184d4f.jpg
  source: https://hackaday.io/project/28800-badgy
  credit: w4ilun
  caption: Badgy e-ink WiFi badge, Hackaday.io project photo
  archived: https://web.archive.org/web/20251005110119/https://hackaday.io/project/28800-badgy
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/28800-badgy
  title: Badgy
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
  archived: https://web.archive.org/web/20251005110119/https://hackaday.io/project/28800-badgy
- kind: url
  url: https://hackaday.io/project/28800-badgy
  title: badgy | Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed description, maker (w4ilun), submission date (2017-12-28), header/og image.
  archived: https://web.archive.org/web/20251005110119/https://hackaday.io/project/28800-badgy
- kind: url
  url: https://github.com/sqfmi/badgy
  title: sqfmi/badgy
  accessed: '2026-09-07'
  note: Hardware/firmware repo; MCU, display, battery, MIT license, hardware revisions Rev 1 through Rev 2C (Sept 2019).
  archived: https://web.archive.org/web/20260616225051/https://github.com/sqfmi/badgy
- kind: url
  url: https://www.tindie.com/products/squarofumi/badgy-iot-badge/
  title: Badgy - IoT Badge (Tindie)
  accessed: '2026-09-07'
  note: Price ($29.99, volume pricing), out-of-stock status since Dec 2019, product photo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Badgy was not made for a specific hacker convention; it was submitted to Hackaday's "Coin Cell Challenge" contest (a Hackaday.io online competition, not a physical con) on 2017-12-28, then sold as a general-purpose IoT name badge on Tindie. No matching event exists in events.yml, so event is left as "other". LED count/type not stated by any source (device has no addressable LEDs, only the e-paper display). Quantity made not stated.
last_modified_date: '2026-09-07'
---

Badgy is an open-hardware electronic name badge built around an ESP8266 (ESP-12E) module and a 2.9" e-paper display, created by w4ilun (Tindie store squarofumi) and first shown on Hackaday.io in December 2017 as an entry to Hackaday's Coin Cell Challenge. Rather than being made for a specific hacker convention, it was designed as a general-purpose, rechargeable e-paper "smart badge": it runs on a rechargeable LIR2450 coin cell charged over USB, uses a 5-way tactile switch for input, and connects to WiFi for OTA firmware updates, IFTTT integration, and a browser-based WYSIWYG designer for laying out the badge's screen content.

Because the display just shows whatever image or text is pushed to it, the maker pitched Badgy for uses well beyond a static name tag: a smart-home remote and dashboard, a weather or news display, a scoreboard, or a WiFi "deauther," among other ESP8266 projects. It was sold fully assembled through the squarofumi Tindie store for $29.99 (with volume discounts down to $26.99 for 100+ units), but has been listed out of stock since December 2019.

## Make your own

Hardware and firmware are both open source (MIT license) at [github.com/sqfmi/badgy](https://github.com/sqfmi/badgy), which includes KiCad hardware design files spanning revisions from the original Rev 1 through Rev 2C (September 2019), plus example firmware for the ESP8266. The board is built primarily with 0805 footprints to keep hand-soldering practical.
