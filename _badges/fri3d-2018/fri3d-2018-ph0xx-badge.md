---
title: Ph0xx (Fri3d Camp 2018 Badge)
id: fri3d-2018-fri3d-2018-ph0xx-badge
layout: badge
parent: Fri3d 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: fri3d-2018
year: 2018
makers:
- name: Fri3d Camp (Wim Van Gool, Bert Outtier)
  url: https://github.com/Fri3dCamp
summary: Ph0xx is the fox-shaped attendee badge for Fri3d Camp 2018, a family hacker/maker/DIY camp in Belgium with around 600 attendees, built around an ESP32-WROOM-32 with two 5x7 LED matrices, an ADXL345 accelerometer, an 18650 cell with TP4056 charger, touch buttons, a buzzer, expansion headers for "jewel" add-ons and Lego Technic compatible holes.
functions: Two touch buttons and two touchpads, a buzzer (frequency/volume control), and two 5x7 LED matrix "eyes" driven via 74HC595 shift registers; expandable through add-on "jewel" boards (an Air Jewel for environmental sensors and a Bot Jewel for servo control) plugged into onboard expansion headers.
look:
  colors:
  - red
  shape: fox
  themes:
  - animal
  - mascot
  - wearable
tech:
  mcu: ESP32-WROOM-32
  leds:
    count: null
    type: LED matrix
    note: Two 5x7 LED matrix displays used as the fox's "eyes", driven via 74HC595 shift registers; originally blue, later revised to green.
  display: LED matrix 5x7 (x2)
  connectivity:
  - wifi
  - ble
  inputs:
  - touch
  - accelerometer
  battery: 18650 Li-ion cell with TP4056 charger and DW01-P protection
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ~650
  availability: free
  availability_note: Given to attendees of Fri3d Camp 2018 as part of the camp; checked 2026-09-07.
  distribution:
  - kit
  where: Given to attendees of Fri3d Camp 2018 in Belgium.
make_your_own:
  open_source: true
  hardware_url: https://github.com/Fri3dCamp/badge
  firmware_url: https://github.com/Fri3dCamp/Fri3dBadge
  eda_tool: Altium
links:
- label: github.com/Fri3dCamp/badge
  url: https://github.com/Fri3dCamp/badge
  kind: repo
  archived: https://web.archive.org/web/20260312123042/https://github.com/Fri3dCamp/badge
- label: hackaday.io/project/160451-ph0xx
  url: https://hackaday.io/project/160451-ph0xx
  kind: hackaday
  archived: https://web.archive.org/web/20260904220754/https://hackaday.io/project/160451-ph0xx
- label: github.com/Fri3dCamp/Fri3dBadge
  url: https://github.com/Fri3dCamp/Fri3dBadge
  kind: repo
images:
- file: assets/images/badges/fri3d-2018/fri3d-2018-ph0xx-badge/c9b8bf3af3.jpg
  source: https://hackaday.io/project/160451-ph0xx
  credit: Fri3d Camp
  caption: Ph0xx badge, fox-shaped PCB with dual LED matrix eyes
  archived: https://web.archive.org/web/20260904220754/https://hackaday.io/project/160451-ph0xx
- file: assets/images/badges/fri3d-2018/fri3d-2018-ph0xx-badge/994ab39b08.jpg
  source: https://github.com/Fri3dCamp/badge
  credit: Fri3d Camp
  caption: Fri3d Camp 2018 badge prototype 3
  archived: https://web.archive.org/web/20260312123042/https://github.com/Fri3dCamp/badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Fri3dCamp/badge
  title: Fri3dCamp/badge - Elk hacker/maker/DIY Kamp heeft zijn eigen badge nodig...
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260312123042/https://github.com/Fri3dCamp/badge
- kind: url
  url: https://hackaday.io/project/160451-ph0xx
  title: Ph0xx - Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed maker names, event/year, chip, sensors, battery circuitry, jewel expansion system, Lego Technic holes, fox theme, and mass-production quantity (~650 boards).
  archived: https://web.archive.org/web/20260904220754/https://hackaday.io/project/160451-ph0xx
- kind: url
  url: https://github.com/Fri3dCamp/Fri3dBadge
  title: Fri3dCamp/Fri3dBadge - Arduino library
  accessed: '2026-09-07'
  note: Confirmed ESP32 MCU, ADXL345 accelerometer, buttons/touchpads, buzzer, LED matrix, and Servo Jewel add-on; firmware repo for the badge.
- kind: url
  url: https://raw.githubusercontent.com/Fri3dCamp/badge/master/README.md
  title: Fri3d Camp Badge 2018 README
  accessed: '2026-09-07'
  note: Prototype description and photo filenames (Proto0/1/2) used for the saved image.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own GitHub repos and Hackaday.io project page confirm the core hardware and distribution facts. No price could be found (badges appear to have been included with camp registration rather than sold separately), and exact LED count per matrix (5x7 grid, count not stated as a total) and SAO header type/count were not stated by sources, so those fields are left empty. The GitHub badge README shows prototype-stage photos rather than a final production shot; the Hackaday.io cover image was used as the primary photo instead.
last_modified_date: '2026-09-07'
model:
  file: assets/models/fri3d-2018/fri3d-2018-ph0xx-badge.glb
  method: kicad
  source_file: fri3d-badge-2018.brd
  generated: '2026-09-07'
  bytes: 155556
---

Ph0xx is the attendee badge given out at Fri3d Camp 2018, a family-oriented hacker/maker/DIY camp held in Belgium with roughly 600 attendees. Designed by Wim Van Gool and Bert Outtier for the Fri3d Camp organizing team, the badge takes the shape of a fox and is built around an ESP32-WROOM-32 module, giving it Wi-Fi and Bluetooth connectivity alongside two 5x7 LED matrices used as the fox's glowing eyes (driven through 74HC595 shift registers, and revised from an original blue to a final green during development).

Onboard sensors and interaction include an ADXL345 accelerometer, two touch buttons/touchpads, and a buzzer. Power comes from a user-installed 18650 Li-ion cell with TP4056 charging and DW01-P protection circuitry. The badge carries expansion headers for plug-in "jewel" boards — an Air Jewel adding environmental sensors and a Bot Jewel adding servo control — plus a set of holes on an 8mm grid sized to accept Lego Technic pins, letting attendees mechanically extend the badge with Lego parts. Around 650 units were produced for camp distribution.

## Make your own

Fri3d Camp published the hardware design (Altium project files, prototype revisions) in the `Fri3dCamp/badge` GitHub repository, and firmware/an Arduino library supporting the accelerometer, buttons, buzzer, LED matrix and Servo Jewel in the separate `Fri3dCamp/Fri3dBadge` repository.
