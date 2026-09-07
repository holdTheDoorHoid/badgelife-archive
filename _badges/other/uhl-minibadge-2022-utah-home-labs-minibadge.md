---
title: UHL-minibadge-2022 — Utah Home Labs Minibadge
id: other-uhl-minibadge-2022-utah-home-labs-minibadge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: other
year: 2022
makers:
- name: James Carbine (klipperx / Utah Home Labs)
  url: https://github.com/klipperx
summary: A small stackable minibadge for the Utah Home Labs community, following the SAINTCON minibadge hardware standard.
functions: 'Passive: four LEDs light up when powered through the minibadge''s edge-connector pins. No microcontroller or interactive behavior.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: Each LED wired in series with its own resistor, straight across the power rail supplied through the minibadge's edge pins; no driver IC.
  display: none
  connectivity: []
  battery: null
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
  hardware_url: https://github.com/klipperx/UHL-minibadge-2022
  firmware_url: null
  eda_tool: null
  notes: 'Repo published under MIT license (James Carbine, 2022) but contains only a hand-drawn schematic image (drawio export), not a full KiCad project, Gerbers, or BOM. EDA tool used is not stated anywhere in the repo.'
links:
- label: github.com/klipperx/UHL-minibadge-2022
  url: https://github.com/klipperx/UHL-minibadge-2022
  kind: repo
images: []
contact: {}
notes:
- 'Maker''s other repos include "minibadge-kicad-template" (described as "A Kicad Template for the Saintcon Minibadge") and separate "saintcon2023" / "Saintcon2025" projects, suggesting this maker builds SAINTCON-format minibadges regularly, but no source directly ties UHL-minibadge-2022 itself to a specific SAINTCON year.'
status: listed
sources:
- kind: url
  url: https://github.com/klipperx/UHL-minibadge-2022
  title: UHL-minibadge-2022 — Utah Home Labs Minibadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://raw.githubusercontent.com/klipperx/UHL-minibadge-2022/main/README.md
  title: UHL-minibadge-2022 README
  accessed: '2026-09-07'
  note: 'Confirms name "Utah Home Labs Minibadge for 2022"; no further detail in the README.'
- kind: url
  url: https://raw.githubusercontent.com/klipperx/UHL-minibadge-2022/main/LICENSE
  title: UHL-minibadge-2022 LICENSE
  accessed: '2026-09-07'
  note: 'MIT license, copyright James Carbine 2022 — gives the maker''s real name.'
- kind: url
  url: https://raw.githubusercontent.com/klipperx/UHL-minibadge-2022/main/Circuit_Diagram_A.drawio.png
  title: UHL-minibadge-2022 circuit diagram
  accessed: '2026-09-07'
  note: 'Schematic shows 4 LEDs, each with a series resistor, wired to power/ground across an 8-pad edge connector (4 pairs of pads) — a simple passive lighting circuit, no MCU. Diagram only, not a photo of the item, so not saved as an image.'
- kind: url
  url: https://github.com/klipperx?tab=repositories
  title: klipperx GitHub repositories
  accessed: '2026-09-07'
  note: 'Lists "minibadge-kicad-template" ("A Kicad Template for the Saintcon Minibadge"), a repo authored by klipperx himself. The "saintcon2023" and "Saintcon2025" repos on this account are forks of compukidmike/saintcon2023 and compukidmike/Saintcon2025, not klipperx''s own work, so they are weaker evidence of the maker building SAINTCON minibadges directly. None of these pages state that UHL-minibadge-2022 itself was distributed at a SAINTCON event.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all 5 cited sources and the circuit diagram image directly. Repo file listing (README, LICENSE, Circuit_Diagram_A.drawio.png only, verified via GitHub API) confirms no KiCad project, Gerbers, or BOM exists, so make_your_own.eda_tool was blanked (previously guessed as "KiCad" with no supporting source). The circuit diagram was opened directly and shows exactly 4 LED symbols, each in series with one resistor, across an 8-pad edge connector with shared power/ground rails — matching tech.leds and the body text. One correction to the prior researcher''s inference: two of klipperx''s "other SAINTCON minibadge" repos ("saintcon2023", "Saintcon2025") are forks of compukidmike''s repos, not klipperx''s own work — only "minibadge-kicad-template" is actually his. This weakens (but does not eliminate) the circumstantial case for type=minibadge, which now rests mainly on the repo''s own name and the 8-pad edge-connector schematic matching the known SAINTCON minibadge form factor. No maker statement ties this board to a specific convention; event correctly left as "other". No price, quantity, or availability information exists in the repo. No photos of the physical board exist, only the schematic, so images remains empty, correctly.'
last_modified_date: '2026-09-07'
---

The UHL-minibadge-2022 is a small stackable minibadge made by James Carbine (GitHub handle klipperx) for the Utah Home Labs community in 2022. It follows the SAINTCON minibadge hardware standard — a small board with an edge connector that plugs into a larger minibadge-compatible badge or holder — and its only published schematic shows a purely passive circuit: four LEDs, each with its own current-limiting resistor, wired directly across the power and ground rails supplied through the connector. There is no microcontroller, so the badge simply lights its four LEDs whenever it is powered; it has no interactive functions.

The project is released under the MIT license, but the GitHub repository contains only that one schematic image, a README with the badge's name, and the license file — no full KiCad project, Gerbers, bill of materials, or photos of a finished board. The maker's other repositories include a "Kicad Template for the Saintcon Minibadge" and dedicated SAINTCON 2023 and 2025 badge projects, which suggests this maker was a regular builder of SAINTCON-format minibadges, but nothing in the available sources directly states that the UHL-minibadge-2022 itself was distributed at SAINTCON or any other named convention. No pricing, production quantity, or availability information could be found.
