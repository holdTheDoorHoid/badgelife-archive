---
title: Hello My Name Is SAO
id: supercon-2024-hello-my-name-is-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A deliberately minimal write-your-name-with-a-pen name-tag SAO with an optional single RGB LED, davedarko's first entry to the Supercon 2024 SAO contest, made in red, green and blue board variants.
functions: 'A blank name-tag surface to hand-write on; the LED version adds one onboard RGB LED for a bit of blink without any programming.'
look:
  colors: [red, green, blue, white]
  shape: rectangle
  themes: [minimalist, text]
tech:
  mcu: none
  leds:
    count: 1
    type: RGB
    note: 'LED version only ("blinkyparts style"); the plain version has no LED. Prototype boards had a wiring error where only one of four LEDs per panel was correctly connected.'
  display: none
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: '~90 kits'
  availability: unknown
  distribution: [free_drop, contest]
  where: 'Bagged and tagged for distribution to attendees at Supercon 2024 as a Supercon 8 SAO contest entry.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/HelloMyNameIs
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: hackaday.io/project/197693-hello-my-name-is-sao
  url: https://hackaday.io/project/197693-hello-my-name-is-sao
  kind: hackaday
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/HelloMyNameIs
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/HelloMyNameIs
  kind: repo
images:
  - file: assets/images/badges/supercon-2024/hello-my-name-is-sao/a051b6437a.jpg
    source: "https://hackaday.io/project/197693-hello-my-name-is-sao"
    credit: "davedarko"
    caption: "Hello My Name Is SAO project cover photo, Supercon 2024"
  - file: assets/images/badges/supercon-2024/hello-my-name-is-sao/edce5635ad.jpg
    source: "https://hackaday.io/project/197693-hello-my-name-is-sao"
    credit: "davedarko"
    caption: "Assembled Hello My Name Is SAO boards"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/197693-hello-my-name-is-sao
  title: "Hello My Name Is SAO — Hackaday.io"
  accessed: '2026-09-07'
  note: Maker's project log; confirms event (Supercon 8 SAO contest, 2024), ~90 kits made in red/green/blue, RGB LED with faders, cover photo.
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/HelloMyNameIs
  title: "Simple-Add-ons-SAO/HelloMyNameIs at main"
  accessed: '2026-09-07'
  note: Confirms two variants (plain and LED/"blinkyparts style"), KiCad design files, and the prototype wiring errata (only 1 of 4 LEDs per panel wired correctly).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Price and exact quantity distribution details (kit vs. assembled, cost) were not stated on either source. sao_version assumed v1 (4-pin) as no SAO version is specified by the maker; treat as unconfirmed. Firmware URL left null since the board is passive (LED driven by a coin cell / simple circuit, no MCU) and no firmware repo is referenced.'
last_modified_date: '2026-09-07'
---

Hello My Name Is SAO is davedarko's first entry into the Supercon 8 SAO add-on contest at Supercon 2024. It leans hard into simplicity: the base idea is just a blank name-tag surface meant to be written on by hand, built as a deliberate rejection of the increasingly complex badges seen at the con. As the maker put it on the project's Hackaday.io page, "blinking an LED is already too much, and programming a badge is too much work while listening to amazing talks."

A "blinkyparts style" variant adds a single onboard RGB LED for a bit of visual interest without requiring any code — no microcontroller is involved. Around 90 kits were produced across red, green and blue PCB variants, bagged and tagged for handout to attendees at the event. The prototype run had a wiring slip: on panels of four, only one LED per panel was correctly connected, with the other three needing manual rework.

## Make your own

KiCad hardware files for both the plain and LED versions are published in davedarko's Simple-Add-ons-SAO repository under the `HelloMyNameIs` folder. No firmware is needed since the board carries no microcontroller.
