---
title: DC31_SAO "SEGoSaurus"
id: dc31-sao-segosaurus
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: Blorfus
  url: https://github.com/Blorfus
summary: A double-board SAO built around an ESP12F (ESP8266) driving a 14-segment alphanumeric display, meant to show a WiFi SSID or a custom scrolling message.
functions: Displays a WiFi SSID or a custom message on a 14-segment alphanumeric display; a companion HTML character-creator utility helps compose the segment patterns.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - text
tech:
  mcu: ESP8266 (ESP12F)
  leds: null
  display: 14-segment alphanumeric (JMF-4473BP3-59P6.8)
  connectivity:
  - wifi
  - i2c
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '1 (only functional prototype)'
  availability: cancelled
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/Blorfus/DC31_SAO/tree/main/code
  eda_tool: null
links:
- label: github.com/Blorfus/DC31_SAO
  url: https://github.com/Blorfus/DC31_SAO
  kind: repo
images:
  - file: assets/images/badges/dc31/sao-segosaurus/c1fd07522c.jpg
    source: "https://github.com/Blorfus/DC31_SAO"
    credit: "Blorfus"
    caption: "V1 prototype SEGoSaurus SAO board"
  - file: assets/images/badges/dc31/sao-segosaurus/f19fd4d2a2.jpg
    source: "https://github.com/Blorfus/DC31_SAO"
    credit: "Blorfus"
    caption: "V1 display PCB with 14-segment alphanumeric display"
contact: {}
notes:
- Sweep's summary line ("Custom SAO designed to fit the Defcon 31 badge chamber; production issues meant only a single functional unit existed at the con") is confirmed accurate by the maker's own README.
- Maker states the project will continue as the basis for a DC32 revision; no evidence found that a later version shipped.
status: cancelled
sources:
- kind: url
  url: https://github.com/Blorfus/DC31_SAO
  title: DC31_SAO "SEGoSaurus"
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc31-saos); event read as ''dc31''.'
- kind: url
  url: https://github.com/Blorfus/DC31_SAO
  title: 'Blorfus/DC31_SAO README'
  accessed: '2026-09-10'
  note: 'Confirmed the SAO is real, and supplied maker, event, MCU, display, connector pinout, quantity made, and open-source status.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Maker''s own GitHub repo confirms the item and all core facts; no press coverage, storefront, or Hackaday post found. No hardware/PCB design files (schematic, Gerbers, KiCad project) are in the repo, only Arduino firmware and a character-creator utility, so open_source is marked "partial" rather than "yes". Price and full quantity-made figures are not stated beyond "only one functional prototype."'
last_modified_date: '2026-09-10'
---

The SEGoSaurus is a double-board SAO that Blorfus designed to plug into the Defcon 31 badge. It pairs an ESP12F (ESP8266) module with a JMF-4473BP3-59P6.8 14-segment alphanumeric display driven through an MCP23017 I/O expander, connected over a 4-pin I2C intraboard connector. The intent was for the display to show a WiFi SSID or a custom message, with a small HTML-based character-creator utility included to help compose segment patterns for the display's slightly irregular pinout.

Production of the SAO was never completed in time for DC31 because of manufacturing delays, so only the maker's own prototype unit ever worked. The hardware design (schematics, PCB files) has not been published; only the Arduino firmware and the character utility are in the repo, under a GPL-3.0 license. The README notes the project may continue toward a DC32 revision, but no evidence of a later release was found.
