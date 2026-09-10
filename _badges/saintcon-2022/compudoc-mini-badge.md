---
title: CompuDoc Mini Badge
id: saintcon-2022-compudoc-mini-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: CompuDocUt
summary: A simple two-LED SAINTCON 2022 minibadge featuring the CompuDoc mascot, built as a beginner solder kit.
functions: 'No active logic: two amber LEDs and a single resistor wired across the badge''s power pins, lit whenever the badge is plugged into a powered host badge.'
look:
  colors:
  - green
  shape: rectangle
  themes:
  - mascot
  - retro computer
  - learn to solder
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Two amber surface-mount LEDs (D1/D2), wired opposite the board's + pads; no driver IC.
  display: none
  connectivity: []
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
  firmware_url: null
  eda_tool: null
links:
- label: github.com/CompuDocUt/SaintConMinibadges/blob/main/CompuDocMini%20Badge%20assembly%20instructions.pdf
  url: https://github.com/CompuDocUt/SaintConMinibadges/blob/main/CompuDocMini%20Badge%20assembly%20instructions.pdf
  kind: doc
- label: CompuDocUt/SaintConMinibadges (GitHub repo)
  url: https://github.com/CompuDocUt/SaintConMinibadges
  kind: repo
images:
  - file: assets/images/badges/saintcon-2022/compudoc-mini-badge/kit-parts.jpg
    source: "https://github.com/CompuDocUt/SaintConMinibadges/blob/main/CompuDocMini%20Badge%20assembly%20instructions.pdf"
    credit: "CompuDocUt"
    caption: "Unpopulated PCB (silkscreened with the CompuDoc mascot) alongside its resistor, two amber LEDs, and header pins"
  - file: assets/images/badges/saintcon-2022/compudoc-mini-badge/assembled.jpg
    source: "https://github.com/CompuDocUt/SaintConMinibadges/blob/main/CompuDocMini%20Badge%20assembly%20instructions.pdf"
    credit: "CompuDocUt"
    caption: "Assembled badge plugged into a host board's minibadge socket"
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'Sheet title matched the maker''s own labeling ("CompuDoc Mini Badge"); no rename needed.'
status: released
sources:
- kind: url
  url: https://github.com/CompuDocUt/SaintConMinibadges/blob/main/CompuDocMini%20Badge%20assembly%20instructions.pdf
  title: CompuDoc Mini Badge
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/CompuDocUt/SaintConMinibadges/blob/main/CompuDocMini%20Badge%20assembly%20instructions.pdf
  title: CompuDoc Mini Badge assembly instructions.pdf
  accessed: '2026-09-10'
  note: Maker's own PDF; parts list, assembly steps, and photos of the bare PCB, components, and assembled badge confirmed the item is real, its 2022 date, LED count/type, and passive (no-MCU) design.
- kind: url
  url: https://github.com/CompuDocUt/SaintConMinibadges
  title: 'CompuDocUt/SaintConMinibadges: Badges for Saintcon'
  accessed: '2026-09-10'
  note: Repo description ("Badges Created for Saintcon 2022 - details and assembly instructions") confirms event/year and lists the maker's other minibadges from the same year.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: The maker's own assembly-instructions PDF (with photos of every step) is the only source found; no storefront, price, quantity, or availability information turned up anywhere, and no separate hardware/Gerber repo was found beyond the assembly PDF, so those fields are left empty. The board silkscreen reads "2022 COMPUDOC/SHIFTY", suggesting a collaboration with or nod to fellow SAINTCON minibadge maker Shifty, but no source spells out the nature of that credit, so it isn't added to `makers`.
last_modified_date: '2026-09-10'
---

The CompuDoc Mini Badge is a SAINTCON 2022 minibadge from maker CompuDocUt, part of a small lineup that year that also included a BESD Train minibadge and a Grateful Dead minibadge. It follows the SAINTCON minibadge convention of a roughly 1-inch PCB that plugs into a full conference badge's socket header (silkscreened SDA/SCL/3.3V/GND, "3.3V circuit only") rather than carrying its own microcontroller or battery. The board's silkscreen shows a grinning computer-with-wrench mascot and the credit "2022 COMPUDOC/SHIFTY."

Electrically it is a beginner-friendly kit: one 2200-ohm resistor and two amber surface-mount LEDs (D1/D2), wired in reverse across the board's marked + pads, plus two two-pin headers so it can be soldered onto a host badge or bench-tested in a socket. There is no logic on board — the LEDs simply light whenever the badge draws power from its host, and the maker's own assembly PDF walks through orienting each part by photo, including a note on LED polarity (the green dot on the lead is the negative side).

No pricing, production quantity, or distribution channel for the badge was found; it appears only in CompuDocUt's own GitHub repository of SAINTCON minibadge build instructions, alongside the maker's other 2022-2023 minibadges.
