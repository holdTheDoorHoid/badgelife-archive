---
title: tr23-sao-hw — Troopers 2023 Shitty Add-On
id: other-tr23-sao-hw-troopers-2023-shitty-add-on
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: jeffmakes
summary: A DIY RGB shitty add-on made for Troopers 2023, sold/given as a partial kit — only the LED driver chip is factory-assembled, and the recipient hand-solders their own LEDs.
functions: Lights up RGB LEDs on command over I2C from the host badge; the specific LED pattern depends on what the builder solders on and how the host drives it.
look:
  colors:
  - white
  - black
  shape: null
  themes:
  - console
tech:
  mcu: none
  leds:
    count: null
    type: RGB
    note: Driven by a Kinetic Technologies KTD2052 I2C RGB LED driver (DFN-8, the only part populated at the factory); an LP5018 driver datasheet is also included in the repo as a considered alternative. The actual LEDs are chosen and hand-soldered by the recipient, so their count and type vary per board.
  display: none
  connectivity:
  - i2c
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
  hardware_url: https://github.com/jeffmakes/tr23-sao-hw
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/jeffmakes/tr23-sao-hw
  url: https://github.com/jeffmakes/tr23-sao-hw
  kind: repo
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/jeffmakes/tr23-sao-hw
  title: tr23-sao-hw — Troopers 2023 Shitty Add-On
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''Troopers 2023''.'
- kind: url
  url: https://api.github.com/repos/jeffmakes/tr23-sao-hw/git/trees/main?recursive=1
  title: 'jeffmakes/tr23-sao-hw: full repository file tree'
  accessed: '2026-09-07'
  note: 'Repo contents: KiCad r1 hardware (schematic, PCB, Gerbers, drill files, pick-and-place, BOM), an ERNW logo SVG (ERNW organizes Troopers), a Nintendo Game Boy reference photo and a Wii-connector 3D standin used as design references, and driver-chip datasheets (KTD2052, LP5018).'
- kind: url
  url: https://raw.githubusercontent.com/jeffmakes/tr23-sao-hw/main/r1/build/README.txt
  title: tr23-sao-hw — r1/build/README.txt
  accessed: '2026-09-07'
  note: 'PCB spec (2-layer FR4 1.6mm, white soldermask, black silkscreen, HASL) and assembly note: "please only assemble U1. The rest of the board will be assembled by the user by hand."'
- kind: url
  url: https://raw.githubusercontent.com/jeffmakes/tr23-sao-hw/main/r1/src/tr23-sao-r1.csv
  title: tr23-sao-hw — r1 factory BOM (KiCad-generated)
  accessed: '2026-09-07'
  note: 'Confirms the only factory-placed part is U1, a Kinetic Technologies KTD2052AEVAA-TR RGB LED driver in a DFN-8 package; BOM source path shows the local project folder was "2023/tr23-badge/repos/tr23-sao-hw", tying the project to a 2023 badge effort.'
- kind: url
  url: https://github.com/jeffmakes
  title: jeffmakes — GitHub profile
  accessed: '2026-09-07'
  note: 'Confirms jeffmakes also published hardware for the Troopers19 badge (tr19-badge-hw-public) and a separate "fuccs-shitty-addon-hw" SAO, i.e. a track record of making Troopers conference badge hardware, supporting the Troopers 2023 event attribution. No mention of tr23-sao specifically, and no personal site or blog listed.'
- kind: url
  url: https://www.troopers.de/troopers23/
  title: TROOPERS23 conference page
  accessed: '2026-09-07'
  note: 'Checked for any mention of a conference badge or SAO; the page covers dates, training and CFP only and does not discuss badges or their makers.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No prose write-up or announcement page was found for this SAO — everything here is inferred from the maker''s own GitHub repository (jeffmakes/tr23-sao-hw): its description ("Shitty Add-On 2023"), an included ERNW logo (ERNW organizes the Troopers security conference in Heidelberg), and an internal build-folder path reading ".../2023/tr23-badge/repos/tr23-sao-hw" in the generated BOM. The `_data/events.yml` vocabulary has no Troopers event id yet (checked, none found for "troopers"), so `event` is left as `other`; if an id such as `troopers-2023` is ever added, this entry should move under it. Confirmed: it is a 6-pin-header-style RGB SAO where only the KTD2052 I2C LED driver chip is factory-assembled and the rest (LEDs, resistors) is meant to be hand-soldered by the recipient — a "build it yourself" kit rather than a finished blinky. Not found: price, quantity made, how/whether it was distributed to Troopers 2023 attendees, SAO header pin count, a license for the hardware files (no LICENSE file in the repo), and any photograph of an assembled unit. A Nintendo Game Boy product photo and a Wii-nunchuck-connector 3D model sit in the repo''s design folder as apparent visual/mechanical references (theme/fit checks), not photos of the finished board, so no images were saved for this entry.'
last_modified_date: '2026-09-07'
---

TR23 is a shitty add-on that jeffmakes designed for Troopers 2023, the ERNW-run security conference in Heidelberg, Germany — identified from the ERNW logo bundled in the project's design files and from a build path recorded in the generated bill of materials. Rather than shipping as a finished blinky, the board is a build-it-yourself kit: only a Kinetic Technologies KTD2052 I2C RGB LED driver chip (in a tiny DFN-8 package) comes assembled from the factory, and the recipient hand-solders their own choice of LEDs onto the remaining unpopulated footprints. The two-layer FR4 board uses a white soldermask with black silkscreen on both sides.

The repository includes full KiCad r1 design files — schematic, PCB layout, Gerbers, drill files, and pick-and-place data — along with datasheets for the KTD2052 and a second driver option (LP5018) that appears to have been evaluated. The design folder also holds a stock photo of a Nintendo Game Boy and a 3D standin for a Wii nunchuck-style connector, which look like visual and mechanical references used while designing the board rather than photos of a finished unit; no assembled-board photos or an announcement post were found. jeffmakes has previously published hardware for the Troopers19 badge, so this SAO continues that track record of building badge hardware for the same conference series.

## Make your own

The full r1 hardware design is on GitHub at jeffmakes/tr23-sao-hw, including the KiCad schematic and PCB (`r1/src/tr23-sao-r1.kicad_pcb`), ready-to-fab Gerbers and drill files, pick-and-place position CSVs, and an assembly BOM (`r1/build/`). The board's own README notes that only the KTD2052 LED driver (reference U1) needs to be professionally assembled; everything else is meant to be soldered on by hand.


