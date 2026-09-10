---
title: BSides Augusta 2019 Badge
id: bsides-augusta-2019-bsides-augusta-2019-badge
layout: badge
parent: BSides Augusta 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-augusta-2019
year: 2019
makers:
- name: David Ray / Ashwin Hamal (David Ray Electronics and More / Cyber City Circuits)
summary: A LilyPad-Arduino badge for BSides Augusta 2019 with a 4x6 LED matrix that displays the current time in binary.
functions: Shows the time in binary on a 4x6 LED matrix; two buttons set the time, and a power switch turns the display on and off without losing the time (it keeps counting while dark).
look:
  colors: []
  shape: null
  themes:
  - learn to solder
tech:
  mcu: LilyPad Arduino
  leds:
    count: 24
    type: discrete
    note: 4 rows x 6 columns, individually wired to microcontroller pins (not addressable)
  display: LED matrix 4x6
  connectivity: []
  battery: null
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
  firmware_url: https://github.com/CyberCityCircuits/BSides_Augusta_2019_Badge
  eda_tool: null
links:
- label: github.com/CyberCityCircuits/BSides_Augusta_2019_Badge
  url: https://github.com/CyberCityCircuits/BSides_Augusta_2019_Badge
  kind: repo
images: []
contact: {}
notes:
- Lilypad-Arduino-based badge with a 4x6 LED matrix that displays time in binary, built for BSides Augusta 2019. Found by the event-year sweep, task bsides-augusta.
status: released
sources:
- kind: url
  url: https://github.com/CyberCityCircuits/BSides_Augusta_2019_Badge
  title: BSides Augusta 2019 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-augusta); event read as ''BSides Augusta 2019''.'
- kind: url
  url: https://raw.githubusercontent.com/CyberCityCircuits/BSides_Augusta_2019_Badge/master/Readme.txt
  title: 'Readme.txt - CyberCityCircuits/BSides_Augusta_2019_Badge'
  accessed: '2026-09-10'
  note: Confirms function (binary time LED matrix, 4 rows x 6 columns), MCU (LilyPad Arduino, not USB variant), pinout, and both makers' names/contacts.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Repo confirms the badge and its function but has no photos of the assembled badge and no hardware design files (schematic/PCB), only firmware and a text readme, so make_your_own.open_source is set to partial. Price, quantity made, battery/power source, and availability could not be found in any source. No independent (non-maker) coverage located.
last_modified_date: '2026-09-10'
---

The BSides Augusta 2019 Badge was made by David Ray (David Ray Electronics and More) and Ashwin Hamal, working together as Cyber City Circuits, for BSides Augusta's 2019 event. It runs on a LilyPad Arduino and drives a 4x6 grid of individually-wired LEDs (24 in total) arranged as a matrix that displays the current time in binary. Two buttons set the time, and a power switch can turn the LED display off without resetting the clock, so the badge keeps time in the background while dark.

The project's GitHub repository holds the Arduino firmware and a short readme documenting the badge's pinout and use, but no schematic, PCB files, or photos of the finished badge were published alongside it, so it is only partially open source (firmware only). No price, production quantity, or distribution details were found; nothing beyond the maker's own repository was located discussing the badge.
