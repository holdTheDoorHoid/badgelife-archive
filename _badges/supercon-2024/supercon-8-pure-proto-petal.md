---
title: Pure Proto Petal
id: supercon-2024-supercon-8-pure-proto-petal
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
summary: A plain prototyping SAO for the Supercon 8 badge that breaks out all SAO lines, with power and ground along the sides and I2C and GPIO solder points in the middle.
functions: No built-in function; a blank breakout board for building your own SAO circuit.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - kit
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - i2c
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
  hardware_url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/pure_proto_petal
  firmware_url: null
  eda_tool: null
  gerbers_url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/pure_proto_petal/Expansion_Gerbers_PnP
  notes: Design files include a CSPcbDoc board file, a PDF/PS schematic (Expansion.pdf), and Gerbers/pick-and-place for fabrication.
links:
- label: github.com/astuder/2024-Supercon-8-Add-On-Badge
  url: https://github.com/astuder/2024-Supercon-8-Add-On-Badge
  kind: repo
- label: github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/pure_proto_petal
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/pure_proto_petal
  kind: repo
images: []
contact: {}
notes:
- The badge's own documentation calls its SAO ports "petals" (the badge is "a simple hub for six SAOs"); other official petals in the same repo include an LED petal, a touchwheel petal, and an I2C Proto Petal built around a CH32V003 microcontroller. The Pure Proto Petal is the fully passive version of that idea, with no MCU of its own.
status: listed
sources:
- kind: url
  url: https://github.com/astuder/2024-Supercon-8-Add-On-Badge
  title: 2024 Supercon 8 -- Supercon Add-On Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge/tree/main/hardware/sao/pure_proto_petal
  title: hardware/sao/pure_proto_petal at main -- Hack-a-Day/2024-Supercon-8-Add-On-Badge
  accessed: '2026-09-07'
  note: Confirmed description ("a simple breakout board for all of the SAO lines"), power/ground along the sides, I2C and GPIO solder points in the middle, and listed design files (CSPcbDoc, PDF schematic, Gerbers/PnP). No photo of an assembled board was present, only CAD/fab files.
- kind: url
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  title: Hack-a-Day/2024-Supercon-8-Add-On-Badge
  accessed: '2026-09-07'
  note: Confirmed the Supercon 8 (2024) badge is a MicroPython-based hub for six SAO "petals," and that the Pure Proto Petal is one of several official petals alongside an LED petal, a touchwheel petal, and an I2C Proto Petal (CH32V003-based).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Confirmed via the maker's own GitHub repos (Hack-a-Day org and astuder fork). No storefront, price, quantity, or availability information found -- the petal appears to have been a badge-hacking add-on rather than a sold item, but no source states this explicitly. No assembled-board photo was found in the repo, so no images could be saved; only CAD/schematic/Gerber files exist there.
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2024/supercon-8-pure-proto-petal.glb
  method: gerber
  source_file: hardware/sao/pure_proto_petal/Expansion_Gerbers_PnP/Gerber
  generated: '2026-09-10'
  bytes: 243488
  size_mm:
  - 41.0
  - 55.4
---

The Pure Proto Petal is a bare prototyping add-on for the Hackaday Supercon 8 (2024) badge, published in Hackaday's official GitHub repository for that year's badge alongside the badge's other "petals" (the badge's term for its six SAO ports). Where the badge's other official petals -- an LED petal, a touchwheel petal, and an I2C Proto Petal built around a CH32V003 microcontroller -- each carry their own active circuitry, the Pure Proto Petal is deliberately passive: it breaks out power and ground along its edges and brings I2C and GPIO lines to solder points in the middle, leaving the rest of the board open for whatever the builder wants to add.

Design files (a CSPcbDoc board file, a PDF/PostScript schematic, and Gerbers with pick-and-place data) are published in the `hardware/sao/pure_proto_petal` folder of the `Hack-a-Day/2024-Supercon-8-Add-On-Badge` repository, making it straightforward to fabricate. No information on pricing, quantities made, or how (or whether) it was distributed at Supercon 8 turned up in the sources checked; it reads as a reference design for badge hackers rather than a give-away or sold item, but that is an inference, not something a source states outright.

## Make your own

The hardware folder contains everything needed to fabricate the board: a CSPcbDoc PCB file, an `Expansion.pdf` schematic, and a Gerbers/pick-and-place folder (`Expansion_Gerbers_PnP`) that can be sent directly to a PCB fabricator. No firmware is needed since the board has no MCU of its own.
