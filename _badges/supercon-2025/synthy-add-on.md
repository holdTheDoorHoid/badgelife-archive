---
title: Synthy Add-On
id: supercon-2025-synthy-add-on
layout: badge
parent: Supercon 2025
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2025
year: 2025
makers:
- name: incanus (Justin Miller)
  url: https://github.com/incanus
summary: 'A piezo-buzzer SAO that turns the Supercon 2025 badge into a graphical synth keyboard, built on-device during the conference.'
functions: 'Renders a GarageBand-style keyboard on the badge screen; tapping a key plays the corresponding musical note through a piezo buzzer via PWM on the SAO header, with a 250ms auto note-off that can be interrupted by the next note.'
look:
  colors: []
  shape: null
  themes:
  - music
  - hardware tool
tech:
  mcu: 'ESP32 (host badge''s MCU, via SAO header)'
  leds: null
  display: 'Supercon 2025 badge''s built-in graphical display (used to render the keyboard)'
  connectivity: []
  battery: 'powered by host badge'
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '1 (personal conference hack)'
  availability: not_released
  distribution: []
  where: 'Not sold or distributed; a one-off built by the maker at Supercon 2025.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/incanus/synthy-add-on
  eda_tool: null
links:
- label: github.com/incanus/synthy-add-on
  url: https://github.com/incanus/synthy-add-on
  kind: repo
- label: www.hackster.io/news/a-synthesizer-sao-for-the-supercon-2025-badge-ea5a81866b96
  url: https://www.hackster.io/news/a-synthesizer-sao-for-the-supercon-2025-badge-ea5a81866b96
  kind: article
- label: 'justinmiller.io: Supercon 2025 Badge Hack'
  url: https://justinmiller.io/posts/2025/12/01/supercon-2025-badge-hack
  kind: article
images:
  - file: assets/images/badges/supercon-2025/synthy-add-on/c6b65786fb.png
    source: "https://github.com/incanus/synthy-add-on"
    credit: "incanus (Justin Miller)"
    caption: "The Synthy Add-On piezo buzzer SAO plugged into a Supercon 2025 badge"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/incanus/synthy-add-on
  title: Synthy Add-On
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 2025 badge hack SAO, synthesizer add-on, also covered on Hackster.io''.'
- kind: url
  url: https://github.com/incanus/synthy-add-on
  title: incanus/synthy-add-on (README)
  accessed: '2026-09-07'
  note: 'Confirmed maker (incanus, aka Justin Miller), that it is a Supercon 2025 badge hack, and image hack.png.'
- kind: url
  url: https://justinmiller.io/posts/2025/12/01/supercon-2025-badge-hack
  title: 'Supercon 2025 Badge Hack — justinmiller.io'
  accessed: '2026-09-07'
  note: 'Maker''s own blog post: describes it as an SAO with a piezo buzzer wired to the SAO header GPIO 1 and ground, driven by PWM square waves via MicroPython/Thonny on the badge''s ESP32; keyboard UI modeled on GarageBand; 250ms auto note-off, interruptible.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Confirmed via the maker''s GitHub repo and personal blog post (justinmiller.io); the Hackster.io article could not be fetched directly (Cloudflare block) but its content matches the maker''s own blog post. This was a single, one-off conference hack built during Supercon 2025, not a produced/distributed product, so price, quantity beyond one, and distribution fields are left empty or minimal. Firmware (synthy.py) is public on GitHub but no separate hardware design files (schematic/gerbers) were found beyond the simple wiring description (piezo buzzer to SAO GPIO1 and ground), hence make_your_own.open_source is set to partial rather than yes.'
last_modified_date: '2026-09-07'
---

Synthy Add-On is a small hardware hack Justin Miller (GitHub handle incanus) built during Hackaday Supercon 2025, turning the conference badge into a playable synthesizer. He wired a simple piezo buzzer to the badge's SAO header, using one GPIO pin for signal and the adjacent pin for ground, and wrote MicroPython on the badge itself (via the Thonny IDE) to generate musical notes as square waves through pulse-width modulation.

The badge's own screen displays a keyboard modeled after Apple's GarageBand app, letting the player tap out notes visually. Each note plays for 250 milliseconds and can be cut short by the next note being pressed, so successive notes don't overlap awkwardly. Miller documented the build, including testing the output with a pocket oscilloscope, in a blog post shortly after the con.

This was a one-off personal hack rather than a distributed or sold product: no kits, boards, or files beyond the `synthy.py` firmware were released, though that firmware is public on his GitHub repository for anyone who wants to replicate the idea on their own Supercon 2025 badge.
