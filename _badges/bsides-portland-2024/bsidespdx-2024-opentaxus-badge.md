---
title: BSidesPDX 2024 OpenTaxus Badge
id: bsides-portland-2024-bsidespdx-2024-opentaxus-badge
layout: badge
parent: BSidespdx 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-portland-2024
year: 2024
makers:
- name: PDX Badgers
  url: https://github.com/pdxbadgers
  role: designed by Joe FitzPatrick (@securityfitz), published by the PDX Badgers org
summary: An RP2040 conference badge for BSidesPDX 2024 with an OLED display, two NeoPixels, and an IR link for clue- and candy-trading games, built on the open-source "OpenTaxus" badge platform.
functions: Plays two IR-based social games between attendees, "The Attribution Game" (a Clue-style deduction game) and "Trick or Treat" (a virtual candy-trading game), navigated with a five-way d-pad and shown on the OLED.
look:
  colors: []
  shape: null
  themes:
  - security
  - puzzle
tech:
  mcu: RP2040
  leds:
    count: 2
    type: NeoPixel
    note: ''
  display: 128x64 OLED (I2C, SH1106 or SSD1309)
  connectivity:
  - ir
  - usb
  inputs:
  - five-way directional pad
  battery: AA battery with boost converter, or USB-C with regulator
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to attendees at BSidesPDX 2024 (Portland, OR, Oct 25-26 2024).
make_your_own:
  open_source: true
  hardware_url: https://github.com/pdxbadgers/badge-2024
  firmware_url: https://github.com/pdxbadgers/badge-2024
  eda_tool: KiCad
  license: CC BY-SA 4.0 for hardware/software (names, logos, and artwork are separately restricted)
  notes: Repo also documents OpenSCAD dock files; the "OpenTaxus" platform was reused for BSidesPDX 2024, BSidesSF 2024, and LABScon 2023.
links:
- label: badge.gallery/badges/bsidespdx-2024-opentaxus-badge
  url: https://badge.gallery/badges/bsidespdx-2024-opentaxus-badge
  kind: website
- label: github.com/pdxbadgers/badge-2024
  url: https://github.com/pdxbadgers/badge-2024
  kind: repo
images: []
contact: {}
notes:
- RP2040-based CircuitPython badge with OLED, IR trading, and NeoPixels, based on an open-source design customized for BSidesPDX 2024; discussed in a YouTube badge talk. Found by the event-year sweep, task bsides-portland.
- Spotted by a research agent while working on another entry; not yet researched.
- Sheet/sweep title was "BSidesSF 2024 badge (OpenTaxus platform reuse)"; kept as-is since it accurately describes the item (the repo itself does not give the BSidesSF variant a separate product name).
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/bsidespdx-2024-opentaxus-badge
  title: BSidesPDX 2024 OpenTaxus Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-portland); event read as ''BSidesPDX 2024''.'
- kind: url
  url: https://github.com/pdxbadgers/badge-2024
  title: pdxbadgers/badge-2024 (OpenTaxus badge repo)
  accessed: '2026-09-10'
  note: Maker's own repo; confirmed designer, hardware/firmware open-source license, games, and reuse across three 2023-2024 events.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Core facts (chip, display, LEDs, IR games, open-source status) confirmed by badge.gallery and the maker's own GitHub repo, but price, quantity made, and a photo of the physical badge were not found anywhere in the available sources -- no official image exists per badge.gallery, apparently due to artwork licensing restrictions. Confidence kept at medium rather than high because neither source is a first-person event writeup with photos. Merged with duplicate entry 'BSidesSF 2024 badge (OpenTaxus platform reuse)' (bsides-san-francisco-2024-bsidessf-2024-badge-opentaxus-platform-reuse).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/bsides-san-francisco-2024/bsidessf-2024-badge-opentaxus-platform-reuse/
model:
  file: assets/models/bsides-portland-2024/bsidespdx-2024-opentaxus-badge.glb
  method: kicad
  source_file: hardware/OpenTaxus.kicad_pcb
  generated: '2026-09-10'
  bytes: 262644
---

The OpenTaxus Badge was BSidesPDX 2024's electronic conference badge, designed by Joe FitzPatrick (@securityfitz) and published through the PDX Badgers GitHub organization. It runs on a Raspberry Pi RP2040, with a 128x64 OLED display, two NeoPixel LEDs, a five-way directional pad, and an IR emitter/phototransistor pair used for two attendee-vs-attendee games: "The Attribution Game," a Clue-style deduction game, and "Trick or Treat," a virtual candy-trading game. It can run on a single AA battery through a boost converter or over USB-C.

The badge is built on "OpenTaxus," a permissively licensed, reusable badge platform meant to give conference organizers a starting point for custom hardware badges without redesigning everything from scratch. The same platform, forked and rebranded, was also used for BSidesSF 2024 and LABScon 2023. Hardware and firmware are released under CC BY-SA 4.0 (event-specific names, logos, and artwork carry separate, more restrictive licenses), with full KiCad schematics, board files, and OpenSCAD dock files published in the badge-2024 repository.

No price, production quantity, or photo of the physical badge could be found in the sources checked; badge.gallery notes that no official image is published, likely tied to the artwork licensing.

## Notes merged from the duplicate entry "BSidesSF 2024 badge (OpenTaxus platform reuse)"

This badge was BSidesSF 2024's version of "The Attribution Game," an electronic conference badge and social deduction game built on "OpenTaxus," a permissively licensed, reusable badge platform designed by Joe FitzPatrick (@securityfitz) and published through the PDX Badgers GitHub organization. In the game, attendees trade cards ("clues") and a self-entered alibi name with each other over IR to figure out who the threat actor, attack tool, and victim are for each round -- similar in spirit to Clue. The Attribution Game was originally designed for LABScon 2023 and was, per the maker's own repository, "revised and improved for BSidesSF 2024."

The hardware is the same RP2040-based board used for the BSidesPDX 2024 "Trick or Treat" badge from the same repository: a 128x64 OLED display, two NeoPixel LEDs, a five-way directional pad, and an IR emitter/phototransistor pair, running on a single AA battery through a boost converter or over USB-C. Hardware (KiCad) and software are released under CC BY-SA 4.0, with event names, logos, and artwork carrying separate, more restrictive licenses.

No BSidesSF-specific photo, price, or production quantity could be found; the badge-2024 repository documents the platform generically rather than per-event, and (as with the sibling BSidesPDX entry) no official image of the physical badge appears to be published.
