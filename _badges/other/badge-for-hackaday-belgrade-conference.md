---
title: Badge for Hackaday Belgrade Conference
id: other-badge-for-hackaday-belgrade-conference
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2016
makers:
- name: Voja Antonic
  url: https://hackaday.io/voja-antonic
summary: The official conference badge for the first Hackaday Belgrade conference in 2016, an 8x16 LED-matrix badge attendees programmed with custom code in a workshop.
functions: Runs a Tetris game and scrolling message display out of the box; badge is reprogrammable over USB during a hands-on workshop; can send/receive simple IR messages between badges.
look:
  colors: []
  shape: rectangle
  themes:
  - retro computer
  - electronics
tech:
  mcu: PIC18LF25K50
  leds:
    count: 128
    type: discrete
    note: 8x16 dot-matrix display built from two TA15-11SRWA LED matrix blocks
  display: LED matrix 8x16
  connectivity:
  - usb
  - ir
  battery: 2x AAA
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution:
  - free_drop
  where: Given to attendees of the Hackaday Belgrade 2016 conference; not sold commercially.
make_your_own:
  open_source: yes
  hardware_url: https://hackaday.io/project/9509-badge-for-hackaday-belgrade-conference
  firmware_url: https://github.com/Hack-a-Day/hackaday-belgrade-badge-MPLABX
  eda_tool: null
links:
- label: hackaday.io/project/9509-badge-for-hackaday-belgrade-conference
  url: https://hackaday.io/project/9509-badge-for-hackaday-belgrade-conference
  kind: hackaday
- label: Hack-a-Day/hackaday-belgrade-badge-MPLABX (GitHub)
  url: https://github.com/Hack-a-Day/hackaday-belgrade-badge-MPLABX
  kind: repo
images:
- file: assets/images/badges/other/badge-for-hackaday-belgrade-conference/c425327ea2.jpg
  source: "https://hackaday.io/project/9509-badge-for-hackaday-belgrade-conference"
  credit: "Voja Antonic"
  caption: "Hackaday Belgrade 2016 conference badge, assembled with LED matrix display"
- file: assets/images/badges/other/badge-for-hackaday-belgrade-conference/6f86d13a3c.jpg
  source: "https://hackaday.io/project/9509-badge-for-hackaday-belgrade-conference"
  credit: "Voja Antonic"
  caption: "Hackaday Belgrade 2016 badge PCB detail"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/9509-badge-for-hackaday-belgrade-conference
  title: Badge for Hackaday Belgrade Conference
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''Hackaday Belgrade''.'
- kind: url
  url: https://hackaday.io/project/9509-badge-for-hackaday-belgrade-conference
  title: Badge for Hackaday Belgrade Conference - project page
  accessed: '2026-09-07'
  note: 'Confirmed maker (Voja Antonic), event/year (Hackaday Belgrade 2016), MCU (PIC18LF25K50), display (8x16 LED matrix, two TA15-11SRWA blocks), power (2x AAA), USB bootloader, IR transmit/receive, Tetris/message-display firmware, and free distribution to attendees.'
- kind: url
  url: https://github.com/Hack-a-Day/hackaday-belgrade-badge-MPLABX
  title: Hack-a-Day/hackaday-belgrade-badge-MPLABX
  accessed: '2026-09-07'
  note: 'Firmware/source repository linked from the project page.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'No matching event id exists in _data/events.yml for "Hackaday Belgrade" — this was the inaugural 2016 Hackaday Belgrade conference in Serbia, distinct from DEF CON/Supercon/etc. Left under event: other per instructions; year set to 2016 from the source. Price/quantity not stated on the project page (badges were given to attendees, not sold). PCB colorway not confirmed from available images beyond a standard green/silkscreen look, so look.colors left empty rather than guessed.'
last_modified_date: '2026-09-07'
---

Voja Antonic designed this badge for the first Hackaday Belgrade conference, held in 2016 in Belgrade, Serbia. It centers on an 8x16 dot-matrix LED display built from two TA15-11SRWA blocks, driven by a Microchip PIC18LF25K50 running at 48 MHz. Out of the box it plays Tetris and scrolls text messages, and attendees used a built-in USB bootloader (Microchip's MCHPFSUSB) to reprogram it with their own code during a conference workshop, without needing a dedicated programmer.

Beyond the display, the badge has five tactile buttons plus a reset button, a Micro-B USB port, a 5-pin serial programming header, and an infrared transmitter/receiver pair (940 nm LED with a TSOP6240TTCD receiver) that let badges exchange simple IR signals with each other. Pads for an optional accelerometer/gyroscope breakout (GY-521 or ADXL345-compatible) were also included. It ran on two AAA batteries and was given out to conference attendees rather than sold.

Antonic published the schematics, firmware source, and Windows/Linux bootloader tools alongside the Hackaday.io project page, with the MPLAB X firmware project hosted on Hack-a-Day's GitHub org.
