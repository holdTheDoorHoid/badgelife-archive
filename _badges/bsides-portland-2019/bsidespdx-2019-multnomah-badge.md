---
title: BSidesPDX 2019 Multnomah Badge
id: bsides-portland-2019-bsidespdx-2019-multnomah-badge
layout: badge
parent: BSidespdx 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-portland-2019
year: 2019
makers:
- name: PDX Badgers
  url: https://github.com/pdxbadgers
summary: An ATtiny85-based LED badge for BSidesPDX 2019, named for Multnomah Falls, with two independently PWM-driven banks of blue LEDs.
functions: 'No buttons or interaction: on power-up it runs a fixed animation, cross-fading two banks of LEDs through sine/cosine-shaped PWM brightness curves.'
look:
  colors:
  - blue
  shape: null
  themes:
  - nature
tech:
  mcu: ATtiny85
  leds:
    count: 24
    type: reverse-mount
    note: 24 blue 1206 side-view LEDs, driven as two PWM channels (D1-D24 per the BoM)
  display: none
  connectivity: []
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given out at BSidesPDX 2019 (Portland, OR, Oct 25-26 2019); no storefront or per-unit price found.
make_your_own:
  open_source: true
  hardware_url: https://github.com/pdxbadgers/badge-2019
  firmware_url: https://github.com/pdxbadgers/badge-2019/blob/master/multnomah.ino
  eda_tool: KiCad
links:
- label: badge.gallery/badges/bsidespdx-2019-multnomah-badge
  url: https://badge.gallery/badges/bsidespdx-2019-multnomah-badge
  kind: website
- label: github.com/pdxbadgers/badge-2019
  url: https://github.com/pdxbadgers/badge-2019
  kind: repo
images: []
contact: {}
notes:
- ATtiny85 LED conference badge named "Multnomah" for BSidesPDX 2019. Found by the event-year sweep, task bsides-portland.
- Sweep's title matched the maker's own naming; no change needed.
- The repo README frames "Multnomah Falls" as one of four badge-art ideas floated ("Victorian Belle shape", "Flaming bagpipe on unicycle", "Boat", "Multnomah Falls"), alongside a target of 600 units and a sub-$15 BOM; the KiCad/BOM/firmware files are specifically named multnomah.*, so this was the design that was actually built, not just a pitch.
- No photo of the physical badge was found on badge.gallery, in the repo, or via search; images left empty.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/bsidespdx-2019-multnomah-badge
  title: BSidesPDX 2019 Multnomah Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-portland); event read as ''BSidesPDX 2019''.'
- kind: url
  url: https://github.com/pdxbadgers/badge-2019
  title: GitHub - pdxbadgers/badge-2019
  accessed: '2026-09-10'
  note: Confirms maker, event framing (600 badges, sub-$15 BOM), and that Multnomah was the named/built design with KiCad, BOM, and firmware files.
- kind: url
  url: https://raw.githubusercontent.com/pdxbadgers/badge-2019/master/multnomah.ino
  title: multnomah.ino
  accessed: '2026-09-10'
  note: Firmware source confirms ATtiny85, two PWM outputs, sine/cosine cross-fade animation with no inputs.
- kind: url
  url: https://raw.githubusercontent.com/pdxbadgers/badge-2019/master/BoM.csv
  title: BoM.csv
  accessed: '2026-09-10'
  note: Confirms parts list — ATtiny85, 24x 1206 blue side-view LEDs, DPDT slide switch, CR2032 holder.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Core hardware/firmware facts are confirmed straight from the maker's own GitHub repo (pdxbadgers/badge-2019), so those are solid. Price, exact quantity made, and distribution details (was it free with registration, con badge, or extra?) were not stated anywhere found, so those fields stay empty/unknown. No photo of an assembled badge turned up on badge.gallery, in the repo, or via search — confidence is medium rather than high mainly for that gap and the unconfirmed price/quantity.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsides-portland-2019/bsidespdx-2019-multnomah-badge.glb
  method: kicad
  source_file: multnomah.kicad_pcb
  generated: '2026-09-10'
  bytes: 282420
---

The Multnomah badge was PDX Badgers' conference badge for BSidesPDX 2019 in Portland, Oregon, named after the well-known waterfall east of the city. It runs on an ATtiny85 with no buttons or sensors: the firmware sweeps a floating-point angle through a full circle and writes `sin`/`cos`-derived brightness values to two PWM pins, cross-fading two banks of 24 blue 1206 side-view LEDs against each other in a continuous loop. Power comes from a single CR2032 cell behind a DPDT slide switch.

The project's GitHub README frames "Multnomah Falls" as one of several badge-art concepts under consideration (alongside a Victorian Belle shape, a flaming bagpipe on a unicycle, and a boat) for a run the team was targeting at 600 units with a bill of materials under $15. The repository's actual KiCad schematic, PCB, and Arduino firmware are all named for Multnomah specifically, indicating it's the concept that went into production rather than one that was set aside.

Hardware (KiCad project, footprints, BOM) and firmware are both published in the `pdxbadgers/badge-2019` repository. No photo of an assembled unit, price, or confirmed production quantity was found in the sources checked.
