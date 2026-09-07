---
title: Yo Dawg SAOAO baseplate/standard
id: other-yo-dawg-saoao-baseplate-standard
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: davedarko
summary: ''
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
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
- label: github.com/davedarko/YoDawgSAO/tree/main/StandardSAOAO
  url: https://github.com/davedarko/YoDawgSAO/tree/main/StandardSAOAO
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: not_an_item
sources:
- kind: url
  url: https://github.com/davedarko/YoDawgSAO/tree/main/StandardSAOAO
  title: Yo Dawg SAOAO baseplate/standard
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''supercon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/davedarko/YoDawgSAO/main/README.md
  title: 'YoDawgSAO README: "Yo Dawg, I heard you like add-ons on your badges?"'
  accessed: '2026-09-07'
  note: Confirms this repo is a connector/footprint standard for tiny "add-ons on add-ons" (SAOAOs) made for the Hackaday Supercon 2024 add-on contest, not a specific physical badge or SAO product.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    This is not a distinct badge or SAO product. "YoDawgSAO" by davedarko is a meme-titled
    repo ("Yo Dawg, I heard you like add-ons on your badges?") published around the Hackaday
    Supercon 2024 (Supercon 8) add-on contest, proposing a tiny secondary connector standard
    -- a "SAO Add-On" (SAOAO) -- for slapping small extras (blinky LEDs, in-jokes) onto a
    full SAO/add-on board without it having to be contest-worthy itself. The `StandardSAOAO`
    folder the entry links to contains only `SAOAO.pretty`, a KiCad footprint library
    defining the mechanical/electrical standard: a 19mm x 19mm footprint limit and a
    1.27mm-pitch GND-VCC-GND pin header. No physical board, price, quantity, or
    availability is described anywhere in the repo -- it is a design spec/tool for other
    makers to build SAOAOs against, not an item itself. No maker-published photo of an
    actual populated board was found, only a KiCad render of the footprint/baseplate.
    Recommend closing this entry as not an item; if davedarko or others release an actual
    SAOAO board using this standard, that board would deserve its own entry.
last_modified_date: '2026-09-07'
---

This entry pointed at a GitHub repo, `YoDawgSAO`, rather than a physical badge or SAO. The repo's README ("Yo Dawg, I heard you like add-ons on your badges?") explains that around the Hackaday Supercon 2024 add-on contest, maker davedarko wanted a lightweight way to slap small extras -- a meme, a couple of blinking LEDs -- onto a full SAO/add-on board without it needing to be a contest-grade design in its own right. The proposed fix is a tiny secondary connector standard for these "add-ons on add-ons," which the repo calls a SAOAO.

The `StandardSAOAO` folder referenced by this entry contains only `SAOAO.pretty`, a KiCad footprint library defining that standard: boards are constrained to 19mm x 19mm and connect over a 1.27mm-pitch GND-VCC-GND pin header (a header size the author admits is a pain to solder, but which stuck as the de facto standard anyway). The repo includes a KiCad render of this footprint, but no build of an actual populated board, no price or quantity, and no storefront or distribution information -- because it is a connector spec/tool for other designers to build against, not a product.

No physical "Yo Dawg SAOAO baseplate/standard" badge or SAO exists to catalog here. If a specific SAOAO board using this standard is later released (by davedarko or anyone else), that board should get its own archive entry distinct from this spec repo.
