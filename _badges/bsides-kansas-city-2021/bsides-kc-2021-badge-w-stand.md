---
title: BSides KC 2021 Badge w/ Stand
id: bsides-kansas-city-2021-bsides-kc-2021-badge-w-stand
layout: badge
parent: BSidesKC 2021
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-kansas-city-2021
year: 2021
makers:
- name: BadgePirates
summary: The BSidesKC 2021 conference badge, sold by BadgePirates with an add-on USB-powered stand.
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: $9.99
  price_usd: 9.99
  quantity: ''
  availability: limited
  distribution:
  - purchase
  where: Sold on Tindie by BadgePirates.
make_your_own:
  open_source: true
  hardware_url: https://github.com/BadgePiratesLLC/BSidesKC_2021
  firmware_url: null
  eda_tool: KiCad
links:
- label: www.tindie.com/products/badgepirates/bsides-kc-2021-badge
  url: https://www.tindie.com/products/badgepirates/bsides-kc-2021-badge/
  kind: store
- label: github.com/BadgePiratesLLC/BSidesKC_2021
  url: https://github.com/BadgePiratesLLC/BSidesKC_2021
  kind: repo
  archived: https://web.archive.org/web/20260513190750/https://github.com/BadgePiratesLLC/BSidesKC_2021
images:
- file: assets/images/badges/bsides-kansas-city-2021/bsides-kc-2021-badge-w-stand/63c41d1c01.jpg
  source: https://www.tindie.com/products/badgepirates/bsides-kc-2021-badge/
  credit: BadgePirates
  caption: BSides KC 2021 badge with SAO connectors and USB stand accessory
contact: {}
notes:
- BSidesKC 2021 conference badge with SAO connectors and a USB-powered stand accessory (stand had power issues at release). Found by the event-year sweep, task bsides-kansas-city.
- Tindie listing wording matches the sweep's title exactly; no rename needed.
status: listed
sources:
- kind: url
  url: https://www.tindie.com/products/badgepirates/bsides-kc-2021-badge/
  title: BSides KC 2021 Badge w/ Stand
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-kansas-city); event read as ''BSidesKC 2021''.'
- kind: url
  url: https://www.tindie.com/products/badgepirates/bsides-kc-2021-badge/
  title: BSides KC 2021 Badge w/ Stand (Tindie listing)
  accessed: '2026-09-10'
  note: Confirmed maker (BadgePirates, Lee's Summit MO), price $9.99, stock note ("only 9 units remaining" at time of check), SAO connectors, USB-stand accessory description, and product photo.
- kind: url
  url: https://github.com/BadgePiratesLLC/BSidesKC_2021
  title: 'BadgePiratesLLC/BSidesKC_2021: BSides KC 2021 Files'
  accessed: '2026-09-10'
  note: Repo (archived 2022-04-08) holds KiCad source for Badge, SAO, and stand folders, confirming open hardware and KiCad as the EDA tool. No README with MCU/LED/display specs.
  archived: https://web.archive.org/web/20260513190750/https://github.com/BadgePiratesLLC/BSidesKC_2021
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Maker's own Tindie listing and GitHub repo confirm this is a real, released item, but neither source states the MCU, LED count/type, display, connectivity, battery, quantity made, or overall PCB color/shape. The GitHub repo (archived) has KiCad design files for the Badge, a matching SAO, and the stand, but no README describing the electronics. Left those tech/look fields empty rather than guess. No firmware repo was found (leaving firmware_url null); the hardware appears to be a passive/simple design given the stand-power caveat, but that is not confirmed.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsides-kansas-city-2021/bsides-kc-2021-badge-w-stand.glb
  method: kicad
  source_file: Badge/Bsides-KC.kicad_pcb
  generated: '2026-09-10'
  bytes: 279524
---

The BSidesKC 2021 badge was made and sold by BadgePirates, the Kansas City-area badge-making group behind SecKC's DEF CON party badges and several other BSidesKC editions. It shipped with SAO connectors for add-on modules and an optional USB-powered stand; per the maker's own listing, the first run of the stand had power delivery issues, with an improved version planned for later.

BadgePirates published open KiCad design files for the badge, its matching SAO, and the stand in a GitHub repository (now archived). The repo does not include a README describing the onboard electronics, so the MCU, LED configuration, and display (if any) are not documented in any source found and are left blank here rather than guessed.

At the time of the Tindie listing check, the badge was priced at $9.99 with a small remaining stock, suggesting a limited production run sold after the event rather than distributed to all attendees.

## Make your own

Full KiCad hardware source for the badge, its SAO, and the stand is on GitHub: https://github.com/BadgePiratesLLC/BSidesKC_2021 (Badge/, SAO/, and stand/ folders). No firmware source was found alongside it.
