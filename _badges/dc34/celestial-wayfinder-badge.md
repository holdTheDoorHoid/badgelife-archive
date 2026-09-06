---
title: Celestial Wayfinder Badge
id: dc34-celestial-wayfinder-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: WyrdWyrks
  url: https://wyrdwyrks.com/celestial-wayfinder/
summary: A handheld, battery-powered beacon that shares your GPS location and short status messages with other units over an encrypted LoRa mesh, using a ring of 61 WS2812B LEDs as a compass pointing toward other users.
functions: Ping location-tagged messages over a LoRa mesh. A ring of LEDs acts as the compass leading the way. Also includes games, a flashlight mode, and standalone (no-phone) operation.
look:
  colors: []
  shape: null
  themes:
  - radio
  - space
  - hardware tool
tech:
  mcu: ESP32-S3
  leds:
    count: 61
    type: WS2812B
    note: forms a ring acting as a compass pointing toward other users
  display: 128x128 OLED (SH1107)
  connectivity:
  - wifi
  - ble
  - usb
  - lora
  - gps
  battery: 18650 lithium-ion cell
  sao_version: null
get_one:
  price: 'Complete: $150 DIY: $125'
  price_usd: 150.0
  quantity: ''
  availability: unknown
  availability_note: 'checked 2026-09-06: store page did not state stock status'
  distribution:
  - purchase
  where: Sold directly via the maker's storefront at wyrdwyrks.com.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/WyrdWyrks/Wayfinder-CAD
  firmware_url: https://github.com/WyrdWyrks/Celestial-Wayfinder
  eda_tool: null
  license: MIT
  notes: Firmware repo covers three hardware revisions (v1-v3); no BOM or Gerber files found in the visible repo listing.
links:
- label: wyrdwyrks.com/celestial-wayfinder.html
  url: https://wyrdwyrks.com/celestial-wayfinder.html
  kind: store
- label: github.com/Blake-Ballew/Celestial-Wayfinder
  url: https://github.com/Blake-Ballew/Celestial-Wayfinder
  kind: repo
- label: wyrdwyrks.com/celestial-wayfinder
  url: https://wyrdwyrks.com/celestial-wayfinder/
  kind: store
- label: github.com/WyrdWyrks/Celestial-Wayfinder
  url: https://github.com/WyrdWyrks/Celestial-Wayfinder
  kind: repo
- label: www.youtube.com/watch?v=4n-zAqWz_Tc
  url: https://www.youtube.com/watch?v=4n-zAqWz_Tc
  kind: video
- label: github.com/WyrdWyrks/esp32-utilities
  url: https://github.com/WyrdWyrks/esp32-utilities
  kind: repo
- label: github.com/WyrdWyrks/Wayfinder-CAD
  url: https://github.com/WyrdWyrks/Wayfinder-CAD
  kind: repo
images:
- file: assets/images/badges/dc34/celestial-wayfinder-badge/3df887f2d2.png
  source: "https://wyrdwyrks.com/celestial-wayfinder/"
  credit: "WyrdWyrks"
  caption: "Celestial Wayfinder V3 badge"
- file: assets/images/badges/dc34/celestial-wayfinder-badge/51edea7416.jpg
  source: "https://wyrdwyrks.com/celestial-wayfinder/"
  credit: "WyrdWyrks"
  caption: "Close-up of the LED compass ring lit up"
contact:
  emails:
  - Blakeb130@gmail.com
  - blakeb130@gmail.com
  - wyrdwyrks@mastodon.social
  discord: therisendead
  raw:
  - 'Mastodon: @'
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 23
  updated: 6/22/2026 20:21:06
  listing: New
- kind: sheet
  event: dc34
  row: 29
  updated: 7/5/2026 15:40:55
  listing: Update to Existing
- kind: url
  url: https://wyrdwyrks.com/celestial-wayfinder/
  title: "Celestial Wayfinder - WyrdWyrks"
  accessed: '2026-09-06'
  note: "Primary source for summary, features, LEDs, MCU, display, price, and gallery images."
- kind: url
  url: https://github.com/WyrdWyrks/Celestial-Wayfinder
  title: "WyrdWyrks/Celestial-Wayfinder"
  accessed: '2026-09-06'
  note: "Confirmed hardware revisions (v1-v3), LoRa module (SX127x, 915 MHz), power system, magnetometer options, MIT license; no BOM/Gerbers visible."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Maker''s own store page and GitHub repo confirm core facts. Quantity made and current stock status not stated anywhere found; left empty. No SAO header mentioned by the maker, so tech.sao_version left null. Set status to "released" since the maker sells it directly and documents it as a finished v3 device; the community sheet listed it as "New" then "Update to Existing" for DC34 (2026).'
last_modified_date: '2026-09-06'
---

The Celestial Wayfinder is a handheld, battery-powered LoRa mesh device from WyrdWyrks built for finding friends and sending short encrypted messages at festivals and outdoor events without needing a phone or cell signal, at roughly 750 meters of range. Its most distinctive feature is a ring of 61 WS2812B LEDs that lights up as a compass, pointing the wearer toward the location of another unit that pinged them.

The current (v3) hardware runs on an ESP32-S3 with a 128x128 OLED display, GPS, a magnetometer, a dual IMU, five mechanical switches plus a rotary encoder, haptic feedback, and a piezo buzzer, all powered by a single 18650 lithium-ion cell. Earlier revisions (v1 and v2) used a plain ESP32 with smaller monochrome OLEDs and a 31-LED compass ring. Beyond messaging and navigation, the device also runs small games and a flashlight mode.

WyrdWyrks sells the Wayfinder directly through their own site for $150 assembled or $125 as a DIY kit, and publishes the firmware, a core ESP32 utility library, and CAD files for the enclosure on GitHub under the MIT license. No bill of materials or Gerber files were found in the published repositories, and neither the store page nor the repos state how many units were made or whether it is currently in stock.
