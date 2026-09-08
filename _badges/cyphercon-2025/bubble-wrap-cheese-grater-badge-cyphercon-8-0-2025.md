---
title: Bubble Wrap / Cheese Grater Badge (CypherCon 8.0, 2025)
id: cyphercon-2025-bubble-wrap-cheese-grater-badge-cyphercon-8-0-2025
layout: badge
parent: CypherCon 8.0
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cyphercon-2025
year: 2025
makers:
- name: TYMKRS
summary: 'The official CypherCon 8.0 (2025) badge, a 7x10 grid of custom LED-lit switches designed to look and sound like popping bubble wrap.'
functions: 'Pressing the switches lights and "pops" like bubble wrap; multiple puzzles are built into the badge, and solving them unlocks a free-draw mode on the LED grid.'
look:
  colors: []
  shape: rectangle
  themes:
  - puzzle
  - security
tech:
  mcu: RP2040
  leds:
    count: 70
    type: null
    note: 'Two LED driver ICs (I2C addresses 0x3C and 0x3F) each drive 35 channels, for 70 grid LEDs plus 2 ice-blue indicator LEDs.'
  display: null
  connectivity:
  - i2c
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
- label: hackthebadge.com/cyphercon-8-0-2025
  url: https://hackthebadge.com/cyphercon-8-0-2025/
  kind: website
images: []
contact: {}
notes:
- Official CypherCon 2025 conference badge, a 7x10 grid of LED-lit popping switches mimicking bubble wrap, with puzzles unlocking a free-draw mode. Found by the event-year sweep, task cyphercon.
status: listed
sources:
- kind: url
  url: https://hackthebadge.com/cyphercon-8-0-2025/
  title: Bubble Wrap / Cheese Grater Badge (CypherCon 8.0, 2025)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:cyphercon); event read as ''cyphercon-2025''.'
- kind: url
  url: https://github.com/sakebomb/ctfs/blob/main/cyphercon/2025/example_badge.py
  title: 'ctfs/cyphercon/2025/example_badge.py at main - sakebomb/ctfs'
  accessed: '2026-09-08'
  note: 'Third-party example MicroPython firmware for the badge; confirms RP2040 MCU, I2C LED driver ICs at 0x3C/0x3F (35 channels each), 7x10 button/LED matrix (70 switches, 70 LEDs), and 2 ice-blue indicator LEDs.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'The maker''s own hackthebadge.com page confirms the badge exists, its theme story, the 7x10 popping-switch grid, and the puzzle/free-draw-mode function, but gives no chip, price, quantity, availability, or design-file details. Those hardware specifics (RP2040, I2C LED driver ICs, LED/switch count) come from third-party example firmware (sakebomb/ctfs) rather than a TYMKRS-published source, hence medium rather than high confidence. A related unofficial firmware repo (EekRats/CypherCon8-Badge) exists but its README could not be fetched. No maker-published photos of the badge itself were found within the search budget, so no images were saved. Price, quantity, and availability remain unknown; no hardware/firmware files or Gerbers from TYMKRS were located.'
last_modified_date: '2026-09-08'
---

The Bubble Wrap / Cheese Grater Badge is TYMKRS's official electronic badge for CypherCon 8.0, held in Milwaukee in April 2025. The year's theme, "Fate or No Fate — What Can You Truly Control?", led the team to bubble wrap as inspiration, reasoning that a badge modeled on it would be funny because "who can control themselves around bubble wrap?" TYMKRS spent months sourcing switches from Chinese suppliers that had LEDs built in, so pressing a button both lights up and produces a popping sound reminiscent of popping bubble wrap.

The badge is built around an RP2040 microcontroller driving a 7x10 grid of these lit popping switches (70 buttons, 70 grid LEDs) plus two ice-blue indicator LEDs, with the LEDs handled by a pair of I2C LED-driver chips. Multiple puzzles are embedded in the badge's software; solving them unlocks a free-draw mode that lets the owner light up the grid freely. These hardware details come from third-party example firmware written for the badge rather than from a TYMKRS-published spec sheet, so they should be treated as reasonably well-supported but not maker-confirmed.

No official pricing, production quantity, or continued availability information was found, and TYMKRS has not published hardware files, firmware, or Gerbers for this badge that could be located during research.
