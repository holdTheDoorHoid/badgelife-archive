---
title: Bowtie and Screwdriver Badge
id: dc27-bowtie-and-screwdriver-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: compukidmike
summary: A two-piece DEF CON 27 badge system from compukidmike (MKFactor) - a BowTie badge with 20 charlieplexed LEDs and an IR receiver, paired with a handheld Screwdriver accessory that beeps, lights up, and can trigger the BowTie's lights over infrared.
functions: The BowTie badge cycles through four LED animation modes (a ring chase, a four-wide chase, a symmetric wave, and a fourth mode) via a single push button, and has an IR receiver so it can react to a signal sent by the Screwdriver. The Screwdriver is its own ATtiny84A device with a touch button and three capacitive sliders, three status LEDs, a buzzer that plays a "screwdriver" sound effect, an IR LED for triggering the BowTie, a "Bling" LED dance mode, and a TV-B-Gone mode (built on Adafruit's TV-B-Gone code) that can power off televisions with IR remote codes.
look:
  colors: []
  shape: bow tie (BowTie board); screwdriver (Screwdriver board)
  themes: []
tech:
  mcu: ATtiny84A
  leds:
    count: 20
    type: charlieplexed
    note: The BowTie board charlieplexes 20 red-labeled LEDs across 5 I/O pins in a ring. The separate Screwdriver board has its own 3 status LEDs plus a dedicated IR LED for triggering the BowTie and for its TV-B-Gone function.
  display: none
  connectivity:
  - ir
  inputs:
  - buttons
  - touch
  - capacitive
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
  open_source: true
  hardware_url: https://github.com/compukidmike/dc27/tree/master/Bowtie%20and%20Screwdriver%20Badge
  firmware_url: https://github.com/compukidmike/dc27/tree/master/Bowtie%20and%20Screwdriver%20Badge
  eda_tool: KiCad
links:
- label: github.com/compukidmike/dc27/tree/master/Bowtie%20and%20Screwdriver%20Badge
  url: https://github.com/compukidmike/dc27/tree/master/Bowtie%20and%20Screwdriver%20Badge
  kind: repo
- label: compukidmike/dc27 (repo root README)
  url: https://github.com/compukidmike/dc27
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: listed
sources:
- kind: url
  url: https://github.com/compukidmike/dc27/tree/master/Bowtie%20and%20Screwdriver%20Badge
  title: Bowtie and Screwdriver Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc27''.'
- kind: url
  url: https://github.com/compukidmike/dc27
  title: compukidmike/dc27 - DEFCON 27 Projects
  accessed: '2026-09-07'
  note: Repo root README confirms two badges made for Defcon 27 by "we" (compukidmike's team); links a separate Fifth Element Badge project (already a separate archive entry).
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/dc27/master/Bowtie%20and%20Screwdriver%20Badge/BowTie/Firmware/BowTie/main.cpp
  title: BowTie/Firmware/BowTie/main.cpp
  accessed: '2026-09-07'
  note: 'Firmware source: confirms 20 charlieplexed LEDs, IR receiver pin, single push button cycling 4 display modes (Ring, Chase, Wave, + one more), ATtiny84A target (from BowTie.cppproj), F_CPU 1MHz internal clock.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/dc27/master/Bowtie%20and%20Screwdriver%20Badge/Screwdriver/Firmware/Screwdriver%20Badge/main.c
  title: Screwdriver/Firmware/Screwdriver Badge/main.c
  accessed: '2026-09-07'
  note: 'Firmware source: confirms 3 status LEDs, an IR LED, a buzzer, a touch button, 3 capacitive sliders, a "Bling" mode, and a TV-B-Gone mode built on Adafruit''s TV-B-Gone code; file dated 3/6/2018 (predates DC27), suggesting the Screwdriver firmware was carried over/adapted from an earlier project. ATtiny84A confirmed via Screwdriver Badge.cproj.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/dc27/master/Bowtie%20and%20Screwdriver%20Badge/README.md
  title: Bowtie and Screwdriver Badge/README.md
  accessed: '2026-09-07'
  note: One-line README confirming both KiCad hardware and firmware source are included for "the BowTie and Screwdriver badge for Defcon 27."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Confirmed via the maker's own GitHub repo (KiCad hardware + AVR firmware for both boards, both ATtiny84A). Could not find a storefront listing, price, quantity made, distribution method, or any photo of the finished badges - searched Tindie (compukidmike/MKFactor store; direct product-page and store-page fetches were blocked or returned no results), Hackaday's DEF CON 27 badge round-ups (checked the Sept 2019 pictorial guide and Aug 2019 breakfast-hardware post directly; neither mentions this badge by name), and MKFactor's own blog (no matching post found). A web search summary claimed specific details (Michael/Katie Whiteley as makers, a photo, a description matching Hackaday's pictorial guide) but those details could not be verified in the actual page text, so they were not used. left get_one and look.colors empty rather than guess.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc27/bowtie-and-screwdriver-badge.glb
  method: kicad
  source_file: Bowtie and Screwdriver Badge/BowTie/Hardware/BowTie/BowTie.kicad_pcb
  generated: '2026-09-07'
  bytes: 238040
---

The BowTie and Screwdriver Badge is a two-piece hardware badge compukidmike made for DEF CON 27 (2019), with both parts built around an ATtiny84A microcontroller and designed in KiCad. The BowTie board wears like a bow tie and charlieplexes 20 LEDs into a ring, cycling through animation patterns - a chasing ring, a four-wide chase, and a symmetric wave among them - with a single push button, and it also carries an IR receiver so it can react to a signal from its companion piece.

The Screwdriver is a separate handheld device that pairs with the BowTie: it has its own touch button and three capacitive sliders, three status LEDs, a buzzer that plays a "screwdriver" sound effect, and an IR LED it can use both to trigger the BowTie's lights and, in a built-in TV-B-Gone mode (adapted from Adafruit's TV-B-Gone project), to send universal power-off codes at televisions. Its firmware file is dated March 2018, well before DEF CON 27, suggesting the code was reused or adapted from an earlier compukidmike project rather than written fresh for this badge.

Full KiCad hardware files and AVR firmware source for both boards are published in compukidmike's `dc27` GitHub repository, but no storefront listing, price, production quantity, or photo of the finished badges could be found.
