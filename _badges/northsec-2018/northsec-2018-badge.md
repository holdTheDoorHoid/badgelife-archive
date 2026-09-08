---
title: NorthSec 2018 Badge
id: northsec-2018-northsec-2018-badge
layout: badge
parent: NorthSec 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: northsec-2018
year: 2018
makers:
- name: NorthSec
summary: The official electronic conference badge for NorthSec 2018, built around a Nordic nRF52832 and an STM32F070 USB co-processor, with an OLED display, NeoPixel RGB LEDs, and Bluetooth Low Energy.
functions: 'Customizable NeoPixel LED patterns (some unlocked by finding codes during the conference), BLE services to remotely set LED segment colors/modes/speed/brightness and to set the wearer''s name and avatar (protected by a sync key), and a USB port that exposes a Black Magic Probe-style GDB stub for live firmware debugging/hacking of the nRF52.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - radio
tech:
  mcu: nRF52832
  leds:
    count: null
    type: NeoPixel
    note: RGB NeoPixel LEDs driven via a ported WS2812FX library; secondary STM32F070F6P6 (Cortex-M0) handles USB.
  display: OLED
  connectivity:
  - ble
  - usb
  battery: 1x ICR14500 3.7V Li-ion rechargeable, chargeable over USB (power switch must stay on during charge)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Conference badge for NorthSec 2018 attendees; a NorthSec Facebook post from that period said stock was very limited ("VERY LIMITED number of Electronic Badges left"), but no price or total quantity is stated in the sources found.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/nsec/nsec-badge/tree/nsec18
  firmware_url: https://github.com/nsec/nsec-badge/tree/nsec18
  eda_tool: null
links:
- label: github.com/nsec/nsec-badge/tree/nsec18
  url: https://github.com/nsec/nsec-badge/tree/nsec18
  kind: repo
- label: NorthSec 2018 Badge companion site (source)
  url: https://github.com/marc-etienne/nsec-badge-2018-web/blob/gh-pages/index.html
  kind: doc
images: []
contact: {}
notes:
- Official NorthSec 2018 badge; source on the nsec18 branch of nsec/nsec-badge. Found by the event-year sweep, task northsec.
- 'The repo README links a "Badge website" at http://sputnak.ga/, which no longer resolves (dead/expired domain) as of 2026-09-08; not used as a source.'
- 'A linked schematic PDF (xn--rr8b.ga) was not fetched since it sits on the same expired-looking domain family; hardware/BOM/PCB links in the repo README were themselves empty placeholders in the source.'
status: released
sources:
- kind: url
  url: https://github.com/nsec/nsec-badge/tree/nsec18
  title: NorthSec 2018 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:northsec); event read as ''northsec-2018''.'
- kind: url
  url: https://raw.githubusercontent.com/nsec/nsec-badge/nsec18/README.md
  title: 'nsec/nsec-badge README (nsec18 branch)'
  accessed: '2026-09-08'
  note: 'Confirmed MCU (nRF52832 + STM32F070F6P6), OLED display, NeoPixel LEDs, BLE, battery (1x ICR14500 Li-ion + USB charging), and that hardware/firmware are open source (BOM/PCB links in the README were empty).'
- kind: url
  url: https://github.com/marc-etienne/nsec-badge-2018-web/blob/gh-pages/index.html
  title: The NorthSec 2018 Badge (companion docs site)
  accessed: '2026-09-08'
  note: 'Confirmed LED customization/unlockable patterns, BLE LED-control and identity services, and the USB GDB-stub debug feature.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Maker''s own GitHub repo and a companion docs site (by the same badge team) confirm the hardware and features; no price, quantity, or availability figure was found anywhere. The badge''s own linked "website" (sputnak.ga) is now a dead/expired domain and was not used. Could not verify a still-live PCB/BOM/Gerber link; the README''s own links for those were empty placeholders, so open_source is marked partial rather than yes.'
last_modified_date: '2026-09-08'
---

The NorthSec 2018 badge was the official conference badge handed out at NorthSec, Montreal's applied-security conference. It runs two microcontrollers: a Nordic nRF52832 (ARM Cortex-M4F) that drives the OLED display, Bluetooth Low Energy, battery management, buttons, and a strip of NeoPixel RGB LEDs, and a smaller STMicroelectronics STM32F070F6P6 (Cortex-M0) dedicated to the USB port. Power comes from a single ICR14500 3.7V Li-ion cell, USB, or both, with USB charging while the badge is switched on.

Beyond stock functions, the badge exposed itself to attendees for tinkering: two BLE GATT services let a nearby phone or laptop customize LED segments (index range, mode, color, speed, brightness) or change the wearer's displayed name and avatar, the latter gated by a sync-key check. Some additional LED patterns were only unlocked by finding codes during the event. The USB port doubled as a debug interface, presenting a Black Magic Probe-style GDB stub so attendees could attach a debugger directly to the nRF52 and inspect or modify the running firmware.

Hardware and firmware source is published on the `nsec18` branch of the `nsec/nsec-badge` GitHub repository, alongside a companion documentation site describing the BLE services in detail. No price, production quantity, or clear current availability could be confirmed from the sources found; a period NorthSec Facebook post mentioned the electronic badges running low ahead of the 2018 event, suggesting a limited run, but gave no number.
