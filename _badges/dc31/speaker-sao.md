---
title: speaker SAO
id: dc31-speaker-sao
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: Aerospace Village
  url: https://github.com/AerospaceVillage
summary: A simple switch-activated single-LED SAO made by the Aerospace Village for DEF CON 31, part of a family of SAOs alongside the crew SAO and space shuttle SAO from the same badge repo.
functions: 'Press the SPDT switch to light a single LED, powered by its own coin cell.'
look:
  colors: []
  shape: null
  themes:
  - space
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single through-hole LED, switch-activated (no microcontroller).
  display: none
  connectivity: []
  battery: coin cell
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/speaker%20SAO
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/AerospaceVillage/avBadge_2023/tree/main/speaker%20SAO
  url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/speaker%20SAO
  kind: repo
- label: AerospaceVillage/avBadge_2023 (repo root)
  url: https://github.com/AerospaceVillage/avBadge_2023
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 4).
status: listed
sources:
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/speaker%20SAO
  title: speaker SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run4-spotted); event read as ''dc31''.'
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2023
  title: 'AerospaceVillage/avBadge_2023: Aerospace Village Badge(s) for Def Con 2023'
  accessed: '2026-09-08'
  note: Repo root README confirms this repo is the Aerospace Village's DEF CON 2023 (DC31) badge family, including "a number of SAOs the Village is making."
- kind: url
  url: https://raw.githubusercontent.com/AerospaceVillage/avBadge_2023/main/speaker%20SAO/speaker-SAO.kicad_sch
  title: speaker-SAO.kicad_sch (schematic)
  accessed: '2026-09-08'
  note: Schematic shows an SPDT switch, one resistor, one LED, a coin/button cell (Battery_Cell), and a 6-pin SAO connector — a passive, MCU-less design.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-08'
  notes: >-
    Confirmed real via the maker's own GitHub repo and KiCad source files (not just a search
    snippet). No README, blog post, or press coverage names a specific price, quantity, or
    distribution method for this SAO specifically, and no photo of the assembled board could be
    found — the only image in the repo's images/ folder is a decorative "runway markings" SVG
    graphic, not a photo of the item. The "speaker" in the title likely refers to this being
    given to DEF CON 31 speakers (a guess, not confirmed by any source, so left out of the
    write-up). Gerbers and KiCad source are published, so hardware_url/open_source are filled in
    as partial (no firmware, since there is no MCU). Event/year (DEF CON 31, 2023) already
    matched the entry and needed no correction.
last_modified_date: '2026-09-08'
---

The speaker SAO is one of several small add-on boards the Aerospace Village produced for its DEF CON 31 (2023) badge, alongside a crew SAO and a space shuttle SAO from the same GitHub repository. It is a simple, microcontroller-free design: a single LED wired through an SPDT switch and a resistor, powered by its own coin cell rather than drawing power from the host badge, and it connects through a 6-pin SAO header.

No maker write-up, press coverage, or storefront listing turned up describing how many were made, what they cost, or how they were distributed — the repository's images folder contains only a decorative runway-markings graphic rather than a photo of the assembled board. The name suggests it may have been handed out to conference speakers, but nothing in the available sources confirms that, so it is left as an open question here rather than stated as fact.

## Make your own

KiCad schematic, PCB layout, and Gerber files are published in the `speaker SAO` folder of the `AerospaceVillage/avBadge_2023` repository, including a pre-zipped gerber archive (`AVspeaker2023_v1.zip`). No firmware is applicable since the board has no microcontroller.
