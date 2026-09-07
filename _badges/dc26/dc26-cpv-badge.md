---
title: Crypto & Privacy Village DC26 Badge
id: dc26-dc26-cpv-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Crypto & Privacy Village
  url: https://github.com/cryptovillage
summary: The official Crypto & Privacy Village badge for DEF CON 26 (2018), a gold-plated ESP32 + EFM8UB1 'split-brained' badge with RGB LEDs, capacitive touch pads, LiPo/micro-USB power, a DC26 Shitty Add-On header, and a built-in hardware challenge tied to the village's Gold Bug puzzle; this repo holds its KiCad hardware, ESP32 and EFM8 firmware, emulator, OTA server, and tools.
functions: RGB LEDs light up maze-style passages on the badge face; capacitive touch pads for interaction; badges tessellate edge-to-edge with neighboring badges to form larger shapes; a built-in hardware puzzle tied to the village's Gold Bug challenge.
look:
  colors:
  - gold
  - copper
  shape: null
  themes:
  - puzzle
  - ctf
  - security
  - privacy
tech:
  mcu: ESP32 + EFM8
  leds:
    count: null
    type: RGB
    note: Only RGB LEDs and capacitive touch pads populate the front; no silkscreen text, using solder-mask placement over gold-plated copper for lettering/outline instead.
  display: none
  connectivity:
  - wifi
  battery: LiPo, micro-USB recharge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/cryptovillage/badge2018/tree/master/hardware
  firmware_url: https://github.com/cryptovillage/badge2018/tree/master/firmware
  eda_tool: null
links:
- label: github.com/cryptovillage/badge2018
  url: https://github.com/cryptovillage/badge2018
  kind: repo
  archived: https://web.archive.org/web/20260907115844/https://github.com/cryptovillage/badge2018
- label: hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3
  url: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  kind: article
  archived: https://web.archive.org/web/20260417144127/https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
- label: defcon.org/html/defcon-26/dc-26-villages.html
  url: https://defcon.org/html/defcon-26/dc-26-villages.html
  kind: website
  archived: https://web.archive.org/web/20260824234944/https://defcon.org/html/defcon-26/dc-26-villages.html
images:
- file: assets/images/badges/dc26/dc26-cpv-badge/838ec7217f.jpg
  source: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  credit: Hackaday
  caption: Front of the Crypto & Privacy Village DC26 badge, gold-plated with RGB LEDs and capacitive touch pads
  archived: https://web.archive.org/web/20260417144127/https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
- file: assets/images/badges/dc26/dc26-cpv-badge/f29c1a2bdf.jpg
  source: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  credit: Hackaday
  caption: Crypto & Privacy Village DC26 badge illuminated, showing the maze-style LED lighting
  archived: https://web.archive.org/web/20260417144127/https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/cryptovillage/badge2018
  title: GitHub - cryptovillage/badge2018
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260907115844/https://github.com/cryptovillage/badge2018
- kind: url
  url: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  title: All The Badges Of DEF CON 26, Vol. 3 (Hackaday)
  accessed: '2026-09-07'
  note: Confirmed design details (gold-plated look, RGB LEDs, capacitive touch, maze/tessellation concept, LiPo/micro-USB power) and supplied the front/lit photos used here.
  archived: https://web.archive.org/web/20260417144127/https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
- kind: url
  url: https://raw.githubusercontent.com/cryptovillage/badge2018/master/README.md
  title: badge2018 README
  accessed: '2026-09-07'
  note: Confirms ESP32 + EFM8 dual-MCU firmware build process (ESP-IDF/MicroPython for ESP32, Simplicity Studio for EFM8); no price/quantity/SAO info in the README.
  archived: https://web.archive.org/web/20260907120022/https://raw.githubusercontent.com/cryptovillage/badge2018/master/README.md
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Design and function details come from the maker''s repo and a contemporary Hackaday writeup, both of which describe the same badge consistently. Neither source states price, quantity made, LED count, or whether it carries a DC26 SAO header (the summary field, carried over from the sheet/intake pass, asserts an SAO header but this could not be independently confirmed in the repo or article, so sao_version/sao_ports are left null rather than guessed). EDA tool for the KiCad-named hardware folder was not explicitly confirmed in the files fetched. get_one fields left empty: no sale price, quantity, or distribution method found (village badges are often given to volunteers/attendees rather than sold, but this was not stated).'
last_modified_date: '2026-09-07'
---

The Crypto & Privacy Village (CPV) gave out this badge at DEF CON 26 in 2018. It runs two microcontrollers — an ESP32 as the main brain and an EFM8UB1 handling supporting duties — and is built to look like machined gold-plated metal rather than a typical PCB: there's no silkscreen text, with lettering and outlines instead cut into the solder mask over gold-plated copper. The face carries only RGB LEDs and capacitive touch pads, which light up maze-style passages; badges are designed to tessellate edge-to-edge with neighboring units to build larger shapes when several are placed together. Power comes from a LiPo cell topped up over micro-USB.

Beyond the light show, the badge doubles as a puzzle: it carries a built-in hardware challenge tied to CPV's "Gold Bug" cryptography puzzle for the village. The project's GitHub repository (cryptovillage/badge2018) publishes the hardware design, ESP32 and EFM8 firmware, an emulator, an OTA update server, an LED editor site, and supporting tools, making the full stack open source, though pricing, production quantity, and exact distribution method were not stated in the sources reviewed.
