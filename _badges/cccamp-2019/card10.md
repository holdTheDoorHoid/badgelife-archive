---
title: card10
id: cccamp-2019-card10
layout: badge
parent: CCCamp19
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cccamp-2019
year: 2019
makers:
- name: Chaos Computer Club community
  url: https://card10.badge.events.ccc.de/
summary: 'card10 is the official electronic badge of Chaos Communication Camp 2019, a wrist-worn "sensor playground" built around biosensing (ECG, pulse) rather than the usual LED blinkiness.'
functions: 'Watch-face UI with a menu system, Bluetooth Low Energy pairing and companion apps, an on-device app store ("Hatchery"), ECG and optical pulse sensing, environmental sensing, and addressable RGB LED effects.'
look:
  colors: [black, multicolor]
  shape: rectangle
  themes: [wearable, hardware tool, measurement, radio]
tech:
  mcu: MAX32666
  leds:
    count: 15
    type: SK9822-2020
    note: 11 RGB LEDs facing up, 4 RGB LEDs facing down
  display: 0.96" IPS LCD (ST7735, 80x160)
  connectivity: [ble, usb, uart]
  battery: LiPo 200 mAh
  sao_version: null
get_one:
  price: 'not sold'
  price_usd: null
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: Distributed to attendees of Chaos Communication Camp 2019; not sold ("No sale of card10s!"). A post-event card10 exchange point helped attendees swap for one.
make_your_own:
  open_source: yes
  hardware_url: https://git.card10.badge.events.ccc.de/card10/hardware
  firmware_url: https://git.card10.badge.events.ccc.de/card10/firmware
  eda_tool: null
links:
- label: card10.badge.events.ccc.de
  url: https://card10.badge.events.ccc.de/
  kind: website
  archived: https://web.archive.org/web/20260714144323/https://card10.badge.events.ccc.de/
- label: card10 Firmware Documentation
  url: https://firmware.card10.badge.events.ccc.de/
  kind: doc
  archived: null
- label: card10 GitLab (Hardware)
  url: https://git.card10.badge.events.ccc.de/card10/hardware
  kind: repo
  archived: null
- label: card10 GitLab (Firmware)
  url: https://git.card10.badge.events.ccc.de/card10/firmware
  kind: repo
  archived: null
- label: 'Hackaday: card10 badge coverage'
  url: https://hackaday.com/tag/card10/
  kind: article
  archived: null
images:
  - file: assets/images/badges/cccamp-2019/card10/a3d7eb06b3.jpg
    source: "https://card10.badge.events.ccc.de/userguide/assembly/"
    credit: "card10 community"
    caption: "card10 badge assembled and worn as a wristband"
  - file: assets/images/badges/cccamp-2019/card10/be93ba14d7.jpg
    source: "https://card10.badge.events.ccc.de/"
    credit: "card10 community"
    caption: "card10 default watch-face display"
contact: {}
notes:
- Named from Greek kardía ('heart'); ECG sensor, optical pulse sensor, BLE, IMU+magnetometer, environmental sensor, watch-face UI; ongoing firmware releases post-event (e.g. 'Queer Quinoa' 2021).
- Also used at subsequent events (rC3 2020/2021 online congress had a dedicated card10 assembly); made for CCCamp 2019 originally.
- Price/quantity not stated on the maker's site; badge was distributed to attendees rather than sold, and exact production numbers were not found.
status: released
sources:
- kind: url
  url: https://card10.badge.events.ccc.de/
  title: card10
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''Chaos Communication Camp 2019''.'
  archived: https://web.archive.org/web/20260714144323/https://card10.badge.events.ccc.de/
- kind: url
  url: https://card10.badge.events.ccc.de/hardware/
  title: card10 Hardware
  accessed: '2026-09-07'
  note: 'Confirmed MCU (MAX32666 dual-core Cortex-M4F @96MHz, 512kB RAM, 1MB flash + 8MB external storage), display (0.96" ST7735 IPS LCD, 80x160), battery (200 mAh LiPo), and LED count/type (11 up + 4 down, SK9822-2020).'
- kind: url
  url: https://card10.badge.events.ccc.de/userguide/assembly/
  title: card10 Assembly
  accessed: '2026-09-07'
  note: Source of the assembled wristband photo used in this entry.
- kind: url
  url: https://firmware.card10.badge.events.ccc.de/overview.html
  title: card10 Firmware Overview
  accessed: '2026-09-07'
  note: Confirmed sensor list (MAX30001 ECG, MAX86150 pulse, BHI160 sensor fusion, BME680 environmental), Neopixel/BLE/USB support.
- kind: url
  url: https://card10.badge.events.ccc.de/faq/tldr/
  title: card10 FAQ tl;dr
  accessed: '2026-09-07'
  note: Confirmed open-source hardware and firmware GitLab repo links and the Hatchery app store.
- kind: url
  url: https://hackaday.com/tag/card10/
  title: 'Hackaday: card10 coverage'
  accessed: '2026-09-07'
  note: Confirmed MAX30001/MAX86150 ECG sensors, USB-C electrode kit accessory, and general description as a wearable sensor playground.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own site and firmware docs confirmed core hardware facts. Price/quantity-made not published anywhere found; badge was given to attendees rather than sold. EDA tool for the hardware repo was not confirmed from the pages read.'
last_modified_date: '2026-09-07'
---

card10 was the official electronic badge of the Chaos Communication Camp 2019, built by the Chaos Computer Club community as a wrist-worn device centered on biosensing rather than typical badge blinkiness. Its name comes from the Ancient Greek *kardía* ("heart"), reflecting its focus: an ECG sensor (MAX30001) and an optical pulse sensor (MAX86150) sit alongside a 9-axis IMU with magnetometer (BHI160) and an environmental sensor (BME680). A dual-core MAX32666 (Cortex-M4F, 96 MHz) drives a 0.96" ST7735 color IPS LCD watch-face, Bluetooth Low Energy connectivity, and 15 addressable RGB LEDs (11 facing up, 4 facing down) powered by a 200 mAh LiPo battery.

card10 was not sold — it was distributed to Camp attendees, with a post-event "card10 exchange point" helping people who missed out find one. Both hardware and firmware are open source, hosted on the project's own GitLab instance, and the badge saw continued firmware development well past the 2019 event, including a "Queer Quinoa" release in 2021 and use at the rC3 online congress. Attendees built their own apps for it through "Hatchery," a badge.team-based on-device app store, and a €10 accessory kit let people solder electrode pads onto a USB-C cable for DIY bioelectric experiments — one hacker reportedly used it to detect eye movement via temple electrodes.

Price and total production quantity were not published on the maker's site or in the sources reviewed for this entry.
