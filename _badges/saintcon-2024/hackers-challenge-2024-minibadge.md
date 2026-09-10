---
title: Hackers Challenge 2024 minibadge
id: saintcon-2024-hackers-challenge-2024-minibadge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
series: Hackers Challenge
makers:
- name: unconfirmed
  url: https://github.com/utahsaint-org
summary: A small square PCB minibadge for SAINTCON 2024's Hackers Challenge CTF, with two LEDs powered from the host badge's minibadge header; no onboard microcontroller.
functions: ''
look:
  colors: []
  shape: rectangle
  themes:
  - security
  - ctf
  - puzzle
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Two generic 0805 SMD LEDs (schematic labels them simply "LED", no color specified) with series resistors; no driver IC.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Hackers-Challenge-2024
  firmware_url: null
  gerbers_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/Hackers-Challenge-2024
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Hackers-Challenge-2024
  kind: repo
images: []
contact: {}
notes:
- 2024 edition of the Hackers Challenge minibadge (distinct from the 2017, 2022, and 2023 editions already in the archive: saintcon-2017-hackers-challenge-official-minibadge, saintcon-2022-hackers-challenge-badge, saintcon-2023-hackers-challenge-minibadge-2023). Found by the event-year sweep, task saintcon-2024.
- Title corrected from the sweep's "Hackers-Challenge-2024 minibadge" (the repo folder name) to a spaced form; the repo gives no separate display name.
status: released
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Hackers-Challenge-2024
  title: Hackers-Challenge-2024 minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/Hackers-Challenge-2024/HC24.kicad_sch
  title: HC24.kicad_sch (schematic source)
  accessed: '2026-09-10'
  note: 'Confirms no MCU: only two Device:LED symbols with series resistors and power/GND symbols (power:+3.3V, power:GND). Read via raw.githubusercontent.com.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/Hackers-Challenge-2024/HC24.kicad_pcb
  title: HC24.kicad_pcb (board source)
  accessed: '2026-09-10'
  note: ~20x20mm square board (Edge.Cuts rect 0.16,0.16 to 20.16,20.16) using the standard SAINTCON "MiniBadge_Simple" header footprint with pins labeled 3V3+, VBATT, NC -- confirms it plugs into and is powered by a host badge's minibadge header rather than a SAO connector.
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024
  title: 'utahsaint-org/MiniBadges2024: Minibadges for SAINTCON 2024'
  accessed: '2026-09-10'
  note: Parent repo of official/submitted SAINTCON 2024 minibadge designs, listing 30+ folders including this one; no repo-level README with per-badge maker credits or specs.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: No README, build guide text, storefront listing, or photo of the finished item was found for this specific 2024 edition, so maker name, price, quantity, availability, and LED color remain unconfirmed. The KiCad schematic and PCB files (read directly, since GitHub's own directory view errored out for both WebFetch and the browser) show a simple two-LED board with no microcontroller, powered from the host badge over a standard SAINTCON "MiniBadge_Simple" 3.3V header (not an SAO connector) -- consistent with prior years' Hackers Challenge minibadges being simple, solder-your-own kits handed out around SAINTCON's Hackers Challenge CTF contest, but that link (kit distribution via the SAINTCON minibadge trading booth) is inferred from the general SAINTCON minibadge convention (per badge.gallery's SAINTCON 2024 minibadge trading page and minibadge.wiki, which catalog SAINTCON minibadges as solder-it-yourself kits) and not confirmed for this exact badge, so it is left out of get_one rather
    than stated as fact. The repo is maintained by the utahsaint-org GitHub org (SAINTCON's organizers), not a named individual designer.
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2024/hackers-challenge-2024-minibadge.glb
  method: kicad
  source_file: Hackers-Challenge-2024/HC24.kicad_pcb
  generated: '2026-09-10'
  bytes: 30620
---

The Hackers Challenge minibadge is a small SAINTCON tradition: a yearly minibadge tied to SAINTCON's Hackers Challenge, the conference's signature Jeopardy-style capture-the-flag contest. The archive already holds the 2017, 2022, and 2023 editions; this is the 2024 version, whose design files live in the `utahsaint-org/MiniBadges2024` repository alongside the rest of that year's official and submitted SAINTCON minibadges.

Unlike some of the archive's other minibadges, this one has no onboard microcontroller. Its KiCad schematic shows just two surface-mount LEDs with series resistors, wired to a standard SAINTCON "MiniBadge_Simple" header (pins for 3.3V, ground, VBATT, and a no-connect) rather than an SAO connector -- meaning it lights up only when plugged into a host badge that supplies power over that header, and does nothing on its own. The board is a roughly 20x20mm square, and the accompanying Illustrator/SVG artwork uses a dense geometric line pattern rather than a clear logo or text.

No build guide, storefront page, or maker credit specific to this 2024 edition turned up during research, so its LED color, price, quantity made, and exact distribution (almost certainly through SAINTCON's minibadge trading/kit convention, as with other entries in the same repo) are left unconfirmed here rather than guessed.
