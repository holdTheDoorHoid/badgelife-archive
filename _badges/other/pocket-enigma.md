---
title: Pocket Enigma
id: other-pocket-enigma
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 0
makers:
- name: Bradán Lane
  url: https://bradanlane.com
summary: A full-functioning electronic Enigma cipher machine repurposed from a SMART Response XE classroom clicker, built by Bradán Lane as part of his "Adventures of Sara Cladlow" story project.
functions: Encodes and decodes Enigma-style messages compatible with historical WWII Enigma machines, Enigma simulators, and online role-playing games. Can send and receive coded messages wirelessly over short range using a built-in 2.4GHz RF transceiver, or exchange messages with other Pocket Enigma units.
look:
  colors: []
  shape: rectangle
  themes:
  - crypto
  - puzzle
tech:
  mcu: null
  leds: null
  display: 384x136 4-gray-level LCD (no backlight)
  connectivity: []
  battery: 4x AAA
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
  firmware_url: https://gitlab.com/bradanlane/enigma
  eda_tool: null
links:
- label: aosc.cc/enigma.php
  url: https://aosc.cc/enigma.php
  kind: website
  archived: https://web.archive.org/web/20260410230344/https://aosc.cc/enigma.php
- label: Pocket Enigma Documentation
  url: https://aosc.cc/enigmadoc.php
  kind: doc
  archived: https://web.archive.org/web/20260410234349/https://aosc.cc/enigmadoc.php
- label: Enigma API (gitlab)
  url: https://gitlab.com/bradanlane/enigma
  kind: repo
  archived: https://web.archive.org/web/20260519084511/https://gitlab.com/bradanlane/enigma
- label: SRXEcore library (gitlab)
  url: https://gitlab.com/bradanlane/srxecore
  kind: repo
  archived: https://web.archive.org/web/20260511011525/https://gitlab.com/bradanlane/srxecore
images:
- file: assets/images/badges/other/pocket-enigma/51b21abf85.png
  source: https://aosc.cc/enigma.php
  credit: Bradán Lane
  caption: Pocket Enigma home screen
  archived: https://web.archive.org/web/20260410230344/https://aosc.cc/enigma.php
- file: assets/images/badges/other/pocket-enigma/1ba61e4360.png
  source: https://aosc.cc/enigma.php
  credit: Bradán Lane
  caption: Pocket Enigma Enigma-machine setup screen
  archived: https://web.archive.org/web/20260410230344/https://aosc.cc/enigma.php
contact: {}
notes:
- Not made for any specific convention; it is a standalone hobbyist project tied to the maker's ongoing "Adventures of Sara Cladlow" fiction/puzzle story, done under the name T.E.C. (with collaborators Tod Troche and Lory Ester credited on the story side).
- No price, quantity-made, or availability/sale information is published on the maker's site; it reads as a personal build documented for others to replicate rather than something sold.
- Connectivity is a built-in 2.4GHz RF transceiver for short-range device-to-device messaging; this does not map cleanly to the archive's connectivity vocabulary (not standard wifi/ble/zigbee), so it is left out of tech.connectivity and noted here instead.
- Hardware is a repurposed SMART Response XE (a classroom "clicker" device), not an original PCB design; open-source firmware is published (SRXEcore library and Enigma API on GitLab) but there is no separate hardware/gerbers repo since the base hardware is the pre-existing commercial clicker unit.
status: listed
sources:
- kind: url
  url: https://aosc.cc/enigma.php
  title: Pocket Enigma
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''unknown''.'
  archived: https://web.archive.org/web/20260410230344/https://aosc.cc/enigma.php
- kind: url
  url: https://aosc.cc/enigmadoc.php
  title: AoSC - Pocket Enigma Documentation
  accessed: '2026-09-07'
  note: Hardware specs (display, battery, dimensions), software repo links, and confirmation the base hardware is a repurposed SMART Response XE.
  archived: https://web.archive.org/web/20260410234349/https://aosc.cc/enigmadoc.php
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own project page and documentation confirm what the device is and how it works, but there is no year, price, quantity, or distribution information published anywhere on the site, and no evidence it was made for or given out at a convention. Left event as "other" since no con could be identified.
last_modified_date: '2026-09-07'
---

The Pocket Enigma is a working electronic Enigma cipher machine built by Bradán Lane, repurposed from the hardware of a SMART Response XE — a classroom "clicker" device originally used for student response systems. It keeps that device's 384x136-pixel 4-gray LCD screen and mini keyboard, but runs custom firmware that emulates several historical Enigma machine configurations (rotors, reflectors, and plugboard), letting the user encode and decode messages compatible with real WWII Enigma traffic, Enigma simulators found online, and other Pocket Enigma units. A built-in 2.4GHz RF transceiver lets two units exchange coded messages wirelessly over short range.

The project is not tied to a hacker convention; it is part of the maker's ongoing "Adventures of Sara Cladlow" story and puzzle universe (credited to Sara Cladlow / T.E.C., a fictional team including Tod Troche and Lory Ester), where the Pocket Enigma is framed as a prop for solving in-story clues. The maker's site documents the device's menus and setup in detail and links to two open-source GitLab repositories — the SRXEcore library and an Enigma API — that implement the underlying cipher logic, but publishes no price, production quantity, or sale information, suggesting it was built and documented for personal/hobbyist use and sharing rather than as a product.
