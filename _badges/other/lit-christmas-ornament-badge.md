---
title: Lit Christmas Ornament/Badge
id: other-lit-christmas-ornament-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: Jeff Wurz (thelogicofpi)
  url: https://hackaday.io/thelogicofpi
summary: A PCB Christmas ornament shaped like a house strung with lights, using an I2C I/O expander to drive 16 individually-controllable LEDs through several animation modes.
functions: 'A single power button cycles through display modes (all-on, flashing, alternating, binary counter, "knight rider" scanner, random), then locks in the chosen pattern to loop on repeat.'
look:
  colors: []
  shape: house
  themes:
  - holiday
tech:
  mcu: ATtiny85
  leds:
    count: 16
    type: discrete
    note: 16 individual LEDs (red, orange, yellow, green, blue) driven via an MCP23017 I2C I/O expander
  display: none
  connectivity:
  - i2c
  battery: CR2032
  sao_version: none
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
  firmware_url: https://github.com/jeffwurz/lit_christmas_ornament
  eda_tool: null
links:
- label: hackaday.io/project/162585-lit-christmas-ornamentbadge
  url: https://hackaday.io/project/162585-lit-christmas-ornamentbadge
  kind: hackaday
- label: github.com/jeffwurz/lit_christmas_ornament
  url: https://github.com/jeffwurz/lit_christmas_ornament
  kind: repo
- label: hackster.io/jeffwurz/lit-house-christmas-ornament
  url: https://www.hackster.io/jeffwurz/lit-house-christmas-ornament-18bd0c
  kind: article
images:
- file: assets/images/badges/other/lit-christmas-ornament-badge/7d2eb24808.jpg
  source: "https://hackaday.io/project/162585-lit-christmas-ornamentbadge"
  credit: "thelogicofpi (Jeff Wurz)"
  caption: "The Lit Christmas Ornament/Badge PCB, styled as a house decorated with Christmas lights"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/162585-lit-christmas-ornamentbadge
  title: Lit Christmas Ornament/Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/162585-lit-christmas-ornamentbadge
  title: Lit Christmas Ornament/Badge
  accessed: '2026-09-07'
  note: Primary source for maker, chip (ATtiny85 + MCP23017), LED count, battery, and display modes; project logged December 2018.
- kind: url
  url: https://github.com/jeffwurz/lit_christmas_ornament
  title: jeffwurz/lit_christmas_ornament
  accessed: '2026-09-07'
  note: Firmware repo (Arduino sketch); confirms mode-cycling behavior via a single power button. No hardware design files (Gerbers/schematic) found in the repo.
- kind: url
  url: https://www.hackster.io/jeffwurz/lit-house-christmas-ornament-18bd0c
  title: Lit House Christmas Ornament - Hackster.io
  accessed: '2026-09-07'
  note: 'Mirror listing found via web search; page returned HTTP 403 to automated fetch so could not be read directly.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a personal holiday project posted to Hackaday.io in December 2018, not a badge made for a specific hacker conference — no con or CTF affiliation is mentioned on the project page, the GitHub repo, or in web search results, so event is left as "other". Price, quantity made, and availability are not stated anywhere found; it reads as a one-off/DIY build shared as an open design rather than a sold item. Firmware is public on GitHub; no hardware files (schematic/Gerbers) were found, so open_source is marked partial rather than yes. The Hackster.io mirror of the same project returned a 403 to automated fetch and could not be checked directly.
last_modified_date: '2026-09-07'
---

The Lit Christmas Ornament/Badge is a small PCB shaped and silkscreened to look like a house decorated with Christmas lights, built by Jeff Wurz (Hackaday.io handle thelogicofpi) and posted to Hackaday.io in December 2018. It is not tied to a specific hacker conference; it appears to be a personal holiday electronics project shared with the badgelife-adjacent maker community rather than sold or distributed at an event.

Under the hood, an ATtiny85 drives an MCP23017 I2C I/O expander to individually control 16 LEDs in red, orange, yellow, green, and blue, standing in for strings of Christmas lights on the house. A single power button cycles through several animation modes — all LEDs on, flashing, alternating patterns, a binary counter, a "knight rider" style scanner, and random flicker — and powering the board off mid-pattern locks in that mode to loop indefinitely on the next power-up. It runs from a single CR2032 coin cell, with firmware using watchdog-timer tricks to manage power draw during longer animations.

The firmware (an Arduino sketch) is published on GitHub at jeffwurz/lit_christmas_ornament, but no hardware design files (schematic or Gerbers) were located, so the project is only partially open source. No price, production quantity, or distribution details were found for this build.
