---
title: DC540 Tree of Life Badge (Kabbalah)
id: dc29-tree-of-life-badge-dc540
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc29
year: 2021
makers:
- name: DC540 Defcon Group
  url: https://dc540.org
summary: A two-board "sandwich" badge from the DC540 Defcon Group for DEF CON 29, themed around the Kabbalistic Tree of Life, with an OLED display, 32 RGB LEDs, and open firmware.
functions: Stock firmware runs a demo, unlockable challenge "levels" tied to the Kabbalah tree-of-life sephirot, and a guided breathing exercise. The board is an open platform meant to be reflashed with custom C, MicroPython, or CircuitPython code.
look:
  colors:
  - black
  - multicolor
  shape: null
  themes:
  - puzzle
  - ctf
  - jewelry
tech:
  mcu: RP2040 (Raspberry Pi Pico, surface-mounted via castellated edges)
  leds:
    count: 32
    type: RGB
    note: ''
  display: 0.96" OLED (SSD1306)
  connectivity: []
  inputs:
  - buttons
  battery: 2x AA
  sao_version: null
get_one:
  price: $65
  price_usd: 65
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing showed sold out / seller "on a break" as of the page checked 2026-09-07; sold via preorder around DEF CON 29 (2021).
  distribution:
  - preorder
  - purchase
  where: Sold via Shopify preorder and in person at DEF CON 29; also listed on Tindie by DC540 Nova. Included the assembled badge, a battery holder with two AA batteries, and a custom lanyard.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/DC540-Nova/DC29-Tree-of-Life-Badge
  firmware_url: https://github.com/DC540-Nova/DC29-Tree-of-Life-Badge
  gerbers_url: null
  eda_tool: null
  license: MIT
  fab_url: null
  notes: Repo has pinout documentation and the stock .uf2 firmware (tolb_0.1.0.uf2); the maker explicitly declined to publish Gerbers ("Not on your life").
links:
- label: github.com/DC540-Nova/DC29-Tree-of-Life-Badge
  url: https://github.com/DC540-Nova/DC29-Tree-of-Life-Badge
  kind: repo
- label: DC540 Tree of Life Badge for DC29 (dc540.org)
  url: https://dc540.org/xxx/2021/07/dc540-tree-of-life-badge-for-dc29/
  kind: article
- label: Tree of Life Badge documentation released (dc540.org)
  url: https://dc540.org/xxx/2021/08/tree-of-life-badge-documentation-released/
  kind: article
- label: DC540 Kabbalah (Tree of Life) Badge for DC29 (Tindie)
  url: https://www.tindie.com/products/dc540_nova/dc540-kabbalah-tree-of-life-badge-for-dc29/
  kind: store
  archived: https://web.archive.org/web/20260503102450/https://www.tindie.com/products/dc540_nova/dc540-kabbalah-tree-of-life-badge-for-dc29/
- label: DC540's Tree of Life badge for DC29 (DEF CON Forums)
  url: https://forum.defcon.org/node/238102
  kind: article
images:
- file: assets/images/badges/dc29/tree-of-life-badge-dc540/37b91ea8c7.jpg
  source: https://dc540.org/xxx/2021/07/dc540-tree-of-life-badge-for-dc29/
  credit: DC540 Defcon Group
  caption: The assembled Tree of Life badge showing the two-board sandwich, OLED display, and RGB LEDs
- file: assets/images/badges/dc29/tree-of-life-badge-dc540/e217a80695.jpg
  source: https://www.tindie.com/products/dc540_nova/dc540-kabbalah-tree-of-life-badge-for-dc29/
  credit: DC540 Nova (Tindie)
  caption: Tree of Life badge product photo lit up with RGB LEDs
  archived: https://web.archive.org/web/20260503102450/https://www.tindie.com/products/dc540_nova/dc540-kabbalah-tree-of-life-badge-for-dc29/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/DC540-Nova/DC29-Tree-of-Life-Badge
  title: DC29-Tree-of-Life-Badge (DC540)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 29''.'
- kind: url
  url: https://dc540.org/xxx/2021/07/dc540-tree-of-life-badge-for-dc29/
  title: DC540 Tree of Life Badge for DC29 - DC540 Defcon Group
  accessed: '2026-09-07'
  note: 'Maker announcement post: design, MCU, LEDs, display, distribution, images.'
- kind: url
  url: https://dc540.org/xxx/2021/08/tree-of-life-badge-documentation-released/
  title: Tree of Life Badge documentation released - DC540 Defcon Group
  accessed: '2026-09-07'
  note: Follow-up post referenced when searching; confirms public documentation/firmware release.
- kind: url
  url: https://www.tindie.com/products/dc540_nova/dc540-kabbalah-tree-of-life-badge-for-dc29/
  title: DC540 Kabbalah (Tree of Life) badge for DC29 - Tindie
  accessed: '2026-09-07'
  note: Price ($65), sold-out/on-break status, feature list, product photo.
  archived: https://web.archive.org/web/20260503102450/https://www.tindie.com/products/dc540_nova/dc540-kabbalah-tree-of-life-badge-for-dc29/
- kind: url
  url: https://forum.defcon.org/node/238102
  title: DC540's Tree of Life badge for DC29 - DEF CON Forums
  accessed: '2026-09-07'
  note: Surfaced in search results as community discussion of the badge; not separately fetched for content.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Quantity made was not disclosed in any source found. Gerbers/hardware design files were explicitly not published by the maker, so make_your_own.open_source is "partial" (firmware/pinout docs only). NRF24L01+ wireless transceiver was mentioned in maker posts and the GitHub repo pinouts but not consistently listed as a working/shipped feature (one source noted lower confidence in its functionality), so it was left out of tech.connectivity rather than guessed at; noted here instead.
last_modified_date: '2026-09-07'
---

The DC540 Tree of Life Badge was DC540 Defcon Group's entry for DEF CON 29 (2021), built as a two-board "sandwich" PCB held together with standoffs and connectors. It runs on a Raspberry Pi Pico (RP2040) soldered directly to the board via castellated edges, with 32 RGB LEDs on the lower board and a small OLED display on the top board. The design draws its name and visual theme from the Kabbalistic Tree of Life, with stock firmware offering unlockable challenge "levels" tied to the ten sephirot, a demo light show, and a guided breathing exercise.

Badges were sold as fully-assembled units through a Shopify preorder campaign ahead of the con, in person at DEF CON 29, and afterward via a Tindie listing at $65, which included a two-AA battery holder and a custom lanyard. As an "open platform" badge, DC540 published pinout documentation and the stock .uf2 firmware image to a public GitHub repo so owners could reflash it with their own C, MicroPython, or CircuitPython code; the maker declined to release the board's Gerber files.

An NRF24L01+ wireless transceiver was included in the design and documented in the repo's pinouts, though maker commentary suggests its functionality at launch was less certain than the rest of the board. No public source found states how many units were produced.
