---
title: AND!XOR DC27 Badge
id: dc27-and-xor-badge-year-unspecified
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: AND!XOR (Zapp, Andrew, Hyr0n, and team)
  url: https://hackaday.io/project/164346-andxor-dc27-badge
summary: A hackable open-source badge for DEF CON 27 (2019) built around a Fallout-style gas-mask hoodie character, with two arcs of RGB light-pipe "bling," a Bluetooth mesh network the team called BOTNET, and an embedded text-adventure/CTF called B.E.N.D.E.R.
functions: RGB LED matrix with glow-in-the-dark capacitive touch sensing; Bluetooth mesh ("BOTNET") for remote command execution between badges; B.E.N.D.E.R. (Badge Enabled Non Directive Enigma Routine) text-adventure with embedded security challenges; CTF leaderboard integration via proxy nodes; breakout pins for hardware hacking.
look:
  colors:
  - black
  - multicolor
  shape: null
  themes:
  - robot
  - sci-fi
  - cyberpunk
  - security
  - ctf
  - wearable
tech:
  mcu: Rigado BMD-340 (nRF52840 core)
  leds:
    count: null
    type: RGB
    note: IS31FL3741 LED controller driving RGB LEDs (HQ19-2333RGBC) behind light-pipe arcs
  display: none
  connectivity:
  - bluetooth
  - uart
  - usb
  battery: Keystone 2460 cell, adjustable LDO/boost regulation
  sao_version: v1.69bis
get_one:
  price: free
  price_usd: 0
  quantity: '600'
  availability: sold_out
  distribution:
  - free_drop
  where: Given away free at DEF CON 27 (Las Vegas, Aug 8-11, 2019) through sponsorship
make_your_own:
  open_source: true
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: podcasts.apple.com/us/podcast/s1-episode-009-badgelife-ft-and-xor/id1605313494?i=1000565459682
  url: https://podcasts.apple.com/us/podcast/s1-episode-009-badgelife-ft-and-xor/id1605313494?i=1000565459682
  kind: website
- label: AND!XOR DC27 Badge (Hackaday.io project page)
  url: https://hackaday.io/project/164346-andxor-dc27-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260517132807/https://hackaday.io/project/164346-andxor-dc27-badge
- label: AND!XOR badge listed on DEF CON forums
  url: https://forum.defcon.org/node/229672
  kind: article
images:
- file: assets/images/badges/dc27/and-xor-badge-year-unspecified/5d7167109e.jpg
  source: https://hackaday.io/project/164346-andxor-dc27-badge
  credit: AND!XOR
  caption: AND!XOR DC27 badge, front
  archived: https://web.archive.org/web/20260517132807/https://hackaday.io/project/164346-andxor-dc27-badge
contact: {}
notes:
- Sheet/original source was a Cyber Distortion podcast episode interviewing AND!XOR generally, without naming a specific badge; the Hackaday.io project "AND!XOR DC27 Badge" (project 164346) matches the entry's existing event/year (dc27, 2019) and supplied the concrete details filled in here.
- AND!XOR's current GitHub org (github.com/ANDnXOR) lists badge repos for DC24, DC28, DC31, DC32, DC33 but no DC27-specific hardware/firmware repo was found there; Hackaday.io describes the DC27 badge as fully open-source hardware and firmware, but no working repo link could be confirmed, so hardware_url/firmware_url are left empty.
- LED count not stated in sources found; left null.
status: released
sources:
- kind: url
  url: https://podcasts.apple.com/us/podcast/s1-episode-009-badgelife-ft-and-xor/id1605313494?i=1000565459682
  title: AND!XOR badge (year unspecified)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: video-podcast); event read as ''DEF CON / #badgelife culture generally''.'
- kind: url
  url: https://hackaday.io/project/164346-andxor-dc27-badge
  title: AND!XOR DC27 Badge | Hackaday.io
  accessed: '2026-09-07'
  note: 'Primary source: makers, event/year, features, MCU, LED controller, touch IC, SAO version, battery, quantity (600), free distribution, open-source claim, badge photo.'
  archived: https://web.archive.org/web/20260517132807/https://hackaday.io/project/164346-andxor-dc27-badge
- kind: url
  url: https://forum.defcon.org/node/229672
  title: 'AND!XOR Badge, HackADay: Mike Szczys: DEF CON 27 - DEF CON Forums'
  accessed: '2026-09-07'
  note: Corroborates the DC27 event identification (link fetch failed with a connection error, so used only as a supporting search-result citation, not read directly).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (maker, event/year, MCU, features, SAO version, quantity, free distribution) come from the maker's own Hackaday.io project page. Could not confirm a live GitHub repo for DC27 hardware/firmware, exact LED count, or a specific price beyond "free" and quantity source language ("distributed free... through philanthropic sponsorship"). The DEF CON forum thread reference could not be fetched directly (connection reset) so is cited as a supporting mention only.
last_modified_date: '2026-09-07'
---

AND!XOR built this badge for DEF CON 27 in Las Vegas (August 2019) as a hackable, open-source dev-board-style wearable, continuing their yearly tradition of elaborate conference badges. The design departs from the team's earlier aesthetic with a Fallout-inspired gas-mask, hoodie-wearing character, set off by two arcs of light-pipe material that glow with RGB color driven by an IS31FL3741 controller. Underneath, an nRF52840-based Rigado BMD-340 module runs the show, alongside an FT2232H USB-UART bridge/debugger and an IQS333 capacitive touch controller for glow-in-the-dark touch sensing.

Beyond blinking lights, the badge doubled as a game platform: an embedded text-adventure and puzzle challenge called B.E.N.D.E.R. (Badge Enabled Non Directive Enigma Routine), a CTF leaderboard reachable through proxy nodes, and a Bluetooth mesh network nicknamed BOTNET that let badges issue commands to each other across the conference floor. It carries a SAO 1.69bis header for add-ons, including AND!XOR's own DOOM-themed SAO sold separately as a fundraiser.

Around 600 units were manufactured and given away free at DEF CON 27, underwritten by sponsors including Urbane Security, Macrofab, Mouser Electronics, and Rigado. AND!XOR describes the hardware and firmware as fully open source, though a working GitHub link to the DC27-specific repository could not be located during this research pass; their organization page instead hosts badge projects for other years.
