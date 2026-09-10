---
title: Penghito Poco
id: other-penghito-poco-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A small SAO version of davedarko's Penghicorn (Phengicorn) badge, shaped like a purple penguin with a unicorn horn.
functions: ''
look:
  colors:
  - purple
  shape: penguin
  themes:
  - animal
  - bird
  - fantasy
  - mascot
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
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
  open_source: true
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Penghito%20Poco
  firmware_url: null
  eda_tool: Eagle
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/Penghito%20Poco
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Penghito%20Poco
  kind: repo
- label: Penghicorn | Hackaday.io
  url: https://hackaday.io/project/162293-penghicorn
  kind: hackaday
images:
- file: assets/images/badges/other/penghito-poco-sao/2245dbe626.png
  source: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Penghito%20Poco
  credit: davedarko
  caption: OSH Park render of the Penghito Poco SAO board
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/Penghito%20Poco/readme.md
  title: Penghito Poco readme (Simple-Add-ons-SAO repo)
  accessed: '2026-09-07'
  note: 'Maker''s own description: "Small version of the Phengicorn Badge as a somple Add-on, made in Eagle"; confirms Eagle CAD files (.sch/.brd) and the OSH Park render image.'
- kind: url
  url: https://hackaday.io/project/162293-penghicorn
  title: Penghicorn | Hackaday.io
  accessed: '2026-09-07'
  note: 'Parent full-size badge this SAO is a mini version of. Built by davedarko with deantonious and Stefan Kremser for 35C3 (2018): ESP8266, 1.3in OLED, NRF24L01, CC1101, WS2812 LED, ATtiny45 touch controller. The Poco SAO itself is a simplified, passive board and does not carry these components.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No event or year is stated for the Penghito Poco SAO itself, so event is left as 'other' rather than assumed. The parent full badge (Penghicorn) was made for 35C3 (Chaos Communication Congress, Dec 2018) but events.yml has no 35C3 entry and there is no guarantee the SAO was made for the same con/year, so it is not carried over to the event field. The board (from the OSH Park render) shows a 2x3 (6-pin) header on the flipper, consistent with an SAO connector, but the maker's files do not label a SAO version so tech.sao_version is left null rather than guessed. No MCU, LEDs, price, quantity, or availability information is published anywhere found; this appears to be a simple/passive decorative SAO with no active electronics shown in the render.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/penghito-poco-sao.glb
  method: kicad
  source_file: penghitopoco.brd
  generated: '2026-09-10'
  bytes: 41996
---

Penghito Poco is a small Simple Add-on (SAO) by davedarko, described in its own repository as "a small version of the Phengicorn Badge." It takes the penguin-with-a-unicorn-horn mascot of davedarko's full-size Penghicorn conference badge and renders it as a compact purple PCB, complete with the horn, beak, and flipper feet, with a 2x3 pin header on one flipper for plugging into a host badge.

The design files (Eagle schematic and board) and an OSH Park render are published in davedarko's `Simple-Add-ons-SAO` GitHub repository alongside dozens of his other small add-on boards. No firmware, chip, or LED information accompanies the files, and the render shows no obvious component footprints beyond the header, suggesting this is a simple, likely passive, decorative SAO rather than an electronically active one. No event, year, price, or distribution details are given anywhere in the source material.

The parent badge it references, Penghicorn, was a considerably more elaborate ESP8266-based conference badge that davedarko built with deantonious and Stefan Kremser for 35C3 in 2018, featuring an OLED display, dual radios (NRF24L01 and CC1101), a WS2812 LED, and touch-sensitive horn/beak controls. Penghito Poco appears to be a later, stripped-down tribute to that badge's mascot rather than a functional derivative of its electronics.

## Make your own

The Eagle schematic (`penghitopoco.sch`) and board (`penghitopoco.brd`) files are in the [Penghito Poco folder](https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Penghito%20Poco) of davedarko's Simple-Add-ons-SAO repository, ready to open in Eagle CAD and send to a fab such as OSH Park.
