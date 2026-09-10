---
title: SponsorSidecar minibadge
id: saintcon-2024-sponsorsidecar-minibadge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: SAINTCON community (utahsaint-org)
  url: https://github.com/utahsaint-org
summary: A passive add-on PCB sized to attach alongside a sponsor's minibadge in the SAINTCON 2024 minibadge lineup.
functions: 'No electronics; a physical sidecar/extension board that mounts to a companion minibadge via mounting holes.'
look:
  colors: []
  shape: null
  themes:
  - village badge
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/SponsorSidecar
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/SponsorSidecar
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/SponsorSidecar
  kind: repo
images: []
contact: {}
notes:
- Sponsor sidecar add-on board for the SAINTCON 2024 minibadge system. Found by the event-year sweep, task saintcon-2024.
- 'Sweep title used the repo folder name verbatim ("SponsorSidecar minibadge"); no alternate maker-given title was found.'
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/SponsorSidecar
  title: SponsorSidecar minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://api.github.com/repos/utahsaint-org/MiniBadges2024
  title: 'utahsaint-org/MiniBadges2024: Minibadges for SAINTCON 2024'
  accessed: '2026-09-10'
  note: Confirms the repo is the official SAINTCON community org's 2024 minibadge collection; SponsorSidecar is one folder among ~30 minibadge projects in it.
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/SponsorSidecar/SponsorSidecar.kicad_pcb
  title: SponsorSidecar.kicad_pcb
  accessed: '2026-09-10'
  note: 'The PCB file contains only mounting-hole footprints (no MCU, LED, or connector footprints) — supports that this is a passive, unpowered board rather than an electronic minibadge.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-10'
  notes: >-
    Confirmed the item exists as a real design in the official SAINTCON 2024 minibadge
    GitHub org (utahsaint-org/MiniBadges2024), alongside dozens of other 2024 minibadges,
    so this is not just a search-snippet ghost. However there is no README, build guide
    entry, or press coverage found that names an individual maker, states a sponsor name,
    price, quantity made, or distribution method. The KiCad PCB file has no component
    footprints beyond mounting holes, suggesting a passive physical sidecar (no MCU,
    LEDs, or display) rather than a powered minibadge, but this is inferred from the
    design file itself, not stated anywhere. Could not find the item named in the 2024
    SAINTCON MiniBadge Guide PDF or on badge.gallery's SAINTCON 2024 minibadge page
    (checked, no hits) — the guide PDF itself was too large to search directly. No
    photos of an assembled/painted board were found; only vector artwork files (.ai/.svg)
    in the repo, which are design assets rather than photos of the item, so no images
    were saved. Maker credited as the SAINTCON community org rather than a named
    individual, since no specific designer is stated anywhere.
last_modified_date: '2026-09-10'
---

The SponsorSidecar is one of roughly thirty minibadge designs in `utahsaint-org/MiniBadges2024`, the official GitHub repository the SAINTCON community used to collect minibadge projects for SAINTCON 2024. Its own KiCad PCB file contains no component footprints beyond mounting holes, which points to a passive add-on board — something meant to physically attach alongside a sponsor's electronic minibadge rather than a standalone electronic badge of its own.

No README, build guide, or press writeup naming a specific sponsor, designer, price, or quantity was found. The repository provides full open design files (KiCad schematic and PCB, Gerbers, and Illustrator/SVG artwork), so the hardware itself is open, but nothing confirms whether it was actually distributed at the convention or only prepared as a design.
