---
title: Biohacking Village Badge (DC30)
id: dc30-biohacking-village-badge-dc30
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: Badge Pirates
  url: https://blog.badgepirates.com/
summary: 'The official DEF CON 30 Biohacking Village badge, a playable riff on the "Operation" board game: tweezers lift acrylic-cradled "body part" charms out of the board without tripping a health meter of LEDs.'
functions: 'A physical skill game modeled on Operation: players use the included tweezers to remove "body parts" charms held in acrylic cavities without touching the edges; a 3-LED health meter tracks strikes, and the badge is out after 3.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - puzzle
  - village badge
  - game
tech:
  mcu: none
  leds:
    count: 3
    type: reverse-mount
    note: Health-meter LEDs cycled by a 74HC4017D decade counter rather than an MCU.
  display: none
  connectivity: []
  battery: CR2450
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed at the DEF CON 30 Biohacking Village; Badge Pirates also linked a Tindie store listing from the project page, though it is not confirmed the DC30 badge itself was sold there versus given out at the village.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/BadgePiratesLLC/BiohackVillage_DC30
  firmware_url: null
  eda_tool: null
  notes: 'Repo (now archived) holds Artwork, CAD, and Mechanical folders but no schematic/PCB source was confirmed reachable; treated as partial (design files present, but full open-source status for the electronics is unconfirmed).'
links:
- label: github.com/BadgePiratesLLC/BiohackVillage_DC30
  url: https://github.com/BadgePiratesLLC/BiohackVillage_DC30
  kind: repo
- label: 'Badge Pirates blog: DefCon 30 Biohacking Village Badge'
  url: https://blog.badgepirates.com/DC30_BiohackBadge/
  kind: article
- label: 'DEF CON 30 - Biohacking Village Badge Mod (nullcasa)'
  url: https://nullcasa.github.io/dc30-biohacking-village-badge-mod/
  kind: article
images:
- file: assets/images/badges/dc30/biohacking-village-badge-dc30/8aec5c00ec.jpg
  source: "https://blog.badgepirates.com/DC30_BiohackBadge/"
  credit: "Badge Pirates"
  caption: "Front of the DC30 Biohacking Village badge, Operation-game themed with acrylic cavities holding removable body-part charms"
- file: assets/images/badges/dc30/biohacking-village-badge-dc30/cde092c353.jpg
  source: "https://nullcasa.github.io/dc30-biohacking-village-badge-mod/"
  credit: "nullcasa"
  caption: "Unmodified DC30 Biohacking Village badge board before the community mod"
contact: {}
notes:
- Official Biohacking Village badge for DEF CON 30, designed by Badge Pirates, with a separate community mod project (nullcasa/dc30-biohacking-village-badge-mod) built for it. Found by the event-year sweep, task dc30-badges.
- 'Sweep''s maker credit read "Badge Pirates (BadgePiratesLLC)"; the maker''s own blog and repo consistently use just "Badge Pirates," used here as the title/maker wording.'
- 'Sources disagree on assembly: the maker''s BOM lists a switch, power LED, and "various resistors and capacitors" alongside the pre-made charms and tweezers, suggesting at least some soldering; a community mod writeup describes the badge as usable pre-assembled with no soldering required. Left tech.mcu/battery as documented by the BOM; did not assert an assembly method either way.'
status: listed
sources:
- kind: url
  url: https://github.com/BadgePiratesLLC/BiohackVillage_DC30
  title: Biohacking Village Badge (DC30)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc30-badges); event read as ''dc30''.'
- kind: url
  url: https://blog.badgepirates.com/DC30_BiohackBadge/
  title: DefCon 30 Biohacking Village Badge - badgepirates
  accessed: '2026-09-08'
  note: Maker's own project writeup with theme, full BOM (74HC4017D counter, 74HC14 inverter, 3 reverse-mount LEDs, CR2450 battery/holder, switch, tweezers, body-part charms), and the front-badge photo.
- kind: url
  url: https://nullcasa.github.io/dc30-biohacking-village-badge-mod/
  title: 'DEF CON 30 - Biohacking Village Badge Mod'
  accessed: '2026-09-08'
  note: Third-party mod writeup confirming the Operation-game concept, health-meter LEDs, and decade-counter design; source of the unmodified-board photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own blog post and repo. Could not confirm price, quantity made, or precise distribution mechanics (free village giveaway vs. sold) beyond "distributed at the Biohacking Village"; get_one.price and quantity left empty. Could not verify whether the electronics/BOM design files (schematic, PCB, gerbers) are actually present in the archived GitHub repo beyond folder names (Artwork/CAD/Mechanical), so make_your_own.open_source is set to partial rather than yes. Assembly/soldering requirement is ambiguous between sources (see notes above).'
last_modified_date: '2026-09-08'
---

The DEF CON 30 Biohacking Village badge was designed by Badge Pirates as a physical riff on the classic Operation board game. Rather than an MCU, the board deliberately used simple logic ICs — a 74HC4017D decade counter driving three reverse-mount LEDs as a health meter, debounced through a 74HC14 hex Schmitt-trigger inverter — a choice the makers say was partly a throwback and partly a hedge against the chip supply-chain crunch of the time. A layer of acrylic sandwiched between the PCBs forms cavities that hold small "body part" charms; players use the included tweezers to lift the charms free without touching the edges, and three strikes ends the game.

The badge was distributed at DEF CON 30's Biohacking Village. Badge Pirates published Artwork, CAD, and Mechanical files in a GitHub repository (since archived), and also linked a YouTube demo and their Tindie storefront from the project page, though it isn't confirmed the DC30 badge itself was sold there rather than given out at the village. The design later inspired a community mod project (nullcasa's dc30-biohacking-village-badge-mod) that reworked the badge's internals, and Badge Pirates returned to the Biohacking Village with a follow-up badge at DEF CON 31.

## Make your own

Hardware source files (Artwork, CAD, and Mechanical folders) are published at github.com/BadgePiratesLLC/BiohackVillage_DC30, though the repository is now archived and read-only. No firmware is applicable, since the badge's logic runs on discrete counter/inverter ICs rather than a microcontroller.
