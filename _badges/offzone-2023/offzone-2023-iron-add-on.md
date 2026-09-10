---
title: OFFZONE 2023 Iron add-on
id: offzone-2023-offzone-2023-iron-add-on
layout: badge
parent: OFFZONE 2023
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: offzone-2023
year: 2023
makers:
- name: BI.ZONE / Craft.Zone
  url: https://github.com/bi-zone/offzone-hw
summary: A DIY, iron-shaped SAO add-on from BI.ZONE's Craft.Zone hardware line for OFFZONE 2023, built around two blinking LEDs driven by a discrete astable-style transistor circuit rather than a microcontroller.
functions: Two red 0805 LEDs blink/alternate, driven by a simple two-transistor (BC807-25) discrete oscillator circuit rather than firmware.
look:
  colors:
  - black
  - white
  - red
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 2x red 0805 LEDs, driven by a 2-transistor (BC807-25) discrete blinker circuit, no MCU.
  display: none
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Published as open-source design files (KiCad + Gerbers + BOM) on GitHub for badge-goers to fabricate and solder themselves; not sold as a finished product.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/bi-zone/offzone-hw/tree/master/2023/iron_addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bi-zone/offzone-hw/tree/main/2023/iron_addon
  url: https://github.com/bi-zone/offzone-hw/tree/main/2023/iron_addon
  kind: repo
- label: github.com/bi-zone/offzone-hw (repo root, default branch is master)
  url: https://github.com/bi-zone/offzone-hw
  kind: repo
- label: github.com/bi-zone/offzone-hw/tree/master/2023/iron_addon
  url: https://github.com/bi-zone/offzone-hw/tree/master/2023/iron_addon
  kind: repo
images:
- file: assets/images/badges/offzone-2023/offzone-2023-iron-add-on/8599a35034.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2023/iron_addon
  credit: BI.ZONE / Craft.Zone
  caption: Iron add-on board, front
- file: assets/images/badges/offzone-2023/offzone-2023-iron-add-on/a1acf41527.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2023/iron_addon
  credit: BI.ZONE / Craft.Zone
  caption: Iron add-on board, back
- file: assets/images/badges/offzone-2023/offzone-2023-iron-add-on/8599a35034.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2023/iron_addon
  credit: BI.ZONE / Craft.Zone
  caption: Iron add-on PCB, front view
- file: assets/images/badges/offzone-2023/offzone-2023-iron-add-on/a1acf41527.jpg
  source: https://github.com/bi-zone/offzone-hw/tree/master/2023/iron_addon
  credit: BI.ZONE / Craft.Zone
  caption: Iron add-on PCB, back view
contact: {}
notes:
- Iron-themed add-on board for the OFFZONE 2023 badge. Found by the event-year sweep, task con-phdays.
- The repo's default branch is `master`, not `main`; the original sweep-found link (…/tree/main/2023/iron_addon) 404s. The working path is https://github.com/bi-zone/offzone-hw/tree/master/2023/iron_addon.
- The repo also contains an unreleased "iron_v2_addon" under a `nevermadeit/` folder — a second-version design that was apparently never produced. Not part of this entry.
- Sweep wording was 'iron_addon' (the repo folder name); the maker's page names the board simply as the "Iron addon" for OFFZONE 2023, styled after a clothes iron.
- This entry duplicates offzone-2023-offzone-2023-iron-add-on, an already-researched entry for the same GitHub project (same repo path, same board, same photos). See that entry for the fuller writeup and source trail.
status: released
sources:
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/main/2023/iron_addon
  title: OFFZONE 2023 Iron add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2023''.'
- kind: url
  url: https://github.com/bi-zone/offzone-hw/tree/master/2023/iron_addon
  title: 'bi-zone/offzone-hw: 2023/iron_addon (README, KiCad files, Gerbers, BOM)'
  accessed: '2026-09-08'
  note: Confirmed the item exists (repo tree via GitHub API, since the sweep's /main/ link 404s on the actual default branch /master/); read README.md and iron_addon_BOM.html for build instructions, PCB spec, BOM (2x red 0805 LEDs, 2x 220R + 2x 100k resistors, 2x BC807-25 transistors, 2x 10-22uF SMD electrolytic caps, 1x PLD-4 connector).
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/images/iron_addon_front.jpg
  title: iron_addon_front.jpg
  accessed: '2026-09-08'
  note: Front photo of the assembled board, saved to images.
- kind: url
  url: https://raw.githubusercontent.com/bi-zone/offzone-hw/master/images/iron_addon_back.jpg
  title: iron_addon_back.jpg
  accessed: '2026-09-08'
  note: Back photo of the assembled board, saved to images.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: The maker's own repo (BI.ZONE org on GitHub) confirms the item and gives a complete BOM, PCB fab spec, and build instructions, so confidence is high despite no price/quantity/distribution details being published (this is a share-your-own-Gerbers project, not a storefront listing, so get_one fields mostly stay empty/unknown). No English-language coverage found; all source text is in Russian. Could not confirm exact SAO pin count from the PLD-4 connector alone, so sao_version is a best-effort v1 based on OFFZONE/Craft.Zone add-ons generally using 4-pin SAO headers; not verified against the schematic pinout. Merged with duplicate entry 'OFFZONE 2023 Iron add-on' (offzone-2023-iron-addon).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/offzone-2023/iron-addon/
model:
  file: assets/models/offzone-2023/offzone-2023-iron-add-on.glb
  method: kicad
  source_file: 2023/iron_addon/iron_addon.kicad_pcb
  generated: '2026-09-10'
  bytes: 37096
---

The Iron add-on is one of several small SAO-style boards BI.ZONE's Craft.Zone project released for OFFZONE 2023, styled after a household clothes iron. Unlike a microcontroller-driven SAO, it runs entirely on discrete components: two red 0805 LEDs are driven by a simple two-transistor (BC807-25) astable blinker circuit, with a pair of resistors and electrolytic capacitors setting the timing, and a single PLD-4 connector to plug into a host badge.

BI.ZONE published the full KiCad source, Gerbers, and an HTML bill of materials for the board on GitHub rather than selling it as a finished product — the repository's stated purpose is to let OFFZONE attendees order their own PCBs and hand-solder the kit themselves, with the README walking through soldering order (resistors first, then polarity-sensitive LEDs, then transistors and capacitors, then the connector). No price, production quantity, or distribution channel is stated anywhere in the source; it reads as a build-it-yourself design share rather than a badge given out pre-assembled.

The same repository also contains a second-generation "iron_v2_addon" design sitting in a folder named `nevermadeit`, suggesting a follow-up revision was designed but never produced or released; that design is not covered by this entry.

## Notes merged from the duplicate entry "OFFZONE 2023 Iron add-on"

The Iron add-on is one of several small SAO-style boards BI.ZONE's Craft.Zone project released for OFFZONE 2023, styled after a household clothes iron — its silkscreen shows two crossed soldering irons under a "CRAFT ZONE / OFFZONE 2023" logo. Unlike a microcontroller-driven SAO, it runs entirely on discrete components: two red 0805 LEDs are driven by a simple two-transistor (BC807-25) astable blinker circuit, with a pair of resistors and electrolytic capacitors setting the timing, and a single PLD-4 connector to plug into a host badge.

BI.ZONE published the full KiCad source, Gerbers, and an HTML bill of materials for the board on GitHub rather than selling it as a finished product, so no price, production quantity, or distribution channel is stated. This appears to be the same board already documented under the entry `offzone-2023-offzone-2023-iron-add-on`; see that entry for a longer writeup.
