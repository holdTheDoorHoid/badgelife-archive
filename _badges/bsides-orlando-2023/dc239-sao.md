---
title: DC239 SAO
id: bsides-orlando-2023-dc239-sao
layout: badge
parent: 'BSides Orlando 2023: Rise of the Robots'
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: bsides-orlando-2023
year: 2023
makers:
- name: BSides Orlando badge team
  url: https://github.com/bsidesorlando/2023-badge
- name: Jose Rodriguez
  role: committed the SAO's KiCad files to the badge repo
summary: A KiCad-designed SAO named for DC239 (the Orlando DEF CON group), built alongside the BSides Orlando 2023 "Rise of the Robots" conference badge.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - security
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
  hardware_url: https://github.com/bsidesorlando/2023-badge/blob/main/bsidesorl-v1/dc239-sao.kicad_pcb
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bsidesorlando/2023-badge/tree/main/bsidesorl-v1
  url: https://github.com/bsidesorlando/2023-badge/tree/main/bsidesorl-v1
  kind: repo
- label: 'commit: "introduced additional sao" (Jose Rodriguez, 2023-09-07)'
  url: https://github.com/bsidesorlando/2023-badge/commit/ba7172df61764dbdc8b7568b6a78d03fee2170ae
  kind: repo
images: []
contact: {}
notes:
- Sweep's title used the raw filename styling; kept as-is since it matches the file (dc239-sao.kicad_pcb) and no other name for it was found.
- 'This is one of several DEF CON group-branded SAOs in the same repo folder: sibling files dc321-sao.kicad_pcb, dc321-2-sao.kicad_pcb (a separate archive entry) and dc407-sao.kicad_pcb name the other Central Florida DEF CON groups (Tampa, Orlando-area). All four were added in the same single commit, which also added a sponsor SAO (bsidesorl-sponsor-sao.kicad_pcb) and an unrelated "iwc-iron-sao" board; the con''s staff and speaker SAOs were added separately, in a different commit.'
status: listed
sources:
- kind: url
  url: https://github.com/bsidesorlando/2023-badge/tree/main/bsidesorl-v1
  title: DC239 SAO (dc239-sao.kicad_pcb, found in the same repo/folder as this badge)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/bsidesorlando/2023-badge/commit/ba7172df61764dbdc8b7568b6a78d03fee2170ae
  title: 'Commit ba7172d: "introduced additional sao"'
  accessed: '2026-09-10'
  note: Confirms the file's origin (added by Jose Rodriguez, 2023-09-07, alongside the sibling DC321/DC321-2/DC407 SAO files) but gives no description, image, or distribution detail.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: 'Confirmed the item is a real KiCad PCB design (dc239-sao.kicad_pcb) in the BSides Orlando 2023 badge repo, not just a search snippet, but no source beyond the repo itself was found: no write-up, storefront, social post, or photo describes what it looks like, whether it has any active components, or whether it was actually fabricated and handed out. Could not confirm MCU/LEDs/display, colors/shape, price, quantity, or availability. No image found to save (the repo holds only KiCad source files, no renders or photos). Fact-check pass (2026-09-10): re-fetched both cited sources via the GitHub API. The commit and its file list check out, but the earlier draft''s claim that the con''s standard staff/speaker/sponsor SAOs were added in the same commit as this one was wrong — that commit only added a sponsor SAO and an unrelated "iwc-iron-sao" board alongside the four DEF CON group SAOs; the staff and speaker SAOs were committed separately. Corrected the notes and body accordingly. All
    other non-empty fields (title, event/year, makers, hardware_url, eda_tool, links) check out against the two sources. Also fixed an unrelated YAML error in this file''s `parent:` front-matter value (an unquoted colon was breaking the site build).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/other/dc239-sao/
model:
  file: assets/models/bsides-orlando-2023/dc239-sao.glb
  method: kicad
  source_file: bsidesorl-v1/bsidesorl-v1.kicad_pcb
  generated: '2026-09-10'
  bytes: 128672
---

DC239 SAO is a KiCad-designed add-on board named for DC239, the DEF CON group based in Orlando, Florida. Its design files sit in the same GitHub repository as the BSides Orlando 2023 "Rise of the Robots" conference badge, added in a single September 2023 commit by contributor Jose Rodriguez alongside sibling SAOs for the DC321 and DC321-2 groups (Tampa) and DC407 (Orlando-area code), plus a sponsor SAO and an unrelated "iwc-iron-sao" board. The con's staff and speaker SAOs were committed separately, at a different time.

No announcement, storefront listing, or photo of the finished board has surfaced — only the raw KiCad PCB, project, and library files. It is reasonable to guess this was one of a set of DEF CON group SAOs meant for trading among Central Florida hacker groups at the conference, but that is not confirmed by any source, so it is not stated as fact here. Its electronics (any MCU, LEDs, or display), physical appearance, and whether it was ever actually fabricated and distributed remain unknown.
