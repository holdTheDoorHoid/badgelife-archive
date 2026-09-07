---
title: Firefly Jar SAO
id: dc34-firefly-jar-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: Lepi Labs
  url: https://www.lepi-labs.com/
  role: 'artwork by RaiVesper'
summary: A decorative jar of illuminated fireflies built as a SAOv3-compliant add-on for DEF CON 34, with seven reverse-mounted orange LEDs driven by an ATtiny824.
functions: Lights the seven reverse-mounted LEDs in configurable modes via onboard vendor commands; identifies itself to a host badge and exposes custom controls over I2C per the SAOv3 standard.
look:
  colors:
  - orange
  - clear
  shape: jar
  themes:
  - nature
  - jewelry
tech:
  mcu: ATtiny824
  leds:
    count: 7
    type: reverse-mount
    note: Orange LEDs made to look like fireflies inside the jar.
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: v3
get_one:
  price: $25
  price_usd: 25
  quantity: '25'
  availability: sold_out
  availability_note: Listed as "OUT" (sold out) on Uberflux as of 2026-09-07.
  distribution:
  - purchase
  where: Sold through Uberflux's online store for DEF CON 34.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'Reprogrammable over UPDI (adapter not included); no schematic, firmware, or Gerber files were found published.'
links:
- label: uberflux.com/product/LEPI-dc34-fireflies
  url: https://uberflux.com/product/LEPI-dc34-fireflies
  kind: store
- label: Lepi Labs
  url: https://www.lepi-labs.com/
  kind: website
images:
- file: assets/images/badges/dc34/firefly-jar-sao/e72aba6f75.jpg
  source: "https://uberflux.com/product/LEPI-dc34-fireflies"
  credit: "Lepi Labs"
  caption: "Firefly Jar SAO product photo"
- file: assets/images/badges/dc34/firefly-jar-sao/67319f35b4.jpg
  source: "https://uberflux.com/product/LEPI-dc34-fireflies"
  credit: "Lepi Labs"
  caption: "Firefly Jar SAO, alternate angle"
contact: {}
notes:
- 'Uberflux. $25, status: sold out.'
status: released
sources:
- kind: url
  url: https://uberflux.com/product/LEPI-dc34-fireflies
  title: Firefly Jar SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''DEF CON 34''.'
- kind: url
  url: https://uberflux.com/product/LEPI-dc34-fireflies
  title: Firefly Jar SAO
  accessed: '2026-09-07'
  note: 'Product description: maker, chip (ATtiny824), 7 reverse-mount orange LEDs, SAOv3 compliance (no ARP/hot-plug support), 25 made, $25, sold out, prototype v0.1 vs release v1.0.'
- kind: url
  url: https://www.lepi-labs.com/
  title: Lepi Labs
  accessed: '2026-09-07'
  note: 'Confirms Lepi Labs as a maker of PCB badges and acrylic lights; no separate listing for the Firefly Jar SAO found on their current site (likely delisted after selling out).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, chip, LED count, price, quantity, sold-out status) come from the Uberflux product listing itself, which reads as the maker''s own storefront copy. Could not find a Lepi Labs-hosted page, GitHub repo, Hackaday.io post, or open-source design files for this specific item; it is not currently listed on lepi-labs.com (probably removed after selling out). Other DC34 entries credit Lepi Labs work to a maker named "Xenu" (team name Lepi Labs) but no source tied Xenu specifically to the Firefly Jar, so that name was not added here.'
last_modified_date: '2026-09-07'
---

The Firefly Jar SAO is a small decorative piece built for DEF CON 34: a jar shape lit from within by seven reverse-mounted orange LEDs made to look like fireflies. It plugs into a host badge as a SAOv3-compliant add-on, using an ATtiny824 to run onboard lighting modes and to identify itself and expose controls to the host over I2C, though it does not implement SAOv3's optional auto-recognition/hot-plug (ARP) features. Lepi Labs made it in a run of 25, sold through Uberflux for $25; the listing notes minor hardware differences between an early v0.1 prototype and the final v1.0 release. Artwork for the piece is credited to RaiVesper. The board is reprogrammable over UPDI (adapter sold separately), but no schematic, firmware, or fabrication files for it were found published, so it does not appear to be open source.

All 25 units sold, and the piece is no longer listed on Lepi Labs' own current storefront.
