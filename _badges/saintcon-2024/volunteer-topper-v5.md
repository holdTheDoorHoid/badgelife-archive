---
title: Volunteer Topper V5
id: saintcon-2024-volunteer-topper-v5
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: unconfirmed
summary: 'A clip-on "topper" minibadge for SAINTCON 2024 volunteers, decorated with gear and helmet artwork and lit by onboard LEDs.'
functions: 'Lights 1206 LEDs when powered through its Sidecar connector; no other interactivity found.'
look:
  colors: []
  shape: bracket/arch clip
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: '1206 SMD LEDs with matching 1206 SMD series resistors; not addressable.'
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Volunteer%20Topper%20V5
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/Volunteer%20Topper%20V5
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Volunteer%20Topper%20V5
  kind: repo
images:
- file: assets/images/badges/saintcon-2024/volunteer-topper-v5/a7033dfe88.jpg
  source: "https://github.com/utahsaint-org/MiniBadges2024/tree/main/Volunteer%20Topper%20V5"
  credit: "utahsaint-org / MiniBadges2024"
  caption: "Front silkscreen artwork of the Volunteer Topper V5 PCB, showing the gear and helmet motif"
- file: assets/images/badges/saintcon-2024/volunteer-topper-v5/51b7ccfdfa.jpg
  source: "https://github.com/utahsaint-org/MiniBadges2024/tree/main/Volunteer%20Topper%20V5"
  credit: "utahsaint-org / MiniBadges2024"
  caption: "Front copper/mask layer plot of the Volunteer Topper V5 PCB, showing the LED and sidecar-connector layout"
contact: {}
notes:
- Fifth-version volunteer 'topper' minibadge for SAINTCON 2024. Found by the event-year sweep, task saintcon-2024.
- 'The sweep''s sources list a repo folder titled "Volunteer Topper V5"; the KiCad project inside is still named "Volunteer Topper V2" even though the folder and its board footprints ("Topper v5", "Topper v5a") are versioned V5 — kept the folder/sweep title.'
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Volunteer%20Topper%20V5
  title: Volunteer Topper V5
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://api.github.com/repos/utahsaint-org/MiniBadges2024/contents/Volunteer%20Topper%20V5
  title: 'Directory listing: Volunteer Topper V5 (GitHub API)'
  accessed: '2026-09-10'
  note: 'Confirmed folder contents: KiCad PCB/schematic/footprints, SVG art, a Photoshop source file, and rendered gerber-layer PNGs; no README or BOM in the folder.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/Volunteer%20Topper%20V5/Volunteer%20Topper%20V2.kicad_pcb
  title: 'Volunteer Topper V2.kicad_pcb (raw KiCad board file)'
  accessed: '2026-09-10'
  note: 'Read the board file directly: footprints are Gears, Gears2, Helmet, Klippy1, Topper V2/v5/v5a decorative shapes, plus 3x 1206 LED, 3x 1206 resistor, and two "Saintcon 2024 Sidecar Footprint" connectors (Full_Sidecar, Top_Sidecar). No MCU footprint present.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/README.md
  title: 'utahsaint-org/MiniBadges2024 README'
  accessed: '2026-09-10'
  note: 'Repo-level README only says "Minibadges for SAINTCON 2024"; no maker/price/quantity info for this specific badge.'
- kind: url
  url: https://minibadge.wiki/2024.json
  title: 'MiniBadge Wiki 2024 data export'
  accessed: '2026-09-10'
  note: 'Checked the community wiki''s 2024 badge list for a "Volunteer Topper" entry to get maker/price/quantity/rarity; no matching title or description found.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-10'
  notes: 'Maker/designer name, price, quantity made, and availability could not be found anywhere — the GitHub repo (utahsaint-org, the SAINTCON community minibadge design-file collection) has no README, BOM, or credits for this specific folder, and the community MiniBadge Wiki''s 2024 export has no entry matching this title. Confirmed from the board file itself (not just the folder name) that this is a passive LED accessory: 3 LEDs + 3 resistors, no MCU, powered through a "Sidecar" connector (SAINTCON''s badge-to-badge header) rather than its own battery. The edge-cut outline shows a two-pronged bracket/clip shape meant to sit over the top edge of a host badge, consistent with "topper" minibadges. Soldermask/PCB color is not stated anywhere (the only visuals are black-and-white gerber-layer plots and vector art, not a colored render or photo), so look.colors is left empty. Could not confirm whether this exact badge is the SAINTCON volunteer minibadge for 2024 versus an earlier-year V2-V4 lineage reused here; the repo folder and file names suggest an iterative V2->V5 design history for the same "Volunteer Topper" line.'
last_modified_date: '2026-09-10'
---

The Volunteer Topper V5 is a clip-on "topper" minibadge made for SAINTCON 2024, part of the utahsaint-org community's `MiniBadges2024` design-file repository. Like other SAINTCON toppers, it is not a standalone badge: its edge-cut outline forms a two-pronged bracket that clips over the top edge of a host badge, and it draws power through a "Sidecar" connector (SAINTCON's badge-to-badge header) rather than carrying its own battery or MCU. The board carries three 1206 SMD LEDs with matching series resistors, and its silkscreen and cutout artwork use a recurring gear-and-helmet motif also present in the repo's separate footprint files (`Gears`, `Gears2`, `Helmet`, `Klippy1`).

No page names the designer, states a price or quantity made, or says whether/how it was distributed to volunteers; the repository itself has no README or bill of materials for this folder, and the community-run MiniBadge Wiki's 2024 badge list has no entry matching this title. The "V5" in the name, together with footprints and files labeled V2 through v5a inside the same folder, suggests this is the latest revision of a recurring "Volunteer Topper" line rather than a one-off design, but no source confirms that history explicitly.

## Make your own

KiCad schematic, PCB, and custom footprint files are published in the repo folder linked above (project name internally still reads "Volunteer Topper V2" despite the V5 folder/board revision). No firmware is applicable — the board is a passive LED accessory. No separate BOM file was found; the parts used (3x 1206 LED, 3x 1206 resistor, 2x SAINTCON Sidecar connector) were read directly out of the KiCad board file.
