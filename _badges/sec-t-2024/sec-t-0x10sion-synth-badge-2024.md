---
title: SEC-T 0x10sion Music Synthesizer Badge (2024)
id: sec-t-2024-sec-t-0x10sion-synth-badge-2024
layout: badge
parent: SEC-T 2024
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: sec-t-2024
year: 2024
makers:
- name: SEC-T
summary: A solder-it-yourself Arduino-compatible music synthesizer badge given to SEC-T 0x10sion 2024 attendees, based on Mitch Altman's open-hardware ArduTouch.
functions: Touch keyboard for playing notes, built-in speaker/amp, audio output jack, 5 programmable RGB LEDs, 2 extra buttons and 4 potentiometers for controlling sound. Ships pre-loaded with 'Quadrant', a looper-style synth with a default patch plus 4 presets (Scaffold, Farsy, Teleprompt, Glacial, Blur), reprogrammable as an Arduino sketch.
look:
  colors: []
  shape: null
  themes:
  - music
  - kit
  - learn to solder
tech:
  mcu: ATmega328
  leds:
    count: 5
    type: RGB
    note: programmable, used to indicate parameter-control mode
  display: none
  connectivity:
  - audio
  inputs:
  - touch
  - buttons
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Given to attendees of SEC-T 0x10sion 2024 as a soldering-kit conference badge; assembly required.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/SEC-T/badge-2024
  firmware_url: https://github.com/SEC-T/badge-2024
  eda_tool: null
  license: CC BY-SA 4.0
links:
- label: github.com/SEC-T/badge-2024
  url: https://github.com/SEC-T/badge-2024
  kind: repo
images:
  - file: assets/images/badges/sec-t-2024/sec-t-0x10sion-synth-badge-2024/d43ecca741.png
    source: "https://github.com/SEC-T/badge-2024"
    credit: "SEC-T"
    caption: "SEC-T 0x10sion Music Synthesizer Badge kit, assembled"
contact: {}
notes:
- SEC-T's 2024 conference badge is a soldering-kit music synthesizer based on Mitch Altman's open-hardware ArduTouch, with touch keyboard, speaker, audio out and 5 RGB LEDs, running the pre-loaded 'Quadrant' looper firmware. Found by the event-year sweep, task con-disobey.
- 'The sweep''s wording was "SEC-T 0x10sion Synth Badge (2024)"; the maker''s repo/README calls it the "SEC-T 0x10sion Music Synthesizer Badge" (also written "SEC-T Synth Badge" for short). Title updated to match.'
status: released
sources:
- kind: url
  url: https://github.com/SEC-T/badge-2024
  title: SEC-T 0x10sion Synth Badge (2024)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-disobey); event read as ''SEC-T 2024''.'
- kind: url
  url: https://github.com/SEC-T/badge-2024
  title: 'SEC-T/badge-2024: README'
  accessed: '2026-09-08'
  note: Confirmed maker, event/year, ArduTouch basis, features (touch keyboard, speaker/amp, audio jack, 5 RGB LEDs, 2 buttons, 4 pots), ATmega328 MCU, pre-loaded 'Quadrant' firmware and its presets, CC BY-SA 4.0 open-hardware license, and assembly-instructions PDFs. No price, quantity or unit-availability info found.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Maker's own GitHub repo (README + linked assembly PDFs) confirms this is a real, distributed item (status set to released, since attendees assembled and kept it). Price, quantity made, and current availability are not stated anywhere in the repo; left empty. No separate storefront, Hackaday.io page, or press coverage found in the searches run.
last_modified_date: '2026-09-08'
---

The SEC-T 0x10sion Music Synthesizer Badge was the conference badge for SEC-T 0x10sion 2024, distributed as a soldering kit that attendees assembled themselves. Rather than a typical blinky PCB badge, it is a small Arduino-compatible music synthesizer: a touch keyboard, a built-in speaker and amplifier, an audio output jack for external speakers, 5 programmable RGB LEDs, two extra buttons, and four potentiometers for shaping the sound. It runs on an ATmega328, the same chip used on the Arduino Uno, chosen specifically to keep the board approachable for first-time solderers.

The badge is built directly on Mitch Altman and Cornfield Electronics' open-hardware ArduTouch music synthesizer platform, released under a CC BY-SA 4.0 license, and SEC-T published a modified version of the ArduTouch Arduino library alongside the badge so owners can write their own synth sketches. Out of the box the badge comes pre-loaded with "Quadrant," a looper-style synth with a default patch and four named presets (Scaffold, Farsy, Teleprompt, Glacial, Blur), controlled via the touch keys, two red buttons, and the four pots; holding both red buttons repurposes the pots and lights the RGB LEDs to indicate the new control mode.

SEC-T's GitHub repository includes two PDF assembly guides covering both soldering the kit and reprogramming the badge with new Arduino sketches, along with demo videos of each Quadrant preset. No price, production quantity, or ongoing availability information is published in the repo, so those fields are left blank.

## Make your own

Hardware and firmware are both open (CC BY-SA 4.0), maintained at [github.com/SEC-T/badge-2024](https://github.com/SEC-T/badge-2024). The repo's README links two PDF assembly-instructions documents (soldering the kit, and reprogramming it with a new Arduino sketch) plus the modified ArduTouch Arduino library used to write synth patches for the badge.
