---
title: SAO Lora Walkie Talkie
id: supercon-2024-sao-lora-walkie-talkie
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Jeremy Geppert (JayGee)
  url: https://hackaday.io/hacker/1277492-jeremygeppert
summary: A retro walkie-talkie shaped SAO that carries a Reyax RYLR998 LoRa transceiver on the SAO GPIO pins for wireless serial between badges, with a red power LED and a push-to-talk button wired as the module reset; 30 were assembled for Supercon 2024, 10 of them with the LoRa module fitted.
functions: Wireless serial communication between SAO badges over LoRa, controlled with simple AT commands; the PTT button resets the LoRa module rather than keying a mic. Works purely as a decorative walkie-talkie-shaped SAO even without the LoRa module fitted.
look:
  colors:
  - black
  - gold
  shape: null
  themes:
  - radio
  - retro computer
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single SMD red LED (CMD17-21VRD/TR8) as a power indicator, mounted on the back shining through a board hole.
  display: none
  connectivity:
  - lora
  - uart
  battery: powered by host badge
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: 30 assembled (10 fitted with the LoRa module and fully tested/labeled)
  availability: unknown
  distribution: []
  where: Distributed as swag at Supercon 2024; entered in the SAO Contest.
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/198109-sao-lora-walkie-talkie
  firmware_url: https://cdn.hackaday.io/files/1981098475895456/LoraTest.ino
  eda_tool: null
links:
- label: hackaday.io/project/198109-sao-lora-walkie-talkie
  url: https://hackaday.io/project/198109-sao-lora-walkie-talkie
  kind: hackaday
  archived: https://web.archive.org/web/20260506054919/https://hackaday.io/project/198109-sao-lora-walkie-talkie
- label: hackaday.io/project/198109-sao-lora-walkie-talkie/logs
  url: https://hackaday.io/project/198109-sao-lora-walkie-talkie/logs
  kind: hackaday
- label: Gerber/drill files (zip)
  url: https://cdn.hackaday.io/files/1981098475895456/SAOLoRaWalkieTalkie.zip
  kind: fab
- label: Arduino example code (LoraTest.ino)
  url: https://cdn.hackaday.io/files/1981098475895456/LoraTest.ino
  kind: repo
images:
- file: assets/images/badges/supercon-2024/sao-lora-walkie-talkie/cdfa64291d.png
  source: https://hackaday.io/project/198109-sao-lora-walkie-talkie
  credit: Jeremy Geppert
  caption: SAO Lora Walkie Talkie board, powered on with red PWR LED lit, plugged in over its test harness
  archived: https://web.archive.org/web/20260506054919/https://hackaday.io/project/198109-sao-lora-walkie-talkie
- file: assets/images/badges/supercon-2024/sao-lora-walkie-talkie/c03a4e465b.png
  source: https://hackaday.io/project/198109-sao-lora-walkie-talkie/logs
  credit: Jeremy Geppert
  caption: The 10 assembled and tested LoRa units, laid out for labeling
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198109-sao-lora-walkie-talkie
  title: SAO Lora Walkie Talkie
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260506054919/https://hackaday.io/project/198109-sao-lora-walkie-talkie
- kind: url
  url: https://hackaday.io/project/198109-sao-lora-walkie-talkie
  title: SAO Lora Walkie Talkie (project page)
  accessed: '2026-09-07'
  note: Confirmed maker, event (Supercon 8 / 2024, SAO Contest entry), components (Reyax RYLR998, SMD LED, 180ohm resistor, tactile switch, 6-pin SAO header), and design file links.
  archived: https://web.archive.org/web/20260506054919/https://hackaday.io/project/198109-sao-lora-walkie-talkie
- kind: url
  url: https://hackaday.io/project/198109-sao-lora-walkie-talkie/logs
  title: SAO Lora Walkie Talkie - build logs
  accessed: '2026-09-07'
  note: Confirmed quantity (30 assembled, 10 with LoRa module fitted and tested), PTT-as-reset function, LED part number and placement, and that the board is roughly quarter-sized.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price and general public availability were not stated anywhere on the project page or logs; it reads as event swag / contest entry rather than a sold item, so get_one fields beyond quantity are left empty/unknown. No repository (GitHub) was found, only the Hackaday.io project page hosting gerbers and example code directly.
last_modified_date: '2026-09-07'
---

The SAO Lora Walkie Talkie is a Simple Add-On built by Jeremy Geppert (JayGee) for Supercon 2024's SAO Contest, shaped like a miniature walkie-talkie complete with a printed antenna, speaker grille, and VOL/CH/SQL knobs silkscreened onto the board. Rather than actual audio, it carries a socket for a Reyax RYLR998 LoRa transceiver module, giving two badges wireless serial communication over simple AT commands. The board's "PTT" button is wired as a reset for the LoRa module rather than a real push-to-talk switch, and a single small red LED on the back lights up through a drilled hole as a power indicator.

Geppert assembled 30 of the boards for the event, but LoRa modules run about $12 each, so only 10 were actually populated, configured (9600 baud, network ID 8, sequential addresses), tested, and labeled; the rest went out as LED-and-button-only decorative SAOs that still work as a badge accessory without the radio. Design files — schematic, gerbers/drill files, and an example Arduino sketch for talking to the RYLR998 — are posted directly on the Hackaday.io project page rather than a separate repository.

## Make your own

Gerber and drill files are available as a zip from the project page, along with an example Arduino sketch (`LoraTest.ino`) for driving the Reyax RYLR998 over serial AT commands. The BOM is small: a 6-pin SAO header, an SMD red LED (CMD17-21VRD/TR8) with a 180-ohm series resistor, an SPST-NO tactile switch, and, if you want the radio to work, a Reyax RYLR998 module (~$12).
