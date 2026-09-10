---
title: LAN TAP (BSidesDFW 2018 Badge)
id: bsidesdfw-2018-lan-tap-bsidesdfw-2018-badge
layout: badge
parent: BSides Dfw 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsidesdfw-2018
year: 2018
makers:
- name: gowenrw / alt_bier (based on Michael Ossmann's Throwing Star LAN TAP)
summary: The official BSidesDFW 2018 conference badge, a fully passive network tap adapted from Michael Ossmann's open-source Throwing Star LAN TAP design.
functions: Functions as a real passive Ethernet LAN tap; no active electronics, just RJ45 connectors and capacitors wired to mirror traffic between two ports.
look:
  colors:
  - red
  - black
  - blue
  - green
  shape: null
  themes:
  - security
  - hardware tool
  - radio
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given out as the conference badge at BSidesDFW 2018; color indicated attendee/staff/speaker/sponsor status.
make_your_own:
  open_source: true
  hardware_url: https://github.com/gowenrw/BSidesDFW_2018_Badge
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/gowenrw/BSidesDFW_2018_Badge
  url: https://github.com/gowenrw/BSidesDFW_2018_Badge
  kind: repo
- label: altbier.us/HHV2018/Making_Badgelife_The_BSidesDFW_9_Badge-v1.pdf
  url: https://altbier.us/HHV2018/Making_Badgelife_The_BSidesDFW_9_Badge-v1.pdf
  kind: website
- label: altbier.us
  url: https://altbier.us/
  kind: website
images:
- file: assets/images/badges/bsidesdfw-2018/lan-tap-bsidesdfw-2018-badge/532830a7f4.jpg
  source: https://github.com/gowenrw/BSidesDFW_2018_Badge
  credit: gowenrw
  caption: Assembled red LAN TAP badge with RJ45 connectors
- file: assets/images/badges/bsidesdfw-2018/lan-tap-bsidesdfw-2018-badge/8a4b234620.jpg
  source: https://github.com/gowenrw/BSidesDFW_2018_Badge
  credit: gowenrw
  caption: Photo of the finished BSidesDFW 2018 LAN TAP badge
contact: {}
notes:
- Official BSidesDFW 2018 conference badge, a Texas-star-shaped passive LAN tap (4x RJ45 connectors, 2x 220pF caps) adapted from Ossmann's Throwing Star design, in color variants for attendee/staff/speaker/sponsor. Found by the event-year sweep, task bsides-bsidesdfw.
status: listed
sources:
- kind: url
  url: https://github.com/gowenrw/BSidesDFW_2018_Badge
  title: LAN TAP (BSidesDFW 2018 Badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsidesdfw); event read as ''BSides DFW 2018''.'
- kind: url
  url: https://github.com/gowenrw/BSidesDFW_2018_Badge
  title: gowenrw/BSidesDFW_2018_Badge README and images
  accessed: '2026-09-10'
  note: Confirmed maker, event/year, LAN tap function, BOM (4x RJ45, 2x 220pF caps), open KiCad source, and that colors (red/black/blue/green) distinguish attendee/staff/speaker/sponsor badges.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Maker's own GitHub repo confirms all core facts. The linked altbier.us PDF (a Hardware Hacking Village talk deck) could not be parsed as text via WebFetch, so it was not used as a source beyond what the repo already confirms. No price, quantity made, or PCB shape/outline description found in any source, so those fields are left empty. look.shape left null since no source describes the board outline (the entry notes call it "Texas-star-shaped" from the sweep, but this was not independently confirmed and so was not carried into look.shape).
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsidesdfw-2018/lan-tap-bsidesdfw-2018-badge.glb
  method: kicad
  source_file: BSidesDFW_2018_Badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 254712
---

The LAN TAP was the official conference badge for BSidesDFW 2018, designed by gowenrw (Twitter: @alt_bier). Rather than an electronic blinky badge, it is a fully passive hardware hacking tool: a direct adaptation of Michael Ossmann's open-source Throwing Star LAN TAP, built from four RJ45 jacks and two 220pF capacitors with no active components. Assembled, it works as a real Ethernet tap that can mirror traffic passing between two ports.

Badges were produced in at least four PCB colors — red, black, blue, and green — used to distinguish attendee, staff, speaker, and sponsor badges from each other; attendees received the red version.

## Make your own

The maker published the complete KiCad project on GitHub, including schematic, PCB layout, gerbers, a bill of materials, datasheets, and 3D models. Building one requires sourcing 4x Amphenol RJ45 connectors (RJHSE-5080 unshielded or RJHSE-5380 shielded) and 2x 220pF through-hole capacitors, then having the gerbers fabricated or ordering the boards.
