---
title: BSides San Diego 2025 Badge
id: bsides-san-diego-2025-bsides-san-diego-2025-badge
layout: badge
parent: BSides San Diego 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-san-diego-2025
year: 2025
makers:
- name: Electronic Cats
  url: https://electroniccats.com/
summary: The official conference badge for BSides San Diego 2025, an open-source PCB badge built by Electronic Cats around a CH32V003 microcontroller with an OLED display.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - security
  - village badge
tech:
  mcu: CH32V003
  leds: null
  display: OLED
  connectivity: []
  battery: 2x AAA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/ElectronicCats/badge-bsides-sandiego-2025
  firmware_url: null
  eda_tool: KiCad
  license: CERN-OHL-1.2
links:
- label: github.com/ElectronicCats/badge-bsides-sandiego-2025
  url: https://github.com/ElectronicCats/badge-bsides-sandiego-2025
  kind: repo
images: []
contact: {}
notes:
- Open-source official conference badge for BSides San Diego 2025 built by Electronic Cats around a CH32V003 MCU with OLED display, LEDs, 2xAAA holder and an SAO connector, released under CERN-OHL-1.2. Found by the event-year sweep, task bsides-bsides-san-diego.
status: listed
sources:
- kind: url
  url: https://github.com/ElectronicCats/badge-bsides-sandiego-2025
  title: BSides San Diego 2025 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-san-diego); event read as ''BSides San Diego 2025''.'
- kind: url
  url: https://github.com/ElectronicCats/badge-bsides-sandiego-2025/blob/main/README.md
  title: Badge bsides San Diego 2025 (README)
  accessed: '2026-09-10'
  note: Confirms maker, CH32V003 MCU, LEDs, OLED display, 2x AAA battery holder, SAO ("Shitty Addon Connector"), and CERN-OHL-1.2 hardware license. No price, quantity, or availability given.
- kind: url
  url: https://www.linkedin.com/posts/-brewer_github-electroniccatsbadge-bsides-sandiego-activity-7315429176998514691-nFL7
  title: LinkedIn post announcing the badge repo release
  accessed: '2026-09-10'
  note: Third-party confirmation that Electronic Cats released this badge's repo for BSides San Diego; no additional technical detail or photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: The maker's GitHub repo and README confirm the core facts already in the sweep notes (CH32V003, OLED, LEDs, 2x AAA, SAO connector, CERN-OHL-1.2). Could not find price, quantity made, availability/distribution, LED count/type, SAO connector version, or any photo of the physical badge (the repo has no image assets; only a generic GitHub social-card og:image was found, not a photo of the item, so no images were saved). Note that BSides San Diego's own site currently promotes a different "Cyberpunk Bunny" ESP32 badge described as this year's badge challenge, which appears to be a distinct (likely 2026) item, not this one; that Electronic Cats CH32V003 badge is unambiguously tied to the 2025 event by the repo name and README title.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsides-san-diego-2025/bsides-san-diego-2025-badge.glb
  method: kicad
  source_file: hardware/Bsides_sandiego_2025.kicad_pcb
  generated: '2026-09-10'
  bytes: 139456
---

The BSides San Diego 2025 badge is an open-source hardware conference badge designed by Electronic Cats for the 2025 edition of BSides San Diego. It is built around a CH32V003 RISC-V microcontroller and includes an OLED display and LEDs, runs on a 2x AAA battery holder, and carries a "Shitty Addon Connector" (SAO) header so attendees could plug in add-on boards.

Electronic Cats published the full hardware design on GitHub, generated from their standard KiCad CI template, and released it under the CERN Open Hardware Licence v1.2, continuing their pattern of releasing conference badge designs as open hardware. Beyond the repository and a brief LinkedIn announcement of its release, no pricing, production quantity, or distribution details were found, and no photos of the assembled badge were located.

## Make your own

The KiCad hardware source is published in full at the GitHub repository linked above, released under CERN-OHL-1.2. No separate firmware repository, Gerber/fab share link, or bill of materials was found.
