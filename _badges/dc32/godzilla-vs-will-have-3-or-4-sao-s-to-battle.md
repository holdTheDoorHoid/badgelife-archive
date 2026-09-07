---
title: G0dzilla VS Badge
id: dc32-godzilla-vs-will-have-3-or-4-sao-s-to-battle
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Alt_Bier
  url: https://gowen.net/about
summary: An ESP32-based indie badge with Godzilla battling four interchangeable kaiju SAOs, plus a wireless and silkscreen crypto challenge.
functions: Touching a "Godzilla Minus One" logo area boops Godzilla and launches a crypto challenge game over a local Wi-Fi access point and web server; a separate crypto challenge is built into the silkscreen on the back. The badge detects which of the four SAO monsters are plugged in via a GPIO voltage read per SAO.
look:
  colors: []
  shape: rectangle
  themes:
  - monster
  - sci-fi
  - movie
  - ctf
tech:
  mcu: ESP32 (Wemos Lolin32)
  leds:
    count: 16
    type: mixed
    note: 8 addressable NeoPixels and 8 traditional white LEDs on the main badge, plus 2 traditional white LEDs on each of the four SAOs; 2 additional indicator LEDs on the ESP32 dev board.
  display: none
  connectivity:
  - wifi
  battery: LiPo (rechargeable, onboard charge circuit, 3-4 hour full charge)
  sao_version: v1
  sao_ports: 4
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed at DEF CON 32 (August 2024); the sheet's original listing anticipated "3 or 4 SAOs to battle," matching the four monster SAOs (Mothra, King Ghidorah, Rodan, Hedorah) that shipped with the badge.
make_your_own:
  open_source: true
  hardware_url: https://github.com/gowenrw/g0dzilla_vs
  firmware_url: https://github.com/gowenrw/g0dzilla_vs
  eda_tool: KiCad
  license: MIT
  notes: Repo (KiCad 7.x project) includes the main badge PCB and the four-way-breakout SAO PCB, firmware, artwork, and assembly/operations guide pages; maker credited on GitHub as gowenrw.
links:
- label: g0dzilla.altbier.us
  url: https://g0dzilla.altbier.us/
  kind: doc
- label: gowenrw/g0dzilla_vs (GitHub)
  url: https://github.com/gowenrw/g0dzilla_vs
  kind: repo
- label: twitter.com/alt_bier
  url: https://twitter.com/alt_bier
  kind: social
- label: altbier.us
  url: https://altbier.us/
  kind: website
  archived: https://web.archive.org/web/20260608053942/https://altbier.us/
images:
- file: assets/images/badges/dc32/godzilla-vs-will-have-3-or-4-sao-s-to-battle/23066589c1.jpg
  source: https://g0dzilla.altbier.us/
  credit: Alt_Bier
  caption: Assembled G0dzilla VS badge with SAO monster addons attached
- file: assets/images/badges/dc32/godzilla-vs-will-have-3-or-4-sao-s-to-battle/afde1b6db0.jpg
  source: https://g0dzilla.altbier.us/
  credit: Alt_Bier
  caption: Mothra SAO, one of the four interchangeable monster add-ons
contact: {}
notes:
- Sheet title was literal at import time ("will have 3 or 4 SAO's to battle"); the finished badge shipped with four monster SAOs, so the title has been updated to the maker's own name for the project, "G0dzilla VS Badge."
status: released
sources:
- kind: sheet
  event: dc32
  row: 11
  updated: ''
- kind: url
  url: https://g0dzilla.altbier.us/
  title: G0dzilla VS Badge - DEFCON 32
  accessed: '2026-09-06'
  note: Maker's own project page; source for MCU, LED counts, SAO mechanism (GPIO voltage detection), Wi-Fi/silkscreen crypto challenges, battery, and photos.
- kind: url
  url: https://github.com/gowenrw/g0dzilla_vs
  title: gowenrw/g0dzilla_vs
  accessed: '2026-09-06'
  note: Confirms open-source hardware (KiCad) and firmware under MIT license, DC32 badge.
- kind: url
  url: https://altbier.us/
  title: altbier.us
  accessed: '2026-09-06'
  note: Maker's landing page listing all of Alt_Bier's badges, linking to g0dzilla.altbier.us for this one.
  archived: https://web.archive.org/web/20260608053942/https://altbier.us/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts confirmed on the maker's own project site and GitHub repo. Price, quantity produced, and precise availability (sold, given away, or con-exclusive) are not stated anywhere found, so those fields are left empty/unknown rather than guessed. The maker's Twitter/X account could not be fetched directly to check for further distribution details.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc32/godzilla-vs-will-have-3-or-4-sao-s-to-battle.glb
  method: kicad
  source_file: eda/g0dzilla_vs/g0dzilla_vs_middle.kicad_pcb
  generated: '2026-09-07'
  bytes: 904632
---

The G0dzilla VS Badge is Alt_Bier's DEF CON 32 entry: an ESP32-based badge built around Godzilla fighting a rotating cast of kaiju opponents, each one a separate Shitty Add-On (SAO). The main board runs on a Wemos Lolin32 ESP32 dev board and mixes eight addressable NeoPixels with eight traditional white LEDs, all powered by a rechargeable LiPo battery with an onboard charge circuit. Four SAO connectors sit on the badge — two powered ports on the front where Godzilla's opponent plugs in, and two unpowered "green room" ports on the back that act as holders for whichever monsters aren't currently in the fight. Each SAO reports its identity back to the main board over a GPIO pin at a specific voltage, letting the badge tell which of the four monsters — Mothra, King Ghidorah, Rodan, or Hedorah — is currently connected.

Beyond the monster-battling gimmick, the badge doubles as two separate CTF-style puzzles: touching its "Godzilla Minus One" logo area launches a crypto challenge over a self-hosted, password-free Wi-Fi access point and web server, while a second, independent challenge is worked into the silkscreen artwork on the back of the board. The maker's project write-up also covers the PCB design challenges of aligning four (seven counting the SAO breakout) separate boards during assembly. The community sheet's original listing for this entry — "will have 3 or 4 SAO's to battle" — reflected the badge's SAO count before release; it shipped with all four monster SAOs, so the entry's title has been updated to the maker's own name for the finished project.

## Make your own

The full KiCad 7.x hardware project, firmware, and artwork are published under the MIT license in the [gowenrw/g0dzilla_vs](https://github.com/gowenrw/g0dzilla_vs) GitHub repo, alongside the maker's own assembly instructions and operations guide at [g0dzilla.altbier.us](https://g0dzilla.altbier.us/assembly.html).
