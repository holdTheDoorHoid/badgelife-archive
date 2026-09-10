---
title: BSides Bournemouth 2025 Skull Badge
id: bsides-bournemouth-2025-bsides-bournemouth-2025-skull-badge
layout: badge
parent: BSides Bournemouth 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-bournemouth-2025
year: 2025
series: Punk Security Skull/UFO Badge
makers:
- name: Punk Security
  url: https://github.com/punk-security
summary: A UV full-colour silkscreened, skull-shaped electronic badge with an addressable RGB LED, made by Punk Security for BSides Bournemouth 2025.
functions: Runs Arduino-style firmware (via MegaTinyCore) that drives a single addressable Neopixel LED for lighting effects, triggered/controlled with an onboard button.
look:
  colors:
  - black
  shape: skull
  themes:
  - skull
  - security
tech:
  mcu: ATtiny402
  leds:
    count: 1
    type: WS2812B
    note: Neopixel 5050 addressable RGB LED
  display: none
  connectivity:
  - uart
  inputs:
  - buttons
  battery: 2x CR2032 (surface-mount clips, 6V total)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/punk-security/bsides-bournemouth-2025-badge/tree/main/eagle-files
  firmware_url: https://github.com/punk-security/bsides-bournemouth-2025-badge/blob/main/bsides-bournemouth-2025-badge.ino
  gerbers_url: https://github.com/punk-security/bsides-bournemouth-2025-badge/blob/main/gerber-files.zip
  eda_tool: EasyEDA
  notes: PCB was designed first in AutoCAD EAGLE (schematic/board files provided), then exported for fabrication at JLCPCB via EasyEDA. Firmware is written for the Arduino IDE using MegaTinyCore, flashed over UPDI through the SAO connector.
links:
- label: github.com/punk-security/bsides-bournemouth-2025-badge
  url: https://github.com/punk-security/bsides-bournemouth-2025-badge
  kind: repo
images:
- file: assets/images/badges/bsides-bournemouth-2025/bsides-bournemouth-2025-skull-badge/94eda2c821.png
  source: https://github.com/punk-security/bsides-bournemouth-2025-badge
  credit: Punk Security
  caption: The assembled skull badge PCB with UV full-colour silkscreen
- file: assets/images/badges/bsides-bournemouth-2025/bsides-bournemouth-2025-skull-badge/f657cb5d94.jpg
  source: https://github.com/punk-security/bsides-bournemouth-2025-badge
  credit: Punk Security
  caption: Silkscreen artwork for the skull badge as ordered from JLCPCB
contact: {}
notes:
- Official electronic PCB skull badge sponsored/made by Punk Security for BSides Bournemouth's 2025 edition. Found by the event-year sweep, task bsides-any.
- Punk Security's README says the bill of materials is shared with their BSides Cheltenham 2024 badge ("this is the list for the BSIDES Cheltenham 2024 badge, but it is the same bits"), and the firmware file even carries a leftover reference to a "bsides-cheltenham-2024-badge.ino" filename in its setup instructions - this appears to be one board in a recurring series of similarly-built Punk Security con badges (Cheltenham 2024 UFO badge is already a separate archive entry). Price, quantity made, and availability/distribution (e.g. sponsor giveaway vs. sold) are not stated anywhere in the repo and were left empty.
status: listed
sources:
- kind: url
  url: https://github.com/punk-security/bsides-bournemouth-2025-badge
  title: BSides Bournemouth 2025 Skull Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-any); event read as ''BSides Bournemouth 2025''.'
- kind: url
  url: https://github.com/punk-security/bsides-bournemouth-2025-badge/blob/main/README.md
  title: 'punk-security/bsides-bournemouth-2025-badge: README'
  accessed: '2026-09-10'
  note: Confirmed maker, event, MCU (ATtiny402), LED (Neopixel 5050/WS2812B-compatible), battery (2x CR2032), button, UV full-colour silkscreen, EAGLE/EasyEDA/JLCPCB fabrication, and MegaTinyCore/Arduino firmware flashed via UPDI over the SAO connector. Also notes the BOM is shared with the BSides Cheltenham 2024 badge.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Maker's own GitHub repo (code, gerbers, EAGLE files, README) confirms the badge exists and gives hardware/firmware detail. No storefront, price, quantity, or distribution info was found anywhere (likely a free sponsor giveaway at the con, but that is not stated, so left as unknown/empty rather than guessed). No SAO header pinout is documented beyond "SAO connector for programming," so sao_version was left null.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsides-bournemouth-2025/bsides-bournemouth-2025-skull-badge.glb
  method: kicad
  source_file: main.brd
  generated: '2026-09-10'
  bytes: 32272
---

Punk Security built this UV full-colour silkscreened, skull-shaped electronic badge for BSides Bournemouth's 2025 edition. It is a small standalone board powered by an ATtiny402 microcontroller, with a single Neopixel 5050 (WS2812B-compatible) addressable RGB LED and a surface-mount button, running on two CR2032 coin cells wired through surface-mount clips for 6V of headroom. The board is programmed and flashed over UPDI through its SAO connector, using Arduino IDE firmware built on MegaTinyCore.

The badge appears to be one entry in a recurring line of similarly-built Punk Security conference badges: the project's own bill-of-materials notes it reuses the parts list from their BSides Cheltenham 2024 badge ("the same bits"), and the firmware's setup instructions still reference a "bsides-cheltenham-2024-badge.ino" filename left over from that earlier design. No pricing, production quantity, or distribution details (sold vs. given away) were published in the repository or found elsewhere.

## Make your own

The full design is open source: AutoCAD EAGLE schematic/board files, a gerber-files.zip ready to upload directly to JLCPCB, the original skull.svg vector artwork, the ordered skull.png silkscreen, and the Arduino .ino firmware are all in the GitHub repo. Building one requires an ATtiny402, a compatible surface-mount button, two surface-mount CR2032 clips, and a Neopixel 5050 LED (the maker stresses getting the correct LED variant). Firmware is flashed via the Arduino IDE (pre-v2) using MegaTinyCore and a UPDI programmer wired to the SAO connector's 3V3/GND/UPDI-RxD pins.
