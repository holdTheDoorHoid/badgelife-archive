---
title: 'NolaCon 2018 badge ("@nola_con")'
id: nolacon-2018-nolacon-2018-badge-dead10c5-nola-con
layout: badge
parent: NolaCon 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: nolacon-2018
year: 2018
makers:
- name: DEAD10C5
  url: https://github.com/pale-shadow/badge-2018-nolacon
  role: hardware and firmware team (credited handles @theDevilsVoice, @p0lr_, @mzbat, @dead10c5)
summary: The official NolaCon 2018 electronic badge, a fleur-de-lis shaped PCB with an OLED screen, an 8-pixel APA102 LED strip, and a 4-button menu for games and light shows.
functions: A menu system (up/down/back/enter) drives a Pong clone ("burgess_pong"), several LED animation modes (rainbow, gradient, "cyberPolice", "ytCracker"), and an about screen; boots to a Deadlocks logo splash then the NolaCon logo.
look:
  colors:
  - black
  - gold
  shape: fleur-de-lis
  themes:
  - hardware tool
  - security
tech:
  mcu: ESP8266 (ESP-12E module)
  leds:
    count: 8
    type: APA102
    note: driven over a 2-wire data/clock bus at low brightness (max setting of 31)
  display: 0.96" 128x64 OLED (SSD1306, I2C address 0x3C)
  connectivity: []
  inputs:
  - buttons
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to NolaCon 2018 attendees as the conference badge.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/pale-shadow/badge-2018-nolacon/tree/main/eagle
  firmware_url: https://github.com/pale-shadow/badge-2018-nolacon/tree/main/src/nola_con
  eda_tool: Eagle
links:
- label: github.com/r00k5A58/NolaCon_2018
  url: https://github.com/r00k5A58/NolaCon_2018
  kind: repo
- label: github.com/pale-shadow/badge-2018-nolacon
  url: https://github.com/pale-shadow/badge-2018-nolacon
  kind: repo
  note: Fuller development mirror of the same project (Eagle and later KiCad PCB files, BOM, Gerbers, multiple firmware revisions, build photos); appears to be the maker team's working repo, r00k5A58's repo the public release copy.
images:
- file: assets/images/badges/nolacon-2018/nolacon-2018-badge-dead10c5-nola-con/4a7ea40b8f.jpg
  source: "https://github.com/pale-shadow/badge-2018-nolacon"
  credit: "DEAD10C5 / @thedevilsvoice"
  caption: "Assembled fleur-de-lis PCBs fresh from Seeed fabrication, before component population"
- file: assets/images/badges/nolacon-2018/nolacon-2018-badge-dead10c5-nola-con/71011efae0.jpg
  source: "https://github.com/pale-shadow/badge-2018-nolacon"
  credit: "DEAD10C5 / @thedevilsvoice"
  caption: "Eagle PCB layout of the fleur-de-lis badge showing the ESP-12E module, four buttons (LEFT/RIGHT/BACK/ENTER), and 8 APA102 LED pads"
contact: {}
notes:
- Official NolaCon 2018 electronic conference badge with Arduino firmware and Eagle PCB design files, mirrored also at https://github.com/pale-shadow/badge-2018-nolacon. Found by the event-year sweep, task con-nolacon.
- 'The sweep''s title quoted the repo''s ASCII-art wordmark ("DEAD10C5 NOLA CON") rather than a title the maker actually uses anywhere; the firmware and menu code instead identify the badge by the handle "@nola_con", which is used here instead. DEAD10C5 is the maker team''s name (credited in the firmware header as @theDevilsVoice, @p0lr_, @mzbat, @dead10c5), not the badge''s title.'
status: released
sources:
- kind: url
  url: https://github.com/r00k5A58/NolaCon_2018
  title: NolaCon_2018 badge ("DEAD10C5 NOLA CON")
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-nolacon); event read as ''NolaCon 2018''.'
- kind: url
  url: https://raw.githubusercontent.com/r00k5A58/NolaCon_2018/master/arduino/nola_con/nola_con.ino
  title: nola_con.ino firmware source
  accessed: '2026-09-08'
  note: Firmware header credits @theDevilsVoice, @p0lr_, @mzbat, @dead10c5, dated March 31 2018, version 0.4; confirms SSD1306 OLED at I2C 0x3C and APA102 LED strip.
