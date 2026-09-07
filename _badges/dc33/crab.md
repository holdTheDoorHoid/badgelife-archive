---
title: cRab
id: dc33-crab
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Alee
  url: https://www.tindie.com/stores/alee97422/
summary: A Rust-themed badge (listed on Tindie as "Rust_Badge for DC33") with an OLED display and neopixels, built around a CH32V203 microcontroller.
functions: OLED display and neopixels with multiple animations, cycled with onboard buttons; SAO port; USB-C for charging, power, and firmware updates; battery included
look:
  colors: []
  shape: null
  themes:
  - mascot
  - animal
tech:
  mcu: CH32V203
  leds: null
  display: OLED
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: $75.00
  price_usd: 75.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Listed for sale on Tindie ($75), but the maker stated it would not be shipped — buyers arranged pickup in person at DEF CON 33, with shipping only possibly available for some units after the con.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/alee97422/rust_badge-for-dc33
  url: https://www.tindie.com/products/alee97422/rust_badge-for-dc33/
  kind: store
images: []
contact:
  emails:
  - alee97422.tindiestore@gmail.com
notes: []
status: listed
sources:
- kind: sheet
  event: dc33
  row: 16
  updated: 7/4/2025 9:55:08
- kind: url
  url: http://web.archive.org/web/20250716213438/https://www.tindie.com/products/alee97422/rust_badge-for-dc33/
  title: 'Rust_Badge for DC33 from @alee97422 on Tindie (Wayback Machine snapshot, 2025-07-16)'
  accessed: '2026-09-06'
  note: The live Tindie listing returns a Cloudflare 403 to automated fetches, so this archived snapshot (taken about three weeks before DEF CON 33) was used. Confirms title, $75 price, product description (OLED, neopixels, CH32V203, USB port for charging/power/firmware, buttons to switch animations), in-stock status at that time, and the pickup-only distribution note.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    The maker's Tindie listing is titled "Rust_Badge for DC33"; the sheet's "cRab" title is the maker's
    own pun (Rust's mascot is Ferris the crab), so it was kept as the entry title. Could not reach the
    live Tindie page directly (Cloudflare blocks automated fetches); all product detail comes from an
    Internet Archive snapshot dated 2025-07-16, about three weeks before the con, which showed the item
    in stock. Current availability after the con is unknown. The listing said hardware/firmware file
    links would be posted after the con, but no such repo, Hackaday.io project, or GitHub org for
    alee97422 could be located, so make_your_own fields are left empty. LED count/type, exact display
    size, battery chemistry, colors, and shape could not be confirmed without a working image or a
    reachable product page, so those fields are left empty rather than guessed. Two product photo URLs
    were found in the archived page's structured data but the underlying Tindie CDN links returned 404s
    (signed/expiring image URLs) when fetched directly, so no images could be saved.
last_modified_date: '2026-09-06'
---

Alee's "cRab" badge for DEF CON 33 (listed on Tindie under the more literal name "Rust_Badge for DC33") pairs a CH32V203 microcontroller with an OLED display and a set of neopixels, with onboard buttons to cycle through different animations on each. It charges and takes firmware updates over USB-C, and shipped with its battery included.

Unusually for a Tindie listing, the badge was not sold as a mail-order item: the maker's description says these were made to be handed out in person at DEF CON 33, with buyers expected to arrange pickup at the con rather than shipping, and only a possibility of some units going out by mail afterward. The $75 listing was still marked in stock a few weeks before the con, per an archived copy of the page; whether any were shipped after the con, and how many were made in total, is not known from the sources found here.

The maker said links to the hardware and firmware files would be posted after the con, but no such repository, Hackaday.io project, or other public source could be located for this research pass, so the design is not confirmed as open source.
