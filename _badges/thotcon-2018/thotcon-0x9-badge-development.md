---
title: ThotCon 0x9 Badge
id: thotcon-2018-thotcon-0x9-badge-development
layout: badge
parent: Thotcon 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: thotcon-2018
year: 2018
makers:
- name: Jay Margalus
  url: https://github.com/poplicola
  role: hardware/firmware
- name: Rudy Ristich
  role: hardware/firmware
- name: Workshop88
  role: sponsoring hackerspace
summary: A key-shaped ESP8266 conference badge for ThotCon 0x9, built by Jay Margalus and Rudy Ristich of Workshop88 with DePaul Consulting Group students, running WiFi-connected games and an in-badge currency.
functions: 'A boot sequence with Morse code and binary displays leads into a tic-tac-toe-style menu for Space Invaders and a Pokemon mini-game. Attendees also mined and gambled "ThotCoin," an in-badge currency, and could take part in an external Twitch-Plays-Pokemon-style game controlled from their badges, with in-badge augmentations giving ThotCoin mining multipliers.'
look:
  colors:
  - red
  - black
  shape: key
  themes:
  - retro computer
  - arcade
  - crypto
tech:
  mcu: ESP8266
  leds: null
  display: 0.96" OLED (portrait)
  connectivity:
  - wifi
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '16 prototype boards, hand-soldered'
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/poplicola/Thotcon-0x9/
  firmware_url: https://github.com/poplicola/Thotcon-0x9/
  eda_tool: null
links:
- label: hackaday.io/project/159222-thotcon-0x9-badge-development
  url: https://hackaday.io/project/159222-thotcon-0x9-badge-development
  kind: hackaday
- label: github.com/poplicola/Thotcon-0x9
  url: https://github.com/poplicola/Thotcon-0x9/
  kind: repo
images:
  - file: assets/images/badges/thotcon-2018/thotcon-0x9-badge-development/27d1bdaac9.png
    source: "https://hackaday.io/project/159222-thotcon-0x9-badge-development"
    credit: "Jay Margalus / Workshop88"
    caption: "ThotCon 0x9 badge, key-shaped PCB with OLED display"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/159222-thotcon-0x9-badge-development
  title: ThotCon 0x9 Badge Development
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''ThotCon 0x9''.'
- kind: url
  url: https://hackaday.io/project/159222-thotcon-0x9-badge-development
  title: ThotCon 0x9 Badge Development
  accessed: '2026-09-07'
  note: Maker/team names, ESP8266 chip, OLED display, WiFi, key shape, games (tic-tac-toe menu, Space Invaders, Pokemon), ThotCoin currency, 16 hand-soldered prototypes, Micro-USB port.
- kind: url
  url: https://github.com/poplicola/Thotcon-0x9/
  title: poplicola/Thotcon-0x9
  accessed: '2026-09-07'
  note: Confirms open hardware/firmware repo with BOM (Mouser), schematic PDF, board outline DXF, and .ino firmware for games and ThotCoin currency.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No maker photo of the assembled physical badge was found, only a PCB layout/render from the Hackaday project page; used that as the image. Price, exact quantity distributed to attendees vs. the 16 prototypes, LED info, and battery/power details were not stated in the sources found. Repo does not display an explicit license.'
last_modified_date: '2026-09-07'
---

The ThotCon 0x9 badge was a key-shaped, ESP8266-powered game badge built for ThotCon's 2018 (0x9) conference by Jay Margalus and Rudy Ristich of Workshop88, working with students from the DePaul Consulting Group. Sixteen prototype boards were hand-soldered with an OLED screen, buttons, capacitors, and resistors, and programmed in the Arduino environment using the u8g2 OLED library.

Powering on the badge triggers a boot sequence mixing Morse code and binary readouts before dropping into a tic-tac-toe-styled menu. From there, attendees could play Space Invaders and a Pokemon-themed mini-game, and mine or gamble "ThotCoin," an in-badge currency. The badge also tied into an external, Twitch-Plays-Pokemon-style game that attendees could influence from their badges, with in-badge augmentations acting as mining multipliers for ThotCoin.

## Make your own

Hardware and firmware are published on GitHub (poplicola/Thotcon-0x9), including a bill of materials sourced from Mouser, a schematic PDF, a DXF board outline, and the .ino firmware files implementing the games, currency system, and a device identifier generated via MD5 hashing. A packaged prototype release (`tc0x9_proto_release.zip`) is also linked from the Hackaday project page.
