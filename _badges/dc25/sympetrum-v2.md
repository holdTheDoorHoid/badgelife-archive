---
title: Sympetrum v2
id: dc25-sympetrum-v2
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: borgel
  url: https://github.com/borgel
summary: A dragonfly-shaped electronic conference badge whose 10 RGB LEDs fade through colors on an internal clock and synchronize with nearby badges via infrared beacons.
functions: Continuous RGB color-fade animation across 10 LEDs, driven by an internal clock. Each badge beacons its clock and metadata over infrared; badges that see each other's beacons sync their clocks, so isolated badges cycle random colors while a group of badges converges on shared color patterns.
look:
  colors: []
  shape: dragonfly
  themes:
  - insect
  - nature
tech:
  mcu: STM32F030K6T6
  leds:
    count: 10
    type: APA102C
    note: 5050 package RGB LEDs; alternate CPU STM32F051K8T6 supported if the primary part is unavailable.
  display: none
  connectivity:
  - ir
  battery: AA
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold/distributed by the maker at DEF CON 25 (2017); the maker states they are "totally out" and it is not for sale, though hardware and firmware are open source for self-build.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/borgel/sympetrum-v2/tree/master/Hardware
  firmware_url: https://github.com/borgel/sympetrum-v2/tree/master/Firmware
  eda_tool: KiCad
notes: []
images:
- file: assets/images/badges/dc25/sympetrum-v2/d0e14d3b2f.png
  source: https://kitspace.org/borgel/sympetrum-v2
  credit: borgel
  caption: Sympetrum v2 dragonfly-shaped badge, top view
contact: {}
status: released
sources:
- kind: url
  url: https://kitspace.org/borgel/sympetrum-v2
  title: Sympetrum v2 on Kitspace
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://github.com/borgel/sympetrum-v2
  title: borgel/sympetrum-v2 (GitHub repo)
  accessed: '2026-09-07'
  note: Confirmed DEF CON 25 (2017) target, MIT license, open-source hardware and firmware, IR-sync behavior.
- kind: url
  url: https://raw.githubusercontent.com/borgel/sympetrum-v2/master/README.md
  title: sympetrum-v2 README
  accessed: '2026-09-07'
  note: 'Maker''s own description: dragonfly theme inspired by Neal Stephenson''s The Diamond Age; sequel to a hastier DEFCON 24 version (borgel/sympetrum); "totally out" of units; links to a 2017 Hackaday writeup.'
- kind: url
  url: https://raw.githubusercontent.com/borgel/sympetrum-v2/master/Hardware/README.md
  title: sympetrum-v2 Hardware README
  accessed: '2026-09-07'
  note: MCU part number and alternate, APA102C LED count/type, KiCad design files, AA battery holder, gerbers labeled FF1.1, firmware release v4 used at DEFCON25.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's GitHub repo and Kitspace listing agree on all core facts. Price and quantity made were never stated by the maker and are left empty. A 2017 Hackaday article ("Badge From Diamond Age Comes To DEF CON") is referenced in the README but was not independently fetched. No photo of the assembled badge in hand was found beyond the Kitspace board-render image saved here; PCB solder-mask color was not specified by the maker (boards are designed for white mask/black silkscreen but "the design should work correctly in any color").
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/sympetrum-v2/
model:
  file: assets/models/dc25/sympetrum-v2.glb
  method: kicad
  source_file: Hardware/FF1.1/sympetrum-v2 FF1.1.kicad_pcb
  generated: '2026-09-07'
  bytes: 253768
---

Sympetrum v2 is a dragonfly-shaped electronic badge built by borgel for DEF CON 25 in 2017, a full rewrite of a hastier version 1 made for DEF CON 24. Ten APA102C RGB LEDs run a continuous color-fade animation driven by an STM32F030K6T6 microcontroller, while an infrared transmitter beacons the badge's internal clock and metadata to nearby badges. Badges that pick up each other's beacons synchronize their clocks and therefore their color patterns: alone, a badge cycles random colors, but a cluster of them tends to converge on shared patterns. The concept is a direct homage to a scene in Neal Stephenson's novel *The Diamond Age*, in which partygoers wear cloisonné dragonfly pins that shift from random flickering into synchrony as a crowd gathers.

The maker gave the badges away/sold them at DEF CON 25 and has since said they are completely out of stock, with no further production planned under this name (a mailing list signup in the README was for a possible DEFCON 26 successor). Hardware and firmware are both fully open source under the MIT license: KiCad design files and gerbers (tagged FF1.1) are on GitHub and mirrored on Kitspace, and the firmware is tagged as release v4, the version used at DEF CON 25.

## Make your own

Gerbers are downloadable directly from the Kitspace project page (which also offers one-click ordering through Aisler or PCBWay) or from the `Hardware/FF1.1` folder in the GitHub repo. The boards are sized to fit the common 100mm x 100mm cheap-PCB tier, and the maker's own bill of materials totals roughly $13 per board from Digikey plus about $25 for a set of 10 boards from a budget fab house. Firmware source is in the repo's `Firmware` directory and builds against the STM32F030K6T6 (or the pin-compatible STM32F051K8T6 with a one-line Makefile edit); APA102C LEDs and a AA battery holder complete the build.
