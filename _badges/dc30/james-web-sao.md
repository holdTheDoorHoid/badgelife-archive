---
title: James Webb SAO
id: dc30-james-web-sao
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: sqearlsalazar
  url: https://www.tindie.com/stores/sqearlsalazar/
summary: A small SAO honoring the James Webb Space Telescope, sold as one half of a two-piece "Telescope SAOs" pack alongside a matching Hubble SAO.
functions: Lights a single onboard LED when powered through a host badge's SAO header; no other interactivity.
look:
  colors:
  - black
  shape: null
  themes:
  - space
  - sci-fi
tech:
  mcu: none
  leds:
    count: 1
    type: null
    note: Single red LED with resistor.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: $10
  price_usd: 10.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  - village
  where: Hardware Hacking Village at DEF CON; also sold as a pair with the Hubble SAO on the maker's Tindie store
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/sqearlsalazar/telescope-saos-hubble-james-webb
  url: https://www.tindie.com/products/sqearlsalazar/telescope-saos-hubble-james-webb/
  kind: store
  archived: https://web.archive.org/web/20260503112957/https://www.tindie.com/products/sqearlsalazar/telescope-saos-hubble-james-webb/
images:
- file: assets/images/badges/dc30/james-web-sao/f38821354a.jpg
  source: https://www.tindie.com/products/sqearlsalazar/telescope-saos-hubble-james-webb/
  credit: sqearlsalazar
  caption: Hubble and James Webb telescope SAO pair, assembled with LEDs lit
  archived: https://web.archive.org/web/20260503112957/https://www.tindie.com/products/sqearlsalazar/telescope-saos-hubble-james-webb/
- file: assets/images/badges/dc30/james-web-sao/46b3f6b1be.jpg
  source: https://www.tindie.com/products/sqearlsalazar/telescope-saos-hubble-james-webb/
  credit: sqearlsalazar
  caption: Telescope SAO pair, alternate angle
  archived: https://web.archive.org/web/20260503112957/https://www.tindie.com/products/sqearlsalazar/telescope-saos-hubble-james-webb/
contact: {}
notes:
- Sheet title was 'James Web SAO' (typo for 'James Webb'); corrected here. Sheet also read 'D3FC0N', corrected to DEF CON.
status: listed
sources:
- kind: sheet
  event: dc30
  row: 54
  updated: '2022-07-28'
- kind: url
  url: https://www.tindie.com/products/sqearlsalazar/telescope-saos-hubble-james-webb/
  title: Telescope SAOs - Hubble & James Webb by sqearlsalazar
  accessed: '2026-09-07'
  note: 'Maker''s Tindie listing: describes the pack as two pre-assembled SAO PCBs (Hubble with 4x yellow reverse-gullwing LEDs, James Webb with 1x red LED), each with a 2x3 male SAO header for use with a compatible badge or external 2x3 power supply. Listed price for the pair is $20; product photos are dated November 2019.'
  archived: https://web.archive.org/web/20260503112957/https://www.tindie.com/products/sqearlsalazar/telescope-saos-hubble-james-webb/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Only source found is the maker's own Tindie storefront, which sells the James Webb SAO bundled with a matching Hubble SAO for $20/pair — not as a standalone $10 item as the community sheet listed it. It's unclear whether sqearlsalazar also sold the James Webb SAO separately at DEF CON 30's Hardware Hacking Village for $10, or whether the sheet price reflects a per-unit share of the pair; left get_one.price as the sheet stated it since no separate listing was found. The Tindie product photos are dated November 2019, suggesting this SAO was originally made for DEF CON 27 and continued to be sold at HHV in later years including DC30; kept event as dc30 per the sheet entry. No hardware files, firmware, MCU details (the board appears passive, LED-only), or a Hackaday.io / GitHub presence for the maker were found. A web search engine (DuckDuckGo) returned no usable results during this pass; only the Tindie page and a Hackaday.io search (login wall, no results) were reachable.
last_modified_date: '2026-09-07'
---

The James Webb SAO is a small, passive add-on board that plugs into a DEF CON badge's SAO header and lights a single red LED, made by the badgelife maker sqearlsalazar. It was sold as one half of a "Telescope SAOs" two-pack alongside a companion Hubble Space Telescope SAO (four yellow reverse-gullwing LEDs), both simple space-themed novelty boards aimed at "space & science fans" in the #badgelife community. The maker's Tindie listing, whose photos date to November 2019, prices the pair at $20; the community sheet for DEF CON 30 lists the James Webb piece alone at $10, which may reflect a separate per-unit sale at the Hardware Hacking Village rather than the bundled Tindie price.

No schematic, firmware, or design files were found, and the board does not appear to carry a microcontroller — it is a straightforward LED-and-resistor SAO powered entirely by the host badge. No independent press coverage, Hackaday.io project, or GitHub repository for the maker turned up in this pass.
