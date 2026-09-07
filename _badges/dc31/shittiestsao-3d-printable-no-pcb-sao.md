---
title: ShittiestSAO — 3D printable no-PCB SAO
id: dc31-shittiestsao-3d-printable-no-pcb-sao
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: jmarler
  url: https://github.com/jmarler
summary: A deliberately minimal, 3D-printed SAO with a single blinking LED and no PCB at all — a design for last-minute con attendees who need an SAO fast.
functions: 'A single LED blinks when powered by the host badge''s SAO header. No microcontroller, no resistor, no other logic.'
look:
  colors:
  - white
  - red
  shape: circle
  themes:
  - radio
  - minimalist
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: A generic blinking LED (self-flashing, no driver needed); no current-limiting resistor is used.
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
  where: 'Not sold; a free, open-source design meant to be 3D-printed and hand-assembled by the maker themself from a parts kit or scavenged parts.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/jmarler/ShittiestSAO
  firmware_url: null
  eda_tool: null
  license: Unlicense
  notes: 'Repo includes an STL and STEP file for the 3D-printed body, a full photographed assembly guide, and an Apple Pages template for the round paper sticker that forms the SAO''s face.'
links:
- label: github.com/jmarler/ShittiestSAO
  url: https://github.com/jmarler/ShittiestSAO
  kind: repo
images:
- file: assets/images/badges/dc31/shittiestsao-3d-printable-no-pcb-sao/a57aade618.jpg
  source: "https://github.com/jmarler/ShittiestSAO"
  credit: "jmarler"
  caption: "Completed ShittiestSAO with sticker applied, plugged into a badge"
- file: assets/images/badges/dc31/shittiestsao-3d-printable-no-pcb-sao/123d27280f.jpg
  source: "https://github.com/jmarler/ShittiestSAO"
  credit: "jmarler"
  caption: "Parts kit: 3D-printed SAO body, LED, headers, and sticker"
contact: {}
notes:
- unconventional 3D-printed SAO, no PCB
- 'Repo created 2023-07-31, days before DEF CON 31 (Aug 2023); maker made stickers for the Ham Radio Village at DEF CON. Event/year attributed to DC31 on that basis, not stated explicitly on the repo.'
- 'Sticker art on the assembled example is a pun on "ham radio": a G.I. Joe-style soldier with a handheld radio next to a radio tower and a cut of ham meat, with the LED protruding as the antenna signal.'
status: released
sources:
- kind: url
  url: https://github.com/jmarler/ShittiestSAO
  title: ShittiestSAO — 3D printable no-PCB SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/jmarler/ShittiestSAO
  title: 'jmarler/ShittiestSAO README'
  accessed: '2026-09-07'
  note: 'Full README, parts list, assembly steps, and "Intended Use" text describing it as a design for con attendees who realize too late they need an SAO; sticker made for the Ham Radio Village.'
- kind: url
  url: https://github.com/jmarler
  title: 'jmarler GitHub profile'
  accessed: '2026-09-07'
  note: 'Maker is Jon Marler, a Las Vegas-based ham radio operator and speaker at the DEF CON Ham Radio Village (DC30-32).'
- kind: url
  url: https://api.github.com/repos/jmarler/ShittiestSAO
  title: 'GitHub API: ShittiestSAO repo metadata'
  accessed: '2026-09-07'
  note: 'Repo created 2023-07-31, last pushed 2023-08-07 — timed just before DEF CON 31 (Aug 10-13, 2023).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The repo and README never name a specific event or year outright; the DC31/2023 attribution is inferred from the repo creation date (days before DEF CON 31) and the README''s mention of stickers made for the Ham Radio Village at DEF CON. No price, quantity-made, or availability info exists because this was never sold — it is a free plan for makers to fabricate their own. No maker photo of the physical assembled SAO beyond the README''s step photos was found.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/shittiestsao-3d-printable-no-pcb-sao/
---

The ShittiestSAO is a joke-named but genuinely functional add-on for badge lanyards, built by Jon Marler (a Las Vegas ham radio operator active in the DEF CON Ham Radio Village) to solve a very specific problem: showing up to a hacker con having forgotten to make an SAO. Instead of a PCB, it uses a 3D-printed plastic housing that holds a single self-flashing LED soldered directly across a cut-down 2x3 pin header, following the SAO 1.69bis pinout. There is no resistor, no microcontroller, and no other circuitry — the README leans into this with lines like "it's a shitty add-on... the LED may eventually die... it's shitty."

Assembly involves bending and soldering the LED's legs directly to the header pins, filling the resulting cavity with non-conductive epoxy (JB Weld's conductive epoxy will not work), and finishing the face with a 40mm round sticker — the repo includes an Apple Pages template originally used to print Ham Radio Village stickers for DEF CON, with the branding removed so others can substitute their own. The design (STL and STEP files) and full photographed assembly guide are released into the public domain under the Unlicense.

The GitHub repository was created on 2023-07-31 and last updated 2023-08-07, days before DEF CON 31 (held August 10-13, 2023) — consistent with the README's framing as a last-minute solution for that con season, though the project itself was never sold or distributed as a finished product; it exists purely as an open design for other makers to print and assemble themselves.
