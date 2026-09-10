---
title: BSides SLC 2019 Badge
id: bsides-slc-2019-bsides-slc-2019-badge
layout: badge
parent: BSides Slc 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-slc-2019
year: 2019
makers:
- name: Professor-plum (with challenge design by bashNinja)
summary: A touchscreen conference badge for BSides SLC 2019 built around an STM32F103 microcontroller, packed with a 12-challenge CTF-style puzzle sequence designed by bashNinja of 801 Labs.
functions: Drives a touchscreen UI (arcade, DJ mixer, TV, phone dialer, market, alley and other in-game "scenes") built from on-badge bitmap/GIF assets, gating access to a 12-stage set of hidden challenges/puzzles; also plays WAV audio cues from onboard serial flash.
look:
  colors: []
  shape: null
  themes:
  - ctf
  - puzzle
  - retro computer
tech:
  mcu: STM32F103CB
  leds: null
  display: touchscreen
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
  open_source: true
  hardware_url: https://github.com/Professor-plum/BSides-SLC-Badge-2019/tree/master/eagle
  firmware_url: https://github.com/Professor-plum/BSides-SLC-Badge-2019/tree/master/src
  eda_tool: Eagle
links:
- label: github.com/Professor-plum/BSides-SLC-Badge-2019
  url: https://github.com/Professor-plum/BSides-SLC-Badge-2019
  kind: repo
- label: 'bashNinja: Solving the BSidesSLC 2019 Badge (YouTube)'
  url: https://www.youtube.com/watch?v=G3LeRYf3Ors
  kind: video
  note: Walkthrough of all 12 badge challenges and their solutions.
- label: 'Security Boulevard: BSides SLC 2019, bashNinja''s ''Solving The BSidesSLC 2019 Badge'''
  url: https://securityboulevard.com/2019/05/bsides-slc-2019-bashninjas-solving-the-bsidesslc-2019-badge/
  kind: article
images: []
contact: {}
notes:
- STM32F103CB-based conference badge with touchscreen and serial flash storage, source/design files published by Professor-plum; badge's 12 challenges were later walked through by bashNinja/801Labs. Found by the event-year sweep, task bsides-bsides-slc.
- Sweep imported the title as "BSides SLC 2019 Badge"; the maker's own repo/README use the same wording, so no title change was needed.
status: listed
sources:
- kind: url
  url: https://github.com/Professor-plum/BSides-SLC-Badge-2019
  title: BSides SLC 2019 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-slc); event read as ''BSides SLC 2019''.'
- kind: url
  url: https://raw.githubusercontent.com/Professor-plum/BSides-SLC-Badge-2019/master/README.md
  title: 'Professor-plum/BSides-SLC-Badge-2019: README'
  accessed: '2026-09-10'
  note: Confirms MCU (STM32F103CB, Arduino_STM32 core), touchscreen (XPT2046) and serial flash storage; MIT license; build instructions.
- kind: url
  url: https://www.youtube.com/watch?v=G3LeRYf3Ors
  title: Solving the BSidesSLC 2019 Badge by bashNinja
  accessed: '2026-09-10'
  note: Confirms the badge shipped with 12 challenges and that bashNinja (801 Labs) designed and later walked through the solutions.
- kind: url
  url: https://securityboulevard.com/2019/05/bsides-slc-2019-bashninjas-solving-the-bsidesslc-2019-badge/
  title: BSides SLC 2019, bashNinja's 'Solving The BSidesSLC 2019 Badge'
  accessed: '2026-09-10'
  note: Cross-posted coverage of the same walkthrough talk, corroborating the challenge-design credit.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: The maker's GitHub repo (README, Eagle files, Arduino source, a schematic PDF) confirms the hardware and firmware, and a separate walkthrough talk confirms the 12-challenge design credited to bashNinja. No price, production quantity, distribution method, or LED info is stated anywhere found; get_one fields and tech.leds are left empty rather than guessed. The repo's img/ and gifs/ folders hold in-game UI bitmaps (arcade, DJ mixer, TV, etc.) used by the touchscreen challenges, not photos of the physical badge, so no images were saved for this entry — a real photo would need to come from a con recap or social post not found in this pass.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsides-slc-2019/bsides-slc-2019-badge.glb
  method: kicad
  source_file: Badge Proto.brd
  generated: '2026-09-10'
  bytes: 195196
---

The BSides SLC 2019 badge is a touchscreen conference badge built by Professor-plum around an STM32F103CB microcontroller (Arduino_STM32 core), an XPT2046 resistive touchscreen, and serial flash for storage. Rather than a simple blinky badge, it runs a small on-screen "world" — an arcade, a DJ mixer, a TV, a phone dialer, a street/alley scene, a market — built from custom bitmap and GIF assets, with WAV audio cues played from the flash chip.

Layered on top of the hardware is a 12-stage puzzle/CTF sequence designed by bashNinja of 801 Labs (the Salt Lake City hackerspace behind BSidesSLC). After the con, bashNinja published a full walkthrough covering all 12 challenges and their solutions, later covered by Security Boulevard and Infosecurity.us.

Hardware, Eagle design files, and Arduino source are published on GitHub under the MIT license, along with a `SLCBadge.pdf` schematic. No pricing, production quantity, or distribution details for the physical badge were found in this research pass.
