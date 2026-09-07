---
title: Hom3c0ming Badge
id: dc30-hom3c0ming-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: Alt_Bier
  url: https://homecoming.altbier.us/
summary: A two-part DIY kit badge for DEF CON 30's "Hacker Homecoming" theme, a wearable floral corsage plus a small pin-on boutonniere, built around a Raspberry Pi Pico and detailed silkscreen art.
functions: Addressable and discrete LEDs light up 3D-printed flower diffusers on both the corsage and boutonniere; the boutonniere has trimmer potentiometers to adjust its LED behavior.
look:
  colors:
  - black
  shape: flower
  themes:
  - floral
  - jewelry
tech:
  mcu: RP2040 (Raspberry Pi Pico)
  leds:
    count: 6
    type: WS2812D, discrete RGB/2-color THT
    note: Corsage has 4x WS2812D addressable LEDs plus 4x two-color 3mm discrete LEDs; boutonniere has 1x RGB common-cathode 5mm LED and 1x green 3mm LED.
  display: none
  connectivity: []
  battery: 3x AAA (corsage), CR2032 (boutonniere)
  sao_version: null
get_one:
  price: $80
  price_usd: 80.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  - free_drop
  where: In Person at the con; half were sold and half were given away in drops during DEF CON 30
make_your_own:
  open_source: yes
  hardware_url: https://github.com/gowenrw/hom3c0ming_badge
  firmware_url: https://github.com/gowenrw/hom3c0ming_badge/tree/main/code
  eda_tool: KiCad
  notes: MIT-licensed. Repo includes KiCad EDA files for both PCBs, CircuitPython firmware, 3D-printable flower LED diffusers, artwork, and step-by-step assembly guides with an assembly walkthrough video.
links:
- kind: repo
  label: GitHub - hom3c0ming_badge
  url: https://github.com/gowenrw/hom3c0ming_badge
- kind: website
  label: hom3c0ming badge project site
  url: https://homecoming.altbier.us/
- kind: video
  label: Hom3c0ming Badge Assembly walkthrough
  url: https://www.youtube.com/watch?v=d4AU95CxsSo
- kind: social
  label: '@alt_bier on Twitter/X'
  url: https://twitter.com/alt_bier
images:
- file: assets/images/badges/dc30/hom3c0ming-badge/d0513ec690.jpg
  source: "https://homecoming.altbier.us/"
  credit: "alt_bier"
  caption: "Corsage and boutonniere kit lit up"
- file: assets/images/badges/dc30/hom3c0ming-badge/6f9474651e.jpg
  source: "https://homecoming.altbier.us/corsage-assembly.html"
  credit: "alt_bier"
  caption: "Corsage badge lit, showing floral silkscreen and LED diffusers"
contact: {}
notes:
- Half will be sold and half will have drops during the con.
status: released
sources:
- kind: sheet
  event: dc30
  row: 20
  updated: '2022-07-28'
- kind: url
  url: https://github.com/gowenrw/hom3c0ming_badge
  title: "gowenrw/hom3c0ming_badge"
  accessed: '2026-09-07'
  note: Repo README, file structure, license (MIT), and GitHub code search confirming maker handle "alt_bier".
- kind: url
  url: https://homecoming.altbier.us/
  title: "hom3c0ming badge"
  accessed: '2026-09-07'
  note: Project site (GitHub Pages, redirected from repo docs) with maker's own description, theme story, and photo of the lit badge.
- kind: url
  url: https://raw.githubusercontent.com/gowenrw/hom3c0ming_badge/main/docs/corsage-assembly.md
  title: "Corsage Assembly Instructions"
  accessed: '2026-09-07'
  note: Bill of materials for the corsage — Raspberry Pi Pico, 3x AAA batteries, WS2812D and discrete LEDs, 3D-printed flower diffusers.
- kind: url
  url: https://raw.githubusercontent.com/gowenrw/hom3c0ming_badge/main/docs/boutonniere-assembly.md
  title: "Boutonniere Assembly Instructions"
  accessed: '2026-09-07'
  note: Bill of materials for the boutonniere — CR2032 cell, RGB LED, green LED, trimmer potentiometers.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's own GitHub repo and project site confirm the sheet's price ($80) and half-sold/half-dropped distribution note. Quantity made, current availability, and SAO header details were not stated anywhere found, so those fields are left as unknown/empty. The boutonniere attaches as a small pin-on add-on but the docs never call it an SAO or specify a standard SAO header, so tech.sao_version is left null.
last_modified_date: '2026-09-07'
---

The Hom3c0ming Badge is a two-piece, build-it-yourself kit made by Alt_Bier (gowenrw) for DEF CON 30's "Hacker Homecoming" 30th-anniversary theme. Riffing on high-school homecoming dances, the kit takes the form of a corsage — the main badge, worn on a lanyard — paired with a smaller boutonniere accessory. Both PCBs carry an unusually detailed silkscreen layer the maker says took hundreds of hours to design, and both use 3D-printed flower shapes as LED diffusers, prioritizing look over feature count.

The corsage runs on a Raspberry Pi Pico (RP2040) powered by 3x AAA batteries, driving four WS2812D addressable LEDs alongside four discrete two-color LEDs. The boutonniere is a simpler, CR2032-powered add-on with one RGB LED, one green LED, and three trimmer potentiometers for adjusting its look, attaching to clothing via a broach clip. Per the community sheet, roughly half the run was sold and the other half given away in drops during the con, at $80 for the kit.

Everything is open hardware and software under an MIT license: KiCad files for both boards, CircuitPython firmware, the 3D-printable diffuser models, and written assembly guides (plus a video walkthrough) all live in the maker's GitHub repository, so anyone who missed getting one at DEF CON 30 can build their own.
