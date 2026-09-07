---
title: Expandable Display
id: saintcon-2025-expandable-display
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2025
year: 2025
makers:
- name: Cyberm3n
summary: 'A USB-C powered main board that supplies power and a shared clock signal to up to seven "daughter"/expander mini badge boards through picoblade jumper connectors, for wearing in a non-rigid chain or mounting into a custom enclosure.'
functions: 'Acts as a hub badge: a single USB-C source powers and clocks up to 7 connected expander boards, worn loose (non-rigid) or built into a custom interlocking-brick style enclosure (the maker suggests Lego-style bricks).'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - kit
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: USB-C
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed in person at SAINTCON 2025 ("Find me").'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=Expandable%20Display&year=2025
  url: https://minibadge.wiki/?search=Expandable%20Display&year=2025
  kind: website
- label: minibadge.wiki 2025 data export (JSON entry)
  url: https://minibadge.wiki/2025.json
  kind: doc
- label: cyberm3n-org/SC_2025 (GitHub, build files not yet published for this badge)
  url: https://github.com/cyberm3n-org/SC_2025
  kind: repo
images:
  - file: assets/images/badges/saintcon-2025/expandable-display/64f2bf3783.png
    source: "https://minibadge.wiki/2025.json"
    credit: "Cyberm3n"
    caption: "Front of the Expandable Display main board"
  - file: assets/images/badges/saintcon-2025/expandable-display/8c57d729b8.png
    source: "https://minibadge.wiki/2025.json"
    credit: "Cyberm3n"
    caption: "Back of the Expandable Display main board"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=Expandable%20Display&year=2025
  title: Expandable Display
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''saintcon-2025''.'
- kind: url
  url: https://minibadge.wiki/2025.json
  title: MiniBadge Wiki 2025 data export
  accessed: '2026-09-07'
  note: 'JSON record for "Expandable Display" by Cyberm3n: description, soldering instructions, category (Other), board house (JLCPCB), rarity (Rare), how to acquire ("Find me"), and front/back image filenames. The search page itself renders client-side and returned no results via fetch, so this data export was used instead.'
- kind: url
  url: https://github.com/cyberm3n-org/SC_2025
  title: cyberm3n-org/SC_2025 (GitHub)
  accessed: '2026-09-07'
  note: 'Repo exists and is referenced by the maker for build instructions, but the specific "tbd" folder path given in the minibadge.wiki entry for this badge does not exist yet (maker noted the real link would be on packaging instead).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Description and specs come from the maker''s own submission to minibadge.wiki (a community-run SAINTCON minibadge wiki), so treated as maker-sourced. No independent press coverage, storefront, price, or quantity-made figure found. The linked GitHub build-instructions folder for this specific badge is not yet published (repo exists; folder returns 404) — the maker''s own note says the real link would be printed on packaging instead. No MCU, LED, or display specs are stated for this piece; it is described purely as a power/clock distribution hub board, so those tech fields are left empty rather than guessed. Category on minibadge.wiki is "Other" (distinct from the more common badge/microbadge/sponsor categories); type was kept as the sheet''s existing "minibadge".'
last_modified_date: '2026-09-07'
---

The Expandable Display is a hub board by SAINTCON badge maker Cyberm3n, part of a large 2025 minibadge lineup that also included the Arctic Wolf sponsor series and several personal-themed pieces. Rather than being a badge itself, it is meant to power and coordinate other minibadges: a single USB-C connection feeds power and a shared clock to up to seven "daughter" expander boards, linked through small picoblade jumper connectors.

The maker describes two ways to wear or display it — loose and non-rigid, worn as a chain of connected boards, or built into a custom enclosure made from interlocking bricks (the write-up specifically suggests a Lego-compatible block). Detailed build instructions were promised via a GitHub link to be printed on the badge's packaging; as of research, the referenced repository folder had not yet been published, though the maker's `cyberm3n-org/SC_2025` GitHub org that hosts the rest of that year's badge files does exist.

No price, quantity made, or independent coverage beyond the minibadge.wiki community listing was found. It was categorized on that wiki as "Other" (outside the more common badge/microbadge/sponsor groupings) and given a rarity of "Rare," and the maker's stated way to acquire one was simply "Find me" at the 2025 conference.
