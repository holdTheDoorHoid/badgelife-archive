---
title: BornHack 2025 badge
id: bornhack-2025-bornhack-2025-badge
layout: badge
parent: Bornhack 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bornhack-2025
year: 2025
makers:
- name: BornHack
  url: https://github.com/bornhack
- name: Thomas Flummer
summary: A large, Ø-shaped (circular with a slash, the Danish letter O) LoRa experimentation badge for BornHack 2025, built around an ESP32-C3 and an 868MHz SX1262 LoRa module, preloaded with Meshtastic mesh-networking firmware.
functions: Runs as a Meshtastic mesh-network node out of the box, configurable via the Meshtastic smartphone app over Bluetooth. Front face shows the BornHack logo and a row of backlit status icons; the rear holds the electronics and battery holders.
look:
  colors:
  - white
  shape: circle
  themes:
  - radio
  - logo
tech:
  mcu: ESP32-C3
  leds:
    count: 5
    type: RGB
    note: Five RGB LEDs mounted along the side of the board.
  display: none
  connectivity:
  - lora
  - wifi
  - bluetooth
  - i2c
  battery: 2x AA
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to attendees at BornHack 2025 (Denmark); exact distribution method/price not stated in available sources.
make_your_own:
  open_source: true
  hardware_url: https://github.com/bornhack/badge2025
  firmware_url: https://github.com/bornhack/badge2025
  eda_tool: KiCad
  notes: Hardware released under CC BY-SA 4.0. Repo includes KiCad v9 design files, a schematic PDF, and an OpenSCAD 3D-printable case (closed and wall-mount variants). Ships preinstalled with Meshtastic firmware rather than custom firmware.
links:
- label: github.com/bornhack/badge2025
  url: https://github.com/bornhack/badge2025
  kind: repo
- label: 'Hackaday: Two For The Price Of One: BornHack 2024 And 2025 Badges'
  url: https://hackaday.com/2025/08/01/two-for-the-price-of-one-bornhack-2024-and-2025-badges/
  kind: article
images:
- file: assets/images/badges/bornhack-2025/bornhack-2025-badge/dea28a270d.jpg
  source: https://github.com/bornhack/badge2025
  credit: BornHack / Thomas Flummer
  caption: BornHack 2025 badge, an Ø-shaped LoRa/Meshtastic board with ESP32-C3
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/bornhack/badge2025
  title: BornHack 2025 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''bornhack-2025''.'
- kind: url
  url: https://github.com/bornhack/badge2025
  title: bornhack/badge2025 README and repo contents
  accessed: '2026-09-07'
  note: Primary source for MCU, LEDs, connectivity, SAO version, open-source status, KiCad tooling, and image.
- kind: url
  url: https://hackaday.com/2025/08/01/two-for-the-price-of-one-bornhack-2024-and-2025-badges/
  title: 'Two For The Price Of One: BornHack 2024 And 2025 Badges'
  accessed: '2026-09-07'
  note: Confirmed shape/color (white, Ø-shaped), battery (2x AA), status icons/logo layout, designer name (Thomas Flummer), and that it pairs with the 2024 badge to spell "10" for the camp's 10th year.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched both cited sources (bornhack/badge2025 GitHub repo, Hackaday article) and confirmed MCU, LED count, connectivity, battery, SAO version, EDA tool, open-source license, and body claims against them. The saved board photo carries the repo''s own "BornHack 2025 Circle Badge / Design: hxr.social/@thomasflummer / Files: github.com/bornhack/badge2025 / License: CC-BY-SA" caption printed on the PCB silkscreen, confirming it is this item from that source. Removed `get_one.distribution: [purchase]`, which no source supported (the entry''s own `where` text says distribution method is unstated) -- set to empty. Price, exact quantity made, and distribution method remain unconfirmed. The companion BornHack 2024 badge (which pairs with this one to spell "10") is a separate item and may deserve its own entry.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/bornhack-2025/bornhack-2025-badge.glb
  method: kicad
  source_file: circle-badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 366068
---

The BornHack 2025 badge is a large, white, Ø-shaped circuit board — a nod to the Danish letter that also stands in for BornHack's home country — designed by Thomas Flummer for the 2025 edition of the Danish hacker camp. At its core is an ESP32-C3 paired with an 868MHz SX1262 LoRa module, and it ships preloaded with Meshtastic node firmware, letting attendees join the camp's mesh network out of the box and reconfigure it later through the Meshtastic mobile app over Bluetooth. Five side-mounted RGB LEDs, a Qwiic/StemmaQT connector, and a SAO v1.69bis footprint round out the expansion options. The front carries the BornHack logo and a strip of backlit status icons, while the back holds the electronics and a pair of AA battery holders alongside a PCB antenna and a bundled stick-on Molex antenna.

The badge was designed to be read alongside BornHack's 2024 badge: placed together, the two boards spell out "10," marking the camp's tenth iteration. Hardware design files (KiCad v9), a schematic PDF, and an OpenSCAD 3D-printable case are published in the project's GitHub repository under a CC BY-SA 4.0 license.

## Make your own

Hardware and case files are open in the `bornhack/badge2025` GitHub repository: clone it for the KiCad v9 project and schematic PDF, and use the included OpenSCAD files to 3D print either a fully enclosed case or a wall-mount variant. The board ships with Meshtastic firmware pre-flashed, so no separate firmware build is needed to get mesh networking working; the Meshtastic app is used for configuration.
