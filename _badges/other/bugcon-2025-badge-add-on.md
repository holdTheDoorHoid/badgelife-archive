---
title: BugCON 2025 Badge Add-On (Barrio del Hardware)
id: other-bugcon-2025-badge-add-on
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: other
year: 2025
makers:
- name: Electronic Cats
summary: A small expansion board for the BugCON 2025 Linux badge, built around a Puya PY32F002A microcontroller and carrying custom "Barrio del Hardware" silkscreen artwork.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: PY32F002A
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
  open_source: true
  hardware_url: https://github.com/ElectronicCats/badge-bugcon-2025/tree/main/hardware/Add_On_Bugcon_2025
  firmware_url: https://github.com/ElectronicCats/badge-bugcon-2025/tree/main/hardware/Add_On_Bugcon_2025/firmware
  eda_tool: KiCad
links:
- label: github.com/ElectronicCats/badge-bugcon-2025/tree/main/hardware/Add_On_Bugcon_2025
  url: https://github.com/ElectronicCats/badge-bugcon-2025/tree/main/hardware/Add_On_Bugcon_2025
  kind: website
- label: badge-bugcon-2025 (repo root README)
  url: https://github.com/ElectronicCats/badge-bugcon-2025
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- Sheet/original title was "BugCON 2025 Badge Add-On"; the board files name it "Add_On_Barrio_del_Hardware", so the title here adds that name in parentheses.
status: listed
sources:
- kind: url
  url: https://github.com/ElectronicCats/badge-bugcon-2025/tree/main/hardware/Add_On_Bugcon_2025
  title: BugCON 2025 Badge Add-On
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/ElectronicCats/badge-bugcon-2025
  title: Badge BugCon 2025 (repo README)
  accessed: '2026-09-10'
  note: Confirms this is a companion expansion board to the main BugCon 2025 Linux badge; gives its MCU (PY32F002AA15M) and describes it as "decorative custom design".
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: 'Confirmed to exist as a real hardware design in Electronic Cats'' badge-bugcon-2025 repo, but only design-file metadata was found, not a product page, photo, or writeup. The repo README (in Spanish) says the add-on is "a expansion board that includes a PY32F002AA15M microcontroller, additional components for extended capabilities, and a custom decorative design" — no further detail on what those extended capabilities are (no LEDs, display, or connectivity confirmed either way). The board files are named "Add_On_Barrio_del_Hardware", suggesting it ties into a "Barrio del Hardware" village/theme at BugCON rather than being a general-purpose add-on; this is inferred from filenames, not stated outright. No pricing, quantity, or distribution information was found — this looks like it may not have been sold separately at all, possibly a village giveaway or badge-bundle extra, but that is not confirmed. No photo of the assembled board was found; the repo has only KiCad source files and
    an SVG silkscreen artwork file (not a product photo, so not saved as an image here). BugCON itself: a hacker/hardware conference (the badge repo describes it as for "hackers, developers and technology enthusiasts"); no explicit city/date found in the fetched pages, and no matching event id exists yet in events.yml, so event is left as "other".'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/bugcon-2025-badge-add-on.glb
  method: kicad
  source_file: hardware/Add_On_Bugcon_2025/Add_On_Barrio_del_Hardware.kicad_pcb
  generated: '2026-09-10'
  bytes: 146992
---

The BugCON 2025 Badge Add-On is a small expansion board that plugs into (or accompanies) Electronic Cats' main BugCON 2025 badge, itself a Linux-capable badge built around a Rockchip RV1106G3 processor. Where the main badge handles the heavy lifting, this add-on is a separate PCB carrying a Puya PY32F002A microcontroller, described by the maker only as adding "additional components for extended capabilities" alongside a "custom decorative design."

The board's design files in the GitHub repository are named "Add_On_Barrio_del_Hardware," which suggests the add-on is tied to a "Barrio del Hardware" (Hardware Neighborhood) theme or village at the event rather than being a standalone accessory sold on its own — though no page was found that spells this out directly. All design files (KiCad schematic and PCB layout, plus a PY32F0-based firmware template) are published in the same repository as the main badge, but no assembly guide, bill of materials, price, or photo of the finished board could be found.

## Make your own

Hardware files (KiCad schematic, PCB, and a custom footprint library) and a PY32F0 firmware template are in the `hardware/Add_On_Bugcon_2025` folder of the `badge-bugcon-2025` GitHub repository. The firmware side is a fork of the generic `py32f0-template` project adapted for Windows toolchains, targeting the Puya PY32F002A/PY32F003/PY32F030 family via a J-Link programmer.
