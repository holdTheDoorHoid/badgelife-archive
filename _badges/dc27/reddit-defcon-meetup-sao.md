---
title: reddit-defcon-meetup-SAO
id: dc27-reddit-defcon-meetup-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: patrickrb
  url: https://github.com/patrickrb
summary: A shitty-add-on shaped like Reddit's Snoo mascot, made for a Reddit meetup at DEF CON 27.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - mascot
  - meme
form_factor: pcb sao
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: CR2032
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
  hardware_url: https://github.com/patrickrb/reddit-defcon-meetup-SAO
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/patrickrb/reddit-defcon-meetup-SAO
  url: https://github.com/patrickrb/reddit-defcon-meetup-SAO
  kind: repo
images:
- file: assets/images/badges/dc27/reddit-defcon-meetup-sao/d9b44c360e.png
  source: https://github.com/patrickrb/reddit-defcon-meetup-SAO
  credit: patrickrb
  caption: Reddit Snoo meetup SAO, front
- file: assets/images/badges/dc27/reddit-defcon-meetup-sao/10f3c2b313.png
  source: https://github.com/patrickrb/reddit-defcon-meetup-SAO
  credit: patrickrb
  caption: Reddit Snoo meetup SAO, back
contact: {}
notes: []
status: unknown
sources:
- kind: url
  url: https://github.com/patrickrb/reddit-defcon-meetup-SAO
  title: reddit-defcon-meetup-SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 27''.'
- kind: url
  url: https://github.com/patrickrb/reddit-defcon-meetup-SAO
  title: patrickrb/reddit-defcon-meetup-SAO README
  accessed: '2026-09-07'
  note: README confirms it is a SAO for a reddit meetup at DEF CON 27, describes CR2032 + SAO connector, and includes two Imgur photos of the built board; repo also contains KiCad schematic/PCB files, gerbers, and Snoo-shaped SVG artwork.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source found is the maker''s own GitHub repo; no press coverage, storefront, or forum posts turned up. MCU, LED count/type, display, price, and quantity made are not documented anywhere in the repo and are left empty rather than guessed. Chip is unclear from the repo''s schematic library alone without opening the KiCad files, so tech.mcu is left null. Fact-check correction (2026-09-07) — status was changed from released to unknown: the repo confirms design files and a README description of the SAO''s purpose, but nothing in it states the board was actually fabricated and handed out at the meetup, so ''released'' (people have it) was unsupported. The two saved images are the KiCad 3D-viewer renders embedded in the README, not photographs of a physically assembled board; the body text was corrected to say so instead of calling them photos.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc27/reddit-defcon-meetup-sao.glb
  method: kicad
  source_file: reddit-snoo-meetup.kicad_pcb
  generated: '2026-09-07'
  bytes: 80276
---

This is a shitty-add-on (SAO) made by GitHub user patrickrb for a Reddit meetup held at DEF CON 27 in 2019. It's shaped after Reddit's Snoo mascot and was designed to plug into a badge's SAO header, with an alternate CR2032 coin-cell connector for standalone power (the maker's own README jokes that using both power sources at once is "probably not a good idea").

The hardware is fully open source: the repository holds KiCad schematic and PCB files, gerbers ready for fabrication, and SVG artwork for the Snoo-shaped board outline, along with two KiCad 3D-render images of the board design (front and back). Beyond the repository itself, no press coverage, storefront listing, or social posts about this SAO were found, so whether it was actually fabricated and handed out at the meetup, along with details like the microcontroller, LED count, price, and production quantity, remains undocumented.
