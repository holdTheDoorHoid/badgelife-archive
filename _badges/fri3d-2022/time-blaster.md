---
title: Time Blaster
id: fri3d-2022-time-blaster
layout: badge
parent: Fri3d 2022
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: fri3d-2022
year: 2022
makers:
- name: Fri3d Camp — Wim Van Gool (Brubacker), Hans Polders
  url: https://hackaday.io/hacker/187437-wim-van-gool
summary: A hand-solderable, through-hole ATmega328 infrared lasertag blaster kit that plugs into the Fri3d Camp badge for power and data, with IR transmitter and two receivers, buzzer, optional WS2812B RGB LEDs, optional CH340C USB (USB-B/Micro/USB-C) for standalone Arduino use, and 3D-printable grips; OSHWA certified BE000005.
functions: 'Infrared lasertag: transmits and receives IR "shots" (850nm/940nm) between units for outdoor tag-style games, with a buzzer for hit feedback and optional WS2812B RGB LED effects.'
look:
  colors: []
  shape: null
  themes:
  - radio
  - kit
  - learn to solder
tech:
  mcu: ATmega328
  leds:
    count: null
    type: WS2812B
    note: Optional, hand-solderable
  display: null
  connectivity:
  - ir
  - usb
  battery: powered by host badge
  sao_version: null
make_your_own:
  open_source: true
  hardware_url: https://github.com/Fri3dCamp/timeblaster-2020
  firmware_url: https://github.com/area3001/Timeblaster
  eda_tool: null
  license: GPL-3.0
  notes: Hardware repo includes multiple PCB revisions (00, 01, 02), block diagrams, assembly notes, and OpenSCAD files for a 3D-printable grip and LED protector. Firmware repo (area3001/Timeblaster) holds binaries, docs, firmware, and sample/MicroPython code for the IR link.
links:
- label: hackaday.io/project/167668-time-blaster
  url: https://hackaday.io/project/167668-time-blaster
  kind: hackaday
- label: github.com/Fri3dCamp/timeblaster-2020
  url: https://github.com/Fri3dCamp/timeblaster-2020
  kind: repo
- label: github.com/area3001/Timeblaster
  url: https://github.com/area3001/Timeblaster
  kind: repo
images:
- file: assets/images/badges/fri3d-2022/time-blaster/a57ea70ea1.jpg
  source: https://github.com/Fri3dCamp/timeblaster-2020
  credit: Fri3d Camp
  caption: Assembled Time Blaster kit
- file: assets/images/badges/fri3d-2022/time-blaster/48191e870c.jpg
  source: https://github.com/Fri3dCamp/timeblaster-2020
  credit: Fri3d Camp
  caption: Time Blaster PCB, full assembly
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/167668-time-blaster
  title: Time Blaster
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/167668-time-blaster
  title: Time Blaster - Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed maker names, event, IR/RGB/buzzer/USB features, ATmega328 chip, OSHWA cert BE000005, and that units were available at Fri3d Camp shop.
- kind: url
  url: https://github.com/Fri3dCamp/timeblaster-2020
  title: 'Fri3dCamp/timeblaster-2020: Hardware for the time blaster'
  accessed: '2026-09-07'
  note: Confirmed the kit was designed for Fri3d Camp 2020 (not 2022), GPL-3.0 hardware license, multiple PCB revisions, and grip/LED-protector design files; source of the two saved images.
- kind: url
  url: https://github.com/area3001/Timeblaster
  title: area3001/Timeblaster
  accessed: '2026-09-07'
  note: Firmware/addon repository (binaries, docs, firmware, sample code); page did not show a full README with MCU/license detail beyond what the hardware repo already confirmed.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: |
    Sources (the maker's own Hackaday project and the Fri3dCamp/timeblaster-2020 GitHub repo) consistently describe this kit as made for Fri3d Camp 2020, not 2022 — the repo name and README both say "2020" explicitly. No fri3d-2020 event id exists in _data/events.yml (only fri3d-2018, fri3d-2022, fri3d-2024), so the event field is left as fri3d-2022 per the research guide's rule for when no matching event exists; the correct con/year (Fri3d Camp 2020) is recorded here for whoever adds that event later. Price, quantity made, and exact availability status were not stated on the sources checked. LED count and OSHWA certificate BE000005 taken from the existing sheet-derived summary, not independently re-confirmed since it was already specific and plausible (unable to re-verify due to web search budget exhaustion this session).
last_modified_date: '2026-09-07'
model:
  file: assets/models/fri3d-2022/time-blaster.glb
  method: gerber
  source_file: design/Time_Blaster_00/OUTPUT/Gerber
  generated: '2026-09-07'
  bytes: 60676
  size_mm:
  - 420.0
  - 297.0
  note: The published files have no board outline, so the model is shown on a rectangular board.
---

Time Blaster is an infrared lasertag blaster designed by Fri3d Camp (Wim Van Gool and Hans Polders) as a plug-in accessory for the Fri3d Camp badge, drawing power and data from the host badge rather than carrying its own battery. It ships as a hand-solderable, through-hole kit built around an ATmega328, with two IR receivers, an 850nm/940nm IR transmitter, a buzzer for hit feedback, and pads for an optional WS2812B RGB LED strip for shot effects. Builders can also add a CH340C USB interface (in USB-B, Micro-USB, or USB-C form) to let the board run standalone as an Arduino-compatible device outside the badge ecosystem, and 3D-printable grips and an LED protector are provided for a more finished, holdable form.

Both hardware and firmware are open source: the PCB design (through several revisions, 00–02) and mechanical files live in Fri3dCamp's `timeblaster-2020` GitHub repository under a GPL-3.0 license, while the firmware and IR protocol sample code sit in a companion `area3001/Timeblaster` repository. The design is OSHWA-certified under BE000005. Sources consistently describe the project as built for Fri3d Camp 2020 rather than 2022 — the repository name, README, and project history all reference 2020 — but no `fri3d-2020` event entry currently exists in this archive, so this record stays filed under fri3d-2022 pending that addition.

## Make your own

The `Fri3dCamp/timeblaster-2020` repository has the PCB design files, a block diagram, assembly/soldering notes, and OpenSCAD sources for the printable grip and LED protector across its 00/01/02 hardware revisions. The `area3001/Timeblaster` repository carries the corresponding firmware, precompiled binaries, and IR sample code (including a MicroPython variant) needed to flash a built unit.
