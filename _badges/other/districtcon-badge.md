---
title: DistrictCon Year 1 Badge
id: other-districtcon-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2026
makers:
- name: BigTaro's Badges
  url: https://bigtaro.net/discoone
summary: The official electronic badge for DistrictCon Year 1 (2026), featuring a round color display, an SAO connector, and a built-in game called SNOWPOCALYPSE.
functions: Runs a game mode called SNOWPOCALYPSE with high-score saving; navigable menu via six tactile buttons; IR receiver for badge-to-badge or environment interaction; built-in microphone.
look:
  colors: []
  shape: null
  themes:
  - security
tech:
  mcu: RP2350
  leds:
    count: 12
    type: WS2812B
    note: ''
  display: 1.28" round LCD (GC9A01 driver, 240x240)
  connectivity:
  - ir
  battery: 18650 Li-ion with onboard charging circuit
  sao_version: v2
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
  firmware_url: https://github.com/bigtasobadges/DistrictConYear1Badge
  eda_tool: null
links:
- label: bigtaro.net/discoone
  url: https://bigtaro.net/discoone
  kind: website
- label: DistrictConYear1Badge firmware (GitHub)
  url: https://github.com/bigtasobadges/DistrictConYear1Badge
  kind: repo
images:
  - file: assets/images/badges/other/districtcon-badge/ce0065ab98.png
    source: "https://bigtaro.net/discoone"
    credit: "BigTaro's Badges"
    caption: "DistrictCon Year 1 badge"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://bigtaro.net/discoone
  title: DistrictCon Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''unknown''.'
- kind: url
  url: https://bigtaro.net/discoone
  title: "DistrictCon Year 1 Badge - bigtaro.net"
  accessed: '2026-09-07'
  note: 'Maker''s own project page: confirmed event (DistrictCon Year 1, 2026), RP2350 MCU with 4MB flash, 240x240 GC9A01 display, 12x WS2812B LEDs, six buttons, IR receiver, microphone, 18650 LiPo battery, SAO connector with I2C, SNOWPOCALYPSE game mode, and a link to open-source starter firmware on GitHub (bigtasobadges/DistrictConYear1Badge, v1.2).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Made for DistrictCon Year 1 (2026); no matching event id exists yet in _data/events.yml (only dc## and other cons are defined, no districtcon entries), so event is left as "other" pending a dedicated event id. Price, quantity made, and general-public availability are not stated on the maker''s page. Hardware design files (schematics/PCB/gerbers) were not found, only firmware; make_your_own.open_source is set to "partial" on that basis. Could not confirm whether the GitHub firmware repo is public/reachable via automated tools (returned 404 to an authenticated-style fetch, but the maker''s own page links directly to it, so the URL is trusted and kept).'
last_modified_date: '2026-09-07'
---

The DistrictCon Year 1 Badge is the official electronic conference badge made by BigTaro's Badges for DistrictCon's first edition in 2026. It centers on an RP2350 microcontroller driving a round 240x240 color LCD (GC9A01 driver), with a ring of 12 WS2812B addressable LEDs for lighting effects, six tactile buttons for menu navigation, an IR receiver, a built-in microphone, and a 6-pin SAO connector with I2C so the badge can host add-ons. Power comes from a user-supplied 18650 Li-ion cell with an onboard charging circuit.

The badge's headline feature is an on-board game called SNOWPOCALYPSE, which saves high scores locally. BigTaro's Badges published starter firmware for the platform on GitHub (bigtasobadges/DistrictConYear1Badge, versioned to at least v1.2), giving badge holders and other developers a base to build their own firmware against, though no hardware design files (schematics, PCB layout, or gerbers) were found alongside it — only the firmware is confirmed open.

Pricing, production quantity, and how the badge was distributed (con-included, sold separately, etc.) are not stated on the maker's project page, and no dedicated event id for DistrictCon exists yet in this archive's event list, so this entry remains filed under "Other."
