---
title: Half-assed DC30 Hacker Homecoming Nametag
id: dc30-half-assed-dc30-hacker-homecoming-nametag
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: DC540 Nova
  url: https://www.tindie.com/stores/dc540_nova/
summary: A TV-antenna-shaped, business-card-sized nametag made by the DC540 Defcon group for DEF CON 30, meant to double as an NFC business card but shipped with the NFC disabled after a PCB layout error.
functions: 'Wearable nametag with an adhesive pinback and lanyard holes; blank silkscreen space for writing a hacker handle in marker. Was designed to share contact info by NFC tap, but the onboard antenna was blocked by a copper fill error, so an anti-metal NFC sticker was applied to the back as a workaround instead of using the onboard chip.'
look:
  colors: []
  shape: null
  themes:
  - text
  - minimalist
tech:
  mcu: none
  leds: null
  display: null
  connectivity:
  - nfc
  battery: null
  sao_version: none
get_one:
  price: $10.00
  price_usd: 10
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listing checked 2026-09-07: distributed at DEF CON 30 (2022); the maker''s store page indicated the item was off sale while working on other badges.'
  distribution:
  - purchase
  where: Sold/distributed by the DC540 Defcon group (DC540 Nova) at DEF CON 30, and listed on their Tindie store.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/dc540_nova/half-assed-dc30-hacker-homecoming-nametag
  url: https://www.tindie.com/products/dc540_nova/half-assed-dc30-hacker-homecoming-nametag/
  kind: store
- label: 'DC540: Did you get one of our half-assed NFC business card name tags?'
  url: https://dc540.org/xxx/2022/08/did-you-get-one-of-our-half-assed-nfc-business-card-name-tags/
  kind: article
images:
- file: assets/images/badges/dc30/half-assed-dc30-hacker-homecoming-nametag/752c70404e.jpg
  source: "https://www.tindie.com/products/dc540_nova/half-assed-dc30-hacker-homecoming-nametag/"
  credit: "DC540 Nova"
  caption: "The half-assed DC30 Hacker Homecoming nametag, a TV-antenna-shaped PCB badge with NFC sticker on the back"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/dc540_nova/half-assed-dc30-hacker-homecoming-nametag/
  title: Half-assed DC30 Hacker Homecoming Nametag
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc30''.'
- kind: url
  url: https://dc540.org/xxx/2022/08/did-you-get-one-of-our-half-assed-nfc-business-card-name-tags/
  title: 'Did you get one of our half-assed NFC business card name tags? – DC540 Defcon Group'
  accessed: '2026-09-07'
  note: 'Maker''s own blog post explaining the NFC antenna copper-fill design flaw and the sticker workaround.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Quantity made and exact original distribution method (free with something vs. straight sale) not stated by either source. No repo or design files found for this specific nametag (DC540 does publish some other badge repos on GitHub, e.g. DC29-Tree-of-Life-Badge, but nothing was found specifically for this nametag).'
last_modified_date: '2026-09-07'
---

DC540, a regional DEF CON group based near Dulles, Virginia, made this nametag as a piece of DEF CON 30 (2022) memorabilia. It is a business-card-sized PCB cut into the shape of an old TV antenna, meant to be worn with an adhesive pinback or a lanyard, with blank silkscreen space where the wearer can write their handle in marker.

The nametag was originally designed to work as a tap-to-share NFC business card. A layout mistake carried a keepout zone from the back copper layer onto the front, so the front copper fill ended up overlapping and blocking the antenna trace, which killed the NFC function on the built boards. Rather than scrap the run, DC540 removed the onboard NFC chip and stuck a separate anti-metal NFC sticker to the back of each badge, letting it still function as an NFC tap tag while sidestepping the broken circuit — the source of the "half-assed" name. The maker wrote about the mistake and the fix on the DC540 blog, offering to mail replacement NFC chips to anyone who wanted to try repairing the onboard circuit themselves.

It sold for $10 on DC540's Tindie store alongside their other badges (including the DC29 Tree of Life badge and the DC30 Tarot badge); by the time it was checked for this entry the listing indicated it was unavailable while the group worked on other projects.
