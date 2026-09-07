---
title: DC30 JollyBadge
id: dc30-jollybadge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
series: JollyBadge
makers:
- name: Jolly Roger
  url: https://x.com/GetJollyBadge
summary: A round, skull-and-crossbones puzzle badge sold and hidden around DEF CON 30, built around eight sequential electronic challenges.
functions: 'Eight sequentially-unlocked challenges gating a light-up "finale" state: an NFC tap, Morse code, a binary readout, a serial/UART puzzle, a data dump, and a crypto challenge, plus temperature and spin/orientation elements. Solving all eight before closing ceremonies made the holder eligible for a prize.'
look:
  colors:
  - black
  - silver
  shape: circle
  themes:
  - skull
  - pirate
  - puzzle
  - ctf
tech:
  mcu: SAMD21 (Arduino Zero-family, Microchip/Atmel)
  leds:
    count: 8
    type: NeoPixel (WS2812-compatible)
    note: Ring of 8 addressable RGB LEDs around the skull-and-crossbones face, driven with Adafruit_NeoPixel.
  display: none
  connectivity:
  - nfc
  - i2c
  inputs:
  - accelerometer
  battery: CR2032 (maker supplied a couple of cells; badge was reported to draw them down quickly)
  sao_version: none
get_one:
  price: $25
  price_usd: 25.0
  quantity: 50 for sale, plus additional units hidden around the venue as free finds
  availability: sold_out
  availability_note: 'Sold out during DEF CON 30 (August 2022); checked 2026-09-07, no longer offered anywhere.'
  distribution:
  - purchase
  - free_drop
  where: 'Sold in person at DEF CON 30 for $25 (50 made), with more copies hidden around the con as a scavenger hunt; clues to the hidden badges were posted on the maker''s @GetJollyBadge account.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/imjollyroger/JollyBadge_DC30/tree/main/hw/dc30
  firmware_url: https://github.com/imjollyroger/JollyBadge_DC30/tree/main/fw
  eda_tool: KiCad
  license: MIT
  notes: 'Repo also includes a separate small "programmer" PCB (hw/programmer/dc30-programmer) used to flash badges. Firmware is Arduino/SAMD-based C++, split into per-challenge .ino files (NFC, Morse, binary, serial, data dump, crypto, temperature, spin, plus setup/state/animation).'
links:
- label: twitter.com/GetJollyBadge
  url: https://twitter.com/GetJollyBadge
  kind: social
- label: JollyBadge_DC30 hardware & firmware (GitHub)
  url: https://github.com/imjollyroger/JollyBadge_DC30
  kind: repo
- label: jollybadge.com (current JollyBadge series site)
  url: https://www.jollybadge.com
  kind: website
images:
  - file: assets/images/badges/dc30/jollybadge/2a0692fa1f.jpg
    source: "https://twitter.com/GetJollyBadge/status/1554183524730580998"
    credit: "Jolly Roger (@GetJollyBadge)"
    caption: "JollyBadge_DC30 board: 8 addressable RGB LEDs ringing a skull-and-crossbones badge outline, powering on"
contact: {}
notes:
- Follow @GetJollyBadge on twitter for free drop hints.
- 'JollyBadge is a recurring series by the same maker (Jolly Roger / Steve Jabs): a DC31 listing and a DC32 entry ("Name not released as of yet") also exist in this archive, and a JollyBadge V2 was sold for DC33 via jollybadge.com.'
status: released
sources:
- kind: sheet
  event: dc30
  row: 8
  updated: '2022-07-09'
- kind: url
  url: https://twitter.com/GetJollyBadge
  title: 'JollyBadge (@GetJollyBadge) / X'
  accessed: '2026-09-06'
  note: Current profile; confirms series continuity into DC32/DC33 and links to jollybadge.com.
- kind: url
  url: https://web.archive.org/web/20220801191352/https://twitter.com/GetJollyBadge/status/1554183528501448706
  title: 'JollyBadge_DC30 announcement thread (Aug 1, 2022)'
  accessed: '2026-09-06'
  note: 'Confirms 8 sequential challenges, a prize for solving all before closing ceremonies, 50 for sale at $25, additional hidden badges, and CR2032 power.'
- kind: url
  url: https://web.archive.org/web/2022id_/https://twitter.com/GetJollyBadge/status/1546563923637420034
  title: JollyBadge power-management reply (Jul 2022, pre-con)
  accessed: '2026-09-06'
  note: Battery life improved from ~1 hour to 4+ hours with LEDs lit ~90% of the time in demo code.
