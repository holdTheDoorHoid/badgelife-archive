---
title: Featuring You!
id: supercon-2024-featuring-you-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Nanik Adnani (nanikgeorge)
  url: https://www.nanik.ca
summary: An SAO shaped like a big red flashing arrow sign that gives Supercon badges a spot to display the wearer's name, designed by Nanik Adnani to share at Hackaday Supercon 2024.
functions: 'Flashes an LED chase/arrow pattern to draw attention to the wearer''s name; no interactivity beyond the flashing display.'
look:
  colors:
  - red
  shape: arrow
  themes:
  - text
  - minimalist
tech:
  mcu: none
  leds:
    count: 32
    type: discrete
    note: 0603 discrete LEDs driven by an astable-multivibrator-style transistor chase circuit (no microcontroller).
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
  open_source: partial
  hardware_url: https://github.com/nanikgeorge/FeaturingYouSAO/tree/main/MovieMarqueeSAO_KiCAD
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/nanikgeorge/FeaturingYouSAO
  url: https://github.com/nanikgeorge/FeaturingYouSAO
  kind: repo
- label: github.com/nanikgeorge
  url: https://github.com/nanikgeorge
  kind: repo
- label: nanik.ca (maker portfolio)
  url: https://www.nanik.ca
  kind: website
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/nanikgeorge/FeaturingYouSAO
  title: Featuring You! SAO (nanikgeorge/FeaturingYouSAO)
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://raw.githubusercontent.com/nanikgeorge/FeaturingYouSAO/main/README.md
  title: FeaturingYouSAO README
  accessed: '2026-09-07'
  note: Confirms it is an SAO designed for Hackaday Supercon 2024, shaped like a flashing arrow sign for displaying the wearer's name; maker was speaking at Supercon 2024.
- kind: url
  url: https://raw.githubusercontent.com/nanikgeorge/FeaturingYouSAO/main/MovieMarqueeSAO_KiCAD/MovieMarqueeSAO.kicad_pcb
  title: MovieMarqueeSAO.kicad_pcb
  accessed: '2026-09-07'
  note: KiCad PCB file confirms no MCU; the board is a discrete analog circuit with 4x MMBT3904 transistors driving 32 discrete (0603) LEDs in a chase/flasher arrangement, the internal project name is "MovieMarqueeSAO".
- kind: url
  url: https://www.nanik.ca/projects
  title: Nanik Adnani portfolio - Projects
  accessed: '2026-09-07'
  note: Lists "Featuring You! SAO" as a Supercon 2024 project, describing it as a quick analog (no-microcontroller) circuit with a big flashing arrow displaying the wearer's name; links back to the same GitHub repo. No photo of the assembled hardware could be reliably identified on this page (a Google Sites export with many unlabeled background images).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Core facts (what it is, maker, event/year, that it is a discrete analog circuit with
    no MCU) are confirmed by the maker's own repo and portfolio site. Price, quantity made,
    and availability/distribution were not stated anywhere found and are left empty. No
    photo of the assembled/soldered SAO could be located: the GitHub repo only contains
    SVG artwork (board edge and silkscreen), not photos, and the maker's portfolio page
    is a minified Google Sites export where dozens of background images could not be
    reliably matched to this specific project, so no image was saved to avoid guessing.
    hardware_url points at the KiCad folder (schematics/PCB); make_your_own.open_source
    is 'partial' because no firmware exists to publish (it's a non-MCU analog board) but
    full hardware design files (KiCad zip + PCB) are shared, along with LTSpice
    simulation files for the flasher circuit.
last_modified_date: '2026-09-07'
---

"Featuring You!" is a shitty add-on (SAO) designed by Nanik Adnani (an analog mixed-signal designer) to share at Hackaday Supercon 2024. The idea grew out of a simple complaint: Supercon badges are great, but they rarely have anywhere to put the wearer's name. Adnani's fix is a small board shaped like one of those big red flashing theater-marquee arrows, meant to "feature" whoever is wearing it.

Unlike most SAOs, it has no microcontroller. The KiCad design shows a purely discrete analog circuit: four MMBT3904 transistors arranged in astable-multivibrator-style chase stages, driving 32 individual 0603 LEDs to produce the arrow's flashing/chasing light pattern. The project also includes LTSpice simulation files for that flasher circuit and SVG artwork for the board edge and silkscreen (the internal project name in the files is "MovieMarqueeSAO").

The hardware design (KiCad project and PCB files) is published on GitHub, but there is no firmware to share since the board runs no code. Price, production quantity, and how (or whether) it was distributed beyond Supercon 2024 attendees were not stated in any source found.
