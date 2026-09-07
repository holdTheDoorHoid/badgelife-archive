---
title: Lie Detector Badge (re-release of DC29)
id: dc31-lie-detector-badge-re-release-of-dc29
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Tor Project
  url: https://github.com/seeess
summary: A polygraph-style electronic badge with GSR and heart-rate sensors, graphing the readings on two OLED screens; DEF CON 31 re-release of the maker's DC29 Tor badge.
functions: 'Lie Detector mode plots GSR (galvanic skin response) and heart-rate sensor readings on two displays; also has cheat/calibration modes and "bling" modes (fake pulse, logo scroll, name scroll, "bad DEFCON advice" scrolling text) stored in flash.'
look:
  colors: []
  shape: null
  themes:
  - privacy
  - security
  - measurement
tech:
  mcu: Seeeduino XIAO (SAMD21 Cortex M0+)
  leds:
    count: 5
    type: reverse-mount
    note: four onboard XIAO LEDs plus one reverse-mounted green LED for the heart-rate sensor
  display: 2x 1.3" i2c OLED (SH1106 driver)
  connectivity:
  - i2c
  - usb
  battery: 2x AA (boosted to 3.3V) or USB-C
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold at the Tor Project booth at DEF CON 31; all profits went to the Tor Project.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/seeess/Defcon-Tor-31-Badge
  eda_tool: null
links:
- label: github.com/seeess/Defcon-Tor-29-Badge (original DC29 badge)
  url: https://github.com/seeess/Defcon-Tor-29-Badge
  kind: repo
- label: github.com/seeess/Defcon-Tor-31-Badge (this DC31 re-release)
  url: https://github.com/seeess/Defcon-Tor-31-Badge
  kind: repo
images:
- file: assets/images/badges/dc31/lie-detector-badge-re-release-of-dc29/242da92ae2.jpg
  source: "https://github.com/seeess/Defcon-Tor-31-Badge"
  credit: "seeess (Tor Project)"
  caption: "The Tor Project lie detector badge, DEF CON 31 re-release of the DC29 design"
contact: {}
notes:
- This badge was so popular they are doing another release!! Get them while you can
- 'Maker (GitHub handle seeess) states they personally front all development costs and that all sale profits go to the Tor Project.'
status: released
sources:
- kind: sheet
  event: dc31
  row: 79
  updated: '2023-08-02'
- kind: url
  url: https://github.com/seeess/Defcon-Tor-31-Badge
  title: "seeess/Defcon-Tor-31-Badge: code and manual for the defcon 31 electronic Tor badge"
  accessed: '2026-09-06'
  note: 'Primary source: confirms this is a re-release of the DC29 badge (OLED driver changed SSD1306->SH1106), full hardware/feature list, sold at Tor booth at DEF CON 31, all profits to Tor Project.'
- kind: url
  url: https://github.com/seeess/Defcon-Tor-29-Badge
  title: "seeess/Defcon-Tor-29-Badge"
  accessed: '2026-09-06'
  note: Original DC29 version of this badge; confirms MCU, sensors, and display details carried over to the DC31 re-release.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Sheet had linked to the DC29 repo instead of the DC31 one; found and linked the correct github.com/seeess/Defcon-Tor-31-Badge repo, which documents this specific re-release. Price and quantity made are not stated anywhere in the repo/manual. Availability is marked sold_out as a one-time con-booth sale from 2023; current stock status was not separately verified.'
last_modified_date: '2026-09-06'
---

The Tor Project's DEF CON 31 badge is a re-release of maker seeess's popular DC29 "lie detector" badge, sold at the Tor Project's booth with all profits going to the project. It uses a Seeeduino XIAO (SAMD21 Cortex M0+) to drive two galvanic-skin-response and heart-rate sensors — the same pair of measurements used in a polygraph — and plots the live readings as graphs across two 1.3" i2c OLED displays. The main hardware change from the DC29 version was swapping the OLED driver chip from SSD1306 to SH1106, while keeping the same display library.

Beyond its core Lie Detector mode, the badge includes calibration and "cheat" modes plus a set of bling modes (a fake pulse animation, a scrolling Tor logo, scrolling "bad DEFCON advice," and a name-scroll feature backed by flash storage). It runs on two AA batteries boosted to 3.3V or over USB-C, has an on/off switch and a 100k-ohm potentiometer for GSR calibration, and carries a keyed 1.69bis SAO header so it can host other add-ons. Firmware and a manual are published on GitHub under the WTFPL; the maker notes they personally cover development costs so that all badge revenue benefits the Tor Project.
