---
title: HTH Elite 2019 Badge
id: hackers-teaching-hackers-2019-hth-elite-2019-badge-2
layout: badge
parent: Hackers Teaching Hackers 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hackers-teaching-hackers-2019
year: 2019
makers:
- name: syn-ack-zack
  url: https://github.com/syn-ack-zack
summary: 'A dual-microcontroller electronic badge made for the 2019 Hackers Teaching Hackers (HTH) event, with a color OLED, NeoPixel LEDs, and a LoRa chat system.'
functions: 'LoRa "HTH NET" chat over 915MHz (button-based and via a badge-hosted web app), WiFi tools (802.11 channel monitor, AP scanner/open-AP detector, packet/deauth sniffer, client or AP mode, built-in webserver with SPIFFS file editor and NTP client), a partially-working HID keystroke/mouse-jiggler toolkit on the secondary MCU, 40+ programmable LED patterns, and a snake game.'
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
  - hardware tool
tech:
  mcu: ESP32 + Atmel 32u4
  leds:
    count: 19
    type: NeoPixel
    note: Mini NeoPixel RGB LEDs, 40+ programmable patterns
  display: 96x64 color OLED
  connectivity:
  - wifi
  - lora
  - usb
  battery: 2x AA or USB
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/syn-ack-zack/HTH-Elite-2019-Badge
  firmware_url: https://github.com/syn-ack-zack/HTH-Elite-2019-Badge
  eda_tool: null
links:
- label: github.com/syn-ack-zack/HTH-Elite-2019-Badge
  url: https://github.com/syn-ack-zack/HTH-Elite-2019-Badge
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 4).
- 'Sweep''s title wording was "HTH-Elite-2019-Badge" (repo name); corrected to the maker''s own README wording, "HTH Elite 2019 Badge".'
status: released
sources:
- kind: url
  url: https://github.com/syn-ack-zack/HTH-Elite-2019-Badge
  title: HTH-Elite-2019-Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run4-spotted); event read as ''other''.'
- kind: url
  url: https://github.com/syn-ack-zack/HTH-Elite-2019-Badge
  title: HTH-Elite-2019-Badge (README)
  accessed: '2026-09-08'
  note: 'Confirmed full hardware spec, functions, and a badge photo URL (imgur.com/naiMRHil.jpg). This is a fork/mirror of the same repo already documented as entry other-hth-elite-2019-badge (HTHackers org, credited to contributor @syn-ack-zack).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Duplicate of entry other-hth-elite-2019-badge: same badge, same README/repo content, just fetched from @syn-ack-zack''s personal GitHub fork/mirror instead of the HTHackers org repo. Corrected event from "other" to hackers-teaching-hackers-2019 (present in _data/events.yml) since the badge was made for that specific con. No pricing, quantity, or availability info found. Only one photo (an Imgur link in the README) was located; not re-saved here since it is already attached to the other-hth-elite-2019-badge entry.'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/other/hth-elite-2019-badge-2/
---

The HTH Elite 2019 Badge was made by contributor @syn-ack-zack for the 2019 Hackers Teaching Hackers (HTH) event. It pairs an ESP32 with a secondary Atmel 32u4, driving a 96x64 color OLED display and 19 mini NeoPixel RGB LEDs, and runs on 2 AA batteries or USB power.

Its headline feature is "HTH NET," a long-range chat system built on a 915MHz SX1278 LoRa radio, usable either through the badge's four tactile buttons or through a web app hosted from the badge's own built-in webserver. The badge also includes a suite of WiFi tools (channel monitoring, access-point scanning and open-AP detection, packet and deauth sniffing, and client/AP modes), plus over 40 LED lighting patterns and a snake game. A planned HID keystroke-injection and mouse-jiggler toolkit on the Atmel 32u4 was not fully working at release.

This entry's source (github.com/syn-ack-zack/HTH-Elite-2019-Badge) is the same project already catalogued as a separate archive entry (other-hth-elite-2019-badge), reached there via the HTHackers org's copy of the same repo. Hardware and firmware are both open source on GitHub. No pricing, production quantity, or ongoing availability information was found.

## Make your own

The GitHub repository (https://github.com/syn-ack-zack/HTH-Elite-2019-Badge) contains hardware design files, firmware for both the ESP32 and the Atmel 32u4, and full build/flashing instructions, including required Arduino libraries, board settings (SparkFun ESP32 Thing / SparkFun Pro Micro at 3.3V), and steps for flashing over FTDI and uploading the SPIFFS filesystem for configuration and web assets.
