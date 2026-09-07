---
title: Stargate Badge (DC27)
id: dc27-stargate-badge-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: KeeperOfBits
  url: https://github.com/countmurphy
summary: 'A Stargate-shaped LED badge with animated chevrons and a lit "wormhole" sequence, made for DEF CON 27.'
functions: 'Blinkenlights-style animations: chevrons light in rotating clockwise/counterclockwise sequences followed by a wormhole-style lighting effect across the ring of blue LEDs.'
look:
  colors: [blue]
  shape: 'stargate ring'
  themes: [sci-fi, space, movie, tv]
tech:
  mcu: NXP KL27
  leds:
    count: 104
    type: discrete
    note: '38 side-mounted LEDs for the chevrons plus 66 blue LEDs for the ring, driven via 5x 74HC/HCT595 shift registers'
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '119'
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/countmurphy/DoorwayToHeaven
  firmware_url: https://github.com/countmurphy/DoorwayToHeaven
  eda_tool: KiCad
  license: MIT
  notes: 'Repo (DoorwayToHeaven) contains KiCad schematic/PCB files and firmware source, with build and flashing instructions in the README under software/.'
links:
- label: random-hackery.net/post/stargate
  url: https://random-hackery.net/post/stargate/
  kind: website
- label: DoorwayToHeaven (GitHub)
  url: https://github.com/countmurphy/DoorwayToHeaven
  kind: repo
images:
  - file: assets/images/badges/dc27/stargate-badge-dc27/9f8c6b259c.jpg
    source: "https://random-hackery.net/post/stargate/"
    credit: "KeeperOfBits (CountMurphy)"
    caption: "The assembled Stargate-shaped PCB badge"
  - file: assets/images/badges/dc27/stargate-badge-dc27/979724bfb5.jpg
    source: "https://random-hackery.net/post/stargate/"
    credit: "KeeperOfBits (CountMurphy)"
    caption: "Badge worn on a custom lanyard"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://random-hackery.net/post/stargate/
  title: Stargate Badge (DC27)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
- kind: url
  url: https://random-hackery.net/post/stargate/
  title: Stargate Badge - random-hackery.net
  accessed: '2026-09-07'
  note: 'Maker''s own project writeup: confirms creator (CountMurphy / KeeperOfBits), 2019 date, NXP KL27 MCU, LED counts and shift registers, 119 units made, GitHub repo, and photos of the assembled badge and lanyard.'
- kind: url
  url: https://github.com/countmurphy/DoorwayToHeaven
  title: countmurphy/DoorwayToHeaven
  accessed: '2026-09-07'
  note: 'Repo README states "This is the Stargate badge for DEF con 27"; confirms KiCad hardware files, firmware, and MIT license.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Price and sale/distribution details (whether it was sold, given away, or contest-only) were not stated on the maker''s page or repo, so get_one.price/where/distribution/availability are left empty/unknown. The badge was also featured in a Hak5 segment with Shannon Morse per the maker''s writeup, but that video was not located to verify further details.'
last_modified_date: '2026-09-07'
---

The Stargate Badge is a DEF CON 27 (2019) electronic badge shaped like the ring gate from the Stargate sci-fi franchise, made by KeeperOfBits (GitHub/Twitter handle for CountMurphy). It uses an NXP KL27 microcontroller driving 38 side-mounted LEDs for the badge's chevrons plus 66 blue LEDs around the ring, controlled through five 74HC/HCT595 shift registers. The firmware animates the chevrons in rotating sequences before lighting the ring in a "wormhole" effect, echoing the show's gate-activation sequence.

The maker built 119 units, assembled by PCBWay with only minor rework needed on most boards, and had custom lanyards made through CustomLanyard.net for wearing the badge at the con. The project picked up some outside attention at the time, reportedly reaching about 30,000 social-media views within days and appearing in a Hak5 segment with Shannon Morse.

## Make your own

Hardware and firmware are published on GitHub under the MIT license (countmurphy/DoorwayToHeaven). The repo includes KiCad schematic and PCB files (with supporting footprint libraries) and firmware source, along with build and flashing instructions in the README under the software directory.
