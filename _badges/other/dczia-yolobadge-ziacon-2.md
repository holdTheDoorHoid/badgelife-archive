---
title: DCZia yolobadge (Ziacon 2)
id: other-dczia-yolobadge-ziacon-2
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2021
makers:
- name: DCZia
  url: https://dczia.net/
summary: A one-shot electronic badge that DCZia designed and built live on stage during a talk at ZiaCon 2 in April 2021, finished in about four hours.
functions: Lights up 10 addressable LEDs in patterns via an Arduino/FastLED sketch; breaks out serial and an SAO port for further hacking.
look:
  colors: []
  shape: null
  themes:
  - meme
  - badgelife
tech:
  mcu: ATmega32U4
  leds:
    count: 10
    type: WS2812B
    note: Neopixel-compatible, driven with the FastLED library.
  display: none
  connectivity:
  - usb
  - uart
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/dczia/yolobadge/tree/main/Hardware
  firmware_url: https://github.com/dczia/yolobadge/tree/main/Software
  eda_tool: KiCad
links:
- label: github.com/dczia/yolobadge
  url: https://github.com/dczia/yolobadge
  kind: repo
  archived: https://web.archive.org/web/20260523084137/https://github.com/dczia/yolobadge
- label: DCZia
  url: https://dczia.net/
  kind: website
  archived: https://web.archive.org/web/20260514004509/https://dczia.net/
images:
- file: assets/images/badges/other/dczia-yolobadge-ziacon-2/34ac082c1b.jpg
  source: https://github.com/dczia/yolobadge
  credit: DCZia
  caption: Rendering of the yolobadge PCB
  archived: https://web.archive.org/web/20260523084137/https://github.com/dczia/yolobadge
- file: assets/images/badges/other/dczia-yolobadge-ziacon-2/dbd797d67e.jpg
  source: https://github.com/dczia/yolobadge
  credit: DCZia
  caption: Photo of the assembled yolobadge
  archived: https://web.archive.org/web/20260523084137/https://github.com/dczia/yolobadge
contact: {}
notes:
- Made for ZiaCon 2 (DCZia's own convention, held in Albuquerque, NM), not a DEF CON badge, despite the repo README also mentioning "DefCon 29" in its title line (ZiaCon 2 ran alongside DEF CON 29's 2021 hybrid/remote year).
status: released
sources:
- kind: url
  url: https://github.com/dczia/yolobadge
  title: DCZia yolobadge (Ziacon 2)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''Ziacon 2''.'
  archived: https://web.archive.org/web/20260523084137/https://github.com/dczia/yolobadge
- kind: url
  url: https://github.com/dczia/yolobadge
  title: 'GitHub - dczia/yolobadge: Ziacon 2 #yolobadge design files'
  accessed: '2026-09-07'
  note: 'README: badge was designed and built live during a ~4 hour talk at ZiaCon 2, April 2021. Credits hamster (layout), jediguybob/lithochasm/DCZia (design input), LunaSylumDancer (art), Syntax (challenge). Hardware: ATmega32U4, 10x WS2812B, micro-USB power, SAO port, serial breakout. Software: Arduino sketch with FastLED. KiCad hardware files and Arduino sketch both present in the repo.'
  archived: https://web.archive.org/web/20260523084137/https://github.com/dczia/yolobadge
- kind: url
  url: https://dczia.net/
  title: DCZia 2025
  accessed: '2026-09-07'
  note: Confirms DCZia is an Albuquerque, NM based electronics/badge-making community that runs its own convention, ZiaCon, first held in 2019.
  archived: https://web.archive.org/web/20260514004509/https://dczia.net/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No dedicated event entry exists for ZiaCon in _data/events.yml, so event is left as "other"; the con is DCZia's own ZiaCon 2 (Albuquerque, NM, 2021). Price, quantity made, and distribution/availability are not stated anywhere found (this reads as a one-off live-build demo rather than a badge produced in quantity for distribution) and are left empty. No maker photo shows the badge worn or lit up; the two saved images are a CAD-style front render and a bare assembled-board photo from the repo.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/dczia-yolobadge-ziacon-2.glb
  method: kicad
  source_file: Hardware/yolo-badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 188520
---

DCZia's yolobadge began as a stunt: during a talk at ZiaCon 2 in April 2021, the group designed and built a complete electronic badge live on stage in about four hours. Badge layout came from hamster, with design input from jediguybob, lithochasm, and DCZia, artwork from LunaSylumDancer, and the framing challenge from Syntax. ZiaCon is DCZia's own convention, run by the Albuquerque, New Mexico badge-making community rather than by DEF CON, though it took place the same year as DEF CON 29's hybrid/remote edition.

The board itself is simple and hacker-friendly: an ATmega32U4 microcontroller running an Arduino sketch, ten WS2812B ("Neopixel") addressable LEDs driven with the FastLED library, micro-USB for power, a serial breakout, and a 4-pin SAO port so it could host other badges' add-ons. Both the KiCad hardware design and the Arduino firmware are published in the GitHub repository, making the whole thing open source.

No pricing, production quantity, or distribution details were found; nothing in the repo or DCZia's own site suggests it was sold or handed out beyond the talk where it was made, so it reads as a one-off live-build demonstration rather than a badge produced for wider distribution.
