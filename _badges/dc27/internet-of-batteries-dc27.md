---
title: Internet of Batteries (DC27)
id: dc27-internet-of-batteries-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: Aask42 / Whiskey Pirate Crew
  url: https://github.com/Aask42
summary: A battery-badge/SAO hybrid ("DEF CELL") that back- or forward-powers other badges and add-ons over the SAO VCC pins while tracking power draw, built for DEF CON 27.
functions: Supplies 500mA @ 3.3V to power other badges/SAOs through the SAO header; monitors current with an INA219 shunt IC and can auto-disable backpower if current reverses. Hosts a "Captive Arcade" WiFi web UI for viewing battery/capacity stats. Runs an ESP32 WiFi mesh network ("Itero") for broadcast group chat and private messages to up to 25 nearby nodes. Five buttons cycle display modes, toggle backpower, trigger a light show via a capacitive touch strip, and a "safe mode" auto-engages on low battery.
look:
  colors:
  - green
  - gold
  shape: rectangle
  themes:
  - battery
  - hardware tool
  - radio
  - pirate
tech:
  mcu: ESP32
  leds:
    count: 8
    type: null
    note: 'Eight status LEDs: capacity levels (20/40/60/80/100%), node status, battery status, and power-output indicator.'
  display: none
  connectivity:
  - wifi
  battery: LiPoly, USB rechargeable
  sao_version: v1.69bis
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
  firmware_url: https://github.com/Aask42/InternetOfBatteries_DC27
  eda_tool: null
links:
- label: github.com/Aask42/InternetOfBatteries_DC27
  url: https://github.com/Aask42/InternetOfBatteries_DC27
  kind: repo
  archived: https://web.archive.org/web/20260115130833/https://github.com/Aask42/InternetOfBatteries_DC27
- label: Internet of Batteries (IoB-DC27) — Hackaday.io
  url: https://hackaday.io/project/172051-internet-of-batteries-iob-dc27
  kind: hackaday
images:
- file: assets/images/badges/dc27/internet-of-batteries-dc27/8046c96501.jpg
  source: https://hackaday.io/project/172051-internet-of-batteries-iob-dc27
  credit: Aask42 / Internet of Batteries
  caption: The Internet of Batteries DC27 SAO/badge ("DEF CELL"), pictured still sealed in its retail bag
contact: {}
notes:
- battery-source add-on for other badges/SAOs; GitHub repo, no hackaday.io page found
- A sequel, IoB-DC28, was made for DEF CON 28 with a Cypress PSOC5, RGB LEDs, and more capacity; that is a separate item.
status: released
sources:
- kind: url
  url: https://github.com/Aask42/InternetOfBatteries_DC27
  title: Internet of Batteries (DC27)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
  archived: https://web.archive.org/web/20260115130833/https://github.com/Aask42/InternetOfBatteries_DC27
- kind: url
  url: https://github.com/Aask42/InternetOfBatteries_DC27
  title: Aask42/InternetOfBatteries_DC27 README
  accessed: '2026-09-07'
  note: 'Maker''s own README: full feature list, button layout, boot behavior, board dimensions (~6.5cm x 3.5cm).'
  archived: https://web.archive.org/web/20260115130833/https://github.com/Aask42/InternetOfBatteries_DC27
- kind: url
  url: https://hackaday.io/project/172051-internet-of-batteries-iob-dc27
  title: Internet of Batteries (IoB-DC27) | Hackaday.io
  accessed: '2026-09-07'
  note: Hackaday.io project page; confirmed ESP32/INA219/SAO 1.69bis details and provided project photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own GitHub README and Hackaday.io project page agree on all core facts. Price, quantity made, and distribution method were not stated on either page. No separate storefront or fabrication-share link found. A DC28 sequel (IoB-DC28) exists as a distinct project and should get its own entry if not already archived.
last_modified_date: '2026-09-07'
---

The Internet of Batteries, nicknamed "DEF CELL," is a battery badge/SAO hybrid built by Aask42 (credited on the community sheet with the Whiskey Pirate Crew) for DEF CON 27 in 2019. Its whole premise is a dare: the SAO spec doesn't officially support a battery back-powering the host circuit over VCC, so the maker built one that does anyway, warning in the README that plugging it into the official DC27 badge "will most likely blow up the moon." In practice it is a self-contained LiPoly battery pack, built around an ESP32, that can push 500mA at 3.3V out through the SAO header to run other people's badges and add-ons, while an INA219 current-sense IC watches the shunt resistor and can cut backpower automatically if current starts flowing the wrong way.

Beyond being a power source, the badge is its own small ESP32 project: a "Captive Arcade" web interface (reached by joining its open WiFi AP) shows battery capacity and discharge stats, and a WiFi mesh network called Itero lets nearby units exchange broadcast or private messages with up to 25 other nodes. Eight LEDs report capacity in 20% steps plus node/battery/power-output state, five buttons handle mode-cycling, backpower toggling, a capacitive-touch light-show control hidden in the "DEF CON XXVII" text strip, and a "safe mode" kicks in automatically if the battery voltage drops too low.

Firmware is published on GitHub (with a modified fork of Adafruit's INA219 and AsyncTCP libraries), flashable over USB via PlatformIO; no hardware design files (schematic/Gerbers) were found alongside it, so it is only partially open source. Neither the GitHub repo nor the Hackaday.io project page states a price, production quantity, or how it was distributed at DEF CON 27. The maker built a direct sequel, IoB-DC28, for DEF CON 28 with an upgraded PSOC5-based design and RGB LEDs — that is a separate project and not covered by this entry.
