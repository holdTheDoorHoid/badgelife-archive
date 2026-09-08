---
title: Supercon2017 Badge with BSOD
id: supercon-2017-supercon2017-badge-with-bsod
layout: badge
parent: Supercon 2017
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2017
year: 2017
makers:
- name: Paul Stoffregen
  url: https://hackaday.io/paul-stoffregen
summary: A Teensy 3.2 + TFT display add-on Paul Stoffregen taped to the back of his official 2017 Supercon badge, with a touch-activated fake Blue Screen of Death easter egg.
functions: Shows Stoffregen's name and a photo of a Teensy by default; touching the screen triggers a fake Windows BSOD, and a hidden mode shows collaborator Metalnat Hayes's name instead.
look:
  colors: []
  shape: null
  themes:
  - meme
  - pop culture
  - hardware tool
tech:
  mcu: Teensy 3.2
  leds: null
  display: 2.8" TFT
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '1 (one-off)'
  availability: not_released
  distribution: []
  where: 'Not distributed; a single unit Stoffregen wore himself, then handed off to Metalnat Hayes for the rest of the con.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/PaulStoffregen/supercon2017
  eda_tool: null
links:
- label: hackaday.io/project/28300-supercon2017-badge-with-bsod
  url: https://hackaday.io/project/28300-supercon2017-badge-with-bsod
  kind: hackaday
- label: github.com/PaulStoffregen/supercon2017
  url: https://github.com/PaulStoffregen/supercon2017
  kind: repo
images:
  - file: assets/images/badges/supercon-2017/supercon2017-badge-with-bsod/6c2250e643.jpg
    source: "https://hackaday.io/project/28300-supercon2017-badge-with-bsod"
    credit: "Paul Stoffregen"
    caption: "Teensy 3.2 + TFT BSOD add-on mounted on the back of the 2017 Supercon badge"
contact: {}
notes:
- Sweep found this via the Hackaday.io project page; title and event id both confirmed correct.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/28300-supercon2017-badge-with-bsod
  title: Supercon2017 Badge with BSOD
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2017); event read as ''supercon-2017''.'
- kind: url
  url: https://hackaday.io/project/28300-supercon2017-badge-with-bsod
  title: Supercon2017 Badge with BSOD (Hackaday.io project page)
  accessed: '2026-09-08'
  note: 'Confirmed maker, event, hardware (Teensy 3.2 + 2.8" TFT), how it was made and used, and source repo link.'
- kind: url
  url: https://github.com/PaulStoffregen/supercon2017
  title: PaulStoffregen/supercon2017 (GitHub)
  accessed: '2026-09-08'
  note: 'Source code repository for the BSOD sketch, linked from the Hackaday.io project.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Firmware source is public on GitHub; no separate hardware design files (it used a stock Teensy 3.2 and an off-the-shelf TFT taped to the badge, not a custom PCB), so make_your_own.hardware_url is left empty and open_source is "partial". This was a one-off hack Stoffregen built for himself at the con (not a kit or product), so get_one fields describe that rather than a sale.'
last_modified_date: '2026-09-08'
---

Paul Stoffregen built this as a personal add-on to his official 2017 Hackaday Superconference badge: a Teensy 3.2 driving a 2.8" TFT display, taped to the back of the badge and powered from the badge's own 3V supply. It originally just showed his name and a photo of a Teensy board.

At a Friday pre-party, fellow attendee Metalnat Hayes suggested giving it a fake Blue Screen of Death, and Stoffregen coded the feature the next morning as a touch-activated easter egg — tapping the screen throws up a mock Windows crash screen. He also built in a hidden mode that displays Hayes's name instead of his own. Stoffregen wore the badge through the first half of Saturday's conference, then handed it off to Hayes to keep using for the rest of the event.

## Make your own

The Teensy sketch is published on GitHub at PaulStoffregen/supercon2017. There is no separate schematic or PCB — the build is a stock Teensy 3.2 and an off-the-shelf TFT module wired up and taped to the host badge, so replicating it means following the code and wiring described there rather than fabricating a board.
