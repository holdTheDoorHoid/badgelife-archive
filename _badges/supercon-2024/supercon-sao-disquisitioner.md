---
title: Supercon-SAO (disquisitioner)
id: supercon-2024-supercon-sao-disquisitioner
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: disquisitioner
  url: https://github.com/disquisitioner
summary: A hobbyist-built SAO for Hackaday Supercon 2024 that reads live CO2 levels and shows air quality as a red/yellow/green "stoplight" of LEDs.
functions: Reads CO2 concentration from an onboard Sensirion SCD40 sensor and lights a red, yellow, or green LED to show "alert", "warning", or "good" air quality around the wearer.
look:
  colors: []
  shape: rectangle
  themes:
  - measurement
  - hardware tool
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: Red, yellow and green through-hole rectangular indicator LEDs (Lumex), driven by discrete digital logic from the SAO connector's two GPIO lines rather than a microcontroller on the add-on itself.
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: 'Not sold or distributed; a single one-off unit the maker designed, built, and wore at Supercon 2024.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/disquisitioner/Supercon-SAO/tree/main/2024/KiCad%20Projects
  firmware_url: https://github.com/disquisitioner/Supercon-SAO/tree/main/2024
  eda_tool: KiCad
links:
- label: github.com/disquisitioner/Supercon-SAO
  url: https://github.com/disquisitioner/Supercon-SAO
  kind: repo
images:
  - file: assets/images/badges/supercon-2024/supercon-sao-disquisitioner/dab24b7ac9.jpg
    source: "https://github.com/disquisitioner/Supercon-SAO"
    credit: "disquisitioner"
    caption: "Assembled CO2 SAO worn at Supercon 2024, showing the RGB stoplight LEDs and the Adafruit SCD40 breakout mounted on top"
  - file: assets/images/badges/supercon-2024/supercon-sao-disquisitioner/55e6d39b7e.jpg
    source: "https://github.com/disquisitioner/Supercon-SAO"
    credit: "disquisitioner"
    caption: "First working prototype PCB driving the red/yellow/green stoplight LEDs, with the SCD40 CO2 sensor connected via Qwiic"
contact: {}
notes:
- "Maker's repo groups the project under the general name 'Supercon SAO Projects'; the specific 2024 project is a CO2 air-quality add-on, referred to in the repo as the 'CO2 Add-On (SAO)' or 'AQ-SAO' (KiCad folder name)."
status: released
sources:
- kind: url
  url: https://github.com/disquisitioner/Supercon-SAO
  title: Supercon-SAO (disquisitioner)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''Hackaday Supercon''.'
- kind: url
  url: https://github.com/disquisitioner/Supercon-SAO/blob/main/2024/README.md
  title: 'Supercon 2024 Badge Add-On Project (README)'
  accessed: '2026-09-07'
  note: 'Primary source for what the SAO is, its build, components (SCD40 sensor, Lumex LEDs), design process, and photos.'
- kind: url
  url: https://github.com/disquisitioner/Supercon-SAO/tree/main/2024/KiCad%20Projects
  title: '2024/KiCad Projects folder'
  accessed: '2026-09-07'
  note: 'Confirms KiCad hardware design files exist for the add-on (AQ-SAO) and a companion SAO-Breakout test board.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own repo and README fully describe the project; it was a personal one-off build for Supercon 2024, not sold or mass-produced, so get_one fields are mostly empty by design. No MCU is on the add-on itself (the logic is discrete, driven by the host badge''s GPIO); the badge itself was expected to run MicroPython on an RP2040, per the README, but that is the host badge, not this SAO. No standalone price, quantity, or storefront found. sao_version (pin count) not stated anywhere in the repo.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/supercon-sao-disquisitioner/
---

"disquisitioner" (a GitHub handle) built this CO2 air-quality SAO for their first Hackaday Supercon in 2024. Rather than a smart RGB LED, the add-on uses three discrete red, yellow, and green through-hole LEDs as a "stoplight," driven directly by digital logic wired to the SAO connector's two GPIO lines — a deliberate throwback to the maker's college electronics days rather than the simplest modern approach. A Sensirion SCD40 CO2 sensor (on Adafruit's breakout board) reads air quality via I2C, and the add-on translates the reading into "good" (green), "warning" (yellow), or "alert" (red).

Because Supercon badge details aren't released until about a month before the event, the maker designed and prototyped the add-on around a stand-in Adafruit Feather RP2040 board, writing early code in CircuitPython before the actual 2024 badge turned out to run MicroPython. They used KiCad to design both the final add-on PCB and a separate SAO breakout board (with both male and female SAO connectors) so the add-on could be built and tested without having the real conference badge in hand. The finished board was worn at Supercon 2024 with the SCD40 sensor board piggybacked on top.

This was a one-off personal project, not sold, kitted, or distributed — the value here is the open KiCad design files and build write-up in the maker's repo, published under the MIT license alongside similar year-by-year Supercon SAO attempts.
