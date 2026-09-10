---
title: SAINTCON 2017 208 Mini Badge
id: saintcon-2017-saintcon-2017-208-mini-badge
layout: badge
parent: Saintcon 2017
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2017
year: 2017
makers:
- name: phrackd
summary: A DIY SAINTCON 2017 minibadge (number 208) built around an ATtiny13A driving 18 charlieplexed red/blue LEDs from just 5 GPIO pins.
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: ATtiny13A
  leds:
    count: 18
    type: charlieplexed
    note: Charlieplexed via 5 GPIO pins; red LEDs (Everlight CMDA6BR7D1S-100) and blue LEDs (Inolux/Harvatek HT-193NB-5589)
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
  hardware_url: https://github.com/phrackd/2017-208-saintcon-minibadge/tree/master/pcb
  firmware_url: https://github.com/phrackd/2017-208-saintcon-minibadge/tree/master/firmware
  eda_tool: KiCad
links:
- label: github.com/phrackd/2017-208-saintcon-minibadge
  url: https://github.com/phrackd/2017-208-saintcon-minibadge
  kind: repo
images: []
contact: {}
notes:
- Unofficial SAINTCON 2017 minibadge using an ATtiny13A to drive 18 charlieplexed LEDs, by phrackd. Found by the event-year sweep, task saintcon-2017.
status: listed
sources:
- kind: url
  url: https://github.com/phrackd/2017-208-saintcon-minibadge
  title: SAINTCON 2017 208 Mini Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2017); event read as ''saintcon-2017''.'
- kind: url
  url: https://github.com/phrackd/2017-208-saintcon-minibadge/blob/master/README.md
  title: 'README: SAINTCON 2017 208 Mini Badge'
  accessed: '2026-09-10'
  note: Confirmed maker, event, ATtiny13A MCU, 18 charlieplexed LEDs (red/blue variants), and part numbers.
- kind: url
  url: https://api.github.com/repos/phrackd/2017-208-saintcon-minibadge/git/trees/master?recursive=1
  title: Repository file tree
  accessed: '2026-09-10'
  note: Confirmed the repo publishes both KiCad PCB design files and AVR firmware source; no photos or renders present anywhere in the repo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Core facts (maker, event/number, ATtiny13A, 18 charlieplexed LEDs) confirmed directly from the maker's own GitHub repo, which publishes complete open-source PCB (KiCad) and firmware (AVR C++) files under an MIT license. No price, quantity, or availability information is given anywhere in the repo, and no photos or renders of the assembled badge exist in the repo or were found elsewhere (a search of minibadge.wiki, which catalogs SAINTCON minibadges, only covers 2021 onward). Could not independently confirm the badge was physically built/distributed at SAINTCON 2017 beyond the repo's own framing as badge number 208 for that event; status left as "listed" rather than upgraded to "released" for that reason.
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2017/saintcon-2017-208-mini-badge.glb
  method: kicad
  source_file: pcb/saintcon-208.kicad_pcb
  generated: '2026-09-10'
  bytes: 63844
---

The 208 Mini Badge is a homebrew SAINTCON 2017 minibadge by maker phrackd, published as a complete open-source hardware project on GitHub. It centers on a single ATtiny13A microcontroller, an 8-pin AVR chip with only 5 usable GPIO pins, driving 18 LEDs through charlieplexing rather than one-LED-per-pin wiring. The LEDs come in two variants across the design, red (Everlight CMDA6BR7D1S-100) and blue (Inolux/Harvatek HT-193NB-5589), suggesting two color runs of the same board rather than mixed colors on one unit.

The repository includes full KiCad schematic and PCB layout files alongside the AVR firmware source, released under the MIT license, but no photos or renders of an assembled badge, and no information on price, quantity produced, or how it was distributed at the con. As with many minibadges from the SAINTCON community scene, it appears to have been a small, independently-made board rather than an official con badge.

## Make your own

The maker's GitHub repository (linked above) has everything needed to build one: a KiCad schematic and board layout under `pcb/`, and AVR C++ firmware under `firmware/src/` with a `build.sh` script. The README lists exact Mouser part numbers for the ATtiny13A, both LED color options, and the supporting capacitor.

