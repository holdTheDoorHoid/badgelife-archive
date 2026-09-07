---
title: SAINTCON 2018 badge (compukidmike)
id: saintcon-2018-saintcon-2018-badge-compukidmike
layout: badge
parent: Saintcon 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: saintcon-2018
year: 2018
makers:
- name: compukidmike
summary: The official SAINTCON 2018 conference badge, built around a LOLIN D32 (ESP32) board running MicroPython, with an 8x32 LED matrix display and 12 minibadge (SAO-style) header spots.
functions: 'Cycles through display modes (SAINTCON logo, a custom message, Hacker Challenge score, Hacker Challenge ID) via UP/DOWN buttons; a SELECT menu offers brightness control, wifi status, and a wifi config mode that spins up an access point for setting the network and custom message from a phone or computer. Twelve minibadge headers accept community-made minibadges.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - village badge
tech:
  mcu: ESP32 (LOLIN D32)
  leds:
    count: 256
    type: LED matrix
    note: 8x32 LED matrix display
  display: LED matrix 8x8
  connectivity:
  - wifi
  battery: rechargeable LiPo, charged via microUSB
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to SAINTCON 2018 attendees as the conference badge.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/compukidmike/Saintcon2018/tree/master/Badge/Hardware%20Files
  firmware_url: https://github.com/compukidmike/Saintcon2018/tree/master/Badge/Badge%20Source%20Code
  eda_tool: KiCad
links:
- label: github.com/compukidmike/Saintcon2018
  url: https://github.com/compukidmike/Saintcon2018
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- 'The GitHub repo README describes this as a documentation/support repo ("all the info you need about the 2018 Saintcon badge") rather than an announcement page; it was not possible to confirm from the repo alone whether compukidmike designed the badge or is a SAINTCON badge-team member sharing build/flash instructions and hardware files on the team''s behalf. Treating "compukidmike" as the maker credit per the repo ownership, per the archive''s existing convention for this entry.'
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/Saintcon2018
  title: SAINTCON 2018 badge (compukidmike)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''saintcon-2018''.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2018/master/Badge/Readme.md
  title: 'Badge/Readme.md - About the Badge'
  accessed: '2026-09-07'
  note: Source for chip (ESP32/LOLIN D32, MicroPython), 8x32 LED matrix, 3 buttons, 12 minibadge spots, rechargeable battery/microUSB charging, wifi config flow, and menu/display functions.
- kind: url
  url: https://github.com/compukidmike/Saintcon2018/tree/master/Badge/Hardware%20Files
  title: Badge/Hardware Files directory listing
  accessed: '2026-09-07'
  note: Confirms published Gerbers, KiCad source, schematic PDF and assembly BOM alongside the firmware binary and MicroPython source, supporting open_source yes and eda_tool KiCad.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core specs (ESP32/LOLIN D32, MicroPython, 8x32 LED matrix, 3 buttons, 12 minibadge headers, LiPo battery/microUSB) and open-source hardware/firmware confirmed directly from the maker''s own repo. Not found anywhere in the repo: price, quantity made, PCB color, board shape/outline, and whether compukidmike personally designed the badge versus documenting/distributing files for the official SAINTCON badge team. No usable photo of the assembled hardware was found in the repo (only unrelated animated GIFs used by the badge''s own web UI); the BadgeBuildSheet.pdf likely contains assembly photos but was not parsed for images.'
last_modified_date: '2026-09-07'
---

The SAINTCON 2018 badge was the official conference badge for SAINTCON (Utah's security conference) that year, built around a LOLIN D32 board (ESP32) running MicroPython. It carries an 8x32 LED matrix display, three navigation buttons (UP, DOWN, SELECT), a rechargeable LiPo battery charged over microUSB, and twelve headers for attaching community-made minibadges — SAINTCON's long-running take on the SAO concept, distinct in size and count from the more common 2-pin/6-pin SAO standard.

On power-up the badge cycles through display screens (the SAINTCON logo, a custom message, and Hacker Challenge score/ID for the conference's CTF-style challenge), with a SELECT-button menu for brightness, wifi status, and a wifi configuration mode that opens an access point so attendees can set their network and custom message from a phone or laptop. The GitHub repository, maintained by user compukidmike, published everything needed to build, flash, and modify one: a build sheet PDF, full KiCad hardware files and Gerbers, a schematic and BOM, the MicroPython firmware source, and a precompiled firmware binary flashable with esptool — making it fully open source on both the hardware and firmware sides.

It is unclear from the repository alone whether compukidmike was the badge's designer or a SAINTCON badge-team member distributing the official build materials; the repo reads as reference documentation for badge holders ("here's all the info you need about the 2018 Saintcon badge") rather than a personal project announcement.