- kind: url
  url: https://web.archive.org/web/2022id_/https://twitter.com/GetJollyBadge/status/1555680994103070722
  title: Art credit tweet
  accessed: '2026-09-06'
  note: Badge artwork credited to @Mr_0rng.
- kind: url
  url: https://github.com/imjollyroger/JollyBadge_DC30
  title: imjollyroger/JollyBadge_DC30 (GitHub)
  accessed: '2026-09-06'
  note: 'Firmware (fw/a_GLOBAL, Arduino/SAMD C++ using Adafruit_NeoPixel, ArduinoLowPower, ST25DVSensor, MPU6050_light) and KiCad hardware (hw/dc30) under MIT license. Confirms SAMD21-class MCU, 8 NeoPixels, NFC (ST25DV) and IMU (MPU6050) peripherals.'
- kind: url
  url: https://www.jollybadge.com
  title: 'JollyBadge [V2] - The Final Batch'
  accessed: '2026-09-06'
  note: Current site for the V2/DC33 successor badge; used only to confirm the series and maker's ongoing branding, not for DC30-specific facts.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Core facts (challenges, price, quantity, distribution, battery, MCU family, LED count, NFC/IMU peripherals, open-source hardware/firmware) confirmed directly from the maker''s own DC30-era tweets (via Wayback Machine, since the live account no longer shows 2022 posts without login) and the maker''s own GitHub repo. The IMU (MPU6050) is present in firmware but its initialization call is commented out in setup(), so it may not have been active in the shipped build; noted rather than guessed at. Exact PCB solder-mask color and precise LED part number (e.g. WS2812B vs SK6812) were not confirmed by a written source, only inferred from the board photo and the NeoPixel library choice, so colors/leds.type are left as best-supported approximations rather than exact. No individual review or press coverage (Hackaday, etc.) was found for this specific year''s badge.'
last_modified_date: '2026-09-06'
---

JollyBadge_DC30 was a round, skull-and-crossbones puzzle badge sold by a solo maker going by Jolly Roger (also known online as Steve Jabs) at DEF CON 30 in 2022. It packed eight sequentially-unlocked challenges — touching an NFC tag, reading Morse code, decoding binary, working a serial/UART puzzle, dumping data, and solving a crypto step, alongside temperature and spin/orientation elements — into a ring of eight addressable RGB LEDs around the skull-and-crossbones outline. Anyone who solved all eight challenges before closing ceremonies qualified for a prize; the badge artwork was credited to @Mr_0rng.

Fifty badges were sold in person for $25 each, and the maker hid additional units around the convention for attendees to find as a scavenger hunt, posting clues from the @GetJollyBadge account. It ran into a rough launch — sales slipped a day due to the maker being sick, and an early firmware bug caused freezes after certain correct answers (worked around by power-cycling, with in-person re-flashes offered) — but it sold out during the con. The board runs on a SAMD21-class microcontroller (Arduino Zero family) with an ST25DV NFC tag and an MPU6050 IMU on board, though the IMU's initialization is commented out in the shipped firmware. Power came from a couple of included CR2032 cells, which the maker candidly warned would drain quickly; a firmware update ahead of the con stretched battery life from about an hour to over four hours with the LEDs lit most of the time.

JollyBadge became a recurring series: this archive also has a DC31 listing (details unknown) and a DC32 entry under a placeholder title, and the maker later sold a JollyBadge V2 for DC33 through jollybadge.com. The DC30 hardware (KiCad) and firmware (Arduino/SAMD C++) are published under the MIT license at github.com/imjollyroger/JollyBadge_DC30, including the standalone board used to program badges.

## Make your own

The DC30 hardware and firmware are open source:

1. Hardware: KiCad project at `hw/dc30` in the [GitHub repo](https://github.com/imjollyroger/JollyBadge_DC30/tree/main/hw/dc30) (there's also a separate small programmer board under `hw/programmer`).
2. Firmware: Arduino sketches under `fw/a_GLOBAL`, split one file per challenge (NFC, Morse, binary, serial, data dump, crypto, temperature, spin) plus shared setup/state/animation code. Requires the Adafruit_NeoPixel, FlashAsEEPROM, FlashStorage, ArduinoLowPower, ST25DVSensor, and MPU6050_light Arduino libraries.
3. A pre-built `.bin` is included in the repo for flashing without a full toolchain.

## History

JollyBadge is a recurring series by the same maker: DC30 (this entry) was the original, followed by a DC31 appearance (details not found), a DC32 badge listed in the community sheet without a released name, and a JollyBadge V2 sold for DC33 via jollybadge.com with its own [V2 firmware/hardware repo](https://github.com/stevejabs/jollybadge-v2).
