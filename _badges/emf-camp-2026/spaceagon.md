---
title: Spaceagon
id: emf-camp-2026-spaceagon
layout: badge
parent: EMF Camp 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: emf-camp-2026
year: 2026
makers:
- name: EMF Camp badge team
  url: https://www.emfcamp.org/badge
summary: 'The official 2026 EMF Camp badge, a space-themed successor to the Tildagon platform with a round display, RGB LEDs, six hexpansion expansion slots, and a compass and joystick.'
functions: 'General-purpose hackable badge running MicroPython; six hexpansion slots for add-ons (the first official one is a keyboard); IMU-driven motion sensing; WiFi/BLE for badge apps and networking.'
look:
  colors: []
  shape: hexagon
  themes:
  - space
  - sci-fi
tech:
  mcu: ESP32-S3
  leds: null
  display: round display
  connectivity:
  - wifi
  - ble
  battery: compatible with 2016/2018 EMF badge batteries
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution:
  - purchase
  where: 'Sold to attendees at EMF Camp 2026; existing Tildagon owners can instead buy a Spaceagon front-board upgrade kit to swap onto their existing badge.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/emfcamp/badge-2024-hardware
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2026/06/02/the-2026-emf-badge-arrives-with-an-add-on-as-expected-its-familiar
  url: https://hackaday.com/2026/06/02/the-2026-emf-badge-arrives-with-an-add-on-as-expected-its-familiar/
  kind: article
- label: emfcamp.org/badge
  url: https://www.emfcamp.org/badge
  kind: website
- label: tildagon.badge.emfcamp.org
  url: https://tildagon.badge.emfcamp.org
  kind: doc
images:
- file: assets/images/badges/emf-camp-2026/spaceagon/f1b96653d3.jpg
  source: "https://hackaday.com/2026/06/02/the-2026-emf-badge-arrives-with-an-add-on-as-expected-its-familiar/"
  credit: "EMF Camp / Hackaday"
  caption: "Prototype Spaceagon badge, the 2026 EMF Camp badge (final badge art differs from the prototype shown)"
contact: {}
notes:
- Update to Tildagon; sold with an upgrade front panel for existing owners
- 'Design for 2026 was not yet finalized as of the badge team''s own site; the Hackaday article notes the final badge art will differ from the prototype pictured.'
status: announced
sources:
- kind: url
  url: https://hackaday.com/2026/06/02/the-2026-emf-badge-arrives-with-an-add-on-as-expected-its-familiar/
  title: Spaceagon
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''EMF Camp 2026''.'
- kind: url
  url: https://www.emfcamp.org/badge
  title: EMF Camp Badge
  accessed: '2026-09-07'
  note: 'Official badge page; confirms Spaceagon is the space-themed 2026 badge and that an upgrade front-board kit is sold to returning Tildagon owners. States the 2026 design was not yet released at time of check.'
- kind: url
  url: https://tildagon.badge.emfcamp.org
  title: Tildagon badge documentation
  accessed: '2026-09-07'
  note: 'Platform docs: ESP32-S3 MCU, 2MB PSRAM, 8MB flash, round display, six buttons, RGB LEDs, IMU, WiFi/BLE, USB-C, MicroPython firmware; confirms Spaceagon keeps the hexagonal six-hexpansion-slot form factor; links hardware repo emfcamp/badge-2024-hardware.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Spaceagon is the 2026 EMF Camp badge, a space-themed iteration of the reusable Tildagon platform
    (hexagonal, ESP32-S3, six hexpansion slots). Core MCU/platform specs come from the Tildagon project
    docs (which describe the ongoing platform generally, not confirmed 2026-specific LED count/exact
    display size). As of the last check the EMF Camp badge page itself said the 2026 design had not been
    finalized/released, so pricing, quantity, and final art are unknown. The first official hexpansion
    accessory is a rubber-keyboard add-on connecting via edge connector. hardware_url points to the
    emfcamp/badge-2024-hardware repo referenced by the Tildagon docs; a 2026-specific hardware repo was
    not located, so open_source is marked partial pending confirmation.
last_modified_date: '2026-09-07'
---

The Spaceagon is the 2026 EMF Camp badge, the latest edition of the EMF badge team's Tildagon platform — a hexagonal, reusable badge design built so that software written for one year's badge keeps working on later ones. It keeps the Tildagon's core hardware: an ESP32-S3 microcontroller running MicroPython, a round display, RGB LEDs, six buttons, an IMU for motion sensing, WiFi and Bluetooth, and USB-C power (compatible with battery packs from the 2016 and 2018 EMF badges). Where earlier Tildagon badges carried a "solarpunk" design, Spaceagon swaps in a space theme, and adds a compass and joystick along with refined button, LED, and display mounting.

Spaceagon keeps the Tildagon's signature hexagonal shape with six hexpansion expansion slots. The first official hexpansion for it is a small rubber-keyboard add-on that connects via edge connector rather than pins, reusing a rubber-moulding approach seen in prior maker projects for the platform. Existing Tildagon owners are not required to buy a whole new badge: EMF Camp is selling a Spaceagon front-board upgrade kit that lets them swap the front panel of a badge from a previous year onto the new space-themed design.

As of the last check, EMF Camp's own badge page stated that the full 2026 design had not yet been finalized or released, and Hackaday's coverage noted that the final badge art will differ from the prototype shown in early photos. Pricing, production quantity, and exact LED count/display specs for the finished badge were not available from the sources checked; the badge is expected to be sold to attendees at EMF Camp 2026.
