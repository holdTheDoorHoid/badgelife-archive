---
title: End Summer Camp Mini Badge 2024
id: other-minibadge-endsummercamp
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2024
makers:
- name: End Summer Camp
  url: https://github.com/endsummercamp
summary: 'The first official End Summer Camp badge with a microcontroller: an RP2040-powered board with 9 RGB(W) LEDs, IR badge-to-badge communication, and a library of built-in light animations.'
functions: Cycles through 12+ built-in light animation effects (selected with a user button), IR remote control and badge-to-badge communication over infrared (NEC/Samsung NEC protocols), USB CDC for debug/control, and USB MIDI so the lights can be driven by standard MIDI messages. Includes automatic over-temperature protection and a torchlight mode (hold the button while powering on).
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - security
tech:
  mcu: RP2040
  leds:
    count: 9
    type: RGBW
    note: 9 addressable RGB(W) LEDs driving the animation engine
  display: null
  connectivity:
  - ir
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
  open_source: true
  hardware_url: https://github.com/endsummercamp/minibadge/tree/master/antani_hw
  firmware_url: https://github.com/endsummercamp/minibadge/tree/master/antani_sw
  eda_tool: KiCad
links:
- label: github.com/endsummercamp/minibadge
  url: https://github.com/endsummercamp/minibadge
  kind: repo
  archived: https://web.archive.org/web/20251226225553/https://github.com/endsummercamp/minibadge
images:
- file: assets/images/badges/other/minibadge-endsummercamp/e941f90e40.jpg
  source: https://github.com/endsummercamp/minibadge
  credit: End Summer Camp
  caption: 3D render of the End Summer Camp 2024 minibadge
  archived: https://web.archive.org/web/20251226225553/https://github.com/endsummercamp/minibadge
- file: assets/images/badges/other/minibadge-endsummercamp/2d80121836.jpg
  source: https://github.com/endsummercamp/minibadge
  credit: End Summer Camp
  caption: Front view of the End Summer Camp 2024 minibadge PCB
  archived: https://web.archive.org/web/20251226225553/https://github.com/endsummercamp/minibadge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/endsummercamp/minibadge
  title: minibadge (endsummercamp)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
  archived: https://web.archive.org/web/20251226225553/https://github.com/endsummercamp/minibadge
- kind: url
  url: https://raw.githubusercontent.com/endsummercamp/minibadge/master/README.md
  title: End Summer Camp - Mini Badge 2024 (README)
  accessed: '2026-09-07'
  note: Confirms event/year (End Summer Camp 2024), RP2040 MCU, 9 RGB(W) LEDs, IR comms, USB CDC/MIDI, licensing (GPLv3 firmware, CERN-OHL-P hardware), and full credits list.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Made for "End Summer Camp" (ESC), an Italian hacker camp/CHAOS-style event; no matching event id exists in _data/events.yml, so event is left as "other". Price, quantity made, and distribution/availability were not stated anywhere in the repo or its docs; left empty. No storefront or press coverage found in a short search beyond the GitHub repo itself.
last_modified_date: '2026-09-07'
---

The End Summer Camp Mini Badge 2024 was, per the maker's own README, "the first official ESC badge with a microcontroller" — a step up for End Summer Camp (ESC), an Italian hacker camp, from earlier passive badges. It is built around an RP2040 microcontroller driving 9 RGB(W) LEDs through a composable animation engine, with more than a dozen built-in light patterns (with names like "hacker glider," "gigaPride," and "under arrest") that attendees cycle through with a button press.

Beyond decorative lighting, the badge has an infrared transmitter and receiver supporting the NEC and Samsung NEC protocols, used both for IR remote control and for badge-to-badge communication. It also exposes a USB-C connector offering a CDC interface for debug/control and a USB MIDI interface, so the LED animations can be driven directly by standard MIDI messages. Firmware includes automatic over-temperature protection and a torchlight mode activated by holding the button down at power-on.

The project is fully open source: hardware design files (KiCad) live in the repo's `antani_hw/` directory under the CERN Open Hardware Licence v2 (Permissive), and firmware in `antani_sw/` is released under GPLv3, alongside a `minibadge-cli` tool for interacting with the badge from a computer. The README credits a large team led by "Kezii" and "sebastiano," with contributions from over a dozen named community members. No information on unit pricing, quantity produced, or how it was distributed to attendees was found in the repository or its documentation.
