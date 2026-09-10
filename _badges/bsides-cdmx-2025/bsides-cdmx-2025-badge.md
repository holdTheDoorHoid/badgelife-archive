---
title: Security BSides CDMX 2025 Badge
id: bsides-cdmx-2025-bsides-cdmx-2025-badge
layout: badge
parent: BSides Cdmx 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-cdmx-2025
year: 2025
makers:
- name: Electronic Cats
  url: https://electroniccats.com/
summary: Official conference badge for Security BSides CDMX 2025, with an OLED display, NeoPixels, AAA-battery power, and an SAO expansion connector.
functions: Runs pre-installed firmware driving the OLED display and NeoPixel LEDs; reprogrammable over its programming header/binaries. Comes in five role variants (staff, speaker, sponsor, guest, community).
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: Puya PY32F030F28U6TR
  leds:
    count: null
    type: NeoPixel
    note: ''
  display: OLED
  connectivity: []
  battery: 2x AAA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to attendees of Security BSides CDMX 2025 (July 18, 2025, Ex Fabrica MX, Mexico City); role-specific PCB variants for staff, speakers, sponsors, guests, and community.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ElectronicCats/Badge-bsides-cdmx-2025
  firmware_url: https://github.com/ElectronicCats/Badge-bsides-cdmx-2025/tree/main/firmware
  eda_tool: KiCad
  gerbers_url: null
  bom_url: null
  license: CERN-OHL-1.2 (hardware)
  fab_url: null
  notes: 'Repo includes KiCad source, board rasters, silkscreen/edge-cut SVGs per role variant, footprints, STEP models, and manufacturing outputs.'
links:
- label: github.com/badge-gallery/badge-bsides-cdmx-2025
  url: https://github.com/badge-gallery/badge-bsides-cdmx-2025
  kind: repo
- label: badge.gallery/addons/bsides-cdmx-2025-badge/oled-neopixels-aaa-power-and-sao
  url: https://badge.gallery/addons/bsides-cdmx-2025-badge/oled-neopixels-aaa-power-and-sao
  kind: website
- label: github.com/ElectronicCats/Badge-bsides-cdmx-2025
  url: https://github.com/ElectronicCats/Badge-bsides-cdmx-2025
  kind: repo
  note: Maker's own repository (the original design source; badge-gallery's copy is a mirror/listing).
images:
  - file: assets/images/badges/bsides-cdmx-2025/bsides-cdmx-2025-badge/66b44000fa.jpg
    source: "https://github.com/ElectronicCats/Badge-bsides-cdmx-2025"
    credit: "Electronic Cats"
    caption: "Community-role variant of the BSides CDMX 2025 badge PCB render"
  - file: assets/images/badges/bsides-cdmx-2025/bsides-cdmx-2025-badge/03e27c7e81.jpg
    source: "https://github.com/ElectronicCats/Badge-bsides-cdmx-2025"
    credit: "Electronic Cats"
    caption: "Staff-role variant of the BSides CDMX 2025 badge PCB render"
contact: {}
notes:
- 2025 BSides Mexico City badge with OLED display, NeoPixels, AAA power and an SAO connector. Found by the event-year sweep, task bsides-any.
- 'The sweep''s sheet used the plain title "BSides CDMX 2025 Badge"; the maker''s own README and repo title it "Security BSides CDMX 2025 Badge".'
status: released
sources:
- kind: url
  url: https://github.com/badge-gallery/badge-bsides-cdmx-2025
  title: BSides CDMX 2025 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-any); event read as ''BSides CDMX 2025''.'
- kind: url
  url: https://badge.gallery/addons/bsides-cdmx-2025-badge/oled-neopixels-aaa-power-and-sao
  title: BSides CDMX 2025 Badge - OLED, Neopixels, AAA power and SAO
  accessed: '2026-09-10'
  note: Confirmed maker (Electronic Cats), event date/venue, MCU, and open-hardware licensing.
- kind: url
  url: https://github.com/ElectronicCats/Badge-bsides-cdmx-2025
  title: Badge-bsides-cdmx-2025
  accessed: '2026-09-10'
  note: Maker's own repository; confirmed README description, license, firmware/hardware structure, and role-variant PCB renders used as images.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Confirmed via the maker''s own GitHub repo (ElectronicCats/Badge-bsides-cdmx-2025) and its badge.gallery listing. Could not find price, quantity produced, or a specific availability/resale status (likely free-drop only, not sold) — left as unknown/blank rather than guessed. No dedicated Hackaday.io page or press coverage found.'
last_modified_date: '2026-09-10'
---

The Security BSides CDMX 2025 badge was designed by Electronic Cats for the fifth edition of Security BSides CDMX, held July 18, 2025 at Ex Fabrica MX in Mexico City. It carries a Puya PY32F030F28U6TR microcontroller, an OLED display, NeoPixel RGB LEDs, a 2x AAA battery holder for standalone power, and a Shitty Add-On (SAO) connector for further expansion. The badge ships with pre-installed firmware and can be reprogrammed using the hex binaries published in the project's GitHub releases.

Rather than a single design, the badge was produced as five separate PCB variants distinguishing badge-holder roles: staff, speaker, sponsor, guest, and community — each with its own silkscreen and board files in the repository.

## Make your own

The full hardware and firmware are open source (hardware under CERN-OHL-1.2), published at github.com/ElectronicCats/Badge-bsides-cdmx-2025. The repo includes KiCad source files, per-role board rasters, silkscreen and edge-cut SVGs, footprints, STEP models, and manufacturing outputs, plus a firmware folder with its own build instructions.
