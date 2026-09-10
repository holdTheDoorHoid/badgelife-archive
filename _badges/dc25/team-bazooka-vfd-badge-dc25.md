---
title: Team Bazooka VFD Badge (DC25)
id: dc25-team-bazooka-vfd-badge-dc25
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: Team Bazooka
  url: https://github.com/TeamBazooka
summary: A one-off DEF CON 25 badge built around an HD44780-compatible vacuum fluorescent display, an ATmega328P, and an 18650 cell.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - retro computer
tech:
  mcu: ATmega328P
  leds:
    count: 8
    type: WS2812B
    note: ''
  display: VFD (HD44780-compatible character display)
  connectivity: []
  battery: 18650 Li-ion cell
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '1'
  availability: rumored
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/TeamBazooka/DC25/tree/master/hardware
  firmware_url: https://github.com/TeamBazooka/DC25/tree/master/firmware
  eda_tool: KiCad
links:
- label: github.com/TeamBazooka/DC25
  url: https://github.com/TeamBazooka/DC25
  kind: repo
- label: "Hackaday: All The Hardware Badges Of DEF CON 25 – Team Bazooka VFD Badge"
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/team-bazooka-vfd-badge/
  kind: article
images:
  - file: assets/images/badges/dc25/team-bazooka-vfd-badge-dc25/6800f58f3a.jpg
    source: "https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/team-bazooka-vfd-badge/"
    credit: "Hackaday / Mike Szczys"
    caption: "Front of the Team Bazooka VFD badge, showing the vacuum fluorescent display"
  - file: assets/images/badges/dc25/team-bazooka-vfd-badge-dc25/4db37d32e3.jpg
    source: "https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/team-bazooka-vfd-badge-back-shows-18650/"
    credit: "Hackaday / Mike Szczys"
    caption: "Back of the badge, showing the 18650 cell battery holder"
contact: {}
notes:
- Sweep's original note called it "ultra-rare (reportedly one unit)... built for DEF CON 25 around an ATmega and 18650 cell"; that line is now confirmed by Hackaday's DEF CON 25 badge roundup, which independently describes it as "an ultra-rare badge -- so far there's only one."
status: rumored
sources:
- kind: url
  url: https://github.com/TeamBazooka/DC25
  title: Team Bazooka VFD Badge (DC25)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc25-saos); event read as ''dc25''.'
- kind: url
  url: https://github.com/TeamBazooka/DC25
  title: TeamBazooka/DC25 repository (KiCad hardware + Arduino firmware)
  accessed: '2026-09-10'
  note: 'No README; confirmed via schematic (DC25.sch) and library (DC25.lib) contents: VFD component, ATMEGA328P-AU, 18650 battery cell, 8x WS2812B LEDs. firmware/platformio.ini targets an Arduino Nano (atmega328) with LiquidCrystal library, consistent with an HD44780-protocol VFD.'
- kind: url
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/team-bazooka-vfd-badge/
  title: "All The Hardware Badges Of DEF CON 25 – Team Bazooka VFD Badge"
  accessed: '2026-09-10'
  note: 'Confirms the badge is real (not just a search snippet), describes it as the only DEF CON 25 badge with a vacuum fluorescent display, HD44780-compatible, ATmega-based, 18650-powered, and states only one unit existed as of the article.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: >-
    Existence and core specs confirmed by an independent Hackaday article plus the maker's own
    KiCad/Arduino source files, so this is upgraded from a bare search-snippet stub. Left rumored/low-
    quantity because Hackaday itself calls it a one-off and no storefront, price, or distribution
    method was ever found -- it reads as a personal build shown off at the con rather than something
    handed out or sold. functions, look.colors/shape, get_one.price, and contact are still empty:
    no source described what the display actually showed or gave the badge's shape/color scheme
    beyond "black PCB with a VFD tube," and no maker contact info was published anywhere found.
    firmware.ino in the repo is an empty placeholder file, so firmware_url points at the folder
    rather than a working sketch.
last_modified_date: '2026-09-10'
---

Team Bazooka's DEF CON 25 badge is a hand-built one-off notable for using a vacuum fluorescent
display (VFD) instead of the LCD or OLED panels common on badges of that era. Hackaday's roundup
of DEF CON 25 hardware badges singled it out as "the only badge with a Vacuum Fluorescent Display
on it," running an HD44780-compatible character display driven by an ATmega328P and powered from
a single 18650 lithium-ion cell, with eight WS2812B addressable LEDs for additional lighting.

The team published KiCad schematics and PCB files along with an Arduino/PlatformIO firmware
project on GitHub, though the firmware repository's main sketch file is an empty placeholder --
only the hardware design appears to have been finished and shared in usable form. Hackaday
described the badge as "ultra-rare... so far there's only one," and no evidence turned up of it
being sold, kitted, or given away beyond that single unit shown at the con.

## Make your own

KiCad schematic and PCB source live under `hardware/` in the [TeamBazooka/DC25 repo](https://github.com/TeamBazooka/DC25/tree/master/hardware),
including a custom VFD symbol and WS2812B footprint. A PlatformIO project targeting an Arduino
Nano (ATmega328) is under `firmware/`, but its `firmware.ino` is empty, so the firmware as
published is not a working build -- treat the hardware files as the useful part.
