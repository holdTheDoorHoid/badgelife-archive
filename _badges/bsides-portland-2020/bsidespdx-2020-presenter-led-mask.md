---
title: BSidesPDX 2020 Presenter LED Mask
id: bsides-portland-2020-bsidespdx-2020-presenter-led-mask
layout: badge
parent: BSidespdx 2020
grand_parent: Badge Archive
nav_exclude: true
type: other
event: bsides-portland-2020
year: 2020
makers:
- name: PDX Badgers
  url: https://github.com/pdxbadgers
summary: A voice-reactive LED face mask given to presenters at the all-digital BSidesPDX 2020, animating mouth shapes on an 8x8 LED matrix in response to microphone input.
functions: Samples ambient/mic volume and maps audio peaks to five mouth-shape images plus a smile/idle state; also displays a multicolor BSidesPDX banner animation. A pushbutton toggles standby (display and mic off) to save power.
look:
  colors: []
  shape: null
  themes:
  - wearable
  - mascot
tech:
  mcu: ATmega32u4 (Arduino Pro Micro)
  leds:
    count: 64
    type: WS2812
    note: Flexible 8x8 WS2812 LED matrix sewn onto a cotton mask
  display: LED matrix 8x8
  connectivity: []
  battery: USB power bank (5V)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to presenters at BSidesPDX 2020 (a virtual/all-digital conference held October 23-24, 2020) rather than sold or badge-swapped.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/pdxbadgers/2020-mask
  firmware_url: https://github.com/pdxbadgers/2020-mask
  eda_tool: null
links:
- label: badge.gallery/badges/bsidespdx-2020-presenter-led-mask
  url: https://badge.gallery/badges/bsidespdx-2020-presenter-led-mask
  kind: website
- label: github.com/pdxbadgers/2020-mask
  url: https://github.com/pdxbadgers/2020-mask
  kind: repo
images: []
contact: {}
notes:
- Voice-reactive LED face-mask wearable distributed in place of a traditional badge for BSidesPDX 2020. Found by the event-year sweep, task bsides-portland.
- The sweep's summary text matches the maker's own project description; confirmed against the PDX Badgers GitHub repo (pdxbadgers/2020-mask).
- No production quantity, price, or license is stated anywhere; treat this as a presenter gift/artifact rather than a mass-distributed badge.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/bsidespdx-2020-presenter-led-mask
  title: BSidesPDX 2020 Presenter LED Mask
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-portland); event read as ''BSidesPDX 2020''.'
- kind: url
  url: https://github.com/pdxbadgers/2020-mask
  title: pdxbadgers/2020-mask
  accessed: '2026-09-10'
  note: Maker's own repo; confirms hardware (Arduino Pro Micro, MAX4466 mic, 8x8 WS2812 matrix), design derived from TylerGlaiel's voicemask project, and that it was made for BSides 2020 presenters. No license file present; no image assets in the repo.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Fact-check pass (2026-09-10): re-fetched both cited sources plus the repo''s raw README.md and 2020-mask.ino directly. Every non-empty field and every factual sentence in the body/Make-your-own section checked out against them: hardware list (Pro Micro/ATmega32u4, MAX4466 mic, 8x8 WS2812 matrix, SMT switch, USB power bank), the five mouth-shape frames plus smile/idle state and pushbutton standby toggle (confirmed by reading the .ino source directly), the multicolor scrolling BSidesPDX banner, the Tyler Glaiel voicemask/Jabbermask Kickstarter lineage, the wiring/library/Arduino-Leonardo build steps, the absence of a license file (confirmed via `gh api repos/pdxbadgers/2020-mask` returning license: null and a two-file repo listing), and badge.gallery''s explicit statement that no image is published for this item. No contradictions found; no unsupported claims found. Quantity made and exact distribution mechanics remain unstated anywhere found, so those fields stay empty. Confidence held at medium (third-party badge.gallery + maker''s own repo, no independent press coverage).'
last_modified_date: '2026-09-10'
---

The BSidesPDX 2020 Presenter LED Mask was a voice-reactive wearable that PDX Badgers gave to speakers at BSidesPDX 2020, held as an all-digital conference on October 23-24, 2020. In place of a traditional hardware badge, presenters received a cotton face mask fitted with a flexible 8x8 WS2812 LED matrix that animates a set of mouth shapes in response to a MAX4466 microphone, plus a smile/idle state and a multicolor BSidesPDX banner display. An Arduino Pro Micro (ATmega32u4) runs the show, powered by a standard USB power bank, with a single pushbutton to cut the display and mic into a low-power standby.

The design is an explicit refinement of Tyler Glaiel's earlier "voicemask" project (later crowdfunded as Jabbermask): PDX Badgers swapped the original Arduino Nano/ATmega328p/USB-Mini combo for the more robust Pro Micro with USB-Micro, replaced the 9V-battery-and-regulator power scheme with a 5V USB power bank, and trimmed the wiring down to a handful of direct solder points on the microcontroller.

Firmware and build instructions are published on GitHub at pdxbadgers/2020-mask, including the full parts list, wiring diagram, and Arduino library dependencies (Adafruit NeoMatrix, NeoPixel, and GFX), though no license is stated. No photos of a finished, worn mask were located during research, and figures for how many were made or given out were not found.

## Make your own

The GitHub repo (pdxbadgers/2020-mask) documents the build: an Arduino Pro Micro, a MAX4466 microphone module, a flexible 8x8 WS2812 matrix, an SMT switch, a cotton mask base, and a USB power bank. Wiring is minimal — the LED matrix's 5V/GND/DIN lines and the microphone's power/ground/output lines solder directly to the Pro Micro's pins, plus a solder-jumper bridge to route VUSB straight to VCC. The Arduino sketch (`2020-mask.ino`) is programmed as an "Arduino Leonardo" board after installing the Adafruit NeoMatrix, NeoPixel, and GFX libraries.
