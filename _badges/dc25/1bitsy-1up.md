---
title: 1Bitsy 1up
id: dc25-1bitsy-1up
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: Piotr Esden-Tempski
  url: https://hackaday.io/piotr-esden-tempski
  role: ''
- name: Bob Miller
  url: https://hackaday.io/bob-miller
  role: ''
summary: A retro-inspired handheld game console shaped like a Game Boy DMG, worn by its creator as a personal badge at DEF CON 25.
functions: Handheld gaming console with touchscreen UI, D-Pad/ABXY/Start/Select controls, microSD storage, and headphone/speaker audio output.
look:
  colors: []
  shape: rectangle
  themes:
  - retro computer
  - console
  - arcade
tech:
  mcu: STM32F415RGT6
  leds: null
  display: 2.8" TFT LCD (240x320, ILI9341) with capacitive touchscreen
  connectivity: []
  battery: LiPo with onboard charger
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 3
  availability: not_released
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/1bitsy/1bitsy-1up
  firmware_url: https://github.com/1bitsy/1bitsy-1up
  eda_tool: null
links:
- label: hackaday.io/project/25632-1bitsy-1up
  url: https://hackaday.io/project/25632-1bitsy-1up
  kind: hackaday
  archived: https://web.archive.org/web/20260412172838/https://hackaday.io/project/25632-1bitsy-1up
- label: github.com/1bitsy/1bitsy-1up
  url: https://github.com/1bitsy/1bitsy-1up
  kind: repo
images:
- file: assets/images/badges/dc25/1bitsy-1up/28e39cd81d.jpg
  source: https://hackaday.io/project/25632-1bitsy-1up
  credit: Piotr Esden-Tempski
  caption: 1Bitsy 1UP handheld console, Game Boy DMG form factor
  archived: https://web.archive.org/web/20260412172838/https://hackaday.io/project/25632-1bitsy-1up
- file: assets/images/badges/dc25/1bitsy-1up/8bf9cf3cb2.jpg
  source: https://hackaday.io/project/25632-1bitsy-1up
  credit: Piotr Esden-Tempski
  caption: 1Bitsy 1UP assembled prototype
  archived: https://web.archive.org/web/20260412172838/https://hackaday.io/project/25632-1bitsy-1up
contact: {}
notes: []
status: announced
sources:
- kind: url
  url: https://hackaday.io/project/25632-1bitsy-1up
  title: 1Bitsy 1up
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
  archived: https://web.archive.org/web/20260412172838/https://hackaday.io/project/25632-1bitsy-1up
- kind: url
  url: https://hackaday.io/project/25632-1bitsy-1up
  title: 1Bitsy 1UP project page
  accessed: '2026-09-07'
  note: Confirmed maker(s), DEF CON 25 (2017) context, hardware spec (STM32F415RGT6, 2.8in touchscreen LCD, microSD, DAC audio), three prototypes built, GitHub repo link.
  archived: https://web.archive.org/web/20260412172838/https://hackaday.io/project/25632-1bitsy-1up
- kind: url
  url: https://github.com/1bitsy/1bitsy-1up
  title: 1bitsy/1bitsy-1up on GitHub
  accessed: '2026-09-07'
  note: Confirmed hardware and firmware repository is public; no explicit license found, so open_source set to partial rather than yes.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Creator wore three assembled prototypes as a personal badge at DEF CON 25 (2017); no evidence of a wider release, sale, or distribution to other attendees. LED count/type, price, EDA tool, and explicit license not stated in the sources reviewed. GitHub repo exists with hardware and firmware files but no license file was found on the page, so open_source is marked partial rather than confirmed yes.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/1bitsy-1up/
model:
  file: assets/models/dc25/1bitsy-1up.glb
  method: kicad
  source_file: hardware/V0.1/1bitsy-1up.kicad_pcb
  generated: '2026-09-07'
  bytes: 510008
---

The 1Bitsy 1UP is a handheld game console built by Piotr Esden-Tempski (with Bob Miller) in the shape of a Game Boy DMG, created as a personal badge for DEF CON 25 in July 2017. It runs on an STM32F415RGT6 ARM Cortex-M4F processor and pairs a 2.8" capacitive-touch TFT LCD (240x320, ILI9341 driver) with classic D-Pad, ABXY, Start, and Select buttons, a microSD card slot, and onboard DAC audio with headphone and optional speaker output, all powered by a rechargeable LiPo battery.

Only three prototypes were assembled in time for the con, and the creator wore them as a personal badge rather than distributing them to other attendees; the project page expresses hope for a future, more widely available version, but no evidence of that release was found. Hardware and firmware files are published on GitHub, though no explicit open-source license was located on the repository page.
