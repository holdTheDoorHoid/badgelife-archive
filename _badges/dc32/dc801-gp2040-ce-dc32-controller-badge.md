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
- label: Source files (GitHub)
  url: https://github.com/hamster/Defcon32-Badge/tree/main/Hardware
  kind: hardware
images: []
contact: {}
notes: []
status: unknown
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
  note: Confirms the fork targets an RP2040 chip on "the DC801 Defcon 32 Controller Badge", adding a TLA2528 ADC chip for analog inputs and an ESP32-C3 Super Mini module for Bluetooth controller support.
- kind: url
  url: https://github.com/dc801
  title: DC801 GitHub org
  accessed: '2026-09-07'
  note: Lists the GP2040-CE fork among DC801's repos; no separate hardware/schematic repo for this badge found.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): confirmed via the DC801 fork README (raw.githubusercontent.com/dc801/GP2040-CE/main/README.md) and repo/org pages that this is a GP2040-CE fork targeting an RP2040 on "the DC801 Defcon 32 Controller Badge", adding a TLA2528 ADC and an ESP32-C3 Super Mini for BLE, and listing the SOCD cleaning modes, per-button RGB, web configurator, and input modes (X-Input, Switch, PS4/5, Xbox One, D-Input, keyboard) described in functions/body. DC801''s Salt Lake City location and prior DC25-28 badges are confirmed from the GitHub org page. Corrected status from "released" to "unknown": no source found (README, repo, or org page) states the badge was actually manufactured or given to attendees rather than being a firmware project for a planned/prototype badge. Still no dedicated hardware repo, storefront listing, photos, price, or quantity found, so those fields stay empty and confidence stays low.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc32/dc801-gp2040-ce-dc32-controller-badge.glb
  method: kicad
  source_file: Hardware/dc32.kicad_pcb
  generated: '2026-09-07'
  bytes: 2372
---

DC801, the Salt Lake City DEF CON group known for a series of badges at past cons, built a game-controller badge for DEF CON 32 (2024). Rather than write firmware from scratch, they forked GP2040-CE — an open-source, low-latency gamepad firmware widely used in arcade sticks and fight sticks — to run on the badge's RP2040 microcontroller.

The fork's two additions are a TLA2528 ADC chip, which brings analog stick/trigger input to a firmware that is normally digital-button-focused, and an ESP32-C3 Super Mini module, which adds Bluetooth so the badge can act as a wireless game controller. Everything else — the multi-platform input modes (X-Input, Nintendo Switch, PlayStation 4/5, Xbox One, D-Input, keyboard), SOCD cleaning, per-button RGB support, and the web-based configurator — carries over from upstream GP2040-CE.

No hardware repository, storefront listing, price, quantity, or photos of the physical badge were found; the only public trace of the project is the firmware fork and its README, which the maintainers note may not track future upstream GP2040-CE releases.
