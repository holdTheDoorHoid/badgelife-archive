---
title: DC31 H4X0R Badge
id: dc31-h4x0r-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc31
year: 2023
makers:
- name: NilbinSec
  url: https://github.com/NilbinSec
summary: A non-electronic, KiCad-designed PCB add-on for the DEF CON 31 conference badge, styled around the leetspeak "H4X0R" name.
functions: 'None: it is a passive, unpopulated PCB panel meant to attach to or accompany the DC31 badge as decoration, not an electronic device.'
look:
  colors: []
  shape: null
  themes:
  - security
  - text
tech:
  mcu: none
  leds:
    count: 0
    type: null
    note: Non-electronic add-on; no components are populated.
  display: none
  connectivity: []
  battery: none
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/NilbinSec/DC31H4X0R-Badge
  firmware_url: null
  gerbers_url: https://github.com/NilbinSec/DC31H4X0R-Badge/tree/main/gerbers
  eda_tool: KiCad
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/NilbinSec/DC31H4X0R-Badge
  title: DC31 H4X0R Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 31, non-electronic add-on''.'
- kind: url
  url: https://api.github.com/repos/NilbinSec/DC31H4X0R-Badge
  title: NilbinSec/DC31H4X0R-Badge (repo metadata)
  accessed: '2026-09-07'
  note: Confirms repo description "Upload of Non-Electronic Add-On For the Defcon31 Conference Badge" and repo creation date 2023-05-31, consistent with DEF CON 31 (Aug 2023).
- kind: url
  url: https://github.com/NilbinSec/DC31H4X0R-Badge/tree/main
  title: Repository file listing
  accessed: '2026-09-07'
  note: File listing shows only KiCad PCB/schematic files, SVG vector art, and gerbers for two board variants (H4X0R, H4X0R-small) plus a card-outline board; no README, no photos, no BOM.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all three cited sources directly. repos/NilbinSec/DC31H4X0R-Badge confirms description "Upload of Non-Electronic Add-On For the Defcon31 Conference Badge" and created_at 2023-05-31T00:26:13Z. The root file listing (via GitHub API) confirms only KiCad project/PCB/library files, SVG artwork, and a gerbers folder for H4X0R, H4X0R-small, and a separate DC31BADGE-CARD-OUTLINE board; no README, BOM, or photo file is present. Downloaded H4X0R.kicad_pcb directly and confirmed zero `(footprint ...)` entries — the only placed elements are graphic lines, and the referenced H4X0R.pretty library holds only per-layer artwork modules, not header/connector footprints — supporting tech.mcu/sao_version: none and type: accessory. gerbers/ was confirmed to contain gerber sets for all three boards. Only source found remains the maker''s own GitHub repo; no press coverage, storefront listing, social post, or photo of a finished unit turned up, so price, quantity,
    distribution method, colors, and exact shape stay blank. Confidence stays low for that reason even though every remaining field is now independently verified against source content, not just the entry''s own citations.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc31/h4x0r-badge.glb
  method: kicad
  source_file: _autosave-H4X0R-small.kicad_pcb
  generated: '2026-09-07'
  bytes: 66480
---

NilbinSec's H4X0R Badge is a companion PCB made for DEF CON 31 (2023) attendees, distributed as an open-source KiCad design rather than a documented product. Unlike NilbinSec's usual SAOs and powered badges, the maker's own repository describes it plainly as a "Non-Electronic Add-On" for the DC31 conference badge: the board carries no microcontroller, LEDs, or connector footprints, so it functions purely as a shaped, artwork-only PCB panel referencing the "H4X0R" hacker slang.

The repository holds two sizes of the design (`H4X0R` and `H4X0R-small`) along with vector artwork, gerbers, and a separate `DC31BADGE-CARD-OUTLINE` board whose exact relationship to the H4X0R piece (whether a frame, holder, or unrelated companion file) isn't explained in any available source. No photos of an assembled unit, pricing, quantity, or distribution details were found in press coverage, storefronts, or social posts, so those fields are left blank pending a firsthand account or maker post.

## Make your own

The full hardware design is published on GitHub: KiCad schematic/PCB files for both size variants, SVG vector artwork, and ready-to-fab gerbers.

- Repo: https://github.com/NilbinSec/DC31H4X0R-Badge
- Gerbers: https://github.com/NilbinSec/DC31H4X0R-Badge/tree/main/gerbers
