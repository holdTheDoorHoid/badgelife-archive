---
title: 30-in-One Badge (DCZia YOLO Badge)
id: dc30-30-in-1-badge-dczia-yolo-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc30
year: 2022
makers:
- name: DCZia
  url: https://dczia.net
summary: A "learn electronics" kit on a single PCB, built and sold as a wearable badge for DEF CON 30. Duplicate of this archive's dc30-30-in-1-badge entry.
functions: End users solder up to 30 different described circuits onto one board (OLED display, RGB LED, speaker, switches, potentiometer, transformer), using it as a jumping-off point to explore analog electronics; ships with a printed instruction booklet and a wooden box that doubles as a soldering jig.
look:
  colors: []
  shape: rectangle
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 1
    type: RGB
    note: Single RGB LED among the 30 circuits; no microcontroller is used (a passive/analog electronics kit).
  display: 0.96" OLED
  connectivity: []
  battery: not specified (has a battery case)
  sao_version: none
get_one:
  price: $100
  price_usd: 100.0
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing shows "Out of Stock" as of 2026-09-07.
  distribution:
  - purchase
  where: Sold via Tindie (seller "hamster" / snurkle engineering).
make_your_own:
  open_source: true
  hardware_url: https://github.com/dczia/thirtyinone
  firmware_url: null
  eda_tool: null
  license: Unlicense
links:
- label: www.hackster.io/news/dczia-s-30-in-one-badge-built-for-def-con-30-is-a-throwback-to-classic-educational-circuit-kits-f2f204d7aafe
  url: https://www.hackster.io/news/dczia-s-30-in-one-badge-built-for-def-con-30-is-a-throwback-to-classic-educational-circuit-kits-f2f204d7aafe
  kind: article
- label: dczia/thirtyinone (GitHub)
  url: https://github.com/dczia/thirtyinone
  kind: repo
- label: DC Zia 30-in-One Badge (Hackaday.io)
  url: https://hackaday.io/project/188464-dc-zia-30-in-one-badge
  kind: hackaday
- label: DCZia '30-in-One' defcon 30 Badge (Tindie)
  url: https://www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge/
  kind: store
images:
- file: assets/images/badges/dc30/30-in-1-badge-dczia-yolo-badge/7b907fc96e.jpg
  source: https://www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge/
  credit: DCZia / snurkle engineering (Tindie)
  caption: Assembled DCZia 30-in-One badge kit
- file: assets/images/badges/dc30/30-in-1-badge-dczia-yolo-badge/95f9347c2b.jpg
  source: https://hackaday.io/project/188464-dc-zia-30-in-one-badge
  credit: DCZia
  caption: DCZia 30-in-One badge circuit board detail
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.hackster.io/news/dczia-s-30-in-one-badge-built-for-def-con-30-is-a-throwback-to-classic-educational-circuit-kits-f2f204d7aafe
  title: 30-in-1 Badge (DCZia YOLO Badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc30''. hackster.io itself returned a Cloudflare 403 on direct fetch; content summarized via web search snippet only.'
- kind: url
  url: https://github.com/dczia/thirtyinone
  title: dczia/thirtyinone - GitHub
  accessed: '2026-09-07'
  note: Confirms Hardware/Software folders, Unlicense, booklet, component list (OLED, RGB LED, speaker, switches, battery case, transformer, key switch/cap).
- kind: url
  url: https://hackaday.io/project/188464-dc-zia-30-in-one-badge
  title: DC Zia 30-in-One Badge - Hackaday.io
  accessed: '2026-09-07'
  note: Maker background, OSHWA certification mention, component list, DEF CON 30 / 2022 context.
- kind: url
  url: https://www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge/
  title: DCZia '30-in-One' defcon 30 Badge - Tindie
  accessed: '2026-09-07'
  note: Price ($100), out-of-stock status, description, product photo used for images.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: This entry is a duplicate of the archive's existing, more fully researched dc30-30-in-1-badge entry (title "30-in-One Badge"), which covers the same DCZia DEF CON 30 kit sold via Tindie seller snurkle engineering. That entry is OSHWA-certified (US002134) and already merged one prior duplicate. No microcontroller is used in this kit despite a web-search summary claiming an ATSAMD21 MCU - the maker's own GitHub repo, Hackaday.io project, and OSHWA record all describe it as a passive/analog electronics teaching board (one RGB LED, OLED display, speaker, and discrete components), consistent with the canonical entry. Quantity made is not stated in any source found.
last_modified_date: '2026-09-07'
---

The 30-in-One Badge is a "learn electronics" kit built by DCZia and sold as a badge for DEF CON 30 (2022) through Tindie under seller "snurkle engineering." Rather than running firmware on a microcontroller, it is a single PCB carrying 30 separate analog circuit projects — an OLED screen, an RGB LED, a speaker, switches, a potentiometer, and a transformer among them — that the owner solders together themselves, following a printed instruction booklet. A wooden box doubles as a soldering jig, and the board reportedly hides some challenges/puzzles for people who go looking. It sold for $100 and has since gone out of stock on Tindie.

The project is fully open source under the Unlicense, with hardware and software design files and the booklet available in DCZia's `thirtyinone` GitHub repository, and it holds an OSHWA certification (US002134).

This entry duplicates the archive's existing `dc30-30-in-1-badge` entry for the same item; see that entry for the canonical, more fully sourced record.
