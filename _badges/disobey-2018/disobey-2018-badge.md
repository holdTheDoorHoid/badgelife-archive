---
title: Disobey 2018 Badge
id: disobey-2018-disobey-2018-badge
layout: badge
parent: Disobey 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: disobey-2018
year: 2018
makers:
- name: Disobey
summary: 'An electronic conference badge given to every Disobey 2018 attendee, shaped like a Nintendo-style gamepad, that plays LED animations and lets badges trade keys over UART to unlock puzzles.'
functions: 'Plays generated LED animations while idle; badges exchange "keys" over a half-duplex UART link, and collecting keys from all 9 badge variants unlocks further puzzles online; accepts a Konami-code button sequence to enter a code-input mode; when plugged into USB, presents as a HID gamepad (two axes, four buttons) or, after the Konami code, as a HID keyboard.'
look:
  colors: []
  shape: null
  themes:
  - console
  - puzzle
  - ctf
tech:
  mcu: STM32F0
  leds:
    count: 14
    type: null
    note: 14-pixel LED array used as a low-res display for generated animations
  display: LED array 14px
  connectivity:
  - uart
  - usb
  battery: coin cell (with USB power detection/override)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to all Disobey 2018 attendees as their conference badge.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/disobeyfi/badge-2018
  firmware_url: https://github.com/disobeyfi/badge-2018
  eda_tool: null
  license: GPL-3.0
links:
- label: github.com/disobeyfi/badge-2018
  url: https://github.com/disobeyfi/badge-2018
  kind: repo
images:
- file: assets/images/badges/disobey-2018/disobey-2018-badge/f3f1bd5080.jpg
  source: "https://github.com/disobeyfi/badge-2018"
  credit: "Disobey"
  caption: "Disobey 2018 badge, gamepad-style PCB with LED array"
contact: {}
notes:
- Hardware design and source files for the Disobey 2018 conference badge (GPL-3.0), published in the disobeyfi GitHub org. Found by the event-year sweep, task con-disobey.
status: released
sources:
- kind: url
  url: https://github.com/disobeyfi/badge-2018
  title: Disobey 2018 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-disobey); event read as ''Disobey 2018''.'
- kind: url
  url: https://raw.githubusercontent.com/disobeyfi/badge-2018/master/README.md
  title: 'Sources for Disobey 2018 badge (README)'
  accessed: '2026-09-08'
  note: 'README describing the badge''s hardware (STM32F0, 8MHz, 14-pixel LED display, coin battery with USB detect), the key-collecting/UART game across 9 badge types, Konami-code input, and USB HID gamepad/keyboard modes.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts confirmed directly from the maker''s own repo and README. Price, exact quantity made, and PCB color were not stated anywhere found and are left empty. The repo also mentions a bonus SBUS-to-USB adapter firmware bundled in the same project, unrelated to the badge itself, not recorded as a separate field.'
last_modified_date: '2026-09-08'
---

The Disobey 2018 badge was given to every attendee of Disobey, the Finnish hacker conference, as part of that year's badge challenge. Built around an STM32F0 microcontroller, it spends most of its time asleep, waking to play generated LED animations across a 14-pixel LED array that doubles as a low-resolution display. It is shaped to resemble a Nintendo-style gamepad, a form factor it leans into further when connected to USB.

Nine different badge variants were produced, each with its own hardcoded key. Badges trade these keys with each other over a half-duplex UART link; accumulating the full set unlocks further puzzles hosted online, tying the badge into a wider scavenger-hunt-style challenge for the conference. Entering a Konami-code button sequence puts the badge into a code-input mode used for the key exchange, and when plugged into a computer over USB the badge can act as a HID gamepad (two axes, four buttons) or, after the Konami code, as a HID keyboard.

Hardware and firmware were published to GitHub under the disobeyfi organization, licensed GPL-3.0, giving a full account of the badge's electronics and the animation, key-exchange, and USB HID logic.
