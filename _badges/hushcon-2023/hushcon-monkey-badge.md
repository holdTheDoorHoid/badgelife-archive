---
title: Monkey Badge
id: hushcon-2023-hushcon-monkey-badge
layout: badge
parent: HushCon West 2023 (Winter)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hushcon-2023
year: 2023
makers:
- name: PacketChat
  url: http://packetchat.com/
summary: A MicroPython-powered badge for HushCon West 2023 built around the three wise monkeys, with an onboard FM radio receiver and over-the-air firmware updates that unlocked new challenges through the event.
functions: Runs a series of puzzles and challenges tied to a FastAPI/Redis backend; attendees plug in earphones to catch clues hidden in a tuned FM broadcast, and completing a challenge triggers an over-the-air firmware update that starts the next one. Badges also pair over IR to trade emotes and hidden-object/"monkey" secret codes.
look:
  colors: []
  shape: null
  themes:
  - animal
  - radio
  - security
  - puzzle
  - ctf
tech:
  mcu: ESP32
  leds: null
  display: 0.96" OLED (128x64, I2C)
  connectivity:
  - wifi
  - ir
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: '400'
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/PacketChat/MonkeyBadge
  eda_tool: null
links:
- label: github.com/PacketChat/MonkeyBadge
  url: https://github.com/PacketChat/MonkeyBadge
  kind: repo
- label: packetchat.com — The Monkey Badge
  url: http://packetchat.com/monkey-badge.html
  kind: website
- label: packetchat.com
  url: http://packetchat.com/
  kind: website
- label: delayedpackets.net — MonkeyBadge
  url: https://www.delayedpackets.net/projects/monkeybadge/
  kind: article
images:
- file: assets/images/badges/hushcon-2023/hushcon-monkey-badge/81fdb88905.jpg
  source: "http://packetchat.com/monkey-badge.html"
  credit: "PacketChat"
  caption: "The Monkey Badge with its LEDs lit"
- file: assets/images/badges/hushcon-2023/hushcon-monkey-badge/fca5b70e9b.jpg
  source: "http://packetchat.com/monkey-badge.html"
  credit: "PacketChat"
  caption: "The Monkey Badge with its LEDs off, showing the three-monkeys artwork"
contact: {}
notes:
- 'The discovery sweep filed this under the title "HushCon Monkey Badge"; the maker calls it simply "The Monkey Badge" or "Monkey Badge" (repo name MonkeyBadge).'
- HushCon West 2023 badge (400 made) claimed as the first cyber-conference badge with a built-in FM radio receiver and over-the-air firmware updates. Found by the event-year sweep, task con-toorcon.
status: released
sources:
- kind: url
  url: https://github.com/PacketChat/MonkeyBadge
  title: HushCon Monkey Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-toorcon); event read as ''HushCon West/Winter 2023''.'
- kind: url
  url: http://packetchat.com/
  title: 'PacketChat: Custom Conference Badges And More'
  accessed: '2026-09-08'
  note: Maker's own site; confirms 400 units made for HushCon West, December 2023, and that designs/firmware are released open source after the con.
- kind: url
  url: http://packetchat.com/monkey-badge.html
  title: 'The Monkey Badge: PacketChat'
  accessed: '2026-09-08'
  note: Maker's product page; three-monkeys theme, FM radio clue broadcast, OTA firmware unlocking new challenges per puzzle solved; source of both photos.
- kind: url
  url: https://raw.githubusercontent.com/PacketChat/MonkeyBadge/main/badge/config.py
  title: MonkeyBadge badge/config.py
  accessed: '2026-09-08'
  note: Firmware source confirms ESP32 (esp32.NVS), 128x64 I2C OLED, four buttons, IR opcodes for badge-to-badge pairing/emotes, and two SAO GPIO headers.
- kind: url
  url: https://www.delayedpackets.net/projects/monkeybadge/
  title: MonkeyBadge - delayedpackets
  accessed: '2026-09-08'
  note: Independent project page by builder Ken Williams (delayedpackets), corroborates MicroPython firmware and FastAPI+Redis backend; no new hardware specs.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Maker''s own site and firmware source confirm the badge is real, was made for HushCon West 2023 (400 units), and give MCU/display/connectivity details. Price, per-unit availability/distribution method, LED count/type, battery, and hardware design files (schematics/gerbers) were not found published anywhere; PacketChat''s site says designs are released "once the conference is over" but no hardware repo or files could be located beyond the firmware/software repo. Confidence kept at medium since no third-party press coverage was found to corroborate the "first FM radio + OTA badge" claim beyond the maker''s own site.'
last_modified_date: '2026-09-08'
---

The Monkey Badge was made by PacketChat, a small Northern California electronics shop, for HushCon West in December 2023 — 400 units were produced. It runs MicroPython on an ESP32 with a 128x64 I2C OLED display and four buttons, and its artwork riffs on the three wise monkeys (see no evil, hear no evil, speak no evil), rendered as a monkey in sunglasses, one in headphones, and one in a mask.

The badge's signature feature was pairing an onboard FM radio receiver with over-the-air firmware updates: attendees plugged earphones into the badge to pick up clues from a specially tuned broadcast, and solving each puzzle pushed a firmware update that unlocked the next challenge. Badges could also exchange IR signals with each other for peer-to-peer emotes and hidden-object/"monkey" pairing codes, and each carries SAO GPIO headers for add-ons. A FastAPI-and-Redis backend tracked challenge state and scores across the event.

PacketChat has published the badge and backend software (badge firmware, API server, and Flask scoreboard) on GitHub, and says on its own site that it releases full designs for its badges once each conference wraps — but no hardware schematics, board files, or BOM for the Monkey Badge could be found published, so hardware openness is marked partial pending those files surfacing.
