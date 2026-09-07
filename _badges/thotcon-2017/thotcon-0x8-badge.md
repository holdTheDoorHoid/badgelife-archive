---
title: ThotCon 0x8 Badge
id: thotcon-2017-thotcon-0x8-badge
layout: badge
parent: Thotcon 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: thotcon-2017
year: 2017
makers:
- name: Workshop 88
  url: null
  role: 'hardware/production (hackerspace)'
- name: Jedha
  url: null
  role: designer
- name: John Wallis
  url: null
  role: firmware programmer
summary: The official electronic badge for ThotCon 0x8 (2017) in Chicago, an ATmega32u4 board that runs "tesserHack," a maze game navigated with three potentiometers and shown on four RGB LEDs and a USB serial console.
functions: 'Stock firmware runs tesserHack, a maze puzzle set in an 8x8x8 cube. Three potentiometers set your X/Y/Z position in the maze; the four NeoPixel LEDs show open pathways (white), portals between layers (purple), and keys to collect (orange), with all LEDs flashing red if you hit a wall. A USB serial console (9600 8-N-1) exposes a "tesserHack" text menu with a map view and help screen for the same maze.'
look:
  colors:
  - black
  - white
  shape: rectangle
  themes:
  - puzzle
  - retro computer
  - meme
tech:
  mcu: ATmega32u4
  leds:
    count: 4
    type: NeoPixel (WS2812B-style RGB)
    note: Used to render maze pathways/portals/keys and a red "you're dead" flash.
  display: none
  connectivity:
  - usb
  inputs:
  - potentiometer
  - buttons
  battery: 2x CR2032
  sao_version: none
  sao_ports: 0
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed as the official electronic badge to ThotCon 0x8 (2017) attendees in Chicago.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/poplicola/shibboleth
  eda_tool: null
links:
- label: hackaday.io/project/21797-thotcon-0x8-badge
  url: https://hackaday.io/project/21797-thotcon-0x8-badge
  kind: hackaday
- label: 'Hackaday: Hacking The ThotCon 0x8 Badge'
  url: https://hackaday.com/2017/05/10/hacking-the-thotcon-0x8-badge/
  kind: article
- label: 'Stock badge firmware source (poplicola/shibboleth)'
  url: https://github.com/poplicola/shibboleth
  kind: repo
images:
- file: assets/images/badges/thotcon-2017/thotcon-0x8-badge/a679dcf395.jpg
  source: "https://hackaday.io/project/21797-thotcon-0x8-badge"
  credit: "Gigawatts (Hackaday.io)"
  caption: "Back of the badge PCB, showing the ATmega32u4, dual CR2032 holders, boot button, micro USB port, and the 'Designed on Jedha / Programmed by John Wallis' silkscreen."
- file: assets/images/badges/thotcon-2017/thotcon-0x8-badge/3b6f72de2f.jpg
  source: "https://hackaday.io/project/21797-thotcon-0x8-badge"
  credit: "Gigawatts (Hackaday.io)"
  caption: "Front of the badge lit up, showing the four RGB NeoPixel LEDs, the three navigation potentiometers, and the 'THOTCON 2017' silkscreen."
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/21797-thotcon-0x8-badge
  title: ThotCon 0x8 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''ThotCon 0x8''.'
- kind: url
  url: https://hackaday.io/project/21797-thotcon-0x8-badge
  title: ThotCon 0x8 Badge (Gigawatts, Hackaday.io)
  accessed: '2026-09-07'
  note: 'Third-party review/writeup (not the maker''s own page) confirming maker (Workshop 88), MCU, LEDs, pots, USB, batteries, maze game mechanics, and serial console details; source of both saved images.'
- kind: url
  url: https://hackaday.com/2017/05/10/hacking-the-thotcon-0x8-badge/
  title: 'Hacking The ThotCon 0x8 Badge'
  accessed: '2026-09-07'
  note: 'Names the individual designer (Jedha) and firmware programmer (John Wallis) of Workshop 88, and confirms the badge is ThotCon''s Chicago con badge.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Both sources are third-party (a Hackaday.io reviewer and the Hackaday.com blog), not the maker''s own project page, so confidence is medium rather than high. Price and quantity made are not stated anywhere found. The firmware repo linked from the project page (github.com/poplicola/shibboleth) returned 404 on 2026-09-07, so it may have been renamed, made private, or deleted; listed as-is per the source but likely dead. No PCB/hardware design files (schematic, Gerbers) were found published, hence open_source: partial. Event was already correctly thotcon-2017; no correction needed.'
last_modified_date: '2026-09-07'
---

The ThotCon 0x8 badge was the official electronic conference badge for ThotCon 8 (2017) in Chicago, built around an ATmega32u4 (the same microcontroller used in the Arduino Leonardo) by members of the Workshop 88 hackerspace. According to Hackaday's coverage, it was designed by Jedha and programmed by John Wallis. The board carries four RGB NeoPixel LEDs, three potentiometers, a micro USB port, and two CR2032 coin cell holders, and its silkscreen leans into retro-computing in-jokes ("SYS 64738", "ALL YOUR HAX ARE BELONG TO US") alongside a cryptic date ("November 22.1987") that goes unexplained in the sources found.

Stock firmware turns the badge into "tesserHack," a maze puzzle navigated through an 8x8x8 cube: the three potentiometers control the player's Z, X, and Y position, and the four LEDs indicate open pathways (white), inter-layer portals (purple), and collectible keys (orange), flashing red on a wall collision. A USB serial console at 9600 baud offers a text-based map view and help menu as a second way to play. A Hackaday.io writeup (by "Gigawatts") also documents re-flashing the badge with custom Arduino code, which requires first burning an Arduino bootloader over the ICSP header with an external AVR programmer, since the badge as shipped does not boot into one on its own.

No price or production quantity was found in the sources checked, and no hardware design files (schematic/Gerbers) were located; a firmware repository was linked from the project page but no longer resolves as of this check.
