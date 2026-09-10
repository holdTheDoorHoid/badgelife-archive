---
title: Ox Vox
id: bsides-portland-2017-ox-vox-add-on
layout: badge
parent: BSidesPDX 2017
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: bsides-portland-2017
year: 2017
makers:
- name: Rob Rehrig
  url: https://www.robrehrig.com/ox_vox
summary: An ox-and-wagon-shaped add-on that turns the BSidesPDX 2017 (BMD-300) badge into a tiny eight-key synthesizer.
functions: Replaces the badge's two joysticks with eight momentary buttons wired as a full octave (C to C); an on-board amplifier and speaker play the pressed note as a smoothed sine wave, and a small OLED shows "THE OX VOX" / the current note.
look:
  colors:
  - purple
  - black
  shape: wagon
  themes:
  - animal
  - music
tech:
  mcu: none (uses host badge's BMD-300 / nRF52832)
  leds: null
  display: 0.9" OLED (host badge display, driven by Ox Vox firmware)
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: 'Not sold; a one-off add-on Rehrig built and demoed himself, with design files released on GitHub for anyone to build their own.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/mediumrehr/oxvox
  firmware_url: https://github.com/mediumrehr/oxvox
  eda_tool: Eagle
links:
- label: badge.gallery/badges/bsidespdx-2017-bmd-300-badge
  url: https://badge.gallery/badges/bsidespdx-2017-bmd-300-badge
  kind: website
- label: robrehrig.com/ox_vox
  url: https://www.robrehrig.com/ox_vox
  kind: website
- label: mediumrehr/oxvox (GitHub)
  url: https://github.com/mediumrehr/oxvox
  kind: repo
- label: 'Ox-Vox: Hacking Con Badges Before the Con (talk)'
  url: https://allbsides.com/talk/ko67pbjqiME.html
  kind: video
images:
- file: assets/images/badges/bsides-portland-2017/ox-vox-add-on/5f162d190c.jpg
  source: "https://www.robrehrig.com/ox_vox"
  credit: "Rob Rehrig"
  caption: "Ox Vox v2 mounted on a BSidesPDX 2017 badge, OLED reading THE OX VOX"
- file: assets/images/badges/bsides-portland-2017/ox-vox-add-on/455a1ac8a0.jpg
  source: "https://www.robrehrig.com/ox_vox"
  credit: "Rob Rehrig"
  caption: "Ox Vox v2 board, front and back, silkscreened OX VOX v2 / BSIDES PDX / 2017"
contact: {}
notes:
- Add-on built for the (then-unreleased) BSidesPDX 2017 badge, presented by Rob Rehrig at the con. Found by the event-year sweep, task bsides-portland.
- The community sheet/sweep called this "Ox-Vox add-on"; the maker's own name for it is just "Ox Vox" (title updated to match).
- 'Source disagreement: the GitHub README describes the project as made for the "DEF CON 25 503 party and BSides PDX 2018 badges," and one GitHub Open-Graph caption also says "BSides PDX 2017 badge." The BSidesPDX badge timeline (badge.gallery/series/bsidespdx) puts the BMD-300 badge itself at 2017, and a photo of the finished v2 board is silkscreened "BSIDES PDX / 2017," which matches this entry''s event/year. Treated the silkscreen + timeline as authoritative and kept event/year at 2017; the "2018" in the README note is most likely the writer conflating it with when the talk video went up (published March 2018) or a slip of memory, not a second badge revision.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/bsidespdx-2017-bmd-300-badge
  title: Ox-Vox add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-portland); event read as ''BSidesPDX 2017''.'
- kind: url
  url: https://www.robrehrig.com/ox_vox
  title: Ox Vox — Rob Rehrig
  accessed: '2026-09-10'
  note: 'Maker''s own project page: what it is, how the two versions (DC25 / BSidesPDX) were built, and photos of the finished boards.'
- kind: url
  url: https://github.com/mediumrehr/oxvox
  title: mediumrehr/oxvox
  accessed: '2026-09-10'
  note: 'Source repo: BMD-300/nRF52832 host chip, Eagle hardware files, nRF5 SDK firmware, MIT license, button/speaker/amplifier details, and the "BSides PDX 2018 badges" wording that conflicts with the board silkscreen.'
- kind: url
  url: https://badge.gallery/series/bsidespdx
  title: 'BSidesPDX · Hacker Con Badges (badge.gallery)'
  accessed: '2026-09-10'
  note: 'Confirms the BMD-300 badge is the 2017 BSidesPDX badge and that Rehrig presented Ox-Vox at the 2017 conference targeting that badge.'
- kind: url
  url: https://allbsides.com/talk/ko67pbjqiME.html
  title: 'Rob Rehrig - Ox-Vox: Hacking Con Badges Before the Con'
  accessed: '2026-09-10'
  note: 'Talk describing the reverse-engineering process (built from a single photo before the badge was released) and the eight-key/sine-wave/nRF52 design.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Core facts (maker, what it does, chip, event) confirmed on the maker''s own page, GitHub repo, and a board photo. Left quantity/price empty — this was a personal build/demo, not sold, and no quantity is stated anywhere. One unresolved disagreement about badge year across sources; see notes above for how it was resolved.'
last_modified_date: '2026-09-10'
---

The Ox Vox is an ox-and-wagon-shaped add-on built by Rob Rehrig (@mediumrehr) for the BSidesPDX 2017 badge, itself built around a Nordic BMD-300 (nRF52832) module. It replaces the badge's two joystick inputs with eight momentary push buttons wired as a full musical octave (C to C), generating notes as wavetables on a PWM pin, smoothing them into a sine wave, and pushing the result through an LM4861 amplifier into a small onboard speaker; the host badge's OLED is repurposed to show "THE OX VOX" and the currently played note.

Rehrig's first version was built for the DEF CON 25 503-party badge in about a week, before he had physical access to that badge — he worked from a single published photo to reverse-engineer its joystick pinout. He then built a refined second version, professionally fabricated and silkscreened "OX VOX v2 / BSIDES PDX / 2017," to match that year's BSidesPDX badge, and presented the whole process — inspiration, reverse-engineering, prototyping, and the finished board — as a talk at the con. It was never sold; Rehrig made it for himself and to demonstrate the technique, then released the Eagle hardware files and nRF5-SDK firmware on GitHub under the MIT license so others could build their own.

## Make your own

Hardware (Eagle PCB) and firmware source are both on GitHub at [mediumrehr/oxvox](https://github.com/mediumrehr/oxvox). Building one means: fabricate the PCB, solder in the eight buttons, speaker, and LM4861 amp circuit, wire it in place of the two joysticks on a compatible BMD-300 badge (DC25 503 badge or BSidesPDX badge pinouts are both documented in the repo), then flash the BMD-300 (nRF52832) over SWD with the provided firmware, built against nRF5 SDK v13.0.0 in Keil uVision.

