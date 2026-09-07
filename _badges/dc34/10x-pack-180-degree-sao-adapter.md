---
title: 10x pack! 180 Degree SAO Adapter
id: dc34-10x-pack-180-degree-sao-adapter
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc34
year: 2026
makers:
- name: bud-lightbeer (Uberfoo Heavy Industries)
summary: A 10-pack of passive adapters that flip the orientation of a SAO port so standard SAO 2.0 add-ons can plug into the DEF CON 34 official badge.
functions: 'Corrects a port-rotation mismatch: the DEF CON 34 badge''s SAO headers are mounted upside-down relative to the SAO 2.0 spec, so a standard SAO plugged in directly is misoriented or non-functional. The adapter sits between badge and SAO to fix orientation. It does not correct the DEF CON 34 badge''s 3.0V supply versus the SAO spec''s 3.3V, so voltage-sensitive SAOs may still behave oddly.'
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
  sao_version: v2
get_one:
  price: $10
  price_usd: 10
  quantity: '10 adapters per pack; 501 packs sold'
  availability: sold_out
  availability_note: 'Listed as out of stock (0 remaining, 501 sold) on uberflux.com, checked 2026-09-07.'
  distribution:
  - purchase
  where: Sold via Uberflux (uberflux.com), Uberfoo Heavy Industries' storefront; shipping was Continental USA only.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: uberflux.com/product/BUD-SAO-180-Adapter
  url: https://uberflux.com/product/BUD-SAO-180-Adapter
  kind: store
images:
  - file: assets/images/badges/dc34/10x-pack-180-degree-sao-adapter/9e66c7c885.jpg
    source: "https://uberflux.com/product/BUD-SAO-180-Adapter"
    credit: "bud-lightbeer / Uberfoo Heavy Industries"
    caption: "10-pack of 180 degree SAO port adapters"
contact: {}
notes:
- 'Uberflux. $10, status: sold out.'
- 'Maker bud-lightbeer/Uberfoo Heavy Industries also produced several DEF CON badges (dc30/dc31 Z80 Retro Badge, dc32 UberBox Badge, dc33/dc34 Shitty Kitty V2); this adapter is a separate accessory item, not a duplicate of those entries.'
status: released
sources:
- kind: url
  url: https://uberflux.com/product/BUD-SAO-180-Adapter
  title: 10x pack! 180 Degree SAO Adapter
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://uberflux.com/product/BUD-SAO-180-Adapter
  title: 10x pack! 180 Degree SAO Adapter - product page
  accessed: '2026-09-07'
  note: 'Confirmed maker (bud-lightbeer), that it targets the DEF CON 34 official badge''s rotated SAO ports, price ($10), pack quantity (10), sold-out status (501 sold), and pulled the product image.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Event corrected from "other" to dc34 based on the product page explicitly describing the fix as being for the DEF CON 34 badge''s rotated SAO header. No hardware files, schematics, or design source found; likely a simple passive PCB but this is not confirmed by any source, so tech fields are left empty. No separate maker profile page (Hackaday/GitHub) was found for bud-lightbeer beyond the Uberflux storefront.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/10x-pack-180-degree-sao-adapter/
---

Uberfoo Heavy Industries (maker "bud-lightbeer") sold this 10-pack of small SAO port adapters through their Uberflux storefront to fix a design quirk on the DEF CON 34 official badge: its SAO headers are mounted rotated 180 degrees relative to the standard SAO 2.0 pinout, which otherwise makes ordinary SAOs plug in misaligned or non-functional. The adapter is a passive pass-through that flips the orientation so any standard SAO can be seated correctly on the badge.

The listing notes one limitation the adapter does not solve: the DEF CON 34 badge supplies 3.0V to its SAO header rather than the 3.3V called for by the SAO spec, so voltage-sensitive add-ons could still misbehave even with the orientation corrected.

The pack sold for $10 and shipped only within the continental United States. By the time it was checked for this entry it was sold out, with 501 packs sold. No schematic, board files, or open-source release were found for the adapter itself.
