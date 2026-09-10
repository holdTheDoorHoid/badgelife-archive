---
title: BSidesSLC 2015 Electronic Badge
id: bsides-slc-2015-bsidesslc-2015-electronic-badge
layout: badge
parent: BSides Slc 2015
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-slc-2015
year: 2015
makers:
- name: theTransistor / D3c4f, Compukidmike, Devino, 801 Labs, DC801
summary: An Arduino-bootloaded conference badge with a Nokia 5110 LCD, a small 5-way joypad, and two action buttons, built for BSidesSLC 2015.
functions: 'Reprogrammable over USB (Arduino IDE) or a serial "HACK" ISP header; drives the Nokia 5110 LCD with adjustable backlight and software-adjustable contrast, read by the joypad and two action buttons; breaks out extra GPIO along the bottom edge for hacking.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ATmega32u4
  leds: null
  display: Nokia 5110 LCD (84x48)
  connectivity:
  - usb
  battery: 2x AAA (or USB power)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/thetransistor/BSidesSLC2015/tree/master/Hardware
  firmware_url: https://github.com/thetransistor/BSidesSLC2015/tree/master/Code
  eda_tool: null
links:
- label: github.com/thetransistor/BSidesSLC2015
  url: https://github.com/thetransistor/BSidesSLC2015
  kind: repo
images:
  - file: assets/images/badges/bsides-slc-2015/bsidesslc-2015-electronic-badge/5c6d4e6ed5.jpg
    source: "https://github.com/thetransistor/BSidesSLC2015"
    credit: "theTransistor / DC801 / 801 Labs"
    caption: "Badge PCB outline/design"
contact: {}
notes:
- Atmel ATmega32u4-based badge with a Nokia 5110 84x48 LCD, 5-way joypad plus two action buttons, USB or 2xAAA power, built by theTransistor/DC801/801 Labs for BSidesSLC 2015. Found by the event-year sweep, task bsides-bsides-slc.
- 'Sweep title matched the maker''s own repo/README title exactly ("BSidesSLC 2015 Electronic Badge"); no change needed.'
status: listed
sources:
- kind: url
  url: https://github.com/thetransistor/BSidesSLC2015
  title: BSidesSLC 2015 Electronic Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-slc); event read as ''BSides SLC 2015''.'
- kind: url
  url: https://raw.githubusercontent.com/thetransistor/BSidesSLC2015/master/README.md
  title: BSidesSLC2015 README
  accessed: '2026-09-10'
  note: 'Confirmed maker/team credits, MCU, display, controls, power, reprogramming method, and open-source hardware/firmware links.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Core facts confirmed directly from the maker''s own GitHub repo and README. No price, quantity made, or distribution/availability details are given anywhere in the repo, so those fields are left empty. No SAO header, LED count, or additional connectivity (beyond USB) is mentioned. No other photos of the assembled badge were found beyond the repo''s outline.png design image.'
last_modified_date: '2026-09-10'
---

The BSidesSLC 2015 Electronic Badge was built by theTransistor, DC801, and 801 Labs (Salt Lake City-area hacker groups) for the 2015 BSidesSLC conference. It centers on an Arduino-bootloaded ATmega32u4 running at 8MHz/3.3V, driving a Nokia 5110 LCD (84x48 pixels, adjustable backlight and software contrast) alongside a compact 5-way joypad and two action buttons. The board can run on USB or 2x AAA batteries and breaks out extra GPIO along its bottom edge for further hacking.

Design and firmware work was led by D3c4f, with electronics and processing handled by Compukidmike and Devino, and assembly/QA credited to l3mur (aarobc), Nemus, Compukidmike, and Yukaia. The maker's README notes the badge uses leftover, no-longer-produced Nokia 5110 displays sourced from old Chinese stock, and warns that some units may need gentle pressure on the LCD's metal frame to reseat a loose display connector.

## Make your own

Both hardware and firmware are published on GitHub under an open license. The badge can be reprogrammed over USB via the Arduino IDE (using SparkFun's 8MHz ATmega32u4 hardware files) or through a serial "HACK" ISP breakout header. Hardware files live under `Hardware/` and code under `Code/` in the [thetransistor/BSidesSLC2015](https://github.com/thetransistor/BSidesSLC2015) repository.
