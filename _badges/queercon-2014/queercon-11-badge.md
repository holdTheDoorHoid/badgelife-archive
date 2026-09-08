---
title: Queercon 11 Badge
id: queercon-2014-queercon-11-badge
layout: badge
parent: Queercon 11 (2014)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: queercon-2014
year: 2014
makers:
- name: Queercon
  url: https://queercon.org
summary: 'A floppy-disk-shaped MSP430 social badge for Queercon 11 (co-located with DEF CON 22) that uses IR peer exchange and an ISM-band radio to track proximity between attendees and award points at base stations.'
functions: 'Exchanges identifiers with nearby badges over IR; when two badges pair, both light up and display the other wearer''s name. A HopeRF RF69 radio counts nearby QC11 badges for a running proximity score. Base stations placed around the event read badges over IR/radio and award attendance points; the badge won 1st place in the DEF CON 22 badge contest.'
look:
  colors: []
  shape: floppy disk
  themes:
  - retro computer
tech:
  mcu: MSP430F5308
  leds:
    count: null
    type: WS2812
    note: WS2812 addressable LED grid used for the on-badge display
  display: LED matrix
  connectivity:
  - ir
  - sub-ghz
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed to Queercon 11 attendees at DEF CON 22 (2014).'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/duplico/qc11
  firmware_url: https://github.com/duplico/qc11
  eda_tool: null
links:
- label: hackaday.com/2014/09/15/the-queercon-11-badge
  url: https://hackaday.com/2014/09/15/the-queercon-11-badge/
  kind: article
- label: github.com/duplico/qc11
  url: https://github.com/duplico/qc11
  kind: repo
- label: github.com/Queercon/QC11-Badge
  url: https://github.com/Queercon/QC11-Badge
  kind: repo
images:
  - file: assets/images/badges/queercon-2014/queercon-11-badge/f8ddf57b05.jpg
    source: "https://hackaday.com/2014/09/15/the-queercon-11-badge/"
    credit: "Hackaday"
    caption: "The Queercon 11 floppy-disk-shaped badge"
  - file: assets/images/badges/queercon-2014/queercon-11-badge/9996d36cb1.jpg
    source: "https://hackaday.com/2014/09/15/the-queercon-11-badge/"
    credit: "Hackaday"
    caption: "The Queercon 11 base station reader used to award points"
contact: {}
notes:
- 'Sweep task dc22-all originally logged this as: "Floppy-disk-shaped MSP430 social badge for Queercon 11, co-located with DEF CON 22, using IR peer exchange and a HopeRF RF69 radio to track proximity and award points at base stations; won 1st place in the DC22 badge contest." Confirmed by Hackaday coverage and the maker''s own GitHub repos (duplico/qc11, Queercon/QC11-Badge).'
status: released
sources:
- kind: url
  url: https://hackaday.com/2014/09/15/the-queercon-11-badge/
  title: Queercon 11 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc22-all); event read as ''queercon-2014''.'
- kind: url
  url: https://github.com/duplico/qc11
  title: 'duplico/qc11: Queercon 11 electronic badge'
  accessed: '2026-09-08'
  note: 'Maker''s own repo; confirms MSP430F5308, WS2812 LED grid, IR pairing, ISM radio neighbor tracking, and CC BY-SA 4.0 / BSD 3-clause open-source licensing.'
- kind: url
  url: https://github.com/Queercon/QC11-Badge
  title: 'Queercon/QC11-Badge'
  accessed: '2026-09-08'
  note: 'Queercon org''s own copy of the hardware/firmware repo referenced by the Hackaday article as the source of the released design files.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Price, quantity made, and exact LED count were not stated in any source found and are left empty. Note: a separate entry, queercon-2015-queercon-11-badge, exists with the identical title "Queercon 11 Badge" but filed under the queercon-2015 event folder — Queercon 11 was the 2014 event (co-located with DEF CON 22), so that other entry appears to be a duplicate misfiled by year; not touched here per task scope.'
last_modified_date: '2026-09-08'
---

The Queercon 11 badge, worn by attendees of the 2014 Queercon party co-located with DEF CON 22, took the form of a 3.5" floppy disk and ran on an MSP430F5308 microcontroller. It used an infrared link to exchange identifiers with nearby badges — when two badges paired, each lit up its WS2812 LED grid and displayed the other wearer's name — while a HopeRF RF69 ISM-band radio kept a running count of other QC11 badges nearby. Base stations set up around the venue collected this pairing and proximity data to award attendees points, and the badge went on to win first place in the DEF CON 22 badge contest.

Queercon released the hardware design and firmware source for the badge on GitHub (as `Queercon/QC11-Badge` and, from designer George Louthan's own account, `duplico/qc11`), with the hardware under CC BY-SA 4.0 and the software largely under a BSD 3-clause license.

## Make your own

The full KiCad-era hardware files and MSP430 firmware source are published at [github.com/duplico/qc11](https://github.com/duplico/qc11) and [github.com/Queercon/QC11-Badge](https://github.com/Queercon/QC11-Badge); see each repo's README for the build and flashing steps.
