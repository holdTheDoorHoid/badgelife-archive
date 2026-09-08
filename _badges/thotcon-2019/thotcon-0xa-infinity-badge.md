---
title: THOTCON 0xA / Infinity Badge
id: thotcon-2019-thotcon-0xa-infinity-badge
layout: badge
parent: THOTCON 0xA
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: thotcon-2019
year: 2019
makers:
- name: DePaul University Idea Realization Lab (with THOTCON Infinity)
summary: The official badge for THOTCON 0xA (May 3-4, 2019, Chicago), an ESP32-based board with capacitive touch controls, LEDs, a speaker and a microphone, built as a six-month student project.
functions: Runs a puzzle-challenge firmware for the conference CTF; plays sounds and streams microphone audio via a soundboard, and lights six position-mapped LEDs in response to touch input.
look:
  colors: []
  shape: null
  themes:
  - ctf
  - puzzle
  - security
tech:
  mcu: ESP32
  leds:
    count: 6
    type: discrete
    note: Six individual LEDs mapped to "ears", "eyes", and "mustache" positions on the badge silkscreen art.
  display: none
  connectivity:
  - wifi
  - audio
  inputs:
  - touch
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '1700'
  availability: unknown
  distribution:
  - free_drop
  where: Given to THOTCON 0xA attendees in Chicago, May 3-4, 2019.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/poplicola/Thotcon0xA_Pub
  eda_tool: null
links:
- label: badge.gallery/badges/thotcon-0xa-infinity-badge
  url: https://badge.gallery/badges/thotcon-0xa-infinity-badge
  kind: website
- label: en.wikipedia.org/wiki/THOTCON
  url: https://en.wikipedia.org/wiki/THOTCON
  kind: website
- label: github.com/poplicola/Thotcon0xA_Pub
  url: https://github.com/poplicola/Thotcon0xA_Pub
  kind: repo
- label: metalmancy.tech/blogs/thotcon-0xa
  url: https://metalmancy.tech/blogs/thotcon-0xa/
  kind: website
- label: appsec.wtf/blog/thotcon-0xa
  url: https://appsec.wtf/blog/thotcon-0xa/
  kind: website
images:
- file: assets/images/badges/thotcon-2019/thotcon-0xa-infinity-badge/dce13c9169.jpg
  source: "https://metalmancy.tech/blogs/thotcon-0xa/"
  credit: "metalmancy.tech"
  caption: "Front of the THOTCON 0xA / Infinity badge"
- file: assets/images/badges/thotcon-2019/thotcon-0xa-infinity-badge/5915e7395d.jpg
  source: "https://metalmancy.tech/blogs/thotcon-0xa/"
  credit: "metalmancy.tech"
  caption: "Back of the THOTCON 0xA / Infinity badge"
contact: {}
notes:
- Official 2019 THOTCON conference badge built on a SparkFun ESP32 Thing Dev board with five capacitive touch pads, six LEDs, speaker and microphone, produced in a 1,700-unit run through a six-month DePaul lab collaboration. Found by the event-year sweep, task thotcon-b.
- 'Sweep''s title/wording matched the maker''s own naming; no correction needed.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/thotcon-0xa-infinity-badge
  title: THOTCON 0xA / Infinity Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:thotcon-b); event read as ''thotcon-2019''.'
- kind: url
  url: https://github.com/poplicola/Thotcon0xA_Pub
  title: Thotcon0xA_Pub (poplicola)
  accessed: '2026-09-08'
  note: Maker's own firmware repo; confirms MCU, LED/touch pinout, speaker/mic driver, and that only firmware (not hardware design files) is published.
- kind: url
  url: https://metalmancy.tech/blogs/thotcon-0xa/
  title: THOTCON 0xA blog post
  accessed: '2026-09-08'
  note: Attendee write-up with two photos of the badge (front and back) and description of the CTF puzzle firmware.
- kind: url
  url: https://appsec.wtf/blog/thotcon-0xa/
  title: THOTCON 0xA badge challenge writeup
  accessed: '2026-09-08'
  note: Confirms badge hardware (5 buttons, mic, WiFi antenna, speaker, data matrix barcode on back) and describes the badge-challenge/CTF scoring.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Maker (DePaul Idea Realization Lab) has no dedicated project page found, so core facts (1,700-unit run, six-month build) rest on the badge.gallery listing and press/attendee accounts rather than a primary maker source; no hardware design files (schematic/PCB/gerbers) were found, only firmware. Price and exact distribution details (e.g. whether it required registration) were not stated anywhere found.
last_modified_date: '2026-09-08'
---

The THOTCON 0xA badge, also called the Infinity badge, was the official badge for THOTCON's 10th anniversary conference (0xA), held May 3-4, 2019 in Chicago. It was built by DePaul University's Idea Realization Lab in partnership with THOTCON Infinity, a six-month student project that produced a run of roughly 1,700 units.

The badge is built around a SparkFun ESP32 Thing Dev board and carries five capacitive touch pads (up/down/left/right/select), six LEDs mapped to "ear", "eye", and "mustache" positions in the badge artwork, a speaker, and a microphone with a custom I2S driver. Stock firmware shipped as a puzzle for the conference's badge-hacking CTF: attendees who dug into the code could get the badge to play messages (including one encoded in the NATO phonetic alphabet), and the badge also carried a data-matrix barcode on the back as part of the wider scavenger-hunt-style challenge run over THOTCON's IRC channel.

Hardware design files (schematics, PCB, gerbers) have not surfaced publicly; the maker's GitHub repo publishes only Arduino example firmware, a soundboard sketch, audio-streaming code, and the stock-firmware binaries needed to restore a badge, released without an explicit license.

## Make your own

Firmware examples and the stock-restore images are published at [github.com/poplicola/Thotcon0xA_Pub](https://github.com/poplicola/Thotcon0xA_Pub). To flash: install the Arduino IDE with the ESP32 board package, then use the LED and SoundBoard example sketches in the repo, which document the pinout (touch pads on pins T4/T6/T3/T7/T2, LEDs on pins 21/19/18/17/16/5, speaker on pin 26, microphone on pins 25/23/22). Stock firmware can be restored with `esptool.py` using the bootloader, partition table, and app binaries included in the repo's `bins` folder.
