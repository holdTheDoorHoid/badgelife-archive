---
title: NorthSec 2019 Badge
id: northsec-2019-northsec-2019-badge
layout: badge
parent: NorthSec 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: northsec-2019
year: 2019
makers:
- name: NorthSec
  url: https://nsec.io/
  role: Team Badge
summary: The official electronic conference badge for NorthSec 2019, cut in a brain-shaped outline and built around two microcontrollers to drive a color display, NeoPixel LEDs, buttons, and Bluetooth Low Energy.
functions: Runs a boot animation and menu system on its color screen, lights NeoPixel RGB LEDs, communicates over Bluetooth Low Energy, and is used for badge/CTF-related interactions during the conference.
look:
  colors:
  - pink
  - white
  shape: other
  themes:
  - security
  - wearable
tech:
  mcu: nRF52832 + STM32F070F6P6
  leds:
    count: null
    type: NeoPixel
    note: White NeoPixel RGB LEDs outlining the brain-shaped PCB, driven by the nRF52832.
  display: 0.96" 80x160 RGB IPS LCD
  connectivity:
  - ble
  - usb
  inputs:
  - buttons
  power: USB and/or 1x ICR14500 3.7V Li-ion rechargeable battery
  battery: ICR14500 (3.7V Li-ion)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Distributed to attendees of NorthSec 2019 (Montreal); exact distribution method not stated in sources found.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/nsec/nsec-badge/tree/nsec19
  firmware_url: https://github.com/nsec/nsec-badge/tree/nsec19
  eda_tool: null
  notes: 'Schematics, firmware source, and pre-built firmware images are published on the nsec19 branch; the PCB and bill-of-material links in the repo README were empty placeholders at time of research. The nRF52 firmware depends on Nordic''s proprietary SDK/SoftDevice, which carries its own license, so hardware/firmware is only partially open.'
links:
- label: github.com/nsec/nsec-badge/tree/nsec19
  url: https://github.com/nsec/nsec-badge/tree/nsec19
  kind: repo
- label: NorthSec badge page
  url: https://nsec.io/badge/
  kind: website
images:
- file: assets/images/badges/northsec-2019/northsec-2019-badge/317c4ec0f4.jpg
  source: "https://www.linkedin.com/posts/northsec_nsec19-badgelife-activity-6533345100750217216-VyhC"
  credit: "NorthSec"
  caption: "NorthSec 2019 badge with RGB display and NeoPixel LEDs, from NorthSec's own LinkedIn post"
contact: {}
notes:
- Official NorthSec 2019 badge; source on the nsec19 branch of nsec/nsec-badge. Found by the event-year sweep, task northsec.
- The community sheet's wording ("NorthSec 2019 Badge") matches how NorthSec itself refers to it; title unchanged.
status: released
sources:
- kind: url
  url: https://github.com/nsec/nsec-badge/tree/nsec19
  title: NorthSec 2019 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:northsec); event read as ''northsec-2019''.'
- kind: url
  url: https://raw.githubusercontent.com/nsec/nsec-badge/nsec19/README.md
  title: 'nsec-badge README (nsec19 branch)'
  accessed: '2026-09-08'
  note: 'Confirms dual-MCU design (nRF52832 + STM32F070F6P6), OLED/display, NeoPixel LEDs, BLE, USB, battery (ICR14500), schematic and firmware availability, and that the Nordic SDK/SoftDevice carry a separate proprietary license.'
- kind: url
  url: https://www.linkedin.com/posts/northsec_nsec19-badgelife-activity-6533345100750217216-VyhC
  title: 'NorthSec LinkedIn post, #nsec19 #badgelife'
  accessed: '2026-09-08'
  note: 'NorthSec''s own post confirms an 80x160 RGB IPS screen and 15 NeoPixel RGB LEDs, and supplied the badge photo used here; the photo also shows the badge cut as a brain shape and labels the display module "0.96in 80x160(RGB)IPS".'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'The repo README calls the screen an "OLED display" but the physical part (visible in the photo and its own silkscreen) is a 0.96" 80x160 RGB IPS LCD module, not OLED; this entry uses the more specific, maker-photographed spec. LED count is reported as 15 in NorthSec''s own social post but was not independently confirmed against the schematic, so tech.leds.count is left empty rather than guessed. Price, quantity made, and exact distribution method (registration swag vs. purchase) were not stated in any source found; PCB and BOM links in the repo README are empty placeholders. "TALOS" printed on the pictured unit appears to be a badge-holder name or team label, not a product name, and was not treated as such.'
last_modified_date: '2026-09-08'
---

The NorthSec 2019 badge is the official electronic conference badge for NorthSec, the Montreal-based hacker/security conference, built by the event's own Team Badge. It is cut into a brain-shaped PCB and carries a 0.96" 80x160 RGB IPS color display, NeoPixel RGB LEDs around its edge, a 4-way button cluster, and Bluetooth Low Energy — worn on an "nsec" lanyard as conference credential and interactive gadget in one.

Electronically it splits work across two chips: a Nordic nRF52832 (ARM Cortex-M4F) that drives the display, LEDs, buttons, battery management, and BLE radio, and an STMicroelectronics STM32F070F6P6 (ARM Cortex-M0) dedicated to the USB port. It can run from USB power or a single ICR14500 3.7V Li-ion cell, with charging handled through USB while the power switch is on.

NorthSec published schematics, firmware source, and several pre-built firmware images for the nsec19 branch of its `nsec-badge` repository, along with SWD and USB-DFU programming instructions — though the nRF52's firmware depends on Nordic's own SDK and SoftDevice, each under its own license, and the repo's PCB/BOM links were left empty, so the release is open in spirit but incomplete in practice.
