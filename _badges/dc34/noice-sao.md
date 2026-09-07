---
title: '#NOICE SAO'
id: dc34-noice-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: caelyb
summary: A memorial and activism SAO made for DEF CON 34, with 16 red LEDs and
  multiple flashing/animation modes; a portion of proceeds supports the Immigrant
  Defenders Law Center.
functions: Cycles through LED effects (fast and slow flashing, heartbeat, breathing/fade)
  via a single tactile button, and remembers the last-used effect in persistent memory.
look:
  colors: [red]
  shape: null
  themes: [privacy, security]
tech:
  mcu: null
  leds:
    count: 16
    type: side-emitting
    note: 16x XL-1606SURC red side-emitting LEDs, mounted to shine through the FR4 PCB
  display: none
  connectivity: []
  battery: powered by host badge (2.7V-3.7V input)
  sao_version: null
get_one:
  price: $20
  price_usd: 20.0
  quantity: ''
  availability: sold_out
  availability_note: Uberflux listing showed 9 sold, 0 remaining as of 2026-09-07.
  distribution: [purchase]
  where: Sold via the maker's Uberflux storefront; shipped after DC34 to the continental
    US only ($7 shipping). Included one SAO unit and a lanyard with lobster clasp.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: uberflux.com/product/DC34-noice
  url: https://uberflux.com/product/DC34-noice
  kind: store
images:
- file: assets/images/badges/dc34/noice-sao/02b982cedf.jpg
  source: "https://uberflux.com/product/DC34-noice"
  credit: "Uberflux / caelyb"
  caption: "The #NOICE SAO, front view showing red LED array"
- file: assets/images/badges/dc34/noice-sao/8247887233.jpg
  source: "https://uberflux.com/product/DC34-noice"
  credit: "Uberflux / caelyb"
  caption: "The #NOICE SAO, alternate view"
contact: {}
notes:
- 'Uberflux. $20, status: sold out.'
- This appears to be the same item as dc34-noice (#NoIce by RivaClan/caelyb), sold
  through two storefronts (Uberflux here, ko-fi.com/caelybr on the other entry) with
  matching specs (16x XL-1606SURC red LEDs, single-button effect cycling, persistent
  memory, 2.7-3.7V input, $20, DC34, ICE/DHS memorial theme). See duplicate_of in
  the research report.
status: listed
sources:
- kind: url
  url: https://uberflux.com/product/DC34-noice
  title: '#NOICE SAO'
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''DEF CON 34''.'
- kind: url
  url: https://uberflux.com/product/DC34-noice
  title: '#NOICE SAO'
  accessed: '2026-09-07'
  note: Confirmed product description, LED count/type, button/effect features, price
    ($20), sold-out status (9 sold, 0 remaining), shipping terms, and package
    contents (unit + lanyard). Fetched two product photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (LEDs, button/effects, price, sold-out status) confirmed from
    the Uberflux storefront itself. Could not find the maker's MCU choice, SAO
    header version, quantity made, or open-source design files from this listing.
    A web search for the maker "caelyb" turned up no additional profile, repo, or
    social presence beyond what is already linked from the sibling entry dc34-noice.
    This entry is very likely a duplicate of dc34-noice (#NoIce, maker RivaClan) --
    same LED hardware, same button/effect behavior, same $20 price, same DC34/ICE-DHS
    memorial theme, same power input range -- just sold through a different storefront
    (Uberflux vs. ko-fi.com/caelybr). Left as a separate entry per instructions; see
    duplicate_of in the research report.
last_modified_date: '2026-09-07'
---

The #NOICE SAO is a Simple Add-On made for DEF CON 34, sold through the maker's
Uberflux storefront for $20. It carries 16 red XL-1606SURC side-emitting LEDs
mounted so their light shines through the FR4 PCB, with a single tactile button
that cycles through several lighting effects -- fast and slow flashing, a heartbeat
pattern, and a breathing/fade sequence -- and persistent memory that restores the
last-used effect after power loss. It runs on host-badge power across a wide
2.7V-3.7V input range.

The listing sold out with 9 units purchased; each order included one SAO and a
lanyard with a lobster clasp, shipped after DC34 to continental US addresses only.
A portion of proceeds went to the Immigrant Defenders Law Center.

This item's specifications and description closely match another archive entry,
dc34-noice ("#NoIce" by maker RivaClan/caelyb), which describes the same LED
hardware, button behavior, price, and DEF CON 34 ICE/DHS memorial theme, but was
sold via ko-fi.com/caelybr rather than Uberflux. The two are almost certainly the
same physical SAO sold through two different storefronts by the same person.
