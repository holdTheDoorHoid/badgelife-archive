---
title: Light Rail
id: other-light-rail
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 0
makers:
- name: Nick Brown
  url: https://hackaday.io/nick-brown
summary: A PCB "train badge" whose LED track lights up sequentially to simulate a train picking up and delivering cargo between platforms.
functions: Simulates a train traveling along an LED-lit track, switching between eight forks/crossings via buttons, picking up and delivering cargo from platforms; a three-character seven-segment display shows game status/score. Multiple game modes were planned. Not tied to a specific convention.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - puzzle
tech:
  mcu: ATMega32U4
  leds:
    count: 144
    type: charlieplexed
    note: Yellow "track" LEDs and red "platform" LEDs, driven by an IS31FL3731 charlieplexed LED matrix driver.
  display: 3-character 7-segment
  connectivity: []
  battery: 2x LIR2032 or USB
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/nonik0/Light-Rail
  firmware_url: https://github.com/nonik0/Light-Rail
  eda_tool: KiCad
links:
- label: hackaday.io/project/202885-light-rail
  url: https://hackaday.io/project/202885-light-rail
  kind: hackaday
- label: github.com/nonik0/Light-Rail
  url: https://github.com/nonik0/Light-Rail
  kind: repo
images:
- file: assets/images/badges/other/light-rail/1f4f781abd.jpg
  source: https://hackaday.io/project/202885-light-rail
  credit: Nick Brown
  caption: Light Rail PCB badge with illuminated LED track
- file: assets/images/badges/other/light-rail/db951a05ee.jpg
  source: https://hackaday.io/project/202885-light-rail
  credit: Nick Brown
  caption: Light Rail badge close-up
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: announced
sources:
- kind: url
  url: https://hackaday.io/project/202885-light-rail
  title: Light Rail
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://github.com/nonik0/Light-Rail
  title: nonik0/Light-Rail
  accessed: '2026-09-07'
  note: Confirmed MCU (ATMega32U4), LED count/driver (144 LEDs, IS31FL3731), KiCad hardware design, open-source hardware and firmware (C++/PlatformIO and Rust).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a personal hardware-badge project by Nick Brown (hackaday.io user nick-brown, GitHub nonik0), not tied to any specific convention or year the sources state, so it stays filed under "other". No price, quantity, or sale/distribution info was found; prototypes exist per the Hackaday.io project log but no store listing was located. A linked project writeup at altonimb.us/writeups/light-rail/ returned 404 and could not be checked.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/light-rail.glb
  method: kicad
  source_file: hardware/kicad8.0/light_rail.kicad_pcb
  generated: '2026-09-10'
  bytes: 524584
---

Light Rail is a PCB "train badge" made by Nick Brown (Hackaday.io user nick-brown, GitHub nonik0) as a personal hardware project rather than an item made for or sold at a specific convention. Yellow LEDs along a printed track light up sequentially to simulate a train moving along a rail line, switching between eight forks and crossings via onboard buttons as it picks up and delivers cargo between illuminated red "platform" LEDs. A three-character seven-segment display shows game status or score, and four buttons beneath the track provide control input. The board is driven by an ATMega32U4 microcontroller and lights all 144 LEDs through an IS31FL3731 charlieplexed LED-matrix driver, running on either two LIR2032 cells or USB power.

The hardware (KiCad 8.0) and firmware (both a C++/PlatformIO version and a Rust implementation) are fully open source and published in the `nonik0/Light-Rail` GitHub repository, with the maker crediting PCBWay for manufacturing support on the prototype. As of the last check, the project's Hackaday.io log describes working prototypes and a hardware demo with basic train animation, with additional game modes still in development; no price, production quantity, or sales channel was found, so its availability is recorded as unknown.

## Make your own

Hardware design files (KiCad 8.0) and firmware source (PlatformIO/C++ and a Rust rewrite) are published at https://github.com/nonik0/Light-Rail, which includes the full schematic/PCB project and both firmware implementations needed to build and program a Light Rail board.
