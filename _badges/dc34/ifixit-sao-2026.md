---
title: 2026 iFixit SAO
id: dc34-ifixit-sao-2026
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: iFixit
  url: https://github.com/NerdFlare
- name: Cal Poly NerdFlare club
  url: https://github.com/NerdFlare
- name: znjp
  role: artist
summary: PCB-art SAO shaped like a raised fist holding a soldering iron, made for DEF CON 2026 (DC34) as a collaboration between iFixit, the Cal Poly NerdFlare club and artist znjp; an ATtiny1604 drives seven SK6805-EC15 addressable LEDs along the iron shaft, a red 0402 tip LED and two SunLED reverse-mount lightning-bolt LEDs (10 LEDs total), with Off/Candle/Propane animation modes plus a locked mode unlocked by soldering four 0-ohm resistors (1206/0805/0603/0402) onto challenge footprints, and the firmware is a PlatformIO/Arduino project programmable over UPDI.
functions: Off, Candle and Propane animation modes on the shaft LEDs, selectable via the firmware; the two lightning-bolt LEDs animate continuously regardless of the selected mode; soldering four 0-ohm resistors (1206, 0805, 0603 and 0402 packages) onto marked challenge footprints unlocks a bonus fourth animation mode.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
  - puzzle
tech:
  mcu: ATtiny1604
  leds:
    count: 10
    type: mixed
    note: Seven SK6805-EC15 addressable LEDs (LED1-LED7) along the iron shaft, one red 0402 LED (D3) at the tip, and two SunLED XZM2CYK45WT-9 reverse-mount gull-wing LEDs (D1, D2) forming the lightning bolt.
  display: null
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
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/NerdFlare/iFixit-SAO-2026/tree/main/pcb
  firmware_url: https://github.com/NerdFlare/iFixit-SAO-2026/tree/main/code
  eda_tool: KiCad
links:
- label: github.com/NerdFlare/iFixit-SAO-2026
  url: https://github.com/NerdFlare/iFixit-SAO-2026
  kind: repo
- label: raw.githubusercontent.com/NerdFlare/iFixit-SAO-2026/HEAD/README.md
  url: https://raw.githubusercontent.com/NerdFlare/iFixit-SAO-2026/HEAD/README.md
  kind: website
images:
- file: assets/images/badges/dc34/ifixit-sao-2026/074e353728.jpg
  source: https://github.com/NerdFlare/iFixit-SAO-2026
  credit: iFixit / Cal Poly NerdFlare / znjp
  caption: The assembled iFixit 2026 SAO, a fist holding a soldering iron with addressable LEDs along the shaft
- file: assets/images/badges/dc34/ifixit-sao-2026/264b2efe90.jpg
  source: https://github.com/NerdFlare/iFixit-SAO-2026
  credit: iFixit / Cal Poly NerdFlare / znjp
  caption: The soldering challenge footprints (four 0-ohm resistor pads) that unlock the bonus animation mode
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/NerdFlare/iFixit-SAO-2026
  title: NerdFlare/iFixit-SAO-2026 — iFixit DEFCON 2026 SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://raw.githubusercontent.com/NerdFlare/iFixit-SAO-2026/HEAD/README.md
  title: iFixit-SAO-2026 README
  accessed: '2026-09-07'
  note: Full build details - makers, chip, LED breakdown, animation modes, soldering challenge, open-source file layout (art/code/pcb), EDA tool.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's own repo and README confirm all core technical facts. Price, quantity made, and distribution/availability were not stated anywhere in the repo and could not be found via search, so those fields are left empty. No press coverage or storefront listing was found; this appears to be a give-away/learn-to-solder style SAO distributed at DEF CON 34 rather than a store item, but that distribution method is not explicitly confirmed by a source, so get_one.distribution is left empty rather than guessed. Not the same item as dc34-badgelife-village-saos (a separate three-level learn-to-solder kit series sponsored by iFixit but designed by Ozma of Oz and the GhostGlitch team).
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc34/ifixit-sao-2026.glb
  method: kicad
  source_file: pcb/iFixit-SAO-2026.kicad_pcb
  generated: '2026-09-07'
  bytes: 195000
---

The 2026 iFixit SAO is a PCB-art Shitty Add-On shaped like a raised fist gripping a soldering iron, made for DEF CON 34 as a joint project between iFixit, the Cal Poly NerdFlare club, and artist znjp. An ATtiny1604 microcontroller drives ten LEDs total: seven SK6805-EC15 addressable LEDs run up the iron's shaft, a single red 0402 LED lights the tip, and two SunLED XZM2CYK45WT-9 reverse-mount LEDs form a lightning bolt that animates continuously no matter which mode is selected. The shaft LEDs cycle through Off, Candle, and Propane animation modes.

Beyond the built-in modes, the board doubles as a soldering exercise: four unpopulated footprints for 0-ohm resistors, in four different package sizes (1206, 0805, 0603, and 0402), sit on the board waiting to be bridged. Soldering all four unlocks a bonus fourth animation mode, turning basic surface-mount soldering practice into a functional unlock rather than a no-op exercise.

The project is fully open source, with the GitHub repository split into `art/` (SVG artwork), `code/` (PlatformIO/Arduino firmware, programmed over the UPDI protocol), and `pcb/` (KiCad schematic and layout) directories. No pricing, production quantity, or distribution channel is stated in the repository or findable elsewhere; it is not clear from available sources whether it was sold, freely distributed, or built as a workshop kit.
