---
title: Untitled Electronics DEF CON 32 badge
id: dc32-untitled-electronics-def-con-32-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: wrickert
  url: https://github.com/wrickert
summary: A handheld, DOOM-playing badge ("MilkTastic") built by wrickert (Untitled Electronics) around a Milk-V Duo RISC-V module, with a D-pad and face buttons laid out like a game controller.
functions: Runs Linux (buildroot) on the onboard Milk-V Duo module and boots into fbDOOM (a framebuffer port of Doom) for gameplay using the badge's D-pad and buttons; reachable over a USB-Ethernet gadget interface for development/debugging.
look:
  colors:
  - green
  shape: handheld console
  themes:
  - console
  - arcade
tech:
  mcu: Milk-V Duo (Sophgo/CVITEK CV1800B/CV1801B, RISC-V)
  leds: null
  display: null
  connectivity:
  - usb
  - uart
  battery: null
  sao_version: null
  inputs:
  - buttons
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon32/Schematics
  firmware_url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon32/Linux
  eda_tool: KiCad
  fab_url: null
  notes: KiCad project is named "MilkTastic"; Gerbers, drill files, and a bill of materials are included alongside 3D-printable case parts (FreeCAD/STEP/3MF for a D-pad and front panel).
links:
- label: github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon32
  url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon32
  kind: repo
images:
- file: assets/images/badges/dc32/untitled-electronics-def-con-32-badge/e077e0c7c5.jpg
  source: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon32
  credit: wrickert
  caption: Bare MilkTastic PCB showing D-pad and face button footprints
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- The maker's KiCad project and Gerbers name this board "MilkTastic"; the sheet/entry title has been left as-is since no separate public title was found.
- Same maker (wrickert / Untitled Electronics) also has entries for DC31 (0xCafebabe badge) and DC33 (NeoSword); this DC32 board is a distinct, unrelated project.
status: released
sources:
- kind: url
  url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon32
  title: Untitled Electronics DEF CON 32 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc32''.'
- kind: url
  url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon32/Schematics
  title: MilkTastic KiCad schematics and Gerbers (Defcon32 folder)
  accessed: '2026-09-07'
  note: Confirms the board is named "MilkTastic" in KiCad; hardware is open (schematic, PCB, Gerbers, BOM published).
- kind: url
  url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon32/Linux
  title: Defcon32 Linux folder (buildroot SDK, fbDOOM, DOOM.WAD)
  accessed: '2026-09-07'
  note: Shows the badge boots a Milk-V Duo buildroot Linux image and runs fbDOOM (framebuffer Doom port); confirms Milk-V Duo (CV1800B/CV1801B) as the onboard SoC via the datasheet in Documents/.
- kind: url
  url: https://raw.githubusercontent.com/wrickert/UntitledElectronics/main/Badges/Defcon32/Documents/PXL_20240702_134725829.MP.jpg
  title: Photo of the bare MilkTastic PCB
  accessed: '2026-09-07'
  note: Photo of the fabricated, partially populated PCB showing four tactile-switch pads laid out as a D-pad plus additional face buttons, and an ICs for power/USB.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a personal project repo, not a store or crowd-sourced badge list entry, so no price/quantity/availability information exists to find. No display panel, LED, or battery specs are stated anywhere in the repo (the badge clearly drives some kind of screen to show DOOM, but the specific part is never named). No secondary coverage (Hackaday, forums, social posts) of this specific board was found; the only source is the maker's own GitHub repository. Commit history ("Started badge" -> "Ready to start PCB" -> "I guess I'm going to defcon") suggests it was built and brought to DEF CON 32 in 2024.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc32/untitled-electronics-def-con-32-badge.glb
  method: kicad
  source_file: Badges/Defcon32/Schematics/MilkTastic.kicad_pcb
  generated: '2026-09-07'
  bytes: 269552
---

wrickert (who also builds badges under the name Untitled Electronics, and made the DC31 0xCafebabe badge and the DC33 NeoSword) built this handheld badge for DEF CON 32 in 2024. Internally the KiCad project is named "MilkTastic." The board is built around a Milk-V Duo module — a small RISC-V (Sophgo/CVITEK CV1800B/CV1801B) Linux-capable SoC board — and is laid out like a small game controller, with four tactile switches arranged as a D-pad plus additional face buttons.

The badge's software runs a buildroot Linux image on the Milk-V Duo and boots into fbDOOM, a framebuffer port of Doom, so the badge plays Doom using its own D-pad and buttons. The repository includes a full RISC-V toolchain and buildroot SDK checkout alongside the game files, and the board exposes a USB-Ethernet gadget interface for development access.

## Make your own

Everything needed to build one is published: the KiCad schematic, PCB layout, Gerbers, drill files and a bill of materials for the "MilkTastic" board (in `Badges/Defcon32/Schematics`), FreeCAD/STEP/3MF files for a 3D-printable D-pad and front panel (in `Badges/Defcon32/Cad`), and the Linux buildroot SDK plus fbDOOM/DOOM.WAD used to run the game (in `Badges/Defcon32/Linux`). No separate written build guide was found in the repo.
