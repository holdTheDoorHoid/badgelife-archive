---
title: DC801 GP2040-CE DC32 Controller Badge
id: dc32-dc801-gp2040-ce-dc32-controller-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: DC801
  url: https://github.com/dc801
summary: A gamepad-style controller badge from the DC801 group for DEF CON 32, built on an RP2040 running a custom fork of the GP2040-CE gamepad firmware.
functions: Acts as a USB/BLE game controller (X-Input, Switch, PlayStation, and other GP2040-CE-supported modes), with analog stick/trigger input added via an external ADC and wireless controller support added via a Bluetooth module.
look:
  colors: []
  shape: null
  themes:
  - console
  - arcade
tech:
  mcu: RP2040
  leds: null
  display: null
  connectivity:
  - ble
  - usb
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
  firmware_url: https://github.com/dc801/GP2040-CE
  eda_tool: null
links:
- label: github.com/dc801/GP2040-CE
  url: https://github.com/dc801/GP2040-CE
  kind: repo
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/dc801/GP2040-CE
  title: DC801 GP2040-CE DC32 Controller Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 32, fork adding analog inputs + BLE for the DC32 controller badge''.'
- kind: url
  url: https://raw.githubusercontent.com/dc801/GP2040-CE/main/README.md
  title: DC801 fork README — GP2040-CE
  accessed: '2026-09-07'
  note: 'Confirms the fork targets an RP2040 chip on "the DC801 Defcon 32 Controller Badge", adding a TLA2528 ADC chip for analog inputs and an ESP32-C3 Super Mini module for Bluetooth controller support.'
- kind: url
  url: https://github.com/dc801
  title: DC801 GitHub org
  accessed: '2026-09-07'
  note: 'Lists the GP2040-CE fork among DC801''s repos; no separate hardware/schematic repo for this badge found.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Only source available is the DC801 fork of GP2040-CE and its README; no dedicated hardware repo, storefront listing, photos, price, or quantity information was found via web search. Could not confirm LEDs, display, exact power/battery arrangement, or SAO header presence. The badge is a controller device (buttons/stick input) rather than a display badge, consistent with the GP2040-CE gamepad-firmware basis, but no image of the physical hardware was located to verify form factor.'
last_modified_date: '2026-09-07'
---

DC801, the Salt Lake City DEF CON group known for a series of badges at past cons, built a game-controller badge for DEF CON 32 (2024). Rather than write firmware from scratch, they forked GP2040-CE — an open-source, low-latency gamepad firmware widely used in arcade sticks and fight sticks — to run on the badge's RP2040 microcontroller.

The fork's two additions are a TLA2528 ADC chip, which brings analog stick/trigger input to a firmware that is normally digital-button-focused, and an ESP32-C3 Super Mini module, which adds Bluetooth so the badge can act as a wireless game controller. Everything else — the multi-platform input modes (X-Input, Nintendo Switch, PlayStation 4/5, Xbox One, D-Input, keyboard), SOCD cleaning, per-button RGB support, and the web-based configurator — carries over from upstream GP2040-CE.

No hardware repository, storefront listing, price, quantity, or photos of the physical badge were found; the only public trace of the project is the firmware fork and its README, which the maintainers note may not track future upstream GP2040-CE releases.
