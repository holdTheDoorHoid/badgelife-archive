---
title: Minibadge expansion board
id: saintcon-2024-minibadge-klip-on-expansion-board
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: saintcon-2024
year: 2024
makers:
- name: compukidmike
  url: https://github.com/compukidmike
summary: A lanyard-worn accessory that came with every SAINTCON 2024 badge, adding a standard 20-pin minibadge connector with 8 slots for displaying extra minibadges.
functions: Holds and powers up to 8 minibadges for display (via the 20-pin minibadge extension connector). It draws power from the main badge's USB-C port, but is not wired to the badge's I2C bus, so minibadges plugged into it are decorative only and cannot take part in the badge's on-screen game (which only reads the two I2C-connected klip-on slots on the wrist badge itself).
look:
  colors: []
  shape: null
  themes:
  - minibadge
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: powered by host badge (via USB-C); no battery of its own
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Included with every SAINTCON 2024 official badge; not sold or distributed separately.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/compukidmike/Saintcon2024
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/compukidmike/Saintcon2024
  url: https://github.com/compukidmike/Saintcon2024
  kind: repo
  note: SAINTCON 2024 badge repo; README describes the minibadge expansion board and provides KiCad libraries/an example klip-on board.
images: []
contact: {}
notes:
- Sweep found this under the title "MiniBadge Klip-on expansion board"; the maker's own README calls it the "minibadge expansion board" and treats "klip-on" as the separate term for the screw-mounted boards on the wrist badge itself, so the title was corrected here.
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/Saintcon2024
  title: MiniBadge Klip-on expansion board
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2024/main/README.md
  title: Saintcon2024 README (compukidmike/Saintcon2024)
  accessed: '2026-09-10'
  note: 'Primary source: confirms the minibadge expansion board is an 8-slot, 20-pin-connector, lanyard-worn accessory included with every badge, USB-C powered from the main badge, with no I2C connection to the badge (so it cannot host the two "official" game minibadges).'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: No photo of the physical expansion board itself was found (the repo's only images are a joke "leaked engineering drawing" of the main wrist badge and a fictional press-release graphic, not usable as item photos, so images was left empty). Exact quantity made and whether the expansion board's own KiCad files (vs. the general 2-slot klip-on example) were published are not stated in the README. A related but distinct item, the "SAINTCON 2024 Minibadge Expansion Board Cover," has its own entry (saintcon-2024-saintcon-2024-minibadge-expansion-board-cover) and is not a duplicate of this one.
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2024/minibadge-klip-on-expansion-board.glb
  method: kicad
  source_file: Klip-ons/Saintcon2024MinibadgeKlip-onExample/Saintcon2024MinibadgeKlip-onExample.kicad_pcb
  generated: '2026-09-10'
  bytes: 59988
---

Every SAINTCON 2024 attendee badge (a wrist-mounted "Wrist Communicator" designed by compukidmike) shipped with a matching minibadge expansion board worn on a lanyard. Where the badge itself only supports two "official" game minibadges over I2C, the expansion board adds a standard 20-pin minibadge connector with room for eight minibadges at once, letting attendees show off their whole collection at the con. It draws its power from the main badge's USB-C port rather than carrying its own battery.

The expansion board is explicitly cosmetic: the README is direct that it "will NOT have I2C connected to the badge," so minibadges plugged into it light up and display but do not interact with whatever on-badge game SAINTCON ran that year. The badge team's public repo also shares KiCad libraries and footprints, along with an example two-slot "klip-on" minibadge board, so hobbyists could design their own compatible add-ons for the wrist badge, though the expansion board's own design files were not found to be published separately.

## Make your own

The compukidmike/Saintcon2024 GitHub repo's `Klip-ons` directory contains KiCad libraries (a schematic symbol for the 3V3/GND power connections and board footprints for the badge's four klip-on positions) plus a worked example minibadge klip-on project, which is the closest published starting point for building a compatible minibadge-holder accessory.
