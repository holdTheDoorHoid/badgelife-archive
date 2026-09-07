---
title: Spiral Matrix Petal
id: supercon-2024-supercon-8-spiral-matrix-petal
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Hackaday
  url: https://github.com/Hack-a-Day
summary: An LED-matrix SAO shipped with the Supercon 8 badge (repo folder and BOM call it Petal Matrix), driven by an AS1115 I2C display driver with an RGB LED at the center.
functions: 'Blinky LED effects driven over I2C by the AS1115 display driver, with an RGB LED at the center; the chip has extra features beyond basic blinking ("hidden goodies in the datasheet").'
look:
  colors: []
  shape: null
  themes:
  - floral
tech:
  mcu: none
  leds:
    count: null
    type: RGB
    note: AS1115 I2C LED matrix driver plus a center RGB LED; exact LED count not stated in the sources reviewed.
  display: LED matrix
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Shipped as one of several interchangeable "petal" SAOs bundled with the Supercon 8 badge (2024 Hackaday Superconference); not sold separately as far as sources found.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/petal_matrix
  firmware_url: null
  eda_tool: null
links:
- label: github.com/astuder/2024-Supercon-8-Add-On-Badge
  url: https://github.com/astuder/2024-Supercon-8-Add-On-Badge
  kind: repo
- label: github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/petal_matrix
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/petal_matrix
  kind: repo
- label: github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  kind: repo
images:
- file: assets/images/badges/supercon-2024/supercon-8-spiral-matrix-petal/38250a51d1.jpg
  source: "https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/petal_matrix"
  credit: "Hackaday"
  caption: "Petal Matrix SAO prototype photo"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/astuder/2024-Supercon-8-Add-On-Badge
  title: 2024 Supercon 8 -- Supercon Add-On Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/petal_matrix
  title: hardware/sao/petal_matrix at main - Hack-a-Day/2024-Supercon-8-Add-On-Badge
  accessed: '2026-09-07'
  note: Confirms name "Spiral Matrix Petal" / "Petal Matrix", AS1115 I2C display driver, center RGB LED, and design/Gerber files; references a prototype photo used here.
- kind: url
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  title: Hack-a-Day/2024-Supercon-8-Add-On-Badge
  accessed: '2026-09-07'
  note: Confirms the badge is a 6-SAO I2C hub for Supercon 8 (2024) and Hackaday Europe 2025, running MicroPython, open source on GitHub; lists Petal Matrix among the bundled petal SAOs (with touchwheel petal, LED petal, and an I2C protoboard petal).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Sources confirm the SAO's identity, its AS1115 driver, the center RGB LED, and that it
    shipped as one of several bundled "petal" SAOs for the Supercon 8 (2024) badge (also used
    at Hackaday Europe 2025). Could not find a named individual designer, exact LED count,
    EDA tool, license, price, or production quantity in the pages fetched -- these are left
    empty rather than guessed. No separate storefront listing was found, suggesting it was
    distributed only with the badge rather than sold on its own.
last_modified_date: '2026-09-07'
---

The Spiral Matrix Petal -- called "Petal Matrix" in the project's own folder and BOM -- is one of several interchangeable SAO "petals" Hackaday designed for the 2024 Supercon 8 badge, a six-port I2C hub badge also reused at Hackaday Europe 2025. Rather than driving individual LEDs directly, it uses an AS1115 I2C LED-matrix display driver chip, with a single RGB LED at its center, giving it a distinct blinky-effects role alongside the badge's other petals (a touchwheel petal, a plain LED petal, and an I2C protoboard petal built around a CH32V003 for making custom devices).

The hardware is open source, published in the Hack-a-Day GitHub organization's `2024-Supercon-8-Add-On-Badge` repository alongside Gerbers and schematic files for the petal. The badge itself runs MicroPython and is programmable over serial with tools like Thonny or VSCode, letting owners write their own effects for the matrix. Sources reviewed did not give a named individual designer, a bill of materials, a production quantity, or a price -- it appears to have shipped bundled with the Supercon 8 badge rather than sold separately, but that could not be confirmed with certainty.

## Make your own

Hardware design files (schematic/PCB) for the Petal Matrix SAO are in the Hack-a-Day repo under `hardware/sao/petal_matrix`, including Gerbers ready for fabrication. No separate firmware repo for the SAO itself was found; the host badge's MicroPython firmware and I2C libraries (in the main repo) are what drive it.