- kind: url
  url: https://raw.githubusercontent.com/r00k5A58/NolaCon_2018/master/arduino/nola_con/nola.h
  title: nola.h header (pin/LED/display definitions)
  accessed: '2026-09-08'
  note: Confirms 8 APA102 LEDs, 4 buttons (UP/DOWN/BACK/ENTER), 128x64 display dimensions, and a built-in Pong game.
- kind: url
  url: https://github.com/pale-shadow/badge-2018-nolacon
  title: pale-shadow/badge-2018-nolacon
  accessed: '2026-09-08'
  note: Fuller mirror/working repo with Eagle and KiCad PCB files (ESP12E_DEVKIT and APA102_5050 footprints confirm ESP-12E MCU), BOM, Gerbers, and build/fabrication photos; README credits hardware and software to @thedevilsvoice (thedevilsvoice@protonmail.ch).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker team''s own repos (firmware source, PCB footprints, and fabrication photos): ESP8266/ESP-12E MCU, SSD1306 OLED, 8x APA102 LEDs, 4-button menu with a Pong game and LED animation modes, Eagle/KiCad design files all public. No pricing, quantity-made, or battery/power-source details were stated anywhere in either repo or its (empty) wiki, so those are left blank. Not confirmed by any third-party press coverage or a maker storefront listing (this was a free con badge, so none was expected). "Medium" confidence rather than "high" because the core facts come from source code and PCB files rather than an explicit specs page or announcement.'
last_modified_date: '2026-09-08'
---

The NolaCon 2018 badge is a free electronic conference badge shaped like a fleur-de-lis, designed and built by the DEAD10C5 team (credited in the firmware as @theDevilsVoice, @p0lr_, @mzbat, and @dead10c5) for NolaCon in New Orleans. It runs on an ESP8266 (ESP-12E module) and pairs a 128x64 SSD1306 OLED display with an 8-pixel APA102 addressable LED strip, all driven by a small cooperative-multitasking firmware (using the Arduino `Thread`/`ThreadController` libraries) written in C for the Arduino core.

Four buttons (labeled LEFT/UP, DOWN, BACK, and ENTER in the schematic) drive an on-screen menu that boots through a Deadlocks logo and a NolaCon fleur-de-lis splash screen before offering a handful of features: an "about" screen, several LED light-show modes (a rainbow cycle, a gradient, and effects named "cyberPolice" and "ytCracker"), and a built-in Pong-style game adapted from an existing open-source Arduino Pong sketch.

Two related GitHub repositories document the badge: `r00k5A58/NolaCon_2018`, a smaller public release copy with the Arduino firmware and a placeholder Eagle folder, and `pale-shadow/badge-2018-nolacon`, a much fuller working repository with the complete Eagle schematic/board history (nola1 through nola8a), a later KiCad re-layout, Gerbers sent to Seeed and OSH Park, a bill of materials, and in-progress photos of bare and fabricated boards. No pricing, production quantity, or battery/power details are stated in either repository; the badge appears to have simply been distributed to attendees as the conference's own badge.

## Make your own

Firmware lives under `src/nola_con` (or the simpler `arduino/nola_con` in the release repo) and builds with the Arduino IDE against the ESP8266 board core plus the Adafruit SSD1306/GFX libraries and an APA102 LED library. PCB design files are in Eagle format (`eagle/nola8.sch` / `.brd`, the final revision) with Gerbers already generated for Seeed's 2-layer process, plus a later, unfinished KiCad conversion (`pcb/nola8.kicad_pcb`) that keeps the ESP-12E and APA102 footprints from the Eagle original.
