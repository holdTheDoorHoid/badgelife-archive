---
title: Baphomet SAO
id: dc30-baphomet-sao
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: Sqearlsalazar
  url: https://www.tindie.com/stores/sqearlsalazar/
summary: A goat-headed "Satanic Goat" SAO from sqearlsalazar's Baphomet/HailSatan line, an SMD-LED add-on for a SAO-equipped DEF CON badge.
functions: Lights up its red LEDs when powered by a host badge's SAO header; pairs with the maker's companion HailSatan SAO for a two-part "#hailsatan" info challenge.
look:
  colors:
  - red
  shape: null
  themes:
  - horror
tech:
  mcu: none
  leds:
    count: 8
    type: 0805 red SMD
    note: 9x 0805 red SMD LED pads, 1 unused
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: $20
  price_usd: 20.0
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing showed "Sold out since Jun 15, 2020" as of the most recent archived snapshot (2021-09-23); no listing found still active as of 2026-09-07.
  distribution:
  - purchase
  where: Sold by sqearlsalazar on Tindie; the sheet entry lists it as distributed at the Hardware Hacking Village at DEF CON.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/sqearlsalazar/baphomet-defcon-sao
  url: https://www.tindie.com/products/sqearlsalazar/baphomet-defcon-sao/
  kind: store
- label: sqearlsalazar's Tindie store
  url: https://www.tindie.com/stores/sqearlsalazar/
  kind: store
  archived: https://web.archive.org/web/20260503113838/https://www.tindie.com/stores/sqearlsalazar/
images: []
contact: {}
notes:
- The Tindie product description refers to the item as the "Satanic Goat SAO"; "Baphomet Defcon SAO" is the listing title.
status: listed
sources:
- kind: sheet
  event: dc30
  row: 56
  updated: '2022-07-28'
- kind: url
  url: http://web.archive.org/web/20210923022751/https://www.tindie.com/products/sqearlsalazar/baphomet-defcon-sao/
  title: Baphomet Defcon SAO from sqearlsalazar on Tindie (Wayback Machine snapshot, 2021-09-23)
  accessed: '2026-09-07'
  note: Product description, price ($15.00 at time of snapshot), LED/component count, SAO connector type, and sold-out status
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: |
    The live Tindie listing returns a Cloudflare challenge page for automated fetches and could not be read directly.
    The only Wayback Machine snapshot of this product page (2021-09-23) shows it listed at $15.00 and "Sold out since Jun 15, 2020" -
    this predates the DC30 (2022) sheet entry, which lists a price of $20. It is unclear whether the maker relisted/restocked
    it for DEF CON 30 at a higher price or whether the sheet price is otherwise inaccurate; kept the sheet's $20 as the recorded
    price and noted the discrepancy here rather than guessing. No maker Hackaday.io project, GitHub repo, or press coverage was
    found for this specific SAO. Quantity made, open-source status, and product photos could not be confirmed - no image
    snapshots of the product photos exist in the Wayback Machine, so no images were saved. web search was unavailable for this task
    (session search budget exhausted), so coverage relied on the archived Tindie page and direct fetch attempts only.
last_modified_date: '2026-09-07'
related:
- dc30-hailsatan-sao-s
- dc30-devil-trap
---

The Baphomet SAO is a small horror-themed shameless-plug add-on made by sqearlsalazar, sold on Tindie as the "Baphomet Defcon SAO" but described in the listing itself as the "Satanic Goat SAO." It is a bare PCB, roughly 3" x 2.25", populated with nine 0805 red SMD LEDs (one pad left unused), four SMD resistors, and a 2x3 DEF CON-style SAO connector; it has no microcontroller and draws power entirely from the host badge.

The listing ties it to a companion piece, the HailSatan SAO, describing a "#hailsatan" challenge that required information from both SAOs together - a small collectible puzzle rather than a standalone gadget. The only surviving copy of the product page, a Wayback Machine snapshot from September 2021, shows it priced at $15.00 and marked sold out since June 2020, which predates the $20 price recorded on the DEF CON 30 community sheet; it isn't clear from available sources whether the item was restocked for DC30 or whether the sheet price reflects a different batch or a markup at the con itself.

No hardware files, firmware, or maker write-up beyond the Tindie listing were found, so open-source status and build details are left unconfirmed.
