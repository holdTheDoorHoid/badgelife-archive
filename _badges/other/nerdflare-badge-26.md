---
title: NerdFlare Badge 26
id: other-nerdflare-badge-26
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2026
series: NerdFlare Badge
makers:
- name: NerdFlare
  url: https://nerdflare.github.io
summary: The 2025-26 club/team badge of NerdFlare, a Cal Poly (San Luis Obispo) student club "dedicated to making art from technology." It runs CircuitPython, carries a level-based game mode, and continues an annual team-badge series the club started with NerdFlareBadge25.
functions: Runs a "sparkle" LED animation mode and a "game" mode that tracks a saved progress level (settings persisted to onboard storage as JSON); colors are shuffled per-badge using the microcontroller's unique ID as a random seed.
look:
  colors: []
  shape: null
  themes:
  - logo
tech:
  mcu: null
  leds:
    count: null
    type: NeoPixel
    note: Addressable NeoPixels plus separate discrete/digital LEDs driven directly by GPIO; animations built with adafruit_led_animation (RainbowComet, SparklePulse).
  display: none
  connectivity:
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Made for NerdFlare's own club members, not sold to the public.
make_your_own:
  open_source: true
  hardware_url: https://github.com/NerdFlare/NerdFlareBadge26/tree/main/pcb
  firmware_url: https://github.com/NerdFlare/NerdFlareBadge26/tree/main/code
  eda_tool: KiCad
links:
- label: github.com/NerdFlare/NerdFlareBadge26
  url: https://github.com/NerdFlare/NerdFlareBadge26
  kind: repo
- label: Cal Poly NerdFlare (club site)
  url: https://nerdflare.github.io
  kind: website
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- This is an internal club/team badge, not a con-specific badge sold or distributed at an event; it was not something available "to buy."
status: released
sources:
- kind: url
  url: https://github.com/NerdFlare/NerdFlareBadge26
  title: NerdFlare Badge 26
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/NerdFlare/NerdFlareBadge26/main/code/code.py
  title: NerdFlareBadge26 code.py (CircuitPython firmware)
  accessed: '2026-09-07'
  note: Confirms CircuitPython firmware, NeoPixel + digital LEDs, a sparkle mode and a game mode with a saved progress level, and per-badge color shuffling seeded from the MCU's unique ID.
- kind: url
  url: https://api.github.com/orgs/NerdFlare
  title: NerdFlare GitHub organization
  accessed: '2026-09-07'
  note: Identifies NerdFlare as "Cal Poly NerdFlare," a student organization.
- kind: url
  url: https://nerdflare.github.io
  title: Cal Poly NerdFlare club site
  accessed: '2026-09-07'
  note: Describes NerdFlare as a Cal Poly club "dedicated to making art from technology"; also links their other SAO/badge projects (SAO library, iFixit DEFCON 2026 SAO, sparky-sao-display, solder challenge).
- kind: url
  url: https://api.github.com/repos/NerdFlare/NerdFlareBadge26/contents/pcb
  title: NerdFlareBadge26 repo /pcb contents
  accessed: '2026-09-07'
  note: Confirms KiCad hardware design files (schematic, PCB, footprint library) but no BOM/README naming the MCU part.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'NerdFlareBadge26 is the 2025-26 team/club badge of NerdFlare, a Cal Poly San Luis Obispo student club ("dedicated to making art from technology") that also makes SAOs and other badgelife projects (an SAO footprint/symbol library, an iFixit DEFCON 2026 SAO, the "sparky-sao-display", and an annual NerdFlare Soldering Challenge). It continues a series that began with NerdFlareBadge25 (2024-25 AY). The repo (art/code/pcb folders) has no README or BOM, so the exact MCU, LED count, colorway, price, quantity, and distribution could not be confirmed; firmware imports point to a CircuitPython-capable microcontroller driving NeoPixels and separate digital LEDs. No photo of NerdFlareBadge26 itself was found (the club''s gallery site currently only shows photos of the prior year''s NerdFlareBadge25); GitHub''s repo social-preview image is a generic OG card, not a badge photo, so no image was saved. Not sold to the public as far as sources indicate, so this does not match the sheet''s framing
    as something "to buy." Event kept as "other": this is a club badge, not made for a specific hacker convention, so no events.yml id applies.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/nerdflare-badge-26.glb
  method: kicad
  source_file: pcb/NerdFlareBadge26.kicad_pcb
  generated: '2026-09-10'
  bytes: 243144
---

NerdFlareBadge26 is the 2025-26 academic-year team badge of NerdFlare, a student club at Cal Poly San Luis Obispo that describes itself as being "dedicated to making art from technology." It's the latest entry in an annual internal badge series that started with NerdFlareBadge25 the year before, made for the club's own members rather than sold or distributed at a convention.

The badge runs CircuitPython firmware built around Adafruit's LED animation library. It drives a set of addressable NeoPixels alongside separate discrete LEDs, offering a "sparkle" animation mode and a "game" mode that tracks a saved progress level in an onboard settings file. Each badge shuffles its accent colors differently by seeding the shuffle from the microcontroller's own unique hardware ID, so no two units animate quite the same way. The KiCad hardware files, CircuitPython source, and badge artwork (edge cut, silkscreen, and soldermask SVGs) are all published in the project's GitHub repository, though it lacks a README or bill of materials, so the specific MCU part, LED count, and other hardware specifics couldn't be pinned down from available sources.

NerdFlare is active in the wider badgelife/SAO community beyond this one badge: the same GitHub organization hosts a reusable SAO footprint/symbol library, an "iFixit DEFCON 2026 SAO," a 13-badge SAO display board nicknamed "Sparky," and a recurring NerdFlare Soldering Challenge. No photos of NerdFlareBadge26 itself turned up during research — the club's gallery website currently shows only images of the previous year's badge (NerdFlareBadge25) — so this entry has no images of the item.
