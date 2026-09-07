---
title: TEST-O Robot Buddy Addon Continuity Tester
id: supercon-2023-test-o-robot-buddy-addon-continuity-tester
layout: badge
parent: Supercon 2023
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2023
year: 2023
makers:
- name: trueControl
  url: https://basic.truecontrol.org/
summary: A robot-shaped badge addon that doubles as a continuity meter, diode tester, and RGB light-show toy, usable standalone on a coin cell or plugged into a GAT/SAO-compatible badge.
functions: 'Three modes selected by a bottom switch: continuity test (cheek probes, buzzer toggle, two sensitivity levels, RGB eye status), diode test (probes output ~3.15V at up to 2mA to light standard and power LEDs), and RGB Fun mode (two potentiometers pick a lightshow program and adjust its parameters, with four brightness levels).'
look:
  colors: []
  shape: robot
  themes:
  - robot
  - hardware tool
  - measurement
tech:
  mcu: PY32F003
  leds:
    count: null
    type: RGB
    note: RGB eyes for status/lightshow, plus a top LED used in diode-test mode.
  display: none
  connectivity:
  - i2c
  battery: CR2032
  sao_version: null
get_one:
  price: $35
  price_usd: 35
  quantity: ''
  availability: available
  availability_note: 'Listed in the trueControl webshop as of 2026-09-07 at $35; blank boards and BOM also offered for DIY builders.'
  distribution:
  - purchase
  where: trueControl webshop (shop.truecontrol.org); originally distributed at Hackaday Supercon 7 (2023) and later submitted to the Supercon 8 (2024) SAO contest.
make_your_own:
  open_source: yes
  hardware_url: https://basic.truecontrol.org/database/sc7/testo_REV2_sch.pdf
  firmware_url: https://git.trueserve.org/trueControl/sc7-testo-firmware
  eda_tool: null
links:
- label: basic.truecontrol.org/database/sc7/testo-qs
  url: https://basic.truecontrol.org/database/sc7/testo-qs/
  kind: website
- label: TEST-O Code, Schematics, etc (trueControl BASIC)
  url: https://basic.truecontrol.org/database/sc7/testo-dev/
  kind: doc
- label: TEST-O the Test Robot Addon (Hackaday.io)
  url: https://hackaday.io/project/198571-test-o-the-test-robot-addon
  kind: hackaday
- label: sc7-testo-firmware (git.trueserve.org)
  url: https://git.trueserve.org/trueControl/sc7-testo-firmware
  kind: repo
- label: sc7-testo-bootloader (git.trueserve.org)
  url: https://git.trueserve.org/trueControl/sc7-testo-bootloader
  kind: repo
- label: trueControl Shop - TEST-O Robot Buddy Addon Continuity Tester
  url: https://shop.truecontrol.org/index.php?manufacturer_id=11&route=product%2Fmanufacturer%2Finfo
  kind: store
images:
- file: assets/images/badges/supercon-2023/test-o-robot-buddy-addon-continuity-tester/a810b63e8a.jpg
  source: "https://hackaday.io/project/198571-test-o-the-test-robot-addon"
  credit: "true (trueControl)"
  caption: "TEST-O robot buddy addon, front view"
- file: assets/images/badges/supercon-2023/test-o-robot-buddy-addon-continuity-tester/3e642529b7.jpg
  source: "https://hackaday.io/project/198571-test-o-the-test-robot-addon"
  credit: "true (trueControl)"
  caption: "TEST-O robot buddy addon, alternate view"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://basic.truecontrol.org/database/sc7/testo-qs/
  title: TEST-O Robot Buddy Addon Continuity Tester
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''supercon-2023''.'
- kind: url
  url: https://basic.truecontrol.org/database/sc7/testo-dev/
  title: TEST-O Code, Schematics, etc - trueControl BASIC
  accessed: '2026-09-07'
  note: Firmware/bootloader git repos, PY32F003 MCU, REV2 schematic PDF link, header pinout notes (SWD/UART on addon header pins 5-6).
- kind: url
  url: https://hackaday.io/project/198571-test-o-the-test-robot-addon
  title: TEST-O the Test Robot Addon
  accessed: '2026-09-07'
  note: Maker attribution (Hackaday user "true"), confirms Supercon 7 origin and Supercon 8 SAO contest submission (2024), source of the two gallery photos saved.
- kind: url
  url: https://shop.truecontrol.org/index.php?manufacturer_id=11&route=product%2Fmanufacturer%2Finfo
  title: trueControl Shop - Badges
  accessed: '2026-09-07'
  note: Confirms current listing and price ($35) in the trueControl webshop.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Quantity made not stated anywhere found. LED count not specified beyond "RGB eyes" (two) plus one top diode-test LED and cheek continuity LEDs; exact count left null since sources never give a number. No SAO header pin-count/version given (it uses the GAT addon standard, described elsewhere on the site, rather than plain SAO v1/v2). EDA tool not stated.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/test-o-robot-buddy-addon-continuity-tester/
---

TEST-O is a robot-shaped badge addon from trueControl (Hackaday user "true") that packs a continuity meter, a diode tester, and an RGB light-show toy into one board. It runs on a PY32F003 microcontroller, works standalone off a CR2032 coin cell, or draws power through a GAT/SAO-compatible addon header when plugged into a host badge, with a rear switch choosing which power source is active. A second switch on the front picks between continuity test mode (probes on the robot's arms, status shown on the left eye, with a toggleable buzzer and two sensitivity levels), diode test mode (probes output about 3.15V at up to 2mA, enough to light standard and power LEDs, status on the right eye), and an RGB Fun mode where two potentiometers select and tune a lightshow program across four brightness levels.

The addon was originally released at Hackaday Supercon 7 in 2023, and trueControl later submitted it to the Supercon 8 SAO contest in 2024. Hardware and firmware are both published: a REV2 schematic PDF, and separate git repositories for the main application firmware and a custom XMODEM bootloader. As of research date it remains listed for sale in the trueControl webshop for $35, with bare boards and a bill of materials also offered for people who want to build their own.

## Make your own

Firmware and bootloader source are on trueControl's self-hosted git server (`sc7-testo-firmware` and `sc7-testo-bootloader`), and the REV2 schematic is published as a PDF. The addon's 5th and 6th header pins carry SWD or UART depending on firmware state (UART for the bootloader, SWD once the bootloader hands off), which is how a builder would reflash it via a DAPLink debugger if needed.
