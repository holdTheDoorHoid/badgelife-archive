---
title: Iron Man SAO
id: dc26-iron-man-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: Twinkle Twinkie
  url: https://hackaday.io/twinkletwinkie
summary: A last-minute Iron Man themed Shitty Add-On that Twinkle Twinkie produced in a small handful for DEF CON 26, shaped like the Iron Man Mark III helmet with light-up eyes.
functions: Lights up the helmet's eye slits with LEDs.
look:
  colors: [red, gold]
  shape: robot
  themes: [pop culture, movie, sci-fi]
tech:
  mcu: null
  leds:
    count: 2
    type: reverse-mount
    note: "Two LEDs light the helmet's eye slits from behind, visible lit blue/white in the maker's project photo; count and type inferred from the photo, not stated explicitly on the project page."
  display: null
  connectivity: [i2c]
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: small handful
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/161120-iron-man-sao
  firmware_url: null
  gerbers_url: https://cdn.hackaday.io/files/1611206893358080/Iron_Man_hackaday.zip
  eda_tool: KiCad
links:
- label: hackaday.io/project/161120-iron-man-sao
  url: https://hackaday.io/project/161120-iron-man-sao
  kind: hackaday
- label: cdn.hackaday.io/files/1611206893358080/Iron_Man_hackaday.zip
  url: https://cdn.hackaday.io/files/1611206893358080/Iron_Man_hackaday.zip
  kind: hackaday
images:
- file: assets/images/badges/dc26/iron-man-sao/d8254b3324.jpg
  source: "https://hackaday.io/project/161120-iron-man-sao"
  credit: "TwinkleTwinkie"
  caption: "Iron Man SAO project photo"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/161120-iron-man-sao
  title: Iron Man SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/161120-iron-man-sao
  title: Iron Man SAO
  accessed: '2026-09-07'
  note: "Confirmed maker (TwinkleTwinkie), event (DEF CON 26, 2018), that it was a small last-minute run, and that KiCad/Gerber files are published in a downloadable zip. Photo shows an Iron Man Mark III helmet-shaped board with two illuminated eye slits."
- kind: url
  url: https://cdn.hackaday.io/files/1611206893358080/Iron_Man_hackaday.zip
  title: Iron_Man_hackaday.zip
  accessed: '2026-09-07'
  note: "Verified the archive contains KiCad Gerber files (copper and soldermask layers) and a footprint library table, confirming open hardware files are genuinely published."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: "The Hackaday.io project page (the only source found) does not state soldermask color/finish, exact quantity made, price, MCU (if any beyond simple LED driving), or firmware/software source. The project photo shows red/gold coloring and two lit eye areas resembling LEDs; sao_version and connectivity (I2C, per the DC26 badge's standard SAO connector convention) are inferred from the general DC26 SAO connector spec referenced on the project page rather than stated specifically for this board. No press coverage, storefront listing, or additional photos beyond the two on the Hackaday.io gallery were found. A second gallery photo shows a bench full of many different SAOs being tested together and was not used since it does not clearly depict this item alone."
last_modified_date: '2026-09-07'
---

Iron Man SAO is a Shitty Add-On that Twinkle Twinkie describes making "last minute," producing only a small handful for DEF CON 26 in 2018. It is shaped like an Iron Man Mark III-style helmet, with two illuminated eye slits — visible lit blue/white in the maker's project photo, likely LEDs mounted behind translucent eye cutouts in the board.

The maker published KiCad and Gerber files for the board on Hackaday.io as a downloadable archive, which contains the copper and soldermask layer files needed to fabricate a copy. No firmware repository, bill of materials, price, or sales channel is given on the project page, so it is unclear whether the design was ever sold or was purely handed out among the small run the maker produced.

## Make your own

The project page (linked above) offers a zip archive of KiCad source files and Gerbers, sufficient to reproduce the PCB. No firmware or assembly instructions were found alongside it.
