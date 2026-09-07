---
title: DC801 Black Mage Badge
id: dc28-dc801-bm-badge
layout: badge
parent: DC28
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc28
year: 2020
makers:
- name: DC801
  url: https://dc801.store
summary: A fully custom, open-source DEF CON party badge built around an nRF52840 SoC and a touchscreen, running a built-in game ("Hex Quest") where the hero's power is opening a hex editor and patching the game's own live memory.
functions: >-
  Runs a custom-built game engine playing "Hex Quest," a story-driven puzzle game whose
  central mechanic is a live hex editor: the player edits RAM to manipulate the overworld,
  NPCs, enemies, and their own character. Chapter 2 adds a USB-C serial console interface,
  a "bling mode" with screensaver-style LED patterns, and a sandbox demo mode. Content is
  authored in Tiled Map Editor plus a custom JSON scripting language, so owners can build
  their own playable scenarios.
look:
  colors: []
  shape: null
  themes:
  - fantasy
  - hardware tool
  - puzzle
  - retro computer
tech:
  mcu: Nordic nRF52840 (u-blox BMD-340 module, ARM Cortex-M4F @ 64MHz)
  leds: 19
  display: 2.4" 240x320 TFT LCD with touch panel
  connectivity:
  - bluetooth
  - usb
  inputs:
  - buttons
  - touch
  power: LiPo battery with on-board USB-C charging
  battery: LiPo, on-board charging
  sao_version: v1.69bis
  sao_ports: 1
make_your_own:
  open_source: yes
  hardware_url: https://github.com/DC801/BM-Badge/tree/main/Hardware
  firmware_url: https://github.com/DC801/BM-Badge
  eda_tool: KiCad
  license: AGPL-3.0
  notes: Full hardware (KiCad) and firmware source on GitHub, including a browser-playable web build of the game and a binary encoder for building custom scenarios.
links:
- label: github.com/dc801/BM-Badge
  url: https://github.com/dc801/BM-Badge
  kind: repo
- label: dc801.github.io/BM-Badge (play in browser)
  url: https://dc801.github.io/BM-Badge/
  kind: website
- label: DC801 store
  url: https://dc801.store
  kind: store
- label: DEF CON Forums thread
  url: https://forum.defcon.org/node/234773
  kind: article
images:
- file: assets/images/badges/dc28/dc801-bm-badge/7f6fbceec3.png
  source: "https://dc801.store/products/dc801-black-mage-badge-2nd-batch"
  credit: "DC801"
  caption: "DC801 Black Mage Badge (2nd batch, 2022) product photo"
contact: {}
notes:
- 'Sheet/sweep listed this generically as a "badge platform"; the maker calls it the "DC801 Black Mage Badge."'
status: released
sources:
- kind: url
  url: https://github.com/dc801/BM-Badge
  title: DC801 BM-Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 28+ badge platform''.'
- kind: url
  url: https://github.com/DC801/BM-Badge/blob/main/README.md
  title: 'BM-Badge README'
  accessed: '2026-09-07'
  note: Hardware spec list, SAO/MiniBadge/ART headers, open-source license, game engine and Chapter 1/2 description.
- kind: url
  url: http://web.archive.org/web/20231004141623/https://dc801.store/products/dc801-black-mage-badge-2nd-batch
  title: 'DC801 Black Mage Badge: 2nd Batch (archived store listing)'
  accessed: '2026-09-07'
  note: Confirms full hardware spec, origin story (funds the DC801 DEF CON party and 801Labs hackerspace), 2nd-batch pricing ($801 list / $180 sale) and shipping for DC30 (2022), and that DEF CON 28 was the badge's debut year.
- kind: url
  url: https://forum.defcon.org/node/234773
  title: DC801 Badge - DEF CON Forums
  accessed: '2026-09-07'
  note: 'Corroborates: 1st-batch sales ran Aug 8 2020 - end of Jan 2021 and sold out, badges shipped within a week of July 12 2021.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    This entry covers the original DC28 (2020) "1st batch" Black Mage Badge. No source gave
    the 1st-batch price or exact unit count, so get_one.price/price_usd/quantity are left
    empty rather than guessed; the $801/$180 pricing found is specifically for the 2nd batch
    (sold for DC30, 2022) and is not applied here. The badge line continued with new batches
    and firmware chapters through at least DC32 (2024); those later releases belong to
    separate history, not this DC28 entry. A different, unaffiliated maker ("redactd") sold a
    "Bootleg Edition" reproduction of this badge on Tindie (black FR4, blue LEDs, $250,
    out of stock since Aug 2022) — noted below as a possible separate entry, not folded in here.
last_modified_date: '2026-09-07'
---

The DC801 Black Mage Badge is the DEF CON 28 (2020) debut of an open-source badge platform built by DC801, the group behind Salt Lake City's DEF CON party crew and the 801Labs hackerspace. Proceeds from badge sales fund both the annual DC801 party and the hackerspace. Around an nRF52840 SoC (on a u-blox BMD-340 module), a 2.4" touchscreen, 27 NKRO buttons, 19 LEDs, a speaker, and a SAO/SAINTCON MiniBadge expansion header, the badge runs a fully custom game engine rather than off-the-shelf badge firmware.

The built-in game, "Hex Quest," casts the wearer as a hacker-wizard whose signature power (a nod to the Final Fantasy "Black Mage" class) is a live hex editor: rather than casting fire or ice, the player edits the running game's own RAM to solve puzzles, uncover secrets, and manipulate NPCs and the world itself. The 2020 badge shipped with Chapter 1 of the story; a free firmware update later added Chapter 2, which layered in a USB-C serial console interface, additional puzzles, a "bling mode" of LED screensaver patterns, and a sandbox/demo mode, and is playable by all existing badges as well as a second hardware batch.

Both the KiCad hardware design and the firmware are open source (AGPL-3.0) on GitHub, along with a browser-playable build of the game and tooling (Tiled Map Editor + a custom JSON scripting language) for anyone who wants to author their own scenario. Sales for the original 2020 run were open from August 2020 through the end of January 2021 and sold out, with badges shipping in July 2021; DC801 has since continued the line with further batches and story chapters for later DEF CONs.

## Make your own

Hardware (KiCad projects, schematics, and SAO/ART board designs) and firmware live in the [DC801/BM-Badge GitHub repository](https://github.com/DC801/BM-Badge), under `Hardware/` and `Software/` respectively, licensed AGPL-3.0. The repo also includes an SD-card game-authoring toolchain (binary encoder plus Tiled Map Editor + JSON scripting) for building custom playable scenarios, and a browser-playable version of the game at [dc801.github.io/BM-Badge](https://dc801.github.io/BM-Badge/).
