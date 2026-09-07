---
title: SAINTCON 2022 badge (compukidmike)
id: saintcon-2022-saintcon-2022-badge-compukidmike
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: compukidmike
  url: https://github.com/compukidmike
summary: A "#badgelife" personal minibadge made by compukidmike for SAINTCON 2022, shaped like a flex-circuit heart with a magnet, meant to be traded and worn on the official SAINTCON badge's minibadge wings.
functions: Passive trading minibadge; no electronics function beyond the flex-circuit heart coil artwork and magnet hinge. Plugs into the two 8-pin minibadge "wings" soldered onto the official SAINTCON 2022 badge.
look:
  colors:
  - black
  - gold
  shape: heart
  themes:
  - minibadge
  - jewelry
  - village badge
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - swap
  where: Traded in person at SAINTCON 2022 as part of the con's minibadge/wing trading tradition.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/compukidmike/saintcon2022
  firmware_url: null
  eda_tool: null
links:
- label: github.com/compukidmike/saintcon2022
  url: https://github.com/compukidmike/saintcon2022
  kind: repo
images:
  - file: assets/images/badges/saintcon-2022/saintcon-2022-badge-compukidmike/9782913e87.jpg
    source: "https://github.com/compukidmike/saintcon2022"
    credit: "compukidmike"
    caption: "Minibadge kit parts: PCB, flex-circuit heart coil, magnet, resistors and headers"
  - file: assets/images/badges/saintcon-2022/saintcon-2022-badge-compukidmike/53284167b6.jpg
    source: "https://github.com/compukidmike/saintcon2022"
    credit: "compukidmike"
    caption: "Assembled minibadge showing the flex circuit wrapped around the magnet"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/saintcon2022
  title: SAINTCON 2022 badge (compukidmike)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''saintcon-2022''.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/saintcon2022/main/MinibadgeInstructions/README.md
  title: 'Compukidmike Personal Minibadge: Assembly Instructions'
  accessed: '2026-09-07'
  note: Confirms this is a personal minibadge (not the main con badge), its kit contents (PCB, flex circuit, magnet, two 51-ohm 0603 resistors, four 2-pin headers) and assembly steps.
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/saintcon2022/main/SolderingInstructions/README.md
  title: SAINTCON 2022 Badge - Wing Assembly Instructions
  accessed: '2026-09-07'
  note: Describes the official SAINTCON 2022 badge's two 8-header "wings" (4 minibadge slots each) that this and other minibadges plug into.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The repo is compukidmike's own; it documents (1) a firmware fix for the official RP2040-based SAINTCON 2022 badge, (2) assembly instructions for that badge's minibadge "wings", and (3) this entry's actual subject, a personal heart-shaped minibadge compukidmike made to trade at the con. No listed price, quantity, or exact PCB manufacturer info was found. The board reads "#badgelife 3487737 SAINTCON 2022" per the parts photo. Not the official SAINTCON 2022 attendee badge itself.
last_modified_date: '2026-09-07'
---

compukidmike's SAINTCON 2022 minibadge is a small black PCB, marked "#badgelife" and "SAINTCON 2022," carrying a heart made from a gold flex-printed coil trace. The flex circuit wraps around a magnet mounted through the board so that the heart "breathes" — it can pinch and release slightly against the magnet's pull, per the maker's own assembly notes. It's a purely mechanical/decorative piece (no LEDs, no MCU): four 2-pin headers, two 51-ohm 0603 resistors, and the flex-circuit/magnet assembly make up the whole kit.

This minibadge was made for the official SAINTCON 2022 badge, which that year shipped with two 8-header "wings" (soldered on by attendees) providing four minibadge slots each — a con-wide trading system where attendees swap personal minibadges like this one to fill out their badge's wings. compukidmike's GitHub repo bundles the minibadge assembly guide alongside the wing-soldering instructions for the main badge and a firmware fix for an LED bug on that main badge, but the repo does not include the main badge's own hardware/firmware source.

## Make your own

Hardware files (photos and a written assembly guide, not board design files) are in the maker's repo under `MinibadgeInstructions/`. The kit is: one minibadge PCB, one flex-circuit heart coil, a magnet, two 51-ohm 0603 resistors, and four 2-pin headers. Solder the resistors and header jumpers, attach one end of the flex circuit to the back of the board, wrap it around the front and solder the other end, then solder the 2-pin headers to the back and adjust the flex circuit's pinch so the heart sits about 1mm from the magnet.
