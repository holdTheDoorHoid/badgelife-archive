---
title: Monorail badge with sphere and high roller SAO
id: dc34-monorail-badge-with-sphere-and-high-roller-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Zach Resmer
  url: https://resmer.co.za
summary: A self-made badge with a small monorail car that rolls along a track between magnetically-triggered stations, a ticket clip, and two add-on SAOs (a color-changing sphere and a "high roller" blinker) that plug into its extra SAO ports.
functions: Monorail ticket storage clip, mini monorail car that rolls along a track and lights up station markers via hall-effect switches, 1x extra SAO port for other people's SAOs, plus the badge's own sphere and high roller SAOs
look:
  colors: []
  shape: null
  themes:
  - transit
  - kit
tech:
  mcu: none
  leds:
    count: null
    type: null
    note: Station-marker LEDs are side-mounted and switched directly by hall-effect sensors (no microcontroller); the sphere SAO uses a single color-changing LED; the high roller SAO blinks LEDs in a circle driven by a 555 timer and decade counter.
  display: none
  connectivity: []
  battery: 2x AA or AAA (boosted to 3.3V with a TPS61023DRLR converter; MOSFET reverse-battery protection)
  sao_version: null
notes: []
get_one:
  price: ~$50
  price_usd: 50.0
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/zacharesmer/monorail-con-badge
  firmware_url: none - no microcontroller, no firmware
  eda_tool: KiCad
links:
- kind: website
  label: "Project writeup: Monorail Con badge"
  url: https://resmer.co.za/ch/posts/monorail-badge/
  archived: false
- kind: repo
  label: monorail-con-badge on GitHub
  url: https://github.com/zacharesmer/monorail-con-badge
  archived: false
- kind: social
  label: "Zach Resmer's Mastodon (@zachr@infosec.exchange)"
  url: https://infosec.exchange/@zachr
  archived: false
images:
- file: assets/images/badges/dc34/monorail-badge-with-sphere-and-high-roller-sao/3b4e1c70c0.jpg
  source: "https://resmer.co.za/ch/posts/monorail-badge/"
  credit: "Zach Resmer"
  caption: "Two monorail badges, one with the SAOs attached and lit up, next to a monorail ticket, on a background of colorful wool"
- file: assets/images/badges/dc34/monorail-badge-with-sphere-and-high-roller-sao/1c404841dd.png
  source: "https://resmer.co.za/ch/posts/monorail-badge/"
  credit: "Zach Resmer"
  caption: "Close-up of a station marker on the monorail track PCB, showing a side-mounted LED shining through a cutout"
contact:
  discord: __fladnag
  emails:
  - badgestuff@resmer.co.za
  - zachr@infosec.exchange
  raw:
  - 'Mastodon:'
status: released
sources:
- kind: sheet
  event: dc34
  row: 7
  updated: 5/25/2026 22:14:20
  listing: New
- kind: url
  url: https://resmer.co.za/ch/posts/monorail-badge/
  title: "Monorail Con badge"
  accessed: '2026-09-06'
  note: "Maker's own project writeup: full design story, mechanism, power design, 3D printing, and confirms there is no microcontroller/firmware; identifies the sphere and high roller SAOs plus a speaker SAO."
- kind: url
  url: https://github.com/zacharesmer/monorail-con-badge
  title: "zacharesmer/monorail-con-badge"
  accessed: '2026-09-06'
  note: "Repo with KiCad schematics/PCBs (5 boards), STL files for the monorail cars, lanyard design, and assembly notes; maker asks that it not be resold for an exorbitant price."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Maker''s own writeup and repo confirm the mechanism, "no firmware" design, and open-source KiCad files. Price kept from the community sheet (~$50). The maker mentions reworking "about 30" track boards during development, but that is a board-revision count, not a stated total of finished badges, so quantity is left blank. Availability, exact LED counts, and current sold/available status were not stated anywhere found; left unknown. The writeup also mentions a third SAO (a speaker/DFPlayer module) not named in this entry''s title - see other_items_found.'
last_modified_date: '2026-09-06'
---

Zach Resmer built this badge after riding the DEF CON monorail two years earlier, and it grew from a planned ticket-sized SAO into a full badge with its own SAOs. A small 3D-printed monorail car (two articulated cars, printed with an embedded magnet and a metal ring added mid-print) rolls along a PCB track; hall-effect switches at each station light side-mounted LEDs directly as the car passes, with no microcontroller involved anywhere in the design. The badge also holds a real monorail ticket in a clip, and carries a spare SAO port so other people's SAOs can ride along.

The badge comes with two of its own SAOs: a "high roller" SAO that blinks LEDs around a circle using a 555 timer and decade counter, and a sphere SAO built from a single color-changing LED. A third SAO with a DFPlayer Mini MP3 module and a button (for playing sound effects) is also part of the project but isn't named in this entry's title. Power comes from 2 AA/AAA cells boosted to 3.3V by a TPS61023DRLR converter, with MOSFET-based reverse-battery protection instead of a diode or a warning printed on the silkscreen.

The full design - five PCBs done in KiCad, STL files for the monorail cars, a sublimation lanyard design, and assembly notes - is published on GitHub. The maker's only condition on reuse is not reselling it "for an exorbitant amount of money."
