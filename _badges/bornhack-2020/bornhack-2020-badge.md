---
title: BornHack 2020 badge
id: bornhack-2020-bornhack-2020-badge
layout: badge
parent: Bornhack 2020
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bornhack-2020
year: 2020
makers:
- name: Thomas Flummer
  url: https://github.com/bornhack/badge2020
- name: BornHack
summary: 'The official electronic badge for BornHack 2020, an arc-shaped PCB with a 9x32 SMD LED matrix, designed to tile into a seamless multi-badge display when several are placed edge to edge.'
functions: 'Runs Adafruit CircuitPython, editable over USB mass storage as a code.py file with no toolchain required. Drives animations/games on the 9x32 LED matrix, and sends/receives badge-to-badge messages over infrared.'
look:
  colors: []
  shape: circle
  themes:
  - hardware tool
  - minimalist
tech:
  mcu: SAMD21G18A
  leds:
    count: 288
    type: charlieplexed
    note: 9x32 SMD LED matrix driven by two IS31FL3731 charlieplexing LED controllers
  display: LED matrix 9x32
  connectivity:
  - ir
  - usb
  inputs:
  - buttons
  battery: 2x AA
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Given to BornHack 2020 attendees; exact distribution terms (included with ticket vs. separate) not stated in sources found.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/bornhack/badge2020
  firmware_url: https://github.com/bornhack/badge2020
  eda_tool: null
  license: CC-BY-SA-4.0
links:
- label: github.com/bornhack/badge2020
  url: https://github.com/bornhack/badge2020
  kind: repo
- label: 'Hackaday: Hands-On: BornHack 2020 Badge Has 9x32 Of Bling Fed By CircuitPython'
  url: https://hackaday.com/2020/08/27/hands-on-bornhack-2020-badge-has-9x32-of-bling-fed-by-circuitpython/
  kind: article
- label: 'Adafruit blog: The Bornhack Badge 2020, programmable in CircuitPython'
  url: https://blog.adafruit.com/2020/09/02/the-bornhack-badge-2020-programmable-in-circuitpython-circuitpython-circuitpythonday-badgelife/
  kind: article
images:
  - file: assets/images/badges/bornhack-2020/bornhack-2020-badge/2e48cc7570.jpg
    source: "https://hackaday.com/2020/08/27/hands-on-bornhack-2020-badge-has-9x32-of-bling-fed-by-circuitpython/"
    credit: "Hackaday / Thomas Flummer"
    caption: "BornHack 2020 badge, 9x32 LED matrix arc-shaped PCB"
  - file: assets/images/badges/bornhack-2020/bornhack-2020-badge/c078cee471.jpg
    source: "https://hackaday.com/2020/08/27/hands-on-bornhack-2020-badge-has-9x32-of-bling-fed-by-circuitpython/"
    credit: "Hackaday / Thomas Flummer"
    caption: "BornHack 2020 badge lit up, showing the LED matrix and SAO connector"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/bornhack/badge2020
  title: BornHack 2020 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''bornhack-2020''.'
- kind: url
  url: https://hackaday.com/2020/08/27/hands-on-bornhack-2020-badge-has-9x32-of-bling-fed-by-circuitpython/
  title: 'Hands-On: BornHack 2020 Badge Has 9x32 Of Bling Fed By CircuitPython'
  accessed: '2026-09-07'
  note: 'Confirmed designer (Thomas Flummer), exact shape (72-degree arc, 1/5 of a circle), LED matrix and MCU details, battery/USB power, source of photos.'
- kind: url
  url: https://blog.adafruit.com/2020/09/02/the-bornhack-badge-2020-programmable-in-circuitpython-circuitpython-circuitpythonday-badgelife/
  title: 'The Bornhack Badge 2020, programmable in CircuitPython'
  accessed: '2026-09-07'
  note: 'Corroborated CircuitPython programming model and hardware summary.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'PCB solder-mask color not confirmed in any source found, so look.colors left empty. Price, quantity made, and exact distribution mechanism (bundled with ticket vs. separate) were not stated in the sources checked; get_one.price/quantity left empty and distribution/where marked accordingly. Shape recorded as circle (an exact 1/5 arc of a circle per the designer, meant to tile into a multi-badge display) since no more specific vocabulary term fits.'
last_modified_date: '2026-09-07'
---

The BornHack 2020 badge is the official electronic conference badge handed out at BornHack, the Danish outdoor hacker camp, for its 2020 edition. Designed by Thomas Flummer and manufactured in Denmark, it takes the form of a PCB cut to an exact one-fifth arc of a circle (72 degrees), with LED spacing along the edge deliberately matched so that several badges placed together tile into one seamless display. The front is dominated by a 9x32 array of SMD LEDs driven by two IS31FL3731 charlieplexing controllers, alongside a four-button navigation array and an unpopulated Shitty Add-On v1.69bis header; the back carries exposed GPIO pads and a pair of AA battery holders.

At its core is a SAMD21G18A ARM Cortex M0+ microcontroller, offering roughly four times the flash and RAM of the chips used in BornHack's earlier badges, backed by 4MB of SPI flash. The badge runs Adafruit CircuitPython out of the box, so attendees could edit a `code.py` file over a USB mass-storage connection without installing any development toolchain. Badges could also exchange short messages with each other over an onboard infrared transmitter/receiver pair. The hardware and firmware are released under a CC-BY-SA-4.0 license via the `bornhack/badge2020` GitHub repository.

## Make your own

The full hardware design files and CircuitPython firmware are published at github.com/bornhack/badge2020 under CC-BY-SA-4.0. Building or reflashing one would mean cloning that repository for the schematics/PCB files and firmware source, then copying updated CircuitPython code onto the badge's USB mass-storage drive as `code.py`.
