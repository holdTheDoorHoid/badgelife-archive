---
title: Briefs minibadge (v2)
id: saintcon-2024-briefs-minibadge-v2
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
series: Briefs
makers:
- name: SHIFTY
  url: https://github.com/utahsaint-org
summary: A small square SAINTCON minibadge silkscreened with the word "BRIEFS" over a pair of underwear/shorts, lit by a single SMD LED.
functions: Lights a single LED when powered through the shared minibadge/SAO-style connector; otherwise a passive novelty badge with no other interactivity.
look:
  colors: []
  shape: rectangle
  themes:
  - meme
  - minimalist
  - text
tech:
  mcu: 'none'
  leds:
    count: 1
    type: SMD 1206
    note: Single 1206 LED in series with a 1206 resistor; no microcontroller.
  display: 'none'
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
  open_source: yes
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Briefs%20v2%20-%20SHIFTY
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/Briefs%20v2%20-%20SHIFTY
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Briefs%20v2%20-%20SHIFTY
  kind: repo
- label: MiniBadges2024 repo (SAINTCON 2024 minibadges)
  url: https://github.com/utahsaint-org/MiniBadges2024
  kind: repo
- label: SAINTCON MiniBadges community page
  url: https://saintcon.org/minibadges/
  kind: website
images:
- file: assets/images/badges/saintcon-2024/briefs-minibadge-v2/fe94505170.jpg
  source: "https://github.com/utahsaint-org/MiniBadges2024/tree/main/Briefs%20v2%20-%20SHIFTY"
  credit: "SHIFTY"
  caption: "Front silkscreen render of the Briefs minibadge (v2): the word BRIEFS stacked vertically beside a pair of shorts/underwear outline"
contact: {}
notes:
- '''Briefs'' minibadge design v2 in the SAINTCON 2024 repo, credited to SHIFTY. Found by the event-year sweep, task saintcon-2024.'
- 'The "v2" in the title is the maker''s own folder naming (the repo has no "Briefs v1" alongside it, so an earlier version was not located).'
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Briefs%20v2%20-%20SHIFTY
  title: Briefs minibadge (v2)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Briefs%20v2%20-%20SHIFTY
  title: "Briefs v2 - SHIFTY (repo folder contents)"
  accessed: '2026-09-10'
  note: "KiCad project files (schematic, PCB, footprint) plus PNG/JPG renders; confirms one SMD LED, one resistor, and the standard MiniBadge_Simple square footprint, no MCU."
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024
  title: "utahsaint-org/MiniBadges2024"
  accessed: '2026-09-10'
  note: "Repo README confirms this is the community minibadge collection for SAINTCON 2024."
- kind: url
  url: https://saintcon.org/minibadges/
  title: "MiniBadges - SAINTCON 26"
  accessed: '2026-09-10'
  note: "Confirms SHIFTY co-leads the SAINTCON MiniBadge community/program that this design was submitted to."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed via the maker''s own KiCad repo folder: a real, submitted SAINTCON 2024 minibadge, single-LED, no MCU, standard 20mm square MiniBadge_Simple form factor. Could not find price, quantity made, or availability/distribution details (no storefront, no trading-page listing found for this specific design) or the actual board/soldermask color (the copper and mask PNG renders in the repo came back as blank/black images and could not be used). Could not confirm whether an earlier "v1" of this design exists elsewhere. SHIFTY is confirmed as a real SAINTCON minibadge-community organizer, supporting the maker attribution. The archive also has two related, but distinct, "Briefs" entries from SAINTCON 2023 by the same maker (saintcon-2023-briefs-community-badge and saintcon-2023-briefs-speaker-minibadge); this 2024 minibadge looks like the same running "Briefs" gag/series continued into 2024, not a duplicate of either.'
last_modified_date: '2026-09-10'
---

"Briefs" is a small square minibadge made for the SAINTCON 2024 MiniBadge community, credited to SHIFTY, one of the two people who run SAINTCON's long-running MiniBadge program. Like most minibadges, it is a simple, passive board sized to plug into the shared minibadge connector on a host badge or display board: no microcontroller, just a single SMD LED and a series resistor that lights up when the badge is powered. The front silkscreen spells out "BRIEFS" next to a printed outline of a pair of shorts/underwear, playing on the maker's own community-organizer nickname/branding rather than referencing any external show or product.

The design's hardware (KiCad schematic, PCB, and footprint files, along with the render images used for silkscreen and soldermask art) is published in the community's public `MiniBadges2024` GitHub repository, which collects the year's submitted minibadges as one archive rather than each having its own storefront. No pricing, print-run size, or standalone distribution page for this specific badge was found; SAINTCON minibadges are typically traded in person at the con's MiniBadge community space rather than sold individually, but that could not be confirmed for this particular design.
