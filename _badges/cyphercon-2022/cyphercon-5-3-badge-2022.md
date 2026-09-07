---
title: CypherCon 5.3 Badge (2022)
id: cyphercon-2022-cyphercon-5-3-badge-2022
layout: badge
parent: Cyphercon 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cyphercon-2022
year: 2022
makers:
- name: TYMKRS
  url: https://www.tymkrs.com/
  role: badge design (PCB art, mechanical, vending-machine concept)
- name: Peter Shabino
  url: https://github.com/Wireb
  role: firmware, electronics, vending machine server
summary: The official CypherCon 5.3 (2022) badge, a "Flamingo & Friends" set of five animal-shaped PIC-based badges (Coyote, Flamingo, Llama, Parrot, Peacock) with an animated LCD, IR badge-to-badge communication, and a tie-in vending machine game.
functions: Animated LCD eye/face graphics stored on SPI EEPROM, IR communication between badges and with IR-equipped fixtures, a cryptographic "lifetime badge" anti-forgery/key-generation scheme, and an interactive vending-machine game that badges could unlock.
look:
  colors: []
  shape: animal
  themes:
  - animal
  - security
  - crypto
tech:
  mcu: PIC
  leds: null
  display: LCD
  connectivity:
  - ir
  inputs:
  - buttons
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
  open_source: true
  hardware_url: https://github.com/Wireb/Cyphercon-5_3-2022
  firmware_url: https://github.com/Wireb/Cyphercon-5_3-2022
  eda_tool: KiCad
  license: MIT
  notes: Repo also includes FreeCAD mechanical files (stencils, fixtures, alignment tools), Inkscape silkscreen art, and Perl animation-build scripts.
links:
- label: github.com/Wireb/Cyphercon-5_3-2022
  url: https://github.com/Wireb/Cyphercon-5_3-2022
  kind: repo
- label: CypherCon 5.3 event page
  url: https://cyphercon.com/cyphercon-5-3/
  kind: website
- label: 'TYMKRS: Flamingo & Friends Badges (YouTube)'
  url: https://www.youtube.com/watch?v=zcMo0n8MihE
  kind: video
- label: 'r/Tymkrs: CypherCon Badge 2022 (CypherCon 5.0)'
  url: https://www.reddit.com/r/Tymkrs/comments/129sqlv/cyphercon_badge_2022_cyphercon_50/
  kind: social
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/Wireb/Cyphercon-5_3-2022
  title: CypherCon 5.3 Badge (2022)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''cyphercon-2022''.'
- kind: url
  url: https://github.com/Wireb/Cyphercon-5_3-2022/blob/master/README.md
  title: 'Wireb/Cyphercon-5_3-2022: README'
  accessed: '2026-09-07'
  note: Confirmed maker (Peter Shabino / TYMKRS, copyright 2019-2022), five badge variants (Coyote, Flamingo, Llama, Parrot, Peacock), PIC MCU, LCD display, SPI EEPROM animation storage, IR features, vending-machine and lifetime-badge mechanics, KiCad/FreeCAD/Inkscape/MPLAB toolchain, MIT license.
- kind: url
  url: https://cyphercon.com/cyphercon-5-3/
  title: CypherCon 5.3 – CypherCon
  accessed: '2026-09-07'
  note: Confirms TYMKRS as the badge designer and the "Flamingo & Friends" theme for CypherCon 5.3 (April 28-29, 2022, Wisconsin Center).
- kind: url
  url: https://goetzman.com/projects/
  title: Projects - Michael Goetzman
  accessed: '2026-09-07'
  note: Links the 2022 badge to the TYMKRS Reddit post, corroborating "flamingos and friends" naming.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own GitHub README and the CypherCon event page agree on the core facts (TYMKRS design, Peter Shabino firmware/electronics, five animal badge variants, PIC/LCD/IR hardware). Could not find price, quantity made, exact distribution method (whether it shipped with registration or was sold separately), the specific PIC part number, LED count/type, or any photos of an assembled physical badge (only PCB silkscreen artwork and FreeCAD render files were found in the repo, not photographs) - r/Tymkrs, the likely source of photos, could not be fetched (blocked). A FreeCAD subfolder in the repo is named "tymkrs_Cyphercon_2020", suggesting these animal badge designs may date back to or reuse work from a 2020 TYMKRS Cyphercon badge; not confirmed.
last_modified_date: '2026-09-07'
model:
  file: assets/models/cyphercon-2022/cyphercon-5-3-badge-2022.glb
  method: kicad
  source_file: kicad/tymkrs_Cyphercon_2020_Llama/tymkrs_Cyphercon_2020_llama.kicad_pcb
  generated: '2026-09-07'
  bytes: 120408
---

The CypherCon 5.3 (2022) badge was a set of five animal-themed badges - Coyote, Flamingo, Llama, Parrot, and Peacock - designed by TYMKRS with firmware and electronics work by Peter Shabino, distributed as the official badge for CypherCon 5.3 (April 28-29, 2022, Wisconsin Center, Milwaukee). CypherCon promoted the year's theme as "Flamingo & Friends." Each badge runs on a PIC microcontroller and drives an LCD with animated graphics loaded from an SPI EEPROM, and badges could talk to each other and to IR fixtures around the con.

Beyond the display, the badges were part of a larger game: they supported a cryptographic "lifetime badge" scheme with anti-forgery key generation, and tied into a vending machine system that dispensed rewards or unlocked content based on badge interaction. The GitHub repository (published under the MIT license) is a complete record of that ecosystem - KiCad PCB design, FreeCAD mechanical files for stencils and programming fixtures, Inkscape silkscreen artwork for each animal's outline, Perl scripts that build the animation data, and the vending-machine server code - but it does not state a price, production quantity, or how the badges were distributed to attendees.

## Make your own

Hardware and firmware are both published in the repository. The PCB was designed in KiCad, animations are authored as PNG frames per badge type (grouped by eye/face folders for the Coyote/Parrot/Llama, Flamingo, and Peacock variants) and compiled into `.bin` files with the included Perl `build_animations.pl` script, then flashed to the badge's SPI EEPROM; firmware for the PIC MCU was built with MPLAB X 5.35 and programmed via a PicKit4. Mechanical fixtures (screen alignment jigs, flocking stencils) are provided as FreeCAD 0.19 files.
