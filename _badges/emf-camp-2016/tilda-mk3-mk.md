---
title: TiLDA Mk3 (Mkπ)
id: emf-camp-2016-tilda-mk3-mk
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
  colors:
  - black
  shape: rectangle
  themes:
  - wearable
  - learn to solder
tech:
  mcu: STM32L486VGT6
  leds:
    count: 1
    type: WS2812B
    note: Single NeoPixel on pin PB13; commonly reported as non-functional/defunct on many units.
  display: 320x240 colour LCD
  connectivity:
  - wifi
  inputs:
  - joystick
  - buttons
  - accelerometer
  battery: rechargeable LiPo, charges via microUSB (2-3 hours for a full charge)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to every attendee of EMF Camp 2016 as their conference badge.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/emfcamp/Mk3-Hardware
  firmware_url: https://github.com/emfcamp/Mk3-Firmware
  eda_tool: EAGLE
links:
- label: badge.emfcamp.org/TiLDA_MK3/Get_Started
  url: https://badge.emfcamp.org/TiLDA_MK3/Get_Started/
  kind: website
- label: github.com/emfcamp/Mk3-Firmware
  url: https://github.com/emfcamp/Mk3-Firmware
  kind: repo
- label: github.com/emfcamp/Mk3-Hardware
  url: https://github.com/emfcamp/Mk3-Hardware
  kind: repo
- label: badge.emfcamp.org/TiLDA_MK3
  url: https://badge.emfcamp.org/TiLDA_MK3/
  kind: website
images:
- file: assets/images/badges/emf-camp-2016/tilda-mk3-mk/b494ee45ca.jpg
  source: https://badge.emfcamp.org/TiLDA_MK3/
  credit: EMF Camp badge team
  caption: TiLDA Mk3 (Mkπ) badge, front
- file: assets/images/badges/emf-camp-2016/tilda-mk3-mk/b494ee45ca.jpg
  source: https://badge.emfcamp.org/TiLDA_MK3/
  credit: EMF Camp
  caption: TiLDA Mk3 badge, front view
contact: {}
notes:
- Official EMF Camp 2016 badge, a MicroPython-hackable conference badge; firmware/hardware also hosted at github.com/emfcamp/Mk3-Firmware and Mk3-Hardware; not yet in the archive. Found by the event-year sweep, task emf-badges.
- The sweep's source page names it "TiLDA MK3 (Mkπ)"; the badge's own hardware repo styles it "TiLDA MKπ Badge", and the emfcamp.org site's landing page for it uses the plain name "TiLDA Mk3" (see also archive entry emf-camp-2016-tilda-mk3, which appears to be the same badge).
- Official EMF Camp 2016 conference badge, built around a colour LCD, Wi-Fi (cc3100), accelerometer and compass; not yet in the archive. Found by the event-year sweep, task emf-addons.
status: released
sources:
- kind: url
  url: https://badge.emfcamp.org/TiLDA_MK3/Get_Started/
  title: TiLDA Mk3 (Mkπ)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-badges); event read as ''emf-camp-2016''.'
- kind: url
  url: https://badge.emfcamp.org/TiLDA_MK3/
  title: TiLDA MK3 Badge Documentation
  accessed: '2026-09-08'
  note: Confirmed display (320x240 colour LCD), joystick/A/B/Menu buttons, Wi-Fi (cc3100), accelerometer, compass, buzzer, and battery.
- kind: url
  url: https://raw.githubusercontent.com/emfcamp/Mk3-Hardware/master/README.md
  title: emfcamp/Mk3-Hardware README
  accessed: '2026-09-08'
  note: Confirmed MCU (STM32L486VGT6), Wi-Fi module (CC3100MOD), accelerometer/gyro (LSM6DS3), magnetometer (LIS3MDL), EAGLE schematic/board files, and CERN OHL v1.2 open hardware license; repo itself names the board "TiLDA MKπ Badge for Electromagnetic Field 2016".
