---
title: Ubuntu SAO
id: other-ubuntu-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: 'Alee (Tindie: alee97422)'
  url: https://www.tindie.com/stores/alee97422/
summary: A small SAO with an orange Ubuntu logo on colored silkscreen, driven by an ATtiny85 with two LEDs.
functions: Lights two LEDs; plugs into a host badge's SAO header as a decorative add-on.
look:
  colors: [orange, black]
  shape: null
  themes: [logo, minimalist]
tech:
  mcu: ATtiny85
  leds:
    count: 2
    type: discrete
    note: Two LEDs with two current-limiting resistors.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: $10.99
  price_usd: 10.99
  quantity: ''
  availability: unknown
  availability_note: 'Listed in stock on Tindie as of a June 22, 2024 snapshot; live page could not be checked on 2026-09-07 (Cloudflare-blocked).'
  distribution: [purchase]
  where: Sold individually on the maker's Tindie store (alee97422).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/alee97422/ubuntu-sao
  url: https://www.tindie.com/products/alee97422/ubuntu-sao/
  kind: store
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/alee97422/ubuntu-sao/
  title: Ubuntu SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''not on any sheet; sold individually on Tindie mid-2024''.'
- kind: url
  url: http://web.archive.org/web/20240622062120/https://www.tindie.com/products/alee97422/ubuntu-sao/
  title: UBUNTU SAO from @alee97422 on Tindie (Wayback Machine snapshot, 2024-06-22)
  accessed: '2026-09-07'
  note: 'Live Tindie page returned a Cloudflare challenge (403) on direct fetch; used an archived snapshot instead for description, price ($10.99), MCU/LED specs, and product images. Confirmed ATtiny85, two LEDs, colored-silkscreen JLCPCB process, orange Ubuntu logo front / tie-dye back.'
- kind: url
  url: http://web.archive.org/web/20241211101001/https://www.tindie.com/stores/alee97422/
  title: Browse products by @alee97422 on Tindie (Wayback Machine snapshot, 2024-12-11)
  accessed: '2026-09-07'
  note: 'Confirms maker is a #BADGELIFE seller (Alee) making SAOs and conference badges; no specific event named for the Ubuntu SAO.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The maker''s own description calls it "a must-have for any cyber conference" but does not name a specific con or year it was made for, so event is left as other/unaffiliated rather than guessed. Quantity made is not stated. The live Tindie listing is behind a Cloudflare bot-check that blocked automated fetch on 2026-09-07 (used an archived June 2024 snapshot instead, when it appears to have been newly listed and in stock); current availability is unknown. Two product photos (front logo, tie-dye back) were located on the archived page but the CDN image URLs use time-limited signed links that had expired and were not separately archived by the Wayback Machine, so no images could be saved. This maker (Alee / alee97422) already has several entries in the archive for specific DEF CON years (dc32-tpb-badge, dc33-crab, dc34-breadbadge); this SAO does not appear to duplicate any of them.'
last_modified_date: '2026-09-07'
---

The Ubuntu SAO is a small shameless-add-on made by Alee (Tindie seller alee97422), a badgelife maker also known for the TPB Badge, cRab, and Breadbadge conference badges. It runs on an ATtiny85 microcontroller and lights two LEDs through a pair of current-limiting resistors -- simple, low-power blinky logic typical of a SAO meant to be plugged into a host badge's SAO header rather than worn on its own.

Its main selling point is cosmetic: the board uses JLCPCB's colored-silkscreen process to print an orange Ubuntu logo on the front, paired with a tie-dye pattern on the back. It was sold individually through the maker's Tindie store for $10.99, first appearing on the listing in mid-2024. The maker's own copy pitches it generically as good for "any cyber conference" rather than naming one specific event, so it is catalogued here under Other/unaffiliated rather than tied to a particular con.
