---
title: DEFCON Furs Badge DC28 (Boop Blocker)
id: dc28-defcon-furs-badge-dc28
layout: badge
parent: DC28
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc28
year: 2020
makers:
- name: DEFCON Furs (defconfurs)
  url: https://dcfurs.com/
summary: 'A wearable mask badge with a 20x14 RGB matrix, made by the DEFCON Furs community for the 2020 (virtual) DEF CON in honor of the in-person event being cancelled.'
functions: 'Voice-reactive LED animations via an onboard MEMS microphone; ships with several built-in animation programs (rainbow, matrix, lineface, DJ mode, etc.) and supports custom RISC-V animation programs loaded over USB DFU.'
look:
  colors: [black, multicolor]
  shape: mask
  themes: [wearable, mascot, radio]
tech:
  mcu: 'Lattice iCE40 UltraPlus FPGA (RISC-V soft core)'
  leds:
    count: 280
    type: RGB
    note: '20x14 RGB matrix'
  display: 'LED matrix 20x14'
  connectivity: [usb, audio]
  battery: 'USB (micro-USB powered, no battery)'
  sao_version: null
get_one:
  price: '$120 donation'
  price_usd: 120
  quantity: ''
  availability: sold_out
  distribution: [purchase, free_drop, raffle]
  where: 'Sold as a $120 donation gift (with free worldwide shipping) through donate.dcfurs.com; a limited number were also given away via a Twitter retweet raffle.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/defconfurs/dc28-fur-fpga
  eda_tool: null
  notes: 'Animation/bootloader source (this repo) and FPGA gateware source (dc28-fur-fpga) are public; no PCB/hardware design files were found.'
links:
- label: github.com/defconfurs/dcfurs-badge-dc28
  url: https://github.com/defconfurs/dcfurs-badge-dc28
  kind: repo
- label: github.com/defconfurs/dc28-fur-fpga
  url: https://github.com/defconfurs/dc28-fur-fpga
  kind: repo
- label: dcfurs.com
  url: https://dcfurs.com/
  kind: website
- label: 'DEFCON Furs Announcements (Telegram)'
  url: https://t.me/s/defconfursnews?before=212
  kind: social
images:
  - file: assets/images/badges/dc28/defcon-furs-badge-dc28/1f1fc4bfaf.jpg
    source: "https://github.com/defconfurs/dcfurs-badge-dc28"
    credit: "DEFCON Furs"
    caption: "Front render of the 2020 DEFCON Furs mask badge"
contact: {}
notes:
- A wearable PPE-mounted mask badge with a 20x14 RGB matrix driven by a Lattice iCE40 UltraPlus FPGA, MEMS mic for audio reactivity, and USB DFU programmability, made by the DEFCON Furs community for DC28. Found by the event-year sweep, task dc28-badges.
- 'The sweep''s title omitted the maker''s own name for the badge; DEFCON Furs called it the "Boop Blocker" in their 2020 announcements.'
status: released
sources:
- kind: url
  url: https://github.com/defconfurs/dcfurs-badge-dc28
  title: DEFCON Furs Badge DC28
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc28-badges); event read as ''dc28''.'
- kind: url
  url: https://github.com/defconfurs/dc28-fur-fpga
  title: defconfurs/dc28-fur-fpga
  accessed: '2026-09-08'
  note: 'Linked from the main repo README as the source for the FPGA gateware and bootloader.'
- kind: url
  url: https://t.me/s/defconfursnews?before=212
  title: 'DEFCON Furs Announcements (Telegram channel)'
  accessed: '2026-09-08'
  note: 'Maker''s own announcement channel: names the badge "Boop Blocker", gives the $120 donation price, free shipping, and the Twitter retweet raffle for a free unit.'
- kind: url
  url: https://dcfurs.com/
  title: DEFCON Furs
  accessed: '2026-09-08'
  note: 'Organization background page; confirms DEFCON Furs is a project of the 501(c)(3) Hack Your Lives.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core specs and distribution confirmed via the maker''s own GitHub README and Telegram announcements. Quantity made was not stated anywhere found. No PCB/hardware design files (Gerbers, schematics) were located, only firmware/gateware source, so open_source is marked partial. Exact close date of the donation raffle (mentioned as September 13, 2020) noted for context but not otherwise fielded.'
last_modified_date: '2026-09-08'
---

The 2020 DEFCON Furs badge, nicknamed the "Boop Blocker," was made in honor of that year's DEF CON going virtual. Rather than a traditional PCB badge, it takes the form of a flexible mask meant to be worn over a face covering, built around a Lattice iCE40 UltraPlus FPGA running a RISC-V soft core. A 20x14 RGB LED matrix and an onboard MEMS microphone let it react to ambient sound and voice, and its firmware, bootloader, and animation programs can all be reprogrammed over USB DFU without special tools.

DEFCON Furs distributed the badge as a $120 donation gift through their own donation site, with free worldwide shipping, and separately gave away a limited number of units through a retweet-to-win raffle on Twitter that closed in mid-September 2020. Fulfillment updates to donors continued into late November 2020, suggesting badges were hand-assembled and shipped in batches after the con.

The animation firmware and FPGA gateware are both published on GitHub, and the badge supports user-written animations compiled from C using a provided RISC-V toolchain and `make.py` build script, making it one of the more hackable badges the group has released.

## Make your own

1. Install a RISC-V cross compiler (`gcc-riscv64-unknown-elf` on Ubuntu 20.04+, or a prebuilt SiFive toolchain elsewhere) and `dfu-util`.
2. Clone [dcfurs-badge-dc28](https://github.com/defconfurs/dcfurs-badge-dc28) and write a new animation as a small RISC-V C program (a "Hello World" example is included in the README).
3. Add the animation's name to the `animations` list near the top of `make.py`, then run `./make.py build` to compile and bundle it into a flash image.
4. Connect the badge over micro-USB and run `./make.py upload` to reflash it via USB DFU.
5. FPGA gateware and bootloader source, for anyone wanting to modify the hardware logic itself, is in the companion [dc28-fur-fpga](https://github.com/defconfurs/dc28-fur-fpga) repository.
