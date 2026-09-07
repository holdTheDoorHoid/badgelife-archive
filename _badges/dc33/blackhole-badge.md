---
title: Blackhole Badge
id: dc33-blackhole-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Kaizen Labs
  url: https://kaizenlabs.uk/
summary: A DEF CON 33 "proof of concept" badge built around an ESP32 with a pair of nRF24 modules, sold as a short-range (about 6 inch) 2.4GHz jammer/spectrum-testing platform for Bluetooth, Wi-Fi, BLE and similar devices.
functions: 'Runs third-party ESP32/nRF24 jamming firmware (not preloaded) to disrupt or test 2.4GHz devices (Bluetooth, Wi-Fi, BLE, RC, IoT) at close range; an optional add-on OLED screen shows status.'
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
  - hardware tool
tech:
  mcu: ESP32
  leds: null
  display: 'optional add-on OLED (sold separately)'
  connectivity:
  - wifi
  - ble
  - bluetooth
  battery: 3x AA (batteries not included)
  sao_version: null
get_one:
  price: Board only $50 / DIY Kit $100 / Assembled $175 / Assembled + Screen $189.99 (sheet price; later marked down to $49.99/$99.99/$175/$189.99 in a site sale)
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - purchase
  where: Kaizen Labs' own online store (kaizenlabs.uk / kaizentechlabs.us)
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: "Ships with no firmware installed (\"for regulatory reasons\"). The product page lists four third-party open-source firmware projects buyers can flash themselves: nrfBlueNullifier (github.com/wirebits/nrfBlueNullifier), ESP32-BlueJammer (github.com/EmenstaNougat/ESP32-BlueJammer, the maker's recommended option), NRF24-BlueJammer (github.com/jbalagiya/NRF24-BlueJammer), and RF-Clown (github.com/cifertech/RF-Clown). These are independent community projects, not Kaizen Labs' own hardware/firmware release for this board."
links:
- label: kaizenlabs.uk/product/defcon-blackhole-badge
  url: https://kaizenlabs.uk/product/defcon-blackhole-badge/
  kind: website
- label: 'Wayback Machine capture, 2025-12-15 (site returns a database error as of 2026-09-06)'
  url: http://web.archive.org/web/20251215000314/https://kaizenlabs.uk/product/defcon-blackhole-badge/
  kind: website
- label: 'ESP32-BlueJammer (recommended flashable firmware, third-party)'
  url: https://github.com/EmenstaNougat/ESP32-BlueJammer
  kind: repo
- label: 'nrfBlueNullifier (alternative firmware, third-party)'
  url: https://github.com/wirebits/nrfBlueNullifier
  kind: repo
- label: 'NRF24-BlueJammer (alternative firmware, third-party)'
  url: https://github.com/jbalagiya/NRF24-BlueJammer
  kind: repo
- label: 'RF-Clown (alternative firmware, third-party)'
  url: https://github.com/cifertech/RF-Clown
  kind: repo
images:
- file: assets/images/badges/dc33/blackhole-badge/78dcefe703.jpg
  source: "https://kaizenlabs.uk/product/defcon-blackhole-badge/"
  credit: "Kaizen Labs"
  caption: "Blackhole Badge PCB, front view"
- file: assets/images/badges/dc33/blackhole-badge/7b74d9da48.jpg
  source: "https://kaizenlabs.uk/product/defcon-blackhole-badge/"
  credit: "Kaizen Labs"
  caption: "Blackhole Badge, back render showing components"
contact: {}
notes:
- Assembled Badge $175, Badge Kit $100, Board Only $50
- 'Maker markets it as "Signal Terminator" / "weaponized ESP32 platform" and warns RF jamming is legally gray depending on jurisdiction; range is hardware-limited to roughly 6 inches for compliance.'
status: listed
sources:
- kind: sheet
  event: dc33
  row: 53
  updated: 7/28/2025
- kind: url
  url: http://web.archive.org/web/20251215000314/https://kaizenlabs.uk/product/defcon-blackhole-badge/
  title: 'Blackhole Badge - Kaizen Labs (Wayback Machine capture)'
  accessed: '2026-09-06'
  note: 'Primary source for description, specs, price tiers, firmware links, and images. Live site (kaizenlabs.uk and kaizentechlabs.us) returned server/database errors on 2026-09-06, so the December 2025 archive snapshot was used; product images at kaizentechlabs.us/wp-content/uploads/ were still reachable directly.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Live product page is currently broken (database error on kaizenlabs.uk, 403 on kaizentechlabs.us); all detail comes from a Wayback Machine capture dated 2025-12-15, so current stock/availability could not be confirmed firsthand. No Hackaday.io project, GitHub repo, or press coverage specific to this badge was found — the four GitHub links on the product page are third-party firmware projects the buyer is pointed to, not a release by Kaizen Labs itself, so make_your_own.open_source is left null. LED count/type and exact quantity made are not stated anywhere found.'
last_modified_date: '2026-09-06'
---

Kaizen Labs' Blackhole Badge is a DEF CON 33 "proof of concept" badge built around an ESP32 paired with dual nRF24 modules. The maker markets it under the tagline "Signal Terminator," describing it as a short-range 2.4GHz jamming and spectrum-testing platform aimed at Bluetooth, Wi-Fi, BLE, RC, and other IoT devices at close range (roughly six inches by design, which the maker frames as a compliance-motivated hardware limit). It runs on 3x AA batteries and can take an optional add-on OLED screen sold separately for status feedback.

The board ships with no firmware installed. Instead of publishing its own firmware, the product page points buyers to four independent, third-party open-source jammer projects on GitHub to flash themselves, with ESP32-BlueJammer listed as the maker's recommended choice. It was sold in four tiers through Kaizen Labs' own storefront: board-only, a DIY solder-it-yourself kit, a fully assembled unit, and an assembled unit with the screen add-on, priced (per the community sheet from July 2025) at roughly $50/$100/$175 respectively; the site later ran a sale bringing those to $49.99/$99.99/$175/$189.99.

As of this check (September 2026) the live product page is broken — kaizenlabs.uk returns a WordPress database error and kaizentechlabs.us returns a 403 — so current stock could not be verified directly; details here are drawn from a Wayback Machine capture from December 2025, at which point 11-22 units were shown in stock across variants (backorderable).
