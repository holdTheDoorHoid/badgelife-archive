---
title: PnP Badge
id: other-pnp-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: other
year: 0
makers:
- name: securelyfitz
  url: https://github.com/securelyfitz
summary: A simple open-source practice PCB for learning to set up and run a pick-and-place (PnP) machine, not tied to any convention.
functions: Populate with 25 LEDs and 25 resistors plus a coin-cell battery holder and a switch; lighting up correctly demonstrates a successful PnP placement/reflow run.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 25
    type: discrete
    note: 25 individual LEDs, each with its own series resistor
  display: none
  connectivity: []
  battery: coin cell (battery holder in schematic)
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
  hardware_url: https://github.com/securelyfitz/pnpbadge
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/securelyfitz/pnpbadge
  url: https://github.com/securelyfitz/pnpbadge
  kind: repo
images:
- file: assets/images/badges/other/pnp-badge/a1171a7ee4.jpg
  source: https://github.com/securelyfitz/pnpbadge
  credit: Joe FitzPatrick (securelyfitz)
  caption: PnP Badge PCB render/photo
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/securelyfitz/pnpbadge
  title: PnP Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://github.com/securelyfitz
  title: securelyfitz (Joe FitzPatrick) GitHub profile
  accessed: '2026-09-07'
  note: Confirmed maker identity (Joe FitzPatrick, securinghardware.com, Portland OR); no event/con mentioned on profile.
- kind: url
  url: https://raw.githubusercontent.com/securelyfitz/pnpbadge/main/pnpbadge.kicad_sch
  title: pnpbadge.kicad_sch (raw schematic)
  accessed: '2026-09-07'
  note: Confirmed circuit contents -- 25x LED, 25x resistor, one battery cell, one SPDT switch, no MCU.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The repo's own description is "Simple badge for learning to set up and operate a PnP machine" -- it is a practice/demo PCB (25 LEDs + resistors, coin-cell battery, switch, no microcontroller) for learning pick-and-place assembly, not a badge made for a specific hacker convention. No README, license, price, quantity, or storefront was found, so those fields are left empty. Maker is Joe FitzPatrick (securelyfitz / securinghardware.com), a hardware security trainer; the board may be used in his training courses but no source confirms that. No event match found in _data/events.yml, so event is left as "other".
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/pnp-badge.glb
  method: kicad
  source_file: pnpbadge.kicad_pcb
  generated: '2026-09-10'
  bytes: 96032
---

The PnP Badge is a small open-source PCB by Joe FitzPatrick (securelyfitz), published as a bare KiCad project on GitHub. Its stated purpose is to teach someone how to set up and operate a pick-and-place (PnP) machine: the board holds 25 LEDs, each with its own resistor, plus a coin-cell battery holder and a switch, so a successful build lights up all 25 LEDs and visibly demonstrates that the PnP machine placed and reflowed every part correctly.

It is not associated with a specific hacker convention or year -- there is no README, license file, price, or distribution information in the repository, and the maker's GitHub profile does not tie it to an event. It reads as a training/demo board (likely used in FitzPatrick's hardware-hacking or PCB-assembly instruction) rather than a con badge or SAO in the usual badgelife sense.

## Make your own

The KiCad source files (`.kicad_pro`, `.kicad_sch`, `.kicad_pcb`) are published in the GitHub repository at https://github.com/securelyfitz/pnpbadge, with no separate license statement found. No Gerbers, BOM, or firmware are provided separately -- the KiCad project is the full extent of what is shared.
