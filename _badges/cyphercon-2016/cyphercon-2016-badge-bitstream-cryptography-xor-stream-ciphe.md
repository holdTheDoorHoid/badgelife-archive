---
title: Bitstream Cryptography Badge (CypherCon 1.0, 2016)
id: cyphercon-2016-cyphercon-2016-badge-bitstream-cryptography-xor-stream-ciphe
layout: badge
parent: CypherCon 1.0
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cyphercon-2016
year: 2016
makers:
- name: Tymkrs
summary: 'A functional, minimalist XOR stream cipher built entirely from discrete 74-series logic, with no processor or microcontroller.'
functions: 'Encrypts and decrypts short messages using a 3-bit character encoding scheme (CypherTTY): the wearer enters plaintext bits and a cryptographic seed via micro-switches, and an onboard LFSR (shift register + XOR gates) generates a keystream that is XORed with the input to produce ciphertext, shown on 8 indicator LEDs.'
look:
  colors: []
  shape: null
  themes:
  - crypto
  - security
  - hardware tool
  - learn to solder
tech:
  mcu: none
  leds:
    count: 8
    type: discrete
    note: 8 LFSR state/indicator LEDs
  display: none
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
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'The core badge is discrete logic with no firmware. hackthebadge.com also links two Parallax Propeller Spin source files ("Badge Driver_v1_0.spin" and "BadgeMonitor_v1_0.spin", hosted on Pastebin, for Propeller Tool/PropellerIDE) that appear to belong to a companion demo/monitor tool rather than the badge itself; not confirmed as archive-worthy, so no firmware_url was added.'
links:
- label: hackthebadge.com/cyphercon-2016-badge
  url: https://hackthebadge.com/cyphercon-2016-badge/
  kind: website
- label: 'CypherCon 1.0 (cyphercon.com)'
  url: https://cyphercon.com/cyphercon-1-0/
  kind: website
images:
- file: assets/images/badges/cyphercon-2016/cyphercon-2016-badge-bitstream-cryptography-xor-stream-ciphe/9b03cb78e5.png
  source: "https://hackthebadge.com/cyphercon-2016-badge/"
  credit: "Tymkrs"
  caption: "The CypherCon 2016 Bitstream Cryptography badge"
contact: {}
notes:
- CypherCon 1.0 badge implementing a minimalist XOR stream cipher in discrete 7400-series logic with no microcontroller, made by Tymkrs; only CypherCon 2017 and 2019 badges are currently in the archive. Found by the event-year sweep, task general-2016.
- 'The sweep''s title read "CypherCon 2016 Badge (Bitstream Cryptography / XOR Stream Cipher)"; retitled to "Bitstream Cryptography Badge (CypherCon 1.0, 2016)" to match the maker''s and the con''s own naming (cyphercon.com lists it as "Badge: Bitstream Cryptography Badge by the TYMKRS" for "CypherCon 1.0").'
status: listed
sources:
- kind: url
  url: https://hackthebadge.com/cyphercon-2016-badge/
  title: CypherCon 2016 Badge (Bitstream Cryptography / XOR Stream Cipher)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2016); event read as ''CypherCon 2016''.'
- kind: url
  url: https://hackthebadge.com/cyphercon-2016-badge/
  title: CYPHERCON 2016 Electronic Badge
  accessed: '2026-09-08'
  note: 'Description, logic chip list (74HC595, 74HC14, 74HC86, NE555), LED count, functionality, and badge photo URL.'
- kind: url
  url: https://cyphercon.com/cyphercon-1-0/
  title: CypherCon 1.0 - CypherCon
  accessed: '2026-09-08'
  note: 'Confirms maker (TYMKRS) and event/year (CypherCon 1.0, March 2016) with the con''s own naming of the badge.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, event, function, logic-chip list, LED count) confirmed by hackthebadge.com and cyphercon.com, but neither is the maker''s own site/store, so confidence is medium rather than high. Price, quantity made, and availability were not stated anywhere found. No hardware files (schematic/Gerbers) were located; the only linked files are two Propeller Spin sources for what appears to be a separate companion tool, not the badge logic board itself, so make_your_own.open_source is left as partial rather than yes. This entry duplicates an existing one, cyphercon-2016-bitstream-cryptography-badge-cyphercon-1-0-2016.'
last_modified_date: '2026-09-08'
---

The CypherCon 1.0 (2016) badge, built by Tymkrs, is a working exclusive-or stream cipher implemented entirely in discrete 74-series logic — no processor or microcontroller anywhere on the board. It uses a 74HC595 shift register to hold linear-feedback-shift-register (LFSR) state and drive an 8-LED display, a 74HC14 inverter for clock/latch control, 74HC86 XOR gates to do the actual encryption, and an NE555 timer for button debouncing. Wearers key in plaintext using a 3-bit character scheme the makers called CypherTTY, set a cryptographic seed, and watch the badge XOR the keystream against their input to produce ciphertext on the LEDs — an encoder ring made of logic chips rather than software.

It was CypherCon's first badge, made for the inaugural CypherCon 1.0 in Milwaukee (March 2016), whose theme was stream ciphers and cryptography. Two Parallax Propeller Spin source files are linked from the badge's writeup as well, but they read as a separate companion driver/monitor tool for the Propeller platform rather than firmware for the badge itself, which has none.
