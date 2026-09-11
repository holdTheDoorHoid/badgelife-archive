---
title: DC321 SAO and DC321-2 SAO
id: bsides-orlando-2023-dc321-sao-and-dc321-2-sao-dc321-sao-kicad-pcb-dc321-2-sao-ki
layout: badge
parent: 'BSides Orlando 2023: Rise of the Robots'
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: bsides-orlando-2023
year: 2023
makers:
- name: Jose Rodriguez
  url: https://github.com/joehacksalot
summary: A pair of KiCad SAO board designs for DC321 (a Florida DEF CON group based on Florida's Space Coast, not Orlando), included in the design-file repo for the BSides Orlando 2023 "Rise of the Robots" badge.
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
  hardware_url: https://github.com/bsidesorlando/2023-badge/tree/main/bsidesorl-v1
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bsidesorlando/2023-badge/tree/main/bsidesorl-v1
  url: https://github.com/bsidesorlando/2023-badge/tree/main/bsidesorl-v1
  kind: repo
  archived: https://web.archive.org/web/20250920161441/https://github.com/bsidesorlando/2023-badge/tree/main/bsidesorl-v1
images: []
contact: {}
notes:
- 'Sweep''s original title carried the raw filenames: "DC321 SAO and DC321-2 SAO (dc321-sao.kicad_pcb, dc321-2-sao.kicad_pcb)"; shortened here to the plain name.'
status: listed
sources:
- kind: url
  url: https://github.com/bsidesorlando/2023-badge/tree/main/bsidesorl-v1
  title: DC321 SAO and DC321-2 SAO (dc321-sao.kicad_pcb, dc321-2-sao.kicad_pcb)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
  archived: https://web.archive.org/web/20250920161441/https://github.com/bsidesorlando/2023-badge/tree/main/bsidesorl-v1
- kind: url
  url: https://github.com/bsidesorlando/2023-badge/commits/main/bsidesorl-v1
  title: Commit history for bsidesorl-v1
  accessed: '2026-09-10'
  note: Identifies Jose Rodriguez (GitHub login joehacksalot) as the author of the folder's commits (introduction, introduced additional sao, added 561), which include the two DC321 files.
- kind: url
  url: https://github.com/joehacksalot
  title: joehacksalot (Jose E. Rodriguez) - GitHub profile
  accessed: '2026-09-10'
  note: Confirms the commit author's identity and that he is a self-described badgelife maker and Director at bsidesorlando.
  archived: https://web.archive.org/web/20260223041908/https://github.com/joehacksalot
- kind: url
  url: https://forum.defcon.org/node/250963
  title: DC321 September Meetup - DEF CON Forums
  accessed: '2026-09-10'
  note: Confirms DC321/DCG321 is DEF CON Group Space Coast (Melbourne/Brevard County, FL), not an Orlando group; corrects the entry's original "Orlando-area" description.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: 'Confirmed via the GitHub API on the maker''s own repo: dc321-sao.kicad_pcb and dc321-2-sao.kicad_pcb live in bsidesorlando/2023-badge under bsidesorl-v1, alongside sibling SAO designs named dc239-sao, dc407-sao, bsidesorl-otgg-sao, bsidesorl-staff-sao, bsidesorl-sponsor-sao, bsidesorl-speaker-sao, and iwc-iron-sao, all part of the BSides Orlando 2023 badge project. No README, product page, photo, or press coverage of the DC321 SAO specifically was found, only the raw KiCad PCB/project files, so most technical and distribution fields (MCU, LEDs, colors, price, quantity, availability, and look/theme) could not be confirmed and are left empty. The repo''s own file/text content gave no maker name for the SAO itself beyond generic "LOGO"/"SAO" silkscreen labels; attribution to Jose Rodriguez comes from git commit authorship on the folder (GitHub login joehacksalot, whose profile confirms he is a self-described badgelife maker and Director at bsidesorlando), not a byline on the design.
    Event was corrected from "other" to bsides-orlando-2023 since the repo is explicitly the 2023 "Rise of the Robots" badge project. Fact-checking pass corrected a factual error: DC321 is NOT an Orlando-area group as the prior draft said — DEF CON forum records identify DCG321/DC321 as "DCG Space Coast" (SpaceCoastSec), based in Melbourne, FL (Brevard County); DC407 is the actual Orlando DEF CON group. Also removed two unsupported invented labels from the body/summary: "OTGG hat" (no source calls it a hat; it is just another "-sao" file like the rest) and "Iron Widow Challenge" as the expansion of "iwc-iron" (no source gives this board a full name; only the bare filename is confirmed). The "hardware tool" theme tag was also removed since nothing supports any theme classification without a photo or description. No image of the built SAO was found to save.'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/other/dc321-sao-and-dc321-2-sao-dc321-sao-kicad-pcb-dc321-2-sao-ki/
model:
  file: assets/models/bsides-orlando-2023/dc321-sao-and-dc321-2-sao-dc321-sao-kicad-pcb-dc321-2-sao-ki.glb
  method: kicad
  source_file: bsidesorl-v1/bsidesorl-v1.kicad_pcb
  generated: '2026-09-10'
  bytes: 128672
---

DC321 (also known as DCG Space Coast / SpaceCoastSec) is a DEF CON group based in Melbourne, Florida, on the state's Space Coast, not Orlando itself. This entry covers two SAO (Simple Add-On) board designs made for it: `dc321-sao` and a second revision, `dc321-2-sao`. Both live as KiCad project files inside the `bsidesorlando/2023-badge` repository, in the same `bsidesorl-v1` folder that holds the main BSides Orlando 2023 "Rise of the Robots" badge and a whole family of sibling SAOs for other groups and roles: DC239, DC407 (Orlando's own DEF CON group), an "OTGG" SAO, staff, sponsor, and speaker boards, plus one named `iwc-iron-sao`.

No product page, forum post, or photo of the assembled DC321 SAO turned up outside the repo itself, so this looks like a design-file-only artifact rather than something separately marketed or reviewed at the con. The git history for the folder credits Jose Rodriguez with the commits that introduced and expanded these SAO designs, but the PCB files carry no explicit author byline of their own beyond placeholder "LOGO" and "SAO" silkscreen text, so component-level details (chip, LEDs, colors) could not be confirmed from what's public.

## Make your own

Hardware files (KiCad `.kicad_pcb`/`.kicad_pro`/`.kicad_prl`, plus a zipped copy of the PCB) for both `dc321-sao` and `dc321-2-sao` are in `bsidesorl-v1/` of the repo linked above. No firmware or BOM was found alongside them.
