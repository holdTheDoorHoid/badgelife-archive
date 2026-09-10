---
title: TFHT - Alien Head Mini-Badge
id: saintcon-2017-tfht-alien-head-mini-badge
layout: badge
parent: Saintcon 2017
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2017
year: 2017
makers:
- name: Sodium-Hydrogen
summary: 'A SAINTCON 2017 "Tin Foil Hat Talks" (TFHT) minibadge built around an ATtiny85: it ships as a small unpopulated/passive board that the owner modifies themselves by cutting traces and bridging solder jumpers, then programs with their own Arduino firmware.'
functions: 'Programmable via the Arduino IDE. To use it, the owner cuts the trace between the pads of solder jumper SJ1, bridges SJ1 and SJ2 the other way, solders on an SMD ATtiny85, then flashes it (via an 8-pin SMD programming clip and an AVR programmer or Arduino-as-ISP) with the included "awaken.ino" sketch to "Awaken the Alien."'
look:
  colors:
  - black
  shape: null
  themes:
  - sci-fi
  - space
tech:
  mcu: ATtiny85
  leds:
    count: 1
    type: null
    note: 'One small SMD LED is visible next to the ATtiny85 in the maker''s own modification photos; color/part not stated.'
  display: none
  connectivity: []
  battery: null
  sao_version: null
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
  firmware_url: https://github.com/Sodium-Hydrogen/SaintCon2017-TFHT-Mini-Badge/blob/master/awaken.ino
  eda_tool: null
links:
- label: github.com/Sodium-Hydrogen/SaintCon2017-TFHT-Mini-Badge
  url: https://github.com/Sodium-Hydrogen/SaintCon2017-TFHT-Mini-Badge
  kind: repo
images:
  - file: assets/images/badges/saintcon-2017/tfht-alien-head-mini-badge/80ca57c846.png
    source: "https://github.com/Sodium-Hydrogen/SaintCon2017-TFHT-Mini-Badge"
    credit: "Sodium-Hydrogen"
    caption: "PCB showing SJ1/SJ2 solder-jumper trace modification for ATtiny85 programming"
contact: {}
notes:
- Official SAINTCON 2017 'Tin Foil Hat Talks' alien-head minibadge with firmware to 'Awaken the Alien', by Sodium-Hydrogen. Found by the event-year sweep, task saintcon-2017.
- 'The discovery sweep''s notes line called this an "alien-head" minibadge; the repo''s own title and README use the same "Awaken the Alien" theme, but no source seen confirms the board''s silkscreen is literally shaped like an alien head (the maker''s photos show a rectangular board with an "A"/pi-symbol logo). Title kept as-is since it matches the repo name.'
status: released
sources:
- kind: url
  url: https://github.com/Sodium-Hydrogen/SaintCon2017-TFHT-Mini-Badge
  title: TFHT - Alien Head Mini-Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2017); event read as ''saintcon-2017''.'
- kind: url
  url: https://github.com/Sodium-Hydrogen/SaintCon2017-TFHT-Mini-Badge
  title: 'SaintCon2017-TFHT-Mini-Badge README'
  accessed: '2026-09-10'
  note: 'Confirmed ATtiny85 MCU, Arduino-based firmware workflow, solder-jumper trace-cut/bridge modification, and repo contents (README, awaken.ino, imgs/).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Maker''s own GitHub repo confirms the badge, its ATtiny85 MCU, and the Arduino firmware workflow. No price, quantity made, availability, LED color/part, PCB shape, or separate hardware/Gerber files were found — the repo publishes only firmware (awaken.ino) and instructional photos, not schematics or board files, so open_source is marked partial rather than yes. No maker storefront, Hackaday post, or press coverage was found; a targeted search for "TFHT alien head" and "Sodium-Hydrogen SAINTCON" turned up only the same GitHub repo.'
last_modified_date: '2026-09-10'
---

TFHT - Alien Head Mini-Badge is a SAINTCON 2017 minibadge released by the maker Sodium-Hydrogen for the "Tin Foil Hat Talks" track, built around an ATtiny85 microcontroller. Rather than shipping fully built, it is distributed in a state that requires the owner to modify it: cutting a trace between the pads of solder jumper SJ1, bridging SJ1 and SJ2 the other way with solder, then soldering on the SMD ATtiny85 chip themselves.

Once modified, the badge is flashed like an Arduino. The maker's GitHub repository walks through installing the ATtiny board definitions in the Arduino IDE, flashing the ATtiny85 bootloader with an AVR programmer or an Arduino wired as an in-system programmer, and finally uploading the included "awaken.ino" sketch — described as the way to "Awaken the Alien" — using an 8-pin SMD programming clip to reach the chip's pins.

## Make your own

The repository (github.com/Sodium-Hydrogen/SaintCon2017-TFHT-Mini-Badge) publishes the Arduino firmware (`awaken.ino`) and step-by-step photos of the trace-cut/bridge modification, but no schematic, PCB layout, or Gerber files were found in it — so replicating the board itself is not currently possible from what is published, only reprogramming an existing one. To build on it: install the `damellis/attiny` board package in the Arduino IDE, select "ATtiny24/45/85" with an ATtiny85 processor and internal 8 MHz clock, flash the bootloader with a suitable programmer, perform the SJ1/SJ2 trace modification shown in the repo's photos, solder on an ATtiny85, and upload the sketch.

