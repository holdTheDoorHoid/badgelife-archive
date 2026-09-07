---
title: HTH Elite 2019 Badge
id: other-hth-elite-2019-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2019
makers:
- name: HTHackers
  url: https://github.com/HTHackers
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
  hardware_url: https://github.com/HTHackers/HTH-Elite-2019-Badge
  firmware_url: https://github.com/HTHackers/HTH-Elite-2019-Badge
  eda_tool: null
links:
- label: github.com/HTHackers/HTH-Elite-2019-Badge
  url: https://github.com/HTHackers/HTH-Elite-2019-Badge
  kind: repo
images:
- file: assets/images/badges/other/hth-elite-2019-badge/8b052f0dd7.jpg
  source: "https://github.com/HTHackers/HTH-Elite-2019-Badge"
  credit: "HTHackers"
  caption: "The HTH Elite 2019 badge showing its 96x64 color OLED display and NeoPixel LEDs"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/HTHackers/HTH-Elite-2019-Badge
  title: HTH Elite 2019 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/HTHackers/HTH-Elite-2019-Badge/master/README.md
  title: HTH-Elite-2019-Badge README
  accessed: '2026-09-07'
  note: 'Full hardware spec, functions, and badge photo URL; author credited as @syn-ack-zack.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Made for "Hackers Teaching Hackers" (HTH) 2019, a con not present in _data/events.yml, so event is left as "other". No pricing, quantity made, or availability info found in the repo or README. Only one badge photo (an Imgur link in the README) was found; no additional images of the physical badge were located. Design/BOM/schematic files are in the GitHub repo but were not individually reviewed for a specific EDA tool designation.'
last_modified_date: '2026-09-07'
---

The HTH Elite 2019 Badge was made by HTHackers (credited to contributor @syn-ack-zack) for the 2019 Hackers Teaching Hackers (HTH) event. It pairs an ESP32 with a secondary Atmel 32u4, driving a 96x64 color OLED display and 19 mini NeoPixel RGB LEDs, and runs on 2 AA batteries or USB power.

Its headline feature is "HTH NET," a long-range chat system built on a 915MHz SX1278 LoRa radio, usable either through the badge's four tactile buttons or through a web app hosted from the badge's own built-in webserver. The badge also includes a suite of WiFi tools (channel monitoring, access-point scanning and open-AP detection, packet and deauth sniffing, and client/AP modes), plus over 40 LED lighting patterns and a snake game. A planned HID keystroke-injection and mouse-jiggler toolkit on the Atmel 32u4 was not fully working at release, limited by a serial communication issue between the two microcontrollers.

Hardware and firmware are both open source on GitHub, and the README acknowledges Hacker Warehouse and Garrett Gee's DEF CON 26 badge as a reference for the ESP32/Atmel32u4 core design. No pricing, production quantity, or ongoing availability information was found.

## Make your own

The GitHub repository (https://github.com/HTHackers/HTH-Elite-2019-Badge) contains hardware design files, firmware for both the ESP32 and the Atmel 32u4, and full build/flashing instructions, including required Arduino libraries, board settings (SparkFun ESP32 Thing / SparkFun Pro Micro at 3.3V), and steps for flashing over FTDI and uploading the SPIFFS filesystem for configuration and web assets.
