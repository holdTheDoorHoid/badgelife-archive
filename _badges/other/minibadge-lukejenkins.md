---
title: minibadge (lukejenkins)
id: other-minibadge-lukejenkins
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: other
year: 0
makers:
- name: lukejenkins
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
- label: github.com/lukejenkins/minibadge
  url: https://github.com/lukejenkins/minibadge
  kind: repo
  archived: https://web.archive.org/web/20260510061822/https://github.com/lukejenkins/minibadge
images: []
contact: {}
notes: []
status: not_an_item
sources:
- kind: url
  url: https://github.com/lukejenkins/minibadge
  title: minibadge (lukejenkins)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
  archived: https://web.archive.org/web/20260510061822/https://github.com/lukejenkins/minibadge
- kind: url
  url: https://github.com/lukejenkins/minibadge
  title: GitHub - lukejenkins/minibadge
  accessed: '2026-09-07'
  note: Repo README confirms this is the minibadge connector specification/component library (v2.0), not a single physical badge or SAO. Apache-2.0 licensed, KiCad/Eagle library files, I2C protocol, CLK sync pin, PROG pin for AVR ISP/ST-Link SWD/PIC ICSP/UART.
  archived: https://web.archive.org/web/20260510061822/https://github.com/lukejenkins/minibadge
- kind: url
  url: https://hackaday.com/2019/03/20/introducing-the-shitty-add-on-v1-69bis-standard/
  title: Introducing The Shitty Add-On V1.69bis Standard | Hackaday
  accessed: '2026-09-07'
  note: Confirms Luke Jenkins' minibadge standard originated for SAINTCON (used with 5V/3V3/I2C/SPI in under a square inch, over a dozen minibadges built against it) and inspired the Supercon Add-On Add-On (SAOAO) standard.
  archived: https://web.archive.org/web/20260516210428/https://hackaday.com/2019/03/20/introducing-the-shitty-add-on-v1-69bis-standard/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: This is a connector/electrical specification and KiCad/Eagle component library for a minibadge standard (v2.0, Apache-2.0), not a single physical badge or SAO product, so it does not fit this archive's per-item schema. The standard was created by Luke Jenkins for SAINTCON badges (used with I2C, CLK sync, and a PROG pin for AVR ISP/ST-Link SWD/PIC ICSP/UART), and later inspired the separate Supercon Add-On Add-On (SAOAO) standard. Individual minibadges built to this spec (over a dozen exist per Hackaday) are the kind of items that would deserve their own entries, not this spec repo itself.
last_modified_date: '2026-09-07'
---

This repository is not a single badge or SAO but the specification and reference component library for the "minibadge" connector standard, created by Luke Jenkins and maintained with contributions from SparkFun and several other collaborators. Version 2.0 of the standard defines an I2C protocol for badge-to-minibadge communication, a CLK pin for synchronization, a PROG pin supporting AVR ISP, ST-Link SWD, PIC ICSP, and UART programming, and variable supply voltage (3.3V to 5V). Design files are published in both Eagle and KiCad formats under the Apache 2.0 license.

The standard was originally created for SAINTCON, where it let badge makers pack 5V, 3.3V, I2C, and SPI connectivity into a footprint under one square inch; more than a dozen individual minibadges were built to the spec for SAINTCON badges. It later influenced the Supercon Add-On Add-On (SAOAO) standard used at Supercon. Because this entry is the spec repository itself rather than a specific physical badge, most item-level fields (maker's own badge, price, LEDs, images of a specific board) do not apply here.

