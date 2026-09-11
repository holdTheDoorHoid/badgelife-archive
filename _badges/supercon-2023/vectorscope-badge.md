---
title: Vectorscope Badge
id: supercon-2023-vectorscope-badge
layout: badge
parent: Supercon 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2023
year: 2023
makers:
- name: Hackaday
  url: https://github.com/Hack-a-Day
- name: Voja Antonic
  role: hardware design
summary: 'The official Hackaday Superconference 2023 badge: an analog-inspired vector oscilloscope and dual-channel waveform generator built around a Raspberry Pi Pico (RP2040) with a round GC9A01 IPS display and an AK4619 ADC/DAC, programmable in MicroPython, with four buttons, a joystick, a nine-pin 0.1-inch signal header and an included expansion prototyping board; hardware design credited to Voja Antonic.'
functions: Displays incoming 0-3V X-Y signals as a vintage-style vector scope trace with a "fake-phosphor" persistence effect, can plot Lissajous figures, and doubles as an arbitrary waveform generator with an audio amplifier on the Y input; has four programmable memory slots for saved demos and a joystick with a custom keycap for menu control.
look:
  colors: []
  shape: circle
  themes:
  - retro computer
  - measurement
  - hardware tool
tech:
  mcu: RP2040
  leds: null
  display: 1.28" round GC9A01 IPS LCD
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: about 550
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of Hackaday Supercon 2023 as the conference badge.
make_your_own:
  open_source: true
  hardware_url: https://github.com/Hack-a-Day/Vectorscope/tree/main/hardware
  firmware_url: https://github.com/Hack-a-Day/Vectorscope/tree/main/firmware
  eda_tool: Altium
  license: MIT
  notes: Designed in Altium Circuit Maker; a work-in-progress KiCad conversion of the PCB is also included in the repo (ground plane not fully correct, useful mainly for mechanical/case design). Gerbers, drill files and a BOM are provided. Firmware is MicroPython.
links:
- label: github.com/Hack-a-Day/Vectorscope
  url: https://github.com/Hack-a-Day/Vectorscope
  kind: repo
  archived: https://web.archive.org/web/20260419062358/https://github.com/Hack-a-Day/Vectorscope
- label: hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope
  url: https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
  kind: article
  archived: https://web.archive.org/web/20260708121204/https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
- label: hackaday.com/2023/10/29/packing-for-supercon-heres-a-printable-case-for-your-badge
  url: https://hackaday.com/2023/10/29/packing-for-supercon-heres-a-printable-case-for-your-badge/
  kind: article
  archived: https://web.archive.org/web/20260305212909/https://hackaday.com/2023/10/29/packing-for-supercon-heres-a-printable-case-for-your-badge/
- label: github.com/softegg/supercon-2023-badge-enclosure/tree/main/BASIC-2
  url: https://github.com/softegg/supercon-2023-badge-enclosure/tree/main/BASIC-2
  kind: repo
- label: github.com/davedarko/Vectorscope
  url: https://github.com/davedarko/Vectorscope
  kind: repo
- label: github.com/softegg/supercon-2023-badge-enclosure (3D-printable case, community)
  url: https://github.com/softegg/supercon-2023-badge-enclosure/
  kind: repo
images:
- file: assets/images/badges/supercon-2023/vectorscope-badge/4acccde076.jpg
  source: https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
  credit: Hackaday
  caption: The Vectorscope badge displaying a round vector waveform on its GC9A01 IPS screen
  archived: https://web.archive.org/web/20260708121204/https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
- file: assets/images/badges/supercon-2023/vectorscope-badge/d6f3ae7c55.jpg
  source: https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
  credit: Hackaday
  caption: The Vectorscope badge front panel with joystick and buttons
  archived: https://web.archive.org/web/20260708121204/https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
- file: assets/images/badges/supercon-2023/vectorscope-badge/d6f3ae7c55.jpg
  source: https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
  credit: Hackaday
  caption: The Vectorscope badge with its round display
  archived: https://web.archive.org/web/20260708121204/https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
- file: assets/images/badges/supercon-2023/vectorscope-badge/0f3b7426e2.jpg
  source: https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
  credit: Hackaday
  caption: The Vectorscope badge, close-up view
  archived: https://web.archive.org/web/20260708121204/https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Hack-a-Day/Vectorscope
  title: Hack-a-Day/Vectorscope — Vectorscope badge for the 2023 Hackaday Supercon and beyond!
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260419062358/https://github.com/Hack-a-Day/Vectorscope
- kind: url
  url: https://github.com/Hack-a-Day/Vectorscope
  title: Hack-a-Day/Vectorscope README
  accessed: '2026-09-07'
  note: 'Confirmed hardware/firmware details: RP2040, GC9A01 display, AK4619 ADC/DAC, Altium design with WIP KiCad conversion, MIT license, Gerbers/BOM/schematics included, image of finished badge (DSC_0146_featured.png).'
  archived: https://web.archive.org/web/20260419062358/https://github.com/Hack-a-Day/Vectorscope
- kind: url
  url: https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
  title: '2023 Hackaday Supercon Badge: Welcome To The Vectorscope'
  accessed: '2026-09-07'
  note: Confirmed hardware designer (Voja Antonic), functions (vector scope + waveform generator, Lissajous figures, four memory slots, joystick), and approximate production quantity (about 550 badges for attendees).
  archived: https://web.archive.org/web/20260708121204/https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
