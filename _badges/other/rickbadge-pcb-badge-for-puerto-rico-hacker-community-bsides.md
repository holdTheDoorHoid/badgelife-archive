---
title: RickBadge — PCB Badge for Puerto Rico hacker community BSides
id: other-rickbadge-pcb-badge-for-puerto-rico-hacker-community-bsides
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2019
makers:
- name: soynerdito
  url: https://github.com/soynerdito
summary: A Rick-and-Morty-themed PCB badge designed by soynerdito for the Puerto Rico hacker community, made for a BSides Puerto Rico "#BadgeLife" event.
functions: Lights 8 LEDs driven through a 74HC164 shift register from an ATtiny13A microcontroller.
look:
  colors:
  - blue
  shape: null
  themes:
  - pop culture
  - tv
  - security
tech:
  mcu: ATtiny13A-SU
  leds:
    count: 8
    type: discrete
    note: Driven via a 74164 8-bit serial-to-parallel shift register rather than addressable LEDs.
  display: none
  connectivity: []
  battery: CR2032
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
  hardware_url: https://github.com/soynerdito/RickBadge
  firmware_url: null
  eda_tool: KiCad
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/soynerdito/RickBadge
  title: RickBadge — PCB Badge for Puerto Rico hacker community BSides
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''BSides Puerto Rico''.'
- kind: url
  url: https://github.com/soynerdito/RickBadge
  title: soynerdito/RickBadge GitHub repository
  accessed: '2026-09-07'
  note: 'README and repo contents: describes a Rick-and-Morty-themed PCB badge for the Puerto Rico hacker community #BadgeLife BSides; ATtiny13A-SU + 74164 shift register driving 8 LEDs, CR2032 battery; KiCad source files named "Badge2019", commits dated March-June 2019; author notes the circuit "has never been tested" as of publication.'
images:
- file: assets/images/badges/other/rickbadge-pcb-badge-for-puerto-rico-hacker-community-bsides/4cfb31026d.jpg
  source: https://github.com/soynerdito/RickBadge
  credit: soynerdito
  caption: 3D render of the RickBadge PCB, front view
- file: assets/images/badges/other/rickbadge-pcb-badge-for-puerto-rico-hacker-community-bsides/49a1e32c7b.jpg
  source: https://github.com/soynerdito/RickBadge
  credit: soynerdito
  caption: 3D render of the RickBadge PCB, back view
contact: {}
links:
- label: github.com/soynerdito/RickBadge
  url: https://github.com/soynerdito/RickBadge
  kind: repo
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No "BSides Puerto Rico" event exists in events.yml, so event is left as other; the con is BSides Puerto Rico (BSidesPR), and the KiCad project files are named "Badge2019" with all commits dated March-June 2019, indicating it was made for the 2019 event. No pricing, quantity, or availability information was published anywhere found; the maker states in the repo that the circuit "has never been tested," so it is unclear whether it was ever fabricated or distributed at the con. No dedicated firmware repository was found (make_your_own.open_source set to partial since only hardware/KiCad files are published).
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/rickbadge-pcb-badge-for-puerto-rico-hacker-community-bsides.glb
  method: kicad
  source_file: Badge2019.kicad_pcb
  generated: '2026-09-10'
  bytes: 344984
---

RickBadge is a Rick-and-Morty-themed PCB badge designed by soynerdito, a member of the Puerto Rico hacker community, for a BSides Puerto Rico "#BadgeLife" event. The board is built around an ATtiny13A-SU microcontroller paired with a 74164 8-bit serial-to-parallel shift register, which drives 8 discrete LEDs; power comes from a CR2032 coin cell. The KiCad project files in the repository are named "Badge2019," and all commits to the repo fall between March and June 2019, indicating it was made for that year's event.

The hardware design (schematic and PCB layout) is published on GitHub in KiCad format, but no firmware source is included in the repository. The maker notes in the project documentation that, as of publication, "the circuit has never been tested," so it is unclear whether any boards were actually fabricated, assembled, or handed out at BSides Puerto Rico. No pricing, production quantity, or availability information was found in the repository or elsewhere.

## Make your own

The KiCad schematic and PCB files (`Badge2019.sch`, `Badge2019.kicad_pcb`, and supporting library files) are available in the [GitHub repository](https://github.com/soynerdito/RickBadge). No firmware source or bill of materials is published alongside the hardware files.
