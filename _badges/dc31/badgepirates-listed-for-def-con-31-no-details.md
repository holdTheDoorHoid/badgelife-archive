---
title: BioHacking Village Badge (DEF CON 31)
id: dc31-badgepirates-listed-for-def-con-31-no-details
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
series: BioHacking Village Badge
makers:
- name: BadgePirates
  url: https://badgepirates.com
summary: A skull-in-mohawk PCB badge BadgePirates designed for the BioHacking Village at DEF CON 31, with a wrench-and-DNA logo and LEDs lighting the mohawk spikes.
functions: A slide switch cycles four LED modes silkscreened as Blinkie, Off, White, and UV.
look:
  colors: []
  shape: skull
  themes:
  - skull
  - cyberpunk
  - security
tech:
  mcu: none
  leds:
    count: null
    type: through-hole
    note: White and UV LEDs populate the mohawk spikes and face outline; no exact count confirmed from the board render.
  display: none
  connectivity: []
  battery: CR2450
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
  hardware_url: https://github.com/BadgePiratesLLC/BioHackingVillage_31
  firmware_url: null
  eda_tool: KiCad
links:
- kind: repo
  label: BioHackingVillage_31 (GitHub, archived)
  url: https://github.com/BadgePiratesLLC/BioHackingVillage_31
- kind: website
  label: BadgePirates.com portfolio
  url: https://badgepirates.com
images:
- file: assets/images/badges/dc31/badgepirates-listed-for-def-con-31-no-details/400fda9a38.jpg
  source: https://github.com/BadgePiratesLLC/BioHackingVillage_31
  credit: BadgePirates
  caption: '3D CAD render of the BioHacking Village DC31 badge, front side: a mohawked skull silhouette with a wrench-and-DNA icon'
- file: assets/images/badges/dc31/badgepirates-listed-for-def-con-31-no-details/d9c85bda48.jpg
  source: https://github.com/BadgePiratesLLC/BioHackingVillage_31
  credit: BadgePirates
  caption: '3D CAD render of the PCB side: mohawk-spike LEDs, CR2450 holder, and a Blinkie/Off/White/UV mode switch'
contact:
  email: admin@badgepirates.com
notes:
- The community sheet listed only the maker (BadgePirates) for DEF CON 31 with no further details; this entry was retitled after identifying the specific badge from BadgePirates' own GitHub org.
status: released
sources:
- kind: sheet
  event: dc31
  row: 7
  updated: '2023-02-14'
- kind: url
  url: https://badgepirates.com
  title: Badge Pirates — Making badges for fun and no profit
  accessed: '2026-09-06'
  note: Maker's portfolio site; confirms a 'BioHacking Village DC31' badge exists among their DEF CON work, distinct from an earlier 'BioHacking Village' badge.
- kind: url
  url: https://github.com/BadgePiratesLLC/BioHackingVillage_31
  title: BadgePiratesLLC/BioHackingVillage_31 (GitHub)
  accessed: '2026-09-06'
  note: Archived project repo with KiCad source, gerbers, and artwork; confirms design name 'BiohackingPivot', designer credit 'Lee Cyborg', MIT license, and board layout (CR2450, mode switch, no MCU). README is empty; no price, quantity, or distribution details found.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: |
    Confirmed via BadgePirates' own site and GitHub org that their DEF CON 31 contribution was a "BioHacking Village DC31" badge (project internally named "BiohackingPivot", designed by "Lee Cyborg"), distinct from an earlier, undated "BioHacking Village" badge also in their portfolio. The GitHub repo (archived) has KiCad hardware files, gerbers, and artwork under an MIT license but an empty README, so price, quantity made, and how it was distributed (sold, given to volunteers, village giveaway) could not be confirmed from any source found. PCB solder-mask color could not be confirmed either — the only board images found are neutral-shaded 3D CAD renders, not photos of a physical unit, so `look.colors` was left empty rather than guessed from the render's render-engine shading. LED count likewise left unconfirmed (roughly a dozen spike LEDs are visible on the render but not clearly countable). No storefront, press coverage, or BioHacking Village program mention was found in the time budgeted for this pass.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc31/badgepirates-listed-for-def-con-31-no-details.glb
  method: kicad
  source_file: CAD/BiohackingPivot.kicad_pcb
  generated: '2026-09-07'
  bytes: 392200
---

BadgePirates' entry on the community sheet for DEF CON 31 originally listed only the maker's name with no details about what they brought. Cross-referencing BadgePirates' own portfolio site and GitHub organization turned up the answer: a PCB badge for that year's BioHacking Village, shaped like a mohawked skull in profile with a wrench-crossed-with-DNA-strand icon on the "brain," designed by a contributor credited as Lee Cyborg. The board is silkscreened "BIOHACKING VILLAGE DC31" along the jawline and carries the BadgePirates skull-and-crossed-tools logo.

The badge has no microcontroller. It runs off a CR2450 coin cell and uses a small slide switch, silkscreened "BLINKIE / OFF / WHITE / UV," to select between a blinking LED pattern, off, steady white light, and UV light — likely aimed at the Biohacking Village's interest in things like UV-reactive ink or bioluminescent materials. LEDs populate the points of the mohawk and a couple of spots on the face outline.

BadgePirates published the hardware design (KiCad schematic/PCB, gerbers, and source artwork) to GitHub under the MIT license, but the repository's README was never filled in, so no price, production quantity, or distribution method (sold, given to volunteers, handed out at the village) turned up in this pass. It is a separate, later design from an earlier undated "BioHacking Village" badge also shown in BadgePirates' portfolio, which appears to predate this DC31 version.
