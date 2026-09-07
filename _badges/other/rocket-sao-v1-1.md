---
title: Rocket SAO v1.1
id: other-rocket-sao-v1-1
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: 'Alee (Tindie: alee97422)'
summary: 'A revamped SAO shaped as a rocket, hand-soldered with 3 reverse-mounted NeoPixels for dynamic lighting, sold on Tindie in red, blue, and purple PCB colors.'
functions: Dynamic lighting effects from 3 reverse-mounted NeoPixels.
look:
  colors: [red, blue, purple]
  shape: null
  themes: [space]
tech:
  mcu: ATtiny412
  leds:
    count: 3
    type: reverse-mount
    note: NeoPixels (addressable RGB)
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $15.00
  price_usd: 15
  quantity: ''
  availability: available
  availability_note: 'Per an archived Tindie snapshot from 2025-06-20 showing red/blue/purple all in stock (19-20 units each); the live listing could not be rechecked on 2026-09-07 (blocked by Cloudflare bot protection).'
  distribution: [purchase]
  where: Tindie store (alee97422)
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/alee97422/rocket-sao-v11
  url: https://www.tindie.com/products/alee97422/rocket-sao-v11/
  kind: store
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/alee97422/rocket-sao-v11/
  title: Rocket SAO v1.1
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''not on any sheet; sold on Tindie late 2024''.'
- kind: url
  url: https://web.archive.org/web/20250620081038/https://www.tindie.com/products/alee97422/rocket-sao-v11/
  title: 'Wayback Machine snapshot of the Tindie listing (2025-06-20)'
  accessed: '2026-09-07'
  note: 'Live Tindie page returned a Cloudflare bot-check (403) on direct fetch; used an archived snapshot instead for the product description, price, stock, and MCU/LED details.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Only source available is the maker's own Tindie listing (live page blocked by Cloudflare;
    used a 2025-06-20 Wayback Machine snapshot instead). The listing gives no event/con
    association -- it reads as a general storefront product, not tied to a specific
    con's badge lineup. The same maker (Alee / alee97422) has DEF CON SAO/badge entries
    elsewhere in this archive (dc32-tpb-badge, dc33-crab, dc34-breadbadge); product photo
    timestamps on the listing run from June-September 2024, which overlaps DEF CON 32
    (Aug 2024), but nothing in the listing text confirms it was made for or sold at any
    specific convention, so event is left as 'other'. No open-source hardware/firmware
    files, SAO header version, or total production quantity are stated. Two product photo
    URLs were found (an og:image and a gallery image on the archived page) but could not
    be downloaded -- both cdn.tindiemedia.com URLs returned 404 and a follow-up fetch of
    the Wayback Machine's own cached copies failed to connect, so no images were saved.
last_modified_date: '2026-09-07'
---

Rocket SAO V1.1 is a "shameless add-on" (SAO) sold by Alee (Tindie seller alee97422), the same maker behind several DEF CON badges and SAOs (TPB Badge at DC32, cRab at DC33, Breadbadge at DC34). The listing describes it as a revamped version of an earlier Rocket SAO, offered in red, blue, and purple PCB colors, hand-soldered, and built around an ATtiny412 microcontroller with a dedicated UPDI programming pin broken out on the SAO connector.

The board carries 3 reverse-mounted NeoPixels for dynamic RGB lighting effects and adds a leash connection point compared to the prior revision. It sold for $15.00 on Tindie; an archived snapshot of the listing from June 2025 showed all three colorways still in stock (19-20 units each).

The Tindie listing does not say which convention, if any, the SAO was designed for or first sold at -- it reads as a standalone storefront product rather than an entry tied to a specific year's badge lineup. Given the maker's other DEF CON work and the June-September 2024 timestamps on the product photos, a DEF CON 32 (Aug 2024) connection is plausible but unconfirmed, so the event is left as "other" pending a source that states it directly.


