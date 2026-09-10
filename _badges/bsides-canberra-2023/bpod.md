---
title: bPod
id: bsides-canberra-2023-bpod
layout: badge
parent: BSides Canberra 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-canberra-2023
year: 2023
makers:
- name: Peter Rankin (pjranki)
  url: https://gitlab.com/pjranki
summary: An ESP32-S2 electronic badge for BSides Canberra 2023 styled as an homage to the iPod nano, with a touch scroll-wheel interface and a built-in CTF.
functions: Touch scroll-wheel navigation (clockwise/counterclockwise, OK, forward, menu, back, play) drives a modular app-based firmware; ships with seven CTF challenges covering firmware string extraction, UART, I2C, and SPI sniffing, audio watermark extraction, LED binary decoding, and AES reverse engineering.
look:
  colors: []
  shape: rectangle
  themes:
  - retro computer
  - ctf
  - music
tech:
  mcu: ESP32-S2
  leds: RGB, back-mounted; driven from GPIO pins 10, 16, 21
  display: 0.96" ST7735 LCD
  connectivity:
  - usb
  - uart
  - i2c
  battery: none (USB-C powered; no onboard battery as shipped)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Given to BSides Canberra 2023 attendees as the conference badge.
make_your_own:
  open_source: true
  hardware_url: https://gitlab.com/pjranki/bpod
  firmware_url: https://gitlab.com/pjranki/bpod
  eda_tool: KiCad
links:
- label: gitlab.com/pjranki/bpod
  url: https://gitlab.com/pjranki/bpod
  kind: repo
- label: bPod firmware updater
  url: https://bpod.bsidescbr.com.au/update.html
  kind: doc
- label: Pimping my bPod Badge (Bleepity Bloopity)
  url: https://bleepitybloopity.com/posts/bpod-upgrades/
  kind: article
- label: BSides Canberra 2023 badge CTF writeups (h4sh5)
  url: https://github.com/h4sh5/bsidescbr-2023-writeups
  kind: article
images:
- file: assets/images/badges/bsides-canberra-2023/bpod/aadccbb1af.jpg
  source: https://bleepitybloopity.com/posts/bpod-upgrades/
  credit: Peter Rankin (pjranki)
  caption: bPod badge front
- file: assets/images/badges/bsides-canberra-2023/bpod/f73c54ae9a.jpg
  source: https://bleepitybloopity.com/posts/bpod-upgrades/
  credit: Peter Rankin (pjranki)
  caption: bPod case render
contact: {}
notes:
- ESP32-S2 colour-screen BSides Canberra 2023 badge with iPod-style scroll-wheel controls, games and hardware tools; KiCad hardware, firmware, updater and server source published on GitLab. Found by the event-year sweep, task bsides-canberra.
status: released
sources:
- kind: url
  url: https://gitlab.com/pjranki/bpod
  title: bPod
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-canberra); event read as ''BSides Canberra 2023''.'
- kind: url
  url: https://bleepitybloopity.com/posts/bpod-upgrades/
  title: Pimping my bPod Badge
  accessed: '2026-09-10'
  note: Confirmed maker, event/year, iPod-nano design intent, ESP32-S2 MCU, ST7735 display, scroll-wheel UI, RGB LEDs, USB-C, open-source KiCad files; source of the two saved images.
- kind: url
  url: https://github.com/h4sh5/bsidescbr-2023-writeups
  title: Bsides Canberra 2023 Badge challenges writeup
  accessed: '2026-09-10'
  note: Confirmed the badge functioned as the conference badge with a built-in seven-challenge CTF (UART/I2C/SPI, audio watermark, LED, AES); notes some units shipped with different ESP32 variants due to supply constraints.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'No price, quantity made, or post-con availability found; get_one fields for price/quantity left empty. Distribution modeled as "village" (given to attendees) since no purchase/preorder path was described; if it was distributed some other way this should be corrected. Battery: the maker''s own upgrade post says it shipped without one, so tech.battery is recorded as none/USB-C powered.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsides-canberra-2023/bpod.glb
  method: kicad
  source_file: hardware/bpod/bpod.kicad_pcb
  generated: '2026-09-10'
  bytes: 589424
---

The bPod was the badge given to attendees of BSides Canberra 2023, designed by Peter Rankin (pjranki) as an homage to the iPod nano. It pairs an ESP32-S2 with a small ST7735 color LCD and a capacitive touch scroll wheel that echoes the iPod's click wheel, offering clockwise/counterclockwise scrolling plus OK, forward, menu, back, and play controls, alongside RGB LEDs mounted on the back of the board and a USB-C port for power and serial access.

Rather than a single fixed firmware image, the bPod runs a modular, app-based firmware so its scroll-wheel interface can host different mini-programs. The conference built a CTF around the hardware itself: seven challenges asked players to pull strings out of firmware, sniff UART traffic between two bPods, decode I2C and SPI communications, extract an audio watermark, decode a binary LED blink pattern, and reverse an AES routine. Some units reportedly shipped with different ESP32 variants due to chip supply constraints at the time.

Rankin published the complete hardware (KiCad) and firmware source, plus an updater and server, on GitLab, and a companion firmware-updater page was hosted at bpod.bsidescbr.com.au. The badge shipped without a battery; owners who wanted to keep using it after the con documented adding a LiPo cell and charging circuit themselves.
