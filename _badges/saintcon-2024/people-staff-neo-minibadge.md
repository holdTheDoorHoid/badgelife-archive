---
title: People-Staff-Neo minibadge
id: saintcon-2024-people-staff-neo-minibadge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: unconfirmed
summary: A staff-series SAINTCON 2024 minibadge built around 80 individually addressable WS2812B LEDs driven by an ATtiny1614, part of the "People" line of staff minibadges.
functions: 'Drives an 80-LED WS2812B array from a single ATtiny1614 microcontroller; specific lighting patterns/modes are not documented in the available sources.'
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: ATtiny1614
  leds:
    count: 80
    type: WS2812B
    note: WS2812B_1010 package (addressable RGB), per the KiCad schematic.
  display: none
  connectivity: []
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
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/People-Staff-Neo
  firmware_url: null
  eda_tool: KiCad
  notes: KiCad schematic/PCB/Gerbers are published; no firmware source or BOM was found alongside them.
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/People-Staff-Neo
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/People-Staff-Neo
  kind: repo
images: []
contact: {}
notes:
- Staff 'Neo' themed people minibadge for SAINTCON 2024. Found by the event-year sweep, task saintcon-2024.
- Sweep title "People-Staff-Neo minibadge" is the repo folder name; no maker-published title was found, so it is kept as-is.
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/People-Staff-Neo
  title: People-Staff-Neo minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/People-Staff-Neo/People-Staff-Neo.kicad_sch
  title: People-Staff-Neo.kicad_sch (raw KiCad schematic)
  accessed: '2026-09-10'
  note: Confirms 80x WS2812B_1010 LEDs and one ATtiny1614-SS MCU on the board; no other active parts.
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024
  title: 'utahsaint-org/MiniBadges2024: Minibadges for SAINTCON 2024'
  accessed: '2026-09-10'
  note: Repo root README only says "Minibadges for SAINTCON 2024"; no per-badge descriptions, images, pricing, or distribution info anywhere in the repo.
- kind: url
  url: https://github.com/utahsaint-org/saintcon.zip.files/blob/main/2024/2024-SAINTCON-MiniBadge-Guide-v3.0-10.20.2024-1.pdf
  title: 2024 SAINTCON MiniBadge Guide v3.0
  accessed: '2026-09-10'
  note: 'Official 2024 minibadge build guide (40MB PDF, text-extracted and searched in full): contains no entry for "People-Staff-Neo", "Staff", or a matching NeoPixel/ATtiny1614 description, suggesting this staff badge was not part of the public trading-guide roster.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'The GitHub repo (utahsaint-org/MiniBadges2024, official SAINTCON minibadge-community org) confirms this is a real, designed PCB: KiCad schematic/PCB/Gerbers for an 80x WS2812B addressable-LED board driven by a single ATtiny1614-SS. No README, maker credit, photo, price, quantity, or distribution info exists anywhere in the repo or in the official 2024 MiniBadge Guide PDF (searched in full, no match). Could not confirm who designed it, whether it was actually built/distributed, or its physical form factor/shape/colors, so those fields are left empty. The "Staff" in the folder name and the absence from the public trading guide suggest it was made for SAINTCON staff specifically rather than general attendee trading, but no source states this directly.'
last_modified_date: '2026-09-10'
---


People-Staff-Neo is a minibadge design published in the official `MiniBadges2024` GitHub organization for SAINTCON 2024's community minibadge program. The board's schematic and PCB files show a single ATtiny1614-SS microcontroller driving 80 individually addressable WS2812B LEDs (1010 package), making it one of the more LED-dense entries in that year's minibadge lineup — likely the source of the "Neo" (NeoPixel) part of its name, paired with "Staff" suggesting it belonged to a "People" series of minibadges tied to specific con roles or individuals.

No README, build guide, storefront listing, or photo of the finished board could be found. The badge does not appear in the official 2024 SAINTCON MiniBadge Guide PDF, which documents the badges available to the general trading community that year — consistent with this being a staff-specific piece rather than one released for public trading, though no source confirms that directly. Design files (KiCad schematic, PCB, and Gerbers) are published in the repo and appear to be open, but no explicit license is stated.

## Make your own

The repo (linked above) contains the full KiCad project — schematic, PCB layout, and generated Gerbers/drill files under `People-Staff-Neo/`. Anyone with the design files could fabricate the board and populate an ATtiny1614-SS plus 80 WS2812B_1010 LEDs, though no firmware source or bill of materials was found alongside the hardware files.
