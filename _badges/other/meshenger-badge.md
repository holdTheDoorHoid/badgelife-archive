---
title: Meshenger Badge
id: other-meshenger-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2016
makers:
- name: Gee Bartlett
  url: https://hackaday.io/gee-bartlett
  role: ''
summary: An ESP8266-based open-source off-network mesh messaging badge, inspired by the radio badges seen at EMF Camp and similar events.
functions: Peer-to-peer text messaging over Wi-Fi without needing existing network infrastructure, aimed at conference/event use.
look:
  colors: []
  shape: null
  themes:
  - radio
  - privacy
  - hardware tool
tech:
  mcu: ESP8266
  leds: null
  display: unspecified (project describes an onboard display, type not stated)
  connectivity:
  - wifi
  battery: optional onboard battery attachment (unspecified)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/9777-meshenger-badge
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/9777-meshenger-badge
  url: https://hackaday.io/project/9777-meshenger-badge
  kind: hackaday
images:
- file: assets/images/badges/other/meshenger-badge/37e916a2cf.jpg
  source: "https://hackaday.io/project/9777-meshenger-badge"
  credit: "Gee Bartlett"
  caption: "Meshenger Badge project image"
- file: assets/images/badges/other/meshenger-badge/32729cb1d0.jpg
  source: "https://hackaday.io/project/9777-meshenger-badge"
  credit: "Gee Bartlett"
  caption: "PCB board preview render"
contact: {}
notes: []
status: unknown
sources:
- kind: url
  url: https://hackaday.io/project/9777-meshenger-badge
  title: Meshenger Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/9777-meshenger-badge
  title: Meshenger Badge - Hackaday.io project page
  accessed: '2026-09-07'
  note: 'Primary source for description, maker, MCU, design goals, and open-source status.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    This is a personal hobby project by Gee Bartlett (started Feb 2016 on Hackaday.io),
    not a badge made for or distributed at a specific convention -- it says it was
    inspired by the radio badges seen at EMF Camp and similar events, but does not
    claim to have been made for or issued at any particular one. The project appears
    to have been shelved without a completed build: no price, quantity, release, or
    firmware repository was found, and the PCB spec (2-layer, max 50x50mm, single-side
    SMT, BOM target under GBP10) reads as a design goal rather than a confirmed final
    product. LED count, display type, and battery type are not specified on the source
    page. No firmware link was found despite the page mentioning Arduino IDE compatibility.
    A related follow-up project exists, "Meshanger Badge V" (hackaday.io/project/176020),
    an ESP32-C3 reboot by a different/unclear author -- not the same item, noted here
    as a possible separate entry.
last_modified_date: '2026-09-07'
---

The Meshenger Badge is a personal open-source hardware project by Gee Bartlett, posted to Hackaday.io in February 2016. It was inspired by the radio badges seen at EMF Camp and similar events, and set out to build an off-network mesh messaging badge for wearing at conferences -- using Wi-Fi and a custom messaging protocol to let attendees exchange text without relying on venue infrastructure, in the name of privacy and freedom of information.

The design centers on an ESP8266 module, with a 2-layer PCB constrained to 50mm x 50mm and 1.6mm thick, single-sided SMT assembly to keep hand-soldering minimal, and a target bill of materials under GBP10 including assembly. The page describes an onboard display and physical controls (tactile switches or a joystick) and an optional battery attachment, though none of these are specified further. The stated design goals were low cost, hackability, open-source design, wearability, and an attractive form factor with rounded corners.

The project does not appear to have reached a finished, distributed product -- there is no evidence of a price, a quantity built, or a public firmware repository, and the Hackaday.io page has seen no updates since shortly after it was posted. It is treated here as never released. A later, apparently unrelated ESP32-C3-based project called "Meshanger Badge V" exists on Hackaday.io and may warrant its own entry.
