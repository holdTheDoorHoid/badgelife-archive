---
title: CactusCon 8 Electronic Badge (2019)
id: cactuscon-2019-cactuscon-8-electronic-badge-2019
layout: badge
parent: CactusCon 8 (2019)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cactuscon-2019
year: 2019
makers:
- name: CactusCon
  url: https://github.com/cactuscon/cactuscon8
summary: 'The optional electronic badge for CactusCon 8 (Mesa, AZ, Dec 6-7 2019), built around a TTGO T-Display ESP32 dev board and marketed as a "bio data" collector with a heart-rate/pulse-ox sensor and a 6-axis gyro/accelerometer.'
functions: 'Reads biometric-style sensor data (motion via the MPU-6050, heart rate/blood oxygen via the MAX30102) and shows it on the T-Display''s built-in screen; optional add-ons (thermal IR sensor, gas sensor, piezo speaker, OLED) extended it further.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ESP32 (TTGO T-Display dev board)
  leds: null
  display: TTGO T-Display integrated LCD (optional 0.96" OLED add-on)
  connectivity:
  - wifi
  - ble
  battery: LiPo 1200 mAh (3.7V, 603450 cell)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Distributed as a badge kit tied to CactusCon 8 registration/ticket tier; exact sale terms not documented in recovered sources.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/cactuscon/cactuscon8
  firmware_url: https://github.com/cactuscon/cactuscon8
  eda_tool: KiCad
  gerbers_url: https://github.com/cactuscon/cactuscon8/raw/master/doc/2019CactusCon_PCB.zip
  notes: 'Firmware built for the TTGO T-Display ESP32 board via PlatformIO; assembly instructions in doc/build_the_cactuscon_8_badge.docx.'
links:
- label: badge.gallery/badges/cactuscon-8-electronic-badge
  url: https://badge.gallery/badges/cactuscon-8-electronic-badge
  kind: website
- label: github.com/cactuscon/cactuscon8
  url: https://github.com/cactuscon/cactuscon8
  kind: repo
images:
- file: assets/images/badges/cactuscon-2019/cactuscon-8-electronic-badge-2019/059828eabe.jpg
  source: "https://github.com/cactuscon/cactuscon8"
  credit: "CactusCon"
  caption: "CactusCon 8 badge kit components: PCB, TTGO T-Display ESP32, MPU-6050, MAX30102, battery, lanyard"
contact:
  email: badge@cactuscon.com
  social: 'Twitter: @CactusCon'
notes:
- Official electronic badge for the 8th CactusCon (2019). (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task con-layerone.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/cactuscon-8-electronic-badge
  title: CactusCon 8 Electronic Badge (2019)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''CactusCon 2019''.'
- kind: url
  url: https://github.com/cactuscon/cactuscon8/
  title: 'cactuscon/cactuscon8: Firmware for the CactusCon 8 badge'
  accessed: '2026-09-10'
  note: 'Maker''s own GitHub repo; confirms hardware (TTGO T-Display ESP32, MPU-6050, MAX30102, LiPo battery), KiCad design files, PlatformIO firmware, and assembly doc.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Core hardware and firmware details confirmed by the maker''s own GitHub repo (cactuscon/cactuscon8), which the initial sweep source (badge.gallery) had not recovered. Price, exact quantity made, and precise sale/registration terms are not stated anywhere found and are left blank. The sheet''s original wording ("Official electronic badge for the 8th CactusCon (2019)") is consistent with sources and was kept as the basis for the summary.'
last_modified_date: '2026-09-10'
---

The CactusCon 8 Electronic Badge was the optional electronic badge tier offered at CactusCon's 8th annual event, held December 6-7, 2019 at the Mesa Convention Center in Arizona. Rather than a typical blinky con badge, it was built around a TTGO T-Display ESP32 development board and marketed as a "bio data" collector: an MPU-6050 6-axis gyroscope/accelerometer and a MAX30102 pulse-oximeter/heart-rate sensor came standard in the kit, with optional add-ons (a thermal IR sensor, an MQ-type gas sensor, a piezo speaker, and a 0.96" OLED display) available for further hacking.

The badge kit shipped as a PCB plus the TTGO T-Display board, sensors, headers, a lanyard, an adhesive foam pad, and a 3.7V 1200mAh LiPo battery. CactusCon published the full project — KiCad PCB design files, PlatformIO-based ESP32 firmware, and a Word-document assembly guide — on GitHub at cactuscon/cactuscon8, and invited attendees to build on it and share their hacks via email or Twitter.

Sale price, production quantity, and the exact registration terms for who received the electronic version versus the printed badge were not documented in any source found during this research pass.
