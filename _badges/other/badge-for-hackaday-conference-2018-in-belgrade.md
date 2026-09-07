---
title: Badge for Hackaday Conference 2018 in Belgrade
id: other-badge-for-hackaday-conference-2018-in-belgrade
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: Voja Antonic
  url: https://hackaday.io/voja-antonic
summary: 'A standalone retro-computer badge given to attendees of Hackaday Belgrade 2018, with a color LCD, a full mechanical keyboard, and a BASIC/CP-M software stack.'
functions: 'Runs a BASIC interpreter (based on and expanded from the uBASIC project) and a Z80 CP/M emulation environment; plays 3-voice polyphonic music through an onboard speaker; talks badge-to-badge or badge-to-computer over a 3.3V serial UART on its expansion header.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - learn to solder
tech:
  mcu: PIC32MX370F512H
  leds: null
  display: 320x240 RGB TFT LCD
  connectivity:
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: 'Given to all ticketed attendees of Hackaday Belgrade 2018 as their conference badge; a limited number of extras may have been offered for purchase afterward, per the project page.'
make_your_own:
  open_source: yes
  hardware_url: https://hackaday.io/project/80627-badge-for-hackaday-conference-2018-in-belgrade
  firmware_url: https://github.com/Hack-a-Day/basic-badge
  eda_tool: null
links:
- label: hackaday.io/project/80627-badge-for-hackaday-conference-2018-in-belgrade
  url: https://hackaday.io/project/80627-badge-for-hackaday-conference-2018-in-belgrade
  kind: hackaday
- label: Hack-a-Day/basic-badge (firmware repo)
  url: https://github.com/Hack-a-Day/basic-badge
  kind: repo
images:
  - file: assets/images/badges/other/badge-for-hackaday-conference-2018-in-belgrade/143408fa8c.jpg
    source: "https://hackaday.io/project/80627-badge-for-hackaday-conference-2018-in-belgrade"
    credit: "Voja Antonic"
    caption: "The Hackaday Belgrade 2018 conference badge"
  - file: assets/images/badges/other/badge-for-hackaday-conference-2018-in-belgrade/b905cf9207.jpg
    source: "https://hackaday.io/project/80627-badge-for-hackaday-conference-2018-in-belgrade"
    credit: "Voja Antonic"
    caption: "Badge PCB detail, Hackaday Belgrade 2018"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/80627-badge-for-hackaday-conference-2018-in-belgrade
  title: Badge for Hackaday Conference 2018 in Belgrade
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''Hackaday Belgrade 2018''.'
- kind: url
  url: https://hackaday.io/project/80627-badge-for-hackaday-conference-2018-in-belgrade
  title: Badge for Hackaday Conference 2018 in Belgrade
  accessed: '2026-09-07'
  note: 'Confirmed maker (Voja Antonic, with ~9 project contributors), event (Hackaday Belgrade, held May 26, 2018), hardware (PIC32MX370F512H, 320x240 TFT, 55-key mechanical keyboard, speaker, RGB LED, UART expansion header), firmware (BASIC interpreter + Z80 CP/M emulation, MIT licensed), design file availability (Gerbers + Circuit Studio PCB files, firmware on GitHub), and distribution (given to all ticketed attendees).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Event corrected: this "other" entry is for Hackaday Belgrade 2018, a one-off European
    Hackaday conference. No matching id exists in _data/events.yml (which only lists
    Hackaday Superconference/Supercon USA years and Hackaday Europe 2025/2026), so event
    is left as "other" with the specific con named here. Confidence is medium: the
    project page itself is thorough and appears to be the maker's own writeup, but no
    independent third-party source (press coverage, forum posts) was checked to
    corroborate quantity made or LED count/type, which the page did not state explicitly
    beyond "RGB LED" (count/part number not given, so tech.leds left null). No price is
    listed since it was distributed free with conference admission; get_one.price left
    empty rather than guessed.
last_modified_date: '2026-09-07'
---

The Hackaday Belgrade 2018 badge, led by Voja Antonic with roughly nine other contributors, was less a conference badge than a complete pocket computer. Every ticketed attendee at the May 26, 2018 event in Belgrade received one. Built around a PIC32MX370F512H microcontroller with 512KB of program memory, 128KB of data memory, and 2MB of external flash, it drives a 320x240 color TFT LCD and a full 55-key mechanical keyboard, making it usable as a standalone machine rather than just an LED blinker.

On the software side, the badge shipped with a BASIC interpreter expanded from the uBASIC project and a Z80 CP/M emulation environment, plus a 3-voice polyphonic music synth played through an onboard speaker. A 3.3V-level serial UART on its expansion header let badges talk to each other or to a computer. The firmware was released under the MIT license.

## Make your own

Gerber files for the badge's PCB panel (three boards per panel) and the Circuit Studio PCB source are available from the project's Hackaday.io page, and the firmware lives in the Hack-a-Day/basic-badge GitHub repository, which also documents the BASIC dialect, the music synthesis code, serial communications, the C toolchain setup, and how to run CP/M on the hardware.
