---
title: NorthSec 2023 badge
id: northsec-2023-northsec-2023-badge
layout: badge
parent: Northsec 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: northsec-2023
year: 2023
makers:
- name: NorthSec
  url: https://nsec.io/
summary: 'The official conference badge for NorthSec 2023, an ATmega328PB-based badge with 16 NeoPixel RGB LEDs, six buttons, an optional OLED display, and an SAO connector.'
functions: 'Runs custom Arduino-framework firmware driving 16 addressable RGB LEDs and six buttons; supports an optional 128x32 OLED display and two badge-to-badge pairing connectors (their function is not described in available sources).'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ATmega328PB
  leds:
    count: 16
    type: NeoPixel
    note: WS2812-family addressable RGB LEDs
  display: 128x32 OLED (optional)
  connectivity: []
  inputs:
  - buttons
  power: USB-C
  battery: 3x AAA
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed to NorthSec 2023 conference attendees (Montreal); exact distribution/purchase terms not stated in available sources.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/nsec/badge-conf-2023/tree/nsec2023/PCB
  firmware_url: https://github.com/nsec/badge-conf-2023
  eda_tool: null
  notes: 'Firmware built with PlatformIO on the Arduino framework using the MiniCore core; pre-built firmware.hex provided in binary/ for flashing via USBasp/AVRDUDE. Repository also includes a separate SAO PCB design under PCB/SAO.'
links:
- label: github.com/nsec/badge-conf-2023
  url: https://github.com/nsec/badge-conf-2023
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/nsec/badge-conf-2023
  title: NorthSec 2023 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''northsec-2023''.'
- kind: url
  url: https://raw.githubusercontent.com/nsec/badge-conf-2023/nsec2023/README.md
  title: badge-conf-2023 README
  accessed: '2026-09-07'
  note: 'Confirmed MCU (ATmega328PB), 16 NeoPixels, six buttons, two pairing connectors, one SAO v1.69bis connector, optional 128x32 OLED, USB-C/3xAAA power, and open firmware built with PlatformIO/MiniCore.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07) re-fetched both cited sources (github.com/nsec/badge-conf-2023 repo page and its nsec2023-branch README) and confirmed MCU, LED count/type, button count, SAO v1.69bis connector and count, OLED presence, USB-C/3xAAA power, PlatformIO+MiniCore firmware, firmware.hex in binary/, MIT license, and the PCB/SAO subdirectory. Two claims in the original draft were not supported by the sources and were removed/corrected: the README does not state the OLED''s physical size (the invented "0.91\"" was dropped, leaving just "128x32 OLED"), and it does not say what the two pairing connectors do (the invented claim that they let badges "interact with each other" was removed from functions and the body). get_one.distribution was set to purchase with no supporting source found, contradicting the entry''s own notes that distribution terms were unconfirmed; cleared to empty. No price, quantity, availability, colors, shape, or images were found in any source, so those fields remain empty. Everything remaining in the entry is supported by the two cited sources.'
last_modified_date: '2026-09-07'
---

The NorthSec 2023 badge is the official electronic conference badge for NorthSec, the Montreal-based security conference, given to attendees at the 2023 event. It is built around an ATmega328PB microcontroller (an Arduino UNO-like part) and carries sixteen NeoPixel RGB LEDs and six buttons. A single Shitty Add-On (SAO) v1.69bis connector lets attendees plug in add-on boards, and the badge design supports an optional 128x32 OLED display. It can run on USB-C power or three AAA batteries. The badge also has two "pairing" connectors, though the repository does not describe what function they serve.

NorthSec publishes the badge's hardware and firmware together on GitHub under the `nsec/badge-conf-2023` repository. The firmware is written against the Arduino framework using the MiniCore core and built with PlatformIO; a pre-compiled `firmware.hex` is provided for attendees who want to flash the stock image with an inexpensive USBasp programmer rather than build it themselves. The repository also contains a separate SAO PCB design, suggesting NorthSec made add-on boards available alongside the main badge.

No price, production quantity, or sale/distribution details for the badge were found in the sources checked; it appears to have been given to conference attendees rather than sold as a standalone consumer product, but this could not be confirmed from the maker's own materials.

## Make your own

Hardware (PCB) and firmware are both openly published in the `nsec/badge-conf-2023` GitHub repository (see the `PCB/` and `src/` directories, `nsec2023` branch). To flash the stock firmware, use an AVR-compatible programmer such as a USBasp with AVRDUDE and the provided `binary/firmware.hex`. To modify the firmware, install PlatformIO and build against the MiniCore Arduino core as documented in the repository's README.
