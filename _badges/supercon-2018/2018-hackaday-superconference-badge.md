---
title: 2018 Hackaday Superconference Badge
id: supercon-2018-2018-hackaday-superconference-badge
layout: badge
parent: Supercon 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2018
year: 2018
makers:
- name: Voja Antonic
  url: https://hackaday.io/voja-antonic
  role: hardware design
- name: Jaromir Sukuba
  role: firmware
- name: Mike Szczys
  url: https://hackaday.io/mike-szczys
- name: phase2682
  url: https://hackaday.io/phase2682
- name: Tina Belmont
- name: Dusan Petrovic
- name: Roger
summary: A palm-sized, battery-powered retrocomputer badge for the 2018 Hackaday Superconference, with a mini mechanical keyboard, color TFT, and a built-in BASIC/CP&#47;M programming environment.
functions: 'Runs a BASIC interpreter (based on uBASIC) for on-badge programming, and emulates CP/M on a Z80 emulator for classic games. Includes 3-voice audio, serial comms between badges/computers, and RGB LED blinky effects.'
look:
  colors: []
  shape: rectangle
  themes:
  - retro computer
  - learn to solder
  - village badge
tech:
  mcu: PIC32MX370F512H
  leds: null
  display: 320x240 TFT LCD
  connectivity:
  - uart
  battery: 2x AA
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to all ticketed attendees of the 2018 Hackaday Superconference (Pasadena, CA, Nov 2-4, 2018)
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/Hack-a-Day/2018-Supercon-Badge
  firmware_url: https://github.com/Hack-a-Day/2018-Supercon-Badge
  eda_tool: null
links:
- label: hackaday.io/project/161859-2018-hackaday-superconference-badge
  url: https://hackaday.io/project/161859-2018-hackaday-superconference-badge
  kind: hackaday
- label: github.com/Hack-a-Day/2018-Supercon-Badge
  url: https://github.com/Hack-a-Day/2018-Supercon-Badge
  kind: repo
images:
- file: assets/images/badges/supercon-2018/2018-hackaday-superconference-badge/b6b3a78466.jpg
  source: "https://hackaday.io/project/161859-2018-hackaday-superconference-badge"
  credit: "Voja Antonic / Hackaday"
  caption: "The 2018 Hackaday Superconference badge, a PIC32-based retro-computing wearable"
contact: {}
notes:
- 'Sheet had event listed as "Supercon 2018"; confirmed matches the archive event id supercon-2018.'
status: released
sources:
- kind: url
  url: https://hackaday.io/project/161859-2018-hackaday-superconference-badge
  title: 2018 Hackaday Superconference Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''Supercon 2018''.'
- kind: url
  url: https://hackaday.io/project/161859-2018-hackaday-superconference-badge
  title: 2018 Hackaday Superconference Badge (project page)
  accessed: '2026-09-07'
  note: Confirmed maker team, MCU (PIC32MX370F512H), TFT display, keyboard, AA battery power, event/year, and free distribution to attendees.
- kind: url
  url: https://github.com/Hack-a-Day/2018-Supercon-Badge
  title: Hack-a-Day/2018-Supercon-Badge on GitHub
  accessed: '2026-09-07'
  note: Confirmed open-source hardware/firmware (MIT license), BASIC and CP/M-on-Z80-emulator functionality, 3-voice audio, serial comms between badges.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'LED count/type not stated anywhere found (badge has RGB LEDs per the Hackaday.io summary but exact count/part number not confirmed in sources read, left null). Exact quantity made not found (all Superconference 2018 ticket holders received one; ticket count not sourced). Price is $0/free since it was a conference giveaway, not sold. Enclosure/bezel design is a separate related Hackaday.io project (162134) not folded into this entry.'
last_modified_date: '2026-09-07'
---

The 2018 Hackaday Superconference badge is a standalone, battery-powered retrocomputer built to fit in the palm of your hand, given free to every ticketed attendee of the 2018 Hackaday Superconference in Pasadena, California (November 2-4, 2018). Designed by Voja Antonic with firmware by Jaromir Sukuba, and built with contributions from Mike Szczys, phase2682, Tina Belmont, Dusan Petrovic, and Roger, it pairs a mini mechanical keyboard with a 320x240 color TFT LCD, running off two AA batteries for tens of hours of use.

Rather than being a simple blinky badge, it doubles as a tiny computer: a BASIC interpreter (adapted from the uBASIC project) lets attendees write and run programs directly on the badge, and a built-in Z80 emulator runs CP/M so it can play classic text-based games. It also has 3-voice audio, serial communication between badges (and to a host computer), and an expansion header for "Shitty Add-Ons."

## Make your own

Hardware and firmware are fully open source (MIT license) at github.com/Hack-a-Day/2018-Supercon-Badge, which includes schematics, PCB files, and the BASIC/CP&#47;M firmware. The project's Hackaday.io page also links a bill of materials and a separately-designed laser-cut enclosure project.
