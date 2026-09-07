---
title: tr25-sao-hw — Troopers 25 Shitty Add-On
id: other-tr25-sao-hw-troopers-25-shitty-add-on
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2025
makers:
- name: jeffmakes
  url: https://github.com/jeffmakes
summary: A passive 4-LED SAO made for TROOPERS 25 (ERNW's security conference), shaped as a UFO abducting a cow.
functions: Lights up in RGB via its four addressable LEDs, driven entirely by the host TROOPERS 25 badge (no onboard microcontroller).
look:
  colors: [white]
  shape: ufo
  themes: [sci-fi, space, animal, cow, meme]
tech:
  mcu: none
  leds:
    count: 4
    type: SK6812SMINI-ER
    note: Addressable RGB LEDs in a chain, driven by the host badge's data line; no onboard MCU.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: '420'
  availability: unknown
  distribution: []
  where: 'Made for attendees of TROOPERS 25 (ERNW), the badge''s host conference; distribution method to attendees not confirmed from available sources.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/jeffmakes/tr25-sao-hw
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/jeffmakes/tr25-sao-hw
  url: https://github.com/jeffmakes/tr25-sao-hw
  kind: repo
images:
  - file: assets/images/badges/other/tr25-sao-hw-troopers-25-shitty-add-on/aba0e24047.jpg
    source: "https://github.com/jeffmakes/tr25-sao-hw"
    credit: "jeffmakes (Jeff Gough)"
    caption: "Front of the SAO: a UFO abducting a cow, PCB rendering"
  - file: assets/images/badges/other/tr25-sao-hw-troopers-25-shitty-add-on/100c62f33d.jpg
    source: "https://github.com/jeffmakes/tr25-sao-hw"
    credit: "jeffmakes (Jeff Gough)"
    caption: "Back of the SAO: TROOPERS 25 / ERNW branding, Jeff Gough @jeffmakes, Monad 2025"
contact: {}
notes:
  - "Repo has no README; all facts below are drawn from the KiCad schematic, board renders, and PCB fab job specification committed to the repository."
status: released
sources:
- kind: url
  url: https://github.com/jeffmakes/tr25-sao-hw
  title: tr25-sao-hw — Troopers 25 Shitty Add-On
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''Troopers 2025''.'
- kind: url
  url: https://github.com/jeffmakes/tr25-sao-hw/blob/main/r1/build/tr25-sao-r1-sch.pdf
  title: tr25-sao-r1 schematic (KiCad export)
  accessed: '2026-09-07'
  note: 'Confirms 4x SK6812SMINI-ER RGB LEDs, no MCU, standard 6-pin (v1.69bis) SAO header, and a design note that the host TROOPERS 25 badge uses its ESP32-S3 to drive the LEDs non-standardly through IO2 (audio DAC/SPKR on IO1).'
- kind: url
  url: https://github.com/jeffmakes/tr25-sao-hw/blob/main/r1/build/tr25-sao-job-specification.txt
  title: tr25-sao-r1 PCB fab job specification
  accessed: '2026-09-07'
  note: 'Confirms production quantity of 420pcs, 2-layer 1.6mm FR4, white soldermask, black silkscreen, HASL finish.'
- kind: url
  url: https://github.com/jeffmakes/tr25-sao-hw/blob/main/r1/build/tr25-sao-r1-front.png
  title: tr25-sao-r1 front render
  accessed: '2026-09-07'
  note: 'Front artwork: a flying saucer with a beam abducting a cow, alien silhouette in the dome.'
- kind: url
  url: https://github.com/jeffmakes/tr25-sao-hw/blob/main/r1/build/tr25-sao-r1-back.png
  title: tr25-sao-r1 back render
  accessed: '2026-09-07'
  note: 'Back silkscreen: ERNW logo, "TROOPERS 25", "Jeff Gough @jeffmakes", "Monad 2025".'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Event corrected from "other" (Troopers 2025) — no matching id exists yet in _data/events.yml for TROOPERS (ERNW''s Heidelberg, Germany conference), so event is left as other and the con is named here: this SAO was made for TROOPERS 25 (2025). No README, storefront, or social post was found describing price or exact distribution method to attendees; the repo (design files, schematic, and fab job spec) was the only available source. Web search was unavailable for this task (session search budget exhausted) so third-party coverage could not be checked.'
last_modified_date: '2026-09-07'
---

The tr25-sao-hw is a Shitty Add-On made by Jeff Gough (jeffmakes, trading as Monad) for TROOPERS 25, the ERNW-run security conference. It has no onboard microcontroller: four SK6812SMINI-ER addressable RGB LEDs are wired in a chain straight to a standard 6-pin (v1.69bis) SAO header, so all the animation logic lives on the host TROOPERS 25 conference badge rather than on the add-on itself. The schematic notes a quirk of that host badge: its ESP32-S3 drives the SAO's LEDs over IO2 instead of the standard IO1, because IO1 doubles as the badge's audio DAC/speaker output, and a resistor is added so a spec-compliant badge could still drive the LEDs through IO1 without attenuating the speaker signal.

The board is shaped as a flying saucer beaming up a cow, with a bug-eyed alien peeking out of the dome on the front, and the ERNW logo, "TROOPERS 25," and "Jeff Gough @jeffmakes / Monad 2025" silkscreened on the back. The design (KiCad schematic, PCB layout, and Gerbers/fab job specification) is published in full on GitHub. The PCB fab job specification lists a production run of 420 boards on white-soldermask, black-silkscreen 2-layer FR4 with HASL finish. No storefront, price, or specific attendee-distribution details were found; it reads as conference-badge hardware rather than a sold item.

## Make your own

The `design/` folder holds the front artwork (SVG), `docs/` has datasheets for the LED (SK6812SMINI-ER) and the header connector, and `r1/src` contains the KiCad project (with jeffmakes' own KiCad library as a submodule). `r1/build` has the finished schematic and board PDFs, front/back renders, the Gerber-based production-data archive, and the PCB fab job specification (420pcs, 2-layer 1.6mm FR4, white soldermask/black silkscreen, HASL).
