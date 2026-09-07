---
title: Celestial Wayfinder Badge
id: dc33-celestial-wayfinder-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
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
  display: 128x128 OLED
  connectivity:
  - lora
  - gps
  - usb
  battery: LiPo, rechargeable via USB-C
  sao_version: null
get_one:
  price: 'Complete: $150, DIY: $125'
  price_usd: 150.0
  quantity: ''
  availability: unknown
  distribution:
  - preorder
  where: Pre-ordered via the maker's storefront at wyrdwyrks.com/celestial-wayfinder/.
make_your_own:
  open_source: true
  hardware_url: https://github.com/WyrdWyrks/Wayfinder-CAD
  firmware_url: https://github.com/WyrdWyrks/Celestial-Wayfinder
  eda_tool: null
links:
- label: forum.defcon.org/node/255944
  url: https://forum.defcon.org/node/255944
  kind: social
- label: wyrdwyrks.com/celestial-wayfinder
  url: https://wyrdwyrks.com/celestial-wayfinder/
  kind: store
- label: github.com/WyrdWyrks/Celestial-Wayfinder
  url: https://github.com/WyrdWyrks/Celestial-Wayfinder
  kind: repo
- label: github.com/WyrdWyrks/Wayfinder-CAD
  url: https://github.com/WyrdWyrks/Wayfinder-CAD
  kind: repo
images: []
contact: {}
notes:
- This is the same product already documented in full at dc34-celestial-wayfinder-badge. This forum thread (posted July 2026, by a forum member "d3g3n" who is not the maker) is a pre-order announcement for what became the DC34 (2026) release; the sweep's "DEF CON 33" reading of the event was incorrect.
status: announced
sources:
- kind: url
  url: https://forum.defcon.org/node/255944
  title: Celestial Wayfinder Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: forums-reddit); event read as ''DEF CON 33''.'
- kind: url
  url: https://forum.defcon.org/node/255944
  title: Celestial Wayfinder badge - DEF CON Forums
  accessed: '2026-09-07'
  note: Forum post dated July 5, 2026, by user d3g3n (a poster, not the maker), announcing pre-orders for WyrdWyrks' Celestial Wayfinder ahead of DEF CON 34 (Aug 2026); gives price, features, and pre-order link.
- kind: url
  url: https://wyrdwyrks.com/celestial-wayfinder/
  title: Celestial Wayfinder - WyrdWyrks
  accessed: '2026-09-07'
  note: Maker storefront confirms product identity, ESP32-S3/OLED/LoRa/GPS/LED specs, and price; matches the already-researched dc34 entry.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Duplicate of dc34-celestial-wayfinder-badge, which is already fully researched with images and repo details. This DC33-filed entry came from a forum thread whose event tag ("DEF CON 33") was misread by the discovery sweep: the thread is dated July 2026 and is a pre-order announcement for the device that actually shipped for DEF CON 34 (2026), matching the maker''s own dc34 storefront listing exactly (same price tiers, same specs). No DC33 (2025)-specific release of this badge was found. Left event as dc33 per instructions (not to move/rename the file) but this should be treated as a duplicate/misfile of the dc34 entry, which is the canonical record. status set to "announced" (pre-order stage) rather than "released" to reflect what this specific source actually shows.'
last_modified_date: '2026-09-07'
related:
- dc34-celestial-wayfinder-badge
---

The Celestial Wayfinder is a handheld LoRa mesh device from WyrdWyrks that lets festival- and conference-goers ping their location to friends and follow a ring of 61 WS2812B LEDs, which lights up as a compass pointing toward the sender. It runs on an ESP32-S3 with a 128x128 OLED display, GPS, a magnetometer/IMU, five mechanical switches, a rotary encoder, haptic feedback, and a buzzer, in a cyberpunk-styled 3D-printed case with carabiner and lanyard mounts.

This particular entry originates from a DEF CON forum thread (forum.defcon.org/node/255944), posted July 5, 2026 by a forum member using the handle "d3g3n" — not the maker — announcing pre-orders ahead of DEF CON 34 (August 2026) at $150 assembled or $125 as a DIY kit. The thread's content, pricing, and specs match the maker's own storefront and the archive's existing, more thoroughly researched entry for this same device filed under dc34 (`dc34-celestial-wayfinder-badge`). No evidence was found that this badge had a separate release tied to DEF CON 33 (2025); the "DC33" tag on this entry appears to be a misread of the event by the automated discovery sweep. See the dc34 entry for full technical detail, photos, and repository links.
