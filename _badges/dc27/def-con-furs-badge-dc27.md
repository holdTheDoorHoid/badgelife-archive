---
title: DEF CON Furs Badge DC27
id: dc27-def-con-furs-badge-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: DEF CON Furs (defconfurs org)
  url: https://github.com/defconfurs
summary: An 18x7 RGB LED matrix badge made by the DEF CON Furs community group for DC27 (2019), scriptable in MicroPython with Bluetooth beaconing to other badges.
functions: Runs a MicroPython environment for user-scriptable LED animations (uploadable in JSON or Python); accelerometer-based wake and tap detection; two side pushbuttons; broadcasts BLE "#badgelife" beacons (badge ID, "Awoo" mode, emote/color-suggestion beacons) for interop with other badges at the con.
look:
  colors: []
  shape: null
  themes:
  - mascot
  - radio
tech:
  mcu: STM32L496RET6
  leds:
    count: 126
    type: RGB
    note: 18x7 RGB LED matrix (some matrix positions unpopulated due to the badge's cut shape)
  display: LED matrix 18x7
  connectivity:
  - ble
  - usb
  - i2c
  inputs:
  - buttons
  - accelerometer
  battery: 2x AA or micro-USB
  sao_version: v1.69bis
make_your_own:
  open_source: yes
  hardware_url: https://github.com/defconfurs/dcfurs-badge-dc27
  firmware_url: https://github.com/defconfurs/bluetooth-dc27
  eda_tool: null
  license: MIT
links:
- label: github.com/defconfurs/dcfurs-badge-dc27
  url: https://github.com/defconfurs/dcfurs-badge-dc27
  kind: repo
- label: github.com/defconfurs/bluetooth-dc27
  url: https://github.com/defconfurs/bluetooth-dc27
  kind: repo
images:
  - file: assets/images/badges/dc27/def-con-furs-badge-dc27/09bbd94282.png
    source: "https://github.com/defconfurs/dcfurs-badge-dc27"
    credit: "DEF CON Furs"
    caption: "Front render of the DC27 DEF CON Furs badge showing the 18x7 RGB LED matrix"
  - file: assets/images/badges/dc27/def-con-furs-badge-dc27/7ffe657f9f.png
    source: "https://github.com/defconfurs/dcfurs-badge-dc27"
    credit: "DEF CON Furs"
    caption: "Back detail photo of the DC27 DEF CON Furs badge"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/defconfurs/dcfurs-badge-dc27
  title: 'GitHub - defconfurs/dcfurs-badge-dc27: DEFCON Furs Badge Software for DC27 (2019)'
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''DEF CON 27 (2019)''.'
- kind: url
  url: https://github.com/defconfurs/dcfurs-badge-dc27
  title: dcfurs-badge-dc27 README and doc/ folder
  accessed: '2026-09-07'
  note: Confirmed chip (STM32L496RET6), 18x7 RGB matrix, MicroPython scripting, accelerometer, buttons, battery/USB power, badgelife v1.69bis SAO compliance, MIT license; source of the front-render and back-detail images.
- kind: url
  url: https://github.com/defconfurs/bluetooth-dc27
  title: 'GitHub - defconfurs/bluetooth-dc27: Bluetooth Firmware for the DC27 DEFCON Furs badge'
  accessed: '2026-09-07'
  note: Confirms Zephyr-based BLE firmware implementing the #badgelife beacon spec (badge ID, Awoo mode, emote/color-suggestion beacons) and the Fanstel BT832A BLE module.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No price, quantity made, or distribution details were found on the maker's own repos or in web search; get_one fields left empty rather than guessed. No storefront or press coverage located.
last_modified_date: '2026-09-07'
---

The DC27 badge is the 2019 edition of DEF CON Furs' annual community badge, built around an 18x7 RGB LED matrix and an STM32L496RET6 microcontroller. Rather than fixed firmware, the badge boots into a MicroPython environment so wearers can write or upload their own animations in Python or JSON, alongside built-in accelerometer-driven wake/tap detection and two side pushbuttons. It follows the community "#badgelife" SAO standard (v1.69bis) so other add-ons can plug into it.

A companion Bluetooth firmware, written for the Zephyr RTOS and running on the badge's Fanstel BT832A BLE module, broadcasts short-range beacons compatible with the wider "#badgelife" ecosystem — an identifying badge ID, an "Awoo" mode, and emote/color-suggestion beacons meant to let nearby badges coordinate their lighting.

Both the badge hardware/software and the Bluetooth firmware are published under the MIT license on the DEF CON Furs GitHub org, with schematics, a mechanical drawing, assembly instructions, and photos of the assembled board in the `doc/` folder. No pricing, production quantity, or distribution details (sale, giveaway, village) were found in the repos or via search; these are left blank rather than guessed.
