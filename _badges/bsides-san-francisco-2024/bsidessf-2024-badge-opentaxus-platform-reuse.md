---
title: BSidesSF 2024 badge (OpenTaxus platform reuse)
id: bsides-san-francisco-2024-bsidessf-2024-badge-opentaxus-platform-reuse
layout: badge
parent: BSides San Francisco 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-san-francisco-2024
year: 2024
makers:
- name: PDX Badgers / OpenTaxus
  url: https://github.com/pdxbadgers
  role: designed by Joe FitzPatrick (@securityfitz), published by the PDX Badgers org
summary: An RP2040 conference badge for BSidesSF 2024 running a revised version of "The Attribution Game," built on the open-source "OpenTaxus" badge platform shared with BSidesPDX 2024 and LABScon 2023.
functions: Plays "The Attribution Game," a Clue-style deduction game where attendees trade cards and self-entered alibis over IR to figure out a threat actor, attack tool, and victim each round; this version was revised from the original LABScon 2023 game for BSidesSF 2024.
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
  where: Distributed to attendees at BSidesSF 2024 (San Francisco, CA).
make_your_own:
  open_source: yes
  hardware_url: https://github.com/pdxbadgers/badge-2024
  firmware_url: https://github.com/pdxbadgers/badge-2024
  eda_tool: KiCad
  license: CC BY-SA 4.0 for hardware/software (names, logos, and artwork are separately restricted)
  notes: Same badge-2024 repo and RP2040/OLED/NeoPixel hardware as the BSidesPDX 2024 OpenTaxus badge; only the Attribution Game software/flavor text was customized per event.
links:
- label: github.com/pdxbadgers/badge-2024
  url: https://github.com/pdxbadgers/badge-2024
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'Sheet/sweep title was "BSidesSF 2024 badge (OpenTaxus platform reuse)"; kept as-is since it accurately describes the item (the repo itself does not give the BSidesSF variant a separate product name).'
status: released
sources:
- kind: url
  url: https://github.com/pdxbadgers/badge-2024
  title: BSidesSF 2024 badge (OpenTaxus platform reuse)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/pdxbadgers/badge-2024
  title: pdxbadgers/badge-2024 (OpenTaxus badge repo)
  accessed: '2026-09-10'
  note: Maker's own repo README; confirmed the Attribution Game was "designed for LABScon 2023 and then revised and improved for BSidesSF 2024," plus hardware/software details, designer, and open-source license.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'This is the same badge-2024 repository and RP2040/OLED/NeoPixel/IR hardware documented for the BSidesPDX 2024 OpenTaxus badge (id bsides-portland-2024-bsidespdx-2024-opentaxus-badge) -- the repo README confirms one shared platform reused across LABScon 2023, BSidesSF 2024, and BSidesPDX 2024, with only the game (Attribution Game vs. Trick or Treat) and flavor text differing per event. No BSidesSF-specific photo, price, or production quantity was found anywhere; the repo gives no per-event image. Event corrected from the placeholder "other" to bsides-san-francisco-2024, the matching id in _data/events.yml. Confidence kept at medium since the only source is the maker''s repo, with no independent event writeup or photo confirming the BSidesSF badges as physically distributed.'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/other/bsidessf-2024-badge-opentaxus-platform-reuse/
---

This badge was BSidesSF 2024's version of "The Attribution Game," an electronic conference badge and social deduction game built on "OpenTaxus," a permissively licensed, reusable badge platform designed by Joe FitzPatrick (@securityfitz) and published through the PDX Badgers GitHub organization. In the game, attendees trade cards ("clues") and a self-entered alibi name with each other over IR to figure out who the threat actor, attack tool, and victim are for each round -- similar in spirit to Clue. The Attribution Game was originally designed for LABScon 2023 and was, per the maker's own repository, "revised and improved for BSidesSF 2024."

The hardware is the same RP2040-based board used for the BSidesPDX 2024 "Trick or Treat" badge from the same repository: a 128x64 OLED display, two NeoPixel LEDs, a five-way directional pad, and an IR emitter/phototransistor pair, running on a single AA battery through a boost converter or over USB-C. Hardware (KiCad) and software are released under CC BY-SA 4.0, with event names, logos, and artwork carrying separate, more restrictive licenses.

No BSidesSF-specific photo, price, or production quantity could be found; the badge-2024 repository documents the platform generically rather than per-event, and (as with the sibling BSidesPDX entry) no official image of the physical badge appears to be published.
