---
title: Hearty Backlit Badge
id: dc30-heart-beat-sao
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: Nerfhammer
  url: https://www.tindie.com/stores/nerfhammer/
summary: A heart-shaped PCB badge/SAO with an etched anatomical heart that lights up when tapped or moved sharply.
functions: A tap/vibration sensor triggers an LED to flicker in a heartbeat-like pattern; no on/off switch, minimal idle power draw.
look:
  colors:
  - red
  shape: heart
  themes:
  - jewelry
  - pin
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single LED shines through an etched anatomical-heart cutout; driven by a discrete transistor circuit (no microcontroller).
  display: none
  connectivity: []
  battery: CR2032
  sao_version: null
get_one:
  price: $20 assembled / $10 self-assembly kit
  price_usd: 20.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold on the maker's Tindie store; listed among Nerfhammer's DEF CON 30 items in Tindie's own DEF CON 30 roundup post.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/stores/nerfhammer
  url: https://www.tindie.com/stores/nerfhammer/
  kind: store
- label: Hearty Backlit Badge (Tindie product page)
  url: https://www.tindie.com/products/nerfhammer/hearty-backlit-badge/
  kind: store
- label: Hearty Badge self-assembly kit (Tindie product page)
  url: https://www.tindie.com/products/nerfhammer/hearty-badge-self-assembly-kit/
  kind: store
- label: Tindie Blog, Badge Me if You Can - DEF CON 30
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  kind: article
images:
- file: assets/images/badges/dc30/heart-beat-sao/0844eb6dfb.jpg
  source: "https://www.tindie.com/products/nerfhammer/hearty-backlit-badge/"
  credit: "nerfhammer"
  caption: "Hearty Backlit Badge, heart-shaped tap-activated LED SAO"
contact: {}
notes:
- 'Likely the same item as dc30-heart-tap-sensor-sao: Tindie''s DEF CON 30 roundup post describes a Nerfhammer SAO with "a tap sensor to control an LED to mimic the beating of a heart" alongside Skully; that description matches the maker''s "Hearty Backlit Badge" (and its self-assembly-kit variant), a heart-shaped, tap/vibration-activated backlit badge with a SAO header. No product on Nerfhammer''s Tindie store is literally titled "Heart Beat SAO" -- that name appears to be the sweep''s own paraphrase of the roundup post''s description, not a maker-used title. Title corrected to the maker''s actual product name, "Hearty Backlit Badge."'
- 'Product photos on Tindie date to August 2018, so this design predates DEF CON 30; it was evidently still being sold (or re-offered) at DC30 2022 per the Tindie roundup post. No DC30-specific confirmation beyond that mention.'
status: listed
sources:
- kind: url
  url: https://www.tindie.com/stores/nerfhammer/
  title: Heart Beat SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2020); event read as ''DEF CON 30 2022''.'
- kind: url
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  title: 'Badge Me if You Can - DEF CON 30'
  accessed: '2026-09-08'
  note: Source of the "tap sensor... mimic the beating of a heart" description that the sweep paraphrased as "Heart Beat SAO"; lists it alongside Skully.
- kind: url
  url: https://www.tindie.com/products/nerfhammer/hearty-backlit-badge/
  title: Hearty Backlit Badge
  accessed: '2026-09-08'
  note: Maker's product page; price, description, features, and SAO header confirmed here.
- kind: url
  url: https://www.tindie.com/products/nerfhammer/hearty-badge-self-assembly-kit/
  title: Hearty Badge self-assembly kit
  accessed: '2026-09-08'
  note: DIY kit variant of the same design; $10, no SAO header mentioned for this variant.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Could not confirm an exact maker-titled product called "Heart Beat SAO"; matched by description to the "Hearty Backlit Badge" / "Hearty Badge self-assembly kit" listings, which are almost certainly the same item Tindie''s DEF CON 30 roundup was describing. This is likely a duplicate of dc30-heart-tap-sensor-sao, which cites the same roundup post. tech.mcu/leds inferred from the maker''s described circuit (discrete transistor, no MCU); could not verify sao_version (4-pin vs 6-pin) or exact DC30 sale price/quantity. The nerfhammer.tindie.com store itself is behind a Cloudflare challenge and could not be fetched directly.'
last_modified_date: '2026-09-08'
---

The Hearty Backlit Badge is a small heart-shaped PCB piece by Nerfhammer (San Francisco) with an etched anatomical heart cut into the silkscreen. A single LED behind the cutout is driven by a simple discrete circuit -- one transistor, one resistor, one capacitor, and a vibration/tap switch -- so tapping or shaking the badge makes the LED flicker in a heartbeat-like pattern. There is no microcontroller and no on/off switch; the circuit draws negligible power at rest. It runs on a CR2032 coin cell and includes a SAO header beneath the battery connector, so it can be worn as a stand-alone pin or plugged into a host badge as an add-on.

Tindie's own August 2022 roundup of DEF CON 30 badges, "Badge Me if You Can," names Nerfhammer alongside their better-known Skully SAO and describes "another SAO [that] features a tap sensor to control an LED to mimic the beating of a heart" as one of their DEF CON 30 offerings. No listing on Nerfhammer's Tindie store is titled exactly "Heart Beat SAO"; that appears to be the archive sweep's own paraphrase of the roundup's description. The closest match is the "Hearty Backlit Badge" ($20 assembled) and its "Hearty Badge self-assembly kit" ($10) variant -- both heart-shaped, tap-activated designs whose product photos date to 2018, suggesting the design predates DEF CON 30 and was carried forward or re-offered that year. This entry is likely describing the same physical item as the archive's separate dc30-heart-tap-sensor-sao entry, which cites the same source post.
