---
title: BigFuckingOOTBadge
id: dc32-bigfuckingootbadge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: BigFuckingBadge
  url: https://hackaday.io/hexum064
summary: A huge (18x12") Ocarina of Time-themed badge with touch buttons, RGB LEDs, and song-unlocking gameplay, made by hexum064 and Erin for DEF CON 32.
functions: It's a BigFuckingBadge so it's huge (18x12). It's modeled after the Ocarina Of Time. It plays notes, OOT songs, Nyan Cat. It has lights. It has an Easter Egg or two. Touch buttons let players unlock original in-game songs, similar to how it works in the game itself.
look:
  colors: []
  shape: null
  themes:
  - video game
  - music
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ~$100
  price_usd: 100.0
  quantity: '50'
  availability: unknown
  distribution:
  - purchase
  where: sold only at the con; intended to be sold through Hacker Warehouse rather than by walking around selling them
make_your_own:
  open_source: true
  hardware_url: https://github.com/Hexum064/dc-32-oot-bgb-pcb
  firmware_url: https://github.com/Hexum064/dc32-oot-bfb-code
  eda_tool: KiCad
links:
- label: hackaday.io/project/196537-bigfuckingootbadge
  url: https://hackaday.io/project/196537-bigfuckingootbadge
  kind: hackaday
- label: github.com/Hexum064/dc-32-oot-bgb-pcb
  url: https://github.com/Hexum064/dc-32-oot-bgb-pcb
  kind: repo
- label: github.com/Hexum064/dc32-oot-bfb-code
  url: https://github.com/Hexum064/dc32-oot-bfb-code
  kind: repo
images:
- file: assets/images/badges/dc32/bigfuckingootbadge/e0dee57687.png
  source: https://hackaday.io/project/196537-bigfuckingootbadge
  credit: hexum064 and Erin
  caption: BigFuckingOOTBadge PCB render (project cover image), an Ocarina of Time-themed badge
contact:
  emails:
  - bfb.team.public@gmail.com
notes:
- https://hackaday.io/project/196537-bigfuckingootbadge
status: released
sources:
- kind: sheet
  event: dc32
  row: 20
  updated: '2024-06-18'
- kind: url
  url: https://hackaday.io/project/196537-bigfuckingootbadge
  title: BigFuckingOOTBadge | Hackaday.io
  accessed: '2026-09-06'
  note: Maker names (hexum064 and Erin), price, 50-unit quantity, weight (13 oz), open-source hardware/firmware repo links, distribution via Hacker Warehouse, project image.
- kind: url
  url: https://github.com/Hexum064/dc-32-oot-bgb-pcb
  title: GitHub - Hexum064/dc-32-oot-bgb-pcb
  accessed: '2026-09-06'
  note: Confirms PCB designed in KiCad; BOM and assembly-position files present, but no README with chip/LED specifics.
- kind: url
  url: https://github.com/Hexum064/dc32-oot-bfb-code
  title: GitHub - Hexum064/dc32-oot-bfb-code
  accessed: '2026-09-06'
  note: Firmware repo; build files reference the Raspberry Pi Pico SDK (pico_sdk_import.cmake) but no README confirming the exact MCU, so tech.mcu left blank rather than guessed.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-06'
  notes: Fact-checked 2026-09-06 against the Hackaday.io page and both GitHub repos; an unsupported claim about an earlier Covid badge was removed (the page cites the team's Grumpy Cat badge as the inspiration). The saved image is the project's cover image, a PCB render rather than a photo. Maker's own Hackaday.io project page confirms the team (hexum064 and Erin), the $100 target price, 50 units made, and that hardware/firmware are open-sourced on GitHub. The PCB repo confirms KiCad as the EDA tool. The firmware repo's build system references the Raspberry Pi Pico SDK, suggesting an RP2040-class MCU, but no source document states the chip explicitly, so tech.mcu, tech.leds, tech.display, and tech.battery are left null rather than inferred. Could not confirm current sale/sold-out status (Hacker Warehouse listing not checked), so availability stays unknown.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc32/bigfuckingootbadge.glb
  method: kicad
  source_file: _autosave-oot-badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 395772
---

The BigFuckingOOTBadge is a large (18x12 inch) electronic badge made for DEF CON 32 (2024) by the two-person BigFuckingBadge team, hexum064 and Erin. It continues their "Big Fucking Badge" line of oversized badges ("Bigger Than Last Year!!!", per the project page), is themed around The Legend of Zelda: Ocarina of Time, and the maker describes it as heavily inspired by the team's earlier Grumpy Cat badge, only more advanced. It uses touch buttons and RGB LEDs to let players pick out notes and play back Ocarina of Time songs and other tunes such as Nyan Cat, in a freeplay mode as well as a mode where players unlock the game's original songs the way they do in the game itself. The maker also promised "an Easter Egg or two."

Fifty units were produced with a target price around $100 each; unlike prior years where the team sold badges by walking the con floor, this batch was intended to be sold through Hacker Warehouse. Both the PCB design (in KiCad) and the firmware are published on GitHub under the hexum064 account, making the badge open source, though neither repository's public documentation spells out the exact MCU or LED part numbers used.

## Make your own

Hardware (KiCad PCB, including BOM and assembly-position files) is at github.com/Hexum064/dc-32-oot-bgb-pcb, and the firmware is at github.com/Hexum064/dc32-oot-bfb-code. The firmware's build configuration references the Raspberry Pi Pico SDK, so it likely targets an RP2040-based board, but this was not confirmed in the repositories' own documentation.
