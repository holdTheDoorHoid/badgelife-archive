---
title: Night of the Evil AI Expansion Board
id: saintcon-2024-night-of-the-evil-ai-expansion-board
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: distinctm1nd
  url: https://github.com/distinctm1nd
summary: A SAINTCON 2024 minibadge expansion board with seven Halloween/graveyard-themed
  solder-it-yourself minibadges (tombstones, eyes, a tree) that plug in and light up.
functions: A learn-to-solder kit of seven interlocking minibadges (tombstones, left/right
  eyes, a tree) that plug into a shared SAO-header expansion board. Some minibadges
  blink or chase LEDs off a CD4017 decade counter; the "eye" and "letter" boards run
  AVR firmware with several selectable color/animation modes (named things like "Night
  of the Living Dead," "Night of the Red Moon," and "Night of the Evil Klippy AI").
look:
  colors: []
  shape: null
  themes:
  - halloween
  - horror
  - skull
  - learn to solder
tech:
  mcu: null
  leds:
    count: null
    type: discrete
    note: Mix of 1206 and 0603/0201 discrete LEDs (red, yellow, green, blue, UV,
      yellow-green) across the seven minibadges; some driven by a CD4017 decade
      counter, others by AVR-based firmware with selectable animation modes.
  display: none
  connectivity: []
  battery: USB power (also works with batteries)
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
  hardware_url: https://github.com/distinctm1nd/night_evil_ai
  firmware_url: https://github.com/distinctm1nd/night_evil_ai
  eda_tool: KiCad
links:
- label: github.com/distinctm1nd/night_evil_ai
  url: https://github.com/distinctm1nd/night_evil_ai
  kind: repo
- label: SAINTCON Minibadge Community
  url: https://www.saintcon.org/com-minibadge/
  kind: website
images:
- file: assets/images/badges/saintcon-2024/night-of-the-evil-ai-expansion-board/46fcdd8ec3.png
  source: "https://github.com/distinctm1nd/night_evil_ai"
  credit: "distinctm1nd"
  caption: "The seven soldered minibadges (tombstones, eyes, tree) plugged into the expansion board"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://github.com/distinctm1nd/night_evil_ai
  title: Night of the Evil AI Expansion Board
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''unclear (possibly dc32, 2024) — no archive entry found for it''.'
- kind: url
  url: https://github.com/distinctm1nd/night_evil_ai/blob/main/README.md
  title: Night of the Evil AI Minibadge Expansion Board Instructions
  accessed: '2026-09-07'
  note: Soldering/assembly instructions for the seven minibadges; USB/battery power, LED/resistor values, CD4017 counter and unused EEPROMs.
- kind: url
  url: https://github.com/distinctm1nd/night_evil_ai/blob/main/night_evil_ai_klip_on/night_evil_ai_klip_on.ino
  title: night_evil_ai_klip_on.ino
  accessed: '2026-09-07'
  note: AVR firmware for the eye/letter minibadge with named color/animation modes.
- kind: url
  url: https://web.archive.org/web/20260120213257/https://www.saintcon.org/com-minibadge/
  title: 'Communities: Minibadge — SAINTCON'
  accessed: '2026-09-07'
  note: Confirms distinctm1nd co-runs the SAINTCON Minibadge Community (with SHIFTY); used together with the repo's October 2024 creation date and the maker's other yearly Halloween-themed "expansion board" repos to correct the event from dc32 to saintcon-2024.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Event corrected from dc32 to saintcon-2024: the repo was created Oct 22, 2024 (after DEF CON 32, which was in August), the maker distinctm1nd co-runs the SAINTCON Minibadge Community, and the maker has a yearly pattern of similarly-named Halloween-themed "expansion board" repos (e.g. haunting_specter_expansion_board_2023, cryptid_expansion_board_2023) that fit the SAINTCON minibadge format. No page names this specific badge by title, so confidence is medium rather than high. Price, quantity made, and exact MCU part number are not stated anywhere found; left empty. No maker photo shows the bare PCB color/shape, so look.colors and look.shape are left empty.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc32/night-of-the-evil-ai-expansion-board/
---

"Night of the Evil AI" is a 2024 SAINTCON minibadge set by distinctm1nd, who co-runs SAINTCON's Minibadge Community (with SHIFTY) where attendees trade and design their own small badge-of-honor boards. It follows a format the maker has used in prior years for Halloween-season minibadge collections: a shared expansion board with an SAO-style header holds several smaller, individually-themed minibadges soldered on by the builder, here a graveyard scene of tombstones, a pair of eyes, and a tree.

Assembly is entirely through-hole-free surface-mount soldering: each minibadge takes its own 1206/0603/0201 resistors and LEDs (red, yellow, green, blue, and UV depending on the piece), and the board is powered over USB or battery. Lighting varies by piece — some tombstone and letter boards use a CD4017 decade counter for simple chase/blink patterns, while the eye and letter minibadges run AVR firmware with several selectable color modes carrying names like "Night of the Living Dead," "Night of the Red Moon," and "Night of the Evil Klippy AI." EEPROM footprints are present on several boards but explicitly unused.

The project is fully open source: the GitHub repo includes KiCad schematics for both a full-size and a "micro" version of the expansion board, the klip-on minibadge, Arduino/AVR firmware source, and a bill of materials PDF. No pricing, production quantity, or post-con availability information was found.

## Make your own

The hardware is published as KiCad schematics (`night_of_evil_ai_expansion_board_standalone.kicad_sch` and a micro-version variant with an accompanying BOM PDF), with AVR firmware (`.ino` files) for the klip-on and expansion-board eye/letter minibadges. The README documents exact resistor and LED values, footprint sizes, and orientation notes for each of the seven minibadges.
