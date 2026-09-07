---
title: LECCO postcard
id: hackaday-europe-2026-lecco-postcard-sao
layout: badge
parent: Hackaday Europe 2026
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: hackaday-europe-2026
year: 2026
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A postcard-style reminder-token SAO for Hackaday Europe 2026 in Lecco, Italy, needing only one LED and a 2-row SMD header; the maker notes a footprint error that requires bodging the LED on.
functions: ''
look:
  colors: []
  shape: card
  themes:
  - minimalist
  - text
tech:
  mcu: none
  leds:
    count: 1
    type: null
    note: Single LED, hand-soldered ("botched on") due to a footprint error.
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
  open_source: yes
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Lecco
  firmware_url: null
  gerbers_url: null
  bom_url: null
  eda_tool: KiCad
  license: null
  fab_url: null
  notes: KiCad project (lecco.kicad_pcb, lecco.kicad_pro) plus standalone footprint files (leccoPostcard.kicad_mod, leccoPostcard_40mm.kicad_mod) in the Lecco folder.
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/Lecco
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Lecco
  kind: repo
images: []
contact: {}
notes: []
status: announced
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Lecco
  title: Simple-Add-ons-SAO/Lecco at main
  accessed: '2026-09-07'
  note: "Design files for the LECCO postcard SAO: KiCad footprint files and a full KiCad PCB project (lecco.kicad_pcb)."
- kind: url
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/Lecco/readme.md
  title: Lecco, IT — readme.md
  accessed: '2026-09-07'
  note: "Maker's own description: a reminder token for Hackaday Europe 2026 in Lecco, Italy; needs one LED and a 2-row SMD header; footprint error means the LED has to be bodged on."
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Verified directly against the maker's own repo and the Lecco readme.md
    (fetched raw). Both confirm this is a postcard-shaped SAO made as a reminder
    token for Hackaday Europe 2026 in Lecco, Italy, part of davedarko's
    long-running "Simple-Add-ons-SAO" series (roughly 20 designs listed in the
    repo's tables, not the "25+" an earlier pass claimed - corrected). The Lecco
    readme's exact wording is "you basically need an LED and a simple 2 row SMD
    header ... but you have to botch the LED on it somehow," confirming the
    single LED, the footprint error, and the bodge note; it does not give a
    pin count, so an earlier "2x3"/v1 sao_version reading was invented and has
    been removed - `sao_version` is left blank and the summary now says "2-row"
    rather than "2x3." Fetching the folder directly (github.com/.../Lecco and
    its lecco/ subdirectory via the GitHub API) confirms real KiCad project
    files (lecco.kicad_pcb, lecco.kicad_pro, lecco.kicad_sch) plus the two
    footprint files, so `eda_tool: KiCad` and the make_your_own notes stand -
    note the repo's own top-level readme table marks this design "Eagle: yes /
    Kicad: -", which conflicts with the actual file contents; the direct file
    listing is treated as authoritative here. No pricing, quantity, distribution
    method, or availability information was published anywhere, and no photos of
    an assembled unit were found, so those fields and `images` stay empty.
    Changed `status` from `released` to `announced`: the repo and readme
    describe a finished design with production files, but nothing found confirms
    the SAO was actually assembled or handed out to anyone, which "released"
    would require.
last_modified_date: '2026-09-07'
---

The LECCO postcard is a small, deliberately minimal SAO that davedarko made as a keepsake for Hackaday Europe 2026, held in Lecco, Italy. It's part of his long-running Simple-Add-ons-SAO series — a personal catalog of around twenty small, often joke- or memory-themed add-ons made for various events. This one leans into the "postcard" idea: a card-shaped board meant as a memento of the trip rather than a feature-packed gadget.

Electrically it's about as simple as an SAO gets: one LED and a 2-row SMD header, with no microcontroller or other components called out. The maker's own readme is refreshingly candid about a mistake in the design — the LED footprint doesn't line up correctly, so anyone building the board has to hand-bodge the LED onto the pads to get it working. The joke, as davedarko notes, is that he'd previously given a talk on how to avoid exactly this kind of footprint error.

The repository provides full KiCad design files (a complete PCB project plus two versions of the card footprint, including a 40mm variant), but no pricing, production quantity, or distribution details were published, and no photos of an assembled board were found.

## Make your own

The Lecco folder in davedarko's Simple-Add-ons-SAO repository contains a complete KiCad project (`lecco.kicad_pcb`, `lecco.kicad_pro`) along with standalone footprint files (`leccoPostcard.kicad_mod` and a 40mm variant). Fabricating one requires sourcing a single LED and a 2-row SMD header, and being prepared to bodge the LED onto the board by hand due to the known footprint error.
