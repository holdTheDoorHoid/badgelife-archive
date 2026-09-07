---
title: BADGE FOR SUPERCON.6 / November 2022
id: supercon-2022-badge-for-supercon-6-november-2022
layout: badge
parent: Supercon 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2022
year: 2022
makers:
- name: Voja Antonic
  url: https://hackaday.io/voja-antonic
  role: designer
- name: drwass3
  role: collaborator
- name: hwang_hoyoen
  role: collaborator
- name: Nesib Fiso
  role: collaborator
summary: A conference badge that simulates a complete 4-bit computer in hardware, showing its internal registers, flags, and program counter live on 272 LEDs.
functions: 'Simulates a 4-bit CPU with 31 instructions and adjustable clock speed (0.5 to 250,000 instructions/second). Has 4,096 words (12-bit) of program memory, 256 nibbles of data memory, and a 5-deep subroutine stack. Programs can be entered directly via buttons, written in an included 2-pass assembler, or loaded/saved over serial. A 3x16 LED disassembler display shows opcodes and operands as the simulated CPU runs.'
look:
  colors: []
  shape: rectangle
  themes:
  - retro computer
  - learn to solder
  - hardware tool
tech:
  mcu: PIC24FJ256GA704
  leds:
    count: 272
    type: discrete
    note: LEDs display CPU registers, flags, ALU status, stack pointer, data memory pages, and program counter in binary, plus a 3x16 LED disassembler readout.
  display: none
  connectivity:
  - uart
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of Hackaday Supercon 6 (November 2022); some later changed hands via Tindie.
make_your_own:
  open_source: yes
  hardware_url: https://hackaday.io/project/182568-badge-for-supercon6-november-2022
  firmware_url: https://hackaday.io/project/182568-badge-for-supercon6-november-2022
  eda_tool: null
links:
- label: hackaday.io/project/182568-badge-for-supercon6-november-2022
  url: https://hackaday.io/project/182568-badge-for-supercon6-november-2022
  kind: hackaday
- label: 'GitHub: adrianfreed/Supercon6BadgeWork (community assembler/tooling)'
  url: https://github.com/adrianfreed/Supercon6BadgeWork
  kind: repo
- label: 'Related project: BadgeIO DAC/ADC/SigGen/Buffers expansion board for the badge'
  url: https://hackaday.io/project/188326-badgeio-dacadcsiggenbuffers-for-supercon6
  kind: hackaday
- label: Demo video on YouTube
  url: https://youtu.be/ix__enrtYF4
  kind: video
images:
- file: assets/images/badges/supercon-2022/badge-for-supercon-6-november-2022/6163a07bc9.jpg
  source: "https://hackaday.io/project/182568-badge-for-supercon6-november-2022"
  credit: "Voja Antonic"
  caption: "The Supercon.6 badge showing its LED array simulating a 4-bit CPU"
contact: {}
notes:
- 4-bit CPU simulated by 16-bit MCU with 272 LEDs display.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/182568-badge-for-supercon6-november-2022
  title: BADGE FOR SUPERCON.6 / November 2022
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''Supercon 6 2022''.'
- kind: url
  url: https://hackaday.io/project/182568-badge-for-supercon6-november-2022
  title: BADGE FOR SUPERCON.6 / November 2022 (Hackaday.io project page)
  accessed: '2026-09-07'
  note: 'Primary source: maker (Voja Antonic), team, function, specs, MCU, LED count, open-source files, distribution as a Supercon 6 conference giveaway, and related links.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Core facts confirmed on the maker''s own Hackaday.io project page. Exact production quantity and any resale price were not stated on the page (one commenter mentioned DIY parts running roughly $120, which is not an official price and was not recorded as such). An updated version of the badge was reportedly made for a Berlin 2023 event; not covered by this entry, which covers the original Supercon 6 (November 2022) badge. A related expansion board (BadgeIO, for DAC/ADC/sig-gen) exists as a separate Hackaday.io project and could merit its own entry.'
last_modified_date: '2026-09-07'
---

The Supercon.6 badge, designed by Voja Antonic with contributions from drwass3, hwang_hoyoen, and Nesib Fiso, was given to attendees of Hackaday's Supercon 6 conference in November 2022. Rather than a screen or a game, the badge's centerpiece is a simulated 4-bit computer built entirely from discrete LEDs: 272 of them light up to show the machine's registers, flags, arithmetic status, stack pointer, and program counter in binary as it runs, with a 3x16 LED readout disassembling the running program's opcodes and operands in real time.

Underneath the simulation sits a PIC24FJ256GA704 microcontroller, chosen for its large flash to hold both the badge's firmware and the simulated CPU's own program memory (4,096 twelve-bit words, plus 256 nibbles of data memory and a 5-deep subroutine stack). Attendees could program the simulated CPU three ways: entering instructions directly on the badge's buttons, writing assembly with the included two-pass assembler, or loading and saving programs over a serial connection. The design was released fully open, with schematics, BOM, and firmware published on the project's Hackaday.io page, and community members such as Adrian Freed built additional tooling (an assembler and code synthesizer) around it afterward. A companion expansion board, BadgeIO, was later designed to add DAC/ADC and signal-generator capability to the badge.

## Make your own

The hardware design, bill of materials, and firmware source (for MPLAB X) are published on the project's Hackaday.io page at https://hackaday.io/project/182568-badge-for-supercon6-november-2022, along with an instruction-set reference and user manual. A community-built assembler and related tooling are available at https://github.com/adrianfreed/Supercon6BadgeWork.
