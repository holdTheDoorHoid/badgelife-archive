---
title: HackerHotel 2019 Badge
id: hackerhotel-2019-hackerhotel-2019-badge
layout: badge
parent: Hackerhotel 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hackerhotel-2019
year: 2019
makers:
- name: Badge.Team (Tom Clement, Raboof, Renze Nicolai, Anne Jan Brouwer, Bas van Sisseren)
summary: The badge handed out to attendees of Hackerhotel 2019, built mostly from left-over SHA2017 badge hardware with a few new additions.
functions: General ESP32 badge platform with infrared transmit/receive, stereo audio output, and a Grove I2C port for add-ons.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: ESP32
  leds: null
  display: null
  connectivity:
  - ir
  - i2c
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Handed out to attendees at Hackerhotel 2019.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: badge.team/docs/badges/hackerhotel-2019
  url: https://badge.team/docs/badges/hackerhotel-2019/
  kind: website
  archived: https://web.archive.org/web/20260513013152/https://badge.team/docs/badges/hackerhotel-2019/
images: []
contact: {}
notes:
- Built from SHA2017 badge leftover parts; 8MB extra RAM (4MB addressable), IR tx/rx, stereo audio (reversed jack design flaw), Grove I2C, SAO connector.
status: released
sources:
- kind: url
  url: https://badge.team/docs/badges/hackerhotel-2019/
  title: HackerHotel 2019 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''Hackerhotel 2019''.'
  archived: https://web.archive.org/web/20260513013152/https://badge.team/docs/badges/hackerhotel-2019/
- kind: url
  url: https://badge.team/docs/badges/hackerhotel-2019/
  title: Hackerhotel 2019 | Badge.Team
  accessed: '2026-09-07'
  note: Confirmed maker credits, ESP32 base, extra 8MB PSRAM (4MB addressable), IR transceiver, stereo audio with a reversed-jack design flaw, Grove I2C, and SAO connector; only image found is an SVG illustration (hh2019.svg), not a photo, so no image was saved.
  archived: https://web.archive.org/web/20260513013152/https://badge.team/docs/badges/hackerhotel-2019/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Only source available is the badge.team docs page itself (a maker/community-team page, so treated as primary). No press coverage, storefront, quantity, price, or dedicated hardware/firmware repo link for this specific event build was found; it reuses the SHA2017 badge's ESP32 platform and firmware stack rather than having its own repo. LED count/type and display are not mentioned by the source and are left empty. Distributed free to attendees, consistent with badge.team's other camp-badge giveaways.
last_modified_date: '2026-09-07'
---

The Hackerhotel 2019 badge was the attendee badge for the 2019 edition of Hackerhotel, a small Dutch hacker gathering. Rather than a from-scratch design, Badge.Team (Tom Clement, Raboof, Renze Nicolai, Anne Jan Brouwer, and Bas van Sisseren) built it largely from left-over parts of the SHA2017 camp badge, adding an extra 8MB of PSRAM (4MB of it addressable), an infrared transmitter/receiver, stereo audio output, a Grove I2C connector, and an SAO connector.

One quirk noted in the maker's own documentation: the audio jack was mounted in reverse due to a design error, so the first and third rings need to be swapped for correct stereo output — without the fix, one channel is wired to ground. Beyond the badge.team documentation page, no independent press coverage, storefront listing, or dedicated repository for this specific build was found, so pricing, quantity, and open-source file links are left blank here.
