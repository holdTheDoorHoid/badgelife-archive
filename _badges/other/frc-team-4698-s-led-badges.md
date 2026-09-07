---
title: FRC Team 4698's LED Badges
id: other-frc-team-4698-s-led-badges
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: Rush Robbins
  url: https://hackaday.io/robbinsrush
  role: designer (FRC Team 4698, "Rio Robotics")
summary: A wearable name badge built by FIRST Robotics Competition Team 4698 (Rio Robotics), showing scrolling text on two 8x8 LED matrix displays.
functions: Displays user-configurable scrolling text with adjustable brightness, speed, and scroll direction, saved to EEPROM. Holding a button and pressing reset boots into a WiFi setup mode so the text/settings can be changed from a phone or computer without re-flashing.
look:
  colors:
  - green
  shape: rectangle
  themes:
  - text
  - robot
tech:
  mcu: ESP8266 (Wemos D1 Mini)
  leds:
    count: 128
    type: discrete
    note: Two common-cathode 32mm x 32mm 8x8 LED matrix modules (1088AS), each driven by a MAX7219 driver IC.
  display: LED matrix 16x8 (two 8x8 modules)
  connectivity:
  - wifi
  inputs:
  - buttons
  battery: Optional single 18650 Li-ion cell with charge/protect/boost circuit; can also run from external 3V/5V input
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Not sold; built by the maker for teammates on FRC Team 4698. Design files are public for anyone to build their own.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/robbinsrush/Team4698Badge
  firmware_url: https://github.com/robbinsrush/Team4698Badge
  eda_tool: EasyEDA
  license: GPL-3.0
  notes: Repo includes firmware, PCB/schematic files, and 3D models. PCB was manufactured by JLCPCB. A shared copy of the PCB also appears on OSHWLab.
links:
- label: hackaday.io/project/75999-frc-team-4698s-led-badges
  url: https://hackaday.io/project/75999-frc-team-4698s-led-badges
  kind: hackaday
- label: github.com/robbinsrush/Team4698Badge
  url: https://github.com/robbinsrush/Team4698Badge
  kind: repo
- label: 'video demo (streamable)'
  url: https://streamable.com/58ed7
  kind: video
images:
- file: assets/images/badges/other/frc-team-4698-s-led-badges/9f2338f14d.jpg
  source: "https://hackaday.io/project/75999-frc-team-4698s-led-badges"
  credit: "Rush Robbins"
  caption: "The bare LED-badge PCB, showing the two MAX7219 driver ICs that drive the matrix displays"
- file: assets/images/badges/other/frc-team-4698-s-led-badges/ee78ff04a3.jpg
  source: "https://hackaday.io/project/75999-frc-team-4698s-led-badges"
  credit: "Rush Robbins"
  caption: "The assembled badge lit up and displaying scrolling text, with the Wemos D1 Mini module and \"TEAM 4698\" silkscreen visible"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/75999-frc-team-4698s-led-badges
  title: FRC Team 4698's LED Badges
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/75999-frc-team-4698s-led-badges
  title: FRC Team 4698's LED Badges - Hackaday.io
  accessed: '2026-09-07'
  note: 'Maker, event context, functions, MCU, LED driver, EasyEDA/JLCPCB fabrication, and GitHub/video links.'
- kind: url
  url: https://github.com/robbinsrush/Team4698Badge
  title: robbinsrush/Team4698Badge
  accessed: '2026-09-07'
  note: 'Confirmed hardware detail (Wemos D1 Mini, two 1088AS 8x8 matrices, MAX7219 x2, button count, optional 18650 battery circuit), GPL-3.0 license, and a 3D-model image.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This is a robotics-team club badge, not a hacker-conference badge, so it has no matching entry in _data/events.yml and is left under event: other. Year (2018) is the Hackaday.io project creation date, since no specific event date is given. Price/quantity made and exact battery capacity are not stated by the maker.'
last_modified_date: '2026-09-07'
---

Rush Robbins designed this LED name badge for teammates on FIRST Robotics Competition Team 4698, known as Rio Robotics, publishing the project to Hackaday.io in March 2018. Rather than a badge made for a hacker convention, it's a club project: a Wemos D1 Mini (ESP8266) drives two 32mm common-cathode 8x8 LED matrix modules through a pair of MAX7219 driver chips, scrolling custom text across the display at a configurable brightness, speed, and direction. Those settings are stored in EEPROM, and holding a button while resetting the board drops it into a WiFi configuration mode, so wearers can change their message without re-flashing the firmware.

The badge can run from an external 3-5V supply or an onboard single-cell 18650 Li-ion battery with its own charge/protect/boost circuitry. Robbins designed the PCB in EasyEDA and had it built by JLCPCB; a copy of the design is also mirrored on OSHWLab. All of the code, schematics, PCB files, and 3D models are published on GitHub under the GPL-3.0 license, so anyone wanting to build their own version of the badge has everything needed to do so.

## Make your own

The GitHub repository at github.com/robbinsrush/Team4698Badge contains the firmware sketch, EasyEDA schematic and PCB source, and 3D models. The README documents the bill of materials: a Wemos D1 Mini, two 32mm x 32mm common-cathode 8x8 LED matrices (1088AS), two MAX7219 driver ICs (DIP-24), four 6x6mm pushbuttons, a handful of passive components, and — for battery operation — an 18650 cell with a charge/protect/boost circuit.
