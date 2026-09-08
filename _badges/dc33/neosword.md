---
title: NeoSword
id: dc33-neosword
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: Untitled Electronics
  url: https://untitledelec.com
  role: '@wrickert from the discord, per the community sheet'
summary: A sword-shaped 3-port SAO totem with programmable lights and sound effects, running MicroPython.
functions: SAO totem (hosts up to 3 SAO modules); programmable LED patterns and sound effects (e.g. plays the Wilhelm Scream); user-scriptable via MicroPython
look:
  colors:
  - green
  - purple
  - clear
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
  price: $140
  price_usd: 140.0
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - free_drop
  where: Sold via untitledelec.com; also free pickup available at the Badgelife Village at DEF CON 33
  availability_note: Sold out on both untitledelec.com and Tindie as of 2026-09-07.
make_your_own:
  open_source: true
  hardware_url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon33
  firmware_url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon33/Code
  eda_tool: KiCad
  license: CERN OHL-S
  notes: 'Maker states: "All source code, CAD, and anything else we can think of will be freely available" under CERN OHL-S. No repo, CAD or Gerber link was found, so open_source is left unknown until files are actually published.'
links:
- label: untitledelec.com/products/defcon-33-indy-badge-the-neosword
  url: https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
  kind: website
  archived: https://web.archive.org/web/20260122102330/https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
- label: bsky.app/profile/untitledelec.bsky.social
  url: https://bsky.app/profile/untitledelec.bsky.social
  kind: social
- label: github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon33
  url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon33
  kind: repo
- label: 'Tindie: NeoSword Defcon33 Badge'
  url: https://www.tindie.com/products/untitledelec/neosword-defcon33-badge/
  kind: store
  archived: https://web.archive.org/web/20260503131113/https://www.tindie.com/products/untitledelec/neosword-defcon33-badge/
images:
- file: assets/images/badges/dc33/neosword/6b5490302a.jpg
  source: https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
  credit: Untitled Electronics
  caption: The NeoSword DC33 SAO totem
  archived: https://web.archive.org/web/20260122102330/https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
- file: assets/images/badges/dc33/neosword/9191db8430.jpg
  source: https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
  credit: Untitled Electronics
  caption: Two NeoSword variants (green PCB blade with purple 3D-printed hilt and handle)
  archived: https://web.archive.org/web/20260122102330/https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
- file: assets/images/badges/dc33/neosword/6b5490302a.jpg
  source: https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
  credit: Untitled Electronics
  caption: The NeoSword badge, front view
  archived: https://web.archive.org/web/20260122102330/https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
- file: assets/images/badges/dc33/neosword/5527bd0301.jpg
  source: https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
  credit: Untitled Electronics
  caption: The NeoSword badge illuminated
  archived: https://web.archive.org/web/20260122102330/https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- This entry duplicates an existing entry, dc33-neosword, for the same badge.
status: released
sources:
- kind: sheet
  event: dc33
  row: 24
  updated: 7/14/2025 15:02:31
- kind: url
  url: https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
  title: 'Defcon 33 Indy badge: The NeoSword!'
  accessed: '2026-09-06'
  note: Primary source for price, description, features, battery, license, images, and pickup/shipping details.
  archived: https://web.archive.org/web/20260122102330/https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
- kind: url
  url: https://github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon33
  title: Untitled Electronics DEF CON 33 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc33''.'
- kind: url
  url: https://www.tindie.com/products/untitledelec/neosword-defcon33-badge/
  title: NeoSword Defcon33 Badge
  accessed: '2026-09-07'
  note: Secondary storefront listing; confirms maker location, features, and sold-out/inactive status.
  archived: https://web.archive.org/web/20260503131113/https://www.tindie.com/products/untitledelec/neosword-defcon33-badge/
