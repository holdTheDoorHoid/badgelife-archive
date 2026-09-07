---
title: CHV Badge 2016 (CHVBadge_16)
id: dc24-chv-badge-2016-chvbadge-16
layout: badge
parent: DC24
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc24
year: 2016
makers:
- name: lanrat
summary: 'The official electronic badge for the Car Hacking Village at DEF CON 24 (2016), built around a USB-connected CAN bus interface and an onboard Pawn scripting VM.'
functions: 'Interfaces with vehicle CAN buses over USB; runs user-written Pawn scripts loaded through an included SDK; a companion Linux tool ("socketbadge") bridges the badge to SocketCAN virtual CAN interfaces for use with standard Linux CAN tooling.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - security
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: 'Distributed at the Car Hacking Village, DEF CON 24, July 2016'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/lanrat/CHVBadge_16
  eda_tool: null
links:
- label: github.com/lanrat/CHVBadge_16
  url: https://github.com/lanrat/CHVBadge_16
  kind: repo
  archived: https://web.archive.org/web/20260907112022/https://github.com/lanrat/CHVBadge_16
images:
  - file: assets/images/badges/dc24/chv-badge-2016-chvbadge-16/3a040ebd37.jpg
    source: "https://github.com/lanrat/CHVBadge_16"
    credit: "lanrat"
    caption: "The DEF CON 24 Car Hacking Village badge PCB"
  - file: assets/images/badges/dc24/chv-badge-2016-chvbadge-16/18b75edd03.jpg
    source: "https://github.com/lanrat/CHVBadge_16"
    credit: "lanrat"
    caption: "The CHV badge photographed at DEF CON 24, July 2016"
contact: {}
notes:
- Independent/community badge project tied to Car Hacking Village; year in repo name.
- 'Repo description: "Stuff for the DEFCON 24 Car Hacking Village Badge." The badge''s onboard Pawn script (can_socket.p) is credited in the repo to Nathan Hoch, with modifications by the repo owner (GitHub user lanrat). The badge SDK documentation referenced (for building/installing Pawn scripts) is included in the repo under "Defcon SDK" but was not reviewed in full.'
- 'The Linux-side "socketbadge" USB-to-SocketCAN bridge utility in this repo is credited to Rob "Deker" Dekelbaum.'
status: listed
sources:
- kind: url
  url: https://github.com/lanrat/CHVBadge_16
  title: CHV Badge 2016 (CHVBadge_16)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''DEF CON 24 (2016), Car Hacking Village''.'
  archived: https://web.archive.org/web/20260907112022/https://github.com/lanrat/CHVBadge_16
- kind: url
  url: https://raw.githubusercontent.com/lanrat/CHVBadge_16/master/socketbadge/README.md
  title: 'DEFCON 24 Car Hacking Badge SocketCAN Compatibility (README)'
  accessed: '2026-09-07'
  note: 'Confirms the badge is the official DEF CON 24 Car Hacking Village badge, describes its USB/CAN interface and Pawn-scripting SDK, and names the SDK script author (Nathan Hoch) and the socketbadge tool author (Rob "Deker" Dekelbaum).'
- kind: url
  url: https://api.github.com/repos/lanrat/CHVBadge_16
  title: 'lanrat/CHVBadge_16 (GitHub API)'
  accessed: '2026-09-07'
  note: 'Repo description confirms this is "Stuff for the DEFCON 24 Car Hacking Village Badge"; repo contains Defcon SDK, Photos, a Windows 7 x64 USB driver, and the socketbadge tool.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Could not find the physical specs (MCU, LEDs, display, battery, price, quantity made, availability, or EDA tool) in any source read; the repo has no top-level README and no store/press coverage was found. It is unclear whether "lanrat" designed the physical badge or only contributed the socketbadge USB driver/CAN tooling and hosts photos of it -- the actual hardware/firmware author(s) may be the Car Hacking Village organizers or Nathan Hoch, per the SDK script credit. hardware_url and a dedicated firmware_url for the badge''s own onboard firmware (as opposed to the companion PC-side "socketbadge" tool and the DEF CON-provided Pawn SDK) were not found, so open_source is marked partial (the Pawn script and socketbadge source are public; the badge''s low-level firmware/hardware design files are not present in this repo).'
last_modified_date: '2026-09-07'
---

The CHV Badge is the official electronic badge handed out at the Car Hacking Village during DEF CON 24 in July 2016. Rather than being a purely decorative or blinky badge, it doubles as a small USB-connected CAN bus interface for practicing automotive network hacking, and it can run user-written scripts in an onboard Pawn scripting VM using an included Defcon SDK.

This repository, maintained by GitHub user lanrat, collects supporting material for the badge: the Defcon SDK for writing and loading Pawn scripts, a Windows 7 x64 USB driver, event photos, and a small companion project called "socketbadge." Socketbadge is a Linux userspace tool (using libusb) that bridges the badge's USB CAN interface to two virtual SocketCAN (`vcan`) network interfaces, so the badge's CAN traffic can be worked with using standard Linux CAN tooling. The onboard Pawn script that talks CAN over USB (`can_socket.p`) is credited to Nathan Hoch, with light modifications by the repo owner; the socketbadge bridge itself is credited to Rob "Deker" Dekelbaum.

No pricing, production quantity, or storefront information was found for the badge, and its physical specifications (MCU, LED count, display, battery) are not documented in this repository or any other source checked. The repository was archived (made read-only) by GitHub in 2019.
