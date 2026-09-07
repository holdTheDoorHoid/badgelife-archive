---
title: Vibe Coder Dog SAO
id: dc34-viber-coder-dog-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: coryallegory
summary: A dog character SAO themed around "vibe coding," pounding a tiny keyboard while four LEDs cycle multicolor behind it.
functions: 4 randomly cycling multicolor LEDs light up the keyboard graphic
look:
  colors: []
  shape: dog
  themes:
  - dog
  - meme
  - pop culture
tech:
  mcu: null
  leds:
    count: 4
    type: RGB
    note: randomly cycling multicolor
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: '15'
  price_usd: 15.0
  quantity: ''
  availability: sold_out
  availability_note: 'Both the Uberflux and Tindie listings show 0 in stock as of 2026-09-06; Tindie shows sold out since 2025-09-13, with preorders taken for DEF CON 34.'
  distribution:
  - purchase
  - preorder
  where: Sold assembled through the maker's Uberflux storefront and Tindie shop, $15 each.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: uberflux.com/product/CGORY-VIBECODERDOG
  url: https://uberflux.com/product/CGORY-VIBECODERDOG
  kind: store
- label: Vibe Coder SAO on Tindie
  url: https://www.tindie.com/products/coryallegory/vibe-coder-sao-badgelife-addon/
  kind: store
images:
- file: assets/images/badges/dc34/viber-coder-dog-sao/45dea67178.jpg
  source: "https://uberflux.com/product/CGORY-VIBECODERDOG"
  credit: "coryallegory"
  caption: "Vibe Coder Dog SAO, assembled with keyboard LEDs"
- file: assets/images/badges/dc34/viber-coder-dog-sao/0b624c8eb5.jpg
  source: "https://www.tindie.com/products/coryallegory/vibe-coder-sao-badgelife-addon/"
  credit: "coryallegory"
  caption: "Vibe Coder SAO Tindie listing photo"
contact:
  discord: coryallegory
  emails:
  - corymetcalfe@gmail.com
  handles:
  - '@coryallegory'
  raw:
  - on twitter, bluesky, discord
notes:
- 'Sheet title read "Viber Coder Dog SAO"; the maker''s own listings call it "Vibe Coder (Dog) SAO" — corrected here, sheet spelling kept for reference.'
- 'This looks like the same design as dc33-vibe-coder-sao (also by coryallegory, "Vibe Coder SAO"), originally made for DEFCON 33 and re-listed/pre-ordered for DEF CON 34; flagged as a likely duplicate rather than a new design.'
status: released
sources:
- kind: sheet
  event: dc34
  row: 46
  updated: 7/22/2026 1:26:05
  listing: New
- kind: url
  url: https://uberflux.com/product/CGORY-VIBECODERDOG
  title: Vibe Coder Dog SAO — Uberflux
  accessed: '2026-09-06'
  note: Product description, price, LED behavior, stock status (0 in stock, 5 sold), maker's own framing that it was originally made for DEFCON 33.
- kind: url
  url: https://www.tindie.com/products/coryallegory/vibe-coder-sao-badgelife-addon/
  title: Vibe Coder SAO #badgelife addon — Tindie
  accessed: '2026-09-06'
  note: Confirms maker location (Winnipeg, Canada), 4-LED count, $15 price, sold out since 2025-09-13, and DEF CON 34 preorder note.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'No MCU, battery, or SAO pin-count details published on either storefront, so tech fields other than LEDs are left empty. No design files or repo found for this dog variant (the earlier dc33-vibe-coder-sao entry lists a github.com/coryallegory/vibecoder repo link from the sheet, unverified). Likely the same physical product as dc33-vibe-coder-sao, carried over/re-sold for DC34 rather than a distinct new design — see duplicate note.'
last_modified_date: '2026-09-06'
---

The Vibe Coder Dog SAO is a small add-on by coryallegory (Winnipeg, Manitoba) built around a dog character hammering away at a tiny keyboard, with four LEDs behind the keys cycling through random colors. The maker describes it as a continuation of an earlier "Science Dog" design, now recast as "Coder Dog" for the vibe-coding meme, and notes it was originally produced for DEFCON 33 before being sold again (via preorder) for DEF CON 34.

It sold assembled for $15 through both the maker's own Uberflux storefront and a Tindie listing, with a standard 2x3 SAO header for plugging into a badge. As of this check both storefronts show it out of stock — Tindie has shown it sold out since September 2025, with the DEF CON 34 run taken as preorders for post-con delivery. No MCU, firmware, or hardware files are published for this SAO, and no separate repository specific to the dog variant was found.

This entry is very likely the same underlying board as `dc33-vibe-coder-sao`, also made by coryallegory under the near-identical name "Vibe Coder SAO," rather than a new design made specifically for DC34.
