---
title: CHC 2023 minibadge
id: saintcon-2023-chc-2023-minibadge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: hamster (GitHub)
  url: https://github.com/hamster
summary: 'A passive SAINTCON-style minibadge made for the Circuit Hacking Community (CHC) at SAINTCON 2023, with two LEDs on a standard MiniBadge connector.'
functions: 'No onboard logic; two LEDs light from power supplied through the host badge''s MiniBadge connector.'
look:
  colors: []
  shape: null
  themes:
  - village badge
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 'Generic LED symbols in the schematic; specific LED part/color not stated in the source files.'
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
  - village
  where: 'Distributed through the Circuit Hacking Community (CHC) village at SAINTCON 2023; no storefront or quantity found.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/hamster/SAINTCON/tree/main/CHC/2023
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/hamster/SAINTCON/tree/main/CHC/2023
  url: https://github.com/hamster/SAINTCON/tree/main/CHC/2023
  kind: repo
images:
- file: assets/images/badges/saintcon-2023/chc-2023-minibadge/df542e7a6b.jpg
  source: "https://github.com/hamster/SAINTCON/tree/main/CHC/2023"
  credit: "hamster (GitHub)"
  caption: "CHC 2023 minibadge PCB artwork/logo"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://github.com/hamster/SAINTCON/tree/main/CHC/2023
  title: CHC 2023 minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''saintcon''.'
- kind: url
  url: https://raw.githubusercontent.com/hamster/SAINTCON/main/CHC/2023/chc.kicad_sch
  title: 'chc.kicad_sch (schematic source)'
  accessed: '2026-09-07'
  note: 'Title block reads "Circuit Hacking Community Minibadge", dated 2023-09-01, rev 1.0, company SAINTCON, author @hamster. Confirms event/year and maker. Shows two Device:LED symbols, resistors, a capacitor, a test point, and a MiniBadge:MiniBadge_Simple connector footprint (no MCU) -- a passive, host-powered minibadge.'
- kind: url
  url: https://api.github.com/repos/hamster/SAINTCON/contents/CHC/2023/output
  title: 'CHC/2023/output directory listing'
  accessed: '2026-09-07'
  note: 'Contains chc-panel-1.0.zip (a fab panel of the design) and a "panel" file; no BOM, price, or quantity info published.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The repo is design-source only (KiCad files, a fab panel, and logo/layer image exports) -- no README, BOM, price, quantity, or photos of an assembled/soldered badge were found. LED color/part, price, and distribution numbers are unknown. No press coverage, storefront, or social posts were found in a web search for "CHC 2023 minibadge" or "SAINTCON Circuit Hacking Community badge".'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/chc-2023-minibadge/
---

The CHC 2023 minibadge is a small passive add-on made for the Circuit Hacking Community (CHC) village at SAINTCON 2023 by the GitHub user hamster. Its KiCad schematic title block identifies it plainly as the "Circuit Hacking Community Minibadge," dated September 2023, revision 1.0, credited to SAINTCON and @hamster.

Electrically it is simple: the schematic shows two LEDs, a couple of resistors, a capacitor, and a test point, wired to a standard SAINTCON MiniBadge connector footprint. There is no microcontroller, so the badge has no onboard logic -- it lights up using power drawn through the host badge's MiniBadge header rather than running any code of its own.

The repository holds only design files (KiCad schematic/PCB/project files, a fabrication panel for a batch of the boards, and separate PNG/AI exports of the badge's artwork by PCB layer) with no README, bill of materials, pricing, or production-quantity information, and no photos of an assembled unit. A web search turned up no press coverage or storefront listing, so availability, price, and how many were made remain unknown.

## Make your own

Hardware is fully open: KiCad schematic and PCB files (`chc.kicad_sch`, `chc.kicad_pcb`), a ready-to-fab panel (`chc-panel-1.0.kicad_pcb` and `output/chc-panel-1.0.zip`), and the artwork sources (`images/logo.ai` plus per-layer PNG exports) are all in the `CHC/2023` folder of the `hamster/SAINTCON` GitHub repository (MIT-licensed at the repo root). No firmware is involved since the board is passive.
