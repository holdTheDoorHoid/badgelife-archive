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
summary: A microcontroller-free badge with a 3D-printed monorail car that rolls along a PCB track and lights station LEDs through hall-effect switches, a clip for a real monorail ticket, and its own SAOs (a color-changing sphere and a "high roller" LED chaser, plus a speaker SAO).
functions: Clip that holds a monorail ticket; 3D-printed two-car monorail with an embedded magnet that rolls along a PCB track and lights station-marker LEDs directly through hall-effect switches; three SAO headers carrying the badge's own sphere SAO (color-changing LED), high roller SAO (555 timer + decade counter LED chaser) and speaker SAO (DFPlayer Mini MP3 module with a button to cycle tracks)
look:
  colors:
  - black
  - white
  - blue
  shape: null
  themes:
  - transit
tech:
  mcu: none
  leds:
    count: null
    type: null
    note: Station-marker LEDs (white, side-mounted, shining through cutouts) are switched directly by TMAG5231 hall-effect switches with no microcontroller; the sphere SAO is a single color-changing LED; the high roller SAO blinks LEDs in a circle driven by a 555 timer and decade counter.
  display: none
  connectivity: []
  battery: 2 AA/AAA cells, boosted to 3.3V by a TPS61023DRLR converter, with AO3415A MOSFET reverse-battery protection
  sao_version: null
  sao_ports: 3
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
  firmware_url: null
  eda_tool: KiCad
  notes: No firmware exists by design (no microcontroller). Repo holds KiCad projects and PDF schematics for five boards (main board, top track, high roller SAO, sphere SAO, speaker SAO), STL/3MF files for the monorail cars and sphere stands, the lanyard PDF, and a parts diagram. No license file; the maker asks that modified versions carry the modifier's name and that nothing be sold for more than a reasonable cost of materials.
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
  caption: "Two monorail badges (black PCB, blue track), one with the high roller, sphere and speaker SAOs attached and lit, with a Las Vegas Monorail ticket in the clip and the train lanyard, on a background of colorful wool balls"
contact:
  discord: __fladnag
  emails:
  - badgestuff@resmer.co.za
  mastodon: zachr@infosec.exchange
  raw:
  - 'Mastodon: zachr@infosec.exchange'
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
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-checked 2026-09-07 against the maker''s writeup, the GitHub repo (readme.txt, credits.txt, file listing) and the Mastodon profile. Removed an unsupported claim of a spare SAO port for other people''s SAOs: the maker''s photo shows three SAO headers (SAO1 high roller, SAO2 sphere, SAO3) and the project ships three SAOs. Removed a second image that was a KiCad 3D render, not a photo of the badge. Price (~$50) is from the community sheet only; the repo credits mention a Shopify shop but no storefront URL was found. Quantity is not stated (the "about 30" reworked boards is a rework count, not a run size). Availability, exact LED counts and SAO header version are not stated. The sheet''s "zachr@infosec.exchange" is a Mastodon handle, not an email; moved to contact.mastodon. Event is DEF CON 34 per the sheet; the writeup (June 2026) says only "DEF CON".'
last_modified_date: '2026-09-06'
---

Zach Resmer built this badge after riding the DEF CON monorail two years earlier, and it grew from a planned ticket-sized SAO into a full badge with its own SAOs. A small 3D-printed monorail car (two articulated cars, printed with an embedded magnet and a metal ring added mid-print) rolls along a PCB track; hall-effect switches at each station light side-mounted LEDs directly as the car passes, with no microcontroller involved anywhere in the design. The badge also holds a real monorail ticket in a bulldog clip, and its three SAO headers carry the project's own SAOs.

The badge comes with two of its own SAOs: a "high roller" SAO that blinks LEDs around a circle using a 555 timer and decade counter, and a sphere SAO built from a single color-changing LED. A third, speaker SAO uses a DFPlayer Mini MP3 module and a single button that cycles through MP3s on an SD card (the shipped clips include monorail voiceover audio); it is part of the project but isn't named in this entry's title. Power comes from two AA/AAA cells boosted to 3.3V by a TPS61023DRLR converter so the badge keeps running down to about 0.75 V per cell, with an AO3415A MOSFET for reverse-battery protection instead of a diode or a warning printed on the silkscreen.

The full design - five PCBs done in KiCad, STL files for the monorail cars, a sublimation lanyard design, and assembly notes - is published on GitHub. The maker's only condition on reuse is not reselling it "for an exorbitant amount of money."
