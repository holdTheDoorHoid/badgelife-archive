---
title: Sparky SAO Display
id: other-sparky-sao-display
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: other
year: 2025
makers:
- name: NerdFlare
  url: https://nerdflare.github.io
summary: A USB-C powered display board, shaped like the club's "Sparky" mascot, with a row of SAO headers for showing off a collection of add-on badges rather than being worn itself.
functions: Holds and powers multiple SAOs at once for display; not a wearable badge or a single add-on.
look:
  colors: []
  shape: null
  themes:
  - mascot
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single indicator LED near the power regulator; no addressable LEDs found in the schematic.
  display: none
  connectivity: []
  battery: USB-C
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/NerdFlare/sparky-sao-display
  firmware_url: null
  eda_tool: KiCad
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- 'Repo description says "13 badge SAO display"; the committed schematic (pcb/sparky sao display.kicad_sch) shows 12 SAO connector footprints (SHITTY_ADD-ON_V1.69BIS SAO), each behind its own polyfuse, fed from a USB-C input through an LD1117S33TR 3.3V regulator, with one SPDT switch and one LED.'
status: unknown
sources:
- kind: url
  url: https://github.com/NerdFlare/sparky-sao-display
  title: Sparky SAO Display
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://nerdflare.github.io
  title: NerdFlare (Cal Poly club) website
  accessed: '2026-09-07'
  note: Confirms NerdFlare is a Cal Poly San Luis Obispo student club making interactive PCB artwork, badges, and SAOs; club meets biweekly; no mention of a specific convention tied to this board.
- kind: url
  url: https://github.com/NerdFlare/sparky-sao-display/git/trees/main?recursive=1
  title: Repo file tree (via gh api)
  accessed: '2026-09-07'
  note: 'Repo contains only design files: art/sparky-badge.svg (vector artwork/PCB silkscreen art) and pcb/sparky sao display.kicad_pcb, .kicad_pro, .kicad_sch. No README, no photos of an assembled unit, no license file.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all three sources and the raw KiCad schematic. GitHub repo description ("A USB-C powered, 13 badge SAO display, shaped like our good buddy Sparky.") and file tree (art/sparky-badge.svg, pcb/*.kicad_pcb/.kicad_pro/.kicad_sch, no README, no license) both confirmed via `gh api`. Schematic reference designators confirmed exactly: 13 "J" connectors of which 12 are SHITTY_ADD-ON_V1.69BIS SAO headers and 1 (J13) is the USB-C input; 12 polyfuses (F1-F12, one per SAO header); one LD1117S33TR_SOT223 regulator (U1); one SW_SPDT switch (SW1); one Device:LED (D1). This fully supports the "12 vs 13" discrepancy note and every tech.* field. nerdflare.github.io confirmed as the Cal Poly SLO club site but does not mention "Sparky" or this board by name; the mascot/theme claim rests on the GitHub repo description instead, which is sufficient support. This is a Cal Poly student-club (NerdFlare) hardware project, not a con-sold badge/SAO, so it has no clear conference/year home in events.yml; left under "other." Repo was created and last pushed 2025-10-22 (same timestamp day, single commit), so it may be an in-progress or one-off club project rather than something distributed at an event. No pricing, quantity, availability, or maker photos were found anywhere; only KiCad design files and one SVG artwork file exist in the repo (no README). The "Sparky" shape/colors could not be confirmed visually (only raw SVG path data available, not a rendered image), so look.shape and look.colors were correctly left empty. type is set to "accessory" because this board displays/powers other SAOs rather than being worn or plugging into a badge itself. No images field was present to check.'
last_modified_date: '2026-09-07'
---

Sparky SAO Display is a hardware project from NerdFlare, a student club at Cal Poly San Luis Obispo focused on interactive PCB artwork and badgelife-style electronics. The board is a USB-C powered display base, silkscreened in the shape of the club's "Sparky" mascot, carrying a row of SAO (Shitty Add-On) headers so a collection of add-on badges can be plugged in and powered at once rather than worn on a lanyard.

The schematic in the project's GitHub repository shows twelve SAO v1.69bis headers, each protected by its own polyfuse, fed from a USB-C input through an LD1117S33TR linear regulator down to 3.3V, with a single SPDT power switch and one indicator LED. There is no microcontroller on the board — it is a passive power and display fixture for other people's SAOs, not itself a programmable badge. The repository (created October 2025) holds only KiCad design files and one SVG artwork file; there is no README, no photos of a built unit, and no stated license, price, or production quantity, so it is unclear whether this project was ever built beyond the design files or distributed at any event.

## Make your own

The hardware design is openly available as KiCad files: `pcb/sparky sao display.kicad_pcb`, `.kicad_pro`, and `.kicad_sch`, plus the board artwork as `art/sparky-badge.svg`, all in the [GitHub repo](https://github.com/NerdFlare/sparky-sao-display). No firmware is needed since the board carries no microcontroller; no bill-of-materials or build guide was found beyond the schematic itself.
