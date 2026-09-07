---
title: Oshwi, the octopus IoT Badge
id: oshwdem-2017-oshwi-octopus-iot-badge
layout: badge
parent: OSHWDem 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: oshwdem-2017
year: 2017
makers:
- name: Gustavo Reynaga (Hulkco)
  url: https://hackaday.io/hacker/148221-gustavo-reynaga
summary: An octopus-shaped open-source PCB badge modelled on the OSHWDem mascot, built around an ESP-12 (ESP8266) WiFi module with five addressable WS2812B Neopixels, designed in KiCad and Inkscape in Mazatlan, Mexico for the OSHWDem 2017 maker event in A Coruna, Spain.
functions: 'WiFi-connected IoT badge with five addressable RGB LEDs (Neopixels) arranged as the octopus''s "legs".'
look:
  colors: []
  shape: octopus
  themes:
  - animal
  - mascot
  - wearable
tech:
  mcu: ESP8266 (ESP-12)
  leds:
    count: 5
    type: WS2812B
    note: Referred to by the maker as "Neopixeles"; arranged around the octopus-shaped PCB.
  display: none
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
  hardware_url: https://github.com/hulkco/oshwi_2017
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/116882-oshwi-the-octopus-iot-badge
  url: https://hackaday.io/project/116882-oshwi-the-octopus-iot-badge
  kind: hackaday
- label: github.com/hulkco/oshwi_2017
  url: https://github.com/hulkco/oshwi_2017
  kind: repo
images:
- file: assets/images/badges/oshwdem-2017/oshwi-octopus-iot-badge/c4467d3d4e.jpg
  source: "https://hackaday.io/project/116882-oshwi-the-octopus-iot-badge"
  credit: "Gustavo Reynaga (Hulkco)"
  caption: "Oshwi octopus-shaped IoT badge PCB"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/116882-oshwi-the-octopus-iot-badge
  title: Oshwi, the octopus IoT Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/116882-oshwi-the-octopus-iot-badge
  title: Oshwi, the octopus IoT Badge
  accessed: '2026-09-07'
  note: Confirmed maker, event, ESP-12/ESP8266 MCU, five WS2812B Neopixels, KiCad/Inkscape design tools, and Hackaday Prize/Open Hardware Design Challenge submission; sourced the badge photo.
- kind: url
  url: https://github.com/hulkco/oshwi_2017
  title: hulkco/oshwi_2017 (GitHub)
  accessed: '2026-09-07'
  note: Repo description confirms "Oshwi Badge for OshwDem 2017 a Coruna"; README notes the circuit was still under development with possible errors/omissions; repo contains folders for both 2017 and 2019 iterations; no LICENSE file found via the GitHub API, so hardware openness is marked partial rather than yes.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No pricing, quantity-made, or distribution/availability details found on either the Hackaday.io project page or the GitHub repo; get_one fields left empty. The GitHub repo also contains a 2019 folder, suggesting a follow-up or updated version of the badge was built for a later OSHWDem, but no separate 2019 project page or details were found to confirm this as a distinct release. The repo carries no LICENSE file, so hardware openness is recorded as partial (files are public but not formally licensed) rather than a confirmed open-source license.
last_modified_date: '2026-09-07'
---

Oshwi is an octopus-shaped open-hardware PCB badge that Gustavo Reynaga (working as Hulkco) designed in Mazatlan, Mexico for OSHWDem 2017, the open-source-hardware maker gathering held in A Coruna, Spain. The badge takes its form from OSHWDem's own octopus mascot and centers on an ESP-12 module (ESP8266), giving it WiFi connectivity, with five WS2812B addressable Neopixels lighting up the octopus's legs. Reynaga designed the board in KiCad and did the artwork in Inkscape, and later submitted the project to the Hackaday Prize's Open Hardware Design Challenge.

## Make your own

Design files are published at github.com/hulkco/oshwi_2017, which includes both a 2017 folder and a 2019 folder (the latter's contents were not reviewed for this entry). The repository's README notes that the circuit was still under development at the time of writing, with possible errors or omissions in need of community help. No LICENSE file was found in the repo, so treat the files as shared-but-unlicensed rather than under a confirmed open license.
