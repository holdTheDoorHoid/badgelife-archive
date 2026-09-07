---
title: Mr Fixit
id: other-mr-fixit-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2019
makers:
- name: Tom Keddie
  url: https://github.com/TomKeddie
summary: A single-LED art SAO by Tom Keddie shaped like a cartoon repairman in red solder mask with a gold HASL outline, whose handheld multimeter display lights up from the SAO connector's 3.3 V rail; first designed and manufactured in November 2019 (v1.0/v1.1) and re-spun as rev 1.3 in September 2024.
functions: 'Purely decorative: one LED behind a cut-out "screen" on the meter the character is holding lights up when the SAO is plugged into a badge, powered from the SAO connector''s 3.3 V rail. No microcontroller or other interactivity.'
look:
  colors:
  - red
  - gold
  shape: null
  themes:
  - hardware tool
  - measurement
tech:
  mcu: none
  leds:
    count: 1
    type: null
    note: Single LED lights the multimeter's display cut-out; no driver IC.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/TomKeddie/prj-pcb-experiments/tree/master/mr-fixit
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/TomKeddie/prj-pcb-experiments/tree/master/mr-fixit
  url: https://github.com/TomKeddie/prj-pcb-experiments/tree/master/mr-fixit
  kind: repo
- label: github.com/TomKeddie/prj-pcb-experiments
  url: https://github.com/TomKeddie/prj-pcb-experiments
  kind: repo
- label: github.com/TomKeddie
  url: https://github.com/TomKeddie
  kind: repo
images:
  - file: assets/images/badges/other/mr-fixit-sao/8e1f5cecb2.jpg
    source: "https://github.com/TomKeddie/prj-pcb-experiments/tree/master/mr-fixit"
    credit: "Tom Keddie"
    caption: "Assembled Mr Fixit SAO, lit up"
  - file: assets/images/badges/other/mr-fixit-sao/0b13e2f741.png
    source: "https://github.com/TomKeddie/prj-pcb-experiments/tree/master/mr-fixit"
    credit: "Tom Keddie"
    caption: "Mr Fixit PCB artwork (silkscreen/mask study)"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/TomKeddie/prj-pcb-experiments/tree/master/mr-fixit
  title: prj-pcb-experiments/mr-fixit at master · TomKeddie/prj-pcb-experiments
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://api.github.com/repos/TomKeddie/prj-pcb-experiments/contents/mr-fixit
  title: mr-fixit directory listing (GitHub API)
  accessed: '2026-09-07'
  note: Confirmed KiCad project files, gerbers, mrfixit-v1.0.zip and mrfixit-v1.1.zip archives, and a 2024-09-16 re-export of the board, supporting the v1.0/v1.1 (2019) and rev-1.3-era (2024) dates already in the summary.
- kind: url
  url: https://raw.githubusercontent.com/TomKeddie/prj-pcb-experiments/master/mr-fixit/images/IMG_20191210_090121.jpg
  title: IMG_20191210_090121.jpg
  accessed: '2026-09-07'
  note: Photo of the assembled SAO, dated December 2019; confirms shape, red/gold coloring, and the single lit LED behind the multimeter's display cutout. Used as the primary image.
- kind: url
  url: https://talk.vanhack.ca/t/pcbs-for-tom-keddie-projects-free/11237
  title: PCB's for Tom Keddie Projects (Free) - VHS Talk - Vancouver Hack Space
  accessed: '2026-09-07'
  note: Indicates Tom Keddie (Vancouver Hack Space member) has given away PCBs from his personal projects there; no mention of a specific convention tied to Mr Fixit, so event/price/quantity could not be confirmed.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: This is a personal hobby project in Tom Keddie's general PCB-experiments repo, not tied to any documented convention, storefront, or price/quantity information — extensive web searches (title+maker, maker+SAO, maker+badgelife) turned up nothing beyond the GitHub repo itself and one unrelated Vancouver Hack Space forum post about Keddie giving away PCBs generally. No README or project post describes what event, if any, it was made for, so event is left as "other" rather than guessed. The repo contains mrfixit-v1.0.zip and mrfixit-v1.1.zip (matching the Nov/Dec 2019 build) plus dated KiCad re-exports from September 2024, consistent with the "rev 1.3" respin mentioned in the pre-existing summary, but no changelog text was found to confirm what changed between revisions.
last_modified_date: '2026-09-07'
---

Mr Fixit is a small single-LED art SAO by Tom Keddie (Vancouver-based hobbyist and hardware engineer), cut into the outline of a cartoon repairman in red solder mask with a gold HASL/ENIG finish tracing his overalls, hair, and tool belt. He holds up a handheld multimeter whose display is a cutout window backed by one LED; plugged into a host badge's SAO header, the 3.3 V rail lights that single LED so the "screen" glows, giving the character the look of taking a reading. There is no microcontroller, driver chip, or other logic on the board — it is a passive decorative add-on.

The GitHub repository (`TomKeddie/prj-pcb-experiments`, `mr-fixit` folder) holds the full KiCad source, gerbers, and two dated firmware-free hardware archives, `mrfixit-v1.0.zip` and `mrfixit-v1.1.zip`; assembled-board photos in the repo are dated December 10, 2019, matching that first build. A further set of dated KiCad exports from September 16, 2024 shows the board was revisited and re-exported around that time, consistent with a later "rev 1.3" respin, though no accompanying notes explain what changed. No convention, storefront, price, or production-quantity information could be found for this SAO — it appears to be a personal project shared through Keddie's own repo rather than sold or distributed through a specific event, so those fields are left blank rather than guessed.

## Make your own

The `mr-fixit` folder in `TomKeddie/prj-pcb-experiments` contains the complete KiCad project (schematic, PCB, footprint and symbol library tables), pre-generated gerbers, a mechanical drawing PDF, and DXF/SVG artwork of the character outline, along with a `Makefile` that regenerates gerbers, BOM, and JLCPCB-format files via `kicad-cli`. No firmware is needed since the board is passive.
