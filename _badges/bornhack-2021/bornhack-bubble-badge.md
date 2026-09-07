---
title: BornHack Bubble Badge
id: bornhack-2021-bornhack-bubble-badge
layout: badge
parent: BornHack 2021
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: bornhack-2021
year: 2021
makers:
- name: Inne (attendee project)
  url: https://hackaday.io/inne
summary: 'An attendee-built add-on for the BornHack 2021 hex DIY badge: an inflatable, color-changing bubble with a pressure sensor and NeoPixel lighting.'
functions: 'Inflates a soft bubble via an air pump and monitors the pressure with a sensor; lights the bubble with a single NeoPixel (WS2812) whose color is programmed in CircuitPython.'
look:
  colors: [multicolor, clear]
  shape: null
  themes: [wearable, hardware tool, kit]
tech:
  mcu: QTPy SAMD21
  leds:
    count: 1
    type: WS2812B
    note: Single NeoPixel used for the bubble's color-changing light.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'A one-off project built by an attendee for personal use at BornHack 2021; not distributed or sold.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/bornhack/badge2021
  firmware_url: null
  eda_tool: KiCad
  notes: 'The hardware_url is for the official BornHack 2021 "hex DIY" badge PCB this project was built on top of (CC BY-SA 4.0, designed in KiCad nightly 5.99); the bubble mechanism and its CircuitPython code were not found published separately.'
links:
- label: hackaday.io/project/181411-bornhack-bubble-badge
  url: https://hackaday.io/project/181411-bornhack-bubble-badge
  kind: hackaday
- label: bornhack/badge2021 (base badge repo)
  url: https://github.com/bornhack/badge2021
  kind: repo
images:
  - file: assets/images/badges/bornhack-2021/bornhack-bubble-badge/7ea5b8f1b0.jpg
    source: "https://hackaday.io/project/181411-bornhack-bubble-badge"
    credit: "Inne"
    caption: "The BornHack Bubble Badge, an inflatable NeoPixel badge"
  - file: assets/images/badges/bornhack-2021/bornhack-bubble-badge/47a1600b9b.jpg
    source: "https://hackaday.io/project/181411-bornhack-bubble-badge"
    credit: "Inne"
    caption: "Build progress photo of the bubble badge"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://hackaday.io/project/181411-bornhack-bubble-badge
  title: BornHack Bubble Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''bornhack-2021''.'
- kind: url
  url: https://github.com/bornhack/badge2021
  title: bornhack/badge2021
  accessed: '2026-09-07'
  note: 'Confirmed as the official BornHack 2021 "hex DIY" badge repo the bubble badge was built on; CC BY-SA 4.0, KiCad nightly 5.99, has an SAO/Qwiic header.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is an attendee mod of the official BornHack 2021 badge, not a standalone commercial product, so price/quantity/availability fields do not apply and were left empty. The bubble mechanism''s own firmware/hardware files were not found published (only the base badge repo was located). Component list per Hackaday: 1x NeoPixel, 2x TIP120 transistors, 3x 1A Schottky diodes, 19 parts total. Fact-check pass: tech.sao_version was blanked from ''v1'' to null - neither the Hackaday project page nor the badge2021 repo states an SAO pin count/version, only that the base badge has an SAO/Qwiic breakout. Everything else in the entry was verified against the two cited sources and left as-is.'
last_modified_date: '2026-09-07'
---

The BornHack Bubble Badge is an attendee project built for BornHack 2021, the annual Danish hacker camp, by a maker known as Inne on Hackaday.io. Rather than a standalone badge, it is an add-on built on top of the event's official "hex DIY" badge (an open-source KiCad design from the BornHack hardware village with a Shitty Add-On header). Inne adapted an earlier soft-robotics bubble prototype into a wearable that inflates a small bubble using an air pump and two TIP120 transistors, while a pressure sensor monitors the inflation level.

The bubble is lit by a single WS2812 NeoPixel, driven by a QT Py SAMD21 microcontroller running CircuitPython, so the color can change as part of the badge's behavior. The project page lists about 19 components in total, including three 1A Schottky diodes alongside the transistors and LED. It appears to have been a one-off build for personal use at the event rather than something distributed to other attendees, and no separate hardware or firmware repository for the bubble mechanism itself was found — only the base badge design it was built on.
