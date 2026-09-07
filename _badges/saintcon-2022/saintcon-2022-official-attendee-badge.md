---
title: SAINTCON 2022 official attendee badge
id: saintcon-2022-saintcon-2022-official-attendee-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: saintcon-2022
year: 2022
makers:
- name: compukidmike
  url: https://github.com/compukidmike
summary: 'The official SAINTCON 2022 attendee badge: an RP2040-based badge with two solderable minibadge "wing" expansions, each holding four minibadges, plus a built-in minibadge slot.'
functions: 'Runs a "find clues and collect minibadges" activity: attendees solder on two wing boards (4 minibadge slots each) and a main minibadge slot, then collect and plug in minibadges found around the con. A SELECT button plus USB is used to enter firmware-update (UF2 bootloader) mode.'
look:
  colors: []
  shape: null
  themes:
  - kit
  - learn to solder
  - village badge
tech:
  mcu: RP2040
  leds: null
  display: null
  connectivity: []
  battery: 2x AA or micro USB (switch-selectable)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to SAINTCON 2022 attendees as their conference badge.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/compukidmike/saintcon2022/blob/main/Saintcon2022BadgeFirmwareFix.uf2
  eda_tool: null
links:
- label: compukidmike/saintcon2022 (wing-assembly instructions and a firmware fix, not the full badge source)
  url: https://github.com/compukidmike/saintcon2022
  kind: repo
images:
- file: assets/images/badges/saintcon-2022/saintcon-2022-official-attendee-badge/3538e4e917.jpg
  source: "https://github.com/compukidmike/saintcon2022"
  credit: "compukidmike"
  caption: "SAINTCON 2022 official attendee badge with both minibadge wings soldered on"
- file: assets/images/badges/saintcon-2022/saintcon-2022-official-attendee-badge/98a3de4eba.jpg
  source: "https://github.com/compukidmike/saintcon2022"
  credit: "compukidmike"
  caption: "SAINTCON 2022 badge minibadge slot with a minibadge attached"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/saintcon2022
  title: compukidmike/saintcon2022
  accessed: '2026-09-07'
  note: 'Repo README, SolderingInstructions/README.md, and firmware-fix filename confirm RP2040 (RPI-RP2 UF2 drive), two solderable minibadge "wing" boards (4 slots each), and a built-in minibadge slot; also supplied the two images used.'
- kind: url
  url: https://github.com/compukidmike?tab=repositories
  title: compukidmike repositories
  accessed: '2026-09-07'
  note: 'Confirms compukidmike has authored a SAINTCON badge-related repo for most years 2017-2025, including saintcon2022.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    The linked repo (by compukidmike, a recurring SAINTCON badge contributor) only
    contains minibadge wing-assembly instructions and a firmware fix, not the
    badge's own hardware/firmware source or a full spec sheet; the actual
    designer/maker of the badge PCB itself was not identified, so makers lists the
    repo author rather than a confirmed designer. LED count/type, display,
    connectivity, SAO header version, price, and quantity made were not stated
    anywhere found. A companion repo, CompuDocUt/SaintConMinibadges, and
    then3rd/rad-badge cover third-party minibadges for the same slots but are not
    the attendee badge itself.
last_modified_date: '2026-09-07'
---

The SAINTCON 2022 official attendee badge is an RP2040-based badge built around SAINTCON's long-running "minibadge" collecting game: each badge ships with two panelized "wing" boards that attendees solder on themselves, giving four minibadge slots per wing plus one slot built into the badge itself. Assembly instructions distributed by compukidmike (a recurring contributor to SAINTCON's badge program across multiple years) walk attendees through soldering 1x8 headers and 3x1 pins so the two wings mirror each other correctly before separating the panelized boards.

The badge is powered by two AA batteries or micro USB, selectable with a physical switch, and can be re-flashed by holding its SELECT button while plugging in USB to expose an RPI-RP2 UF2 drive — confirming the RP2040 microcontroller. A firmware update distributed in the same repo fixed an issue where the badge's LEDs failed to light up.

No hardware source, BOM, LED specification, display, or pricing/quantity information for the badge itself was found; the linked GitHub repository documents only the wing-soldering process and the firmware fix, not the underlying board design.

## Make your own

No hardware files for the badge board were found. The firmware fix binary (`Saintcon2022BadgeFirmwareFix.uf2`) is available in the repo and is applied by holding SELECT while connecting USB, then copying the file to the RPI-RP2 drive that appears.
