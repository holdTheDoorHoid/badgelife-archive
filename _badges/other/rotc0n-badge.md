---
title: rotc0n badge
id: other-rotc0n-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2024
makers:
- name: C0ldbru / Rot13 Labs
  url: https://rot13labs.com/
summary: A USB-C macro pad badge for rotc0n, a free no-schedule hacker gathering; solving its puzzle reveals the secret date, time and location of the event.
functions: Six mechanical keyboard keys (QMK-compatible macro pad); the default firmware is part of a puzzle that reveals rotc0n's secret time/date/location. Rot13 Labs also released alternate firmwares for a BSides Tampa 2024 afterparty and a DEFCON 32 party.
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - hardware tool
tech:
  mcu: ATmega328P
  leds:
    count: 1
    type: null
    note: single power-indicator LED, lights when plugged in via USB-C
  display: null
  connectivity:
  - usb
  battery: none, USB-powered
  sao_version: none
get_one:
  price: $60 including shipping (production version, per goimagine listing referenced by reviewer)
  price_usd: 60
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold via a goimagine.com storefront listing ("rotcon-0-badge"); that listing could not be reached to confirm current availability. The maker's GitHub README also links a joke (rickroll) URL as a second "source".
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/c0ldbru/rotc0n
  eda_tool: null
links:
- label: github.com/c0ldbru/rotc0n
  url: https://github.com/c0ldbru/rotc0n
  kind: repo
- label: 'Badge Review: rotc0n Badge by @c0ldbru | t.fish'
  url: https://tdot.fish/2024/02/28/rotc0nbadge.html
  kind: article
  archived: https://web.archive.org/web/20260802161157/https://tdot.fish/2024/02/28/rotc0nbadge.html
- label: rot13labs
  url: https://rot13labs.com/
  kind: website
  archived: https://web.archive.org/web/20260615020751/https://rot13labs.com/
images:
- file: assets/images/badges/other/rotc0n-badge/ec8bd97417.jpg
  source: https://tdot.fish/2024/02/28/rotc0nbadge.html
  credit: t.fish (badge review)
  caption: rotc0n badge, a USB-C macro pad with six keys
  archived: https://web.archive.org/web/20260802161157/https://tdot.fish/2024/02/28/rotc0nbadge.html
- file: assets/images/badges/other/rotc0n-badge/24d8b71c46.jpg
  source: https://tdot.fish/2024/02/28/rotc0nbadge.html
  credit: t.fish (badge review)
  caption: rotc0n badge, close-up view
  archived: https://web.archive.org/web/20260802161157/https://tdot.fish/2024/02/28/rotc0nbadge.html
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/c0ldbru/rotc0n
  title: rotc0n badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''unknown''.'
- kind: url
  url: https://github.com/c0ldbru/rotc0n
  title: c0ldbru/rotc0n README
  accessed: '2026-09-07'
  note: README confirms it is a QMK-compatible ATmega328P badge with three firmware variants (default rotc0n, BSides Tampa 2024 afterparty, DEFCON 32 party); flashing steps.
- kind: url
  url: https://tdot.fish/2024/02/28/rotc0nbadge.html
  title: 'Badge Review: rotc0n Badge by @c0ldbru | t.fish'
  accessed: '2026-09-07'
  note: Independent review describing rotc0n 0 as a free no-schedule con; badge is a ~2in USB-C macro pad with six Kailh Speed Pro switches, single LED, ATmega328p, $60 including shipping; two photos of the badge.
  archived: https://web.archive.org/web/20260802161157/https://tdot.fish/2024/02/28/rotc0nbadge.html
- kind: url
  url: https://rot13labs.com/
  title: rot13labs
  accessed: '2026-09-07'
  note: Maker's site, confirms rot13labs as a small Florida electronics shop making hacker tools and conference badges.
  archived: https://web.archive.org/web/20260615020751/https://rot13labs.com/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Made for "rotc0n 0", a small independent hacker gathering run by C0ldbru/Rot13 Labs (not one of the established cons in events.yml, so event is left as "other"); the badge also had alternate firmwares for BSides Tampa 2024 and DEFCON 32 afterparties. Could not confirm current storefront availability or units-made quantity; the goimagine.com listing linked from the GitHub README returned a 404 when checked. Hardware design files (schematic/PCB/gerbers) were not found, only compiled firmware .hex files in the repo.
last_modified_date: '2026-09-07'
---

The rotc0n badge is a USB-C macro pad built by C0ldbru of Rot13 Labs, a small Florida hacker-electronics shop, as the badge for rotc0n 0 — a free, no-schedule, no-talks hacker gathering the maker organized. About two inches square with six mechanical keys (Kailh Speed Pro switches on the reviewed unit; production units offered a choice of switch types and seven colors), the badge runs an ATmega328P and is fully QMK-compatible, so owners can reflash it with the included firmware files using QMK Toolbox. A single LED lights when the badge is plugged in; it draws power over USB-C and has no battery.

The default firmware doubles as a puzzle: solving it reveals rotc0n's secret date, time, and location, in keeping with the event's low-key, come-as-you-are format. Rot13 Labs later released additional firmware images for the same badge hardware — one for an unofficial rot13labs afterparty at BSides Tampa 2024, and another carrying the time, date, and location for a rotc0n party held at DEFCON 32 — turning the single badge into a reusable key for a small series of events rather than a one-off.

The badge was sold through a goimagine.com storefront listing for $60 including shipping, though that listing could not be reached during this research pass to confirm whether it is still active. Hardware design files were not published; the maker's GitHub repository contains only the README and compiled .hex firmware images.
