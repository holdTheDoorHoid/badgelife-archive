---
title: Communicator Badge Full RGB Keyboard
id: supercon-2025-communicator-badge-full-rgb-keyboard
layout: badge
parent: Supercon 2025
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2025
year: 2025
makers:
- name: makeTVee
  url: https://hackaday.io/makeTVee
summary: A replacement keyboard mod for the 2025 Supercon Communicator Badge, adding one addressable RGB LED under every key.
functions: Lights each keycap individually in RGB, driven by the badge's own MCU over MicroPython; purely a lighting/cosmetic upgrade, no new logic beyond that.
look:
  colors:
  - multicolor
  shape: null
  themes:
  - retro computer
tech:
  mcu: null
  leds:
    count: 73
    type: SK6805-EC4004
    note: 0.4mm side-emitting LEDs, one per key, driven from the host badge's GPIO
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://hackaday.io/project/205750-communicator-badge-full-rgb-keyboard
  firmware_url: null
  eda_tool: KiCad
  notes: KiCad PCB source, Gerbers, and STL files for the resin-printed keycaps (alpha, number, and function keys) are published on the project page.
links:
- label: hackaday.io/project/205750-communicator-badge-full-rgb-keyboard
  url: https://hackaday.io/project/205750-communicator-badge-full-rgb-keyboard
  kind: hackaday
images:
- file: assets/images/badges/supercon-2025/communicator-badge-full-rgb-keyboard/2d5ae29235.jpg
  source: "https://hackaday.io/project/205750-communicator-badge-full-rgb-keyboard"
  credit: "makeTVee"
  caption: "The RGB keyboard PCB with 73 addressable SK6805-EC4004 side-emitting LEDs, one per key"
- file: assets/images/badges/supercon-2025/communicator-badge-full-rgb-keyboard/a5cee73093.jpg
  source: "https://hackaday.io/project/205750-communicator-badge-full-rgb-keyboard"
  credit: "makeTVee"
  caption: "Resin-printed semi-transparent keycaps with hand-marked letters installed on the badge"
contact: {}
notes:
- A custom front PCB with 73 addressable side-emitting LEDs (one per key) plus a resin-printed semi-transparent keyboard, replacing the stock keyboard on the 2025 Supercon Communicator Badge. Found by the event-year sweep, task supercon-2025.
- 'Maker''s own project title matches the sweep''s wording exactly; no correction needed.'
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/205750-communicator-badge-full-rgb-keyboard
  title: Communicator Badge Full RGB Keyboard
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2025); event read as ''supercon-2025''.'
- kind: url
  url: https://hackaday.io/project/205750-communicator-badge-full-rgb-keyboard
  title: Communicator Badge Full RGB Keyboard
  accessed: '2026-09-08'
  note: Confirmed maker, feature set (LED count/type, keyboard fabrication method), and open-source file listing (KiCad, Gerbers, STL).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Documented as a one-off prototype mod on the maker's own Hackaday.io project page; no price, quantity, or distribution info given since it was never sold or distributed, only shared as an open-source build. No separate storefront or social posts found in the budget allotted.
last_modified_date: '2026-09-08'
---

A custom keyboard mod for the 2025 Hackaday Supercon Communicator Badge, built by maker makeTVee. It replaces the stock keyboard with a custom front PCB carrying 73 addressable SK6805-EC4004 side-emitting LEDs, one under every key, wired into the host badge's own MCU and driven over MicroPython. The keycaps themselves are resin-printed in a semi-transparent material with hand-marked letters, so each key glows individually.

The project is documented as a single prototype rather than something sold or given away, but makeTVee published the full build as open source: KiCad PCB source, Gerber manufacturing files, and STL files for the 3D-printed alpha, number, and function keycaps are all available on the Hackaday.io project page for anyone who wants to replicate the mod on their own Communicator Badge.

## Make your own

The project page (linked above) provides everything needed to reproduce the mod: KiCad source and Gerbers for the LED PCB, and STL files for resin-printing the semi-transparent keycap set. Builders would need their own 2025 Supercon Communicator Badge to mount the replacement keyboard onto.
