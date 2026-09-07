---
title: NorthSec 2025 badge
id: northsec-2025-northsec-2025-badge
layout: badge
parent: Northsec 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: northsec-2025
year: 2025
makers:
- name: NorthSec
  url: https://github.com/nsec
summary: The official electronic badge for NorthSec 2025, an ESP32-C3 based conference/CTF badge with 18 NeoPixel RGB LEDs, five buttons, IR pairing, and two SAO ports.
functions: Runs conference and CTF firmware builds; used for badge-to-badge IR pairing and Capture The Flag challenges at the conference.
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
  - hardware tool
tech:
  mcu: ESP32-C3-WROOM-02-N4
  leds:
    count: 18
    type: NeoPixel (WS2812-family RGB)
    note: null
  display: none
  connectivity:
  - ble
  - ir
  - usb
  battery: 3x AAA (backup); primary power via USB-C
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/nsec/nsec-badge/tree/nsec25/hw/2025
  firmware_url: https://github.com/nsec/nsec-badge/tree/nsec25
  eda_tool: null
links:
- label: github.com/nsec/nsec-badge/tree/nsec25
  url: https://github.com/nsec/nsec-badge/tree/nsec25
  kind: repo
images:
- file: assets/images/badges/northsec-2025/northsec-2025-badge/42d2b087d3.png
  source: "https://github.com/nsec/nsec-badge/tree/nsec25"
  credit: "NorthSec"
  caption: "NorthSec 2025 conference/CTF badge (nsec25 hardware repo photo)"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/nsec/nsec-badge/tree/nsec25
  title: NorthSec 2025 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''northsec-2025''.'
- kind: url
  url: https://raw.githubusercontent.com/nsec/nsec-badge/nsec25/README.md
  title: nsec-badge README (nsec25 branch)
  accessed: '2026-09-07'
  note: 'Confirms ESP32-C3-WROOM-02-N4 MCU, 18 NeoPixel LEDs, 5 buttons, 2 SAO v1.69bis connectors, IR pairing connector, USB-C/3xAAA power, conference and CTF firmware builds.'
- kind: url
  url: https://github.com/nsec/nsec-badge/raw/nsec25/hw/2025/badge2025.png
  title: badge2025.png
  accessed: '2026-09-07'
  note: 'Photo of the assembled 2025 badge, saved to images.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Repo (nsec/nsec-badge, nsec25 branch) confirms it is NorthSec''s official 2025 conference/CTF badge with published hardware and firmware; a LICENSE file exists in the repo but the exact license text was not confirmed. No pricing, quantity, or distribution details (e.g. included with ticket vs. sold) were found in the repo or README; NorthSec conference badges are typically given to attendees rather than sold, but this was not confirmed by a source, so get_one fields are left empty/unknown.'
last_modified_date: '2026-09-07'
---

The NorthSec 2025 badge is the official electronic badge for NorthSec, a Montreal-based applied security conference and CTF. It is built around an ESP32-C3-WROOM-02-N4 microcontroller and carries 18 NeoPixel RGB LEDs, five pushbuttons, an IR connector for badge-to-badge pairing, and two Shitty Add-On (SAO v1.69bis) headers for plugging in third-party add-ons. It can run from USB-C or from three AAA batteries.

The badge ships with two firmware builds: a "conference" mode for general attendee use and a "CTF" mode tied into NorthSec's on-site Capture The Flag competition, reflecting the badge's dual role as both a wearable and a puzzle/game platform during the event. Both the hardware design files and firmware source are published in NorthSec's `nsec-badge` GitHub repository under the `nsec25` branch, built with the Espressif IoT Development Framework and PlatformIO.

## Make your own

Hardware design files for the 2025 badge are in `hw/2025` of the [nsec-badge repository](https://github.com/nsec/nsec-badge/tree/nsec25), and firmware source is in the same repository, built with PlatformIO against the Espressif IDF. The README documents building both the conference and CTF firmware variants and flashing/debugging over USB serial at 115200 baud.
