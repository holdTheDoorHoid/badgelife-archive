---
title: Mr Fixit SAO
id: supercon-2024-mr-fixit-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: TomKeddie
  url: https://hackaday.io/tomkeddie
summary: A decorative Simple Add-On (SAO) whose artwork is a photograph Tom Keddie took in Munich, edited to remove distracting shapes from a vehicle in the frame so the image reads cleanly at small size.
functions: 'Decorative only: displays the edited photo as PCB artwork. No stated interactive functions.'
look:
  colors: []
  shape: rectangle
  themes:
  - art
tech:
  mcu: null
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
  distribution:
  - contest
  where: Entered in the Supercon 8 (2024) SAO Contest; no storefront or giveaway details found.
make_your_own:
  open_source: true
  hardware_url: https://github.com/tomkeddie/prj-pcb-experiments/tree/master/mr-fixit
  firmware_url: null
  gerbers_url: https://github.com/tomkeddie/prj-pcb-experiments/tree/master/mr-fixit/gerbers
  eda_tool: KiCad
links:
- label: hackaday.io/project/198222-mr-fixit-sao
  url: https://hackaday.io/project/198222-mr-fixit-sao
  kind: hackaday
- label: tomkeddie/prj-pcb-experiments (mr-fixit)
  url: https://github.com/tomkeddie/prj-pcb-experiments/tree/master/mr-fixit
  kind: repo
images:
- file: assets/images/badges/supercon-2024/mr-fixit-sao/b6fe40e6dc.jpg
  source: https://hackaday.io/project/198222-mr-fixit-sao
  credit: TomKeddie
  caption: Mr Fixit SAO, front artwork
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198222-mr-fixit-sao
  title: Mr Fixit SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 8 SAO Contest entry''.'
- kind: url
  url: https://hackaday.io/project/198222-mr-fixit-sao
  title: Mr Fixit SAO - Hackaday.io project page
  accessed: '2026-09-07'
  note: Confirmed maker (TomKeddie), event (Supercon 8 SAO Contest, created Oct 2024), and that the artwork is an edited Munich photograph; also source of the og:image photo saved to images.
- kind: url
  url: https://github.com/tomkeddie/prj-pcb-experiments/tree/master/mr-fixit
  title: prj-pcb-experiments/mr-fixit on GitHub
  accessed: '2026-09-07'
  note: Confirmed KiCad hardware design (schematic, PCB, gerbers, v1.0/v1.1 archives) published open source; no firmware or BOM found; no README describing MCU/LEDs.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Event corrected from supercon-2025 to supercon-2024: the Hackaday.io page states this was made for the "Supercon 8: SAO Contest" (created Oct 2024), and Supercon 8 is Supercon 2024. No MCU, LED, or connectivity details were found on the project page or in the visible GitHub file listing (no README); the board reads as passive PCB art rather than an active electronic SAO, but that is not confirmed by any source, so tech fields are left null. Price, quantity, and distribution beyond "contest entry" were not found.'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/supercon-2025/mr-fixit-sao/
model:
  file: assets/models/supercon-2024/mr-fixit-sao.glb
  method: kicad
  source_file: mr-fixit/mrfixit.kicad_pcb
  generated: '2026-09-10'
  bytes: 475608
---

Mr Fixit SAO is a Simple Add-On built by Tom Keddie (hackaday.io/tomkeddie) for the Supercon 8 SAO Contest in 2024. The board's artwork is a photograph Keddie took in Munich; he described editing out distracting shapes from a vehicle in the frame so the image would read cleanly once reproduced on the small PCB.

The design is published as open hardware on GitHub under `tomkeddie/prj-pcb-experiments/mr-fixit`, with a KiCad schematic and PCB, a custom footprint library, gerbers, mechanical exports (DXF/PDF), and v1.0/v1.1 release archives. No firmware, bill of materials, or README was found in the repository, and the Hackaday.io project page does not list a chip, LEDs, price, or quantity, so those fields are left empty rather than guessed.

## Make your own

Hardware files (schematic, PCB, gerbers) are in the `mr-fixit` folder of https://github.com/tomkeddie/prj-pcb-experiments, including a `Makefile` for building outputs and pre-generated gerbers for fabrication.
