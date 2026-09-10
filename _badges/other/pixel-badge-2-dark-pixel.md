---
title: 'Pixel Badge 2: Dark Pixel'
id: other-pixel-badge-2-dark-pixel
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2019
makers:
- name: blinkingthing
  url: https://hackaday.io/blinkingthing
summary: A hobbyist electronic conference badge shaped like an oversized WS2812 LED, with bent brass tubes standing in for the chip's bond wires.
functions: User-controlled animation sequencer for the onboard LEDs; can switch between its own generated LED data and an external neopixel data source, and can output data to daisy-chain additional badges. The bent brass "bond wire" tubes double as touch inputs.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
  - minimalist
tech:
  mcu: ESP32 WROOM
  leds:
    type: WS2812S
    note: Badge PCB itself is shaped like an oversized WS2812/WS2812S LED package.
  display: none
  connectivity: []
  battery: LiPo (rechargeable, USB charging)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Not sold; a small hobby build (at least 5 v2.2 boards were assembled by the maker).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/167841-pixel-badge-2-dark-pixel
  url: https://hackaday.io/project/167841-pixel-badge-2-dark-pixel
  kind: hackaday
  archived: https://web.archive.org/web/20251205151434/https://hackaday.io/project/167841-pixel-badge-2-dark-pixel
- label: Pixel Badge (Shitty Pixel) - predecessor project
  url: https://hackaday.io/project/164567-pixel-badge-shitty-pixel
  kind: hackaday
  archived: https://web.archive.org/web/20260606083243/https://hackaday.io/project/164567-pixel-badge-shitty-pixel
- label: Notes on the Brass Tube "Bond Wires"
  url: https://hackaday.io/project/167841-pixel-badge-2-dark-pixel/log/169659-notes-on-the-brass-tube-bond-wires
  kind: doc
images:
- file: assets/images/badges/other/pixel-badge-2-dark-pixel/e5be1cba6e.jpg
  source: https://hackaday.io/project/167841-pixel-badge-2-dark-pixel
  credit: blinkingthing
  caption: 'Pixel Badge 2: Dark Pixel, shaped like an oversized WS2812 LED with brass tube ''bond wires'''
  archived: https://web.archive.org/web/20251205151434/https://hackaday.io/project/167841-pixel-badge-2-dark-pixel
- file: assets/images/badges/other/pixel-badge-2-dark-pixel/1ecf21550b.jpg
  source: https://hackaday.io/project/167841-pixel-badge-2-dark-pixel
  credit: blinkingthing
  caption: Dark Pixel badge detail shot
  archived: https://web.archive.org/web/20251205151434/https://hackaday.io/project/167841-pixel-badge-2-dark-pixel
contact: {}
notes:
- Sources do not name a specific conference this badge was made for or brought to; it reads as an ongoing personal hobby project rather than a badge tied to one event's badgelife scene.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/167841-pixel-badge-2-dark-pixel
  title: 'Pixel Badge 2: Dark Pixel'
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
  archived: https://web.archive.org/web/20251205151434/https://hackaday.io/project/167841-pixel-badge-2-dark-pixel
- kind: url
  url: https://hackaday.io/project/167841-pixel-badge-2-dark-pixel
  title: 'Pixel Badge 2: Dark Pixel'
  accessed: '2026-09-07'
  note: 'Main project page: description, features (ESP32 WROOM, WS2812S LEDs, CP2102, AP2112, MCP73831 LiPo charger), KiCad PCB iterations (v1 cardboard prototype through v2.2), at least 5 v2.2 units assembled, started Sept 30 2019.'
  archived: https://web.archive.org/web/20251205151434/https://hackaday.io/project/167841-pixel-badge-2-dark-pixel
- kind: url
  url: https://hackaday.io/project/167841-pixel-badge-2-dark-pixel/log/169659-notes-on-the-brass-tube-bond-wires
  title: Notes on the Brass Tube "Bond Wires"
  accessed: '2026-09-07'
  note: Confirms brass K&S tube construction as touch-input "bond wires"; no event, price, or quantity info here.
- kind: url
  url: https://hackaday.io/project/164567-pixel-badge-shitty-pixel
  title: Pixel Badge (Shitty Pixel)
  accessed: '2026-09-07'
  note: Predecessor SAO project by the same maker (blinkingthing); Dark Pixel is explicitly a continuation of this design, inspired by Mohit Bhoite's freeform brass-sculpture electronics.
  archived: https://web.archive.org/web/20260606083243/https://hackaday.io/project/164567-pixel-badge-shitty-pixel
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all three cited pages and confirmed every populated field and body sentence -- maker, ESP32 WROOM/WS2812S/CP2102/AP2112/MCP73831 parts, KiCad design, USB-charged LiPo, brass K&S tube "bond wire" touch inputs, daisy-chain/external-data functions, ~5 v2.2 units built in 2019, and the explicit "continuation" of the "Shitty Pixel" SAO with Mohit Bhoite brass-sculpture inspiration. Note: the Dark Pixel project page does mention "Defcon 27," but only as the con the maker had already attended (with the earlier Shitty Pixel SAO) when they decided to keep developing the idea into this badge -- it does not tie Dark Pixel itself to that or any other convention, so event=other and the absence of a con tie remains correct. No specific conference/event, price, or public distribution were found beyond that. Not sold as a product; appears to be a one-off/small-batch hobby build (~5 boards of the final revision). Both images confirmed present on disk and
    depicting this badge on its source page.'
last_modified_date: '2026-09-07'
---

Pixel Badge 2: Dark Pixel is a hobbyist electronic conference badge by Hackaday.io user blinkingthing, built around WorldSemi WS2812S addressable LEDs. The badge's own PCB is shaped like an oversized WS2812 LED package, with bent brass tubes standing in for the four bond wires of the real chip — a nod to Mohit Bhoite's freeform brass-sculpture electronics. The brass tubes double as touch inputs. It runs on an ESP32 WROOM module with a CP2102 USB-UART bridge, AP2112 regulator, and MCP73831 LiPo charge controller, and can generate its own LED animation sequences, accept an external neopixel data feed, or pass data on to daisy-chained badges.

The project is a direct sequel to the maker's earlier "Shitty Pixel" SAO (also on Hackaday.io), scaled up into a full standalone badge. Development ran through KiCad-designed PCB revisions — from a cardboard v1 mockup to v2.1 and v2.2 boards — with at least five v2.2 units assembled by the maker in late 2019. No sources tie the badge to a specific convention or year of use, and there is no evidence it was sold or distributed beyond the maker's own builds; it reads as a documented hobby project rather than a badgelife-scene release for a particular con.
