---
title: Cowboy SAO
id: other-cowboy-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2024
makers:
- name: 'Alee (Tindie: alee97422)'
  url: https://www.tindie.com/stores/alee97422/
summary: 'A small cowboy-themed SAO with clear "eyes" that red LEDs light from behind, built around an ATtiny412.'
functions: 'The two eye cutouts glow via red LEDs mounted on the back of the board and shining through the front.'
look:
  colors: []
  shape: cowboy
  themes:
  - cowboy
tech:
  mcu: ATtiny412
  leds:
    count: 2
    type: reverse-mount
    note: Red LEDs mounted on the back of the board shine through the front to light the cowboy's eyes.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $10.99
  price_usd: 10.99
  quantity: ''
  availability: sold_out
  availability_note: 'Listed on Tindie mid-2024; marked "Sold out since Jul 03, 2024" as of a December 2024 archive snapshot.'
  distribution:
  - purchase
  where: Sold directly through the maker's Tindie store (@alee97422).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/alee97422/cowboy-sao
  url: https://www.tindie.com/products/alee97422/cowboy-sao/
  kind: store
images:
- file: assets/images/badges/other/cowboy-sao/2e00b354d2.jpg
  source: "https://www.tindie.com/products/alee97422/cowboy-sao/"
  credit: "Alee (alee97422)"
  caption: "Front of the Cowboy SAO"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/alee97422/cowboy-sao/
  title: Cowboy SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''not on any sheet; sold on Tindie late 2024''.'
- kind: url
  url: http://web.archive.org/web/2024/https://www.tindie.com/products/alee97422/cowboy-sao/
  title: 'COWBOY SAO from @alee97422 on Tindie (Wayback Machine snapshot, Dec 2024)'
  accessed: '2026-09-07'
  note: 'Live tindie.com is behind Cloudflare and blocked automated fetches; used an archive.org snapshot to read the full description, price ($10.99), MCU (ATtiny412), UPDI-on-SAO-connector detail, and sold-out status/date. Also used to recover a product photo.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >
    Confirmed from the maker's own Tindie listing (via an archived snapshot; the live page is
    behind Cloudflare and blocks automated fetches). The badge breaks out the UPDI programming
    interface to the SAO connector instead of I2C, per the maker's description. No source ties it
    to a specific convention or year of use -- it appears to have been a general Tindie-store
    release, listed around June 2024 and marked sold out since July 3, 2024. The same maker
    (Alee/alee97422) is credited elsewhere in this archive with several DEF CON-specific badges
    (dc32-tpb-badge, dc33-crab, dc34-breadbadge), but nothing found here connects Cowboy SAO to
    any of those. Quantity made, PCB color, hardware/firmware files, and SAO connector version
    (v1 vs v1.69bis) were not stated and are left blank.
last_modified_date: '2026-09-07'
---

Cowboy SAO is a small shameless-add-on badge by the Tindie maker Alee (store handle alee97422): a cowboy-shaped board whose eyes are cut through to clear windows, lit from behind by two red LEDs mounted on the back of the board. The front stays clean because all the components -- including the ATtiny412 microcontroller that drives it -- are surface-mounted on the reverse side. Unusually for an SAO, it wires the ATtiny's UPDI programming/debug interface out to the SAO connector rather than the more common I2C bus, which the maker calls out specifically in the listing.

It sold for $10.99 through the maker's own Tindie store and shows as sold out since July 3, 2024, based on a December 2024 archive of the listing (the live Tindie page is now behind a Cloudflare challenge that blocks automated fetches). No convention, year, or event is named in the listing itself, so it reads as a standalone store release rather than a badge made for a specific con -- despite the same maker's other credits in this archive being DEF CON-specific (dc32-tpb-badge, dc33-crab, dc34-breadbadge).

