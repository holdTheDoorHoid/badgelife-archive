---
title: Limited Ham Radio Fox Badge
id: dc31-limited-ham-radio-fox-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: rot13labs
  url: https://www.tindie.com/stores/rot13labs/
summary: A functioning VHF "fox" transmitter badge built by rot13labs for a DEF CON 31 fox hunt, later sold in a limited production run of 100.
functions: Broadcasts a musical tone sequence followed by a Morse code identification on a 20-second transmit cycle with 30-second gaps, for radio direction-finding ("fox hunting") games.
look:
  colors:
  - black
  - silver
  shape: null
  themes:
  - radio
  - hardware tool
tech:
  mcu: Seeed XIAO ESP32C3
  leds:
    count: null
    type: discrete
    note: LEDs on the radio power and transmit pins for troubleshooting, per the firmware repo.
  display: none
  connectivity:
  - usb
  - sub-ghz
  battery: LiPo 2000 mAh
  sao_version: null
get_one:
  price: $80
  price_usd: 80
  quantity: 100
  availability: sold_out
  distribution:
  - purchase
  where: Sold on Tindie by rot13labs; the listing was retired after the 100-unit run and the seller noted they were "taking a break" from making more, with a restock waitlist.
make_your_own:
  open_source: yes
  hardware_url: null
  firmware_url: https://github.com/c0ldbru/fox
  eda_tool: null
  license: GPL-3.0
  notes: Firmware (fox.ino, Arduino IDE) is adapted from Gregory Stoike's "Yet Another Foxbox" (YAFB). Frequency, delay, and callsign are user-configurable; firmware is uploaded over USB-C via a boot-select button.
links:
- label: www.tindie.com/products/rot13labs/limited-ham-radio-fox-badge
  url: https://www.tindie.com/products/rot13labs/limited-ham-radio-fox-badge/
  kind: store
- label: github.com/c0ldbru/fox
  url: https://github.com/c0ldbru/fox
  kind: repo
images:
- file: assets/images/badges/dc31/limited-ham-radio-fox-badge/1f953f1dcf.png
  source: "https://www.tindie.com/products/rot13labs/limited-ham-radio-fox-badge/"
  credit: "rot13labs"
  caption: "Silver finish Limited Ham Radio Fox Badge"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/rot13labs/limited-ham-radio-fox-badge/
  title: Limited Ham Radio Fox Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''unknown''.'
- kind: url
  url: https://github.com/c0ldbru/fox
  title: c0ldbru/fox
  accessed: '2026-09-07'
  note: Firmware repo; confirms MCU (XIAO ESP32C3), radio module (NiceRF SA868), LED placement, GPL-3.0 license, and that it is adapted from Gregory Stoike's YAFB project.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Tindie listing states the badge was originally made for DEF CON 31 (2023) as fox-hunt prizes, then sold in a final limited run of 100 (black and silver). Designer credited as @skyehopper on the listing. The firmware repo does not itself name an event or transmit power/frequency, and neither source gives an exact chip datasheet beyond "Seeed XIAO ESP32C3" plus a NiceRF SA868 radio module. Could not verify the maker's own site/socials beyond Tindie and GitHub; no second corroborating source was reachable within the search budget for this run.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/limited-ham-radio-fox-badge/
---

The Limited Ham Radio Fox Badge is a working VHF transmitter built by rot13labs (Gainesville, FL) as a "fox" for a radio direction-finding hunt at DEF CON 31 in 2023. Rather than a wearable badge, it is a small transmitter board: it broadcasts a short musical tone sequence followed by a Morse code station identifier on a 20-second cycle, with 30-second gaps, for hunters carrying receivers to track down by signal strength.

After the con, rot13labs sold a final production run of 100 units on Tindie for $80 each, in black and silver finishes, along with a 2000 mAh LiPo battery and rot13labs stickers. The badge is built around a Seeed XIAO ESP32C3 paired with a NiceRF SA868 radio module, with onboard LEDs on the power and transmit lines for troubleshooting. Transmit frequency, timing, and callsign are all configurable by editing and re-flashing the Arduino sketch over USB-C.

## Make your own

The firmware is open source (GPL-3.0) at [c0ldbru/fox](https://github.com/c0ldbru/fox), adapted from Gregory Stoike's "Yet Another Foxbox" (YAFB) project. To build one: assemble a XIAO ESP32C3 with a NiceRF SA868 radio module and status LEDs, edit `fox.ino` in the Arduino IDE to set your frequency/callsign/timing, and flash it over USB-C by holding the board's boot-select button. No separate hardware design files (schematic/PCB) were found published alongside the firmware.
