---
title: Astro-chan Badge
id: other-astro-chan-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2023
makers:
- name: deʃhipu
  url: https://hackaday.io/dehipu
summary: A small wearable badge with a round display that shows an animated astronaut character, reacting to being moved or shaken.
functions: Shows an animated astronaut-girl character on a round screen; the character blinks, reacts to tilting, and responds to shake gestures via an onboard accelerometer.
look:
  colors:
  - black
  - grey
  shape: astronaut
  themes:
  - space
  - anime
  - wearable
tech:
  mcu: Xiao-compatible (ESP32-S3 planned)
  leds:
    count: 2
    type: discrete
    note: Two red LEDs on the astronaut's "gun" accessory
  display: round LCD
  connectivity: []
  battery: 14250 LiPo cell, with power switch
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
- label: hackaday.io/project/192761-astro-chan-badge
  url: https://hackaday.io/project/192761-astro-chan-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260521052452/https://hackaday.io/project/192761-astro-chan-badge
images:
- file: assets/images/badges/other/astro-chan-badge/e63bef191f.jpg
  source: https://hackaday.io/project/192761-astro-chan-badge
  credit: deʃhipu
  caption: The Astro-chan badge with its round display showing the astronaut character
  archived: https://web.archive.org/web/20260521052452/https://hackaday.io/project/192761-astro-chan-badge
- file: assets/images/badges/other/astro-chan-badge/9d5d9f7984.jpg
  source: https://hackaday.io/project/192761-astro-chan-badge
  credit: deʃhipu
  caption: Back of the Astro-chan badge showing the battery holder and dev board footprint
  archived: https://web.archive.org/web/20260521052452/https://hackaday.io/project/192761-astro-chan-badge
contact: {}
notes: []
status: unknown
sources:
- kind: url
  url: https://hackaday.io/project/192761-astro-chan-badge
  title: Astro-chan Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''unknown''.'
  archived: https://web.archive.org/web/20260521052452/https://hackaday.io/project/192761-astro-chan-badge
- kind: url
  url: https://hackaday.io/project/192761-astro-chan-badge
  title: Astro-chan Badge
  accessed: '2026-09-07'
  note: Maker's own project page; confirmed maker, form factor, display, LEDs, battery, accelerometer, and CircuitPython software.
  archived: https://web.archive.org/web/20260521052452/https://hackaday.io/project/192761-astro-chan-badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Made by deʃhipu (hackaday.io/dehipu), posted September 11, 2023. The project page does not say it was made for any specific convention, so it is left under the "other" event rather than corrected. No price, quantity, or availability is stated; no GitHub/hardware repo link was found on the project page. The MCU is described only as a "Xiao-compatible" dev-board footprint, with an ESP32-S3 board mentioned as the intended part; not a confirmed onboard chip.
last_modified_date: '2026-09-07'
---

The Astro-chan Badge is a small wearable piece by hacker "deʃhipu," built around a round display that fills the astronaut character's helmet. The board is designed to plug into a Xiao-compatible development board (the maker mentions an ESP32-S3 board as the intended target) mounted on the back, alongside a footprint for a battery holder and an LIS3DH accelerometer. Two small red LEDs sit on a hand-held "gun" accessory printed alongside the astronaut artwork.

Software for the badge is written in CircuitPython and drives simple animations: the astronaut blinks, reacts when the badge is tilted, and responds to being shaken. The maker's project page frames it as a lightweight, expressive display piece rather than a full-featured conference badge, and does not tie it to any particular event, so it is catalogued here under a general "other" listing rather than a specific convention.

No price, production quantity, or sales channel is mentioned on the project page, and no separate hardware or firmware repository was found, so those fields are left blank pending further sources.
