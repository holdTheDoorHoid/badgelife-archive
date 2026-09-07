---
title: Fri3d 2022 Badge
id: fri3d-2022-fri3d-2022-badge
layout: badge
parent: Fri3d 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: fri3d-2022
year: 2022
makers:
- name: Fri3d Camp (Wim Van Gool)
  url: https://github.com/Fri3dCamp
  role: lead designer
- name: Hans Polders
  url: https://hackaday.io/hans-polders
  role: team member
- name: Bart Cerneels
  url: https://hackaday.io/bart-cerneels
  role: team member
- name: Toon
  url: https://hackaday.io/toon
  role: team member
summary: The official attendee badge for Fri3d Camp 2022 in Belgium, an ESP32-WROVER board with a 240x240 ST7789v IPS LCD, LIS2DH12 accelerometer, IR receiver, CP2102N USB-UART bridge and a micro:bit-style edge expansion connector, of which 700+ units were produced and flashed with MicroPython firmware.
functions: Runs games and camp software on-screen; wakes on movement via the accelerometer's interrupt pin; can receive IR remote signals; supports add-on boards through its micro:bit-style edge connector.
look:
  colors: []
  shape: rectangle
  themes:
  - village badge
  - hardware tool
tech:
  mcu: ESP32-WROVER (4MB PSRAM, 16MB flash)
  leds: null
  display: 0.96" 240x240 IPS LCD (ST7789v)
  connectivity:
  - usb
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 700+
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of Fri3d Camp 2022 as the official conference badge; the same board design was reused from the 2020 edition.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Fri3dCamp/badge-2020
  firmware_url: https://github.com/Fri3dCamp/Badge2020_micropython
  eda_tool: null
links:
- label: hackaday.io/project/169741-fri3d-2022-badge
  url: https://hackaday.io/project/169741-fri3d-2022-badge
  kind: hackaday
- label: github.com/Fri3dCamp/badge-2020
  url: https://github.com/Fri3dCamp/badge-2020
  kind: repo
- label: github.com/Fri3dCamp/Badge2020_micropython
  url: https://github.com/Fri3dCamp/Badge2020_micropython
  kind: repo
- label: github.com/Fri3dCamp/Badge2020_arduino
  url: https://github.com/Fri3dCamp/Badge2020_arduino
  kind: repo
- label: fri3d.be/badge
  url: https://fri3d.be/badge/
  kind: website
images:
- file: assets/images/badges/fri3d-2022/fri3d-2022-badge/1d07ef73fa.jpg
  source: "https://github.com/Fri3dCamp/badge-2020"
  credit: "Fri3d Camp"
  caption: "Front view of the Fri3d 2022 badge PCB"
- file: assets/images/badges/fri3d-2022/fri3d-2022-badge/776f752a54.jpg
  source: "https://github.com/Fri3dCamp/badge-2020"
  credit: "Fri3d Camp"
  caption: "Close-up of the Fri3d 2022 badge, showing the display and expansion connector"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/169741-fri3d-2022-badge
  title: Fri3d 2022 Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/Fri3dCamp/badge-2020
  title: "Fri3dCamp/badge-2020: Fri3dBadge 2020 version"
  accessed: '2026-09-07'
  note: Confirms this hardware design was used for both the 2020 and 2022 badges; hardware and firmware both published (open source); lists the micro:bit V2 edge connector, accelerometer wake-on-movement, and optional CO2/temp-humidity add-ons.
- kind: url
  url: https://github.com/Fri3dCamp/Badge2020_micropython
  title: Fri3dCamp/Badge2020_micropython
  accessed: '2026-09-07'
  note: MicroPython firmware repository for the badge.
- kind: url
  url: https://fri3d.be/badge/
  title: Fri3d Camp badge page
  accessed: '2026-09-07'
  note: Current badge overview page; describes the current-year (2026) badge program rather than the 2022 badge specifically, so not used for hardware specs.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: The Hackaday.io project page and the badge-2020 GitHub repo (whose hardware design was reused unchanged for 2022) confirm the chip, display, sensors, USB bridge, and micro:bit-style expansion connector. Price paid by attendees and exact distribution mechanics (e.g. included with a ticket) were not stated on any source checked, so those fields are left empty. Team credited on the Hackaday.io project page (Wim Van Gool, Hans Polders, Fri3d Camp org account, Bart Cerneels, Toon) added as additional makers. No LED count/type was found in any source, so tech.leds is left null. EDA tool for the PCB design was not stated in the fetched summaries.
last_modified_date: '2026-09-07'
---

The Fri3d 2022 Badge was the official attendee badge given to participants of Fri3d Camp 2022, a Belgian hacker camp held in August 2022. Rather than a new design, the badge reused the hardware from the Fri3d Camp 2020 edition: an ESP32-WROVER module with 4MB of PSRAM and 16MB of flash, driving a 240x240 IPS LCD built around an ST7789v controller. It also carries a LIS2DH12 three-axis accelerometer (wired to wake the board on movement), an IR receiver, and a CP2102N USB-to-UART bridge for programming. More than 700 units were produced.

A distinguishing feature of the design is its BBC micro:bit V2-style edge connector, which let attendees plug the badge into existing micro:bit accessories and add-on boards rather than a proprietary SAO header. The board shipped flashed with MicroPython firmware, though an Arduino firmware option was also published by the Fri3d Camp team.

Both the hardware design and the firmware are open source, published across several repositories under the Fri3dCamp GitHub organization: `badge-2020` for the PCB design, `Badge2020_micropython` for the stock firmware, and `Badge2020_arduino` for the Arduino alternative. The Hackaday.io project credits a team of five: Wim Van Gool, Hans Polders, Bart Cerneels, Toon, and the Fri3d Camp organization itself.
