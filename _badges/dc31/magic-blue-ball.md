---
title: Magic Blue Ball
id: dc31-magic-blue-ball
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: GhostGlitch
  url: https://ghostglitch.net
summary: 'A DEF CON 31 SAO shaped like a Magic 8 Ball: shake it and a tilt switch drives an LED sequence that "settles" on a random answer.'
functions: 'Shake the SAO; a tilt switch feeds a 555 timer / decade counter chain that flashes LEDs, gradually slowing until it settles on one random output, like a D10 roll or a Magic 8 Ball answer.'
look:
  colors:
  - blue
  shape: circle
  themes:
  - meme
  - puzzle
tech:
  mcu: none
  leds: null
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
- label: ghostglitch.net/sao/magicball
  url: https://ghostglitch.net/sao/magicball
  kind: website
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- 'Image seen but not saved: https://ghostglitch.net/assets/magic-blue-ball-photo.png (also .avif/.webp variants) — ghostglitch.net''s TLS certificate has expired, so downloads over https fail certificate verification.'
status: released
sources:
- kind: url
  url: https://ghostglitch.net/sao/magicball
  title: Magic Blue Ball
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''unclear - GhostGlitch''s earliest SAO, predates Blushy per their blog, likely an earlier DEF CON not yet in the archive''.'
- kind: url
  url: https://ghostglitch.net/sao/magicball
  title: Magic Blue Ball
  accessed: '2026-09-07'
  note: 'Maker''s own project page: confirms it was made to fit the DEF CON 31 badge, describes the shake-and-settle operation, and states the circuit uses a 555 timer, a decade counter, and a tilt switch (no microcontroller).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source found is the maker''s own project page, which is thorough on concept/circuit but silent on price, quantity made, distribution method, LED count/type, and design-file links. Could not reach a store listing, repo, or press coverage for this piece. Event corrected from "other"/DC31-unclear to dc31: the maker''s page states outright it was "made to fit the DEFCON 31 badge." Image URLs exist on the page but could not be downloaded because ghostglitch.net currently serves an expired TLS certificate.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/magic-blue-ball/
---

The Magic Blue Ball is an SAO made by GhostGlitch to fit the DEF CON 31 (2023) badge, styled as a miniature Magic 8 Ball — round, blue, and answering yes/no-style questions when shaken. Rather than running on a microcontroller, it uses a small discrete circuit: a tilt switch feeds a 555 timer and decade counter, so shaking the board drives a flashing LED sequence that gradually slows and settles on one of several outputs. The maker describes it as "about as random as any D10" given enough shaking before it settles.

GhostGlitch's site frames Magic Blue Ball as an earlier, simpler SAO than their later Blushy piece, but the project page does not give a price, production quantity, or how it was distributed at DEF CON 31, and no separate store listing, repository, or press coverage turned up in this pass. The maker's photo of the badge is linked from the page (`/assets/magic-blue-ball-photo.png`, with `.avif`/`.webp` variants) but could not be archived here because ghostglitch.net's TLS certificate is currently expired.
