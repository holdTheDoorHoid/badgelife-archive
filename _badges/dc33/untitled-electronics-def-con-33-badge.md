---
title: 'NeoSword'
id: dc33-untitled-electronics-def-con-33-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: wrickert
  url: https://github.com/wrickert
- name: Untitled Electronics
  url: https://untitledelec.com
summary: A sword-shaped independent DEF CON 33 badge with programmable NeoPixel lighting and sound effects, and three SAO ports built into the crossguard.
functions: Programmable LED lighting effects and sound playback (including classic effects like the Wilhelm Scream); described by the maker as "the world's first 3-port SAO totem that actually interacts with you," hosting three SAOs on its own header ports.
look:
  colors:
  - black
  - multicolor
  shape: sword
  themes:
  - fantasy
  - pop culture
tech:
  mcu: ESP32-S3
  leds:
    count: null
    type: NeoPixel
    note: Driven in part through an AW20072 LED driver IC (see Code/AW20072.py in the repo).
  display: none
  connectivity:
  - wifi
  - ble
  battery: 4x AA (in the handle)
  sao_version: v2
  sao_ports: 3
get_one:
  price: $110-$140
  price_usd: 110
  quantity: ''
  availability: sold_out
  availability_note: Sold out on both untitledelec.com and Tindie as of 2026-09-07.
  distribution:
  - purchase
  where: Sold via the maker's own Shopify store (untitledelec.com) and via Tindie; badges were also picked up free at the Badgelife Village at DEF CON 33.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon33
  firmware_url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon33/Code
  eda_tool: KiCad
  license: CERN OHL-S
  notes: Repo includes KiCad schematics/PCB (project named "NeoSword"), a MicroPython-based ESP32-S3 firmware image, an AW20072 LED-driver helper script, CAD files (including a 3D-printed battery lid guide), and sound-effect audio clips (e.g. Zelda "Hey Listen" and a Link scream) used for the badge's audio.
links:
- label: github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon33
  url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon33
  kind: repo
- label: 'Untitled Electronics store: Defcon 33 Indy badge: The NeoSword'
  url: https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
  kind: store
- label: 'Tindie: NeoSword Defcon33 Badge'
  url: https://www.tindie.com/products/untitledelec/neosword-defcon33-badge/
  kind: store
images:
  - file: assets/images/badges/dc33/untitled-electronics-def-con-33-badge/6b5490302a.jpg
    source: "https://untitledelec.com/products/defcon-33-indy-badge-the-neosword"
    credit: "Untitled Electronics"
    caption: "The NeoSword badge, front view"
  - file: assets/images/badges/dc33/untitled-electronics-def-con-33-badge/5527bd0301.jpg
    source: "https://untitledelec.com/products/defcon-33-indy-badge-the-neosword"
    credit: "Untitled Electronics"
    caption: "The NeoSword badge illuminated"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- This entry duplicates an existing entry, dc33-neosword, for the same badge.
status: released
sources:
- kind: url
  url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon33
  title: Untitled Electronics DEF CON 33 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc33''.'
- kind: url
  url: https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
  title: 'Defcon 33 Indy badge: The NeoSword'
  accessed: '2026-09-07'
  note: Maker's own storefront; confirms name, price, power, SAO ports, open-source licensing, and sold-out status.
- kind: url
  url: https://www.tindie.com/products/untitledelec/neosword-defcon33-badge/
  title: NeoSword Defcon33 Badge
  accessed: '2026-09-07'
  note: Secondary storefront listing; confirms maker location, features, and sold-out/inactive status.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: This entry is a duplicate of the existing dc33-neosword entry (same maker, same badge, same event) found via existing_titles.txt. LED count and exact firmware repo structure (KiCad schematic file named NeoSword.kicad_prl) confirm the project name. Exact LED count not stated by any source, left empty.
last_modified_date: '2026-09-07'
---

The NeoSword is a sword-shaped independent badge that Untitled Electronics (maker "wrickert") built for DEF CON 33 in 2025. Rather than a typical flat PCB badge, it takes the form of a handheld sword with an ESP32-S3 at its core, running MicroPython so owners can reprogram it without any exploit. It lights up with programmable NeoPixel effects and plays back sound clips, including callouts to video-game audio (a Zelda "Hey Listen" cue and a Link scream sit in the project's own repo) alongside novelty effects like the Wilhelm Scream. Power comes from four AA batteries housed in the sword's handle.

What sets the NeoSword apart is its crossguard, which carries three SAO header ports of its own — the maker describes it as "the world's first 3-port SAO totem that actually interacts with you," meaning other SAOs plugged into it can be lit and driven by the sword rather than sitting passively. It was sold through the maker's own Shopify storefront and on Tindie (in the $110-$140 range depending on the listing), with free pickup also offered at the Badgelife Village at DEF CON 33; as of this check both storefronts show it sold out.

Full hardware and firmware are open source under the CERN OHL-S license. The GitHub repository (under the project name "NeoSword") includes KiCad schematics and PCB files, the ESP32-S3 MicroPython firmware image and a flashing script, a helper script for the AW20072 LED driver IC, and CAD for a 3D-printed battery lid guide.

## Make your own

The repository at github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon33 has everything needed to build or reflash one: KiCad schematics and Gerbers under `Schematics/`, CAD/STEP files under `CAD/`, and firmware plus a `flash.sh` script under `Code/` for loading the ESP32-S3 MicroPython image.
