---
title: Whiskey Pirates DC22 Badge
id: dc22-whiskey-pirates-dc22-badge
layout: badge
parent: DC22
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc22
year: 2014
makers:
- name: Whiskey Pirate Crew
  url: http://www.whiskeypirates.com/
summary: A dual-microcontroller badge (codename "Three Kings") made by the Whiskey Pirate Crew for DEF CON 22, built as a learning project rather than a commercial release.
functions: 'Not documented beyond firmware for the two onboard microcontrollers; no games, sensors, or radio features are described in the source repo.'
look:
  colors: []
  shape: null
  themes:
  - pirate
tech:
  mcu: STM32 + ATtiny88
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/whiskeypirates/dc22-whiskeypirates/blob/master/3KPirate_rev3_schematic.pdf
  firmware_url: https://github.com/whiskeypirates/dc22-whiskeypirates
  eda_tool: null
links:
- label: github.com/whiskeypirates/dc22-whiskeypirates
  url: https://github.com/whiskeypirates/dc22-whiskeypirates
  kind: repo
- label: whiskeypirates.com
  url: http://www.whiskeypirates.com/
  kind: website
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/whiskeypirates/dc22-whiskeypirates
  title: Whiskey Pirates DC22 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 22, source repo for the badge''.'
- kind: url
  url: https://raw.githubusercontent.com/whiskeypirates/dc22-whiskeypirates/master/README.md
  title: dc22-whiskeypirates README
  accessed: '2026-09-07'
  note: 'Confirms event (DEF CON 22), codename "Three Kings", dual STM32/ATtiny88 MCU design, and that this was a learning project rather than a commercial product.'
- kind: url
  url: http://www.whiskeypirates.com/
  title: the whiskey pirates
  accessed: '2026-09-07'
  note: 'Maker group homepage; confirms the group exists across many DEF CON years but has no dedicated dc22 sub-page (only dc27 onward have per-year sites), and describes the group as a social crew rather than a badge vendor.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This badge was made for DEF CON 22 (2014), but events.yml has no dc22 entry (its DEF CON ids start at dc24), so event is left as "other". No photo of the physical badge, LED/display details, price, or quantity could be found; the repo contains only firmware source, compiled binaries, and a schematic PDF, no images. The Whiskey Pirate Crew is a social/hacking group (not a commercial badgelife maker) that has made a badge nearly every DEF CON year since; other entries in existing_titles.txt note their later badges as "not badgelife", consistent with this one being a gift/learning project rather than a sold item.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/whiskey-pirates-dc22-badge/
---

The Whiskey Pirates DC22 Badge, internally codenamed "Three Kings," was made by the Whiskey Pirate Crew for DEF CON 22 in 2014. It is a dual-microcontroller design pairing an STM32 with an ATtiny88, built explicitly as a learning project so a crew member could understand the hardware and firmware end to end. The maker's own notes describe it self-deprecatingly as a first attempt at low-level electrical design, with firmware developed in CooCox IDE/GCC for the STM32 side and Atmel Studio 6.2 for the ATtiny88 side.

The project's GitHub repository publishes both microcontrollers' firmware source and compiled binaries, along with a schematic PDF ("3KPirate_rev3_schematic.pdf"), making the hardware and firmware fully open. No photos of the physical badge, no LED or display specifications, and no information about how many were made or how they were distributed have surfaced; the Whiskey Pirate Crew appears to be an informal DEF CON social group that builds a badge most years for its own members rather than selling them, consistent with how their later-year badges are described elsewhere in the archive's source sheet.

## Make your own

The GitHub repository (linked above) has everything needed to reproduce the badge: the schematic PDF, STM32 firmware source (buildable with CooCox IDE/GCC), and ATtiny88 firmware source (buildable with Atmel Studio 6.2). The maker notes the STM32 can be flashed/debugged with any ST Discovery or Nucleo board (~$8-15) and the ATtiny88 with a USBasp programmer (~$3-8).
