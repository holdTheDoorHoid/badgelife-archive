---
title: TiLDA Mk3
id: emf-camp-2016-tilda-mk3
layout: badge
parent: EMF Camp 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: emf-camp-2016
year: 2016
makers:
- name: EMF Camp badge team
  url: https://www.emfcamp.org
summary: The official EMF Camp 2016 conference badge, a MicroPython-hackable device with a colour LCD, Wi-Fi, and motion sensors.
functions: Runs MicroPython apps from a menu; joystick + A/B/Menu button navigation; Wi-Fi connectivity for on-site services; motion/orientation sensing via accelerometer and compass; buzzer for sound; microSD storage for user files.
look:
  colors: [black]
  shape: rectangle
  themes: [wearable, learn to solder]
tech:
  mcu: STM32L486VGT6
  leds:
    count: 1
    type: WS2812B
    note: Single NeoPixel on pin PB13; commonly reported as non-functional/defunct on many units.
  display: 320x240 colour LCD
  connectivity: [wifi]
  inputs: [joystick, buttons, accelerometer]
  battery: rechargeable LiPo, charges via microUSB (2-3 hours for a full charge)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: Given to every attendee of EMF Camp 2016 as their conference badge.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/emfcamp/Mk3-Hardware
  firmware_url: https://github.com/emfcamp/Mk3-Firmware
  eda_tool: null
links:
- label: badge.emfcamp.org/TiLDA_MK3
  url: https://badge.emfcamp.org/TiLDA_MK3/
  kind: website
- label: github.com/emfcamp/Mk3-Hardware
  url: https://github.com/emfcamp/Mk3-Hardware
  kind: repo
- label: github.com/emfcamp/Mk3-Firmware
  url: https://github.com/emfcamp/Mk3-Firmware
  kind: repo
images:
  - file: assets/images/badges/emf-camp-2016/tilda-mk3/b494ee45ca.jpg
    source: "https://badge.emfcamp.org/TiLDA_MK3/"
    credit: "EMF Camp"
    caption: "TiLDA Mk3 badge, front view"
contact: {}
notes:
- Official EMF Camp 2016 conference badge, built around a colour LCD, Wi-Fi (cc3100), accelerometer and compass; not yet in the archive. Found by the event-year sweep, task emf-addons.
status: released
sources:
- kind: url
  url: https://badge.emfcamp.org/TiLDA_MK3/
  title: TiLDA Mk3
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-addons); event read as ''emf-camp-2016''.'
- kind: url
  url: https://badge.emfcamp.org/TiLDA_MK3/
  title: TiLDA MK3 Badge Documentation
  accessed: '2026-09-08'
  note: Confirmed display, connectivity, LED, input, and battery details.
- kind: url
  url: https://badge.emfcamp.org/TiLDA_MK3/Badge_Competition_2016/
  title: Badge Competition 2016
  accessed: '2026-09-08'
  note: Confirmed the badge was distributed for EMF Camp 2016.
- kind: url
  url: https://raw.githubusercontent.com/emfcamp/Mk3-Hardware/master/README.md
  title: emfcamp/Mk3-Hardware README
  accessed: '2026-09-08'
  note: Confirmed MCU (STM32L486VGT6), Wi-Fi module (CC3100MOD), accelerometer/gyro (LSM6DS3), magnetometer (LIS3MDL), and CERN OHL open hardware license. Also notes this hardware is styled "TiLDA MKpi" in the repo itself, same badge as Mk3.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: This appears to be the same physical badge as entry emf-camp-2016-tilda-mk3-mk ("TiLDA Mk3 (Mkπ)") — both cite the same badge.emfcamp.org pages and the same Mk3-Hardware/Mk3-Firmware GitHub repos, and the hardware repo itself refers to the board as the "TiLDA MKπ Badge". Flagging as a likely duplicate rather than merging, per instructions. Exact unit quantity and price not published (badge was given free to all attendees, not individually priced/sold).
last_modified_date: '2026-09-08'
---

The TiLDA Mk3 was the official conference badge given to every attendee of EMF Camp 2016, the UK hacker camp run by Electromagnetic Field. It centers on an STM32L486VGT6 ARM Cortex-M4 microcontroller running MicroPython, paired with a 320x240 colour LCD, a joystick and A/B/Menu buttons, a TI CC3100 Wi-Fi module, and an LSM6DS3 accelerometer/gyro plus LIS3MDL magnetometer for orientation sensing. A single WS2812B NeoPixel sits on the board, though it is widely reported as non-functional on many units in the field. The badge charges over microUSB and includes a microSD slot for user storage.

Both hardware and firmware are fully open source, published on GitHub under the emfcamp organization and licensed under CERN OHL v1.2. EMF Camp ran a "Badge Competition 2016" encouraging attendees to hack the Mk3's hardware and software, awarding prizes in separate hardware and software categories.

## Make your own

Hardware design files (CERN OHL v1.2) are at github.com/emfcamp/Mk3-Hardware; MicroPython-based firmware is at github.com/emfcamp/Mk3-Firmware. The badge's own documentation site (badge.emfcamp.org/TiLDA_MK3) includes a "Get Started" guide for building and flashing firmware.

