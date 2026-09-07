---
title: Vectorscope Badge
id: supercon-2023-supercon-2023-vectorscope
layout: badge
parent: Supercon 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2023
year: 2023
makers:
- name: Hackaday (hardware by Voja Antonic)
  url: https://github.com/Hack-a-Day/Vectorscope
summary: 'The official Hackaday Superconference 2023 badge: a Raspberry Pi Pico (RP2040) driving a round GC9A01 display styled as a vintage analog vectorscope, with an AK4619 ADC/DAC for signal input and MicroPython firmware.'
functions: 'X-Y vector display with phosphor-style fading effects; a two-channel programmable waveform generator; an audio amplifier on the Y input; a custom joystick with keycap and four front-panel buttons for storing and playing code snippets; a through-hole prototyping area and nine-pin 0.1" connector for hooking up custom analog circuits.'
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
  display: round GC9A01 LCD
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of the 2023 Hackaday Superconference (October 2023, Pasadena, CA); no public retail sale found.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Hack-a-Day/Vectorscope
  firmware_url: https://github.com/Hack-a-Day/Vectorscope
  eda_tool: Altium
links:
- label: github.com/davedarko/Vectorscope
  url: https://github.com/davedarko/Vectorscope
  kind: repo
- label: github.com/Hack-a-Day/Vectorscope
  url: https://github.com/Hack-a-Day/Vectorscope
  kind: repo
- label: hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope
  url: https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
  kind: article
- label: hackaday.com/2023/10/29/packing-for-supercon-heres-a-printable-case-for-your-badge
  url: https://hackaday.com/2023/10/29/packing-for-supercon-heres-a-printable-case-for-your-badge/
  kind: article
- label: github.com/softegg/supercon-2023-badge-enclosure (3D-printable case, community)
  url: https://github.com/softegg/supercon-2023-badge-enclosure/
  kind: repo
images:
- file: assets/images/badges/supercon-2023/supercon-2023-vectorscope/d6f3ae7c55.jpg
  source: "https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/"
  credit: "Hackaday"
  caption: "The Vectorscope badge with its round display"
- file: assets/images/badges/supercon-2023/supercon-2023-vectorscope/0f3b7426e2.jpg
  source: "https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/"
  credit: "Hackaday"
  caption: "The Vectorscope badge, close-up view"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Vectorscope
  title: davedarko/Vectorscope — fork of Hack-a-Day/Vectorscope (2023 Hackaday Supercon badge)
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
  title: "2023 Hackaday Supercon Badge: Welcome To The Vectorscope"
  accessed: '2026-09-07'
  note: Announcement article - describes badge concept, hardware (RP2040, GC9A01, AK4619), features, inspirations (Sebastian Holzapfel's Eurorack FPGA work, the flow3r badge), and confirms distribution to attendees. Source of the two saved images.
- kind: url
  url: https://github.com/Hack-a-Day/Vectorscope
  title: Hack-a-Day/Vectorscope GitHub repository
  accessed: '2026-09-07'
  note: Official repo - confirms RP2040/GC9A01/AK4619 hardware, MIT license, and that schematics, Gerbers, Altium and KiCad source, and firmware are all published.
- kind: url
  url: https://hackaday.com/2023/10/29/packing-for-supercon-heres-a-printable-case-for-your-badge/
  title: "Packing For Supercon? Here's A Printable Case For Your Badge"
  accessed: '2026-09-07'
  note: Describes a community-made 3D-printable protective case for the badge by T.B. Trzepacz, with design files on GitHub (softegg/supercon-2023-badge-enclosure); confirms badge has SMD buttons and through-hole expansion headers.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all four cited sources (Hack-a-Day/Vectorscope repo, davedarko/Vectorscope fork, both Hackaday.com articles). Every non-empty field and every factual sentence in the summary/functions/body/Make-your-own section is supported: RP2040 + round GC9A01 LCD + AK4619 ADC/DAC repurposed for analog input, MicroPython firmware, MIT-licensed hardware+firmware with schematics/Gerbers/Altium+KiCad published, free distribution to Supercon 2023 attendees, and the community 3D-printable case by T.B. Trzepacz (STL + Fusion 360, preserves buttons/expansion header, adds lanyard holes). Both saved images are sourced from the Hackaday announcement article, which shows photos of this badge. No stated retail price or production quantity exists in any source - this was the standard conference badge, not sold - so get_one.price/quantity remain empty; that is correct, not a gap. tech.eda_tool set to Altium since the repo README lists Altium (Circuit Maker) as the primary format alongside a work-in-progress KiCad conversion. LED count/type, connectivity, battery, sao_version, colors, and gerbers/bom/license sub-fields are not stated in any source reviewed, so they remain empty/null as required.'
last_modified_date: '2026-09-07'
---

The Vectorscope was the official badge of the 2023 Hackaday Superconference, held that October in Pasadena, California. Designed by Voja Antonic with Hackaday's badge team, it reimagines a classic piece of analog test equipment as a wearable: a Raspberry Pi Pico (RP2040) drives a round GC9A01 LCD styled to look like a CRT vectorscope screen, while an AK4619 audio ADC/DAC chip is repurposed to read 0-3V analog signals and plot them in X-Y mode, complete with a simulated phosphor-fade trail. Alongside the scope function, the badge doubles as a two-channel programmable waveform generator with an amplified audio output, a custom joystick, four buttons for storing and replaying short programs, and a through-hole prototyping area with a nine-pin header for attaching outside circuitry - making it as much an analog electronics playground as a conference credential. The design was inspired in part by Sebastian Holzapfel's Eurorack FPGA work and the flow3r badge from Chaos Camp.

Like other Hackaday Supercon badges, the Vectorscope was given to conference attendees rather than sold, and no separate retail listing or price has surfaced. Firmware is written in MicroPython, with setup guides for Thonny, VS Code (MicroPico), and mpremote. Shortly after the event, community member T.B. Trzepacz published a 3D-printable protective case for the badge (STL and Fusion 360 files, both FDM- and SLA-friendly) that preserves access to the buttons and expansion header while adding lanyard mounting holes.

## Make your own

The full hardware and firmware are open source under the MIT license in the official `Hack-a-Day/Vectorscope` GitHub repository (an early community fork lives at `davedarko/Vectorscope`). The repo includes schematics and Gerber files, PCB source in both Altium and KiCad formats, and the MicroPython firmware, so the badge can be fabricated and built from scratch by following the repo's setup instructions.
