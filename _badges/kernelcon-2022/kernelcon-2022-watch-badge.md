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
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, released item via the maker''s own GitHub repo and badge.gallery listing. No maker-published photo of the physical badge was found (repo only contains a screenshot of Arduino IDE settings, not the item), so images were left empty. Price, quantity, LEDs, and display are undocumented in the available sources. ZonkSec is Tyler Rosonke, per this maker''s other Kernelcon badge entries (2019-2026), though this specific repo does not name him directly.'
last_modified_date: '2026-09-08'
---

The Kernelcon 2022 Watch Badge is a wearable, watch-style conference badge made by ZonkSec (Tyler Rosonke) for Kernelcon 2022, held March 30 - April 2, 2022 in Omaha, Nebraska. It runs on a generic ESP8266 (Arduino core, not a DSTIKE-specific target), with firmware descended from SpacehuhnTech's ESP8266 deauther project, giving it Wi-Fi based security-demo capabilities.

Attendees built and customized their own firmware: the badge shipped with hard-coded Wi-Fi settings in a `wifi.h` file that had to be edited before compiling in the Arduino IDE (with the ESP8266 core and ArduinoJson library installed) and flashing over serial. The public GitHub repository holds the firmware source (in a `kernelcon_watch_v4` folder) and a screenshot of the required Arduino IDE settings, but no schematic, BOM, or Gerbers, and no photo of the finished physical badge.

## Make your own

1. Install the Arduino IDE with the ESP8266 board core and the ArduinoJson library.
2. Clone https://github.com/ZonkSec/kernelcon-2022-badge and edit `wifi.h` in the `kernelcon_watch_v4` folder with your own Wi-Fi credentials.
3. Compile and flash to an ESP8266 board over serial using the settings documented in the repo.
