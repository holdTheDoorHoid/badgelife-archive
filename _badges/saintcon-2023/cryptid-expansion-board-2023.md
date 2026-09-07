---
title: Cryptid Expansion Board (2023)
id: saintcon-2023-cryptid-expansion-board-2023
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: saintcon-2023
year: 2023
makers:
- name: distinctm1nd
  url: https://github.com/distinctm1nd
summary: A DIY, cryptid-themed expansion board for the SAINTCON minibadge system that mounts 16 minibadges and drives a discrete (no-MCU) blinky face made of yellow, orange and red LEDs.
functions: Holds 16 minibadges on 8-pin headers and lights a transistor-driven blinky circuit (no microcontroller) forming a forehead triangle, cheek, eye and lip LEDs; a potentiometer sets the flash rate; it can chain to other expansion boards and, when powered from a host badge, exposes a clock pin.
look:
  colors:
  - yellow
  - orange
  - red
  shape: null
  themes:
  - horror
  - village badge
tech:
  mcu: none
  leds:
    count: 28
    type: SMD 1206 / through-hole
    note: 16 yellow, 6 orange, 2 red SMD 1206 LEDs plus 2 red and 2 multicolor-fast-flash through-hole LEDs; flash timing is set by discrete transistors/capacitors and a potentiometer, not a microcontroller.
  display: none
  connectivity: []
  battery: 2x AA (or powered through a host conference badge via a 20-pin connector)
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
  hardware_url: https://github.com/distinctm1nd/cryptid_expansion_board_2023
  firmware_url: null
  eda_tool: null
links:
- label: github.com/distinctm1nd/cryptid_expansion_board_2023
  url: https://github.com/distinctm1nd/cryptid_expansion_board_2023
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: listed
sources:
- kind: url
  url: https://github.com/distinctm1nd/cryptid_expansion_board_2023
  title: Cryptid Expansion Board (2023)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''saintcon-2023''.'
- kind: url
  url: https://www.saintcon.org/com-minibadge/
  title: Community – Minibadge (SAINTCON)
  accessed: '2026-09-07'
  note: Confirms distinctm1nd (with SHIFTY) runs the SAINTCON minibadge community that this expansion board belongs to; page did not name this specific board.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Verified against the raw GitHub README (all BOM/LED counts, no-MCU
    transistor/capacitor blinky circuit, potentiometer, clock-pin behavior,
    battery-vs-badge power, daisy-chain connector, lavaman 3D-printed back,
    and the battery-connector damage warning all match the source text
    word-for-word) and against an archived copy of the saintcon.org community
    page (web.archive.org snapshot dated 2026-01-20), which confirms "Minibadge
    Community Brought to you by: SHIFTY and distinctm1nd" but does not name
    this board specifically. Note: the live saintcon.org/com-minibadge/ URL
    returns 404 as of this check (2026-09-07); the citation is still sound
    because the archived snapshot shows matching content, but the link itself
    may need updating to a wayback URL if it stays down. Only source found is
    the maker's own GitHub repo, which is a build/assembly guide (BOM + solder
    instructions) rather than published PCB design files (no schematic,
    gerbers, or KiCad source in the repo) — make_your_own.open_source is
    correctly "partial" for that reason. No price, quantity, or availability
    info was published anywhere found. The README contains literal "<IMAGE>"
    placeholders with no actual image files or URLs, so no images could be
    saved. Event/year is inferred from context (distinctm1nd's documented role
    running the SAINTCON minibadge community, and the "2023" in the repo name)
    rather than a page that states "SAINTCON 2023" outright; no independent
    source confirms the exact event, but nothing found contradicts it either.
last_modified_date: '2026-09-07'
---

The Cryptid Expansion Board is a DIY solder kit built for the SAINTCON minibadge ecosystem, where attendees collect small trading-card-sized "minibadges" throughout the con. Rather than a badge in its own right, it's a holder/expansion board: sixteen 8-pin headers mount minibadges across its face, while the board itself lights up a cryptid-styled "face" made from SMD and through-hole LEDs — a triangular blinky pattern in the forehead, glowing cheeks, eyes and lips. There's no microcontroller; the flash pattern comes from a small transistor-and-capacitor circuit whose speed is set with an onboard potentiometer.

The board can run standalone on two AA batteries or draw power from a host conference badge through a 20-pin shrouded connector (only power flows this way when connected to the correctly labeled port — the maker's instructions warn that plugging a badge into the wrong connector risks damaging both boards). When powered by a badge rather than batteries, an extra clock pin becomes active. Additional expansion boards can be daisy-chained off a second connector, and the maker (distinctm1nd, who together with SHIFTY runs SAINTCON's minibadge community) documents optional LED color swaps for builders who want to customize the look, plus an offer of a 3D-printed back panel from a collaborator ("lavaman").

Only a build guide and bill of materials are published on GitHub; no schematic, PCB layout, or gerber files were found in the repository, so it is not possible to reproduce the board from source alone — only to assemble one from a kit that included the parts. No pricing, production quantity, or distribution details (e.g., whether it was sold, given away, or built by request) were found in any source checked.
