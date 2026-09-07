---
title: O.R.E.O.
id: dc33-o-r-e-o
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Social Engineering Community Village
  url: https://github.com/secommunity
summary: A round, cookie-themed hackable badge from the Social Engineering Community Village at DEF CON 33, built around an RP2040 with touch-controlled LED light shows.
functions: Light Show
look:
  colors:
  - black
  - multicolor
  shape: circle
  themes:
  - food
  - village badge
  - security
tech:
  mcu: RP2040
  leds:
    count: 23
    type: WS2812
    note: 16 LEDs around the outer ring, 7 in the center "logo"; driven from GPIO 2, max recommended brightness 179/255
  display: none
  connectivity:
  - usb
  - i2c
  inputs:
  - capacitive
  battery: LiPo 3.7V 3000mAh (YDL brand), charged via USB-C through a TI BQ25895
  sao_version: none
get_one:
  price: $50
  price_usd: 50.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold only inside the Social Engineering Community Village at DEF CON 33; proceeds went to support the Village.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/secommunity/SEC-DEF-CON-33-Oreo-Badge-
  firmware_url: https://github.com/secommunity/SEC-DEF-CON-33-Oreo-Badge-/blob/main/SEC_OREO.ino
  eda_tool: null
  notes: Firmware is an Arduino sketch (SEC_OREO.ino) plus a prebuilt SEC_OREO_v1.uf2; repo also includes a 3D-printable display stand STL and a compliance sheet, but no explicit hardware design files (schematic/Gerbers) or license file were found in the repo.
links:
- label: github.com/secommunity/SEC-DEF-CON-33-Oreo-Badge-
  url: https://github.com/secommunity/SEC-DEF-CON-33-Oreo-Badge-
  kind: repo
images:
- file: assets/images/badges/dc33/o-r-e-o/d535f5dc10.png
  source: "https://github.com/secommunity/SEC-DEF-CON-33-Oreo-Badge-"
  credit: "Social Engineering Community (SEC)"
  caption: "Exploded view of the O.R.E.O. badge PCB and enclosure"
- file: assets/images/badges/dc33/o-r-e-o/2ea3578e64.png
  source: "https://github.com/secommunity/SEC-DEF-CON-33-Oreo-Badge-"
  credit: "Social Engineering Community (SEC)"
  caption: "LED map showing the 16 outer-ring and 7 center-logo WS2812 LEDs"
contact:
  emails:
  - brentdukes+SECOreo@gmail.com
notes:
- Will be available only inside the Social Engineering Community Village. Proceeds contribute towards the Village, code will be posted on GitHub before the con.
status: released
sources:
- kind: sheet
  event: dc33
  row: 15
  updated: 7/3/2025 9:03:41
- kind: url
  url: https://github.com/secommunity/SEC-DEF-CON-33-Oreo-Badge-
  title: "secommunity/SEC-DEF-CON-33-Oreo-Badge- (README)"
  accessed: '2026-09-06'
  note: Confirmed MCU (RP2040), LED count/layout, touch controller (MPR121), battery management IC (BQ25895), battery spec, firmware/hardware files, and B.A.D.G.E. compliance framework.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core technical facts confirmed directly from the maker's GitHub repo README and B.A.D.G.E. compliance sheet. Quantity made, exact availability status as of today, and whether hardware design files (schematic/Gerbers, not just firmware and an STL) are published could not be confirmed; no LICENSE file was found in the repo. Price ($50) is carried over from the original community sheet and was not independently re-confirmed by a maker source.
last_modified_date: '2026-09-06'
---

The O.R.E.O. badge was made by the Social Engineering Community (SEC) for their village at DEF CON 33 in 2025. It is a round, cookie-themed wearable badge built on an RP2040 microcontroller (effectively a Raspberry Pi Pico clone), with a light show driven by 23 addressable WS2812 LEDs: 16 arranged around the outer ring and 7 forming the center "logo." Capacitive touch controls, handled by an MPR121 IC, let the wearer switch between lighting modes. Power comes from a 3.7V 3000mAh LiPo battery charged over USB-C through a TI BQ25895 battery management chip, and the badge documents its safety and environmental design choices against the B.A.D.G.E. Framework.

The badge was sold only inside the Social Engineering Community Village at DEF CON 33, with proceeds supporting the Village. SEC published the firmware (an Arduino sketch, SEC_OREO.ino, plus a ready-to-flash SEC_OREO_v1.uf2) and a hacking guide covering the pinout, LED map, and how to write custom lighting modes, along with a 3D-printable display stand. The repository does not appear to include separate schematic or Gerber files, so while the firmware and usage documentation are open, full hardware design files were not found.