- kind: url
  url: https://badge.emfcamp.org/TiLDA_MK3/Badge_Competition_2016/
  title: Badge Competition 2016
  accessed: '2026-09-08'
  note: Confirmed the badge was distributed for EMF Camp 2016.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: This appears to be the same physical badge as entry emf-camp-2016-tilda-mk3 ("TiLDA Mk3") — both cite the same badge.emfcamp.org pages and the same Mk3-Hardware/Mk3-Firmware GitHub repos, and the hardware repo names the board "TiLDA MKπ Badge". Flagging as a likely duplicate rather than merging, per instructions. Exact unit quantity and price not published (badge was given free to all attendees, not individually priced/sold). Merged with duplicate entry 'TiLDA Mk3' (emf-camp-2016-tilda-mk3).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/emf-camp-2016/tilda-mk3/
model:
  file: assets/models/emf-camp-2016/tilda-mk3-mk.glb
  method: kicad
  source_file: Mk3 Prototype3.brd
  generated: '2026-09-10'
  bytes: 909464
---

The TiLDA Mk3 (also styled TiLDA MKπ) was the official conference badge given to every attendee of EMF Camp 2016, the UK hacker camp run by Electromagnetic Field. It is built around an STM32L486VGT6 ARM Cortex-M4 microcontroller running MicroPython, paired with a 320x240 colour LCD, a joystick with A/B/Menu buttons, a TI CC3100 Wi-Fi module, and an LSM6DS3 accelerometer/gyro plus LIS3MDL magnetometer for motion and orientation sensing. A single WS2812B NeoPixel sits on the board, though it is widely reported as non-functional on many units in the field. The badge charges over microUSB and includes storage for user files, with a buzzer for sound feedback.

Both hardware and firmware are fully open source, published on GitHub under the emfcamp organization: the hardware (EAGLE schematic/board files) under CERN OHL v1.2, and MicroPython-based firmware separately. The badge's documentation site (badge.emfcamp.org/TiLDA_MK3) includes a "Get Started" guide for building and flashing firmware, plus an API reference for the built-in MicroPython libraries.

This entry appears to duplicate the archive's existing emf-camp-2016-tilda-mk3 entry, which was found and researched independently and describes the same badge under the plain name "TiLDA Mk3."

## Make your own

Hardware design files (CERN OHL v1.2) are at github.com/emfcamp/Mk3-Hardware; MicroPython-based firmware is at github.com/emfcamp/Mk3-Firmware. The badge's own documentation site (badge.emfcamp.org/TiLDA_MK3) includes a "Get Started" guide for building and flashing firmware.

## Notes merged from the duplicate entry "TiLDA Mk3"

The TiLDA Mk3 was the official conference badge given to every attendee of EMF Camp 2016, the UK hacker camp run by Electromagnetic Field. It centers on an STM32L486VGT6 ARM Cortex-M4 microcontroller running MicroPython, paired with a 320x240 colour LCD, a joystick and A/B/Menu buttons, a TI CC3100 Wi-Fi module, and an LSM6DS3 accelerometer/gyro plus LIS3MDL magnetometer for orientation sensing. A single WS2812B NeoPixel sits on the board, though it is widely reported as non-functional on many units in the field. The badge charges over microUSB and includes a microSD slot for user storage.

Both hardware and firmware are fully open source, published on GitHub under the emfcamp organization and licensed under CERN OHL v1.2. EMF Camp ran a "Badge Competition 2016" encouraging attendees to hack the Mk3's hardware and software, awarding prizes in separate hardware and software categories.

## Make your own

Hardware design files (CERN OHL v1.2) are at github.com/emfcamp/Mk3-Hardware; MicroPython-based firmware is at github.com/emfcamp/Mk3-Firmware. The badge's own documentation site (badge.emfcamp.org/TiLDA_MK3) includes a "Get Started" guide for building and flashing firmware.
