---
title: Blinky Ball (RGB)
id: dc26-blinky-ball-rgb-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Null Space Labs (LA)
  url: https://hackaday.io/project/159292-blinky-ball-rgb
  role: mmca and charliex
summary: A spherical wearable/lamp built from stacked PCB rings holding 384 individually-addressable RGB LEDs, made by mmca and charliex of Null Space Labs (LA) and shown at DEF CON 26 (2018).
functions: Lights up in RGB patterns across 384 LEDs arranged as a sphere; the v2.1 board carries a 9-DoF IMU plus temperature, gesture, light and color sensors, and a microphone with a DAC/headphone jack, all driven over WiFi and Bluetooth from an ESP32.
look:
  colors:
  - multicolor
  shape: sphere
  themes:
  - wearable
tech:
  mcu: ESP-WROOM-32
  leds:
    count: 384
    type: WS2812
    note: 5mm PTH addressable LEDs; v2.1 prototype arranges 20 LEDs per slice across 16 slices
  display: null
  connectivity:
  - wifi
  - bluetooth
  battery: 18650 Li-ion 4000mAh (v2.1 prototype); earliest 2012 monochrome version used an 800mAh cell
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: roughly a dozen of an earlier build, per the project page
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/159292-blinky-ball-rgb
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/159292-blinky-ball-rgb
  url: https://hackaday.io/project/159292-blinky-ball-rgb
  kind: hackaday
  archived: https://web.archive.org/web/20250907230318/https://hackaday.io/project/159292-blinky-ball-rgb
images:
- file: assets/images/badges/dc26/blinky-ball-rgb-badge/c26a1f653a.jpg
  source: https://hackaday.io/project/159292-blinky-ball-rgb
  credit: Null Space Labs
  caption: Blinky Ball RGB sphere lit up
  archived: https://web.archive.org/web/20250907230318/https://hackaday.io/project/159292-blinky-ball-rgb
- file: assets/images/badges/dc26/blinky-ball-rgb-badge/f6fc9a2132.jpg
  source: https://hackaday.io/project/159292-blinky-ball-rgb
  credit: Null Space Labs
  caption: Blinky Ball RGB PCB slice detail
  archived: https://web.archive.org/web/20250907230318/https://hackaday.io/project/159292-blinky-ball-rgb
contact: {}
notes:
- The Hackaday.io page calls it "Blinky Ball (RGB)"; the community sheet appended "Badge" to the title, but the project page never describes it as a con badge — it reads as a personal wearable/lamp piece that the makers demonstrated at DEF CON 26.
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/159292-blinky-ball-rgb
  title: Blinky Ball (RGB) Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 26''.'
  archived: https://web.archive.org/web/20250907230318/https://hackaday.io/project/159292-blinky-ball-rgb
- kind: url
  url: https://hackaday.io/project/159292-blinky-ball-rgb
  title: Blinky Ball (RGB) - Hackaday.io project page
  accessed: '2026-09-07'
  note: Primary source for maker names, components, LED count, history/timeline, and photos.
  archived: https://web.archive.org/web/20250907230318/https://hackaday.io/project/159292-blinky-ball-rgb
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (makers, LEDs, MCU, sensors, event) come from the maker's own Hackaday.io project page, so most fields are solid. Confidence held at medium rather than high because price, quantity sold, and current availability are not stated anywhere on the page, and it is unclear whether this was ever distributed as a wearable con badge versus shown/demoed as an art piece. No independent second source was found to corroborate the DEF CON 26 appearance.
last_modified_date: '2026-09-07'
---

Blinky Ball (RGB) is a spherical LED sculpture/wearable built by mmca and charliex of the LA hackerspace Null Space Labs, using stacked PCB rings as its structure. The current v2.1 prototype carries 384 individually-addressable WS2812 LEDs (20 per slice across 16 slices), an ESP-WROOM-32 for WiFi/Bluetooth control, a Cypress PSOC4 LED driver, a 9-DoF IMU plus temperature, gesture, light and color sensing, and a microphone with a DAC/headphone jack, run off an 18650 cell rated for about four hours per charge.

The project has a long history: it began in 2012 as a monochrome white-LED ball with the same 384-LED count on an 800mAh battery, then a color version was started in 2013 but shelved over cost. It was revived in 2017 as a birthday gift and evolved into the RGB v2.1 board shown here, which the makers demonstrated at DEF CON 26 in 2018. The project page mentions roughly a dozen units of an earlier build and talk of a crowdfunded kit, but does not confirm that a kit ever shipped, so pricing and availability are left blank rather than guessed.

## Make your own

Schematics and board files for several variants (WiFi, Boost, Speaker) are shared on the Hackaday.io project page, but no separate firmware repository was found, so `open_source` is marked `partial`.
