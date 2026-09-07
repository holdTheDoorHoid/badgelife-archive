---
title: Oshwi ESP32 / Oshwi M0 (2019)
id: other-oshwi-badge-2019
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2019
makers:
- name: Gustavo Reynaga (hulkco)
  url: https://github.com/hulkco
summary: 2019 redesign of Gustavo Reynaga's Oshwi octopus badge (originally made for OSHWDem 2017 in A Coruña, Spain), adding new KiCad boards for ESP32 (Oshwi_ESP32), SAMD21 M0 (Oshwi_M0) and an ESP8266 LoRa variant, plus WS2812-2020 reverse-mount LEDs and a 0.96-inch reverse-mount IPS TFT shield.
functions: ''
look:
  colors: []
  shape: octopus
  themes:
  - animal
  - wearable
tech:
  mcu: ESP32-WROOM-32 (Oshwi_ESP32); SAMD21 (Oshwi_M0); ESP8266/ESP-12 (Oshwi_ESP8266_LORA variant)
  leds:
    count: null
    type: WS2812-2020 (reverse-mount)
    note: The original 2017 Oshwi board used 5 addressable RGB LEDs; the 2019 redesign's LED count is not stated in the repo.
  display: 0.96" IPS TFT (no glass, reverse mount)
  connectivity:
  - wifi
  - lora
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
  open_source: 'yes'
  hardware_url: https://github.com/hulkco/oshwi/tree/master/2019
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/hulkco/oshwi
  url: https://github.com/hulkco/oshwi
  kind: repo
- label: github.com/hulkco/oshwi/tree/master/2019
  url: https://github.com/hulkco/oshwi/tree/master/2019
  kind: repo
- label: 'Hackaday.io: Oshwi, the octopus IoT Badge'
  url: https://hackaday.io/project/116882-oshwi-the-octopus-iot-badge
  kind: hackaday
- label: 'OSH Park blog: OSHWi Octopus Badge by Gustavo Reynaga'
  url: https://blog.oshpark.com/2017/12/24/oshwi-octopus-badge-by-gustavo-reynaga/
  kind: article
images: []
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/hulkco/oshwi
  title: hulkco/oshwi - Upload "Oshwi" Badge for OshwDem 2017 a Coruña
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/hulkco/oshwi/tree/master/2019
  title: hulkco/oshwi, 2019 directory listing
  accessed: '2026-09-07'
  note: Confirmed the 2019 folder contains Oshwi_ESP32, Oshwi_M0, and Oshwi_ESP8266_LORA KiCad board variants, plus WS2812-2020 LED and 0.96in reverse-mount TFT reference designs; no assembled-board photos or firmware, just KiCad sources, SVG artwork and screenshots.
- kind: url
  url: https://hackaday.io/project/116882-oshwi-the-octopus-iot-badge
  title: 'Oshwi, the octopus IoT Badge | Hackaday.io'
  accessed: '2026-09-07'
  note: Describes the original Oshwi badge (maker Gustavo Reynaga, Mazatlan, Mexico) as an ESP8266/ESP-12 board with 5 addressable Neopixel LEDs, made for the OSHWDem maker event mascot (La Coruna, Spain); entered in the 2018 Hackaday Prize Open Hardware Design Challenge.
- kind: url
  url: https://blog.oshpark.com/2017/12/24/oshwi-octopus-badge-by-gustavo-reynaga/
  title: OSHWi Octopus Badge by Gustavo Reynaga - OSH Park
  accessed: '2026-09-07'
  note: Confirms maker and open-source status of the original 2017 octopus badge; design files shared as an OSH Park project.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    OSHWDem is an annual open-source hardware maker event in A Coruña, Spain; Oshwi is
    its octopus mascot. The original Oshwi badge (ESP8266/ESP-12, 5 addressable RGB
    LEDs) was made by Gustavo Reynaga for OSHWDem 2017 and is documented on Hackaday.io
    and OSH Park's blog. This entry covers the repo's separate "2019" folder, which
    holds a redesign with new ESP32 and SAMD21 (M0) boards plus an ESP8266 LoRa
    variant, WS2812-2020 reverse-mount LEDs, and a reverse-mount 0.96" IPS TFT shield.
    No page names an "OSHWDem 2019" event or confirms these boards were built and
    distributed as badges that year; there is also no matching event id in
    _data/events.yml (only oshwdem-2017 exists), so event is left as "other". No
    photos of the assembled 2019 boards were found, only KiCad source files, SVG
    artwork, and screenshots of the design software; firmware for the 2019 variant
    was not located either. Price, quantity, and availability are unknown.
last_modified_date: '2026-09-07'
---

Oshwi is the octopus mascot of OSHWDem, an annual open-source hardware event held in A Coruña, Spain. Mexican maker Gustavo Reynaga (hulkco) designed the original Oshwi badge for OSHWDem 2017: an ESP8266 (ESP-12 module) board in an octopus-shaped PCB, carrying five addressable WS2812 RGB LEDs and running on a small LiPo cell, entered into the 2018 Hackaday Prize's Open Hardware Design Challenge and shared as an OSH Park project.

The same GitHub repository, `hulkco/oshwi`, also holds a "2019" folder with a further redesign of the board. It adds new KiCad layouts for an ESP32 version (Oshwi_ESP32) and a SAMD21-based "M0" version (Oshwi_M0), plus an ESP8266-with-LoRa variant, alongside reference footprints for WS2812-2020 reverse-mount LEDs and a 0.96-inch reverse-mount IPS TFT shield. The folder is a working set of KiCad source files, SVG artwork, and screenshots rather than a documented product page, so it is unclear whether these particular boards were fabricated and handed out at OSHWDem 2019 or a later edition, and there is no OSHWDem 2019 entry in this archive's event list to attach it to.

## Make your own

All hardware for both the 2017 and 2019 variants is published as KiCad projects in the `hulkco/oshwi` repository (see the 2019 subfolder for the ESP32, M0, and LoRa boards). No firmware for the 2019 boards was found alongside the hardware files.
