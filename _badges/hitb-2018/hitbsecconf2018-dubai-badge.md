---
title: HITBSecConf2018 Dubai Badge
id: hitb-2018-hitbsecconf2018-dubai-badge
layout: badge
parent: Hitbsecconf 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hitb-2018
year: 2018
makers:
- name: Shepard Lab
- name: HackersBadge.com
- name: UnicornTeam
  url: https://github.com/UnicornTeam
summary: The official electronic conference badge for HITBSecConf2018 Dubai, showing the talks agenda and running a hunt-style game across the Badge Village.
functions: 'Displays the conference schedule and activity info; game mode where attendees hunt down 12 "badge masters" over LoRa to become "master of all the badges."'
look:
  colors: []
  shape: null
  themes:
  - security
  - village badge
  - game
tech:
  mcu: STM32F103
  leds:
    count: 18
    type: SK6805
    note: ''
  display: 1.44" ST7735S 128x128 TFT
  connectivity:
  - lora
  battery: 2x AAA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of HITBSecConf2018 Dubai (Nov 27-28, 2018) as the conference badge.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/UnicornTeam/hitb2018dubai-badge
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/series/hitb
  url: https://badge.gallery/series/hitb
  kind: website
- label: 'HITB Badge Village – HITBSecConf2018 Dubai'
  url: https://archive.conference.hitb.org/hitbsecconf2018dxb/hitb-badge-village/
  kind: article
- label: UnicornTeam/hitb2018dubai-badge (schematic)
  url: https://github.com/UnicornTeam/hitb2018dubai-badge
  kind: repo
images:
- file: assets/images/badges/hitb-2018/hitbsecconf2018-dubai-badge/af3a8e0a86.jpg
  source: "https://archive.conference.hitb.org/hitbsecconf2018dxb/hitb-badge-village/"
  credit: "Shepard Lab / HackersBadge.com"
  caption: "HITBSecConf2018 Dubai electronic conference badge"
contact: {}
notes:
- Special-edition electronic HITB Dubai 2018 badge with a Badge Village hacking path. Found by the event-year sweep, task con-troopers.
- 'Sweep title matched the maker''s usage; kept as-is.'
status: released
sources:
- kind: url
  url: https://badge.gallery/series/hitb
  title: HITBSecConf2018 Dubai Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-troopers); event read as ''HITBSecConf 2018 Dubai''.'
- kind: url
  url: https://archive.conference.hitb.org/hitbsecconf2018dxb/hitb-badge-village/
  title: 'HITB Badge Village « HITBSecConf2018 - Dubai'
  accessed: '2026-09-08'
  note: 'Official event archive page; confirms badge features, MCU, display, LEDs, LoRa, battery, game mode, and names Shepard Lab and HackersBadge.com as the badge designers.'
- kind: url
  url: https://github.com/UnicornTeam/hitb2018dubai-badge
  title: 'UnicornTeam/hitb2018dubai-badge'
  accessed: '2026-09-08'
  note: 'Repo holds the badge schematic (HITB_DXB_V1.1.sch) and a PDF, confirming UnicornTeam (Qihoo360''s Unicorn Team, credited on the sibling HITBSecConf2018 Amsterdam badge) as a hardware contributor. No firmware or README present.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts (MCU, display, LEDs, connectivity, battery, distribution, game mode) confirmed on the official HITB event archive page, which credits Shepard Lab and HackersBadge.com as the badge designers. A companion GitHub repo (UnicornTeam/hitb2018dubai-badge) holds only a schematic and PDF -- no firmware, so make_your_own.open_source is "partial" rather than "yes". Price and total quantity produced are not published anywhere found; left empty. Could not verify a public firmware repository.'
last_modified_date: '2026-09-08'
---

The HITBSecConf2018 Dubai badge was the official electronic conference badge handed to attendees of HITBSecConf2018 in Dubai (November 27-28, 2018), designed by Shepard Lab and HackersBadge.com with hardware work credited to UnicornTeam. It runs on an STM32F103 (ARM Cortex-M3) with a 1.44" ST7735S 128x128 color TFT display, 18 SK6805 addressable RGB LEDs, six navigation buttons, an SX1278 LoRa 433 MHz radio, and power from two AAA batteries.

Beyond showing the talks agenda and schedule, the badge doubled as the centerpiece of the conference's Badge Village: attendees used the LoRa link to hunt down 12 "badge masters" scattered around the venue, with the goal of becoming "master of all the badges." It was distributed free to conference attendees rather than sold.

## Make your own

A companion repository, UnicornTeam/hitb2018dubai-badge, publishes the badge's schematic (`HITB_DXB_V1.1.sch`) and a matching PDF. No firmware source or bill of materials was found alongside it, so only the hardware side is openly available.
