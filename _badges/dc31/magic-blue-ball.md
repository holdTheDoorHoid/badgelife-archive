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
  - pop culture
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
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched https://ghostglitch.net/sao/magicball via curl (WebFetch fails on its expired TLS cert, confirming the researcher''s note) and confirmed the DEF CON 31 attribution, the 555 timer/decade counter/tilt switch circuit, the shake-and-settle operation, and the "about as random as any D10" quote verbatim. Corrected two unsupported claims: look.themes had "meme" and "puzzle", neither stated or implied by the source, replaced with "pop culture" (the page explicitly frames it as resembling the real-world Magic 8 Ball toy); the body wrongly said it answers "yes/no-style questions" (the page describes a multi-output random answer, consistent with a decade counter, not a binary one) and wrongly claimed GhostGlitch''s site frames it as predating/simpler than their Blushy SAO (that claim traces to "their blog" per the discovery-sweep source note, a page never fetched or cited here) — both sentences were corrected or removed. Only source found is the maker''s own project page, which is thorough on concept/circuit but silent on price, quantity made, distribution method, LED count/type, and design-file links; no store listing, repo, or press coverage found. Everything remaining in the entry is supported by that page.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/magic-blue-ball/
---

The Magic Blue Ball is an SAO made by GhostGlitch to fit the DEF CON 31 (2023) badge, styled as a miniature Magic 8 Ball — round, blue, and settling on a random answer when shaken. Rather than running on a microcontroller, it uses a small discrete circuit: a tilt switch feeds a 555 timer and decade counter, so shaking the board drives a flashing LED sequence that gradually slows and settles on one of several outputs. The maker describes it as "about as random as any D10" given enough shaking before it settles.

The project page does not give a price, production quantity, or how it was distributed at DEF CON 31, and no separate store listing, repository, or press coverage turned up in this pass. The maker's photo of the badge is linked from the page (`/assets/magic-blue-ball-photo.png`, with `.avif`/`.webp` variants) but could not be archived here because ghostglitch.net's TLS certificate is currently expired.
