---
title: DC28 Jam Con Badge
id: dc28-jam-con-badge
layout: badge
parent: DC28
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc28
year: 2020
makers:
- name: Robb (dogweather)
summary: 'A one-off instrument tuner badge built for DEF CON 28: it listens for concert A (440Hz) and shows how close a played note is with a NeoPixel ring.'
functions: 'Runs an FFT on incoming audio to detect concert A (440Hz) and drives a NeoPixel ring to show whether the played pitch is high, low, or in tune. The maker''s notes also describe a planned button-triggered "10 seconds of tuning mode" and floated (but did not confirm building) a TensorFlow Lite model for broader note detection.'
look:
  colors: []
  shape: null
  themes:
  - music
  - hardware tool
  - measurement
tech:
  mcu: Teensy 3.2
  leds:
    count: null
    type: NeoPixel
    note: 'Build-log photos show an Adafruit NeoPixel ring (12x 5050 RGB) among the parts; not confirmed as final LED count on the assembled badge.'
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: 'Appears to be a single personal build by the maker for their own use at DEF CON 28, not distributed or sold to others.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/dogweather/jamcon
  eda_tool: null
links:
- label: hackaday.io/project/167265-dc28-jam-con-badge
  url: https://hackaday.io/project/167265-dc28-jam-con-badge
  kind: hackaday
- label: github.com/dogweather/jamcon
  url: https://github.com/dogweather/jamcon
  kind: repo
images: []
contact: {}
notes:
- An instrument-tuner badge for DEF CON 28 using a Teensy 3.2 to sense concert-A 440Hz pitch via FFT. Found by the event-year sweep, task dc28-saos.
- 'The community sheet listed this as "DC28 Jam Con Badge"; the maker''s own Hackaday.io project page uses the same title, so no rename was needed.'
status: unknown
sources:
- kind: url
  url: https://hackaday.io/project/167265-dc28-jam-con-badge
  title: DC28 Jam Con Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc28-saos); event read as ''dc28''.'
- kind: url
  url: https://hackaday.io/project/167265-dc28-jam-con-badge
  title: DC28 Jam Con Badge
  accessed: '2026-09-08'
  note: 'Maker''s own Hackaday.io project page (Robb / dogweather): confirms event, concept, Teensy 3.2, FFT tuner design, NeoPixel ring, and two August 2019 build logs. No log confirms the badge was finished or worn at the con.'
- kind: url
  url: https://github.com/dogweather/jamcon
  title: dogweather/jamcon - Defcon / JAMCON planning - 2020
  accessed: '2026-09-08'
  note: 'MIT-licensed repo linked from the project page; holds only a neopixel-playground.ino test sketch, no hardware files, gerbers, or BOM.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Only source is the maker''s own Hackaday.io project and linked GitHub repo; no press coverage, storefront, or third-party confirmation found. The Hackaday log stops at two entries from August 2019 with no update confirming the badge was completed, worn at DC28, or made for anyone besides the maker, so status is left as unknown rather than assumed released. No photo of the assembled/finished badge was found; the repo and project-log images show only individual parts (Teensy 3.2, NeoPixel ring, breadboard, mic amp) and a hand sketch, so no images were saved. LED count on the final unit, battery, price, and quantity are unconfirmed and left empty.'
last_modified_date: '2026-09-08'
---


The Jam Con Badge is a personal project by Robb (Hackaday.io handle "dogweather"), built as an instrument tuner for DEF CON 28 in 2020. Rather than a general chromatic tuner, it is deliberately narrow: it listens for one specific pitch, concert A at 440Hz, and runs an FFT on the incoming audio to judge how close a played note is to that reference. Feedback is meant to come from a NeoPixel ring, with sketched ideas for lighting patterns that shift depending on whether the pitch is flat, sharp, or dead on, and a possible button-triggered "tuning mode" that would run for about ten seconds before returning to a low-power sleep state.

The build runs on a Teensy 3.2 (ARM Cortex-M4), and the maker's project log shows deliberately starting work in August 2019 to avoid the last-minute soldering crunch common at DEF CON. The two logged build steps cover ordering parts (Teensy, NeoPixel ring, mic amp, breadboard) and early planning sketches. The linked GitHub repository (MIT-licensed) contains only a small NeoPixel test sketch rather than the tuner's full firmware, and no schematic, PCB, or BOM files were published. There is no record on the project page of the badge being finished, worn at the convention, or shared with anyone beyond the maker, so its final build details and outcome remain unconfirmed.
