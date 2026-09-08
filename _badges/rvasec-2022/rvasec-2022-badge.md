---
title: RVAsec 2022 Badge
id: rvasec-2022-rvasec-2022-badge
layout: badge
parent: RVAsec 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rvasec-2022
year: 2022
makers:
- name: HackRVA
  url: https://www.hackrva.org/badge/
summary: A hand-built electronic conference badge made by members of HackRVA (Richmond's member-run makerspace) for RVAsec 2022, with a color LCD, D-pad, and rotary encoder for navigating an app/game framework.
functions: Runs a menu-driven firmware with an interactive terminal, apps, and games navigated via a D-pad and rotary encoder; hardware support for IR transmit/receive.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: RP2040
  leds:
    count: null
    type: null
    note: 3-color LED (per maker's GitHub description)
  display: LCD (color)
  connectivity:
  - ir
  battery: null
  sao_version: null
  inputs:
  - buttons
  - rotary encoder
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Made for and distributed to RVAsec 2022 attendees by HackRVA; not sold.
make_your_own:
  open_source: 'yes'
  hardware_url: null
  firmware_url: https://github.com/HackRVA/badge2022
  eda_tool: null
links:
- label: github.com/badge-gallery/hackrva-2022
  url: https://github.com/badge-gallery/hackrva-2022
  kind: repo
- label: github.com/HackRVA/badge2022
  url: https://github.com/HackRVA/badge2022
  kind: repo
- label: hackrva.github.io/badge2022
  url: https://hackrva.github.io/badge2022/
  kind: website
- label: hackrva.github.io/badge2022/about.html
  url: https://hackrva.github.io/badge2022/about.html
  kind: doc
- label: hackrva.org/badge
  url: https://www.hackrva.org/badge/
  kind: website
images:
  - file: assets/images/badges/rvasec-2022/rvasec-2022-badge/9b06286be7.jpg
    source: "https://hackrva.github.io/badge2022/"
    credit: "HackRVA"
    caption: "RVAsec 2022 badges"
  - file: assets/images/badges/rvasec-2022/rvasec-2022-badge/0c2fef1bff.jpg
    source: "https://hackrva.github.io/badge2022/"
    credit: "HackRVA"
    caption: "RVAsec 2022 badge prototype"
contact: {}
notes:
- HackRVA electronic badge for RVAsec 2022, with an accompanying badge-gallery/hackrva-2022 GitHub repo. Found by the event-year sweep, task con-rvasec.
- The sweep's source (github.com/badge-gallery/hackrva-2022) is a mirror; the maker's own repo is github.com/HackRVA/badge2022, with build/design documentation hosted at hackrva.github.io/badge2022.
status: released
sources:
- kind: url
  url: https://github.com/badge-gallery/hackrva-2022
  title: RVAsec 2022 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-rvasec); event read as ''RVAsec 2022''.'
- kind: url
  url: https://github.com/HackRVA/badge2022
  title: 'HackRVA/badge2022: RVASec Badge 2022'
  accessed: '2026-09-08'
  note: Maker's own repository (badge-gallery/hackrva-2022 is a mirror); firmware source, RP2040/Pico target, CMake build.
- kind: url
  url: https://hackrva.github.io/badge2022/
  title: RVAsec 2022 Badge
  accessed: '2026-09-08'
  note: Maker's badge documentation hub; confirms hand-built by HackRVA members; badge photos.
- kind: url
  url: https://hackrva.github.io/badge2022/about.html
  title: About the Badge
  accessed: '2026-09-08'
  note: Design/build process (several months, design/etch/populate/program stages); build photos.
- kind: url
  url: https://www.hackrva.org/badge/
  title: Badge - hack.RVA
  accessed: '2026-09-08'
  note: HackRVA's general badge page confirming they make an RVAsec badge annually.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Chip/display/LED details come from the GitHub repo description (README itself has no hardware spec section); no price, quantity, or availability figures were published anywhere found. No hardware design files (schematics/gerbers) located, only firmware source.
last_modified_date: '2026-09-08'
---

The RVAsec 2022 badge was hand-built and programmed by members of HackRVA, Richmond, Virginia's member-run, non-profit makerspace, for that year's RVAsec security conference. It is built around a Raspberry Pi Pico (RP2040) and features a color LCD, a D-pad, and a rotary encoder, which attendees use to navigate a menu-driven firmware offering an interactive terminal, apps, and games. The board also has hardware support for IR transmit/receive, though at the time the firmware repository was last documented, IR simulator support and audio I/O remained unimplemented.

HackRVA has produced a badge for RVAsec nearly every year; the team describes spending "several months" meeting at the makerspace to design the badge, etch the circuit boards, populate components, and write the software before the conference. The firmware is open source, built with CMake, and can also be compiled into a desktop simulator (requiring GTK2) so apps can be developed and tested without a physical badge.

No price, production quantity, or public sale information was found — badges of this kind are typically made for and given to conference attendees rather than sold. No hardware design files (schematics or PCB layouts) were located, only the firmware source.
