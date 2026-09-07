---
title: Rust Crab Badge
id: other-rust-crab-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2025
makers:
- name: Tw0nkus
summary: 'A Rust-themed independent badge by maker Tw0nkus, sold on Uberflux with an OLED display, addressable LEDs, and battery power.'
functions: ''
look:
  colors: []
  shape: null
  themes:
  - rust
  - crab
tech:
  mcu: CH32V203
  leds:
    count: 18
    type: WS2812
    note: 'Plus one common red user LED.'
  display: SSD1306 OLED
  connectivity: []
  battery: LiPo, rechargeable
  sao_version: null
get_one:
  price: $35
  price_usd: 35
  quantity: '10 (7 sold, 3 remaining as of 2026-09-07)'
  availability: limited
  distribution:
  - purchase
  where: 'Sold directly through the maker''s storefront on Uberflux.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: uberflux.com/product/TW0N-RustBadge
  url: https://uberflux.com/product/TW0N-RustBadge
  kind: store
images:
  - file: assets/images/badges/other/rust-crab-badge/3afb377a60.jpg
    source: "https://uberflux.com/product/TW0N-RustBadge"
    credit: "Tw0nkus"
    caption: "Rust Crab Badge, front view"
  - file: assets/images/badges/other/rust-crab-badge/1787661a11.jpg
    source: "https://uberflux.com/product/TW0N-RustBadge"
    credit: "Tw0nkus"
    caption: "Rust Crab Badge, alternate view"
contact: {}
notes:
- 'Uberflux. $35, status: upcoming drop.'
status: listed
sources:
- kind: url
  url: https://uberflux.com/product/TW0N-RustBadge
  title: Rust Crab Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://uberflux.com/product/TW0N-RustBadge
  title: Rust Crab Badge - Uberflux product page
  accessed: '2026-09-07'
  note: 'Confirmed maker (Tw0nkus), specs (CH32V203, 18 WS2812 LEDs + 1 red user LED, SSD1306 OLED, LiPo w/ charging, 3D-printed battery sleeve, custom lanyard), price ($35), sales count (7 sold / 10 total), and two gallery image URLs, via the page''s embedded JSON.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    The storefront description says "Rust themed badge made in 2025", which matches DEF CON 33
    (Aug 2025). However, the same listing tags its drop option as "Defcon34" (per _data/events.yml,
    DC34 is August 2026, i.e. in the future as of this check). Since the year statement and the
    drop-option label point to two different DEF CONs, event was left as "other" rather than guessed;
    a human should re-check the listing closer to DEF CON 34 to see whether "Defcon34" was an error
    at listing time or the badge is actually intended for the 2026 con despite the "made in 2025" text.
    No maker profile, repo, or design files were found; open_source and hardware/firmware URLs are
    unknown. functions, look.colors, look.shape, tech.connectivity, tech.sao_version, and contact
    were not stated anywhere found and are left empty.
last_modified_date: '2026-09-07'
---

The Rust Crab Badge is an independent electronic badge by maker Tw0nkus, sold directly through the maker's storefront on Uberflux. Per the listing, it is a "Rust themed badge made in 2025," built around a CH32V203 microcontroller with an SSD1306 OLED display, 18 addressable WS2812 LEDs, and a common red user LED. It is battery-powered with onboard charging, ships with a 3D-printed battery sleeve, and comes with a custom lanyard.

The badge sold for $35 out of a run of 10 units; as of this check, 7 had sold with 3 remaining. The listing tags the badge's drop as "Defcon34," which is at odds with the "made in 2025" description text, since DEF CON 34 falls in August 2026 while DEF CON 33 was the 2025 event — see the research notes above. No hardware, firmware, or design files were found to be published for this badge.
