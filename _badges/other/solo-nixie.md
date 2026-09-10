---
title: Solo-Nixie
id: other-solo-nixie
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: other
year: 0
makers: []
summary: ''
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
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
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/183056-solo-nixie
  url: https://hackaday.io/project/183056-solo-nixie
  kind: hackaday
  archived: https://web.archive.org/web/20250912041420/https://hackaday.io/project/183056-solo-nixie/
images: []
contact: {}
notes:
- Self-contained VFD driver in 'cube' minibadge form factor.
status: not_an_item
sources:
- kind: url
  url: https://hackaday.io/project/183056-solo-nixie
  title: Solo-Nixie
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''unknown''.'
  archived: https://web.archive.org/web/20250912041420/https://hackaday.io/project/183056-solo-nixie/
- kind: url
  url: https://github.com/pierre-muth/solo-nixie
  title: pierre-muth/solo-nixie
  accessed: '2026-09-07'
  note: Confirms it is a standalone desk clock with no convention/badge connection; GPL-3.0 hardware and firmware.
- kind: url
  url: https://pierremuth.wordpress.com/2021/12/11/a-cute-little-single-tube-nixie-clock/
  title: A cute little single tube nixie clock
  accessed: '2026-09-07'
  note: Maker's own blog post describing the project (not fetched directly; referenced from the GitHub repo).
  archived: https://web.archive.org/web/20260611123624/https://pierremuth.wordpress.com/2021/12/11/a-cute-little-single-tube-nixie-clock/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Not a con badge or SAO. This is Solo-Nixie, a standalone single-tube Nixie clock by Pierre Muth (Muth), posted to Hackaday.io on 2021-12-13. It uses a PIC16F18346 MCU, a DS3231 RTC, and an onboard boost converter driving one LD-955a or IN-16 Nixie tube to ~200V, powered over USB, with two buttons for time/brightness. It ships in a 3D-printed (Fusion 360) enclosure and is fully open source (KiCad + MPLAB firmware, GPL-3.0) at github.com/pierre-muth/solo-nixie. Nothing in the Hackaday.io page or GitHub repo ties it to any hacker convention, badge event, or SAO/minibadge form factor; the entry's existing note calling it a 'cube minibadge' does not match the source material and appears to be a discovery-sweep misread.
last_modified_date: '2026-09-07'
---

Solo-Nixie is a desktop Nixie-tube clock designed by Pierre Muth (published to Hackaday.io as project #183056 on December 13, 2021), not a convention badge or SAO. It drives a single LD-955a or IN-16 Nixie tube from an onboard high-voltage boost converter (about 200V, 10µH coil, 100kHz switching) on a 4-layer PCB with isolated high-voltage sections, keeps time with a DS3231 RTC, and runs on a PIC16F18346 microcontroller. Two buttons set the hours/minutes and adjust brightness, and the design includes a voltage-measurement cutoff for protection. The assembled clock sits in a 3D-printed enclosure modeled in Fusion 360.

The project is fully open source: KiCad hardware files, MPLAB firmware, and the enclosure STLs are published under GPL-3.0 at github.com/pierre-muth/solo-nixie, with a build write-up on the maker's WordPress blog. No source found connects Solo-Nixie to any hacker conference, badge sheet, or SAO ecosystem — it appears to have been added to the archive's badge sheet in error.