research:
  status: verified
  confidence: high
  last_checked: '2026-09-06'
  notes: Fact-checked 2026-09-06 against the storefront page; all remaining fields and body sentences are supported by it or by the maker's product photos (colors, themes and the sword/Triforce styling come from the photos). open_source set to null because no published files were found, only the maker's stated intent. The maker's storefront confirms this is a badge-side SAO totem (not itself an SAO plugging into a badge) with 3 SAO ports, MicroPython, CERN OHL-S open-source licensing, and 4xAA power. Could not find an MCU model, LED count/type, quantity made, or a specific GitHub/CAD repo link despite the maker's stated intent to publish source; the Bluesky profile page yielded no readable post content (the storefront itself names @untitledelec.bsky.social as the maker's pickup-announcement account). A companion accessory, "3 Stones SAO," is sold separately by the same maker for DC33 but was not researched as part of this entry. Merged with duplicate entry 'NeoSword' (dc33-untitled-electronics-def-con-33-badge).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc33/untitled-electronics-def-con-33-badge/
model:
  file: assets/models/dc33/neosword.glb
  method: kicad
  source_file: Badges/Defcon33/Schematics/Neoswordkicad.kicad_pcb
  generated: '2026-09-07'
  bytes: 533088
---

The NeoSword is a sword-shaped SAO totem made by Untitled Electronics for DEF CON 33 (2025), sold as an "Indy badge" (independent, unofficial badge) rather than an SAO that plugs into someone else's badge. It hosts up to three SAO modules of its own, runs MicroPython so owners can reflash its behavior without exploiting anything, and combines programmable LED lighting with sound effects (the maker specifically calls out the Wilhelm Scream as a stock effect). It runs on four AA batteries housed in the sword's handle rather than USB power.

Untitled Electronics sold the NeoSword for $140, with badges either shipped by August 1, 2025 or available for free pickup at the Badgelife Village at DEF CON 33; a few early pickups were announced via the maker's Bluesky account. The maker also offered a $20 bundle discount when purchased together with a separate "3 Stones SAO" accessory. As of research, the listing shows the item sold out.

The maker states the hardware design, firmware source, and CAD files will be released under the CERN OHL-S open-source hardware license, though a specific repository or file link was not found during this pass. The same maker (as "Untitled Electronics") also had an unnamed badge/SAO entry on the DC31 community sheet, so this is not the maker's first DEF CON release.

## Notes merged from the duplicate entry "NeoSword"

The NeoSword is a sword-shaped independent badge that Untitled Electronics (maker "wrickert") built for DEF CON 33 in 2025. Rather than a typical flat PCB badge, it takes the form of a handheld sword with an ESP32-S3 at its core, running MicroPython so owners can reprogram it without any exploit. It lights up with programmable NeoPixel effects and plays back sound clips, including callouts to video-game audio (a Zelda "Hey Listen" cue and a Link scream sit in the project's own repo) alongside novelty effects like the Wilhelm Scream. Power comes from four AA batteries housed in the sword's handle.

What sets the NeoSword apart is its crossguard, which carries three SAO header ports of its own — the maker describes it as "the world's first 3-port SAO totem that actually interacts with you," meaning other SAOs plugged into it can be lit and driven by the sword rather than sitting passively. It was sold through the maker's own Shopify storefront and on Tindie (in the $110-$140 range depending on the listing), with free pickup also offered at the Badgelife Village at DEF CON 33; as of this check both storefronts show it sold out.

Full hardware and firmware are open source under the CERN OHL-S license. The GitHub repository (under the project name "NeoSword") includes KiCad schematics and PCB files, the ESP32-S3 MicroPython firmware image and a flashing script, a helper script for the AW20072 LED driver IC, and CAD for a 3D-printed battery lid guide.

## Make your own

The repository at github.com/wrickert/UntitledElectronics/tree/main/Badges/Defcon33 has everything needed to build or reflash one: KiCad schematics and Gerbers under `Schematics/`, CAD/STEP files under `CAD/`, and firmware plus a `flash.sh` script under `Code/` for loading the ESP32-S3 MicroPython image.
