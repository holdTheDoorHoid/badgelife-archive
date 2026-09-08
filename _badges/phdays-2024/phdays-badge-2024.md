---
title: PHDays Badge (2024)
id: phdays-2024-phdays-badge-2024
layout: badge
parent: Phdays Fest 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: phdays-2024
year: 2024
makers:
- name: Positive Labs / Positive Technologies
summary: An interactive badge with a 10x10 pixel LED display that connects over its own Wi-Fi network so wearers can upload custom images and animations.
functions: 'Displays a set of pre-loaded pixel-art images/animations on its 10x10 LED matrix; broadcasts its own Wi-Fi network with a web UI for drawing and uploading custom images/animations; plays RTTTL melodies through a built-in RTTTL editor.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ESP32
  leds:
    count: 100
    type: null
    note: 10x10 matrix (~100 LEDs) behind light guides, a diffusing film, and a darkening screen for a pixel-perfect look
  display: LED matrix 10x10
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'nearly 1,000'
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of PHDays Fest 2 (May 2024); the team hand-flashed all units due to production timeline constraints.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Ushinbuy/PHD_Badge_2025
  firmware_url: https://github.com/nlef/PHDays-Badge
  eda_tool: null
links:
- label: github.com/nlef/PHDays-Badge
  url: https://github.com/nlef/PHDays-Badge
  kind: repo
- label: habr.com/ru/companies/pt/articles/890296
  url: https://habr.com/ru/companies/pt/articles/890296/
  kind: article
- label: github.com/nlef/PHDays-Badge-WebUI
  url: https://github.com/nlef/PHDays-Badge-WebUI
  kind: repo
images:
- file: assets/images/badges/phdays-2024/phdays-badge-2024/336357ba31.png
  source: "https://github.com/nlef/PHDays-Badge"
  credit: "Positive Labs"
  caption: "PHDays Badge (2024) with 10x10 LED display"
- file: assets/images/badges/phdays-2024/phdays-badge-2024/6114941d9f.jpg
  source: "https://habr.com/ru/companies/pt/articles/890296/"
  credit: "Positive Labs / Positive Technologies"
  caption: "The badge lit up on the night of the event"
contact: {}
notes:
- Interactive badge with a 10x10 pixel LED display, Wi-Fi image/animation upload, melody playback and RTTTL editor, made for PHDays Fest 2 (May 2024). Found by the event-year sweep, task con-phdays.
status: released
sources:
- kind: url
  url: https://github.com/nlef/PHDays-Badge
  title: PHDays Badge (2024)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''PHDays Fest 2 2024''.'
- kind: url
  url: https://github.com/nlef/PHDays-Badge
  title: nlef/PHDays-Badge (README)
  accessed: '2026-09-08'
  note: 'Firmware source repo README; confirms maker, 10x10 display, Wi-Fi upload, RTTTL melodies/editor; links a separate WebUI repo and a 3D-models repo (used for the follow-up 2025 badge).'
- kind: url
  url: https://habr.com/ru/companies/pt/articles/890296/
  title: 'Badge From Scratch – Problem Driven Development (Habr, Positive Technologies company blog)'
  accessed: '2026-09-08'
  note: 'Maker''s own dev-diary write-up of the PHDays Fest 2 (May 2024) badge project: confirms ESP32 MCU, ~100-LED 10x10 matrix construction, Wi-Fi drawing tool, ~1000 units made and hand-flashed, planned IR/sound features cut for time; links back to the GitHub repo above.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts confirmed by the maker''s own GitHub repo and a detailed Positive Technologies company-blog write-up on Habr. Exact battery spec, LED part number, PCB color, and price were not stated anywhere found (this was a free con giveaway, not sold). The GitHub repo''s README also references “PHD_Badge_2025 models” — a follow-up badge for PHDays Fest 2025, which has its own entry (phdays-2025-phdays-badge-2025); firmware/hardware appear to be shared or iterated across both years, so open_source is marked partial (firmware repo is public; the linked hardware/3D-model repo is for the 2025 revision, not confirmed identical to the 2024 board).'
last_modified_date: '2026-09-08'
---

The PHDays Badge (2024) is an interactive con badge made by Positive Labs, the R&D arm of Positive Technologies, for PHDays Fest 2 in May 2024. Built around an ESP32, it drives a 10x10 pixel LED display — roughly 100 LEDs behind light guides, a diffusing film, and a darkened front screen for a clean pixel-art look. The badge broadcasts its own Wi-Fi network; attendees could connect with a phone or laptop and use a browser-based tool to draw and upload their own images and animations, on top of a set of pre-loaded pictures. It also plays RTTTL ringtone-format melodies through a built-in melody editor.

Positive Labs made nearly 1,000 units for the festival and gave them out free to attendees, running into enough production and firmware delays that the team ended up hand-flashing every badge before the event. Originally planned features — an infrared port and additional sound hardware — were cut for time and never shipped. The team wrote up the whole process, warts and all, in a company-blog "dev diary" post on Habr.

Firmware for the badge is open source on GitHub (nlef/PHDays-Badge), with a separate repository for the web-based drawing UI. The same firmware repo's README points to a 3D-model repository built for a follow-up badge made for PHDays Fest 2025, which has its own catalog entry; it is not confirmed whether that later hardware design is identical to the 2024 board.
