---
title: Breadbadge
id: dc34-breadbadge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Tw0nkus
  url: https://uberflux.com/maker/tw0nkus
summary: A DEF CON 34 badge that doubles as a breadboard prototyping tool, with an RP2354A, a colour display, six WS2812 LEDs, an INA3221 power monitor and UART/UPDI/I2C breakouts.
functions: Display UI and animations; WS2812 LED animations; UPDI tools (ping, erase, flash); I2C tools; power sensing (voltage, current, power via INA3221); breadboard-compatible breakout headers for UART, UPDI, I2C, 5V, 3.3V and debug.
look:
  colors:
  - green
  shape: rectangle
  themes:
  - hardware tool
  - measurement
  - text
tech:
  mcu: RP2354A
  leds:
    count: 6
    type: WS2812
    note: RGB
  display: ST7789 SPI display
  connectivity:
  - uart
  - i2c
  battery: null
  sao_version: null
  inputs:
  - joystick
  - buttons
get_one:
  price: $80
  price_usd: 80
  quantity: 5
  availability: sold_out
  availability_note: Uberflux listing showed 0 remaining, 5 sold of 5 on 2026-09-07.
  distribution:
  - purchase
  where: Sold through the maker's Uberflux store at $80; the listing shows all 5 units sold.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: Uberflux store listing
  url: https://uberflux.com/product/TW0N-breadbadge
  kind: store
  archived: https://web.archive.org/web/20260727052656/https://uberflux.com/product/TW0N-breadbadge
- label: Tw0nkus on Uberflux
  url: https://uberflux.com/maker/tw0nkus
  kind: store
  archived: https://web.archive.org/web/20260727052709/https://uberflux.com/maker/tw0nkus
images:
- file: assets/images/badges/dc34/breadbadge/78b8032493.jpg
  source: https://uberflux.com/product/TW0N-breadbadge
  credit: Tw0nkus (Uberflux listing)
  caption: Breadbadge, from the Uberflux store listing
  archived: https://web.archive.org/web/20260727052656/https://uberflux.com/product/TW0N-breadbadge
contact:
  emails:
  - Alee97422@gmail.com
notes:
- The community sheet lists the maker as alee97422; the Uberflux store lists the same badge under the maker name Tw0nkus.
status: released
sources:
- kind: sheet
  event: dc34
  row: 48
  updated: 7/22/2026 12:55:43
  listing: Update to Existing
- kind: url
  url: https://uberflux.com/product/TW0N-breadbadge
  title: Breadbadge - Uberflux
  accessed: '2026-09-07'
  note: Price, event (Defcon34), hardware list (RP2354A, INA3221, ST7789 SPI display, 6 WS2812 RGB LEDs, joystick and back button, breakouts), firmware features, stock (0 remaining, 5 sold of 5) and product photo.
  archived: https://web.archive.org/web/20260727052656/https://uberflux.com/product/TW0N-breadbadge
- kind: url
  url: https://uberflux.com/maker/tw0nkus
  title: Tw0nkus - Uberflux
  accessed: '2026-09-07'
  note: Maker page listing Breadbadge ($80) and Rust Crab Badge ($35).
  archived: https://web.archive.org/web/20260727052709/https://uberflux.com/maker/tw0nkus
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Verified against the maker''s Uberflux listing, which the earlier research pass had missed. The listing headline says "RP2354A main MCU" while one bullet mentions "the onboard RP2350"; the RP2354A wording is used throughout and matches the Raspberry Pi package in the photo, so mcu is recorded as RP2354A. Colour and shape are taken from the listing photo (green rectangular PCB, "HACK EVERYTHING" silkscreen). Not stated anywhere: battery, SAO header, open-source files. Sheet handle alee97422 vs store name Tw0nkus is noted in notes.'
last_modified_date: '2026-09-07'
---

Breadbadge is a DEF CON 34 badge by Tw0nkus, sold on Uberflux for $80 with the tagline "Badge by day, breadboard prototyping tool by night." The board carries an RP2354A, an ST7789 SPI colour display, six WS2812 RGB LEDs, a navigation joystick with a back button, and an INA3221 voltage, current and power monitor. Along the bottom edge it breaks out UART, UPDI, I2C, 5 V, 3.3 V and debug headers so it can sit on a breadboard and act as a bench tool.

The firmware provides a menu-driven display UI with animations, LED animations, UPDI tools for pinging, erasing and flashing targets, I2C tools, and a power-sensing screen. The listing shows a run of five units, all sold.
