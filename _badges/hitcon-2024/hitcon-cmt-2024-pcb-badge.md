---
title: HITCON CMT 2024 PCB Badge
id: hitcon-2024-hitcon-cmt-2024-pcb-badge
layout: badge
parent: Hitcon Cmt 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hitcon-2024
year: 2024
makers:
- name: HITCON Activity Team / hacksintaiwan
  url: https://github.com/hacksintaiwan
summary: The official attendee badge for HITCON Community 2024 (HITCON's 20th anniversary), a PCB name badge built around an STM32 MCU with an LED matrix, IR badge-to-badge docking, onboard games, and a BadUSB mode.
functions: Score accrual over the two-day event (attending talks, visiting community booths, docking with other badges via IR), single- and two-player games (Tetris, Snake, Dino), a name/score display, and a documented BadUSB mode that lets the badge act as a USB HID keystroke-injection device.
look:
  colors: [black]
  shape: rectangle
  themes: [ctf, hardware tool, puzzle]
tech:
  mcu: STM32F103C8T6
  leds:
    count: null
    type: discrete
    note: Row/column-scanned LED matrix (0603 discrete LEDs per the bill of materials); exact matrix dimensions not confirmed by sources.
  display: LED matrix
  connectivity: [ir, usb]
  inputs: [buttons]
  battery: AAA battery
  sao_version: none
get_one:
  price: included with HITCON CMT 2024 registration
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: [free_drop]
  where: Handed to attendees, speakers, and staff as their conference ID/badge at HITCON Community 2024, Aug 23-24 2024, Academia Sinica, Taipei.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/hacksintaiwan/hitcon-pcb-badge/tree/main/pcb
  firmware_url: https://github.com/hacksintaiwan/hitcon-pcb-badge/tree/main/fw
  gerbers_url: null
  bom_url: https://github.com/hacksintaiwan/hitcon-pcb-badge/blob/main/pcb/bill-of-materials.md
  eda_tool: KiCad
  license: BSD 3-Clause
  fab_url: null
  notes: Hardware (KiCad schematics/PCB), firmware (STM32CubeIDE-based), a Python game-build toolchain, backend/base-station/web companion code, and a BadUSB protocol spec (BadUSB.md) are all in the same repo, split by hardware revision (V1.1 is the 2024 CMT badge; V2.x are 2025 revisions).
links:
- label: github.com/hacksintaiwan/hitcon-pcb-badge
  url: https://github.com/hacksintaiwan/hitcon-pcb-badge
  kind: repo
- label: HITCON CMT 2024 event page (badge announcement)
  url: https://hitcon.org/2024/CMT/events/
  kind: website
- label: HITCON PCB Badge user manual (2024)
  url: https://pcb.hitcon.org/2024/
  kind: doc
images: []
contact: {}
notes:
- STM32F103C8T6 PCB badge with 16x16 LED matrix, IR badge-docking, BadUSB and games (Tetris/Snake/Dino). Found by the event-year sweep, task con-hitcon.
- 'Sweep title matched the maker''s own naming. LED matrix size could not be confirmed as 16x16 from primary sources; the repo README documents a 4-row / up-to-8-column scanned matrix, so the sweep''s figure is left out of tech.leds pending a source that states it directly.'
- No rights-cleared photo of the badge itself was found: the manual site (pcb.hitcon.org) is behind Cloudflare's bot check and returned no content, and the only maker-posted image found (an Instagram promo graphic for the BadUSB challenge) is a text-overlaid announcement graphic rather than a clean product photo, so no image was saved.
status: released
sources:
- kind: url
  url: https://github.com/hacksintaiwan/hitcon-pcb-badge
  title: HITCON CMT 2024 PCB Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-hitcon); event read as ''HITCON CMT 2024''.'
- kind: url
  url: https://github.com/hacksintaiwan/hitcon-pcb-badge/blob/main/README.md
  title: hitcon-pcb-badge README
  accessed: '2026-09-08'
  note: Confirms V1.1 hardware = 2024 CMT Attendee badge; documents IR tx/rx, LED matrix row/col drive, buttons, cross-board USART.
- kind: url
  url: https://github.com/hacksintaiwan/hitcon-pcb-badge/blob/main/pcb/bill-of-materials.md
  title: hitcon-pcb-badge bill of materials
  accessed: '2026-09-08'
  note: Confirms STM32F103C8T6 MCU, 0603 LED matrix, IRM3638 IR receiver, AAA battery power, MicroUSB.
- kind: url
  url: https://github.com/hacksintaiwan/hitcon-pcb-badge/blob/main/Menu.md
  title: hitcon-pcb-badge Menu.md
  accessed: '2026-09-08'
  note: Confirms menu structure and game list (BadUSB, Snake, Dino, Tetris single-player; Tetris, Snake, xchg two-player) plus name/score display modes.
- kind: url
  url: https://github.com/hacksintaiwan/hitcon-pcb-badge/blob/main/LICENSE
  title: hitcon-pcb-badge LICENSE
  accessed: '2026-09-08'
  note: BSD 3-Clause License, copyright 2024.
- kind: url
  url: https://hitcon.org/2024/CMT/events/
  title: Events | HITCON CMT 2024
  accessed: '2026-09-08'
  note: 'Confirms (search snippet, page itself 403s to fetch) every attendee''s ID at HITCON CMT 2024 was this PCB, that its score rises over the event via talks/booths/docking, and that it plays games.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, event, MCU, IR docking, BadUSB, games, open-source license) confirmed directly from the maker''s own GitHub repo. Could not confirm: exact LED matrix dimensions (sweep notes said 16x16; not stated in any source read), battery count/holder type beyond "AAA", quantity made, and whether it was sold separately or only given to registered attendees. The official 2024 user-manual site (pcb.hitcon.org/2024/) is behind Cloudflare and could not be fetched directly; used only via search snippet. No rights-cleared photo of the badge itself was found.'
last_modified_date: '2026-09-08'
---

The HITCON CMT 2024 PCB Badge was the official conference ID for HITCON Community 2024, held August 23-24, 2024 at Academia Sinica in Taipei to mark HITCON's 20th anniversary. Every speaker, paid attendee, and staff member wore one instead of a printed badge. Built around an STM32F103C8T6 microcontroller, it drives a row/column-scanned LED matrix for its name and score display, reads input from a row of buttons, and talks to other badges over IR for badge-to-badge "docking." A knowledge score accrues over the two days as attendees watch talks, visit community booths, and dock with other badges, and the badge doubles as a small game console with single-player Tetris, Snake, and Dino, plus two-player Tetris, Snake, and an "xchg" mode played over the IR/UART link.

The HITCON Activity Team (posting as hacksintaiwan) also built in a BadUSB mode: the badge can be loaded with an arbitrary keystroke script over its documented HID protocol and used as a USB "rubber ducky," which the team promoted as its own on-site challenge during the event. Hardware and firmware are both open source under a BSD 3-Clause license in the `hacksintaiwan/hitcon-pcb-badge` GitHub repository, which also holds the KiCad source, bill of materials, a BadUSB protocol spec, and companion backend/base-station/web tooling used to run the event's scoring system. The same repository later grew V2.x hardware revisions for HITCON 2025; V1.1 is specifically the 2024 CMT attendee hardware described here.

Sources read for this entry did not state the badge's LED matrix dimensions, exact battery configuration, or how many units were made, and no rights-cleared photo of the physical badge could be located, so those fields are left blank rather than guessed.
