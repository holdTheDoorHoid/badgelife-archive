---
title: MalO SAO
id: dc34-malo
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: ParallelLogic
  url: https://github.com/parallellogic-/
summary: 'An SCP-1471-A themed SAO packed with an OLED display, 50+ LEDs, sensors, and IR chat between units, sold at DEF CON 34.'
functions: 'IR chat between units, mini-games and logic puzzles, LED animations, and sensor-driven interactions (touch, potentiometer, accelerometer/gyro, light, microphone).'
look:
  colors: []
  shape: null
  themes:
  - horror
  - security
  - sci-fi
tech:
  mcu: RP2350B
  leds: 'over 50 LEDs plus a red-green status LED'
  display: 1.5" 128x128 grayscale OLED
  connectivity:
  - ir
  - usb
  - rfid
  battery: null
  sao_version: null
get_one:
  price: $50
  price_usd: 50.0
  quantity: '64'
  availability: sold_out
  distribution:
  - purchase
  where: Sold through the maker's Uberflux storefront (uberflux.com/product/PL-1471) for DEF CON 34, August 2026.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/parallellogic-/MalO_SAO
  firmware_url: https://github.com/parallellogic-/MalO_SAO
  eda_tool: null
links:
- label: uberflux.com/product/PL-1471
  url: https://uberflux.com/product/PL-1471
  kind: store
- label: github.com/parallellogic-/MalO_SAO
  url: https://github.com/parallellogic-/MalO_SAO
  kind: repo
- label: github.com/parallellogic-
  url: https://github.com/parallellogic-/
  kind: repo
images:
  - file: assets/images/badges/dc34/malo/1fdfaaabf3.jpg
    source: "https://uberflux.com/product/PL-1471"
    credit: "ParallelLogic"
    caption: "MalO SAO product photo"
  - file: assets/images/badges/dc34/malo/c13cc31a18.jpg
    source: "https://uberflux.com/product/PL-1471"
    credit: "ParallelLogic"
    caption: "MalO SAO detail photo"
contact:
  discord: ParallelLogic
  emails:
  - parallellogic@gmail.com
notes:
- 'Duplicate: another archive entry (dc34-malo-sao) covers the same item.'
status: released
sources:
- kind: sheet
  event: dc34
  row: 21
  updated: 6/19/2026 17:04:26
  listing: New
- kind: url
  url: https://uberflux.com/product/PL-1471
  title: 'MalO SAO - Uberflux product listing'
  accessed: '2026-09-06'
  note: 'Price, quantity sold (64, sold out), feature list, and product photos.'
- kind: url
  url: https://github.com/parallellogic-/MalO_SAO
  title: 'parallellogic-/MalO_SAO on GitHub'
  accessed: '2026-09-06'
  note: 'MCU (RP2350B), display, sensors, IR details, and CC BY-SA 3.0 open-source license for hardware and firmware.'
- kind: url
  url: https://github.com/parallellogic-/
  title: 'parallellogic- GitHub profile'
  accessed: '2026-09-06'
  note: 'Confirms maker identity and repo listing; no additional DC34-specific details found.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Core facts confirmed directly from the maker''s own storefront and GitHub repo. Could not find a Hackaday.io project page (web search budget was exhausted before this could be checked). This entry duplicates dc34-malo-sao, which covers the same item; left as-is per instructions rather than merging.'
last_modified_date: '2026-09-06'
---

MalO is an SAO themed around the SCP Foundation's "SCP-1471-A" entity, made by ParallelLogic and sold at DEF CON 34 in August 2026. It packs a 1.5" 128x128 grayscale OLED display and more than 50 onboard LEDs onto an RP2350B-based board, alongside a wide sensor suite: accelerometer/gyroscope, ambient light and thermal sensors, a microphone, capacitive touch buttons, and a rotary potentiometer. A buzzer and vibration motor add haptic and audio feedback, and a passive 13.56 MHz RFID/NFC tag and IR transmit/receive hardware (940 nm, 38 kHz, with a default single IR transmitter upgradeable to three via a solder jumper) let units talk to each other and to a host badge.

The board runs mini-games, logic puzzles, and LED animations, with IR chat as a headline feature for interacting with other MalO units nearby. ParallelLogic sold 64 units for $50 each through their Uberflux storefront, and the listing was sold out as of research. Both the hardware design and firmware are published on GitHub under a Creative Commons Attribution-ShareAlike 3.0 Unported license, making it fully open source.

This archive entry duplicates another entry for the same item, dc34-malo-sao, from the same maker and GitHub repository.
