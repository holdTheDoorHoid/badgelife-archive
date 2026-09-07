---
title: BSides20016Badge (STM32F0/Cortex-M0, LED matrix)
id: bsidespr-2016-bsides20016badge-stm32f0-cortex-m0-led-matrix
layout: badge
parent: BSidespr 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsidespr-2016
year: 2016
makers:
- name: soynerdito
  url: https://github.com/soynerdito
summary: An 8x8 LED matrix conference badge built around an STM32F0 (Cortex-M0) MCU, designed and documented in the open by soynerdito for BSidesPR 2016.
functions: Drives a programmable 8x8 LED matrix (via two shift registers, controllable as SPI or bit-banged GPIO on pins PA7/PA5); doubles as a USB device for programming/serial communication.
look:
  colors: []
  shape: rectangle
  themes:
  - security
  - hardware tool
tech:
  mcu: STM32F0
  leds:
    count: 64
    type: discrete
    note: 8x8 LED matrix driven through two shift registers
  display: LED matrix 8x8
  connectivity:
  - usb
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/soynerdito/BSides20016Badge
  firmware_url: https://github.com/soynerdito/BSides20016Badge
  eda_tool: Eagle
  notes: Repo contains multiple board variants (BADGE_LED_MATRIX_STM, plus MicroUSB and PL2303HX alternates), Eagle schematic/board files (.sch/.brd), and an ATtiny85 variant and a CH340G USB-serial sub-project. Firmware was developed with STM32CubeMX-generated project files built in Keil (Windows); the maker notes Linux tooling (System Workbench for STM32) was untested at time of writing.
links:
- label: github.com/soynerdito/BSides20016Badge
  url: https://github.com/soynerdito/BSides20016Badge
  kind: repo
- label: 'Soynerdito''s Blog: BSidesPR 2016 Badge programming tools'
  url: https://blog.soynerdito.com/2016/02/bsidespr-2016-badge-programming-tools.html
  kind: article
- label: 'element14 Community: Conference Badge with a STM32F0'
  url: https://community.element14.com/members-area/personalblogs/b/blog/posts/conference-badge-with-a-stm32f0
  kind: article
images:
- file: assets/images/badges/bsidespr-2016/bsides20016badge-stm32f0-cortex-m0-led-matrix/de4ca4be0f.jpg
  source: https://github.com/soynerdito/BSides20016Badge
  credit: soynerdito
  caption: PCB render of the BSidesPR 2016 badge with the 8x8 LED matrix
- file: assets/images/badges/bsidespr-2016/bsides20016badge-stm32f0-cortex-m0-led-matrix/683d39182e.png
  source: https://github.com/soynerdito/BSides20016Badge
  credit: soynerdito
  caption: Board diagnostic photo of the assembled badge
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- Sheet/repo title reads "BSides20016Badge" (likely a typo for "BSides2016Badge"); kept as the maker's repo name for title but the underlying event is BSidesPR (BSides Puerto Rico) 2016, confirmed by the maker's own blog post title.
- Price, quantity made, and distribution/availability were not stated in any source found.
status: released
sources:
- kind: url
  url: https://github.com/soynerdito/BSides20016Badge
  title: BSides20016Badge (STM32F0/Cortex-M0, LED matrix)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''BSidesPR 2016''.'
- kind: url
  url: https://blog.soynerdito.com/2016/02/bsidespr-2016-badge-programming-tools.html
  title: 'Soynerdito''s Blog: BSidesPR 2016 Badge programming tools'
  accessed: '2026-09-07'
  note: Confirms event (BSidesPR 2016), MCU (STM32F0/Cortex-M0), LED matrix drive pins (PA7/PA5, SPI or GPIO), and toolchain (STM32CubeMX, Keil).
- kind: url
  url: https://community.element14.com/members-area/personalblogs/b/blog/posts/conference-badge-with-a-stm32f0
  title: Conference Badge with a STM32F0 - element14 Community
  accessed: '2026-09-07'
  note: Cross-posted maker writeup; confirms STM32F030F4P6 chip, CH340G USB-serial, two shift registers, and 8x8 LED matrix; describes micro-USB and male USB connector variants on the board.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's GitHub repo and two of the maker's own blog posts (soynerdito's Blog and a cross-post on element14 Community) confirm the badge, its event (BSidesPR 2016), chip, and LED matrix design. No source found states price, quantity made, or how it was distributed at the con, so those fields are left empty. The repo has no top-level README describing the boards; details on the specific board variant (MicroUSB vs MicroUSBALT vs PL2303HX) came from folder names and the blog posts, not a single canonical writeup.
last_modified_date: '2026-09-07'
model:
  file: assets/models/bsidespr-2016/bsides20016badge-stm32f0-cortex-m0-led-matrix.glb
  method: kicad
  source_file: Attiny85VUSB.brd
  generated: '2026-09-07'
  bytes: 121216
---

The BSides20016Badge is an open-hardware conference badge that soynerdito designed and documented for BSidesPR (BSides Puerto Rico) 2016. It centers on an STM32F0-family microcontroller (an STM32F030F4P6, using the Arm Cortex-M0 core) driving an 8x8 LED matrix through two shift registers, with the matrix controllable either as SPI output or as plain bit-banged GPIO on pins PA7 and PA5. The board includes a USB connector for programming and serial communication, and the maker's blog documents building firmware with STM32CubeMX-generated project files compiled in Keil on Windows, noting that Linux alternatives such as System Workbench for STM32 were untested at the time of writing.

The GitHub repository holds several board variants beyond the core LED-matrix design: alternates with a micro-USB connector and with a PL2303HX USB-serial chip, a separate ATtiny85-based project, and a standalone CH340G USB-serial sub-project, all published as Eagle schematic and board files. No pricing, production quantity, or distribution details for the badge were found in the maker's repo or blog posts.

## Make your own

The hardware is fully open: schematic (.sch) and board (.brd) files for each variant are in the GitHub repository (github.com/soynerdito/BSides20016Badge), drawn in Eagle. Firmware was generated with STM32CubeMX and built as a Keil project; the maker's blog post on badge programming tools walks through the toolchain setup.
