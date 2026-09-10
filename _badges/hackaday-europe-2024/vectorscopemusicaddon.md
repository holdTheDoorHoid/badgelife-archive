---
title: VectorScopeMusicAddon
id: hackaday-europe-2024-vectorscopemusicaddon
layout: badge
parent: Hackaday Europe 2024 (Berlin)
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: hackaday-europe-2024
year: 2024
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A small open-source add-on PCB for the Hackaday Vectorscope badge (Supercon 2023 / Hackaday Europe 2024) that lets the badge display oscilloscope music.
functions: Displays oscilloscope music on the Vectorscope badge's built-in scope mode. The original version adds a physical switch to swap the X/Y axes, working around the display's inverted Y-axis; the BASIC-2 revision drops the switch after an upstream software fix rotated/mirrored the display in code instead.
look:
  colors: []
  shape: null
  themes:
  - music
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
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
  where: Design files published on GitHub; no evidence of a storefront listing or a batch built for sale. People built their own from the shared KiCad files.
make_your_own:
  open_source: true
  hardware_url: https://github.com/davedarko/VectorScopeMusicAddon
  firmware_url: null
  eda_tool: KiCad
  license: CC0-1.0
links:
- label: github.com/davedarko/VectorScopeMusicAddon
  url: https://github.com/davedarko/VectorScopeMusicAddon
  kind: repo
- label: 'Upstream fix PR (Hack-a-Day/Vectorscope #15)'
  url: https://github.com/Hack-a-Day/Vectorscope/pull/15
  kind: repo
- label: softegg/supercon-2023-badge-enclosure (companion 3D-printed case)
  url: https://github.com/softegg/supercon-2023-badge-enclosure/
  kind: repo
images:
- file: assets/images/badges/hackaday-europe-2024/vectorscopemusicaddon/3e58780e43.jpg
  source: https://github.com/davedarko/VectorScopeMusicAddon
  credit: davedarko
  caption: KiCad render of the original VectorScopeMusicAddon PCB
- file: assets/images/badges/hackaday-europe-2024/vectorscopemusicaddon/eee2441136.jpg
  source: https://github.com/davedarko/VectorScopeMusicAddon
  credit: davedarko
  caption: KiCad render of the BASIC-2 revision, redesigned with @softegg for a 3D-printed cover
contact: {}
notes:
- Open-source add-on PCB for the Hackaday Supercon 2023 / Hackaday Europe 2024 Vectorscope badge that displays oscilloscope music, with a BASIC-2 revision adding a 3D-printed cover. Found by the event-year sweep, task hackaday-europe.
status: released
sources:
- kind: url
  url: https://github.com/davedarko/VectorScopeMusicAddon
  title: VectorScopeMusicAddon
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:hackaday-europe); event read as ''hackaday-europe-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/davedarko/VectorScopeMusicAddon/master/README.md
  title: VectorScopeMusicAddon README
  accessed: '2026-09-08'
  note: Confirmed project purpose, design notes (axis-swap switch and the reason for it), the BASIC-2 revision and its 3D-printed cover, the upstream fix PR, credits, license, and the two render image URLs.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Maker''s own repo confirms this is a real, released add-on for the Hackaday Vectorscope badge (used at both Supercon 2023 and Hackaday Europe 2024) rather than a standalone badge; kept type: accessory. No price, quantity, or storefront found - it reads as a share-the-files DIY add-on rather than something sold or distributed as a batch, so get_one fields are mostly left empty/unknown. No MCU or SAO header of its own (it piggybacks on the host badge''s display). Event left as hackaday-europe-2024 per the sweep since the README names both Supercon 2023 and Hackaday Europe 2024 as the target badge; a supercon-2023 event id also exists in events.yml if this should instead be filed there.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/hackaday-europe-2024/vectorscopemusicaddon.glb
  method: kicad
  source_file: KiCad PCB files/VectorScopeMusicAddon.kicad_pcb
  generated: '2026-09-10'
  bytes: 88436
---

VectorScopeMusicAddon is a small open-source add-on PCB by davedarko for the Hackaday Vectorscope badge, the badge issued at Supercon 2023 and reused at Hackaday Europe 2024. It lets the badge display oscilloscope music by adding the level-shifting circuitry the badge's audio-in scope mode needs, wiring straight into the host badge's own screen rather than carrying a display of its own.

The original revision includes a physical switch to swap the X and Y axes, working around the badge's display having its coordinate origin in the top-left corner (which otherwise renders the scope trace upside-down). After davedarko contributed an upstream software fix (Hack-a-Day/Vectorscope PR #15) that rotates and mirrors the oscilloscope-mode display in code, a second "BASIC-2" revision dropped the switch and reworked the layout to clear the left side of the pin header, adding mounting holes so it fits a companion 3D-printed enclosure designed by @softegg (softegg/supercon-2023-badge-enclosure).

The project is released as open hardware under CC0-1.0, with KiCad source for both revisions in the GitHub repo. No evidence was found of it being sold or produced as a batch; it reads as a share-your-files community add-on rather than a commercial product, so price, quantity, and distribution details are left blank.
