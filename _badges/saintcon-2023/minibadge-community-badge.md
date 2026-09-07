---
title: Minibadge Community Badge
id: saintcon-2023-minibadge-community-badge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: SHIFTY
summary: 'A 7-LED SAINTCON 2023 minibadge, built to occupy roughly nine slots on a standard minibadge board and given out one-of-a-kind rather than sold.'
functions: 'Lights up 7 LEDs (D5 and D6 are green and share a resistor; the rest are mixed SMD/THT). No games or interactivity beyond lighting up.'
look:
  colors: []
  shape: null
  themes:
  - minibadge
  - village badge
tech:
  mcu: none
  leds: 7
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  - swap
  where: 'Given out at SAINTCON 2023 by SHIFTY at the Badgelife community/minibadge display, awarded to the attendee seen wearing the most lit-up minibadges, with a small number of others available through unique trades or barter.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=Minibadge%20Community%20Badge&year=2023
  url: https://minibadge.wiki/?search=Minibadge%20Community%20Badge&year=2023
  kind: website
images:
  - file: assets/images/badges/saintcon-2023/minibadge-community-badge/4145279969.png
    source: "https://minibadge.wiki/"
    credit: "SHIFTY"
    caption: "Front of the Minibadge Community Badge, a 7-LED SAINTCON minibadge"
  - file: assets/images/badges/saintcon-2023/minibadge-community-badge/b61e5979f5.png
    source: "https://minibadge.wiki/"
    credit: "SHIFTY"
    caption: "Back of the Minibadge Community Badge, showing the custom slot extender area"
contact: {}
notes:
- 'category: Personal; rarity: Super Rare'
- 'Soldering difficulty listed as Intermediate on minibadge.wiki.'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=Minibadge%20Community%20Badge&year=2023
  title: Minibadge Community Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2023''.'
- kind: url
  url: https://minibadge.wiki/2023.json
  title: Minibadge Wiki 2023 data (JSON entry for "Minibadge Community Badge" by SHIFTY)
  accessed: '2026-09-07'
  note: 'Primary data source: description, soldering instructions, difficulty, category, rarity, quantity, and how-to-acquire text, plus front/back image URLs.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No maker page, repo, or press coverage found beyond the minibadge.wiki community listing itself, which is the maker-submitted source of record for SAINTCON minibadges. quantityMade is recorded as 0 on the wiki (field appears unused/default rather than a real zero) so get_one.quantity is left blank rather than guessed. No design files, chip, or price beyond "free drop" were stated.'
last_modified_date: '2026-09-07'
---

The Minibadge Community Badge is a SAINTCON 2023 minibadge made by SHIFTY, built around 7 LEDs (a pair of green LEDs on D5/D6 sharing one resistor, plus other SMD and through-hole LEDs elsewhere on the board). It was designed to take up about nine slots on a standard 10x10 minibadge board, and because of its oversized footprint it shipped with a custom slot extender rather than fitting a normal minibadge holder.

Rather than being sold, it was given away as a one-off prize: SHIFTY awarded it at the con to whichever attendee was seen wearing the most lit-up minibadges, with the handful of remaining copies changing hands only through direct trades or barter within the badgelife community. The wiki lists it as "Super Rare" and rates the build as Intermediate soldering difficulty, calling out the shared-resistor green LED pair and recommending the through-hole LEDs be bent slightly outward so their light shows through the wording on the board.

## Make your own

No hardware files, firmware, or Gerbers have been published for this badge; the only build guidance available is the soldering-order notes captured above.
