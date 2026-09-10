---
title: WHY 2025 Badge
id: why-2025-why-2025-badge
layout: badge
parent: Why 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: why-2025
year: 2025
makers:
- name: WHY 2025 badge team (organizers, name unspecified after mass resignation)
summary: The official electronic badge for WHY (What Hackers Yearn) 2025, a Dutch/European hacker camp near Alkmaar, built around an ESP32-P4 and a LoRa radio for mesh networking, backwards-compatible with earlier Dutch camp badges.
functions: Runs an app store and supports installable community apps; backwards compatible with previous Dutch hacker-camp badges; used with MeshCore/LoRa mesh firmware for off-grid messaging between attendees.
look:
  colors: []
  shape: null
  themes:
  - radio
tech:
  mcu: ESP32-P4
  leds: null
  display: null
  connectivity:
  - lora
  battery: 2x 18650 (unprotected cells)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/kaistierl/why2025-badge-firmware
  eda_tool: null
links:
- label: hackaday.com/2025/08/12/when-a-badge-misses-the-mark-why-2025
  url: https://hackaday.com/2025/08/12/when-a-badge-misses-the-mark-why-2025/
  kind: article
- label: kaistierl/why2025-badge-firmware (GitHub)
  url: https://github.com/kaistierl/why2025-badge-firmware
  kind: repo
- label: zebreus/why2025-badge-rust (GitHub, BadgeVMS/Rust support)
  url: https://github.com/zebreus/why2025-badge-rust
  kind: repo
  archived: https://web.archive.org/web/20251107113207/https://github.com/zebreus/why2025-badge-rust
- label: RevSpace WHY2025 project (Metameeting notes)
  url: https://revspace.nl/index.php?search=WHY2025+badge&title=Speciaal:Zoeken&fulltext=1
  kind: doc
images:
- file: assets/images/badges/why-2025/why-2025-badge/345a16cb22.jpg
  source: https://hackaday.com/2025/08/12/when-a-badge-misses-the-mark-why-2025/
  credit: Hackaday
  caption: PCB layout of the WHY 2025 badge showing the LoRa header and the battery pads at the center of the fire-safety report
- file: assets/images/badges/why-2025/why-2025-badge/6c1ef0bf86.jpg
  source: https://hackaday.com/2025/08/12/when-a-badge-misses-the-mark-why-2025/
  credit: Hackaday
  caption: The unprotected 18650 cell supplied with the WHY 2025 badge, with fire safety warning label
contact: {}
notes:
- Notable for 18650 battery safety issue (unprotected cells, tight trace spacing) covered by RevSpace
status: released
sources:
- kind: url
  url: https://hackaday.com/2025/08/12/when-a-badge-misses-the-mark-why-2025/
  title: WHY 2025 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''WHY (What Hackers Yearn) 2025''.'
- kind: url
  url: https://hackaday.com/2025/08/12/when-a-badge-misses-the-mark-why-2025/
  title: 'When A Badge Misses The Mark: WHY 2025'
  accessed: '2026-09-07'
  note: Confirmed event (WHY 2025, hacker camp near Alkmaar, Netherlands), ESP32 MCU, 2x unprotected 18650 cells, the fire-safety controversy and organizers' epoxy-coating fix; provided the two saved images.
- kind: url
  url: https://github.com/kaistierl/why2025-badge-firmware
  title: kaistierl/why2025-badge-firmware
  accessed: '2026-09-07'
  note: Community firmware repo confirming the badge is ESP32-P4 based, with a display/windowing system and keyboard input.
- kind: url
  url: https://github.com/zebreus/why2025-badge-rust
  title: zebreus/why2025-badge-rust
  accessed: '2026-09-07'
  note: Rust/BadgeVMS support package targeting the badge; corroborates the RISC-V-based ESP32-P4 (riscv32imafc target).
  archived: https://web.archive.org/web/20251107113207/https://github.com/zebreus/why2025-badge-rust
- kind: url
  url: https://revspace.nl/index.php?search=WHY2025+badge&title=Speciaal:Zoeken&fulltext=1
  title: 'RevSpace search: WHY2025 badge'
  accessed: '2026-09-07'
  note: RevSpace metameeting notes mention ongoing "maintenance en feature fixes aan de WHY2025-badge" and "MeshCore UI" work, indicating a LoRa/MeshCore mesh-networking feature; the dedicated RevSpace WHY2025 wiki page itself is empty.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (event, ESP32-P4 MCU, 2x unprotected 18650 batteries, the fire-safety story) are corroborated across Hackaday and two independent community firmware repos, but no official maker/team page, price, quantity, LED count, display spec, or design-file repo could be found -- the original badge team resigned mid-cycle and no single canonical project page surfaced. Left get_one fields, tech.leds, and tech.display empty rather than guess. hardware_url left null: no schematic/PCB source repo was found, only firmware.'
last_modified_date: '2026-09-07'
---

The WHY 2025 badge was the official electronic conference badge for WHY (What Hackers Yearn) 2025, a European hacker camp held near Alkmaar in the Netherlands. It shipped built around an Espressif ESP32-P4 microcontroller and included a LoRa radio, used by the community for MeshCore-based off-grid mesh messaging between attendees. Development was disrupted after the original badge team resigned early in the production cycle following disagreements with the event organizers, and a replacement team finished the badge under a compressed schedule.

The badge became notable for a fire-safety controversy rather than its features: it shipped with two unprotected 18650 lithium cells, and RevSpace hackerspace reported that battery contact pads were undersized for their footprint and that the gap between positive and negative battery traces on the PCB was dangerously tight, protected only by soldermask. The organizers responded with a printed disclaimer leaflet warning against misuse and applied a last-minute epoxy coating to affected boards; attendees also produced 3D-printed protective cases and were advised to use external, protected power banks instead of the bare cells.

No single official project page or storefront for the badge could be located; instead, a scattered set of community firmware repositories (targeting the ESP32-P4 in C and in Rust via a "BadgeVMS" toolchain) and RevSpace hackerspace notes describe ongoing maintenance and feature work, including a MeshCore mesh-networking UI. Price, production quantity, LED configuration, and display specifications were not found in any source reviewed and are left blank rather than guessed.
