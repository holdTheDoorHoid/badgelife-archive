---
title: CO2 Traffic Light SAO
id: supercon-2024-co2-traffic-light-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: David Bryant
  url: https://github.com/disquisitioner
summary: A CO2 air-quality SAO for the Hackaday Supercon 2024 badge that reads a Sensirion SCD40 sensor and shows the reading as a red/yellow/green "stoplight" on three LEDs.
functions: Monitors real-time CO2 concentration and displays overall air quality as a traffic-light indicator (red/yellow/green LEDs) driven off two SAO GPIO lines through discrete NAND-gate logic.
look:
  colors: []
  shape: rectangle
  themes:
  - measurement
  - hardware tool
tech:
  mcu: RP2040
  leds:
    count: 3
    type: discrete
    note: Red, yellow, and green rectangular through-hole LEDs (Lumex) with diffusers, decoded from two SAO GPIO lines by 74HC00 NAND-gate logic rather than driven individually.
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Personal project add-on David Bryant designed and wore at Hackaday Supercon 2024; not sold or distributed as a product.
make_your_own:
  open_source: true
  hardware_url: https://github.com/disquisitioner/Supercon-SAO/tree/main/2024/KiCad%20Projects
  firmware_url: https://github.com/disquisitioner/Supercon-SAO/tree/main/2024/MicroPython
  eda_tool: KiCad
links:
- label: hackaday.com/2024/11/06/a-co2-traffic-light-on-an-sao
  url: https://hackaday.com/2024/11/06/a-co2-traffic-light-on-an-sao/
  kind: article
  archived: https://web.archive.org/web/20251116054634/https://hackaday.com/2024/11/06/a-co2-traffic-light-on-an-sao/
- label: github.com/disquisitioner/Supercon-SAO/tree/main/2024
  url: https://github.com/disquisitioner/Supercon-SAO/tree/main/2024
  kind: repo
images:
- file: assets/images/badges/supercon-2024/co2-traffic-light-sao/66f689433b.png
  source: https://hackaday.com/2024/11/06/a-co2-traffic-light-on-an-sao/
  credit: David Bryant / Hackaday
  caption: The CO2 Traffic Light SAO with red, yellow, and green LED indicators
  archived: https://web.archive.org/web/20251116054634/https://hackaday.com/2024/11/06/a-co2-traffic-light-on-an-sao/
- file: assets/images/badges/supercon-2024/co2-traffic-light-sao/55e6d39b7e.jpg
  source: https://github.com/disquisitioner/Supercon-SAO/tree/main/2024
  credit: David Bryant
  caption: Prototype CO2 SAO PCB with SCD40 breakout connected via Qwiic
contact: {}
notes:
- Sensirion SCD40 CO2 sensor (Adafruit packaged breakout), 74HC00 NAND-gate GPIO decoding drives 3 discrete LEDs
- Built on prior air-quality sensing work the maker did with collaborator ericklein (github.com/ericklein/rco2, github.com/ericklein/air_quality)
- Prototyped in CircuitPython on an Adafruit Feather RP2040 before the badge's chip/language (RP2040/MicroPython) was confirmed; final firmware is MicroPython
status: released
sources:
- kind: url
  url: https://hackaday.com/2024/11/06/a-co2-traffic-light-on-an-sao/
  title: CO2 Traffic Light SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''Hackaday Supercon 2024''.'
  archived: https://web.archive.org/web/20251116054634/https://hackaday.com/2024/11/06/a-co2-traffic-light-on-an-sao/
- kind: url
  url: https://github.com/disquisitioner/Supercon-SAO/tree/main/2024
  title: 'disquisitioner/Supercon-SAO: 2024 Supercon badge add-on'
  accessed: '2026-09-07'
  note: Maker's own repo; confirmed chip, sensor, LED decoding logic, KiCad/MicroPython files, and MIT license.
- kind: url
  url: https://raw.githubusercontent.com/disquisitioner/Supercon-SAO/main/2024/README.md
  title: Supercon 2024 Badge Add-On Project README
  accessed: '2026-09-07'
  note: Maker's writeup of design story, components, and prototype photos; source of both saved images.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: This was a personal badge add-on David Bryant designed and wore himself at Supercon 2024, not a product sold or given out to attendees at scale, so price/quantity/availability fields are left empty (no sources give figures). Repo is MIT-licensed per GitHub API but the README does not itself state a license, so make_your_own.open_source is set yes based on the actual published KiCad and MicroPython/CircuitPython files, with license left unstated in front matter to avoid over-claiming a formal license notice.
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2024/co2-traffic-light-sao.glb
  method: kicad
  source_file: 2024/KiCad Projects/AQ-SAO/AQ-SAO.kicad_pcb
  generated: '2026-09-10'
  bytes: 104544
---

David Bryant built the CO2 Traffic Light SAO as his first Hackaday Supercon badge add-on for Supercon 2024, extending air-quality monitoring work he'd been doing with collaborator ericklein (creators of the rco2 and air_quality projects). The SAO reads a Sensirion SCD40 true CO2 sensor, mounted as an Adafruit-packaged breakout piggybacked on the main board via I2C/Qwiic, and reports overall air quality as a simple three-LED "stoplight": red, yellow, and green rectangular Lumex LEDs with diffusers. Rather than drive an RGB or addressable LED, Bryant chose to decode the two GPIO lines coming off the SAO connector into three discrete LED outputs using 74HC00 NAND-gate logic, a deliberate throwback to discrete digital design.

Design work began in September 2024, before the badge's own microcontroller was known, so Bryant prototyped in CircuitPython on an Adafruit Feather RP2040 standing in for the eventual badge. When Supercon's badge turned out to run an RP2040 under MicroPython, he ported the firmware accordingly. He also designed a small SAO breakout board in KiCad so the add-on could be developed and tested with either a female or male SAO connector before badge hardware was available. Bryant wore the finished SAO at Supercon 2024; it was a personal project rather than something sold or distributed to other attendees.

## Make your own

KiCad PCB projects for both the CO2 SAO and its companion test/breakout board, along with CircuitPython (prototype) and MicroPython (final) firmware, are published in the maker's GitHub repository at [disquisitioner/Supercon-SAO](https://github.com/disquisitioner/Supercon-SAO/tree/main/2024). The README documents the SCD40 sensor wiring, the NAND-gate LED decoding logic, and the LED part used (Lumex through-hole rectangular LEDs with diffusers).
