---
title: eh21badge
id: easterhegg-2024-eh21badge-easterhegg-2024-rca-badge
layout: badge
parent: Easterhegg 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: easterhegg-2024
year: 2024
makers:
- name: x70b1
  url: https://github.com/x70b1
summary: A build-it-yourself badge for Easterhegg 2024's "Rabbit Chaos Adventure" (RCA) puzzle hunt, shaped from several rabbit-form PCB pieces and built around a dual-timer blinking circuit that hid puzzle answers in its component values.
functions: Blinks LEDs at a tuned interval (the exact frequency and one LED's color were themselves puzzle answers in the RCA hunt); the badge fiction describes it as creating "random snapshots of the environment" for the story's protagonist.
look:
  colors:
  - black
  shape: rabbit
  themes:
  - animal
  - puzzle
  - ctf
  - wearable
tech:
  mcu: 'none (NE556 dual timer IC, SOP-14)'
  leds:
    count: null
    type: discrete
    note: 'BOM lists individually-driven through-hole/1206 LEDs across designators D1-D16 in yellow, red, green-yellow and white; exact populated count not confirmed from public sources.'
  display: none
  connectivity: []
  battery: AAA (SMD battery holder in the BOM)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/x70b1/eh21badge/tree/main/Schematics
  firmware_url: null
  eda_tool: null
  gerbers_url: https://github.com/x70b1/eh21badge/tree/main/Gerbers
  bom_url: https://github.com/x70b1/eh21badge/tree/main/Parts
  notes: 'Repo also includes 3D-print files for the badge''s rabbit-shaped enclosure pieces (Arm, Back, Badge, Head, Hood).'
links:
- label: github.com/x70b1/eh21badge
  url: https://github.com/x70b1/eh21badge
  kind: repo
- label: RCA closing talk (media.ccc.de)
  url: https://media.ccc.de/v/eh21-14-rabbit-chaos-adventure-closing
  kind: video
- label: Rabbit Radio coverage of Easterhegg/RCA
  url: https://rabbitradio.de/highlights/easterhegg/
  kind: article
images:
- file: assets/images/badges/easterhegg-2024/eh21badge-easterhegg-2024-rca-badge/15829056c2.jpg
  source: "https://github.com/x70b1/eh21badge"
  credit: "x70b1"
  caption: "The eh21badge rabbit-shaped PCB pieces (arm, back, badge, head, hood)"
contact: {}
notes:
- Custom PCB conference badge for Easterhegg 2024 in Regensburg built around a 'Rabbit Chaos Adventure' gamified puzzle narrative. Found by the event-year sweep, task ccc-adjacent.
- 'The discovery sweep titled the entry "eh21badge (Easterhegg 2024 RCA Badge)"; the maker''s repo names the project simply "eh21badge", used here as the title.'
status: listed
sources:
- kind: url
  url: https://github.com/x70b1/eh21badge
  title: eh21badge (Easterhegg 2024 RCA Badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:ccc-adjacent); event read as ''Easterhegg 2024''.'
- kind: url
  url: https://github.com/x70b1/eh21badge
  title: x70b1/eh21badge README
  accessed: '2026-09-08'
  note: 'Confirmed project is a real, built badge for Easterhegg 2024''s Rabbit Chaos Adventure puzzle hunt; README story text describes the badge''s blinking function, a battery, resistor/LED puzzle steps, and a "simple IC".'
- kind: url
  url: https://raw.githubusercontent.com/x70b1/eh21badge/main/Parts/LCSC_Exported__20240402_211420.csv
  title: eh21badge BOM (LCSC export)
  accessed: '2026-09-08'
  note: 'Identified the main IC as an NE556 dual timer (SOP-14), an SMD AAA battery holder, multiple LED colors (yellow/red/green-yellow/white), and a DPDT slide switch.'
- kind: url
  url: https://media.ccc.de/v/eh21-14-rabbit-chaos-adventure-closing
  title: RCA closing talk
  accessed: '2026-09-08'
  note: 'Listed as a related link in the maker''s README; not fetched in full (video).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Maker''s own repo (README, schematics, Gerbers, BOM, 3D-print files) confirms the badge exists and was built for Easterhegg 2024''s Rabbit Chaos Adventure. Could not confirm price, quantity made, or distribution method (badge appears to have been self-built by participants as part of the puzzle rather than sold/handed out, but no source states this explicitly, so get_one fields are left empty). Exact populated LED count and total resistor/LED designators are listed in the BOM CSVs but not stated as a single count anywhere, so tech.leds.count is left null rather than tallied by hand from ambiguous BOM rows. No maker storefront, Hackaday.io page, or press coverage beyond the two linked German-language sources was found.'
last_modified_date: '2026-09-08'
---

The eh21badge is a self-built conference badge created by x70b1 for Easterhegg 2024, held at OTH Regensburg, tying into that year's "Rabbit Chaos Adventure" (RCA) puzzle narrative that ran through the conference. The badge itself is a supporting prop in the story: its blinking LED pattern, a specific LED's color, a resistor's value, and the output count of its main chip were all puzzle answers participants had to extract by inspecting the hardware.

Electrically the badge is deliberately old-school rather than microcontroller-based: the BOM centers on an NE556 dual 555 timer IC driving a field of discrete LEDs (yellow, red, green-yellow, and white) through transistor drivers, powered from AAA batteries, with a DPDT slide switch. The enclosure is a set of separate PCB pieces shaped and named for parts of a rabbit (Arm, Back, Badge, Head, Hood), matching the RCA rabbit theme.

The hardware is fully open source: the GitHub repository includes schematics, Gerber files, a BOM/parts export from LCSC, and 3D-print files for the rabbit-shaped pieces. No pricing, production quantity, or distribution details (sold, kitted, or freely built by attendees) were found in the available sources.

## Make your own

The repo (github.com/x70b1/eh21badge) provides everything needed to reproduce the badge: schematics and Gerbers under `Schematics/` and `Gerbers/`, a bill of materials as LCSC CSV exports under `Parts/`, and enclosure 3D-print files under `3dprints/` for the rabbit-shaped arm, back, badge, head, and hood pieces.
