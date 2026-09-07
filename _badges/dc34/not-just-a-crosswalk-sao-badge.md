---
title: Not Just a Crosswalk SAO / Badge
id: dc34-not-just-a-crosswalk-sao-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: caelyb
  url: https://ko-fi.com/caelybr
summary: An 18-LED rainbow SAO built as a hardware protest against the removal of rainbow crosswalk street art in several US cities; sold on Uberflux as a DEF CON 34 badge drop.
functions: Two tactile buttons cycle through 10+ LED animation effects (static, party mode, strobe, pulse, chase, sparkle, burst) and 13+ pride-flag color palettes (rainbow, bi, lesbian, trans, nonbinary, asexual, genderfluid, poly, bear, leather, disability, demi). Settings persist in memory across power loss.
look:
  colors: [black, multicolor]
  shape: rectangle
  themes: [pride, security, hardware tool]
tech:
  mcu: null
  leds:
    count: 18
    type: SK6812-EC3210R (side-emitting)
    note: null
  display: none
  connectivity: []
  inputs:
  - buttons
  battery: null
  power: USB-C 5V or 3V badge SAO port with onboard boost converter
  sao_version: null
get_one:
  price: $34
  price_usd: 34.0
  quantity: ''
  availability: sold_out
  availability_note: 'Checked 2026-09-06 via uberflux.com/product/DC34-crosswalk: listed as 0 remaining, 13 sold.'
  distribution: [purchase]
  where: Sold through Uberflux as a DEF CON 34 in-person pickup, with post-event shipping to the continental US available for $10.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: uberflux.com/product/DC34-crosswalk
  url: https://uberflux.com/product/DC34-crosswalk
  kind: store
images:
- file: assets/images/badges/dc34/not-just-a-crosswalk-sao-badge/96de5568d5.jpg
  source: "https://uberflux.com/product/DC34-crosswalk"
  credit: "caelyb / Uberflux"
  caption: "The Not Just a Crosswalk SAO listed on Uberflux's DC34 storefront"
contact: {}
notes:
- 'Uberflux. $34, status: sold out.'
status: released
sources:
- kind: url
  url: https://uberflux.com/product/DC34-crosswalk
  title: Not Just a Crosswalk SAO / Badge
  accessed: '2026-09-07'
  note: 'Primary source: gives the mission statement (protest of rainbow crosswalk removals), LED count/type, effects, flag palettes, price $34, and sold-out status (0 remaining, 13 sold).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This appears to be the same item as the existing entry dc34-not-just-a-crosswalk (title "Not Just a Crosswalk", maker RivaClan / Caelyb Riva / caelybr) — same maker handle (caelyb/caelybr), same DEF CON 34 rainbow-crosswalk-protest SAO concept, same LED family (SK6812/WS2812-2020 side-emitting), likely the Uberflux storefront listing for that same open-source project. That other entry has confirmed MCU (CH32V003), open-source repo, and license details from the maker''s GitHub, which were not re-derived here since the Uberflux product page does not mention chip, SAO header version, or design files. Left mcu, sao_version, and make_your_own fields empty rather than assume they match without a source stating it on this page. Price differs slightly from the other entry''s sheet-sourced $35 (this Uberflux listing says $34); left both as reported by their own sources.'
last_modified_date: '2026-09-07'
---

Not Just a Crosswalk is a rainbow-lit SAO sold through the Uberflux storefront as a DEF CON 34 badge drop, priced at $34 with in-person pickup at the con (post-event shipping available for $10). It carries 18 side-emitting SK6812-EC3210R LEDs behind a crosswalk-styled cutout, with two tactile buttons to cycle through more than ten animation effects — static display, party mode, strobe, pulse, chase, sparkle, and burst — and over a dozen pride-flag color palettes (rainbow, bi, lesbian, trans, nonbinary, asexual, genderfluid, poly, bear, leather, disability, and demi). It can run standalone from USB-C or draw power through a host badge's SAO port, with a boost converter to keep the LEDs at full brightness either way, and it remembers the last effect and palette used across power loss. The listing sold out at 13 units.

This entry and its Uberflux listing describe what looks like the same badge already documented in more technical depth under `dc34-not-just-a-crosswalk`, credited to RivaClan (Caelyb Riva, handle caelybr): both are DEF CON 34 rainbow SAOs built explicitly as a protest against the removal of rainbow crosswalk street art, from the same maker handle (caelyb/caelybr), with the same side-emitting LED family. The Uberflux page itself does not name the microcontroller or link any open-source design files, so those fields are left empty here rather than copied over from the other entry without a source on this page confirming them.
