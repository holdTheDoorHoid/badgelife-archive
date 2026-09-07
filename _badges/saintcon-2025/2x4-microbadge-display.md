---
title: 2x4 Microbadge Display
id: saintcon-2025-2x4-microbadge-display
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2025
year: 2025
makers:
- name: Cyberm3n
  url: https://github.com/cyberm3n-org
summary: A slightly oversized SAINTCON minibadge that holds and lights up eight smaller "microbadges" in a 2x4 grid of sockets.
functions: Displays up to 8 microbadges at once, each socket lit by an onboard LED; built as the display base for Cyberm3n's 2025 "Hacker" and "1337" microbadge sets.
look:
  colors:
  - blue
  - gold
  shape: rectangle
  themes:
  - minibadge
tech:
  mcu: none
  leds:
    count: 8
    type: discrete
    note: 'Silkscreen shows ref designators D1-D8, one per microbadge socket, matching the description of LEDs soldered to the front; back of the board carries resistors R1-R4.'
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - swap
  where: 'Traded in person with the maker (Cyberm3n) at SAINTCON 2025; "Ask and/or Trade" per the minibadge listing.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/cyberm3n-org/SC_2025/tree/main/hacker1337
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=2x4%20Microbadge%20Display&year=2025
  url: https://minibadge.wiki/?search=2x4%20Microbadge%20Display&year=2025
  kind: website
- label: 'MiniBadge Wiki: 2025 badge data (JSON)'
  url: https://minibadge.wiki/2025.json
  kind: doc
- label: 'GitHub: cyberm3n-org/SC_2025 - hacker1337 (design files)'
  url: https://github.com/cyberm3n-org/SC_2025/tree/main/hacker1337
  kind: repo
images:
- file: assets/images/badges/saintcon-2025/2x4-microbadge-display/5a7d4483ca.png
  source: "https://minibadge.wiki/2025.json"
  credit: "Cyberm3n"
  caption: "2x4 Microbadge Display, front, with LEDs and micro socket headers"
- file: assets/images/badges/saintcon-2025/2x4-microbadge-display/eac20e12fa.png
  source: "https://minibadge.wiki/2025.json"
  credit: "Cyberm3n"
  caption: "2x4 Microbadge Display, back, showing resistors and pins"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- 'Related items by the same maker for SAINTCON 2025 (not this entry): Arctic Wolf Base, Arctic Wolf MicroBadge Extender Display (a 2x3 version of the same socket concept), Micro Hacker and Micro 1337 (the microbadge sets meant to plug into this display), and several other Cyberm3n minibadges/microbadges.'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=2x4%20Microbadge%20Display&year=2025
  title: 2x4 Microbadge Display
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''saintcon-2025''.'
- kind: url
  url: https://minibadge.wiki/2025.json
  title: MiniBadge Wiki 2025 data feed
  accessed: '2026-09-07'
  note: 'Underlying JSON record for this badge: description, soldering instructions/difficulty, board house (JLCPCB), category (Personal), how to acquire, rarity rating, and front/back image URLs.'
- kind: url
  url: https://github.com/cyberm3n-org/SC_2025/tree/main/hacker1337
  title: cyberm3n-org/SC_2025 - hacker1337
  accessed: '2026-09-07'
  note: 'Repo folder referenced by the soldering instructions as the source of detailed build files for this badge; confirmed to exist and be public.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Confirmed via the MiniBadge Wiki community database (minibadge.wiki), which is the maker-facing submission site for SAINTCON minibadges; the listing itself (submitted by or on behalf of Cyberm3n) is the primary source. Could not independently verify MCU/EDA tool/exact LED count beyond what the board silkscreen shows, or a firm quantity made (the wiki record lists quantityMade as 0, which likely means "not disclosed" rather than zero units). No separate maker website or storefront found; this appears to be a give-away/trade-only item, not sold.'
last_modified_date: '2026-09-07'
---

The 2x4 Microbadge Display is a SAINTCON 2025 minibadge by Cyberm3n, sized slightly larger than a standard minibadge so it can hold eight of the smaller "microbadges" that plug into it via micro socket headers, arranged in two rows of four. Each socket is lit from behind by its own LED (silkscreened D1 through D8), with resistors on the back of the board, so a fully populated display lights up all eight microbadges at once.

It was built as the display base for a companion pair of microbadge sets Cyberm3n also released that year: "Micro Hacker," four microbadges that spell out HACK using a periodic-table-style design, and "Micro 1337," a set meant to spell 1337 (ordered H-ac-k-er and 1-3-3-7 respectively when seated in the display). The badge was not sold; it was given out or traded in person at the conference. Build instructions call it an intermediate solder, involving straightening LEDs on the front, resistors on the back, and trimming/aligning micro socket headers before final assembly.

## Make your own

Detailed soldering instructions and design files are published in Cyberm3n's SAINTCON 2025 GitHub repository, under the `hacker1337` folder (https://github.com/cyberm3n-org/SC_2025/tree/main/hacker1337). The general build order given by the maker is: solder LEDs to the front of the board, solder resistors to the back, prep the micro socket headers (removing pins and cutting headers to align with the board), solder the micro socket headers in place, then solder standard pins to the minibadge.

## History

This display shares its two-row micro-socket design with a related, larger badge from the same maker that year, the Arctic Wolf MicroBadge Extender Display, which houses six microbadges in a 2x3 layout using the same socket specification (credited to designer pip801).
