---
title: AND!XOR DC25 Badge
id: dc25-and-xor-dc25-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: AND!XOR
  url: https://hackaday.io/AndNXOR
summary: 'A Bender-head-shaped, WS2812-covered electronic badge for DEF CON 25 built around a Nordic nRF52 (Rigado BMD-300) and a 1.44" color TFT, with a CHIP-8 emulator, badge-to-badge BLE games, and thousands of LED animation modes.'
functions: 'Cycles through roughly 2,820 "bling" LED animation patterns; runs a CHIP-8/SCHIP emulator that plays 64+ classic ROMs; exposes a TCL-based scripting engine for controlling the hardware; plays a badge-to-badge wireless mesh game over Bluetooth; pairs with a companion Android app; supports loading custom animations from a microSD card ("Bring Your Own Bling").'
look:
  colors: [black, white, green]
  shape: robot
  themes: [robot, sci-fi, tv, ctf, wearable]
tech:
  mcu: Nordic nRF52 (Rigado BMD-300 module)
  leds:
    count: 15
    type: WS2812B
    note: RGB "NeoPixel" LEDs used for the badge's animation modes
  display: 1.44" color TFT LCD, 128x128
  connectivity: [ble, bluetooth]
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'approximately 500'
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/19121-andxor-dc25-badge
  url: https://hackaday.io/project/19121-andxor-dc25-badge
  kind: hackaday
  archived: https://web.archive.org/web/20251026123457/https://hackaday.io/project/19121-andxor-dc25-badge
images:
  - file: assets/images/badges/dc25/and-xor-dc25-badge/647139130a.jpg
    source: "https://hackaday.io/project/19121-andxor-dc25-badge"
    credit: "AND!XOR"
    caption: "The assembled AND!XOR DC25 badge PCB, shaped like Bender's head, with its color LCD, WS2812 LEDs, and SAO-style header"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/19121-andxor-dc25-badge
  title: AND!XOR DC25 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''DEF CON 25''.'
  archived: https://web.archive.org/web/20251026123457/https://hackaday.io/project/19121-andxor-dc25-badge
- kind: url
  url: https://hackaday.io/project/19121-andxor-dc25-badge
  title: AND!XOR DC25 Badge
  accessed: '2026-09-07'
  note: "Maker's own Hackaday.io project page: description of hardware (nRF52/BMD-300, 128x128 TFT, 15 WS2812B LEDs, microSD, tilt/light sensors), firmware features (CHIP-8 emulator, TCL scripting, ~2,820 LED modes, badge-to-badge BLE game, Android app), ~500 units produced, and open-source hardware/firmware claim. Also source of the badge photo used."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: "Confirmed as the AND!XOR badge for DEF CON 25 (2017) from the maker's own Hackaday.io project page. That page states the design (VRML/SVG/DXF models) and ~11,000 lines of firmware are open-source, but the specific repo/Gerber/BOM URLs were not located in the fetched page content, so hardware_url/firmware_url/gerbers_url are left empty rather than guessed. No price, exact distribution method (sold vs. included with con badge), or battery/power spec was found in the sources checked, so those fields are left empty. No separate storefront, press coverage (hackaday.com), or social posts were checked this pass due to search-budget limits; only the project's own Hackaday.io page was available as a source. A gallery image on that page (a pinout diagram for the badge's 6-pin GPIO header) suggests a custom expansion header rather than a standard SAO connector, so tech.sao_version was left null rather than guessed. AND!XOR is confirmed to have made a badge for several other DEF CONs (dc26, dc27, and per existing archive entries dc30-dc33), so this DC25 badge is part of an annual line, though no formal series name was found."
last_modified_date: '2026-09-07'
---

The AND!XOR DC25 badge was the DEF CON 25 (2017) entry in AND!XOR's series of independently made hacker-conference badges, shaped like Bender's head from *Futurama*. It is built around a Nordic nRF52 ARM Cortex-M4F (in a Rigado BMD-300 module) with 512KB of flash and 64KB of RAM, a 1.44" 128x128 color TFT display capable of playing back video at 19+ frames per second, and 15 WS2812B RGB LEDs arranged as the character's mouth and glowing eyes. A microSD slot, tilt and ambient-light sensors, and an exposed 5-pin GPIO header round out the hardware.

On the software side the badge shipped with roughly 2,820 selectable LED animation modes, a CHIP-8/SCHIP emulator able to run more than 64 classic ROMs, a TCL-based scripting engine for driving the hardware, and a badge-to-badge wireless game played over Bluetooth, paired with a companion Android app. A "Bring Your Own Bling" feature let owners load their own animations from the SD card. The team, described on their project page as five California-based hardware/software engineers, produced approximately 500 units and describe the hardware and firmware (nearly 11,000 lines of code) as open source, following on from their DC24 badge and continuing into badges for later DEF CONs.
