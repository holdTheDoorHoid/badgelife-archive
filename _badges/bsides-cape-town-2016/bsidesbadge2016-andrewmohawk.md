---
title: BSidesBadge2016 (AndrewMohawk)
id: bsides-cape-town-2016-bsidesbadge2016-andrewmohawk
layout: badge
parent: BSides Cape Town 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-cape-town-2016
year: 2016
makers:
- name: AndrewMohawk
  url: https://github.com/AndrewMohawk
summary: 'A WiFi-connected electronic badge for a 2016 BSides event, built around an ESP8266 with an I2C OLED screen, IR transceiver, and shift-register-driven LEDs.'
functions: 'Scans and lists nearby WiFi networks ("warbadging"), plays Pong and Rock-Paper-Scissors-Lizard-Spock against other badges, tracks completed challenges, exchanges "seen" badge lists with other badges over IR/WiFi, and syncs data with a companion server.'
look:
  colors: []
  shape: null
  themes:
  - wifi
  - radio
  - security
  - ctf
  - puzzle
tech:
  mcu: ESP8266
  leds: null
  display: OLED (I2C, SDA/SCL)
  connectivity:
  - wifi
  - ir
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
  open_source: yes
  hardware_url: https://github.com/AndrewMohawk/BSidesBadge2016/blob/master/BadgePinout.txt
  firmware_url: https://github.com/AndrewMohawk/BSidesBadge2016/tree/master/BSidesBadge2016
links:
- label: github.com/AndrewMohawk/BSidesBadge2016
  url: https://github.com/AndrewMohawk/BSidesBadge2016
  kind: repo
  archived: https://web.archive.org/web/20260907104447/https://github.com/AndrewMohawk/BSidesBadge2016
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/AndrewMohawk/BSidesBadge2016
  title: BSidesBadge2016 (AndrewMohawk)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''BSides 2016''.'
  archived: https://web.archive.org/web/20260907104447/https://github.com/AndrewMohawk/BSidesBadge2016
- kind: url
  url: https://raw.githubusercontent.com/AndrewMohawk/BSidesBadge2016/master/BadgePinout.txt
  title: 'BadgePinout.txt'
  accessed: '2026-09-07'
  note: 'Pin map confirming ESP8266 GPIO layout: I2C OLED screen, IR LED/receiver, shift registers for an LED array, ADC temp sensor, program/reset buttons.'
- kind: url
  url: https://raw.githubusercontent.com/AndrewMohawk/BSidesBadge2016/master/BSidesBadge2016/warbadging.h
  title: 'warbadging.h source'
  accessed: '2026-09-07'
  note: 'Confirms a WiFi network scanner ("warbadging") feature that lists nearby SSIDs, signal strength, and encryption type on the badge screen.'
- kind: url
  url: https://raw.githubusercontent.com/AndrewMohawk/BSidesBadge2016/master/BSidesBadge2016/communication.h
  title: 'communication.h source'
  accessed: '2026-09-07'
  note: 'Confirms HTTP sync with a companion server to exchange lists of badges seen by each badge; obfuscated ("shift"-decoded) payloads.'
- kind: url
  url: https://api.github.com/repos/AndrewMohawk/BSidesBadge2016/contents/BSidesBadge2016
  title: 'Firmware directory listing'
  accessed: '2026-09-07'
  note: 'File names (pong.h, rpssl.h, images.h, screen.h, ShiftRegisters.h) confirm on-badge games and a shift-register LED driver.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The GitHub repo (firmware, a Python client, and a companion server component) is the only source found; there is no maker blog post, storefront, or press coverage, so price, quantity, LED count/type, battery, and which specific BSides city/chapter this was made for are unknown. No photo of the physical badge was found -- the only image on the repo page is GitHub''s auto-generated link-preview screenshot, not a picture of the item. Repo has no releases/tags; last activity per GitHub UI predates this check. status set to released on the assumption a badge with working, checked-in firmware and a pinout doc was built and used, but this is not confirmed by a photo or announcement.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/bsides-2016/bsidesbadge2016-andrewmohawk/
---

AndrewMohawk's BSidesBadge2016 is a WiFi-enabled electronic conference badge built around an ESP8266, with an I2C OLED display, an IR transmitter/receiver pair, and an LED array driven through shift registers. The firmware (published on GitHub along with a Python client and a small companion server) lets badges recognize and log each other, either over IR in person or by syncing "seen" lists with a server over WiFi.

Beyond badge-to-badge tracking, the firmware includes a WiFi network scanner that lists nearby access points with signal strength and encryption type directly on the badge's screen -- a "warbadging" feature in the spirit of wardriving. It also runs two on-board games, Pong and Rock-Paper-Scissors-Lizard-Spock, and tracks a set of completed challenges, suggesting the badge doubled as a light CTF/puzzle piece for whatever 2016 BSides event it was built for.

No maker write-up, storefront listing, or press coverage of this badge turned up; everything here comes from reading the repository's source and its BadgePinout.txt. The specific BSides chapter and city it was made for, along with price, quantity made, LED type/count, and battery details, are not stated anywhere in the repo and are left blank rather than guessed.

## Make your own

The Arduino sketch (`BSidesBadge2016/BSidesBadge2016.ino`) and supporting headers are in the repo's `BSidesBadge2016/` folder, targeting an ESP8266 board. `BadgePinout.txt` in the repo root documents the wiring: TX/RX serial, an I2C OLED on GPIO4/GPIO5, an IR LED and IR receiver, two cascaded shift registers for the LED array, a program button and reset button, and an ADC input noted as a possible temperature sensor. No schematic, PCB Gerbers, or bill of materials were found alongside the firmware.
