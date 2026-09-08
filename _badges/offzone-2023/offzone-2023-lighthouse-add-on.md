---
title: OFFZONE 2023 Lighthouse add-on
id: offzone-2023-offzone-2023-lighthouse-add-on
layout: badge
parent: OFFZONE 2023
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2023
year: 2023
makers:
- name: BI.ZONE / Craft.Zone
summary: A lighthouse-shaped solder-it-yourself add-on board for OFFZONE 2023, built around a simple two-transistor astable flasher that alternately blinks two white LEDs.
functions: Alternately flashes its two white LEDs using a discrete two-transistor astable multivibrator circuit; no microcontroller or firmware involved.
look:
  colors:
  - black
  - white
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 2x 3mm white THT LEDs, driven by a 2-transistor (BC807-25) astable flasher circuit, not addressable/software-driven.
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
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2023/lighthouse_addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bi-zone/offzone-hw/tree/master/2023/lighthouse_addon
  url: https://github.com/bi-zone/offzone-hw/tree/master/2023/lighthouse_addon
  kind: repo
images:
  - file: assets/images/badges/offzone-2023/offzone-2023-lighthouse-add-on/c374614219.png
    source: "https://github.com/bi-zone/offzone-hw/tree/master/2023/lighthouse_addon"
    credit: "BI.ZONE / Craft.Zone"
    caption: "PCB render of the Lighthouse add-on"
  - file: assets/images/badges/offzone-2023/offzone-2023-lighthouse-add-on/030d98fe3e.jpg
    source: "https://github.com/bi-zone/offzone-hw/tree/master/2023/lighthouse_addon"
    credit: "BI.ZONE / Craft.Zone"
    caption: "Assembled Lighthouse add-on, front side, LEDs lit"
contact: {}
notes:
- Lighthouse-themed add-on board for the OFFZONE 2023 badge. Found by the event-year sweep, task con-phdays.
- The sweep's source link used the "main" branch, which 404s; the repo's default branch is "master" (same path otherwise).
status: released
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2023/lighthouse_addon
  title: OFFZONE 2023 Lighthouse add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2023''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/master/2023/lighthouse_addon
  title: lighthouse_addon (bi-zone/offzone-hw)
  accessed: '2026-09-08'
  note: "Corrected repo URL (branch is master, not main). Directory listing and README: 2-layer FR4 PCB, black soldermask/white silkscreen; BOM of 2x 3mm white LEDs, 2x 220 ohm resistors, 2x 100k ohm resistors, 2x BC807-25 transistors, 2x SMD electrolytic capacitors, 1x PLD-4 connector; step-by-step soldering instructions; KiCad source files and Gerbers provided."
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/README.md
  title: offzone-hw repo README
  accessed: '2026-09-08'
  note: "Repo-level context: BI.ZONE publishes yearly OFFZONE/Craft.Zone add-on boards as solder-it-yourself kits with Gerbers and BOMs, meant to be beginner-friendly."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: "Confirmed to exist via the maker's own GitHub repo (hardware files, BOM, assembly instructions, and a preview render/photo). No storefront, price, quantity, or distribution details found — likely distributed as a free solder-your-own kit at the OFFZONE 2023 / Craft.Zone village, but this is not confirmed by a source, so get_one fields are left empty. No SAO connector standard confirmed (BOM lists a 'PLD-4' connector, not a documented 4/6-pin SAO header), so tech.sao_version and connectivity are left unset rather than guessed. type is recorded as 'sao' per the archive's existing sibling entries for this same OFFZONE 2023 add-on series (cat/ikarus/iron add-ons), consistent with it being a small plug-in add-on board, but no source explicitly calls it an SAO."
last_modified_date: '2026-09-08'
---

The Lighthouse add-on is one of a small family of solder-it-yourself add-on boards BI.ZONE's Craft.Zone published for OFFZONE 2023, alongside sibling Cat, Ikarus, and Iron add-ons from the same event. It is a lighthouse-shaped PCB with a black soldermask and white silkscreen, built for hobbyists and newcomers to hand-solder themselves rather than something sold pre-assembled.

Electrically it is deliberately simple: no microcontroller, just a classic two-transistor (BC807-25) astable multivibrator that alternately flashes two 3mm white through-hole LEDs, fed by a pair of resistors and small electrolytic capacitors that set the flash timing. It connects to a host board via a PLD-4 connector.

BI.ZONE publishes full KiCad source files, Gerbers ready for fabrication, an HTML bill of materials, and Russian-language step-by-step soldering instructions in the project's GitHub repository, positioning it as an open hardware learn-to-solder kit rather than a commercial product. No pricing, production quantity, or distribution channel is documented in the source material, so those fields are left blank.

## Make your own

The repository (`github.com/bi-zone/offzone-hw`, folder `2023/lighthouse_addon`) includes everything needed to build one: the KiCad project and schematic, a Gerber (`_gbr`) folder ready to send straight to a PCB fabricator, an HTML BOM listing exact part values, and a README with an ordered soldering sequence (resistors first, then transistors and capacitors per the silkscreen, then the LEDs — cathode/short leg up — and finally the connector).
