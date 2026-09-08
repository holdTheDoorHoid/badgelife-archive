---
title: 'RVAsec 2026 Badge: BadgeMan'
id: rvasec-2026-rvasec-2026-badge
layout: badge
parent: RVAsec 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rvasec-2026
year: 2026
makers:
- name: HackRVA
  url: https://www.hackrva.org/badge/
summary: The 15th annual RVAsec electronic badge, hand-built by HackRVA members, styled as "BadgeMan" with a raven/Poe theme ("Nevermore to Risk") and running an open-source app framework on an RP2040.
functions: Runs a custom firmware/app framework (games and utilities loadable as apps) with a D-pad and buttons for input; includes an interactive CLI accessible over serial by holding the D-pad left button at boot; a companion SDL-based simulator lets people write and test apps on a computer without the hardware.
look:
  colors:
  - green
  - white
  - gold
  shape: rectangle
  themes:
  - horror
  - security
  - retro computer
tech:
  mcu: RP2040
  leds: null
  display: LCD (color, D-pad/button navigated)
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/HackRVA/badge2026
  eda_tool: null
links:
- label: github.com/HackRVA/badge2026
  url: https://github.com/HackRVA/badge2026
  kind: repo
- label: hack.RVA badge page
  url: https://www.hackrva.org/badge/
  kind: website
- label: 2026 RVAsec 15 electronic badge demo (YouTube)
  url: https://www.youtube.com/watch?v=1FeKCOANn0w
  kind: video
images:
- file: assets/images/badges/rvasec-2026/rvasec-2026-badge/6d3f93ebd1.png
  source: "https://github.com/HackRVA/badge2026"
  credit: "HackRVA"
  caption: "Render of the RVAsec 2026 badge PCB, showing the display, D-pad, buttons and 3.5mm jack"
contact: {}
notes:
- Custom Hack.RVA electronic badge for RVAsec 2026, demoed on YouTube with a public simulator/firmware repo. Found by the event-year sweep, task con-rvasec.
- The sweep's title was generic ("RVAsec 2026 Badge"); the badge silkscreen itself reads "BADGEMAN" with the tagline "Nevermore to Risk," so the title here notes that maker-facing name.
status: listed
sources:
- kind: url
  url: https://github.com/HackRVA/badge2026
  title: RVAsec 2026 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-rvasec); event read as ''RVAsec 2026''.'
- kind: url
  url: https://raw.githubusercontent.com/HackRVA/badge2026/main/README.md
  title: 'HackRVA/badge2026: README'
  accessed: '2026-09-08'
  note: Confirms RP2040 (Pico) MCU, on-board LCD, D-pad/buttons, micro-USB flashing (hold white button + connect USB to appear as UF2 drive), custom app framework, and an SDL-based simulator; firmware source is public (hardware schematics/Gerbers not found in the repo).
- kind: url
  url: https://raw.githubusercontent.com/HackRVA/badge2026/main/images/badge-image-1024.png
  title: badge-image-1024.png (repo render)
  accessed: '2026-09-08'
  note: Board render showing "RVASEC 2026" silkscreen, "BADGEMAN" name, "Nevermore to Risk" tagline, LCD, D-pad, four face buttons, 3.5mm audio jack, and micro-USB port; used to identify colors/shape/theme and saved as an entry image.
- kind: url
  url: https://www.hackrva.org/badge/
  title: Badge - hack.RVA
  accessed: '2026-09-08'
  note: Confirms HackRVA makes the RVAsec badge annually by hand (etching, SMD soldering, laser-cut acrylic in some years); no 2026-specific specs on this page.
- kind: url
  url: https://www.youtube.com/watch?v=1FeKCOANn0w
  title: 2026 RVAsec 15 electronic badge demo
  accessed: '2026-09-08'
  note: YouTube demo video of the badge, confirms it is for the 15th RVAsec and points to the same GitHub repo; not fetched for transcript content.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed as a real, built badge (not just a sweep snippet) via the maker's own GitHub repo, README, and a repo-hosted render, plus a YouTube demo video. Price, quantity made, and availability were not stated anywhere found and are left empty. No hardware repo, schematics, Gerbers, or BOM were located (only firmware/simulator source), so make_your_own.open_source is "partial" and hardware_url is empty. LED count/type not confirmed even though the repo includes a small "badge-led.png" icon asset (not sufficient to state a count/type). rvasec.com's own badge archive pages had no 2026-specific content when checked.
last_modified_date: '2026-09-08'
---

The RVAsec 2026 badge, the 15th in HackRVA's annual run of badges for the RVAsec security conference in Richmond, Virginia, is built around a Raspberry Pi Pico (RP2040) with an on-board color LCD, a D-pad, and several face buttons. The board's silkscreen names it "BadgeMan" and carries a raven/Edgar Allan Poe-flavored tagline, "Nevermore to Risk," continuing HackRVA's tradition of a yearly theme. It also includes a 3.5mm audio jack and charges/flashes over micro-USB, entering UF2 mass-storage mode when a small white button is held during connection.

Firmware is open source, published by HackRVA on GitHub as `badge2026`, along with a cross-platform SDL2-based simulator so people can write and test their own badge apps without needing the physical hardware. The badge supports a custom app framework (apps live as individual .c/.h files) and an interactive CLI reachable over serial by holding the D-pad left button at power-on. A YouTube demo shows the badge running ahead of the conference. Hardware design files (schematics, PCB layout, BOM) were not found published alongside the firmware, so it is not possible to say whether the board itself is open-hardware; price, production quantity, and how the badge was distributed to attendees were not stated in any source checked.

## Make your own

Firmware and a desktop simulator are available at github.com/HackRVA/badge2026. Building for hardware needs CMake 3.13+, the ARM GCC embedded toolchain, and the Pico SDK (pulled in as a git submodule); the simulator instead needs a C compiler, SDL2, and libpng, and runs on Linux, macOS, or Windows via WSL. No hardware files (schematics/Gerbers) were found in the repo, so replicating the physical board is not currently possible from public sources.
