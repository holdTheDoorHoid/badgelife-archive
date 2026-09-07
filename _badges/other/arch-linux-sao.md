---
title: Arch Linux SAO
id: other-arch-linux-sao
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
summary: 'A tie-dye Arch Linux logo SAO with two LEDs, sold individually on Tindie rather than distributed at a specific event.'
functions: 'Lights two onboard LEDs when powered through the host badge''s SAO header; purely decorative, no other interaction.'
look:
  colors: [multicolor]
  shape: logo
  themes: [logo, retro computer]
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Two LEDs with current-limiting resistors, no microcontroller.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: "$10.99"
  price_usd: 10.99
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold individually on Tindie by @alee97422; listed in stock as of a June 2024 snapshot, current availability not re-checked live (Tindie blocked automated access at time of research).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/alee97422/arch-linux-sao
  url: https://www.tindie.com/products/alee97422/arch-linux-sao/
  kind: store
- label: alee97422 on Tindie
  url: https://www.tindie.com/stores/alee97422/
  kind: store
images:
  - file: assets/images/badges/other/arch-linux-sao/c44bd92571.jpg
    source: "https://www.tindie.com/products/alee97422/arch-linux-sao/"
    credit: "Alee (alee97422)"
    caption: "Arch Linux SAO, front view"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- Sold as a standalone add-on, not tied to any specific convention or year in the listing; year and event could not be confirmed beyond the June 2024 Tindie listing date.
- The same maker (Alee / alee97422) also made the DEF CON 32 "TPB Badge", DEF CON 33 "cRab", and DEF CON 34 "Breadbadge" entries already in this archive, but nothing on the Arch Linux SAO's own listing ties it to any of those events.
status: listed
sources:
- kind: url
  url: https://www.tindie.com/products/alee97422/arch-linux-sao/
  title: Arch Linux SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''not on any sheet; sold individually on Tindie mid-2024''.'
- kind: url
  url: http://web.archive.org/web/20240615145358/https://www.tindie.com/products/alee97422/arch-linux-sao/
  title: Arch Linux SAO from @alee97422 on Tindie (Wayback snapshot, 2024-06-15)
  accessed: '2026-09-07'
  note: 'Live Tindie page returned a Cloudflare challenge to automated fetches; used the Wayback Machine snapshot instead. Provided price ($10.99), product description, LED/resistor details, SAO-standard claim, in-stock status as of the snapshot date, and product photos.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Live Tindie listing is behind a Cloudflare bot check and could not be fetched directly; all confirmed detail comes from a June 2024 Wayback Machine snapshot of the same page, plus AI-summarized web search results that largely corroborate it. Could not confirm current (2026) availability, quantity made, PCB dimensions, or whether it was ever sold at a physical event table versus online only. No maker bio page or social profile beyond the Tindie store was found.'
last_modified_date: '2026-09-07'
---

The Arch Linux SAO is a small "Simple Add-On" shaped like the Arch Linux logo, sold individually on Tindie by the maker known as Alee (Tindie handle alee97422), who also made several DEF CON badges already catalogued in this archive (the DC32 TPB Badge, DC33 cRab, and DC34 Breadbadge). Unlike those, the Arch Linux SAO's own listing does not tie it to a particular convention; it appears to have been an ongoing Tindie storefront item rather than an event giveaway or badge-table sale.

The board is a minimalist, tie-dye-colored rendition of the Arch Linux logo carrying two LEDs and their current-limiting resistors, with no onboard microcontroller. It follows the SAO standard, drawing power and ground from a host badge's SAO header so the LEDs light up when plugged in. A Wayback Machine snapshot from June 2024 shows it listed in stock at $10.99 with free shipping; the live Tindie page could not be re-checked directly during this research pass because it returned a Cloudflare bot challenge, so current stock status, total quantity made, and exact board dimensions remain unconfirmed.
