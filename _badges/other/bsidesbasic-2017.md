---
title: Flux Capacitor Badge (BsidesBASIC-2017)
id: other-bsidesbasic-2017
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2017
makers:
- name: Dale Nunns
  url: https://github.com/dalenunns
summary: The black "Flux Capacitor" attendee badge for BSides Cape Town 2017, an ESP8266 board running a custom BASIC interpreter with WiFi, telnet, and WS2812 LED control.
functions: 'Runs a small BASIC interpreter (LET, IF/THEN, GOTO, GOSUB/RETURN, FOR/NEXT, LED ON/OFF/BRIGHTNESS/FILL/SET/SHOW, etc.) accessible over a serial console or telnet (port 88) with ANSI/VT100 colour and cursor support. A PROGRAM button switches the badge into a WiFi access-point mode (SSID BADGE_*) with a web page for editing .bas files on the on-board SPIFFS filesystem. LEDs are disabled while in WiFi mode.'
look:
  colors:
  - black
  shape: rectangle
  themes:
  - retro computer
  - radio
tech:
  mcu: ESP8266
  leds:
    type: WS2812
    note: Controlled via the FastLED library; LED ON/OFF/BRIGHTNESS/FILL/SET/SHOW are exposed as BASIC commands.
  display: null
  connectivity:
  - wifi
  - uart
  battery: powered via soldered USB cable / power bank
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of BSides Cape Town 2017 (Dec 2, 2017) as the conference badge.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/dalenunns/BsidesBASIC-2017
  eda_tool: null
links:
- label: github.com/dalenunns/BsidesBASIC-2017
  url: https://github.com/dalenunns/BsidesBASIC-2017
  kind: repo
- label: 'leonjza: building the bsidescpt17 rf challenge'
  url: https://leonjza.github.io/blog/2017/12/13/building-the-bsidescpt17-rf-challenge/
  kind: article
- label: 'Telspace: Flux capacitors charged and back to the future'
  url: https://blog.telspace.co.za/2017/12/flux-capacitors-charged-and-back-to.html
  kind: article
images:
  - file: assets/images/badges/other/bsidesbasic-2017/917438c0da.jpg
    source: "https://leonjza.github.io/blog/2017/12/13/building-the-bsidescpt17-rf-challenge/"
    credit: "leonjza"
    caption: "Front of the BSides Cape Town 2017 Flux Capacitor badge"
  - file: assets/images/badges/other/bsidesbasic-2017/f5d853f828.jpg
    source: "https://leonjza.github.io/blog/2017/12/13/building-the-bsidescpt17-rf-challenge/"
    credit: "leonjza"
    caption: "Back of the BSides Cape Town 2017 Flux Capacitor badge, showing the two program/reset buttons"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://github.com/dalenunns/BsidesBASIC-2017
  title: BsidesBASIC-2017
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''bsides-cape-town-2017''.'
- kind: url
  url: https://github.com/dalenunns/BsidesBASIC-2017
  title: dalenunns/BsidesBASIC-2017 README
  accessed: '2026-09-07'
  note: "Maker's own README: confirms maker Dale Nunns, ESP8266 chip, BASIC interpreter feature list, WS2812/FastLED, telnet on port 88, SPIFFS storage, WiFi AP mode."
- kind: url
  url: https://leonjza.github.io/blog/2017/12/13/building-the-bsidescpt17-rf-challenge/
  title: 'building the bsidescpt17 rf challenge | #!/bin/note'
  accessed: '2026-09-07'
  note: "Confirms this was the 'Flux Capacitor' badge for BSides Cape Town 2017 (paired with a separate red RF badge built by others); describes black case, two rear buttons, USB power bank; source of the two saved photos."
- kind: url
  url: https://blog.telspace.co.za/2017/12/flux-capacitors-charged-and-back-to.html
  title: 'Telspace Africa: Flux capacitors charged and back to the future'
  accessed: '2026-09-07'
  note: "Confirms the Back to the Future / flux-capacitor theme and Dec 2, 2017 event date for BSides Cape Town 2017; no badge photos or hardware detail."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: "No matching bsides-cape-town-2017 event exists in _data/events.yml (only bsides-cape-town-2015 and bsides-cape-town-2016 are registered), so event is left as other; this badge was made for BSides Cape Town 2017, held 2 December 2017. It was one of two badges issued that year: this black Flux Capacitor badge (ESP8266, BASIC interpreter, WiFi/telnet) and a separate red RF badge (CC1111, RFCat-compatible) used for an RF CTF challenge; the RF badge is a different item and not covered by this entry. Price, quantity made, and whether hardware design files (schematic/PCB) were ever published could not be found - only firmware/software is on GitHub. Availability left unknown since it was a free con badge, not sold."
last_modified_date: '2026-09-07'
---

The Flux Capacitor badge was the attendee badge for BSides Cape Town 2017, held December 2, 2017 under a "Back to the Future" theme. Built around an ESP8266 and housed in a black case, it runs firmware written by Dale Nunns implementing a small custom BASIC interpreter, complete with its own commands for loops, conditionals, subroutines, and direct control of an onboard strip of WS2812 LEDs (turning them on/off, setting brightness, and filling or setting individual pixel colors). Programs could be written and run over a serial console, or over telnet on port 88, both using ANSI/VT100 escape codes for colour and cursor control in the terminal.

Pressing a PROGRAM button on the back of the badge switched it into a WiFi access-point mode (SSID `BADGE_*`), disabling the LEDs and exposing a small web page at `192.168.4.1` for editing the BASIC programs stored on the badge's SPIFFS flash filesystem; the same interface could also be reached by telnet. The badge shipped with a set of example `.bas` programs written by contributor @HypnZA. It was paired that year with a separate red "RF badge" built around a CC1111 RFCat-compatible radio chip, used for a standalone RF capture-the-flag challenge — a different piece of hardware from a different part of the team, not covered by this entry.

The firmware and SPIFFS filesystem contents are published on GitHub, along with prebuilt binary images and deployment instructions for the Arduino IDE and esptool; no hardware schematic, PCB files, or bill of materials were found published anywhere, so the entry's `make_your_own.open_source` is marked `partial` (firmware only). No pricing or production-quantity figures were located — as a conference-issued badge it was not sold.

## Make your own

The firmware can be rebuilt from source with the Arduino IDE (ESP8266 board support 2.4.0-rc2, plus the ESPAsyncTCP, ESPAsyncWebServer, and FastLED libraries) or flashed directly from the prebuilt binaries in the repository's `bin/` folder using `esptool` (see `upload-commands.txt`). The badge must be put into a programming mode (hold PROGRAM and press RESET, or hold PROGRAM while power-cycling on single-button units) before flashing the Arduino sketch and then again before uploading the SPIFFS data via "ESP8266 Sketch Data Upload."
