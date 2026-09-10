---
title: BSidesKC 2023 Attendee Elect Badge
id: bsides-kansas-city-2023-bsideskc-2023-attendee-elect-badge
layout: badge
parent: BSidesKC 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-kansas-city-2023
year: 2023
makers:
- name: BadgePirates
  url: https://www.tindie.com/stores/badgepirates/
summary: An ESP32-S3 electronic badge made by BadgePirates for BSidesKC 2023, used to collect Badge CTF flags during the conference.
functions: Interacts with other badges/stations to collect Badge CTF flags; the seller notes a post-conference CTF may also be available.
look:
  colors: []
  shape: null
  themes:
  - ctf
tech:
  mcu: ESP32-S3
  leds: null
  display: null
  connectivity: []
  battery: LiPo, rechargeable via USB-C
  sao_version: null
get_one:
  price: $40.00
  price_usd: 40
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing shown as out of stock as of 2026-09-10 (checked by WebFetch); seller had described remaining stock as "a few left over" from the conference.
  distribution:
  - purchase
  where: Sold after the conference via the BadgePirates Tindie store as leftover stock.
make_your_own:
  open_source: true
  hardware_url: https://github.com/BadgePiratesLLC/BSidesKC_2023
  firmware_url: https://github.com/BadgePiratesLLC/BSidesKC_2023
  eda_tool: null
links:
- label: www.tindie.com/products/badgepirates/bsideskc-2023-badge
  url: https://www.tindie.com/products/badgepirates/bsideskc-2023-badge/
  kind: store
- label: github.com/BadgePiratesLLC/BSidesKC_2023
  url: https://github.com/BadgePiratesLLC/BSidesKC_2023
  kind: repo
images:
- file: assets/images/badges/bsides-kansas-city-2023/bsideskc-2023-attendee-elect-badge/4357da36fc.jpg
  source: https://www.tindie.com/products/badgepirates/bsideskc-2023-badge/
  credit: BadgePirates
  caption: BSidesKC 2023 badge, main product photo
- file: assets/images/badges/bsides-kansas-city-2023/bsideskc-2023-attendee-elect-badge/a2e3ed7a60.jpg
  source: https://www.tindie.com/products/badgepirates/bsideskc-2023-badge/
  credit: BadgePirates
  caption: BSidesKC 2023 attendee badge
contact: {}
notes:
- ESP32-S3 badge with USB-C rechargeable battery, used to collect CTF flags at BSidesKC 2023. Found by the event-year sweep, task bsides-kansas-city.
- Tindie's product-name field for this listing is the shorter "BsidesKC 2023 Badge"; "Attendee Elect Badge" comes from the listing's own meta description/schema text ("BsidesKC 2023 Attendee Elect Badge"), which the sweep picked up. The repo's CAD folders are split by role (Organizer, Participant, Speaker, Sponsor, Village, Volunteer, BadgePirate), consistent with an "attendee" tier badge distinct from staff/speaker/sponsor variants, though the repo itself was only browsed at folder-listing level.
- 2023 BSidesKC badge, also listed for sale on Tindie. Found by the event-year sweep, task bsides-any.
- The sweep's title was "BSidesKC 2023 (BSides23)"; the maker's own storefront and GitHub org name it the "BSidesKC 2023 Attendee Elect Badge" / "BSidesKC23" badge, so the title was corrected to match Tindie's listing name.
status: listed
sources:
- kind: url
  url: https://www.tindie.com/products/badgepirates/bsideskc-2023-badge/
  title: BSidesKC 2023 Attendee Elect Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-kansas-city); event read as ''BSidesKC 2023''.'
- kind: url
  url: https://www.tindie.com/products/badgepirates/bsideskc-2023-badge/
  title: BsidesKC 2023 Badge by BadgePirates on Tindie
  accessed: '2026-09-10'
  note: Confirmed maker, ESP32-S3, USB-C rechargeable battery, $40 price, out-of-stock status, and CTF-flag function; source of product photo.
- kind: url
  url: https://github.com/BadgePiratesLLC/BSidesKC_2023
  title: BadgePiratesLLC/BSidesKC_2023
  accessed: '2026-09-10'
  note: Confirms hardware/firmware are open source; repo is archived (read-only) with CAD folders split by attendee role.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Core facts (maker, event, MCU, battery, price, open-source status) confirmed on the maker''s own Tindie listing and GitHub repo. Not found/confirmed: LED count/type, any display, and connectivity (wifi/BLE) — the ESP32-S3 likely supports wifi/BLE but the listing does not state whether either is used, so left empty rather than guessed. Exact quantity made/remaining and a specific "sold out" date are not stated beyond "a few left over." Merged with duplicate entry ''BSidesKC 2023 Attendee Elect Badge'' (bsides-kansas-city-2023-bsideskc-2023-bsides23).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/bsides-kansas-city-2023/bsideskc-2023-bsides23/
---

The BSidesKC 2023 Attendee Elect Badge is an ESP32-S3 electronic conference badge made by BadgePirates (Lee's Summit, MO) for BSidesKC 2023. It runs on a rechargeable LiPo battery charged over USB-C and was used during the conference to collect Badge CTF flags, with the seller noting a post-conference CTF may also be available to badge holders.

BadgePirates sold leftover units after the event through their Tindie store for $40, describing stock as "a few left over"; the listing is out of stock as of this check. Hardware and firmware are published on GitHub (BadgePiratesLLC/BSidesKC_2023), which is organized into CAD folders by conference role (organizer, participant, speaker, sponsor, village, volunteer, badge-pirate), suggesting this attendee-tier badge was one of several role-specific variants made for the event; the repo is now archived/read-only.

## Notes merged from the duplicate entry "BSidesKC 2023 Attendee Elect Badge"

The BSidesKC 2023 Attendee Elect Badge is an electronic conference badge made by BadgePirates (Lee's Summit, Missouri) for BSides Kansas City 2023. It runs on an ESP32-S3 microcontroller with a rechargeable battery charged over USB-C, and during the conference it was used to interact with and retrieve Badge CTF (Capture The Flag) challenges, with post-conference CTF functionality also planned.

BadgePirates sold leftover units on Tindie for $40; as of the most recent check the listing shows sold out. Design files and conference-related materials (CAD for several badge roles, CTF materials, documentation, and photos) are published on GitHub under BadgePiratesLLC/BSidesKC_2023, though that repository was archived in September 2024 and its README carries no further technical specifics beyond the project name.

This entry appears to duplicate `bsides-kansas-city-2023-bsideskc-2023-attendee-elect-badge`, an existing archive entry for the same badge under its full maker-given name.
