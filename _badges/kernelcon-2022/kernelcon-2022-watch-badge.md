---
title: Kernelcon 2022 Watch Badge
id: kernelcon-2022-kernelcon-2022-watch-badge
layout: badge
parent: Kernelcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: kernelcon-2022
year: 2022
makers:
- name: ZonkSec
  url: https://github.com/ZonkSec
summary: A wearable, watch-style conference badge for Kernelcon 2022 built around the ESP8266, with firmware descended from SpacehuhnTech's ESP8266 deauther project.
functions: Wi-Fi based security demo/tool; participants flash and configure it themselves (hard-coded Wi-Fi settings in a wifi.h file) via the Arduino IDE.
look:
  colors: []
  shape: null
  themes:
  - security
  - wearable
  - radio
tech:
  mcu: ESP8266
  leds: null
  display: null
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/ZonkSec/kernelcon-2022-badge
  eda_tool: null
  notes: 'Firmware only (folder kernelcon_watch_v4), built with Arduino IDE + ESP8266 core + ArduinoJson library. No schematic, BOM, or Gerbers found in the repo.'
links:
- label: badge.gallery/badges/kernelcon-2022-watch-badge
  url: https://badge.gallery/badges/kernelcon-2022-watch-badge
  kind: website
- label: github.com/ZonkSec/kernelcon-2022-badge
  url: https://github.com/ZonkSec/kernelcon-2022-badge
  kind: repo
images: []
contact: {}
notes:
- ESP8266-based wearable watch-style conference badge for Kernelcon 2022. Found by the event-year sweep, task con-kernelcon.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/kernelcon-2022-watch-badge
  title: Kernelcon 2022 Watch Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kernelcon); event read as ''Kernelcon 2022''.'
- kind: url
  url: https://github.com/ZonkSec/kernelcon-2022-badge
  title: 'ZonkSec/kernelcon-2022-badge (GitHub repo)'
  accessed: '2026-09-08'
  note: 'Confirms maker (ZonkSec), ESP8266 MCU, watch form factor, deauther-derived Wi-Fi firmware, Arduino IDE build steps; no schematic/BOM/photos in repo.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Fact-check pass (2026-09-08): re-fetched both cited sources (badge.gallery listing and the ZonkSec/kernelcon-2022-badge GitHub repo) and confirmed maker, ESP8266 MCU, watch form factor, wifi.h/Arduino IDE/ArduinoJson build steps, SpacehuhnTech deauther lineage, and the absence of schematic/BOM/Gerbers/photos in the repo, matching the entry. Independently verified the March 30-April 2, 2022, Omaha dates via a web search (badge.gallery/events/kernelcon-2022, Bellevue University cybersecurity blog, and Kernelcon''s own YouTube promo, which also calls it a "smartwatch badge"). No image exists locally or on either source page, consistent with images: []. ZonkSec = Tyler Rosonke is corroborated by the maker''s other Kernelcon entries in this archive (2019, 2020, 2025), which cite the same GitHub org/badge site for that identification; this specific repo does not name him. Price, quantity, LEDs, display, battery, sao_version, colors, and shape remain undocumented in any source found and are left empty, as is correct. No contradictions found.'
last_modified_date: '2026-09-08'
---

The Kernelcon 2022 Watch Badge is a wearable, watch-style conference badge made by ZonkSec (Tyler Rosonke) for Kernelcon 2022, held March 30 - April 2, 2022 in Omaha, Nebraska. It runs on a generic ESP8266 (Arduino core, not a DSTIKE-specific target), with firmware descended from SpacehuhnTech's ESP8266 deauther project, giving it Wi-Fi based security-demo capabilities.

Attendees built and customized their own firmware: the badge shipped with hard-coded Wi-Fi settings in a `wifi.h` file that had to be edited before compiling in the Arduino IDE (with the ESP8266 core and ArduinoJson library installed) and flashing over serial. The public GitHub repository holds the firmware source (in a `kernelcon_watch_v4` folder) and a screenshot of the required Arduino IDE settings, but no schematic, BOM, or Gerbers, and no photo of the finished physical badge.

## Make your own

1. Install the Arduino IDE with the ESP8266 board core and the ArduinoJson library.
2. Clone https://github.com/ZonkSec/kernelcon-2022-badge and edit `wifi.h` in the `kernelcon_watch_v4` folder with your own Wi-Fi credentials.
3. Compile and flash to an ESP8266 board over serial using the settings documented in the repo.
