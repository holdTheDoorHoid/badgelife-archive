---
title: DC24 Psychoholics Pin
id: dc24-psychoholics-pin
layout: badge
parent: DC24
grand_parent: Badge Archive
nav_exclude: true
type: other
event: dc24
year: 2016
makers:
- name: krux702
summary: 'A small Arduino-driven pin made for the Psychoholics group at DEF CON 24, with 11 LEDs that fade on and off at random.'
functions: 'Ambient blinky effect only: an Arduino sketch (using the SoftPWM library) picks a random LED from the 11 on the board every 30ms and fades it on or off, giving a slow, randomized twinkle. No buttons, games, or other interactivity.'
look:
  colors: []
  shape: null
  themes:
  - pin
tech:
  mcu: null
  leds:
    count: 11
    type: discrete
    note: 'Driven directly from microcontroller pins via software PWM (SoftPWM library), not addressable LEDs.'
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
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/krux702/dc24_psychoholics_pin/tree/master/hardware
  firmware_url: https://github.com/krux702/dc24_psychoholics_pin/tree/master/psychoholic_pin
  eda_tool: Eagle
links:
- label: github.com/krux702/dc24_psychoholics_pin
  url: https://github.com/krux702/dc24_psychoholics_pin
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/krux702/dc24_psychoholics_pin
  title: DC24 Psychoholics Pin
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc24''.'
- kind: url
  url: https://raw.githubusercontent.com/krux702/dc24_psychoholics_pin/master/psychoholic_pin/psychoholic_pin.ino
  title: 'psychoholic_pin.ino (firmware source)'
  accessed: '2026-09-07'
  note: 'Confirmed 11 LEDs driven via SoftPWM, random fade-in/fade-out loop, no buttons; sketch header labels it "DEF CON 24 - Psychoholics badge".'
- kind: url
  url: https://raw.githubusercontent.com/krux702/dc24_psychoholics_pin/master/README.md
  title: 'README.md'
  accessed: '2026-09-07'
  note: 'One-line description: "SoftPWM Arduino code for the Psychoholics DEF CON 24 badge".'
- kind: url
  url: https://api.github.com/repos/krux702/dc24_psychoholics_pin/contents/hardware
  title: 'Repo contents: hardware directory'
  accessed: '2026-09-07'
  note: 'Hardware files are Eagle CAD (.brd/.sch), no Gerbers or KiCad; confirms board files are published (firmware + schematic/board, but not a BOM or write-up).'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched README.md, the psychoholic_pin.ino firmware, and the repo/hardware/firmware directory listings directly. All cited facts check out: README confirms "SoftPWM Arduino code for the Psychoholics DEF CON 24 badge"; the .ino confirms 11 LEDs (NUM_LEDS=11) in leds[], SoftPWM-driven, a random-LED loop with a 30ms delay (NEXT_LED) and 1500/2000ms fade times, no button/input code; the hardware directory contains only psychoholics_pin.brd and psychoholics_pin.sch (Eagle CAD format), the firmware directory contains only psychoholic_pin.ino. Corrected two fields the researcher under-filled: make_your_own.open_source to "yes" (guide: yes when both hardware and firmware are published, which they are, regardless of missing BOM/license) and make_your_own.eda_tool to "Eagle" (directly evidenced by the .brd/.sch file extensions already cited, not a maker statement but an objective read of the published files). Psychoholics is a long-running DEF CON phreaking/social group; no maker write-up, storefront, price, quantity, or photo of the finished pin exists anywhere found online, so those fields correctly stay empty. No images were saved (none exist to save) and no contradictions were found between sources.'
last_modified_date: '2026-09-07'
---

This pin was made for the Psychoholics, a group associated with DEF CON's phreaking scene (Telephreak/TeleChallenge), for their presence at DEF CON 24 in 2016. The only public trace of it is a GitHub repository from maker krux702 containing an Eagle CAD schematic/board and a short Arduino sketch.

The firmware drives 11 LEDs directly from microcontroller pins using the SoftPWM software-PWM library rather than addressable LEDs. Every 30 milliseconds the sketch picks one of the 11 LEDs at random and either fades it up or down (with fade times of 1.5-2 seconds), producing a slow, randomized twinkling effect across the board. There is no button, sensor, or other interactivity described in the code.

No photos of the finished pin, pricing, production quantity, or distribution details were found in the repository or elsewhere online, so those fields are left blank rather than guessed.
