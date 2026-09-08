---
title: Bitstream Cryptography Badge (CypherCon 1.0, 2016)
id: cyphercon-2016-bitstream-cryptography-badge-cyphercon-1-0-2016
layout: badge
parent: CypherCon 1.0
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cyphercon-2016
year: 2016
makers:
- name: TYMKRS
  url: https://tymkrs.com/
summary: 'A no-microcontroller electronic badge built entirely from 7400-series logic chips that works as a functional XOR stream cipher, letting attendees encode and decode messages by hand using a 3-bit character scheme.'
functions: 'Acts as a hardware encoder/decoder ring: three input switches (1s, 2s, 4s place) feed a linear feedback shift register built from discrete logic, with override-high/override-low and a debounced step button; eight LEDs show LFSR state and three more show the XOR output, following the CypherTTY 3-bit encoding.'
look:
  colors: []
  shape: null
  themes:
  - crypto
  - security
  - hardware tool
  - puzzle
tech:
  mcu: none
  leds: null
  display: none
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
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackthebadge.com/page/2
  url: https://hackthebadge.com/page/2/
  kind: website
- label: hackthebadge.com - CypherCon 2016 Electronic Badge
  url: https://hackthebadge.com/cyphercon-2016-badge/
  kind: website
- label: cyphercon.com/cyphercon-1-0
  url: https://cyphercon.com/cyphercon-1-0/
  kind: website
images:
- file: assets/images/badges/cyphercon-2016/bitstream-cryptography-badge-cyphercon-1-0-2016/9b03cb78e5.png
  source: "https://hackthebadge.com/cyphercon-2016-badge/"
  credit: "TYMKRS / CypherCon"
  caption: "CypherCon 2016 electronic badge, general edition"
contact: {}
notes:
- Official CypherCon 2016 conference badge, a functional minimalist XOR stream cipher built from 7400-series logic chips with no processor, using the 3-bit CypherTTY encoding. Found by the event-year sweep, task cyphercon.
- 'The sheet titled this entry "Bitstream Cryptography Badge"; the maker''s own hackthebadge.com page calls it the "CypherCon 2016 Electronic Badge" / "Cyphercon 2016 badge". Kept the sheet''s title since it also appears as a descriptive subtitle on the maker''s site.'
status: released
sources:
- kind: url
  url: https://hackthebadge.com/page/2/
  title: Bitstream Cryptography Badge (CypherCon 1.0, 2016)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:cyphercon); event read as ''cyphercon-2016''.'
- kind: url
  url: https://hackthebadge.com/cyphercon-2016-badge/
  title: CYPHERCON 2016 Electronic Badge
  accessed: '2026-09-08'
  note: 'Maker page (TYMKRS/CypherCon) confirming design: 74HC595, 74HC14, 74HC86 logic chips, NE555 timer, 6 controls, 8 LFSR indicator LEDs + 3 output LEDs, no microcontroller. Mentions Propeller Tool / .spin firmware links for a related build/test tool, not the badge itself.'
- kind: url
  url: https://www.reddit.com/r/Tymkrs/comments/4ajh8y/cyphercon_badge_2016/
  title: 'CypherCon Badge 2016 : r/Tymkrs'
  accessed: '2026-09-08'
  note: 'Search snippet only (page itself blocked fetch): confirms TYMKRS members Whisker and unnamed co-creator made the CypherCon 2016 inaugural badges, 5 colors, 3 badge designs, cryptography theme.'
- kind: url
  url: https://cyphercon.com/cyphercon-1-0/
  title: CypherCon 1.0 - CypherCon
  accessed: '2026-09-08'
  note: 'Confirms CypherCon 1.0 was held March 11-12, 2016, theme Stream Ciphers & Cryptography, and references a badge described starting with "Bits..." (truncated in search index).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed real and made by TYMKRS for CypherCon 1.0 (2016). Could not confirm price, quantity made, colors/shape, or availability today — no storefront or listing found; a Reddit thread (search snippet only, page blocked on fetch) mentions the badge line shipped in 5 colors and 3 designs but does not say which applies to this specific board. Design files: the maker page links Pastebin .spin firmware for a companion Propeller-based tool, not files for the logic-chip badge itself, so make_your_own is left empty. A near-duplicate entry exists: cyphercon-2016-cyphercon-2016-badge-bitstream-cryptography-xor-stream-ciphe (same badge, different slug) - flagged as duplicate_of in the report.'
last_modified_date: '2026-09-08'
---

The CypherCon 1.0 (2016) badge, built by TYMKRS, is a functional stream-cipher encoder built entirely from discrete 7400-series logic chips — a 74HC595 shift register, 74HC14 hex inverter, 74HC86 quad XOR gate, and an NE555 timer for button debouncing — with no microcontroller or processor anywhere on the board. Attendees used three input switches (representing the 1s, 2s, and 4s place of a 3-bit value), an override-high and override-low switch, and a step button to run a linear feedback shift register by hand, watching eight LEDs track the LFSR state and three more show the XOR'd output, all following CypherTTY, a 3-bit character encoding TYMKRS designed for the badge.

It was the inaugural badge for CypherCon, held March 11-12, 2016 in Milwaukee around the theme of stream ciphers and cryptography, and TYMKRS (credited on Reddit as "Whisker and I") describes making it with a personal goal of keeping the badge genuinely cryptography-related rather than just badge-shaped hardware. Reporting elsewhere on the same badge line mentions five colors and three distinct badge designs for the event, though sources found here don't specify which color or design this particular record covers.

No price, production quantity, or current availability could be confirmed from the sources checked; this was a conference-distributed badge rather than one still sold through an ongoing storefront.
