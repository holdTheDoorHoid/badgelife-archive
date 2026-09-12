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
summary: A small SAO from the team behind the Darknet Industries DEF CON 26 badge, shared as a hobbyist-grade PCB design.
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
  open_source: partial
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
  archived: https://web.archive.org/web/20260907115647/https://github.com/thedarknet/dc26-badge
- label: 'OSH Park shared project: eggplant5 (Krux)'
  url: https://oshpark.com/shared_projects/3o0COLSK
  kind: fab
images:
- file: assets/images/badges/dc26/eggplant-sao/522486f5b0.png
  source: https://oshpark.com/shared_projects/3o0COLSK
  credit: Krux
  caption: Eggplant SAO PCB, top view (OSH Park render)
- file: assets/images/badges/dc26/eggplant-sao/b6b8eae82f.png
  source: https://oshpark.com/shared_projects/3o0COLSK
  credit: Krux
  caption: Eggplant SAO PCB, bottom view (OSH Park render)
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
  note: Confirms repo is Darknet Industries' badge project for DEF CON 26 (2018); hardware/dc26-sao/eggplant is one of the badge's SAO designs.
  archived: https://web.archive.org/web/20260907115647/https://github.com/thedarknet/dc26-badge
- kind: url
  url: https://github.com/krux702
  title: krux702 (Krux) on GitHub
  accessed: '2026-09-07'
  note: Identifies "Krux" as the GitHub user associated with the dc26-sao/eggplant design; used as the maker credit.
  archived: https://web.archive.org/web/20251012221510/https://github.com/krux702
- kind: url
  url: https://oshpark.com/shared_projects/3o0COLSK
  title: 'OSH Park shared project: eggplant5 by Krux'
  accessed: '2026-09-07'
  note: Likely fab listing for this SAO (2-layer, 1.09x2.20in board, uploaded June 2018, matching DC26 timing); supplied the two board-render images. Not fully confirmed to be the same board as the repo's "eggplant" design since no functional description was on the page.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-checked 2026-09-07: all four cited sources were re-fetched and support what is claimed from them. The thedarknet/dc26-badge repo is confirmed as the Darknet Industries DEF CON 26 (2018) badge project; the hardware/dc26-sao/eggplant directory is confirmed to contain only eggplant.sch, eggplant.brd, and eggplant-BOM.xls, with no README, matching the body''s claim that no function/MCU/LED info exists there. GitHub user krux702 is confirmed to have thedarknet/dc26-badge as a pinned repo, supporting the maker attribution. The OSH Park "eggplant5" listing is confirmed to match the stated dimensions (1.09x2.20in, 2-layer, uploaded June 11 2018) and to carry no DC26/SAO/function description, so the entry''s existing hedge (probable match, not confirmed identical to the repo''s "eggplant") stands and was not strengthened. One field was corrected on fact-check: make_your_own.open_source was ''yes'' but only hardware files are published and no firmware exists or is linked (tech.mcu is
    unknown, not confirmed "none"), so per the guide''s yes-requires-both rule this was changed to ''partial''. No sentence or field was found unsupported or contradicted otherwise; confidence stays low because no source describes the SAO''s actual function, price, or distribution.'
last_modified_date: '2026-09-11'
model:
  file: assets/models/dc26/eggplant-sao.glb
  method: kicad
  source_file: eggplant.brd
  generated: '2026-09-11'
  bytes: 46128
---

The Eggplant SAO is a small add-on board from the `hardware/dc26-sao/` directory of the `thedarknet/dc26-badge` GitHub repository, the open-source hardware and firmware project behind Darknet Industries' badge for DEF CON 26 (2018). The repository directory for Eggplant contains only a schematic, a board file, and a bill of materials, with no accompanying README describing its function, so nothing is known here about what the SAO does, what MCU or LEDs (if any) it carries, or how it was distributed.

The design is credited in the archive's discovery sweep to a contributor styled "Krux," who is also the GitHub user associated with the `dc26-sao/eggplant` path and separately shares an OSH Park PCB project named "eggplant5" — a small two-layer board (1.09 x 2.20 in) uploaded in June 2018, which lines up with the DC26 timeframe. That OSH Park listing is the likely source of a manufacturable board for this SAO and supplied the two board-render images attached to this entry, but no page directly states that "eggplant5" and the repository's "eggplant" SAO are the same revision, so that link should be treated as probable rather than confirmed.

No price, production quantity, availability, or feature list could be found for this item, and it is not clear whether it was ever sold or given away versus remaining a personal/hobbyist design shared alongside the DC26 badge's open-source files.
