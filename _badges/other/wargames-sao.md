---
title: WarGames_SAO
id: other-wargames-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: joshajohnson
  url: https://github.com/joshajohnson
summary: A charlieplexed-LED SAO themed around the 1983 film WarGames, with 18 LEDs (bicolor pairs across a 3x3 grid) forming a tic-tac-toe / "Global Thermonuclear War" motif and a hidden "Shall We Play A Game?" copper-layer callout.
functions: Steps through 15 preprogrammed lighting patterns across a charlieplexed 3x3 grid of bicolor LED pairs (18 LEDs total, 2 per grid position), driven by a PIC microcontroller.
look:
  colors: []
  shape: null
  themes:
  - movie
  - retro computer
  - puzzle
tech:
  mcu: PIC12F1571
  leds:
    count: 18
    type: charlieplexed
    note: 18 discrete SMD LEDs (D1-D18) wired as 9 bicolor pairs in a 3x3 tic-tac-toe grid, charlieplexed across the PIC's GPIO pins through 5 shared 330-ohm resistors (R1-R5); not addressable/WS2812-style.
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
  open_source: true
  hardware_url: https://github.com/joshajohnson/WarGames_SAO/tree/master/hardware
  firmware_url: https://github.com/joshajohnson/WarGames_SAO/tree/master/firmware.X
  eda_tool: KiCad
  license: GPL-3.0
  fab_url: null
  notes: Repo includes KiCad schematic/PCB/gerbers (with a gerbers_SAO_panel folder) and an MPLAB X/XC8 firmware project for the PIC12F1571.
links:
- label: github.com/joshajohnson/WarGames_SAO
  url: https://github.com/joshajohnson/WarGames_SAO
  kind: repo
images: []
contact: {}
notes:
- War Games themed
- Repository created 2019-01-19; no specific convention or year is named anywhere in the repo, so the event/year this SAO was made for could not be confirmed from sources.
status: listed
sources:
- kind: url
  url: https://github.com/joshajohnson/WarGames_SAO
  title: WarGames_SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/joshajohnson/WarGames_SAO
  title: joshajohnson/WarGames_SAO
  accessed: '2026-09-07'
  note: README and repo description ("A War Games themed shitty add on"), GPL-3.0 license, repo folders (firmware.X, hardware).
- kind: url
  url: https://api.github.com/repos/joshajohnson/WarGames_SAO
  title: WarGames_SAO (GitHub API metadata)
  accessed: '2026-09-07'
  note: Repo created 2019-01-19, last updated 2023-01-23, license GPL-3.0, no topics set.
- kind: url
  url: https://raw.githubusercontent.com/joshajohnson/WarGames_SAO/master/firmware.X/main.c
  accessed: '2026-09-07'
  note: Firmware source confirms PIC12F1571 target, 32MHz internal oscillator, a comment stating the LEDs "are charlieplexed", a displayLED() function driving 9 grid positions in 2 colors each via 5 GPIO pins, and a 15-entry table of 9-position sequences (NUM_STATES 15).
- kind: url
  url: https://raw.githubusercontent.com/joshajohnson/WarGames_SAO/master/hardware/WarGames_SAO.kicad_pcb
  accessed: '2026-09-07'
  note: PCB source shows 18 LED footprints (D1-D18) and 5 shared 330-ohm resistor footprints (R1-R5), consistent with a charlieplexed 3x3 grid of bicolor LED pairs; also a PIC12F1571 footprint, a PICKit3 programming header, and a hidden copper-layer text module reading "Shall We Play A Game?" (a WarGames movie quote).
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Only source available is the maker''s own GitHub repo; no Hackaday post, storefront, social media mention, or photo of the assembled board could be found (web search budget was exhausted after one query). Event, year, price, quantity made, and availability are not stated anywhere in the repo and are left blank rather than guessed. The repo was created 2019-01-19, which is consistent with (but does not confirm) an early-2019 con such as ShmooCon 2019. Fact-check correction: the prior draft said 9 discrete LEDs each with its own resistor; the PCB source (D1-D18, R1-R5) and firmware source (main.c comment "as they are charlieplexed", displayLED() driving 2 colors per grid position) actually show 18 LEDs wired as 9 charlieplexed bicolor pairs sharing 5 resistors. Fields were corrected accordingly and all remaining sentences/fields were re-checked against the cited sources.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/wargames-sao.glb
  method: kicad
  source_file: hardware/WarGames_SAO.kicad_pcb
  generated: '2026-09-10'
  bytes: 138384
---

WarGames_SAO is a "shitty add-on" (SAO) made by joshajohnson, themed around the 1983 film *WarGames*. It is built around a PIC12F1571 microcontroller running at 32 MHz, driving 18 LEDs wired as 9 charlieplexed bicolor pairs across a 3x3 grid (sharing just 5 resistors between them) that step through 15 preprogrammed lighting patterns — evoking the tic-tac-toe board the film's WOPR computer plays against itself while simulating "Global Thermonuclear War." The board's hidden copper-layer artwork includes the line "Shall We Play A Game?", a direct quote from the movie.

The hardware is designed in KiCad, with schematic, PCB, and gerber files (including a panelized gerber set) published in the maker's GitHub repository alongside an MPLAB X/XC8 firmware project, all under the GPL-3.0 license. No convention, year, price, production quantity, or availability could be confirmed from available sources — the repository itself does not name an event, and no press coverage, storefront listing, or photo of an assembled unit could be located.

## Make your own

The GitHub repository (linked above) contains everything needed to build one: KiCad schematic and PCB files plus ready-to-fab gerbers under `hardware/` (including a separate panelized gerber set), and the PIC12F1571 firmware source as an MPLAB X project under `firmware.X/`, licensed GPL-3.0.
