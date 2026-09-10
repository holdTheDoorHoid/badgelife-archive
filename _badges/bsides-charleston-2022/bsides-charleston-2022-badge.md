---
title: BSides Charleston 2022 Badge
id: bsides-charleston-2022-bsides-charleston-2022-badge
layout: badge
parent: BSides Charleston 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-charleston-2022
year: 2022
makers:
- name: Badge Pirates
summary: 'The official conference badge for BSides Charleston 2022: an ESP8266-based electronic badge with a built-in CTF, four LEDs, and a laser-cut-style hammock/beach graphic on the PCB silkscreen.'
functions: 'Runs a small on-badge capture-the-flag: the ESP8266 boots a WiFi access point and a web server at 192.168.4.1, serves a page that checks a submitted "plaintext" value against a target string, and separately accepts a 3-digit PIN over serial. Four LEDs track progress through the challenge phases and blink in sequence once flags are solved.'
look:
  colors:
  - blue
  - white
  shape: rectangle
  themes:
  - beach
  - ctf
  - security
tech:
  mcu: ESP8266
  leds:
    count: 4
    type: discrete
    note: Driven directly from GPIO pins (16, 13, 12, 14); used as CTF-progress indicators, not addressable RGB.
  display: none
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to BSides Charleston 2022 attendees; exact distribution method not stated in the sources found.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/BadgePiratesLLC/BSidesCHS_2022/tree/main/CAD
  firmware_url: https://github.com/BadgePiratesLLC/BSidesCHS_2022/blob/main/Code/main.ino
  eda_tool: KiCad
links:
- label: github.com/BadgePiratesLLC/BSidesCHS_2022
  url: https://github.com/BadgePiratesLLC/BSidesCHS_2022
  kind: repo
- label: docs.badgepirates.com/catalog
  url: https://docs.badgepirates.com/catalog/
  kind: website
images:
- file: assets/images/badges/bsides-charleston-2022/bsides-charleston-2022-badge/2d577a8140.jpg
  source: https://github.com/BadgePiratesLLC/BSidesCHS_2022
  credit: Badge Pirates
  caption: Front of the BSides Charleston 2022 badge PCB
- file: assets/images/badges/bsides-charleston-2022/bsides-charleston-2022-badge/cde8c642f8.jpg
  source: https://github.com/BadgePiratesLLC/BSidesCHS_2022
  credit: Badge Pirates
  caption: Back of the BSides Charleston 2022 badge PCB
contact: {}
notes:
- Badge Pirates' conference badge for BSides Charleston 2022, with CAD, firmware/code, and image folders in the (now archived) GitHub repo. Found by the event-year sweep, task bsides-huntsville.
- The sweep's title matched the maker's own repo naming exactly; no wording change needed.
status: released
sources:
- kind: url
  url: https://github.com/BadgePiratesLLC/BSidesCHS_2022
  title: BSides Charleston 2022 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-huntsville); event read as ''BSides Charleston 2022''.'
- kind: url
  url: https://github.com/BadgePiratesLLC/BSidesCHS_2022/blob/main/Code/main.ino
  title: main.ino
  accessed: '2026-09-10'
  note: 'Firmware source: confirms ESP8266 target, WiFi AP + web server CTF (192.168.4.1), 4 discrete LEDs on GPIO 16/13/12/14, and a serial 3-digit-PIN challenge.'
- kind: url
  url: https://github.com/BadgePiratesLLC/BSidesCHS_2022/tree/main/CAD
  title: CAD folder (BsidesCHS-2022-Badge KiCad project)
  accessed: '2026-09-10'
  note: Confirms KiCad project files and a gerbers folder are published alongside the firmware.
- kind: url
  url: https://docs.badgepirates.com/catalog/
  title: Badge Pirates catalog
  accessed: '2026-09-10'
  note: Lists the badge under BSides Charleston 2022 with a link back to the same GitHub repo; no additional specs, price, quantity, or images.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: The GitHub repo and firmware confirm the badge is a real, released ESP8266 CTF badge with full open-source design files, but neither the repo nor the Badge Pirates catalog states price, quantity made, exact distribution method, or battery/power source. No third-party coverage (Hackaday, forums, social posts) was found describing this specific badge. Front/back PCB photos were recovered from the repo's Images folder.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsides-charleston-2022/bsides-charleston-2022-badge.glb
  method: kicad
  source_file: CAD/BsidesCHS-2022-Badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 262076
---

Badge Pirates built the official conference badge for BSides Charleston 2022 around an ESP8266, giving it a small built-in capture-the-flag challenge rather than pure decorative blinky. On boot the badge starts its own WiFi access point and a lightweight web server at 192.168.4.1; visiting the page and submitting the right "plaintext" value solves one flag, while a separate 3-digit PIN challenge is entered over a serial connection. Four LEDs, wired directly to GPIO pins rather than addressable RGB, step through a small state machine to show which flags have been solved.

The PCB itself carries a hammock/beach-themed illustration on the silkscreen, fitting Charleston's coastal setting. Badge Pirates published the full project on GitHub, including the KiCad schematic, PCB layout, and gerbers under a CAD folder, plus the Arduino/ESP8266 firmware under Code — making it straightforward for someone else to reproduce or build on the badge's CTF firmware.

Neither the repository nor Badge Pirates' own catalog page state a price, production quantity, or exactly how badges were handed out at the event, so those fields are left blank pending a source that covers them.

## Make your own

The hardware and firmware are both published in the [BSidesCHS_2022 repo](https://github.com/BadgePiratesLLC/BSidesCHS_2022): open the `CAD` folder's KiCad project (schematic, PCB, and a `gerbers` subfolder) to fab the board, and flash `Code/main.ino` to an ESP8266 to reproduce the on-badge CTF.
