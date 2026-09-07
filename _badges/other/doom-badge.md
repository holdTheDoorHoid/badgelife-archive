---
title: DOOM Badge
id: other-doom-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: avr
  url: https://hackaday.io/adamjvr
summary: A wearable badge shaped like a classic IBM PC (monitor on top, keyboard below) that runs id Software's DOOM on an ESP32, built for the 2018 Hackaday Prize.
functions: Plays DOOM using the Espressif esp32-doom port; planned Bluetooth pairing with phones or game controllers (Nintendo Pro, Xbox, PlayStation) and possible WiFi multiplayer.
look:
  colors: []
  shape: rectangle
  themes:
  - video game
  - retro computer
tech:
  mcu: ESP32 (WROOM module)
  leds: null
  display: ST7735R LCD
  connectivity:
  - wifi
  - ble
  battery: 3.7V LiPo with USB charging
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/126670-doom-badge
  url: https://hackaday.io/project/126670-doom-badge
  kind: hackaday
images:
  - file: assets/images/badges/other/doom-badge/c9707524a0.png
    source: "https://hackaday.io/project/126670-doom-badge"
    credit: "avr"
    caption: "DOOM Badge project photo"
  - file: assets/images/badges/other/doom-badge/f2a44dcaec.jpg
    source: "https://hackaday.io/project/126670-doom-badge"
    credit: "avr"
    caption: "DOOM Badge PCB/display detail"
contact: {}
notes: []
status: announced
sources:
- kind: url
  url: https://hackaday.io/project/126670-doom-badge
  title: DOOM Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/126670-doom-badge
  title: DOOM Badge project page and log
  accessed: '2026-09-07'
  note: 'Confirmed maker (avr), ESP32/ST7735R hardware, LiPo+USB power, Game Boy-shaped PCB, and 2018 Hackaday Prize entry date (2018-04-10); no evidence of it being built for or distributed at any specific hacker convention.'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This is a 2018 Hackaday Prize / Open Hardware Design Challenge submission, not a badge made for a specific hacker con — event left as "other" since no matching con was found in events.yml. Fact-check pass (2026-09-07) against the live Hackaday.io project page found two errors and corrected them: (1) the maker''s profile URL was wrong — https://hackaday.io/avr resolves to an unrelated user ("ak1376"); the project''s actual author link is https://hackaday.io/adamjvr (display name "AVR"), now fixed. (2) the summary/body called the PCB "Game Boy-shaped." The project''s own quick-specs blurb does say "gameboy shaped PCB," but this contradicts the project''s dev logs ("I want it to look kind of like a old school IBM PC") and, decisively, the two saved photos themselves, which show a monitor-and-keyboard IBM-PC desktop silhouette, not a handheld Game Boy shape — corrected text and dropped the unsupported "console" theme tag accordingly. Confirmed via the live project page: maker (AVR/adamjvr), creation date 04/10/2018, ESP32 WROOM MCU with WiFi+BLE, ST7735R LCD, 3.7V LiPo w/ USB charging, expansion I/O (SX1509 I2C IO expander for the keyboard), the Espressif esp32-doom software base, and the stated (unrealized) plans for Bluetooth phone/controller pairing and WiFi multiplayer. The page shows no bill of materials, schematics, published firmware/hardware repo link, price, or production quantity, and no evidence it was ever manufactured beyond a prototype. Not to be confused with the unrelated DEF CON "MicroDOOM" or "MF Doom SAO" entries already in the archive.'
last_modified_date: '2026-09-07'
---

The DOOM Badge is a wearable electronic badge built by Hackaday.io user "avr" (AVR) as an entry in the 2018 Hackaday Prize and Open Hardware Design Challenge. It runs id Software's DOOM on an ESP32 (WROOM module), driving an ST7735R LCD display, and is powered by a 3.7V LiPo battery with USB charging. The PCB is shaped like a classic desktop IBM PC — a monitor-shaped upper section for the screen sitting above a keyboard-shaped lower section — and includes expansion I/O built around an SX1509 I2C IO expander for the keyboard.

The software builds on Espressif's existing esp32-doom port rather than a from-scratch DOOM engine. The maker's stated plans included Bluetooth pairing with a phone or standard game controllers (Nintendo Pro, Xbox, PlayStation), and possibly WiFi-based multiplayer, though the project's public log entries do not show these features being completed or the badge reaching a distributed, sellable state.

Unlike most entries in this archive, the DOOM Badge was not built for or handed out at a specific hacker convention — it is a standalone Hackaday Prize submission. No bill of materials, schematics, firmware repository, price, or production quantity are published on the project page, so those fields are left empty rather than guessed.
