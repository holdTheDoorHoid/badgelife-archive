---
title: Hackaday Superconference Badge 2019 (FPGA Game Boy)
id: supercon-2019-hackaday-superconference-badge-2019-fpga-game-boy
layout: badge
parent: Supercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2019
year: 2019
makers:
- name: Jeroen "Sprite_TM" Domburg
  url: https://github.com/Spritetm
summary: A Game Boy-shaped conference badge built around a large Lattice ECP5 FPGA instead of a fixed-function MCU, given to every 2019 Hackaday Superconference attendee.
functions: Runs a soft RISC-V core and custom FPGA gateware; ships with a built-in Tetris clone, plays sound through a SID-inspired synthesizer, and supports loading custom software or gateware over USB or JTAG. A cartridge slot lets attendees plug in their own hardware (one attendee added a camera during the con).
look:
  colors: []
  shape: null
  themes:
  - console
  - retro computer
  - hardware tool
tech:
  mcu: Lattice LFE5U-45F ECP5 FPGA (soft RISC-V core, ~45,000 LUTs)
  leds: null
  display: 480x320 color LCD
  connectivity:
  - usb
  - ir
  battery: 2x AA
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: 500+
  availability: free
  distribution:
  - free_drop
  where: Handed out to attendees who bought tickets to the 2019 Hackaday Superconference (Pasadena, CA); tickets sold out and the badge was not sold separately.
make_your_own:
  open_source: true
  hardware_url: https://github.com/Spritetm/hadbadge2019_pcb
  firmware_url: https://github.com/Spritetm/hadbadge2019_fpgasoc
  eda_tool: KiCad
  license: CC-BY-SA 3.0
  notes: Firmware/gateware toolchain is fully open source (Yosys, nextpnr-ecp5); hardware repo confirmed CC-BY-SA 3.0 licensed KiCad files.
links:
- label: hackaday.com/2019/11/04/gigantic-fpga-in-a-game-boy-form-factor-2019-supercon-badge-is-a-hardware-siren-song
  url: https://hackaday.com/2019/11/04/gigantic-fpga-in-a-game-boy-form-factor-2019-supercon-badge-is-a-hardware-siren-song/
  kind: article
- label: hackaday.com/2019/11/16/behind-the-scenes-of-the-2019-superconference-badge
  url: https://hackaday.com/2019/11/16/behind-the-scenes-of-the-2019-superconference-badge/
  kind: article
  archived: https://web.archive.org/web/20260518190546/https://hackaday.com/2019/11/16/behind-the-scenes-of-the-2019-superconference-badge/
- label: hadbadge2019_fpgasoc (firmware/gateware repo)
  url: https://github.com/Spritetm/hadbadge2019_fpgasoc
  kind: repo
  archived: https://web.archive.org/web/20260719194838/https://github.com/Spritetm/hadbadge2019_fpgasoc
- label: hadbadge2019_pcb (hardware repo)
  url: https://github.com/Spritetm/hadbadge2019_pcb
  kind: repo
images:
- file: assets/images/badges/supercon-2019/hackaday-superconference-badge-2019-fpga-game-boy/a9cbc5df58.jpg
  source: https://hackaday.com/2019/11/04/gigantic-fpga-in-a-game-boy-form-factor-2019-supercon-badge-is-a-hardware-siren-song/
  credit: Hackaday
  caption: Front of the 2019 Supercon FPGA badge, Game Boy form factor
- file: assets/images/badges/supercon-2019/hackaday-superconference-badge-2019-fpga-game-boy/e68b9e5257.jpg
  source: https://hackaday.com/2019/11/04/gigantic-fpga-in-a-game-boy-form-factor-2019-supercon-badge-is-a-hardware-siren-song/
  credit: Hackaday
  caption: Rear of the 2019 Supercon FPGA badge showing cartridge slot
