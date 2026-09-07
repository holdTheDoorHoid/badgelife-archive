---
title: Ph0xx
id: fri3d-2018-ph0xx
layout: badge
parent: Fri3d 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: fri3d-2018
year: 2018
makers:
- name: Fri3d Camp
  url: https://github.com/Fri3dCamp
summary: Ph0xx is the ESP32-WROOM-32 attendee badge for Fri3d Camp 2018 in Belgium (about 600 made), with two 5x7 LED matrices, an ADXL345 accelerometer, 18650 battery with TP4056/DW01-P charging and protection, touch buttons, buzzer, expansion headers and Lego Technic compatible holes, designed by Wim Van Gool and Bert Outtier.
functions: Blinky/LED-eye display modes with a browser-based animation editor built by Area 3001 volunteers for programming the matrices; expandable through "Jewel" add-on modules (an Air Jewel for environmental sensors and a Bot Jewel for servo control) plugged into the badge's headers.
look:
  colors: []
  shape: null
  themes:
  - robot
  - wearable
tech:
  mcu: ESP32-WROOM-32
  leds:
    count: 70
    type: discrete
    note: Two 5x7 LED matrices used as animated "eyes"; some units were built with blue LEDs, others modified to green.
  display: LED matrix 5x7 (x2)
  connectivity:
  - wifi
  - ble
  - i2c
  battery: 18650 Li-ion with TP4056 charge controller and DW01-P protection IC
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'about 600'
  availability: unknown
  distribution:
  - free_drop
  where: Given to Fri3d Camp 2018 attendees in Belgium; badges were hand-soldered in early builds and later mass-produced (460 boards assembled in one day at More-at-Mere).
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Fri3dCamp/badge
  firmware_url: https://github.com/Fri3dCamp/Fri3dBadge
  eda_tool: null
links:
- label: hackaday.io/project/160451-ph0xx
  url: https://hackaday.io/project/160451-ph0xx
  kind: hackaday
- label: github.com/Fri3dCamp/badge
  url: https://github.com/Fri3dCamp/badge
  kind: repo
- label: github.com/Fri3dCamp/Fri3dBadge
  url: https://github.com/Fri3dCamp/Fri3dBadge
  kind: repo
- label: fri3d.be
  url: http://fri3d.be/
  kind: website
images:
- file: assets/images/badges/fri3d-2018/ph0xx/c9b8bf3af3.jpg
  source: "https://hackaday.io/project/160451-ph0xx"
  credit: "Fri3d Camp"
  caption: "The Ph0xx badge with its two 5x7 LED matrices"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/160451-ph0xx
  title: Ph0xx
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/160451-ph0xx
  title: Ph0xx
  accessed: '2026-09-07'
  note: "Maker's own project page; confirmed maker names, event/year, ~600 units, ESP32-WROOM-32, two 5x7 LED matrices, ADXL345, 18650/TP4056/DW01-P power, touch buttons, buzzer, Lego Technic holes, and the Area 3001 web animation tool. Source of the saved photo."
- kind: url
  url: https://github.com/Fri3dCamp/badge
  title: Fri3dCamp/badge
  accessed: '2026-09-07'
  note: "Hardware design repo for the Fri3d Camp 2018 badge; confirms design files/datasheets are published there and points to fri3d.be/badge and the 2018 camp wiki for more detail."
- kind: url
  url: https://github.com/Fri3dCamp/Fri3dBadge
  title: Fri3dCamp/Fri3dBadge
  accessed: '2026-09-07'
  note: "Arduino library/firmware repo for the badge; confirms ESP32, ADXL345, two buttons plus two touchpads, buzzer, 5x7-ish LED matrix support, and Servo Jewel add-on."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: "Core facts (maker, event/year, chip, LEDs, battery, quantity) confirmed on the maker's own Hackaday project page and corroborated by the Fri3dCamp/badge and Fri3dCamp/Fri3dBadge GitHub repos. Price and a firm availability status were not stated anywhere found; badges were a free attendee drop rather than sold, so get_one.price is left empty and availability is left unknown (some Jewel accessories were separately built by third parties but that is out of scope for this badge entry). fri3d.be's current site (2026) only briefly mentions later-year badges and had nothing on the 2018 unit. The wiki2018.fri3d.be badge page could not be reached (self-signed TLS certificate blocked the fetch); it may hold further detail (e.g. price/BOM) that a future pass with a certificate-tolerant fetch could recover."
last_modified_date: '2026-09-07'
---

Ph0xx was the attendee badge for Fri3d Camp 2018, a family hacker/maker/DIY camp in Belgium, designed by Wim Van Gool and Bert Outtier for the Fri3d Camp team. Built around an ESP32-WROOM-32, it wears two 5x7 LED matrices as animated eyes, an ADXL345 accelerometer for motion-reactive effects, touch buttons, and a buzzer, all powered by a rechargeable 18650 cell with TP4056 charging and DW01-P protection. The board even includes Lego Technic-compatible mounting holes so it could be built into camp builds. Roughly 600 were made and given to attendees; after early units were hand-soldered, the bulk of the run (460 boards in a single day) was mass-produced at a facility called More-at-Mere.

The badge could be extended with plug-in "Jewel" modules, including an Air Jewel carrying environmental sensors and a Bot Jewel for driving servos, and camp volunteers from Area 3001 built a browser-based animation tool for programming the LED-eye patterns.

## Make your own

Both the hardware design and firmware are published on GitHub under the Fri3dCamp organization: `Fri3dCamp/badge` holds the board design and datasheets, and `Fri3dCamp/Fri3dBadge` is the Arduino library used to program the ESP32, its LED matrices, buttons/touchpads, buzzer, and the Servo Jewel accessory.
