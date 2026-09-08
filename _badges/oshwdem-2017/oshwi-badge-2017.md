---
title: Oshwi Badge
id: oshwdem-2017-oshwi-badge-2017
layout: badge
parent: OSHWDem 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: oshwdem-2017
year: 2017
makers:
- name: Gustavo Reynaga (hulkco)
  url: https://github.com/hulkco
summary: Octopus-shaped IoT badge modelled on the OSHWDem mascot, built around an ESP-12 (ESP8266) WiFi module with five addressable NeoPixels, designed in KiCad and Inkscape for OSHWDem 2017 in A Coruña, Spain, with OSHPark, PCBWay, Hackster and Mazmaker board variants in the repo.
functions: WiFi-connected octopus badge; drives 5 directional addressable NeoPixels.
look:
  colors: []
  shape: octopus
  themes:
  - animal
  - robot
  - hardware tool
  - radio
tech:
  mcu: ESP-12 (ESP8266)
  leds:
    count: 5
    type: WS2812B
    note: Described by the maker as 5 directional "Neopixeles"
  display: none
  connectivity:
  - wifi
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/hulkco/oshwi_2017
  firmware_url: https://github.com/hulkco/oshwi_2017
  eda_tool: KiCad
links:
- label: github.com/hulkco/oshwi
  url: https://github.com/hulkco/oshwi
  kind: repo
  archived: https://web.archive.org/web/20251008100422/https://github.com/hulkco/oshwi
- label: github.com/hulkco/oshwi_2017
  url: https://github.com/hulkco/oshwi_2017
  kind: repo
- label: hackaday.io/project/116882-oshwi-the-octopus-iot-badge
  url: https://hackaday.io/project/116882-oshwi-the-octopus-iot-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260519183849/https://hackaday.io/project/116882-oshwi-the-octopus-iot-badge
images:
- file: assets/images/badges/oshwdem-2017/oshwi-badge-2017/c4467d3d4e.jpg
  source: https://hackaday.io/project/116882-oshwi-the-octopus-iot-badge
  credit: Gustavo Reynaga (hulkco)
  caption: Oshwi octopus-shaped IoT badge PCB
  archived: https://web.archive.org/web/20260519183849/https://hackaday.io/project/116882-oshwi-the-octopus-iot-badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/hulkco/oshwi
  title: hulkco/oshwi - Upload "Oshwi" Badge for OshwDem 2017 a Coruña
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20251008100422/https://github.com/hulkco/oshwi
- kind: url
  url: https://hackaday.io/project/116882-oshwi-the-octopus-iot-badge
  title: 'Oshwi: the Octopus IoT badge - Hackaday.io'
  accessed: '2026-09-07'
  note: Maker's project log confirming event, mascot inspiration, ESP-12 + 5 NeoPixels, KiCad/Inkscape design, and Hackaday Prize 2018 submission; source of the badge photo.
  archived: https://web.archive.org/web/20260519183849/https://hackaday.io/project/116882-oshwi-the-octopus-iot-badge
- kind: url
  url: https://github.com/hulkco/oshwi_2017
  title: hulkco/oshwi_2017
  accessed: '2026-09-07'
  note: Repository the maker points to for schematic, firmware, and full project files (checked via GitHub API for folder contents - ArtWork, Firmware, Fritzing_Parts, Schematic, plus OSHPark/PCBWay/Hackster/Mazmaker board variants).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The maker's Hackaday.io log and both GitHub repos (oshwi and oshwi_2017, identical in content) confirm the badge was made for OSHWDem 2017 in A Coruña, Spain, is shaped after the event's octopus mascot, and pairs an ESP-12 (ESP8266) with 5 addressable NeoPixels (WS2812B), inspired by Adafruit's Huzzah. Design software is KiCad and Inkscape; hardware and firmware files are openly published on GitHub, so open_source is set to "yes", though no explicit license file was found in the repo listing. The badge was also entered in the 2018 Hackaday Prize. No price, quantity made, sale channel, or battery/power details are stated anywhere in the sources found; those fields are left empty rather than guessed. The repo's README notes the design was "still under development" with possible circuit errors at time of upload.
last_modified_date: '2026-09-07'
model:
  file: assets/models/oshwdem-2017/oshwi-badge-2017.glb
  method: kicad
  source_file: 2017/Hackster_Version/001.kicad_pcb
  generated: '2026-09-07'
  bytes: 225320
---

The Oshwi Badge is an octopus-shaped IoT badge Gustavo Reynaga (hulkco) built for OSHWDem 2017 in A Coruña, Spain, taking its form from the event's own octopus mascot. It runs on an ESP-12 module (ESP8266) for WiFi, inspired by Adafruit's Huzzah board, and lights up five directionally-placed WS2812B addressable NeoPixels. The design was done with open-source tools — KiCad for the electronics and Inkscape for the artwork — and all files are published on GitHub, with variants prepared for OSHPark, PCBWay, Hackster, and Mazmaker fabrication/kit formats.

Reynaga later submitted Oshwi to the 2018 Hackaday Prize, documenting the build on a Hackaday.io project page. The repository's own README flags the badge as "still under development" with possible circuit errors at the time of upload, so some rough edges may remain in the published files. No information was found on pricing, quantities made, or how (or whether) it was distributed beyond the open files.

## Make your own

Full hardware (schematic, PCB artwork, Fritzing parts) and firmware are published in the [oshwi_2017](https://github.com/hulkco/oshwi_2017) repository (mirrored at [oshwi](https://github.com/hulkco/oshwi)), organized by fabrication target: OSHPark, PCBWay, Hackster, and Mazmaker board versions, plus a `Schematic` folder and `Firmware` folder.
