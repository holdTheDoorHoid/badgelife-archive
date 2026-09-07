---
title: Gold Star Shitty Add-On
id: other-gold-star-shitty-add-on
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: greymanhw
  url: https://github.com/greymanhw
summary: 'An analog LED-chaser SAO: a NE555 timer clocks a 4017 decade counter to light 10 LEDs in sequence, star-shaped, no microcontroller.'
functions: 'Lights ten LEDs one at a time in a repeating chase pattern, driven purely by 555/4017 analog logic (no firmware).'
look:
  colors: []
  shape: star
  themes: []
tech:
  mcu: none
  leds:
    count: 10
    type: discrete
    note: 10 individual LEDs (D1-D10) sequenced by a CD4017 decade counter clocked by an NE555 timer.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/greymanhw/gold-star
  firmware_url: null
  eda_tool: KiCad
notes: []
links:
- label: github.com/greymanhw/gold-star
  url: https://github.com/greymanhw/gold-star
  kind: repo
images: []
contact: {}
status: unknown
sources:
- kind: url
  url: https://github.com/greymanhw/gold-star
  title: Gold Star Shitty Add-On
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://raw.githubusercontent.com/greymanhw/gold-star/master/README.md
  title: 'greymanhw/gold-star: README.md'
  accessed: '2026-09-07'
  note: 'README is just the project name, no other details.'
- kind: url
  url: https://raw.githubusercontent.com/greymanhw/gold-star/master/gold-star.sch
  title: 'greymanhw/gold-star: gold-star.sch (KiCad schematic)'
  accessed: '2026-09-07'
  note: 'Schematic shows NE555 + 4017 LED chaser driving 10 LEDs (D1-D10) through a Badgelife SAO v1.69bis 6-pin connector; confirms no MCU and the LED count/type.'
- kind: url
  url: https://api.github.com/repos/greymanhw/gold-star/contents/
  title: 'greymanhw/gold-star: repository file listing'
  accessed: '2026-09-07'
  note: 'gold-star.kicad_pcb is a 51-byte KiCad placeholder ("dummy file") with no actual board layout, so only the schematic and a star.svg graphic are real design content; no Gerbers or finished PCB exist in the repo.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    The repository (github.com/greymanhw/gold-star) contains a KiCad schematic and a
    star.svg graphic but no completed PCB layout (the .kicad_pcb file is an empty
    placeholder), and no README beyond the project title. No event, year, price,
    quantity, availability, storefront listing, Hackaday post, or photo of a built unit
    could be found anywhere online (web search and greymanhw.com, which was unreachable,
    turned up nothing). It is unclear whether this SAO was ever fabricated or given out
    at a specific convention, or remains an unfinished/unreleased design. The maker's
    GitHub bio reads "#badgelife" and lists two other unrelated ESP32 project repos, but
    none reference this add-on.
last_modified_date: '2026-09-07'
---

The Gold Star Shitty Add-On is a badgelife-style SAO (Shitty Add-On) designed by GitHub user greymanhw. Its schematic shows a purely analog LED chaser: an NE555 timer generates a clock signal that drives a CD4017 decade counter, which lights ten discrete LEDs (D1 through D10) one after another in sequence. There is no microcontroller — the chasing effect comes entirely from the 555/4017 combination — and the board draws power from its host badge through a standard 6-pin Badgelife SAO v1.69bis connector. The board is shaped like a star, matching the "gold star" name, based on an included star.svg graphic in the repository.

The repository itself is minimal: a bare-bones README that states only the project name, a KiCad schematic, the star graphic, and an MIT license, but the accompanying `.kicad_pcb` file is an empty placeholder rather than a real board layout, meaning no finished PCB design (and no Gerbers) is actually present. No event, year, price, quantity produced, or availability information could be found for this add-on on the repository, in web searches, or on the maker's personal site (which did not respond). It is not clear whether this SAO was ever manufactured, distributed at a convention, or remains an unfinished concept design.
