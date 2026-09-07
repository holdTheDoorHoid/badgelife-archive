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
  url: https://hackaday.io/RabidInventor
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
  open_source: null
  hardware_url: null
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
  caption: "PCB board preview render (boardprev1.png)"
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
- kind: url
  url: https://hackaday.io/project/9777-meshenger-badge
  title: Meshenger Badge - Hackaday.io project page (fact-check re-fetch)
  accessed: '2026-09-07'
  note: 'Fact-check pass: verified author profile link, confirmed the two saved images are duplicates of the single Files-section attachment, and confirmed no hardware/firmware design files (only a preview image) are actually published.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    Fact-check pass (2026-09-07) re-fetched the Hackaday.io source and made three
    corrections to the prior research pass: (1) the maker's profile URL was wrong
    (https://hackaday.io/gee-bartlett 404s) -- corrected to the actual author link
    on the page, https://hackaday.io/RabidInventor (display name "Gee Bartlett").
    (2) The two saved images were byte-identical duplicates of the single file the
    project page actually offers (boardprev1.png, a PCB layout preview) -- one was
    mislabeled "Meshenger Badge project image" as if it were a separate photo; the
    duplicate file was deleted and the remaining image's caption corrected to match
    what it actually shows. (3) make_your_own.open_source was set to "partial" and
    hardware_url pointed at the project page, but the page's Files section contains
    only that one preview image -- no schematic, gerbers, BOM, or firmware/GitHub
    link is published, only a stated intent to be open source ("Open Source" is
    listed as a design goal, caveated by ESP8266 libraries being closed). Neither
    hardware nor firmware design files are actually available, so open_source and
    hardware_url were both cleared to null.
    Everything else in the entry (maker, MCU/ESP8266 via ESP-12F module, wifi
    connectivity, unspecified display/battery, PCB spec of 2-layer/max 50x50mm/
    single-side SMT/BOM target under GBP10, rounded-corner wearable design goals,
    privacy/freedom-of-information motivation, EMF Camp-style inspiration, Feb 2016
    posting date, and shelved/not_released status) was independently confirmed
    against the source page and is unchanged. This remains a personal hobby project,
    not a badge made for or distributed at a specific convention, so event: other is
    correct. A related follow-up project, "Meshanger Badge V" (hackaday.io/project/176020),
    an ESP32-C3 reboot by a different/unclear author, is not the same item and may
    warrant its own entry.
last_modified_date: '2026-09-07'
---

The Meshenger Badge is a personal open-source hardware project by Gee Bartlett, posted to Hackaday.io in February 2016. It was inspired by the radio badges seen at EMF Camp and similar events, and set out to build an off-network mesh messaging badge for wearing at conferences -- using Wi-Fi and a custom messaging protocol to let attendees exchange text without relying on venue infrastructure, in the name of privacy and freedom of information.

The design centers on an ESP8266 module, with a 2-layer PCB constrained to 50mm x 50mm and 1.6mm thick, single-sided SMT assembly to keep hand-soldering minimal, and a target bill of materials under GBP10 including assembly. The page describes an onboard display and physical controls (tactile switches or a joystick) and an optional battery attachment, though none of these are specified further. The stated design goals were low cost, hackability, open-source design, wearability, and an attractive form factor with rounded corners.

The project does not appear to have reached a finished, distributed product -- there is no evidence of a price, a quantity built, or a public firmware repository, and the Hackaday.io page has seen no updates since shortly after it was posted. It is treated here as never released. A later, apparently unrelated ESP32-C3-based project called "Meshanger Badge V" exists on Hackaday.io and may warrant its own entry.
