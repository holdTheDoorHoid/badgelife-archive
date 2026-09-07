---
title: Meshanger Badge V
id: other-meshanger-badge-v
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 0
makers:
- name: Gee Bartlett
  url: https://hackaday.io/gee-bartlett
summary: An off-grid mesh-network messaging badge built around the ESP32-C3, a reboot of the maker's earlier ESP8266-based Meshenger Badge.
functions: Off-grid, infrastructure-free mesh messaging between badges over WiFi/BLE.
look:
  colors: []
  shape: null
  themes:
  - radio
  - privacy
tech:
  mcu: ESP32-C3
  leds: null
  display: null
  connectivity:
  - wifi
  - ble
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/176020-meshanger-badge-v
  url: https://hackaday.io/project/176020-meshanger-badge-v
  kind: hackaday
- label: hackaday.io/project/9777-meshenger-badge (original project)
  url: https://hackaday.io/project/9777-meshenger-badge
  kind: hackaday
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/176020-meshanger-badge-v
  title: Meshanger Badge V
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''other''.'
- kind: url
  url: https://hackaday.io/project/176020-meshanger-badge-v
  title: Meshanger Badge V
  accessed: '2026-09-07'
  note: Confirmed maker (Gee Bartlett), MCU (ESP32-C3), and that it is a reboot of an earlier Meshenger Badge; no price, quantity, or event tie found.
- kind: url
  url: https://hackaday.io/project/9777-meshenger-badge
  title: Meshenger Badge (original project)
  accessed: '2026-09-07'
  note: The earlier ESP8266-based project this one reboots; notes it was inspired by radio badges seen at EMF Camp and other events, but was never a badge made for a specific con.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    Fact-check pass (2026-09-07): re-fetched both hackaday.io project pages and confirmed maker
    (Gee Bartlett), MCU (ESP32-C3 with WiFi/BLE 5.0), and that Meshanger Badge V is a reboot of the
    maker's 2016 ESP8266 Meshenger Badge, which the maker describes as "inspired by the radio badges
    from EFM Camp and other events" (not a commission for EMF Camp), so event correctly stays 'other'.
    Removed the one saved image (6958262819.jpg): its id does not appear anywhere in either project
    page's HTML (checked via curl), and the picture itself shows a PCB silkscreened "ESP12-F" and
    "CH340G" — an ESP8266/USB-serial layout, not the ESP32-C3 this entry is about — so it was
    mis-sourced and could not be verified as depicting this item; images field is now empty. This is
    a personal Hackaday.io project, not a con-distributed badge: no price, quantity, availability,
    LEDs, display, battery, or design-file links are stated on either source page, so those fields
    stay empty. Remaining fields/sentences are all supported by the two cited source pages.
last_modified_date: '2026-09-07'
---

Meshanger Badge V is a personal Hackaday.io project by maker Gee Bartlett (hackaday.io/gee-bartlett), a reboot of an earlier project of the same idea. It's built around the ESP32-C3, a RISC-V microcontroller with WiFi and Bluetooth 5.0, and aims to give people an off-grid, infrastructure-free way to send messages badge-to-badge over a mesh network.

The "V" in the title marks it as a revisit of Bartlett's original Meshenger Badge from 2016, which ran on an ESP8266 and was, in the maker's own words, "inspired by the radio badges from EFM Camp and other events" and by a general interest in privacy-preserving communication. Neither project appears to have shipped as a badge distributed at a specific convention — both read as ongoing hobbyist explorations rather than commissioned con hardware, so no event tie could be confirmed and this entry stays filed under Other.

No pricing, unit count, availability, or open-source hardware/firmware links are given on the project page, and no design files are linked from it.
