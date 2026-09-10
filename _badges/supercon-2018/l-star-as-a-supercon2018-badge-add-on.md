---
title: L-Star as a SuperCon2018 Badge Add-On
id: supercon-2018-l-star-as-a-supercon2018-badge-add-on
layout: badge
parent: Supercon 2018
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2018
year: 2018
makers:
- name: Jac Goudsmit
  url: https://github.com/JacGoudsmit
summary: A homebrew expansion board that turns the 2018 Supercon badge into a working 6502/Apple-1-style computer, running Woz Mon, Integer BASIC, and Krusader.
functions: 'Emulates a 6502-based Apple-1 computer: boots into the Woz Mon monitor and can run Integer BASIC and the Krusader assembler/monitor. Connects over serial to a PC (via a Prop Plug) and to the Supercon badge itself.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
tech:
  mcu: Parallax Propeller (paired with a Western Design Center W65C02S)
  leds: null
  display: none (black-and-white NTSC/PAL video via 1-pin TV driver on the L-Star Plus variant, or terminal emulation over serial)
  connectivity:
  - uart
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: Handmade by the maker for Supercon 2018; not sold commercially.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/JacGoudsmit/L-Star
  firmware_url: https://github.com/JacGoudsmit/L-Star
  eda_tool: KiCad
links:
- label: hackaday.io/project/3620-l-star-software-defined-6502-computer/log/155608-l-star-as-a-supercon2018-badge-add-on
  url: https://hackaday.io/project/3620-l-star-software-defined-6502-computer/log/155608-l-star-as-a-supercon2018-badge-add-on
  kind: hackaday
- label: 'GitHub: JacGoudsmit/L-Star'
  url: https://github.com/JacGoudsmit/L-Star
  kind: repo
images:
- file: assets/images/badges/supercon-2018/l-star-as-a-supercon2018-badge-add-on/0eef1975c8.jpg
  source: https://hackaday.io/project/3620-l-star-software-defined-6502-computer/log/155608-l-star-as-a-supercon2018-badge-add-on
  credit: Jac Goudsmit
  caption: Assembled L-Star badge add-on board
- file: assets/images/badges/supercon-2018/l-star-as-a-supercon2018-badge-add-on/c1203ed38b.jpg
  source: https://hackaday.io/project/3620-l-star-software-defined-6502-computer/log/155608-l-star-as-a-supercon2018-badge-add-on
  credit: Jac Goudsmit
  caption: L-Star board connected to the Supercon 2018 badge
contact: {}
notes:
- 'The event-year sweep found this via the search snippet, which read: "An expansion board add-on turning the 2018 Supercon badge into a working 6502/Apple-1-style computer running Woz Mon and Integer BASIC." That description is confirmed by the maker''s own Hackaday.io log and GitHub repo.'
status: released
sources:
- kind: url
  url: https://hackaday.io/project/3620-l-star-software-defined-6502-computer/log/155608-l-star-as-a-supercon2018-badge-add-on
  title: L-Star as a SuperCon2018 Badge Add-On
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2018); event read as ''supercon-2018''.'
- kind: url
  url: https://github.com/JacGoudsmit/L-Star
  title: 'GitHub: JacGoudsmit/L-Star'
  accessed: '2026-09-08'
  note: Confirmed open-source hardware/firmware, KiCad EDA tool, MIT license, chip and connectivity details.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Core facts (maker, event, function, open-source status) confirmed by the maker's own Hackaday.io project log and GitHub repository. Price, quantity made, and LED info were not stated anywhere and are left empty. The board is an ad-hoc badge add-on rather than a standard 4/6-pin SAO, so tech.sao_version is set to none.
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2018/l-star-as-a-supercon2018-badge-add-on.glb
  method: kicad
  source_file: Hardware/Kicad/L-StarPlus/L-Star.kicad_pcb
  generated: '2026-09-10'
  bytes: 739448
---

The L-Star is a homebrew expansion board built by Jac Goudsmit as an add-on for the 2018 Supercon badge, turning it into a working software-defined 6502 computer in the spirit of the original Apple-1. A Parallax Propeller microcontroller emulates the timing and I/O of a Western Design Center W65C02S 6502 processor, with 20KB of RAM available to the emulated machine and a 64KB EEPROM holding the Propeller firmware and ROM images. On boot it drops into the classic Woz Mon monitor, and from there can load Steve Wozniak's Integer BASIC or the Krusader assembler/monitor, all running on real vintage software rather than a modern reimplementation.

The board connects to a PC over serial at 115,200 bps (via a Prop Plug) for programming and console access, and separately to the Supercon badge itself at 19,200 bps. A related variant, the "L-Star Plus," adds an optional 128KB SRAM chip, NTSC/PAL composite video output, and an onboard power supply. Goudsmit built the boards by hand for the conference; they were not sold or mass-produced.

Hardware and firmware are both open source, published on GitHub under the MIT license, with the PCB designed in KiCad and documented alongside build instructions and parts sourced from Mouser.

## Make your own

The GitHub repository (https://github.com/JacGoudsmit/L-Star) contains Hardware, Software, and Documentation folders with the KiCad PCB design files, firmware source, and a bill of materials sourced from Mouser (including the W65C02S and Propeller chips). Follow the repo's documentation for assembly and programming steps.
