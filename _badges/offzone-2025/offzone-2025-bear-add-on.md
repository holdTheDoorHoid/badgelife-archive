---
title: OFFZONE 2025 Bear add-on
id: offzone-2025-offzone-2025-bear-add-on
layout: badge
parent: OFFZONE 2025
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2025
year: 2025
makers:
- name: BI.ZONE / Craft.Zone
summary: A bear-shaped SAO add-on for the OFFZONE 2025 badge, one of several add-on boards Craft.Zone designed for the con that year.
functions: Lights three white LEDs; no microcontroller, so no other behavior.
look:
  colors:
  - green
  - white
  shape: bear
  themes:
  - animal
  - mascot
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: 3x 1206 white LEDs, lens mounted facing down into the board
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2025/bear_addon
  firmware_url: null
  eda_tool: KiCad
notes:
- Bear-themed add-on board for the OFFZONE 2025 badge. Found by the event-year sweep, task con-phdays.
status: listed
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2025/bear_addon
  title: OFFZONE 2025 Bear add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2025''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/master/2025/bear_addon
  title: bear_addon README, offzone-hw repo (BI.ZONE)
  accessed: '2026-09-08'
  note: Confirmed the item exists (default branch is master, not main); README gives BOM, PCB spec, and assembly instructions.
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/images/bear_addon_front.jpg
  title: bear_addon_front.jpg
  accessed: '2026-09-08'
  note: Front photo of the assembled board, saved to images.
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/images/bear_addon_back.jpg
  title: bear_addon_back.jpg
  accessed: '2026-09-08'
  note: Back photo of the assembled board, saved to images.
links:
- label: github.com/bi-zone/offzone-hw/tree/main/2025/bear_addon
  url: https://github.com/bi-zone/offzone-hw/tree/main/2025/bear_addon
  kind: repo
- label: bear_addon README (master branch)
  url: https://github.com/bi-zone/offzone-hw/tree/master/2025/bear_addon
  kind: repo
images:
- file: assets/images/badges/offzone-2025/offzone-2025-bear-add-on/2abab8aa7c.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2025/bear_addon
  credit: BI.ZONE / Craft.Zone
  caption: Bear add-on front, assembled with three white LEDs
- file: assets/images/badges/offzone-2025/offzone-2025-bear-add-on/597d936997.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2025/bear_addon
  credit: BI.ZONE / Craft.Zone
  caption: Bear add-on back, showing solder connections and PLD-4 connector
contact: {}
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: The original repo link in the sweep pointed at the `main` branch, which does not exist; the repo's default branch is `master`, and the same path resolves there. Confirmed via the repo's README, BOM, and Gerbers that this is a real, open-source bear-shaped SAO add-on, one of five 2025 add-ons Craft.Zone made alongside the OFFZONE 2025 main badge (angel-and-devil, anonymous, boombox, terminal). No storefront, price, quantity, or distribution details were found; these badges are typically given to attendees/speakers at the Russian OFFZONE conference rather than sold, but that is not confirmed by a primary source here, so availability is left unknown. No firmware exists (the board has no MCU, just three LEDs and resistors driven directly off the SAO header). KiCad hardware files, Gerbers, and BOM are published in the repo, so open_source is yes for hardware; there is no firmware to publish.
last_modified_date: '2026-09-10'
model:
  file: assets/models/offzone-2025/offzone-2025-bear-add-on.glb
  method: kicad
  source_file: 2025/bear_addon/bear_addon.kicad_pcb
  generated: '2026-09-10'
  bytes: 98392
---

The Bear add-on is one of five SAO-style add-on boards Craft.Zone produced to go with the OFFZONE 2025 main badge for BI.ZONE's OFFZONE security conference (the others being Angel and Devil, Anonymous, Boombox, and Terminal). It is a small bear-shaped PCB carrying three 1206 white LEDs and matching 220 ohm resistors, wired straight to a 4-pin PLD-4 connector with no microcontroller in the loop — the LEDs simply light whenever the host badge supplies power through the SAO header.

The board ships as a bare-copper, green-soldermask 2-layer PCB, and pairs with a separate "bear_plates" board — a thinner, white-soldermask, HASL-finished panel that gets heat-fused onto the front as a decorative overlay during assembly, per the maker's build instructions.

## Make your own

The hardware is fully open: the repository at `bi-zone/offzone-hw` (note: the default branch is `master`, not `main` as an older link might suggest) contains the KiCad schematic and PCB files, Gerbers and drill files for both the bear_addon board and the bear_plates overlay, and a BOM. To build one: solder the three 220 ohm resistors, solder the three white 1206 LEDs lens-side down and observing polarity, reflow the decorative bear_plates overlay onto the front with a heat gun, and solder on the PLD-4 connector. There is no firmware, since the board has no MCU.
