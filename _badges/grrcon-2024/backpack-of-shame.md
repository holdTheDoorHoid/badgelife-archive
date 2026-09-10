---
title: Backpack of Shame
id: grrcon-2024-backpack-of-shame
layout: badge
parent: GrrCON 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: grrcon-2024
year: 2024
makers:
- name: CynicalSignals (ickfosec)
  url: https://www.cynicalsignals.com/
summary: 'A one-off rogue Wi-Fi access point and victim scoreboard that CynicalSignals (ickfosec) wore on their own backpack at GrrCon 2024, built alongside their unofficial GrrCON 2024 BadgeBuddy badge.'
functions: 'Broadcasts an open ("no password") Wi-Fi network named "GrrCon WiFi", counts unique connecting MAC addresses on an LED scoreboard, and uses DNS poisoning to redirect connected devices to a captive-portal webpage with a custom message after they stay connected long enough.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ESP8266
  leds:
    count: 256
    type: LED matrix
    note: Four 8x8 LED matrices, mounted with 90-degree rotations, used as the victim-count scoreboard.
  display: LED matrix 8x8 (x4)
  connectivity:
  - wifi
  battery: portable battery pack
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 'one built, for personal use'
  availability: not_released
  distribution: []
  where: 'Not distributed; a single unit built and worn by the maker at GrrCon 2024.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/ickfosec/esp/tree/main/GrrCon%202024/Backpack%20of%20Shame
  firmware_url: null
  eda_tool: null
  notes: 'A wiring diagram (ESP8266_BackpackOfShame.svg) is published in the repo; no firmware source was found alongside it.'
links:
- label: github.com/ickfosec/esp
  url: https://github.com/ickfosec/esp
  kind: website
- label: 'CynicalSignals: Building an Unofficial Badge for GrrCon 2024'
  url: https://www.cynicalsignals.com/building-an-unofficial-badge-for-grrcon-2024/
  kind: article
- label: 'ESP8266_BackpackOfShame.svg (wiring diagram)'
  url: https://github.com/ickfosec/esp/blob/main/GrrCon%202024/Backpack%20of%20Shame/ESP8266_BackpackOfShame.svg
  kind: fab
images:
- file: assets/images/badges/grrcon-2024/backpack-of-shame/dfdf9b10d6.jpg
  source: "https://www.cynicalsignals.com/building-an-unofficial-badge-for-grrcon-2024/"
  credit: "CynicalSignals (ickfosec)"
  caption: "The backpack's victim counter scoreboard made from four 8x8 LED matrices"
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'The community sheet/sweep listed this only by repo name; the maker''s own blog post is the actual source of detail.'
status: released
sources:
- kind: url
  url: https://github.com/ickfosec/esp
  title: Backpack of Shame
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://www.cynicalsignals.com/building-an-unofficial-badge-for-grrcon-2024/
  title: 'Building an Unofficial Badge for GrrCon 2024'
  accessed: '2026-09-10'
  note: 'Maker''s own writeup; source for what the Backpack of Shame is, its hardware, and its function as a rogue AP/scoreboard.'
- kind: url
  url: https://github.com/ickfosec/esp/blob/main/GrrCon%202024/Backpack%20of%20Shame/ESP8266_BackpackOfShame.svg
  title: 'ESP8266_BackpackOfShame.svg'
  accessed: '2026-09-10'
  note: 'Confirms an ESP8266-based wiring diagram exists in the repo for this project.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Not a badge or SAO despite the repo name suggesting one — it is a one-off rogue access point and LED-matrix victim scoreboard the maker mounted on their own backpack at GrrCon 2024, built alongside their separate GrrCON 2024 BadgeBuddy badge (see grrcon-2024-grrcon-2024-badgebuddy). Only one unit exists; it was never distributed. No firmware source was found published, only a wiring diagram, so make_your_own.open_source is set to partial.'
last_modified_date: '2026-09-10'
---

CynicalSignals (ickfosec) built the Backpack of Shame as a companion piece to their unofficial GrrCON 2024 BadgeBuddy badge. Rather than a badge or SAO, it is a single rogue Wi-Fi access point and scoreboard that the maker wore on their own backpack throughout the con, powered by a portable battery pack and an ESP8266.

The device broadcast an open network called "GrrCon WiFi." Each unique device that connected was tallied on a scoreboard built from four 8x8 LED matrices (mounted at 90-degree rotations, which required custom bitmap character animation to read correctly). Devices that stayed connected long enough were redirected via DNS poisoning to a captive portal serving a custom message from an internal webserver. Over the two days it ran, the maker recorded about 18 unique connections, more than half of them friends trying it out on purpose.

Only one Backpack of Shame was built, purely for the maker's own use at the con; it was never sold, given away, or reproduced. The GitHub repo linked from the write-up includes a wiring diagram for the ESP8266 side of the build, but no firmware source was found alongside it.

## Make your own

A wiring diagram (`ESP8266_BackpackOfShame.svg`) is published in [ickfosec/esp](https://github.com/ickfosec/esp/tree/main/GrrCon%202024/Backpack%20of%20Shame). No firmware source is published, so recreating the captive-portal/DNS-poisoning behavior would require writing that part from scratch, guided by the maker's own description of the build.
