---
title: DEFCON Furs 2024 Badge
id: dc32-an-electronic-badge-is-in-the-works
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: DEFCON Furs
  url: https://dcfurs.com
summary: A Mad Max-themed electronic badge with a LoRa radio, 48 RGB LEDs, and two SAO ports, doubling as entry to the DEFCON Furs suite at DEF CON 32.
functions: LoRa wireless radio, 48 addressable RGB LEDs with animations, capacitive touch points ("booping"), MicroPython scripting, and two Shitty Add-On (v1.69bis) ports.
look:
  colors: [black, purple]
  shape: fox head
  themes: [animal, radio, wearable]
tech:
  mcu: RP2040 + STM32WL
  leds:
    count: 48
    type: RGB
    note: Addressable RGB LEDs driven by the RP2040; animations included in stock firmware.
  display: none
  connectivity: [lora]
  inputs: [touch]
  battery: null
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: $130 donation (assembled) / less for PCB blank
  price_usd: 130.0
  quantity: limited run; exact number not published
  availability: sold_out
  availability_note: 'Gumroad listing marked sold out as of 2026-09-06 check; remaining assembled units were sold in person at DEF CON 32 for a $150 minimum donation.'
  distribution: [purchase, preorder]
  where: Preorders via Gumroad (defconfurs.gumroad.com), with pickup or remaining stock sold in person at the DEFCON Furs suite, Fontainebleau Las Vegas, during DEF CON 32.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/defconfurs/dcfurs-badge-dc32
  firmware_url: https://github.com/defconfurs/dcfurs-badge-dc32
  gerbers_url: null
  bom_url: https://docs.google.com/spreadsheets/d/1Jkg6oq2OzCKG4kRN5Ynu_qSia2YDe5dJ_6Gyr4F5ahs/edit?usp=sharing
  eda_tool: KiCad
  license: null
  fab_url: null
  notes: 'Maker policy publishes only the schematic PDF, board render images, and BoM; full KiCad source files (minus the board) and JTAG wiring notes for the STM32WL are explicitly not released.'
links:
- label: donate.defconfurs.org
  url: https://donate.defconfurs.org
  kind: website
- label: dcfurs.com
  url: https://dcfurs.com
  kind: website
- label: GitHub - dcfurs-badge-dc32
  url: https://github.com/defconfurs/dcfurs-badge-dc32
  kind: repo
- label: Gumroad - 2024 Badge (Fully Assembled + Suite Access)
  url: https://defconfurs.gumroad.com/l/2024-badge
  kind: store
- label: Gumroad - 2024 Badge (PCB Blank)
  url: https://donate.defconfurs.org/l/DEFCONFurs2024Badge-PCBBlank
  kind: store
- label: Bill of Materials (Google Sheets)
  url: https://docs.google.com/spreadsheets/d/1Jkg6oq2OzCKG4kRN5Ynu_qSia2YDe5dJ_6Gyr4F5ahs/edit?usp=sharing
  kind: doc
images:
  - file: assets/images/badges/dc32/an-electronic-badge-is-in-the-works/db315c4bb1.png
    source: "https://defconfurs.gumroad.com/l/2024-badge"
    credit: "DEFCON Furs"
    caption: "DEFCON Furs 2024 badge, fully assembled"
  - file: assets/images/badges/dc32/an-electronic-badge-is-in-the-works/dbabb9cb2b.jpg
    source: "https://github.com/defconfurs/dcfurs-badge-dc32"
    credit: "DEFCON Furs / Kyle \"Kay\" Fox"
    caption: "Prototype (R1) board render, front"
contact: {}
notes:
- There is a version with the pcb and not assembled. You may be able to get the pcb and assemble it yourself. I do not know but it sounds challenging (especially at my age)
- 'Sheet listed this row only as "An electronic badge is in the works"; the maker''s actual product name is "DEFCON Furs 2024 Badge."'
status: released
sources:
- kind: sheet
  event: dc32
  row: 52
  updated: '2024-07-17'
- kind: url
  url: https://github.com/defconfurs/dcfurs-badge-dc32
  title: 'GitHub - defconfurs/dcfurs-badge-dc32: 2024 DEFCON Furs Badge Repo'
  accessed: '2026-09-06'
  note: MCU (RP2040 main + STM32WL radio), firmware/MicroPython, open-source policy, KiCad, BoM/schematic links, credits.
- kind: url
  url: https://defconfurs.gumroad.com/l/2024-badge
  title: DEFCON Furs 2024 Badge - Fully Assembled + Suite Access
  accessed: '2026-09-06'
  note: Price ($130 donation), sold-out status, LoRa radio, 48 RGB LEDs, RP2040, MicroPython, touch/booping, 2x SAO v1.69bis, suite-access bundling, image.
- kind: url
  url: https://donate.defconfurs.org/l/DEFCONFurs2024Badge-PCBBlank
  title: DEFCON Furs 2024 Badge - PCB Blank
  accessed: '2026-09-06'
  note: Confirms a separate unassembled PCB-blank version existed, matching the sheet's note.
- kind: url
  url: https://dcfurs.com
  title: DEFCON Furs
  accessed: '2026-09-06'
  note: Maker's main site; no DC32-specific badge detail found here.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Renamed from the sheet''s placeholder title to the maker''s actual product name, "DEFCON Furs 2024 Badge," per the special-case rule (all core facts came from the maker''s own GitHub repo and Gumroad listing). Exact production quantity is not published anywhere found. License for the hardware/firmware was not stated. The maker deliberately withholds full KiCad source and STM32WL JTAG wiring details, so make_your_own is partial rather than yes. Board shape is a fox/canine head per the repo''s R1 prototype render (purple soldermask); per the repo readme, public-sale and staff PCBs were black rather than the purple prototype, so both colors are listed.'
last_modified_date: '2026-09-06'
---

The DEFCON Furs 2024 Badge was the group's Mad Max: Fury Road-themed hardware badge for DEF CON 32, sold as a fundraiser that doubled as entry to the DEFCON Furs suite at the Fontainebleau in Las Vegas. It runs on an RP2040 paired with an STM32WL radio co-processor for LoRa, drives 48 addressable RGB LEDs, and adds capacitive touch points that bring back the badge line's running "booping" gag. Two SAO (v1.69bis) ports let it host add-ons from other makers. Firmware is MicroPython-based and was deliberately shipped incomplete, with the team publishing the software repo close to the con and inviting attendees to finish features (USB filesystem access, radio AT-command handling, new animations) themselves, with informal prizes offered for things like getting Meshtastic running on the STM32WL.

It was sold two ways: a fully assembled badge with lanyard and suite access, and a bare "PCB Blank" for people who wanted to source parts and assemble it themselves, matching the community sheet's note about an unassembled option. Preorders ran through Gumroad ahead of the con for a $130 minimum donation, with remaining assembled stock sold in person for $150; the Gumroad listing was marked sold out at last check. Boards were manufactured by PCBWay and assembled by PCBx.io in Ohio for the public/staff run, following earlier OSH Park/hand-assembled prototypes.

As a matter of policy, DEFCON Furs publishes only the schematic PDF, board-render images, and bill of materials for its badges rather than full manufacturing files — the GitHub repo explicitly notes that complete KiCad source (minus the board) and JTAG wiring information for the STM32WL are not included, so this entry treats the project as partially open source.
