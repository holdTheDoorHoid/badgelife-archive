---
title: Kermie
id: dc31-kermie
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: scdickson
summary: The official 2023 Frog Badge for DEF CON 31, an ESP32-based electronic badge with a color TFT display showing animated frog GIFs, built as "an homage to amphibians in pop culture."
functions: Displays 12 pre-loaded animated frog GIFs plus one custom user slot; each badge is assigned a unique name based on real amphibian taxonomy and unlocks two random animations at boot. Additional frog animations can be unlocked and shared with other badges over Wi-Fi via a built-in sharing menu. Sharing with eight other badges, or entering a hidden key combo and refrigerating the badge to "hibernate," unlocks secret animations. An onboard AHT10 sensor also supports a temperature-reading mode. An NFC tag on the back links to instructions.
look:
  colors: []
  shape: null
  themes:
  - animal
  - frog
  - meme
  - pop culture
tech:
  mcu: ESP32
  leds: null
  display: TFT LCD
  connectivity:
  - wifi
  - nfc
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
  open_source: true
  hardware_url: https://github.com/scdickson/Kermie/tree/main/Gerber%20Files
  firmware_url: https://github.com/scdickson/Kermie/blob/main/FrogBadge.ino
  eda_tool: KiCad
links:
- label: github.com/scdickson/Kermie
  url: https://github.com/scdickson/Kermie
  kind: repo
- label: frogbadge.com
  url: https://frogbadge.com
  kind: website
images:
- file: assets/images/badges/dc31/kermie/0abbcdc9c8.jpg
  source: https://github.com/scdickson/Kermie
  credit: scdickson
  caption: Kermie / Frog Badge PCB spread, front and back
- file: assets/images/badges/dc31/kermie/b19adc685c.png
  source: https://github.com/scdickson/Kermie
  credit: scdickson
  caption: Kermie / Frog Badge PCB render
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/scdickson/Kermie
  title: Kermie
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/scdickson/Kermie/main/README.md
  title: Kermie - Defcon 2023 Frog Badge (README)
  accessed: '2026-09-07'
  note: Confirms it was made for DEF CON 31 (2023), maker's own description, secrets/unlock mechanics, security design, and links to frogbadge.com and the Gerber files.
- kind: url
  url: https://raw.githubusercontent.com/scdickson/Kermie/main/FrogBadge.ino
  title: FrogBadge.ino source
  accessed: '2026-09-07'
  note: Confirms ESP32 (FreeRTOS/WiFi.h), TFT_eSPI-driven color display, SD card storage, and an Adafruit AHT10 temperature/humidity sensor onboard.
- kind: url
  url: https://api.github.com/repos/scdickson/Kermie/contents/Gerber%20Files
  title: Kermie Gerber Files directory listing
  accessed: '2026-09-07'
  note: Confirms full Gerber/fab files are published in the repo alongside the frog_spread.jpg and pcb_image.png photos used for the entry images.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): every non-empty field and factual sentence was re-checked against the cited sources (README.md, FrogBadge.ino, and the Gerber Files directory listing, all fetched directly from the repo) and confirmed. FrogBadge.ino confirms ESP32 (FreeRTOS/WiFi.h), TFT_eSPI display driving, SD-card image storage, and an Adafruit AHT10 sensor. README.md confirms the DC31/2023 framing, 12+1 GIF slots, amphibian-taxonomy naming, the Wi-Fi sharing/8-badge/hibernate unlock mechanics, the AES/SHA256/WPA2-ECC security details, the NFC tag, and the Custom Image/SD-card-formatting instructions used in the Make your own section. The Gerber Files listing confirms standard KiCad-style gerber/drill naming (F_Cu, B_Cu, Edge_Cuts, .gbrjob) supporting eda_tool: KiCad, and that frog_spread.jpg and pcb_image.png (the two saved images) originate from that same folder. frogbadge.com was independently re-confirmed as non-resolving with no Wayback Machine snapshot (archive.org availability
    API returned an empty result), supporting the empty price/quantity/availability fields. No corrections were needed; confidence stays medium because price, quantity, availability, LEDs, exact display size, and battery details remain unconfirmed by any source and are correctly left empty.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/kermie/
model:
  file: assets/models/dc31/kermie.glb
  method: gerber
  source_file: Gerber Files
  generated: '2026-09-07'
  bytes: 202652
  size_mm:
  - 155.0
  - 173.9
---

Kermie (also called the Frog Badge) was the official electronic badge for DEF CON 31 in 2023, designed by scdickson as "an homage to amphibians in pop culture." Built around an ESP32 with a color TFT display and an SD card for image storage, each badge is given a unique name drawn from real amphibian taxonomy and ships with two of its twelve built-in animated frog GIFs already unlocked, plus one open slot for a custom user animation.

The badge's central mechanic is unlocking the rest of its frog roster: badges can trade unlocks with each other over a built-in Wi-Fi sharing menu, and collecting shares from eight other badges reveals a secret animation, as does a hidden key-combination-and-refrigeration "hibernate" easter egg documented on the badge's included guide and reachable via an NFC tag on its back. Because it was built for DEF CON, the badge's designer paid particular attention to security: its SD card configuration file is encrypted with an AES key burned into the firmware, initial frog frames are hash-verified at boot to deter tampering, and Wi-Fi sharing sessions are secured with WPA2 plus AES encryption over an ECC keypair generated per session. The badge also includes an AHT10 temperature/humidity sensor, exposed through a temperature-display mode.

The hardware and firmware are fully open-sourced on GitHub, including Gerber files, a KiCad-derived PCB layout, and the complete Arduino (.ino) firmware. The badge's own promotional site, frogbadge.com, is no longer online and has no archived snapshot, so pricing, production quantity, and distribution details (e.g., whether it was sold, given away, or a personal/small-group project) could not be verified.

## Make your own

The repository (https://github.com/scdickson/Kermie) contains everything needed to reproduce the badge: Gerber files and drill/paste/silkscreen layers under `Gerber Files/` for fabrication, the full firmware in `FrogBadge.ino`, and a `Custom Image/` folder documenting how to prepare a custom animation for the badge's open GIF slot. To reinitialize a badge's SD card, format it FAT32 and copy the contents of the repo's `Media` folder into an `img` directory at the card's root.
