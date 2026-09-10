---
title: BSides Vilnius 2026 Badge
id: bsides-vilnius-2026-bsides-vilnius-2026-badge
layout: badge
parent: BSides Vilnius 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-vilnius-2026
year: 2026
makers:
- name: BSides-Vilnius
summary: 'The official electronic badge for BSides Vilnius 2026, an STM32H5-based badge with an LCD, a temperature/humidity sensor, sparkling LED effects, and a SAO connector.'
functions: 'Shows graphics on its LCD, reads and displays live temperature/humidity from an onboard sensor, runs sparkling LED effects, drives animations on an attached SAO, and exposes a USB virtual COM port; a button (with debouncing) drives its menus and also enters USB DFU mode for reflashing.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: STM32H563RIT6
  leds:
    count: null
    type: null
    note: 'Firmware includes a "sparkling" LED effect (led_thread_entry); count/type not documented.'
  display: LCD
  connectivity:
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
  hardware_url: https://github.com/BSides-Vilnius/badge2026/tree/main/Other/circuit
  firmware_url: https://github.com/BSides-Vilnius/badge2026
  eda_tool: null
links:
- label: github.com/BSides-Vilnius/badge2026
  url: https://github.com/BSides-Vilnius/badge2026
  kind: repo
- label: badge.gallery/badges/bsides-vilnius-2026-badge
  url: https://badge.gallery/badges/bsides-vilnius-2026-badge
  kind: website
images: []
contact: {}
notes:
- 'Official Lithuanian BSides 2026 electronic badge: STM32H563RIT6 board with SAO connector, temperature/humidity sensor and LCD. Found by the event-year sweep, task bsides-any.'
- 'Sweep title matches the maker''s own repo name and description; no alternate title found.'
status: released
sources:
- kind: url
  url: https://github.com/BSides-Vilnius/badge2026
  title: BSides Vilnius 2026 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-any); event read as ''BSides Vilnius 2026''.'
- kind: url
  url: https://github.com/BSides-Vilnius/badge2026
  title: 'BSides Vilnius badge - README.md'
  accessed: '2026-09-10'
  note: 'Confirmed firmware features (LCD, SAO animation thread, environmental sensor thread, LED sparkle thread, USB CDC/VCP, button debouncing), BSD-2-Clause license, DFU flashing procedure, and that a circuit diagram is published under Other/circuit.'
- kind: url
  url: https://raw.githubusercontent.com/BSides-Vilnius/badge2026/main/BSV2026.ioc
  title: BSV2026.ioc (STM32CubeMX project file)
  accessed: '2026-09-10'
  note: 'Confirmed exact MCU part: STM32H563RITx.'
- kind: url
  url: https://badge.gallery/badges/bsides-vilnius-2026-badge
  title: BSides Vilnius 2026 Badge - badge.gallery
  accessed: '2026-09-10'
  note: 'Corroborated event dates (June 3-4, 2026, Kablys, Vilnius) and MCU; noted no product photo and no named individual designer.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Firmware and circuit files are public on GitHub under BSD-2-Clause, so hardware/firmware is at least partially open (schematics are shared as a "circuit diagram" rather than full KiCad/Eagle source, hence open_source: partial rather than yes). No maker photo of the physical badge was found on either the repo or badge.gallery, so images/colors/shape/LED count/price/quantity/availability are left empty. No individual designer is credited publicly; file paths reference a "vytautas" local path but this is not a confirmed public credit, so makers is left as the org. Set status to released since BSides Vilnius 2026 (June 3-4, 2026) has already occurred as of this check.'
last_modified_date: '2026-09-10'
---

The BSides Vilnius 2026 badge is the official conference badge for BSides Vilnius, held June 3–4, 2026 at Kablys in Vilnius, Lithuania. It is built around an STM32H563RIT6 microcontroller running Azure RTOS/ThreadX, with an onboard LCD for a graphical interface, a temperature/humidity sensor, and a SAO (simple add-on) connector for expansion hardware.

The firmware runs several concurrent threads: one drives the LCD graphics, one reads and displays the environmental sensor, one runs a sparkling LED effect, and one animates whatever is plugged into the SAO port. The badge also exposes a USB virtual COM port and can be reflashed by the owner over USB DFU (entered by holding the leftmost button at power-on), using STM32CubeProgrammer.

Both hardware and firmware artifacts are published on GitHub (BSides-Vilnius/badge2026) under a BSD-2-Clause license, including a circuit diagram, though full CAD source files were not confirmed. No photo of the assembled badge, pricing, production quantity, or distribution details were found on the repo or on badge.gallery.