- kind: url
  url: https://github.com/davedarko/Vectorscope
  title: davedarko/Vectorscope — fork of Hack-a-Day/Vectorscope (2023 Hackaday Supercon badge)
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.com/2023/10/29/packing-for-supercon-heres-a-printable-case-for-your-badge/
  title: Packing For Supercon? Here's A Printable Case For Your Badge
  accessed: '2026-09-07'
  note: Describes a community-made 3D-printable protective case for the badge by T.B. Trzepacz, with design files on GitHub (softegg/supercon-2023-badge-enclosure); confirms badge has SMD buttons and through-hole expansion headers.
  archived: https://web.archive.org/web/20260305212909/https://hackaday.com/2023/10/29/packing-for-supercon-heres-a-printable-case-for-your-badge/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: LED count/type not stated by any source (display uses TFT graphics, not addressable LEDs, so left null). Price not applicable — the badge is given free to Supercon attendees, not sold. SAO header count not mentioned; the badge has a general 9-pin 0.1" signal header rather than a standard SAO port, so sao_version is set to none. Merged with duplicate entry 'Vectorscope Badge' (supercon-2023-supercon-2023-vectorscope).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/supercon-2023/supercon-2023-vectorscope/
model:
  file: assets/models/supercon-2023/vectorscope-badge.glb
  method: gerber
  source_file: hardware/vectorscope/vectorscope.kicad_pcb
  generated: '2026-09-10'
  bytes: 290776
  size_mm:
  - 116.0
  - 73.0
---

The Vectorscope was the official badge for Hackaday Supercon 2023, handed out free to roughly 550 attendees. After two badges built around digital retrocomputing themes, the Hackaday team wanted to go analog: the result is a round-screened device that acts as both a vector oscilloscope and an arbitrary waveform generator, echoing the look of old CRT scopes. A Raspberry Pi Pico (RP2040) drives a round GC9A01 IPS display with a "fake-phosphor" persistence effect, while an AK4619 ADC/DAC chip (borrowed in spirit from Sebastian Holzapfel's Eurorack FPGA frontend) reads and generates 0-3V signals on the X and Y channels, letting the badge trace Lissajous figures or plot whatever voltages are fed into its nine-pin signal header. The badge is programmed in MicroPython, has four buttons and a joystick with a custom keycap for navigating four programmable demo memory slots, and includes a bundled prototyping expansion board for attendees who wanted to hack on it further. Hardware design is credited to Voja Antonic.

## Make your own

The full design is open source under the MIT license in the [Hack-a-Day/Vectorscope repo](https://github.com/Hack-a-Day/Vectorscope). The PCB was designed in Altium Circuit Maker, with Gerbers, drill files, a BOM, and datasheets provided for anyone who wants to fabricate their own board; a work-in-progress KiCad conversion is also included, though its ground plane isn't fully correct and it's better suited to mechanical use (like designing a case) than to respinning the board. Firmware is MicroPython, distributed as source plus a `.uf2` image for restoring a badge to its original state; the repo's setup notes cover getting started with Thonny, VS Code (via the MicroPico extension), or a plain text editor with mpremote. One build note from the maintainers: transistor T1 must be soldered dead-bug style (flipped and rotated) rather than in its silkscreen orientation. A separate community project, the [BASIC-2 enclosure](https://github.com/softegg/supercon-2023-badge-enclosure/tree/main/BASIC-2) by Tina Belmont, provides a 3D-printable case.

## Notes merged from the duplicate entry "Vectorscope Badge"

The Vectorscope was the official badge of the 2023 Hackaday Superconference, held that October in Pasadena, California. Designed by Voja Antonic with Hackaday's badge team, it reimagines a classic piece of analog test equipment as a wearable: a Raspberry Pi Pico (RP2040) drives a round GC9A01 LCD styled to look like a CRT vectorscope screen, while an AK4619 audio ADC/DAC chip is repurposed to read 0-3V analog signals and plot them in X-Y mode, complete with a simulated phosphor-fade trail. Alongside the scope function, the badge doubles as a two-channel programmable waveform generator with an amplified audio output, a custom joystick, four buttons for storing and replaying short programs, and a through-hole prototyping area with a nine-pin header for attaching outside circuitry - making it as much an analog electronics playground as a conference credential. The design was inspired in part by Sebastian Holzapfel's Eurorack FPGA work and the flow3r badge from Chaos Camp.

Like other Hackaday Supercon badges, the Vectorscope was given to conference attendees rather than sold, and no separate retail listing or price has surfaced. Firmware is written in MicroPython, with setup guides for Thonny, VS Code (MicroPico), and mpremote. Shortly after the event, community member T.B. Trzepacz published a 3D-printable protective case for the badge (STL and Fusion 360 files, both FDM- and SLA-friendly) that preserves access to the buttons and expansion header while adding lanyard mounting holes.

## Make your own

The full hardware and firmware are open source under the MIT license in the official `Hack-a-Day/Vectorscope` GitHub repository (an early community fork lives at `davedarko/Vectorscope`). The repo includes schematics and Gerber files, PCB source in both Altium and KiCad formats, and the MicroPython firmware, so the badge can be fabricated and built from scratch by following the repo's setup instructions.
