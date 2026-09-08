---
title: DEF CON 20 Badge
id: dc20-badge
layout: badge
parent: DC20
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc20
year: 2012
makers:
- name: Parallax (manufacturer); Ryan Clarke / LosT (designer)
summary: 'The DEF CON 20 (2012) attendee badge: a Propeller-based multicore IR puzzle and development platform with 21 "Human" variants tied to attendee roles.'
functions: 'Infrared badge-to-badge communication for tracking attendee encounters, an embedded secret-society narrative (hieroglyphics, binary, venue clues, social puzzles), VGA/PS2 expansion allowing attendees to turn the badge into a small computer, and reprogrammable EEPROM-stored firmware (Assembly, C, or Spin) via USB.'
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - security
  - ctf
tech:
  mcu: Propeller P8X32A
  leds:
    count: 8
    type: null
    note: 'Eight LEDs used for visual feedback'
  display: null
  connectivity:
  - ir
  - usb
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
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/badges/def-con-20-badge
  url: https://badge.gallery/badges/def-con-20-badge
  kind: website
images:
- file: assets/images/badges/dc20/badge/b1bf347d2b.jpg
  source: "https://badge.gallery/badges/def-con-20-badge"
  credit: "Wikimedia Commons (CC BY-SA 4.0), via badge.gallery"
  caption: "DEF CON 20 badge (Human variant), Propeller-based IR puzzle badge"
contact: {}
notes:
- Propeller P8X32A-based badge with IR badge-to-badge comms, 21 Human-badge variants, and a VGA/PS2-expandable HHV platform. Found by the event-year sweep, task general-2006.
- 'This entry duplicates dc20-official-badge, which covers the same DEF CON 20 official badge (Ryan Clarke/LosT, Parallax). Both entries filled in independently per research-guide instructions; consider merging.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/def-con-20-badge
  title: DEF CON 20 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2006); event read as ''dc20''.'
- kind: url
  url: https://badge.gallery/badges/def-con-20-badge
  title: DEF CON 20 Badge
  accessed: '2026-09-08'
  note: 'Confirmed designer (Ryan Clarke/LosT), manufacturer (Parallax), chip (Propeller P8X32A), LED count, IR/USB features, VGA/PS2 expansion, and 21 Human-badge variants. Price, quantity, and availability were not stated.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (designer, manufacturer, chip, features) confirmed via badge.gallery, a third-party archive site, not the maker''s own page directly. Price, quantity made, and current availability were not found. This entry duplicates dc20-official-badge (same badge, same designer/maker); see notes for detail. Open-source status set to partial since Parallax published firmware examples, schematics, and code objects per the source, but no direct repo/file URL was found to link.'
last_modified_date: '2026-09-08'
---

The DEF CON 20 badge (2012, Rio Hotel, Las Vegas) was designed by Ryan Clarke (LosT) and manufactured by Parallax, built around Parallax's own Propeller P8X32A multicore microcontroller. It shipped in 21 different "Human" badge shape variants, each tied to one of eight attendee-role color schemes, and used eight onboard LEDs for visual feedback. Firmware lived in onboard EEPROM and could be reprogrammed in Assembly, C, or Spin over USB.

Functionally, the badge combined an infrared badge-to-badge link (used to track and record encounters between attendees) with an embedded secret-society narrative woven from hieroglyphics, binary codes, venue-based clues, and social puzzles for attendees to work out over the course of the con. It also exposed VGA and PS/2 expansion, letting sufficiently motivated attendees turn the badge into a small standalone computer system — a hallmark of the DEF CON hardware-hacking-village (HHV) badges of this era.

Price, production quantity, and current availability were not stated on the source consulted. This entry substantially duplicates `dc20-official-badge`, which was already filled in separately for the same badge, designer, and maker.
