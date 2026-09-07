---
title: RED TEAM
id: saintcon-2021-red-team
layout: badge
parent: Saintcon 2021
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2021
year: 2021
makers:
- name: Jup1t3r
summary: 'A solder-your-own SAINTCON minibadge with three LEDs and a jumper-selectable solid or blinking mode.'
functions: 'Three LEDs (D1, D2, D3) light up in either solid-on or blinking mode, selected by which pair of jumper pads is bridged.'
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds:
    count: 3
    type: null
    note: 'D1, D2, D3; oriented with the green dot toward bottom-left per soldering instructions.'
  display: null
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
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=RED%20TEAM&year=2021
  url: https://minibadge.wiki/?search=RED%20TEAM&year=2021
  kind: website
images:
  - file: assets/images/badges/saintcon-2021/red-team/31dc6802e0.jpg
    source: "https://minibadge.wiki/?search=RED%20TEAM&year=2021"
    credit: "Jup1t3r"
    caption: "RED TEAM minibadge, front"
  - file: assets/images/badges/saintcon-2021/red-team/1fdd125ce0.jpg
    source: "https://minibadge.wiki/?search=RED%20TEAM&year=2021"
    credit: "Jup1t3r"
    caption: "RED TEAM minibadge, back"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=RED%20TEAM&year=2021
  title: RED TEAM
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2021''.'
- kind: url
  url: https://minibadge.wiki/2021.json
  title: 'MiniBadge Wiki 2021 data feed (RED TEAM entry)'
  accessed: '2026-09-07'
  note: 'Underlying JSON record for the RED TEAM card: soldering instructions, difficulty (Beginner), LED count/layout, jumper behavior, and front/back image URLs. Description, category, quantity, and acquisition fields were blank in the source.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'The minibadge.wiki listing page itself is rendered client-side from a JSON data feed (minibadge.wiki/2021.json), which was fetched directly to get the RED TEAM record. That record gives soldering/assembly detail (three LEDs D1-D3, one resistor, a jumper selecting solid-on vs. blinking) and soldering difficulty "Beginner", but leaves description, category, quantity made, board house, how-to-acquire, and rarity all blank, so price, availability, and open-source status could not be determined. No maker page, repo, or storefront for "Jup1t3r" was found via the sources checked. Web search was unavailable for this task (session search budget exhausted), so only the existing link and its underlying data feed could be consulted.'
last_modified_date: '2026-09-07'
---

RED TEAM is a solder-it-yourself minibadge made by Jup1t3r for SAINTCON 2021, part of the convention's long-running community minibadge tradition where attendees trade and swap small badges throughout the event. It carries three LEDs (labeled D1, D2, and D3) and a single resistor, with the build oriented by a green dot on the LEDs pointing toward the bottom-left of the board.

A jumper lets the builder choose the badge's behavior at assembly time: bridging the middle and top pads sets the LEDs to solid on, while bridging the middle and bottom pads makes them blink. The listing warns not to bridge all three jumper pads at once, since doing so can short and affect the rest of the badge. The soldering difficulty is listed as Beginner.

Beyond the assembly instructions and two photos captured from the minibadge.wiki community database, no other detail was recoverable: the source record leaves the badge's description, category, quantity made, board house, price, and how it was distributed all blank, and no separate maker page, repository, or storefront for Jup1t3r turned up in the sources available for this pass.
