---
title: xmas id badge (flair)
id: other-xmas-id-badge-flair
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: other
year: 2018
makers:
- name: tactical_snacks
  url: https://hackaday.io/hacker/294167-tacticalsnacks
summary: A small hand-soldered blinking Christmas-tree PCB built around an ATmega328P (VQFN-28) and a CR1220 coin cell, made as a holiday gift to clip onto a spouse's work ID badge or hang as an ornament; it blinks then sleeps to save the battery.
functions: 'Blinks LED animations on the tree shape, then goes to sleep to conserve the coin cell.'
look:
  colors: []
  shape: null
  themes:
  - holiday
tech:
  mcu: ATmega328P
  leds: null
  display: null
  connectivity: []
  battery: CR1220
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Not sold; made as a one-off personal gift.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/tactical-snacks/xmas_id_badge_pub
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/163899-xmas-id-badge-flair
  url: https://hackaday.io/project/163899-xmas-id-badge-flair
  kind: hackaday
- label: github.com/tactical-snacks/xmas_id_badge_pub
  url: https://github.com/tactical-snacks/xmas_id_badge_pub
  kind: repo
images:
  - file: assets/images/badges/other/xmas-id-badge-flair/34791db0ae.jpg
    source: "https://hackaday.io/project/163899-xmas-id-badge-flair"
    credit: "tactical_snacks"
    caption: "The xmas id badge (flair) PCB, hand-soldered around an ATmega328P"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/163899-xmas-id-badge-flair
  title: xmas id badge (flair)
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/163899-xmas-id-badge-flair
  title: xmas id badge (flair) - project details
  accessed: '2026-09-07'
  note: Confirmed description, maker's motivation (gift for spouse), ATmega328P VQFN-28 MCU, CR1220-class button cell, hand-soldering with a heat gun, and hackaday.io/GitHub links.
- kind: url
  url: https://github.com/tactical-snacks/xmas_id_badge_pub
  title: tactical-snacks/xmas_id_badge_pub
  accessed: '2026-09-07'
  note: Confirmed repo contains schematic, board layout, and BOM under an MIT license; only hardware files are published, no firmware.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Not made for or distributed at any conference; it is a personal Christmas gift, which is why the event stays "other". Hackaday project was posted 2019-02-14 but describes a Christmas-tree ornament, consistent with the 2018 holiday season already recorded. Exact LED count/type, firmware source, and any price/quantity are not stated anywhere found; firmware itself does not appear to be published (only schematic/board/BOM are in the repo), so open_source is "partial".'
last_modified_date: '2026-09-07'
---

tactical_snacks built this small hand-soldered PCB as flair for a spouse's work ID badge during the 2018 holiday season — small enough to clip onto a badge lanyard or hang on a tree as an ornament. It is built around an ATmega328P in the tight VQFN-28 package, powered by a coin cell, and blinks a Christmas-tree LED pattern before sleeping to conserve battery. The maker hand-soldered the fine-pitch MCU with a paint-stripping heat gun and programmed it with an Atmel-ICE; the on-board programming header was later removed and covered with kapton tape to keep the final size small once the battery was installed.

This was a one-off personal gift rather than something made for or sold at a conference, so it isn't tied to any specific event beyond the 2018 Christmas season. The hardware — schematic, board layout, and bill of materials — is published on GitHub under the MIT license, but no firmware source was found in the repository, so the design is only partially open.

## Make your own

Schematic (.sch), board layout (.brd), and a BOM are available at [github.com/tactical-snacks/xmas_id_badge_pub](https://github.com/tactical-snacks/xmas_id_badge_pub) under the MIT license. Firmware source was not found; someone reproducing the board would need to write their own blink/sleep firmware for the ATmega328P.
