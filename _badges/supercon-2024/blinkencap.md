---
title: Blinkencap
id: supercon-2024-blinkencap
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Pat Deegan
  url: https://psychogenic.com
summary: 'A SAO shaped like a small hat that blinks an RGB LED using a Tiny Tapeout ASIC, with a fallback discrete-logic oscillator mode if the ASIC isn''t powered up.'
functions: 'Blinks an RGB LED in patterns driven by a TT05 Tiny Tapeout ASIC when clocked/powered via the SAO header; falls back to a standalone auto-blinking mode built from an SN74HC14 hex inverter wired as relaxation oscillators when the ASIC path isn''t used.'
look:
  colors:
  - yellow
  shape: null
  themes:
  - hardware tool
  - minimalist
tech:
  mcu: 'TT05 (Tiny Tapeout) ASIC'
  leds:
    count: 1
    type: RGB
    note: 'Driven either by the TT05 ASIC or by a standalone SN74HC14-based relaxation-oscillator fallback mode; an AP2112K-1.8 regulator supplies the ASIC.'
  display: none
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
  open_source: yes
  hardware_url: https://github.com/psychogenic/blinkencap
  firmware_url: null
  eda_tool: KiCad
  license: CERN-OHL-S
notes: []
links:
- label: hackaday.io/project/198371-blinkencap
  url: https://hackaday.io/project/198371-blinkencap
  kind: hackaday
- label: github.com/psychogenic/blinkencap
  url: https://github.com/psychogenic/blinkencap
  kind: repo
images:
- file: assets/images/badges/supercon-2024/blinkencap/6023ffa3d7.jpg
  source: "https://github.com/psychogenic/blinkencap"
  credit: "Pat Deegan"
  caption: "Blinkencap SAO front, yellow PCB with RGB LED"
- file: assets/images/badges/supercon-2024/blinkencap/ca39cad0f1.jpg
  source: "https://github.com/psychogenic/blinkencap"
  credit: "Pat Deegan"
  caption: "Blinkencap SAO back, showing ASIC and support circuitry"
contact: {}
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198371-blinkencap
  title: Blinkencap
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/198371-blinkencap
  title: Blinkencap - Hackaday.io
  accessed: '2026-09-07'
  note: 'Confirmed maker (Pat Deegan, with matt venn credited for the concept), Supercon 8 (2024) SAO contest entry, TT05 ASIC + SN74HC14 fallback design, and repo link.'
- kind: url
  url: https://github.com/psychogenic/blinkencap
  title: 'psychogenic/blinkencap - GitHub'
  accessed: '2026-09-07'
  note: 'Confirmed open-source hardware under CERN-OHL-S, KiCad design files, AP2112K-1.8 regulator, and pulled front/back board photos from doc/images/.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own Hackaday.io project page and GitHub repo both confirm the core facts (maker, event, chip, open-source status), so this leans toward high confidence, but neither source states price, quantity made, or distribution/availability, so those fields are left empty. The README credits "matt venn" in connection with the hat concept that inspired the shape, but does not spell out a co-maker role, so only Pat Deegan is listed under makers. No SAO header pin-count (v1 vs v2) was stated on either page.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/blinkencap/
---

Blinkencap is a SAO ("simple add-on") made by Pat Deegan of psychogenic.com for the Hackaday Supercon 8 (2024) add-on contest, styled as a small hat that sits on top of a badge — a nod to a hat associated with Tiny Tapeout's matt venn. The board carries a single RGB LED that can be driven two ways: through a TT05 Tiny Tapeout ASIC for programmable blink patterns, or, when the ASIC path isn't in use, through a standalone fallback mode built from an SN74HC14 hex inverter wired up as relaxation oscillators, with an AP2112K-1.8 regulator supplying power. The project leans into its own novelty, describing itself as an intentionally over-engineered way to blink a single LED.

The yellow PCB keeps the ASIC and its support circuitry tucked on the underside so the visible face stays clean. Pat Deegan has published the full hardware design on GitHub under the CERN-OHL-S open hardware license, with KiCad source files included, alongside a Hackaday.io project page (#198371) documenting the build.

## Make your own

The hardware design (schematics and KiCad layout) is published at github.com/psychogenic/blinkencap under CERN-OHL-S. No firmware repository was found — the "programming" for the TT05 ASIC path is part of the Tiny Tapeout chip design rather than a separate flashable firmware image.
