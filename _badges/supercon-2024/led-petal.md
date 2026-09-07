---
title: LED Petal
id: supercon-2024-led-petal
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
summary: An LED-matrix SAO shipped with the Supercon 8 (2024) badge; the repo folder and BOM call it "Petal Matrix" / "Spiral Matrix Petal", built around an AS1115 I2C display driver with a center RGB LED.
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
  where: Shipped as one of several interchangeable "petal" SAOs bundled with the Supercon 8 badge (2024 Hackaday Superconference, also reused at Hackaday Europe 2025); not sold separately as far as sources found.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/petal_matrix
  firmware_url: null
  eda_tool: null
links:
- label: github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao
  kind: repo
- label: github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/petal_matrix
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/petal_matrix
  kind: repo
- label: github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  kind: repo
images:
- file: assets/images/badges/supercon-2024/led-petal/38250a51d1.jpg
  source: "https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/petal_matrix"
  credit: "Hackaday"
  caption: "Spiral Matrix Petal (LED Petal) SAO, populated with the AS1115 driver and center RGB LED"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- This appears to be a duplicate of the entry "Spiral Matrix Petal" (id supercon-2024-supercon-8-spiral-matrix-petal), which covers the same SAO under the name used in its repo folder and BOM. The badge's own README casually calls it "the LED petal" when contrasting it with "the Touchwheel petal," which is likely how this entry's title originated. No separate "led_petal" folder or distinct plain-LED SAO was found in the repo; only TouchwheelSAO, i2c_proto_petal, petal_matrix, and pure_proto_petal exist under hardware/sao.
status: released
sources:
- kind: url
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao
  title: LED Petal
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''supercon-2024''.'
- kind: url
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/petal_matrix
  title: hardware/sao/petal_matrix at main - Hack-a-Day/2024-Supercon-8-Add-On-Badge
  accessed: '2026-09-07'
  note: README names it "Spiral Matrix Petal," AS1115 I2C display driver, center RGB LED; includes schematic/Gerber files and a prototype photo used here.
- kind: url
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  title: Hack-a-Day/2024-Supercon-8-Add-On-Badge
  accessed: '2026-09-07'
  note: Main README confirms the badge is a 6-SAO I2C hub for Supercon 8 (2024)/Hackaday Europe 2025, running MicroPython; casually refers to "the LED and Touchwheel petals" among the bundled SAOs, which is the likely source of this entry's title.
- kind: url
  url: https://raw.githubusercontent.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/main/i2c-addresses.md
  title: i2c-addresses.md
  accessed: '2026-09-07'
  note: Lists "LED Petal Matrix" (AS1115, address 0x00) as the only LED-matrix SAO among the badge's I2C devices, supporting that this and "Spiral Matrix Petal" name the same part.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    This entry appears to duplicate supercon-2024-supercon-8-spiral-matrix-petal: the repo has
    no folder or product distinct from "petal_matrix" that matches a plain "LED Petal" name, and
    the badge's own README/i2c-addresses.md use "LED petal" and "LED Petal Matrix" informally for
    the same AS1115-driven SAO documented there in more detail. Filled in with the same facts found
    for consistency, but flagging as a likely duplicate rather than a distinct item. Could not find
    a named individual designer, exact LED count, EDA tool, license, price, or production quantity.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/led-petal/
---

"LED Petal" appears to be an informal name for the same SAO documented more fully elsewhere in this archive as the "Spiral Matrix Petal" (its repo folder and BOM call it "Petal Matrix"). It is one of several interchangeable SAO "petals" Hackaday designed for the 2024 Supercon 8 badge, a six-port I2C hub badge also reused at Hackaday Europe 2025. Rather than driving individual LEDs directly, it uses an AS1115 I2C LED-matrix display driver chip with a single RGB LED at its center. The project's main README casually refers to "the LED and Touchwheel petals" when describing the badge's bundled add-ons, which is the likely source of this entry's title -- no separate folder or product distinct from "petal_matrix" was found in the repository.

The hardware is open source, published in the Hack-a-Day GitHub organization's `2024-Supercon-8-Add-On-Badge` repository alongside Gerbers and schematic files. Sources reviewed did not give a named individual designer, a production quantity, or a price; it appears to have shipped bundled with the Supercon 8 badge rather than sold separately.

## Make your own

Hardware design files (schematic/PCB, Gerbers) are in the Hack-a-Day repo under `hardware/sao/petal_matrix`. No separate firmware repo for the SAO itself was found; the host badge's MicroPython firmware and I2C libraries (in the main repo) are what drive it.
