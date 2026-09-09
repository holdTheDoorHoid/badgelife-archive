---
title: Ghibli/Soot Sprites
id: other-ghibli-soot-sprites-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A susuwatari (Studio Ghibli soot sprite) simple add-on by davedarko, one of many small gift SAOs in his "Simple-Add-ons-SAO" repository; no event or year is stated for it.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - anime
  - movie
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: CR2032
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Ghibli/Soot%20Sprites
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/Ghibli
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Ghibli
  kind: repo
- label: Simple Add-ons (SAO) — Hackaday.io
  url: https://hackaday.io/project/175182-simple-add-ons-sao
  kind: hackaday
  archived: https://web.archive.org/web/20260523064211/https://hackaday.io/project/175182-simple-add-ons-sao
- label: Project page (Hackaday.io)
  url: https://hackaday.io/project/205207-soot-sprite-simple-add-on-sao
  kind: project
images: []
contact: {}
notes:
- 'Sheet/repo readme lists this design as "Eagle: yes, Kicad: -", but the only hardware files actually present in the repo folder are a full KiCad project (schematic, PCB, and a Gerber/production zip) — no Eagle files are in the folder. Treated the KiCad files as authoritative.'
status: listed
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/README.md
  title: Simple-Add-ons-SAO README
  accessed: '2026-09-07'
  note: Repo-wide table lists "Ghibli/Soot Sprites | SAO | yes(Eagle) | - | A susuwatari simple add-on"; describes the shared v1.69bis 2x3-pin SAO header used across all designs in the repo; no event/year given for this item.
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Ghibli/Soot%20Sprites
  title: Ghibli/Soot Sprites design folder
  accessed: '2026-09-07'
  note: 'File listing (via GitHub API): a KiCad project (soot.kicad_sch/.kicad_pcb/.kicad_pro, plus a production Gerber zip and IPC netlist), a "Kompeito.scad" OpenSCAD model (a candy-shaped part with a socket for a discrete LED), and several vector-art SVGs. No photos of the finished board were found.'
- kind: url
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/Ghibli/Soot%20Sprites/soot/soot.kicad_sch
  title: soot.kicad_sch (schematic source)
  accessed: '2026-09-07'
  note: Schematic contains only a CR2032 battery holder (BT1), one resistor (R1), the 2x3 SAO header (J1), test points, and power symbols — no MCU and no LED footprint on the PCB itself, confirmed by cross-checking the .kicad_pcb footprint list.
- kind: url
  url: https://hackaday.io/project/175182-simple-add-ons-sao
  title: Simple Add-ons (SAO) — Hackaday.io
  accessed: '2026-09-07'
  note: Davedarko's umbrella Hackaday.io page for the SAO standard and his badge collection; does not mention the Ghibli/Soot Sprites design specifically, but is the maker's own reference page for the standard this board uses.
  archived: https://web.archive.org/web/20260523064211/https://hackaday.io/project/175182-simple-add-ons-sao
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all cited sources (repo root, README table, the Ghibli/Soot Sprites folder and its nested soot/ subfolder and production/ subfolder, the soot.kicad_sch and soot.kicad_pcb source, and the Hackaday.io SAO page) and confirmed every remaining claim -- the README''s Eagle-only claim for this design conflicting with the actual KiCad files present, the schematic/PCB parts list (BT1 CR2032 holder, R1, J1 2x3 header, TP1-4, no LED, no MCU), the production/ subfolder holding netlist.ipc and soot.zip, and the Kompeito.scad candy shell with an LED socket cutout. No event, year, price, quantity, or availability is stated anywhere for this item, so event was left as "other" per the research guide. No photo of the assembled board was found; the repo only contains CAD/vector source files, so no images could be saved. tech.leds is left empty since the discrete-LED-in-3D-printed-shell setup is inferred from separate design files rather than stated directly
    by the maker.'
last_modified_date: '2026-09-07'
---

The Ghibli/Soot Sprites SAO is a small conference-badge add-on by the hardware designer davedarko (GitHub/Hackaday.io), modeled on the susuwatari — the round, black, dust-bunny-like soot sprites from Studio Ghibli films such as *Spirited Away* and *My Neighbor Totoro*. It lives in his "Simple-Add-ons-SAO" repository alongside more than a dozen other small SAO and pin designs he has given away over the years, built around the shared 2x3-pin (v1.69bis) SAO header he documents in that repo. No convention or year is stated for this particular design, so it reads as one of his general personal-gift boards rather than a badge made for a specific event.

The published hardware is a complete KiCad project — schematic, PCB layout, and a production Gerber/netlist bundle — for a very simple board: a 2x3 SAO edge connector, a CR2032 coin-cell holder and a single resistor, with no microcontroller and no LED footprint on the PCB itself. A companion OpenSCAD file, "Kompeito," models a bumpy, candy-like 3D-printable shell (named for the Japanese sugar candy) with a socket sized for a discrete LED, suggesting the finished piece pairs the bare PCB with a 3D-printed soot-sprite body and a separately wired LED rather than relying on surface-mount lighting. No photos of an assembled unit, pricing, or distribution details were found in the repository or in a web search.

## Make your own

The full KiCad source (schematic, PCB, and a ready-to-fab production/Gerber zip) is in the `Ghibli/Soot Sprites` folder of https://github.com/davedarko/Simple-Add-ons-SAO, along with the `Kompeito.scad` OpenSCAD file for 3D-printing the candy-shaped shell that houses the LED.
