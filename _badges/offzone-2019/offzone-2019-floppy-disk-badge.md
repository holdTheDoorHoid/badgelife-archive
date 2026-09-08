---
title: OFFZONE 2019 Floppy Disk Badge
id: offzone-2019-offzone-2019-floppy-disk-badge
layout: badge
parent: OFFZONE 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: offzone-2019
year: 2019
makers:
- name: BI.ZONE
  url: https://bi.zone/
summary: 'A PCB badge shaped like a 3.5-inch floppy disk, made for OFFZONE 2019 and doubling as a wallet for the event''s in-game currency, Offcoin.'
functions: 'Holds and spends Offcoin, the event''s internal currency, at an on-site soldering station (Craft.Zone) to unlock add-on modules: an RFID/NFC reader for reading attendee cards, and a 433 MHz radio receiver for staff broadcast messages and inter-attendee messaging. Shows status on a 0.96" OLED.'
look:
  colors:
  - green
  - white
  shape: rectangle
  themes:
  - retro computer
  - security
  - radio
  - puzzle
tech:
  mcu: STM32F1
  leds:
    count: null
    type: WS2812B
    note: 'WS2812B RGB addressable LEDs; article says 8,000 LED units were ordered for the run of 2,000 badges (implying several per badge), exact per-badge count not stated.'
  display: 0.96" OLED
  connectivity:
  - rfid
  - nfc
  - sub-ghz
  - ir
  battery: 4x AAA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '2,000 (plus prototypes v1.0-v3.1); 100 surplus units later offered to Habr readers'
  availability: unknown
  distribution:
  - free_drop
  where: 'Given to OFFZONE 2019 attendees; components were unlocked by earning and spending Offcoin at the Craft.Zone soldering station. 100 surplus units were later offered by BI.ZONE to Habr readers via email.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: habr.com/ru/companies/bizone/articles/460631
  url: https://habr.com/ru/companies/bizone/articles/460631/
  kind: article
- label: habr.com/ru/articles/707392
  url: https://habr.com/ru/articles/707392/
  kind: article
images:
- file: assets/images/badges/offzone-2019/offzone-2019-floppy-disk-badge/3eb2e1e3ba.jpg
  source: "https://habr.com/ru/companies/bizone/articles/460631/"
  credit: "BI.ZONE"
  caption: "OFFZONE 2019 floppy-disk badges worn on lanyards by conference visitors"
- file: assets/images/badges/offzone-2019/offzone-2019-floppy-disk-badge/83bdd7a14e.jpg
  source: "https://habr.com/ru/companies/bizone/articles/460631/"
  credit: "BI.ZONE"
  caption: "Bare OFFZONE 2019 floppy-disk badge PCB, shaped like a 3.5-inch floppy disk with RFID, OLED and 433 MHz radio sections labeled"
contact: {}
notes:
- First PCB-format OFFZONE badge, shaped like a floppy disk with a retro theme; attendees earned in-game 'Offcoin' currency to buy add-on components including an NFC reader module and a radio message module. Found by the event-year sweep, task con-phdays.
- 'Title as the sweep recorded it matches BI.ZONE''s own description (a floppy-disk-shaped badge); no alternate maker name found.'
status: released
sources:
- kind: url
  url: https://habr.com/ru/companies/bizone/articles/460631/
  title: OFFZONE 2019 Floppy Disk Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2019''.'
- kind: url
  url: https://habr.com/ru/companies/bizone/articles/460631/
  title: 'BI.ZONE blog: OFFZONE 2019 badge write-up'
  accessed: '2026-09-08'
  note: 'Primary source: STM32F1 MCU, 0.96" OLED, WS2812B LEDs (8,000 ordered), RFID reader, IR receiver, 433 MHz transceiver, 4x AAA power, 2,000 units built (2 defective), 100 surplus offered to readers.'
- kind: url
  url: https://habr.com/ru/articles/707392/
  title: 'Habr retrospective on OFFZONE badges'
  accessed: '2026-09-08'
  note: 'Confirms floppy-disk shape was first PCB badge; describes Offcoin currency mechanic and NFC/radio add-on modules unlocked via soldering.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, event, chip, display, LEDs, radios, power, quantity) confirmed by BI.ZONE''s own Habr blog post. Exact per-badge LED count, price (it was a free attendee item, not sold), open-source status, and design file links were not stated in either source and are left empty. No storefront or repo found.'
last_modified_date: '2026-09-08'
---

BI.ZONE built this badge for OFFZONE 2019, its Moscow security conference, shaping the PCB like a 3.5-inch floppy disk to fit that year's retro-computing theme. It was the first PCB-format badge OFFZONE had done. Each badge doubled as a wallet for Offcoin, an in-game currency attendees earned during the event and spent at the on-site Craft.Zone soldering station to unlock and solder on additional components — an RFID/NFC reader and a 433 MHz radio module — progressively adding functions as pieces were added.

Under the hood the badge ran an STM32F1 (Blue Pill-style) microcontroller programmed via the Arduino IDE with an STM32Duino bootloader, drove a 0.96" OLED status display, and lit WS2812B addressable RGB LEDs (BI.ZONE ordered 8,000 LED units for the run). It also carried an 8-position DIP switch, an IR receiver, and ran on four AAA batteries for roughly 16-20 hours. A two-person electronics team designed and iterated the board (prototypes v1.0 through v3.1) in 80 days, then had 2,000 units built by contract assembler M-plata in about a week, with all 2,000 flashed by hand; only two units came back defective. About 100 surplus badges were later offered by BI.ZONE to readers of its Habr blog post.

No public repository, Gerbers, or firmware release was found for this badge, and no price is listed since it was a free-drop item given to conference attendees rather than sold.
