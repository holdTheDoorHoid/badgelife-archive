---
title: Eggplant SAO
id: dc26-eggplant-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: Krux
summary: 'A small SAO from the team behind the Darknet Industries DEF CON 26 badge, shared as a hobbyist-grade PCB design.'
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
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
  open_source: 'yes'
  hardware_url: https://github.com/thedarknet/dc26-badge/tree/master/hardware/dc26-sao/eggplant
  firmware_url: null
  eda_tool: null
links:
- label: github.com/thedarknet/dc26-badge/tree/master/hardware/dc26-sao/eggplant
  url: https://github.com/thedarknet/dc26-badge/tree/master/hardware/dc26-sao/eggplant
  kind: repo
- label: GitHub - thedarknet/dc26-badge
  url: https://github.com/thedarknet/dc26-badge
  kind: repo
- label: 'OSH Park shared project: eggplant5 (Krux)'
  url: https://oshpark.com/shared_projects/3o0COLSK
  kind: fab
images:
  - file: assets/images/badges/dc26/eggplant-sao/522486f5b0.png
    source: "https://oshpark.com/shared_projects/3o0COLSK"
    credit: "Krux"
    caption: "Eggplant SAO PCB, top view (OSH Park render)"
  - file: assets/images/badges/dc26/eggplant-sao/b6b8eae82f.png
    source: "https://oshpark.com/shared_projects/3o0COLSK"
    credit: "Krux"
    caption: "Eggplant SAO PCB, bottom view (OSH Park render)"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: listed
sources:
- kind: url
  url: https://github.com/thedarknet/dc26-badge/tree/master/hardware/dc26-sao/eggplant
  title: Eggplant SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc26''.'
- kind: url
  url: https://github.com/thedarknet/dc26-badge
  title: 'GitHub - thedarknet/dc26-badge: Darknet Industries Badge for Defcon 26'
  accessed: '2026-09-07'
  note: 'Confirms repo is Darknet Industries'' badge project for DEF CON 26 (2018); hardware/dc26-sao/eggplant is one of the badge''s SAO designs.'
- kind: url
  url: https://github.com/krux702
  title: krux702 (Krux) on GitHub
  accessed: '2026-09-07'
  note: 'Identifies "Krux" as the GitHub user associated with the dc26-sao/eggplant design; used as the maker credit.'
- kind: url
  url: https://oshpark.com/shared_projects/3o0COLSK
  title: 'OSH Park shared project: eggplant5 by Krux'
  accessed: '2026-09-07'
  note: 'Likely fab listing for this SAO (2-layer, 1.09x2.20in board, uploaded June 2018, matching DC26 timing); supplied the two board-render images. Not fully confirmed to be the same board as the repo''s "eggplant" design since no functional description was on the page.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    Confirmed context: this is a Shitty Add-On from the hardware/dc26-sao/ directory of
    thedarknet/dc26-badge, the Darknet Industries badge repo for DEF CON 26 (2018). The
    repo directory itself only contains a schematic, board file, and BOM (no rendered
    schematic/BOM text was accessible via fetch). Attributed to GitHub user Krux, who
    also shares a same-named-era OSH Park PCB called "eggplant5" (2-layer, 1.09x2.20in,
    uploaded June 11 2018) that is probably this SAO and supplied the two images used
    here, but no page confirmed the two are identical, so tech/look/get_one fields are
    left empty rather than inferred from the OSH Park listing. No maker page, storefront,
    price, quantity, or feature description was found. GitHub issue #29 ("Darknet 7
    badge pairing") and issue #17 ("BIO Hacking quest") on the same repo suggest the
    DC26 badge platform had inter-badge and quest mechanics, but neither mentions the
    eggplant SAO by name, so nothing from them was added to this entry.
last_modified_date: '2026-09-07'
---

The Eggplant SAO is a small add-on board from the `hardware/dc26-sao/` directory of the `thedarknet/dc26-badge` GitHub repository, the open-source hardware and firmware project behind Darknet Industries' badge for DEF CON 26 (2018). The repository directory for Eggplant contains only a schematic, a board file, and a bill of materials, with no accompanying README describing its function, so nothing is known here about what the SAO does, what MCU or LEDs (if any) it carries, or how it was distributed.

The design is credited in the archive's discovery sweep to a contributor styled "Krux," who is also the GitHub user associated with the `dc26-sao/eggplant` path and separately shares an OSH Park PCB project named "eggplant5" — a small two-layer board (1.09 x 2.20 in) uploaded in June 2018, which lines up with the DC26 timeframe. That OSH Park listing is the likely source of a manufacturable board for this SAO and supplied the two board-render images attached to this entry, but no page directly states that "eggplant5" and the repository's "eggplant" SAO are the same revision, so that link should be treated as probable rather than confirmed.

No price, production quantity, availability, or feature list could be found for this item, and it is not clear whether it was ever sold or given away versus remaining a personal/hobbyist design shared alongside the DC26 badge's open-source files.
