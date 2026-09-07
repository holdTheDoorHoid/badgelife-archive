---
title: Fri3d Badge 2020
id: fri3d-2022-fri3d-badge-2020
layout: badge
parent: Fri3d 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: fri3d-2022
year: 2022
makers:
- name: Fri3d Camp
  url: https://fri3d.be/
summary: The official ESP32-WROVER attendee badge of Fri3d Camp 2022 in Belgium (designed from 2020 for the postponed camp), with a 240x240 ST7789 IPS LCD, LIS2DH12 accelerometer, IR receiver, BadgeLink inter-badge link, a BBC micro:bit V2 edge connector for add-ons, and optional CO2 and temperature/humidity sensor footprints; over 700 units were built and shipped with MicroPython firmware.
functions: 'Programmable via MicroPython or Arduino; games and demos on the LCD (including a companion "GameOn" joystick/audio add-on originally built for the 2020 prototype badge); BadgeLink lets badges exchange data over a wired inter-badge link; accelerometer-based wake from sleep for battery saving.'
look:
  colors:
  - green
  - black
  shape: octopus
  themes:
  - animal
  - hardware tool
  - learn to solder
  form_factor: pcb badge
tech:
  mcu: ESP32-WROVER (4MB PSRAM, 16MB flash)
  leds: null
  display: 1.54" 240x240 IPS LCD (ST7789)
  connectivity:
  - ir
  - usb
  - i2c
  battery: LiPo, rechargeable, with optional GPIO-controlled charging
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '750+'
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of Fri3d Camp 2022 as the event's official badge.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Fri3dCamp/badge-2020
  firmware_url: https://github.com/Fri3dCamp/badge-2020
  eda_tool: null
links:
- label: github.com/Fri3dCamp/badge-2020
  url: https://github.com/Fri3dCamp/badge-2020
  kind: repo
- label: hackaday.io/project/169741-fri3d-2022-badge
  url: https://hackaday.io/project/169741-fri3d-2022-badge
  kind: hackaday
- label: www.espressif.com/en/news/Fri3d_Camp_badge
  url: https://www.espressif.com/en/news/Fri3d_Camp_badge
  kind: website
- label: github.com/Fri3dCamp/gameon-2020
  url: https://github.com/Fri3dCamp/gameon-2020
  kind: repo
images:
- file: assets/images/badges/fri3d-2022/fri3d-badge-2020/b5372ebc64.jpg
  source: "https://hackaday.io/project/169741-fri3d-2022-badge"
  credit: "Fri3d Camp"
  caption: "The production octopus-shaped Fri3d Camp badge, front side, with its 1.54\" IPS LCD and micro:bit-style edge connector"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Fri3dCamp/badge-2020
  title: 'Fri3d Badge 2020 (GitHub: Fri3dCamp/badge-2020)'
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/Fri3dCamp/badge-2020
  title: Fri3dCamp/badge-2020 README (hardware design, revision history)
  accessed: '2026-09-07'
  note: Confirmed MCU, display, sensors, connector, open-source hardware, revision history (REV 00-03), and CO2/temp-humidity sensor footprints.
- kind: url
  url: https://hackaday.io/project/169741-fri3d-2022-badge
  title: Fri3d 2022 badge project on Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed ESP32-WROVER (4MB PSRAM/16MB flash), 240x240 ST7789 IPS LCD, LIS2DH12 accelerometer, IR receiver, CP2102N USB-UART bridge, MicroPython+Arduino firmware, and "mass production of 750+ PCBs"; credits Wim Van Gool, Hans Polders, Bart Cerneels and others as the design team. Also the source of the badge photo used here.
- kind: url
  url: https://www.espressif.com/en/news/Fri3d_Camp_badge
  title: 'Espressif news: Fri3d Camp badge'
  accessed: '2026-09-07'
  note: Confirmed ESP32-WROVER module details and that "each participant received" a badge at the 12-14 August 2022 event; named add-ons GameOn and Time Blaster.
- kind: url
  url: https://github.com/Fri3dCamp/gameon-2020
  title: Fri3dCamp/gameon-2020 (GameOn add-on)
  accessed: '2026-09-07'
  note: GameOn is a separate joystick/SD-card/audio-amp add-on board that plugs into this badge; originally prototyped for the 2020 badge. Reported separately, not merged into this entry.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: LED count/type not stated anywhere found (the badge appears to have no addressable LEDs beyond the LCD and possibly status LEDs on the buttons, not confirmed). Exact per-unit price not found; badge was given free to attendees as part of registration/ticket, not separately sold, so price is left blank. Maker team members named on Hackaday (Wim Van Gool, Hans Polders, Bart Cerneels) but the entry keeps "Fri3d Camp" as the maker per the org convention used elsewhere in the archive; individual names noted here for reference.
last_modified_date: '2026-09-07'
---

The Fri3d Badge 2020 is the official electronic badge of Fri3d Camp, a biennial family-friendly hacker/maker festival in Belgium. Despite the name, it was actually worn at Fri3d Camp 2022: the badge was designed and prototyped in 2020 for that year's camp, but the event itself was postponed (COVID-era disruption), so the design carried over and the final production run — REV 03 — shipped to attendees at the rescheduled 2022 camp, held 12-14 August. The board is cut in the shape of an octopus, with a 1.54" 240x240 IPS LCD (ST7789 driver) mounted in the "head" and five tactile buttons along the bottom edge doubling as a BBC micro:bit V2-style edge connector for pin access.

Under the hood is an ESP32-WROVER module (4MB PSRAM, 16MB flash), a LIS2DH12 accelerometer used to wake the display on motion for battery savings, an IR receiver, and a CP2102N USB-to-UART bridge for programming. Optional component footprints let hackers add an MH-Z19C CO2 sensor or a Wurth temperature/humidity sensor, and a "BadgeLink" circuit allows badges to exchange data with each other over a wired link. Fri3d Camp built and hand-assembled over 750 units through a full SMT production run (paste, pick-and-place, reflow) and shipped them with both MicroPython and Arduino firmware support, all published as open hardware and software on GitHub. A companion accessory called GameOn — a joystick, SD card slot, and small audio amplifier — was designed to plug into the badge, first prototyped alongside the 2020 badge revision.

## Make your own

Hardware design files, firmware (MicroPython and Arduino), and the revision history (REV 00 through the production REV 03) are all published at github.com/Fri3dCamp/badge-2020. The README documents how to populate the optional CO2 and temperature/humidity sensor footprints and how to wire up battery-charging control via GPIO.
