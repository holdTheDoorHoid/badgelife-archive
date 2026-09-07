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
summary: A round hackable badge from the Social Engineering Community Village at DEF CON 33, built around an RP2040 with 23 WS2812 LEDs; capacitive touch pads cycle the light-show modes and toggle brightness.
functions: Light Show
look:
  colors:
  - black
  - gold
  - multicolor
  shape: circle
  themes:
  - village badge
  - security
  - logo
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
  where: Per the community sheet, sold only inside the Social Engineering Community Village at DEF CON 33, with proceeds supporting the Village.
make_your_own:
  open_source: partial
  hardware_url: ''
  firmware_url: https://github.com/secommunity/SEC-DEF-CON-33-Oreo-Badge-/blob/main/SEC_OREO.ino
  eda_tool: null
  notes: Firmware is an Arduino sketch (SEC_OREO.ino) plus a prebuilt SEC_OREO_v1.uf2; the repo also includes a 3D-printable display stand STL, a leaflet PDF and a B.A.D.G.E. compliance sheet. The compliance sheet itself marks "BOM and schematic published" as not compliant, so hardware design files are not published; no license file is in the repo.
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
status: announced
sources:
- kind: sheet
  event: dc33
  row: 15
  updated: 7/3/2025 9:03:41
- kind: url
  url: https://github.com/secommunity/SEC-DEF-CON-33-Oreo-Badge-
  title: "secommunity/SEC-DEF-CON-33-Oreo-Badge- (README)"
  accessed: '2026-09-06'
  note: Confirmed MCU (RP2040, Pi Pico clone), LED count/layout/type/GPIO and brightness limit, MPR121 touch on I2C, BQ25895 charger, YDL 3.7V 3000mAh LiPo, USB-C, firmware files (SEC_OREO.ino, SEC_OREO_v1.uf2), STL stand, B.A.D.G.E. compliance sheet stating BOM/schematic are not published; the sketch shows touch pad A cycles animations and pad B toggles brightness. Images are the repo's ExplodedView_sm.png and LEDs_sm.png.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: "Fact-check 2026-09-07 against the maker's repo (README, compliance sheet, SEC_OREO.ino). Corrected open_source from yes to partial and blanked hardware_url because the compliance sheet says BOM/schematic are not published. Dropped the unsupported \"cookie-themed\"/food wording (no maker source says it) and set status back to announced: no source confirms the badge was actually sold at the con. Price ($50), where and proceeds come only from the community sheet (July 2025, pre-con). Quantity and current availability unknown; no license file in the repo."
last_modified_date: '2026-09-07'
---

The O.R.E.O. badge was made by the Social Engineering Community (SEC) for their village at DEF CON 33 in 2025. It is a round badge built on an RP2040 microcontroller (the maker describes the PCB as basically a Pi Pico clone), with a light show driven by 23 addressable WS2812 LEDs: 16 arranged around the outer ring and 7 forming the center "logo." Two capacitive touch pads, read by an MPR121 IC, cycle through the lighting animations and toggle between two brightness levels. Power comes from a 3.7V 3000mAh LiPo battery charged over USB-C through a TI BQ25895 battery management chip, and the badge documents its safety and environmental design choices against the B.A.D.G.E. Framework.

According to the community badge sheet, the badge was to be sold only inside the Social Engineering Community Village at DEF CON 33, with proceeds supporting the Village. SEC published the firmware (an Arduino sketch, SEC_OREO.ino, plus a ready-to-flash SEC_OREO_v1.uf2) and a hacking guide covering the pinout, LED map, and how to write custom lighting modes, along with a 3D-printable display stand. The repository's B.A.D.G.E. compliance sheet states that the BOM and schematic are not published, so the firmware and usage documentation are open but the hardware design files are not.
