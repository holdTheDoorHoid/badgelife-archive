---
title: HITB+CyberWeek 2021 Packet Hack Badge
id: hitb-2021-hitb-cyberweek-2021-packet-hack-badge
layout: badge
parent: HITB 2021
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hitb-2021
year: 2021
makers:
- name: TweetsFromPanda
  role: badge design
- name: lanrat
  role: firmware / flashing script
summary: A village badge for the Packet Hack Village at HITB+CyberWeek 2021 in Abu Dhabi, with an OLED display and binary-entry keys for a CTF challenge.
functions: 'Displays a flashed username/handle and custom bitmap logos on its OLED. A CTF mode entered via the S1 switch accepts binary-coded input on the right-side keys. Reprogrammable over UART/ISP with a per-attendee username flashing script.'
look:
  colors: []
  shape: null
  themes:
  - ctf
  - village badge
  - security
tech:
  mcu: AVR
  leds: null
  display: OLED
  connectivity:
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed at the Packet Hack Village, HITB+CyberWeek 2021, Abu Dhabi (Nov 21-25, 2021).
make_your_own:
  open_source: yes
  hardware_url: null
  firmware_url: https://github.com/lanrat/PacketHackVillageHitBBadge2021
  eda_tool: null
links:
- label: badge.gallery/series/hitb
  url: https://badge.gallery/series/hitb
  kind: website
- label: 'Hackster: The Packet Hack Badge'
  url: https://www.hackster.io/433948/the-packet-hack-badge-fc54cc
  kind: hackaday
- label: 'GitHub: PacketHackVillageHitBBadge2021'
  url: https://github.com/lanrat/PacketHackVillageHitBBadge2021
  kind: repo
- label: 'HITB news: HITB+CyberWeek brought back to Abu Dhabi'
  url: https://news.hitb.org/content/hack-box-cyberweek-brought-back-abu-dhabi-disruptad
  kind: article
images:
  - file: assets/images/badges/hitb-2021/hitb-cyberweek-2021-packet-hack-badge/cbfe4a52aa.jpg
    source: "https://github.com/lanrat/PacketHackVillageHitBBadge2021"
    credit: "TweetsFromPanda / lanrat"
    caption: "Packet Hack Village badge for HITB+CyberWeek 2021, OLED display and binary-entry keys"
contact: {}
notes:
- AVR/OLED electronic badge for the HITB+CyberWeek 2021 Packet Hack Village, with a CTF binary-input mode. Found by the event-year sweep, task con-troopers.
- The sweep's title matches the maker's naming on badge.gallery; no change needed.
status: released
sources:
- kind: url
  url: https://badge.gallery/series/hitb
  title: HITB+CyberWeek 2021 Packet Hack Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-troopers); event read as ''HITB+CyberWeek 2021''.'
- kind: url
  url: https://www.hackster.io/433948/the-packet-hack-badge-fc54cc
  title: The Packet Hack Badge
  accessed: '2026-09-08'
  note: Maker's Hackster project page; credits Abhinav SP / TweetsFromPanda for the design, describes OLED, S1/S2 controls, binary-entry keys, and CTF mode.
- kind: url
  url: https://github.com/lanrat/PacketHackVillageHitBBadge2021
  title: PacketHackVillageHitBBadge2021
  accessed: '2026-09-08'
  note: Public firmware repo (AVR, avrdude, oled.h) confirming open-source firmware and providing a badge photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed as a real, distributed badge for the Packet Hack Village at HITB+CyberWeek 2021 Abu Dhabi via the maker's Hackster page and firmware repo. Price, quantity made, and PCB colors were not stated in any source found and are left empty. Hardware design files (Gerbers/schematic) were not located, only firmware; open_source is marked "yes" on the strength of the published firmware, but no hardware repo was found. Exact AVR part number not confirmed.
last_modified_date: '2026-09-08'
---

The Packet Hack Badge was made for the Packet Hack Village at HITB+CyberWeek 2021, held in Abu Dhabi that November. It's an AVR-powered wearable with a small OLED display, a set of binary-entry keys on its right edge, and S1/S2 control switches. Attendees could flash their own handle to the display, and a CTF mode - entered via the S1 switch - accepted binary-coded input as part of the village's challenges.

The badge was designed by TweetsFromPanda (credited as Abhinav SP on Hackster), with lanrat contributing firmware refinements including a per-attendee username-flashing script. The firmware, built with AVR tooling and avrdude, is published on GitHub along with custom font and animation libraries and TWI/OLED initialization code; no hardware design files (schematic or Gerbers) were found alongside it.

## Make your own

Firmware source is available at the GitHub repo linked above. It targets an AVR microcontroller and is built and flashed with standard AVR tooling (avrdude); no PCB design files were located.
