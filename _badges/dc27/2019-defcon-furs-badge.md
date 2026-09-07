---
title: 2019 DEFCON Furs Badge
id: dc27-2019-defcon-furs-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: DEFCON Furs
  url: https://dcfurs.com/
summary: A goggle-shaped electronic badge from the DEFCON Furs community for DEF CON 27, built around an STM32L496 running MicroPython with an 18x7 RGB LED matrix and accelerometer.
functions: Scriptable LED-matrix animations (written in Python or loaded as JSON), tap/wakeup detection and orientation sensing via the onboard accelerometer, and a USB REPL for live scripting.
look:
  colors: []
  shape: null
  themes:
  - animal
  - wearable
  - village badge
tech:
  mcu: STM32L496RET6
  leds:
    count: 126
    type: RGB
    note: 18x7 RGB LED matrix, ~64 steps of PWM dimming per color channel, arranged as a goggle shape
  display: LED matrix 18x7
  connectivity:
  - usb
  - i2c
  - bluetooth
  battery: 2x AA or micro-USB
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Made for members of the DEFCON Furs village/community at DEF CON 27; not a general public sale as far as sources show.'
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/defconfurs/dcfurs-badge-dc27
  firmware_url: https://github.com/defconfurs/micropython-dc27
  eda_tool: null
links:
- label: www.strangeparts.com/debugging-the-coolest-def-con-badge
  url: https://www.strangeparts.com/debugging-the-coolest-def-con-badge/
  kind: website
- label: 'GitHub: defconfurs/dcfurs-badge-dc27 (hardware)'
  url: https://github.com/defconfurs/dcfurs-badge-dc27
  kind: repo
- label: 'GitHub: defconfurs/micropython-dc27 (firmware)'
  url: https://github.com/defconfurs/micropython-dc27
  kind: repo
- label: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
- label: DEFCON Furs
  url: https://dcfurs.com/
  kind: website
images:
  - file: assets/images/badges/dc27/2019-defcon-furs-badge/cb2dfff846.jpg
    source: "https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/"
    credit: "Hackaday / DEFCON Furs"
    caption: "Front view of the DC Furs DC27 badge, LED goggle matrix"
  - file: assets/images/badges/dc27/2019-defcon-furs-badge/24c0c8b6a8.jpg
    source: "https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/"
    credit: "Hackaday / DEFCON Furs"
    caption: "Rear view of the DC Furs DC27 badge"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.strangeparts.com/debugging-the-coolest-def-con-badge/
  title: 2019 DEFCON Furs Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc27''.'
- kind: url
  url: https://github.com/defconfurs/dcfurs-badge-dc27
  title: 'GitHub - defconfurs/dcfurs-badge-dc27: DEFCON Furs Badge Software for DC27 (2019)'
  accessed: '2026-09-07'
  note: Confirms MCU (STM32L496RET6), LED matrix, accelerometer, power options, SAO v1.69bis I2C bus, and MIT open-source hardware/firmware.
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27
  accessed: '2026-09-07'
  note: Design description (goggle-shaped LED array, faceplate diffuser PCB) and source of front/rear photos.
- kind: url
  url: https://dcfurs.com/
  title: DEFCON Furs
  accessed: '2026-09-07'
  note: Maker/community homepage.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core specs confirmed via the maker''s own GitHub hardware/firmware repos and a Hackaday roundup; the Strange Parts debugging livestream page named LoialOtter as a contributor providing technical support. Price, quantity made, and general public availability were not found in any source checked; this appears to have been made for the DEFCON Furs village community rather than sold on a public storefront. Continues a series with the DC26 (2018) badge (github.com/defconfurs/dc26-fur-scripts) and later DC30/31/32 DEFCON Furs badges already in the archive.'
last_modified_date: '2026-09-07'
---

The 2019 DEFCON Furs badge was built by the DEFCON Furs community for DEF CON 27's furry-fandom village. It carries on the group's goggle-shaped LED array from the previous year's badge, but split the design so a plain host PCB (with the STM32L496RET6 microcontroller, an 18x7 RGB LED matrix, and an LIS2DE12 accelerometer) sits underneath a separate faceplate PCB that diffuses the LEDs and gives each badge its own decorated look.

The badge runs MicroPython, letting owners write their own animations in Python or load them as JSON over a USB REPL, and the accelerometer supports tap/wakeup detection as well as orientation sensing. It can run off two AA batteries or micro-USB power, includes a Bluetooth module (Fanstel BT832A) and 32 Mbit of SPI flash, and exposes an I2C add-on port built to the badgelife v1.69bis "Shitty Addon" standard. A public debugging livestream covered by Strange Parts, with DC Furs member LoialOtter providing technical support, also surfaced a puzzle element hidden under the battery holder.

## Make your own

Both the hardware and MicroPython firmware are published under an open-source license. Hardware design files are at [github.com/defconfurs/dcfurs-badge-dc27](https://github.com/defconfurs/dcfurs-badge-dc27) (see its `doc/ASSEMBLY.md` for build steps), and the firmware fork is at [github.com/defconfurs/micropython-dc27](https://github.com/defconfurs/micropython-dc27).

## History

This badge follows a 2018 (DC26) DEFCON Furs badge (`github.com/defconfurs/dc26-fur-scripts`) with a similar goggle-array concept, and the community continued the line with badges in later years, some of which already have their own entries in this archive (DC30 "Cereal Booper", DC31 "Vixy", DC32).
