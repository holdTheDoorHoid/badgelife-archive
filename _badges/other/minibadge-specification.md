---
title: Minibadge specification
id: other-minibadge-specification
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 0
makers:
- name: compukidmike
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
- label: github.com/compukidmike/minibadge
  url: https://github.com/compukidmike/minibadge
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: not_an_item
sources:
- kind: url
  url: https://github.com/compukidmike/minibadge
  title: Minibadge specification
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    This is a specification/standards repository for the "minibadge" interface
    (a small modular badge-to-badge add-on connector), not a specific
    manufactured badge or SAO. Originally created by Luke Jenkins
    (github.com/lukejenkins), forked and maintained by compukidmike, with
    contributions from SparkFun, hamster, sodium-hydrogen, and jup1t3r. It
    defines an I2C-based protocol and pin layout (+VBATT 3.3-5V, CLK, SDA/SCL,
    programming pins, reserved NC pins) for minibadges to talk to a host
    badge, plus Eagle and KiCad (v5/v6) design files, footprints, and I2C
    example code, released under Apache 2.0. It is associated in spirit with
    the SAINTCON Enigma minibadge ecosystem (SAINTCON's badge popularized the
    minibadge form factor starting around 2019) but the repo itself is a
    reusable spec/library, not a single badge made for one event/year, so no
    event correction was made. No specific product, price, quantity, or image
    exists to catalog here.
last_modified_date: '2026-09-07'
---

This entry documents "minibadge," an open-source specification and design-file library for the minibadge connector standard rather than any single physical badge. Minibadges are small modular add-on boards that plug into a larger host badge, similar in spirit to an SAO but built around SAINTCON's Enigma-badge ecosystem, which popularized the form factor. The repository, maintained by compukidmike as a fork of an earlier project by Luke Jenkins, defines the physical pin layout and an I2C communication protocol so a host badge and its attached minibadges can exchange data such as button presses, score updates, and brightness control.

The repo bundles reusable engineering assets rather than a finished product: Eagle schematics, KiCad 5 and 6 versions, footprint diagrams, and example I2C code, all released under the Apache 2.0 license. Contributors credited in the project include SparkFun, hamster, sodium-hydrogen, and jup1t3r. Because this is a specification and toolkit for building minibadges rather than a specific badge or SAO that was made for one event and sold or given away, it does not fit the archive's item schema and is marked not_an_item.
