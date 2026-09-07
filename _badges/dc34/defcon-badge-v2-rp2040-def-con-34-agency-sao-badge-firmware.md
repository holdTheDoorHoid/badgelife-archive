---
title: Defcon-badge-V2-RP2040 — DEF CON 34 'Agency' SAO badge firmware
id: dc34-defcon-badge-v2-rp2040-def-con-34-agency-sao-badge-firmware
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: MadmanTimmy3241
  url: https://github.com/MadmanTimmy3241
summary: 'A fan-made SAO built around DEF CON 34''s "Agency" theme: two badges trade an IR handshake and log who they''ve seen, with an OLED/LED-matrix marquee, a buzzer, and a held-button "log purge" to erase that history.'
functions: 'Runs on a Waveshare RP2040-Zero. An omnidirectional IR ring (broadcast/receive) and a separate directional IR handshake pair let two badges detect and log each other; a Confirm button and a Log Purge button (purge requires a 3-second hold, with a warning chime first) give the wearer control over that logging, and a Silent Mode slide switch mutes the piezo buzzer. A scrolling "witty message" marquee (themed around consent/privacy jokes) runs on whichever display is wired up -- either a 128x64 or 64x48 SSD1306 OLED, or an Adafruit 15x7 IS31FL3731 Charlieplex LED matrix wing -- and spotting a reserved "easter egg" badge ID over IR triggers a one-time spinning-pentagram animation with a stinger chime.'
look:
  colors: []
  shape: null
  themes:
  - privacy
  - security
  - text
tech:
  mcu: RP2040
  leds:
    count: null
    type: charlieplexed
    note: 'Optional Adafruit 15x7 Charlieplex LED Matrix FeatherWing (IS31FL3731) as one of two interchangeable display options; only one display is ever wired up at a time.'
  display: '0.96" 128x64 SSD1306 OLED (or a 64x48 SSD1306 variant)'
  connectivity:
  - ir
  - i2c
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
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/MadmanTimmy3241/Defcon-badge-V2-RP2040
  eda_tool: null
  notes: 'Firmware (Arduino sketch) is public on GitHub, targeting the Waveshare RP2040-Zero board via arduino-cli (fqbn rp2040:rp2040:waveshare_rp2040_zero). No PCB/hardware design files, BOM, or schematic are published in the repo -- it appears to be built on off-the-shelf modules (Waveshare RP2040-Zero, an Adafruit OLED or LED matrix wing, TSOP38238 IR receivers, a piezo buzzer) rather than a custom PCB.'
links:
- label: github.com/MadmanTimmy3241/Defcon-badge-V2-RP2040
  url: https://github.com/MadmanTimmy3241/Defcon-badge-V2-RP2040
  kind: repo
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/MadmanTimmy3241/Defcon-badge-V2-RP2040
  title: Defcon-badge-V2-RP2040 — DEF CON 34 'Agency' SAO badge firmware
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 34''.'
- kind: url
  url: https://raw.githubusercontent.com/MadmanTimmy3241/Defcon-badge-V2-RP2040/master/config.h
  title: 'config.h — pin mapping, I2C addresses, OLED variant selection'
  accessed: '2026-09-07'
  note: 'Confirmed hardware: Waveshare RP2040-Zero pins, TSOP38238 IR receivers, piezo buzzer, two buttons plus a silent-mode switch, an Adafruit 15x7 IS31FL3731 Charlieplex Wing at 0x74, and a 128x64 or 64x48 SSD1306 OLED at 0x3C (only one display wired up at a time).'
- kind: url
  url: https://raw.githubusercontent.com/MadmanTimmy3241/Defcon-badge-V2-RP2040/master/V2-RP2040.ino
  title: 'V2-RP2040.ino — main sketch'
  accessed: '2026-09-07'
  note: 'Confirmed functions: scrolling marquee on OLED and/or LED matrix, debounced Confirm/Log-Purge buttons with a 3-second purge hold and warning/confirm chimes, omni + directional IR transmitters/receivers (handshake logic itself not yet wired up), and a one-time spinning-pentagram "easter egg" animation triggered by a reserved badge ID.'
- kind: url
  url: https://raw.githubusercontent.com/MadmanTimmy3241/Defcon-badge-V2-RP2040/master/messages.h
  title: 'messages.h — marquee message pool'
  accessed: '2026-09-07'
  note: 'Confirmed the "Agency" consent/privacy-themed joke messages and that they are kept all-caps to fit the 7-row LED matrix font.'
- kind: url
  url: https://raw.githubusercontent.com/MadmanTimmy3241/Defcon-badge-V2-RP2040/master/compile.ps1
  title: 'compile.ps1 — build script'
  accessed: '2026-09-07'
  note: 'Confirmed target board: Waveshare RP2040-Zero, built via arduino-cli.'
- kind: url
  url: https://api.github.com/repos/MadmanTimmy3241/Defcon-badge-V2-RP2040
  title: 'GitHub API repo metadata'
  accessed: '2026-09-07'
  note: 'Confirmed repo description ("DEF CON 34 ''Agency'' SAO badge firmware (Waveshare RP2040-Zero)"), created July 2026, no license file, no homepage/store link.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a fan-made/community SAO firmware project, not an official DEF CON 34 badge or a product with a storefront -- no price, quantity, or availability information exists anywhere. No PCB/hardware design files are published, only the firmware; the repo does not say whether the badge is a custom PCB or built on protoboard with off-the-shelf modules (Waveshare RP2040-Zero dev board, Adafruit display wings). No photos of the physical badge were found in the repo or via search, so no images could be saved. DEF CON 34''s official theme is confirmed as "Agency" (self-determination), which matches this SAO''s IR-handshake/consent framing, but this project is unrelated to the official conference badge (Bunnie Huang''s Baochip-based badge with 2 SAO ports).'
last_modified_date: '2026-09-07'
---

This is firmware for a fan-made SAO built for DEF CON 34, whose official theme was "Agency." Written by MadmanTimmy3241 for a Waveshare RP2040-Zero board, the badge leans hard into that theme: it uses an infrared LED/receiver ring to detect nearby badges and log the encounter, but gives the wearer explicit control over that surveillance with a physical Confirm button, a Silent Mode switch, and a Log Purge button (which requires a deliberate 3-second hold, with a warning chime, before it actually erases anything). A scrolling marquee of consent- and privacy-themed one-liners runs across whichever display is attached -- a 128x64 or 64x48 SSD1306 OLED, or an Adafruit 15x7 Charlieplex LED matrix wing -- and a piezo buzzer provides audio feedback.

As of the version reviewed, the IR handshake/logging logic and the directional (face-to-face) handshake transmitter are stubbed out but not yet wired up; the sketch currently just runs the marquee, buttons, and buzzer. A hidden feature spins up a full-screen rotating pentagram animation with an ominous chime the first time the badge sees a specific reserved IR badge ID, after which it leaves only a small static star icon in the display's diagnostic strip.

Only firmware is published; no PCB, schematic, or bill of materials was found, so it is unclear whether this runs on a custom board or a protoboard build on top of off-the-shelf parts (the Waveshare RP2040-Zero plus Adafruit display/LED-matrix wings and TSOP38238 IR receivers referenced in the code). No pricing, quantity, or distribution details exist since this does not appear to have been sold or distributed as a kit.
