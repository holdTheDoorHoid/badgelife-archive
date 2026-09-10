---
title: BSidesPDX 2015 Badger Badge
id: bsides-portland-2015-bsidespdx-2015-badger-badge
layout: badge
parent: BSidespdx 2015
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-portland-2015
year: 2015
makers:
- name: PDX Badgers
  url: https://github.com/pdxbadgers
summary: An ESP8266-based hands-on hacking badge built by PDX Badgers for a BSidesPDX 2015 workshop, running a web UI over its own Wi-Fi hotspot.
functions: 'Runs an onboard HTTP server with a /flag endpoint for storing and updating CTF flags and a /leds endpoint for controlling LED state, color, and animation mode (blink, chase, twinkle, all, none). Broadcasts its own Wi-Fi hotspot ("BadgerNet") with mDNS discovery.'
look:
  colors: []
  shape: badger
  themes:
  - animal
  - mascot
  - learn to solder
  - ctf
tech:
  mcu: ESP8266
  leds:
    count: 5
    type: RGB
    note: Four monochrome LEDs on tail/feet/nose pins plus one RGB LED for the eye.
  display: null
  connectivity:
  - wifi
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to attendees of a hardware hacking workshop at BSidesPDX 2015.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/pdxbadgers/pcb-2015
  firmware_url: https://github.com/pdxbadgers/fw-2015
  eda_tool: Eagle
  notes: 'Hardware repo (PCB, Gerbers, OSH Park design rules) is licensed CC BY-SA 3.0; the firmware repo carries no explicit license statement.'
links:
- label: badge.gallery/badges/bsidespdx-2015-badger-badge
  url: https://badge.gallery/badges/bsidespdx-2015-badger-badge
  kind: website
- label: pdxbadgers/pcb-2015 (hardware)
  url: https://github.com/pdxbadgers/pcb-2015
  kind: repo
- label: pdxbadgers/fw-2015 (firmware)
  url: https://github.com/pdxbadgers/fw-2015
  kind: repo
images: []
contact: {}
notes:
- ESP8266-based hackable conference badge for BSidesPDX 2015. Found by the event-year sweep, task bsides-portland.
- 'The workshop was presented by Michael Leibowitz; the public hardware and firmware repos are published under the PDX Badgers GitHub org.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/bsidespdx-2015-badger-badge
  title: BSidesPDX 2015 Badger Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-portland); event read as ''BSidesPDX 2015''.'
- kind: url
  url: https://github.com/pdxbadgers/pcb-2015
  title: pdxbadgers/pcb-2015
  accessed: '2026-09-10'
  note: Hardware repo confirming ESP8266 badge, Eagle CAD design files, Gerbers, CC BY-SA 3.0 license, and BSides Portland branding.
- kind: url
  url: https://github.com/pdxbadgers/fw-2015
  title: pdxbadgers/fw-2015
  accessed: '2026-09-10'
  note: Firmware repo confirming Arduino-based ESP8266 firmware with /flag and /leds HTTP endpoints, no license statement found.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'No documentary photo of the assembled/soldered badge was found on badge.gallery or in either GitHub repo (only conference logo art and PCB design assets); images left empty rather than guessed. Price, quantity made, and battery details are not documented anywhere found. Distribution context (workshop-based hands-out) does not map cleanly to the controlled distribution vocabulary, so get_one.distribution was left empty and described in get_one.where instead.'
last_modified_date: '2026-09-10'
---

The Badger Badge was built by PDX Badgers for a hands-on hardware hacking workshop at BSidesPDX 2015, presented by Michael Leibowitz. It is an ESP8266-based board that runs its own web server and broadcasts a Wi-Fi hotspot nicknamed "BadgerNet," so attendees could connect and interact with the badge over HTTP rather than a serial console. Onboard are four monochrome LEDs (tail, feet, nose) and one RGB LED for the eye, all controllable through a `/leds` endpoint that supports several animation modes (blink, chase, twinkle) alongside solid colors.

The badge doubled as a small CTF exercise: a `/flag` endpoint let the firmware store and serve capture-the-flag flags, giving workshop attendees something concrete to probe and modify as they learned to work with the hardware and its web interface.

## Make your own

PDX Badgers published both halves of the project on GitHub. The hardware repo (`pcb-2015`) contains Eagle CAD schematics and board files, three sets of Gerbers, an OSH Park design-rule file, and the badger/gear artwork used on the silkscreen, released under CC BY-SA 3.0. The firmware repo (`fw-2015`) contains the Arduino-based `badger.ino` sketch along with `leds.cpp/h` and `configspace.cpp/h`, implementing the LED control and flag-storage HTTP endpoints; no explicit license is stated for the firmware.
