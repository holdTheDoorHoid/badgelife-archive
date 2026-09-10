---
title: Vectorscope-Synth
id: hackaday-europe-2024-vectorscope-synth
layout: badge
parent: Hackaday Europe 2024 (Berlin)
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: hackaday-europe-2024
year: 2024
makers:
- name: softegg
  url: https://github.com/softegg
summary: 'An add-on board for the Hackaday Vectorscope badge (Supercon 2023 / Hackaday Europe 2024) that turns it into a small virtual analog synthesizer, based on softegg''s earlier Stylish Trucker Belt Synthesizer.'
functions: 'Virtual analog synthesizer driven by a stylus-tapped keyboard overlay; drives a 16-LED WS2812B ring and an audio amplifier, using the host badge''s existing screen rather than a display of its own.'
look:
  colors: []
  shape: null
  themes:
  - music
  - hardware tool
tech:
  mcu: STM32 Bluepill
  leds:
    count: 16
    type: WS2812B
    note: 16-LED ring, separate KiCad board
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: '$20 (workshop, planned)'
  price_usd: 20
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: 'Planned as a $20 workshop build at the event, but the maker''s README says parts availability and pricing were unconfirmed going in ("you might be able to do a $20 workshop and get one, or you might have to go find parts and build your own"). No storefront or evidence it was actually distributed as a finished batch.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/softegg/Vectorscope-Synth
  firmware_url: https://github.com/softegg/Stylish-Trucker-Belt-Synthesizer
  eda_tool: KiCad
  license: null
  notes: 'Repo has no LICENSE file. Firmware is said to reuse the source from softegg''s separate Stylish-Trucker-Belt-Synthesizer project rather than shipping its own.'
links:
- label: github.com/softegg/Vectorscope-Synth
  url: https://github.com/softegg/Vectorscope-Synth
  kind: repo
- label: 'Stylish Trucker Belt Synthesizer (firmware source)'
  url: https://github.com/softegg/Stylish-Trucker-Belt-Synthesizer
  kind: repo
images:
  - file: assets/images/badges/hackaday-europe-2024/vectorscope-synth/27987296d6.jpg
    source: "https://github.com/softegg/Vectorscope-Synth"
    credit: "softegg"
    caption: "Render of the Vectorscope-Synth add-on board (front)"
  - file: assets/images/badges/hackaday-europe-2024/vectorscope-synth/dde2773cfa.jpg
    source: "https://github.com/softegg/Vectorscope-Synth"
    credit: "softegg"
    caption: "Render of the Vectorscope-Synth add-on board (back)"
contact: {}
notes:
- 'Sweep''s wording was "Add-on board for the Hackaday Supercon 2023 / Hackaday Europe (Berlin) 2024 Vectorscope badge implementing a small virtual analog synthesizer based on the Stylish Trucker Belt Synthesizer" - confirmed by the maker''s own repo, title unchanged from the sweep.'
status: announced
sources:
- kind: url
  url: https://github.com/softegg/Vectorscope-Synth
  title: Vectorscope-Synth
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:hackaday-europe); event read as ''hackaday-europe-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/softegg/Vectorscope-Synth/main/README.md
  title: 'Vectorscope-Synth README'
  accessed: '2026-09-10'
  note: 'Confirmed maker, purpose, host badge, STM32 Bluepill MCU, WS2812B LED ring, amplifier, stylus keyboard, planned $20 workshop pricing with acknowledged uncertainty, and the two front/back render image URLs.'
- kind: url
  url: https://api.github.com/repos/softegg/Vectorscope-Synth
  title: 'GitHub API: softegg/Vectorscope-Synth'
  accessed: '2026-09-10'
  note: 'Repo created 2024-04-03 (after Hackaday Europe 2024, which ran in March 2024) and last pushed 2025-02-24; confirmed no LICENSE file is present.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Maker''s own repo confirms this is a real, designed add-on (KiCad files for the main board, LED ring, and amp board are all present) rather than just a search snippet. However the repo was created 2024-04-03, after Hackaday Europe 2024 (Berlin) ran in March 2024, and the README calls the timeline "very much in flux" with the workshop/pricing unconfirmed and functionality untested at time of writing ("This has not yet been tested... It might work, or it might be crap"). No evidence was found that it was actually built, sold, or handed out at either Supercon 2023 or Hackaday Europe 2024 - set status to announced rather than released or listed. Kept event as hackaday-europe-2024 per the sweep since that is the event the README and repo description name most prominently alongside Supercon 2023 (no dedicated Supercon 2024 badge is implicated); a supercon-2023 event id also exists in events.yml if this should instead be filed there. Not a duplicate of the archive''s existing hackaday-europe-2024-vectorscopemusicaddon entry (davedarko''s VectorScopeMusicAddon) - that is an unrelated, simpler axis-swap PCB for the same host badge''s built-in scope-music mode, with no MCU of its own; this is a separate, MCU-driven synthesizer add-on by a different maker. No price_usd beyond the tentative $20 workshop figure, no quantity, and no photos of an assembled unit (only KiCad renders) were found.'
last_modified_date: '2026-09-10'
---

Vectorscope-Synth is an add-on board by softegg for the Hackaday Vectorscope badge, the badge used at Supercon 2023 and reused at Hackaday Europe 2024 (Berlin). It adds a small virtual analog synthesizer to the host badge, built around an STM32 "Bluepill" board, a 16-LED WS2812B ring, an XH-M125 audio amplifier module, and a stylus-tapped keyboard overlay. The firmware is meant to be shared with softegg's earlier Stylish Trucker Belt Synthesizer project rather than maintained separately.

The maker's README is candid that the design was unfinished and unverified going in: with limited lead time before the show and uncertain parts availability, the plan was a possible $20 build-it-yourself workshop, but the maker flags concern that the Vectorscope badge's own two batteries might not have enough capacity to also drive the synth's Bluepill, LED ring, and amplifier, and notes the board "has not yet been tested." No evidence was found that it was ultimately built, demoed, or distributed at the event - only KiCad design files and two render images (front and back) are in the repo, with no photos of an assembled unit.

Hardware design files (KiCad schematics and PCB layouts for the main board, the LED ring, and the amplifier board, plus a laser-cut stylus keyboard layout) are published on GitHub with no license file attached. This is a separate project from the archive's other Vectorscope-badge accessory, davedarko's VectorScopeMusicAddon - that one is a simple oscilloscope-music switch PCB with no MCU of its own; this one is a full synthesizer with its own microcontroller.
