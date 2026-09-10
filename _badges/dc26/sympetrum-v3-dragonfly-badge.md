---
title: Sympetrum v3 (Dragonfly badge)
id: dc26-sympetrum-v3-dragonfly-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: borgel (Kerry Scharfglass)
  url: https://github.com/borgel
summary: A dragonfly-shaped electronic conference badge for DEF CON 26 with 48 RGB LEDs that sync IR-beaconed light animations across nearby badges.
functions: Runs pleasant RGB fades across 48 RGB LEDs by default. Transmits an IR beacon every 30 seconds and listens for beacons from nearby badges to synchronize a shared clock; a lone badge shows random colors, while a group falls into the same rainbow water-drop animation together.
look:
  colors:
  - green
  - white
  shape: null
  themes:
  - animal
  - insect
  - wearable
tech:
  mcu: STM32F051
  leds:
    count: 48
    type: RGB
    note: ''
  display: none
  connectivity:
  - ir
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
  open_source: true
  hardware_url: https://github.com/borgel/sympetrum-v3/tree/master/Hardware
  firmware_url: https://github.com/borgel/sympetrum-v3/tree/master/Firmware
  eda_tool: KiCad
  license: CC BY-NC 4.0
links:
- label: github.com/borgel/sympetrum-v3
  url: https://github.com/borgel/sympetrum-v3
  kind: repo
- label: Sympetrum v2 (DEF CON 25 predecessor)
  url: https://github.com/borgel/sympetrum-v2
  kind: repo
- label: 'Hackaday: Badge From Diamond Age Comes To DEF CON'
  url: https://hackaday.com/2017/07/14/badge-from-diamond-age-comes-to-def-con/
  kind: article
images:
- file: assets/images/badges/dc26/sympetrum-v3-dragonfly-badge/e38f973218.png
  source: https://github.com/borgel/sympetrum-v3/tree/master/Hardware/Badge
  credit: borgel (Kerry Scharfglass)
  caption: KiCad PCB render of the Sympetrum v3 dragonfly-shaped badge
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 4).
status: released
sources:
- kind: url
  url: https://github.com/borgel/sympetrum-v3
  title: Sympetrum v3 (Dragonfly badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run4-spotted); event read as ''dc26''.'
- kind: url
  url: https://github.com/borgel/sympetrum-v3
  title: borgel/sympetrum-v3 README
  accessed: '2026-09-08'
  note: Confirmed maker, event (DEF CON 26, 2018), 48 RGB LEDs, IR beacon sync behavior, CC BY-NC 4.0 license, link to DC25 predecessor (sympetrum-v2) and 2017 Hackaday writeup.
- kind: url
  url: https://github.com/borgel/sympetrum-v3/tree/master/Hardware/Badge
  title: Hardware/Badge folder listing
  accessed: '2026-09-08'
  note: Found KiCad schematic/PCB files and a rendered PNG of the dragonfly PCB shape; STM32F051 identified from the firmware linker script filename (STM32F051R8Tx_FLASH.ld).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Core facts confirmed directly from the maker's own repo (README, hardware/firmware folders, license file). Could not find price, quantity made, distribution method, or battery type — not documented in the repo, and no Hackaday/press coverage specific to the v3 (2018) version was found (only a 2017 Hackaday piece about the DC25 v2 predecessor). No photos of an assembled/lit badge were found in the repo (only a KiCad render); the Media folder in the repo is a placeholder with no real images.
last_modified_date: '2026-09-10'
model:
  file: assets/models/dc26/sympetrum-v3-dragonfly-badge.glb
  method: kicad
  source_file: Hardware/Badge/Sympetrum-V3 FF3.kicad_pcb
  generated: '2026-09-10'
  bytes: 601824
---

The Sympetrum v3 is a dragonfly-shaped electronic badge that borgel (Kerry Scharfglass) built for DEF CON 26 in 2018, a partial rewrite of the DEF CON 25 "Sympetrum v2" badge. The name comes from *Sympetrum*, a genus of dragonfly, and the whole project is a direct homage to a scene in Neal Stephenson's *The Diamond Age* in which partygoers wear cloisonné dragonfly pins that shift from random colorful flickering into a synchronized pattern as the night goes on.

The badge carries 48 RGB LEDs arranged across the dragonfly's wings and body, plus an STM32F051 microcontroller. By default each badge cycles through gentle RGB color fades on its own. Every 30 seconds it also sends out an infrared beacon and listens for beacons from other nearby badges, using them to align a shared internal clock; a badge on its own displays random colors, but a cluster of them falls into the same rainbow "water drop" animation in sync with each other.

Hardware (KiCad schematics and PCB) and firmware are both published on GitHub under a CC BY-NC 4.0 license, making this an open-source build, though the repository does not state a price, production quantity, or how the badges were distributed to attendees.

## Make your own

The maker's GitHub repository (github.com/borgel/sympetrum-v3) contains the full KiCad hardware design under `Hardware/Badge` and STM32 firmware source under `Firmware`, along with a linked Google Doc with assembly instructions. No BOM or Gerber-specific fabrication share link was found separately from the KiCad project files.

## History

Sympetrum v3 follows Sympetrum v2, borgel's DEF CON 25 (2017) dragonfly badge, which was covered by Hackaday at the time; v3 is described by the maker as a partial rewrite of that earlier design for DEF CON 26.
