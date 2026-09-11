---
title: BSides Orlando 2025 Badge
id: bsides-orlando-2025-bsides-orlando-2025-badge
layout: badge
parent: BSides Orlando 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-orlando-2025
year: 2025
makers:
- name: Jose Rodriguez
  url: https://github.com/bsidesorlando
summary: A simple, battery-powered LED badge made for BSides Orlando 2025, with a slide switch, four LEDs, and a 6-pin SAO header for plugging in accessory boards. There is no microcontroller — it is a passive blinky board rather than a programmable badge.
functions: Turns on/off via a slide switch to light four LEDs; carries a 6-pin SAO header so attendees can plug in SAOs, but has no onboard logic of its own.
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: Custom 3mm LED footprint (named "Jose_3mm_Led" in the KiCad library); color/arrangement not shown in the schematic.
  display: none
  connectivity: []
  battery: coin cell (generic "Battery_Cell" symbol in the schematic; specific cell type not labeled)
  sao_version: v2
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/bsidesorlando/2025-badge
  firmware_url: null
  eda_tool: KiCad
  fab_url: https://www.pcbway.com/project/share/BSides_Orlando_2025_Badge_Prototype_f4d9394c.html
  notes: Repo contains only bare KiCad source (bsidesorl-v1.kicad_sch/.kicad_pcb) with no README, BOM, or renders; no firmware because the board has no MCU.
links:
- label: www.pcbway.com/project/share/BSides_Orlando_2025_Badge_Prototype_f4d9394c.html
  url: https://www.pcbway.com/project/share/BSides_Orlando_2025_Badge_Prototype_f4d9394c.html
  kind: fab
- label: github.com/bsidesorlando/2025-badge
  url: https://github.com/bsidesorlando/2025-badge
  kind: repo
  archived: https://web.archive.org/web/20250920113805/https://github.com/bsidesorlando/2025-badge
images: []
contact: {}
notes:
- PCBWay-hosted prototype listing for the official BSides Orlando 2025 badge, designed by Jose Rodriguez; companion KiCad source also published at github.com/bsidesorlando/2025-badge. Found by the event-year sweep, task bsides-bsides-orlando.
- Search also surfaced github.com/sorooris/bsides-badge-2025, but that repo is a fork of bsidescz/badge-2025 (BSides Czech) with no confirmed link to BSides Orlando — not used as a source here.
status: announced
sources:
- kind: url
  url: https://www.pcbway.com/project/share/BSides_Orlando_2025_Badge_Prototype_f4d9394c.html
  title: BSides Orlando 2025 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-orlando); event read as ''bsides-orlando-2025''.'
- kind: url
  url: https://github.com/bsidesorlando/2025-badge
  title: bsidesorlando/2025-badge
  accessed: '2026-09-10'
  note: KiCad source repo (single commit "introduce badge files" by Jose Rodriguez, 2025-09-05). Schematic shows a battery, slide switch, 4 discrete LEDs, and a 6-pin (Conn_02x03) SAO header; no MCU present.
  archived: https://web.archive.org/web/20250920113805/https://github.com/bsidesorlando/2025-badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Confirmed the badge exists and is real via the maker's own GitHub org (bsidesorlando) and the matching PCBWay prototype share, both attributing it to Jose Rodriguez. The schematic establishes it as a passive (no-MCU) LED badge with a 6-pin SAO header, but no README, photos, BOM, price, quantity, or distribution details were published anywhere found. Could not confirm whether it was actually distributed at the September 27, 2025 event, so left get_one and status conservative (announced rather than released). No usable product photo was found — the PCBWay page's image gallery loads via JS/API and did not appear in the static HTML fetch.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsides-orlando-2025/bsides-orlando-2025-badge.glb
  method: kicad
  source_file: bsidesorl-v1.kicad_pcb
  generated: '2026-09-10'
  bytes: 59340
---

The BSides Orlando 2025 badge is a straightforward, passive electronic badge designed by Jose Rodriguez for the September 2025 BSides Orlando conference. Its KiCad source (published under the event's own `bsidesorlando` GitHub organization) shows a simple board with a coin-cell battery holder, a slide switch, four discrete LEDs, and a 6-pin SAO header — there is no microcontroller, so any onboard behavior is fixed rather than programmable. The badge was manufactured as a prototype through PCBWay, where the shared listing describes it as built "to spec" with good quality.

Beyond the design files and the fabrication record, no maker's writeup, photos, price, or production quantity could be found, so it's unclear how widely the badge was distributed at the event or whether it went to all attendees, a subset, or was staff/speaker-only.

## Make your own

The hardware is openly published as bare KiCad files (schematic and PCB layout, `bsidesorl-v1`) at github.com/bsidesorlando/2025-badge — no BOM, README, or gerbers are included, but the schematic and layout are enough to identify all the parts (battery holder, slide switch, 4 LEDs, and a 2x3 SAO header) and reproduce the board. There is no firmware, since the board carries no MCU.