contact: {}
notes:
- Nearly a year in development; per Hackaday's behind-the-scenes piece, work continued until under 24 hours before distribution, and about 95% of the 500+ boards passed QC in time for the con.
status: released
sources:
- kind: url
  url: https://hackaday.com/2019/11/04/gigantic-fpga-in-a-game-boy-form-factor-2019-supercon-badge-is-a-hardware-siren-song/
  title: Hackaday Superconference Badge 2019 (FPGA Game Boy)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: official-badges); event read as ''Hackaday Superconference 2019''.'
- kind: url
  url: https://hackaday.com/2019/11/16/behind-the-scenes-of-the-2019-superconference-badge/
  title: Behind The Scenes Of The 2019 Superconference Badge
  accessed: '2026-09-07'
  note: Confirmed development timeline, Tetris clone, 2xAA power, ~500+ units manufactured with ~95% QC pass rate.
  archived: https://web.archive.org/web/20260518190546/https://hackaday.com/2019/11/16/behind-the-scenes-of-the-2019-superconference-badge/
- kind: url
  url: https://github.com/Spritetm/hadbadge2019_fpgasoc
  title: Spritetm/hadbadge2019_fpgasoc
  accessed: '2026-09-07'
  note: Firmware/gateware repository; confirmed Lattice ECP5 FPGA (LFE5U-45F), RISC-V soft core, 480x320 LCD, open-source toolchain.
  archived: https://web.archive.org/web/20260719194838/https://github.com/Spritetm/hadbadge2019_fpgasoc
- kind: url
  url: https://github.com/Spritetm/hadbadge2019_pcb
  title: Spritetm/hadbadge2019_pcb
  accessed: '2026-09-07'
  note: Hardware (PCB) repository; confirmed KiCad files and CC-BY-SA 3.0 license.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts (maker, FPGA, display, distribution, open-source repos) confirmed across two Hackaday articles and both of the maker's own GitHub repos. No price applies since it was a free con badge. LED count/type not mentioned in any source, left empty. sao_version not applicable (no SAO header described).
last_modified_date: '2026-09-07'
---

The 2019 Hackaday Superconference badge, designed by Jeroen "Sprite_TM" Domburg, ditched the usual microcontroller-plus-LEDs badge formula for a genuine FPGA computer built into a Game Boy-shaped shell. At its core sits a Lattice ECP5 FPGA (LFE5U-45F, roughly 45,000 LUTs) running a soft RISC-V core, driving a 480x320 color LCD behind a classic D-pad/A/B/Start/Select button layout. A working cartridge slot on the back let attendees plug in their own add-on boards — one attendee wired up a camera during the conference itself — and the badge could be reprogrammed over USB or flashed directly via JTAG for those who wanted to write their own gateware instead of just software.

Every one of the roughly 500+ badges was given free to Supercon attendees as their conference badge; it was never sold separately, and tickets to the 2019 Supercon sold out. Development ran nearly a year, with Hackaday's own behind-the-scenes writeup noting that firmware work continued until less than a day before the badges went out the door, and about 95% of the manufactured units passed quality control in time.

Both the hardware and firmware/gateware are open source: the PCB (KiCad, CC-BY-SA 3.0) is published at `hadbadge2019_pcb`, and the RISC-V SoC gateware and SDK — built entirely on the open-source Yosys/nextpnr-ecp5 FPGA toolchain — live at `hadbadge2019_fpgasoc`, both under Domburg's GitHub account.

## Make your own

- Hardware: clone [hadbadge2019_pcb](https://github.com/Spritetm/hadbadge2019_pcb) (KiCad, CC-BY-SA 3.0) and fabricate the board yourself.
- Firmware/gateware: clone [hadbadge2019_fpgasoc](https://github.com/Spritetm/hadbadge2019_fpgasoc) and build with the open-source ECP5 toolchain (Yosys, nextpnr-ecp5) to load a soft RISC-V core and the badge SDK onto the FPGA.
