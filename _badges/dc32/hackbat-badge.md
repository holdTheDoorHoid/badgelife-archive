---
title: Hackbat Badge
id: dc32-hackbat-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Pablo (thehackbat)
  url: https://github.com/thehackbat
summary: An independent Game Boy-styled badge for DEF CON 32, built around an ESP32-C3 with a 1.3" OLED, six buttons, and four WS2812 LEDs.
functions: Runs custom applications programmed over USB via Arduino IDE or ESP-IDF; shows information on its OLED and drives four addressable WS2812 LEDs.
look:
  colors:
  - black
  shape: rectangle
  themes:
  - retro computer
  - console
  - security
tech:
  mcu: ESP32-C3
  leds:
    count: 4
    type: WS2812
    note: Addressable, chained in series
  display: 1.3" OLED
  connectivity:
  - wifi
  - ble
  - usb
  battery: 3x AA cells
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to attendees at DEF CON 32; open-source files let anyone order their own board through JLCPCB.
make_your_own:
  open_source: true
  hardware_url: https://github.com/thehackbat/defcon32_badge
  firmware_url: https://github.com/thehackbat/defcon32_badge
  eda_tool: KiCad
  gerbers_url: https://github.com/thehackbat/defcon32_badge
  bom_url: https://github.com/thehackbat/defcon32_badge/blob/main/kicad/production_files/bom.csv
  license: GPL-3.0
  notes: Repo includes production_files (gerbers), a centroid/pick-and-place CSV, and a BOM for JLCPCB assembly. README recommends black PCB with LeadFree HASL finish to match the original.
links:
- label: hackaday.io/project/197688-hackbat-badge
  url: https://hackaday.io/project/197688-hackbat-badge
  kind: hackaday
- label: github.com/thehackbat/defcon32_badge
  url: https://github.com/thehackbat/defcon32_badge
  kind: repo
- label: www.hackster.io/news/pablo-trujillo-s-hackbat-hacking-tool-gets-a-new-badge-variant-for-def-con-32-83700f352150
  url: https://www.hackster.io/news/pablo-trujillo-s-hackbat-hacking-tool-gets-a-new-badge-variant-for-def-con-32-83700f352150
  kind: article
- label: hackaday.io/project/197688 (Hackbat Badge Gallery)
  url: https://hackaday.io/project/197688/gallery
  kind: hackaday
images:
- file: assets/images/badges/dc32/hackbat-badge/f3069976c4.png
  source: https://github.com/thehackbat/defcon32_badge
  credit: Pablo (thehackbat)
  caption: 3D render of the Hackbat Badge
- file: assets/images/badges/dc32/hackbat-badge/6aaef738d9.png
  source: https://github.com/thehackbat/defcon32_badge
  credit: Pablo (thehackbat)
  caption: Board layout of the Hackbat Badge, Game Boy-style button arrangement
- file: assets/images/badges/dc32/hackbat-badge/629fe5039d.jpg
  source: https://hackaday.io/project/197688/gallery
  credit: Pablo Trujillo (thehackbat)
  caption: The Hackbat DEFCON32 Badge, GameBoy-style form factor with OLED and WS2812 LEDs
- file: assets/images/badges/dc32/hackbat-badge/bad93516e5.jpg
  source: https://hackaday.io/project/197688/gallery
  credit: Pablo Trujillo (thehackbat)
  caption: Hackbat DEFCON32 Badge, alternate view
contact: {}
notes:
- Sweep's original note described it as an "Independent ESP32-C3 based unofficial DEF CON 32 badge with 1.3in OLED, Game Boy-style buttons and WS2812 LEDs, open-sourced on Hackaday.io" — confirmed accurate against the maker's own GitHub README and Hackaday.io project page.
- A badge-form variant of Pablo Trujillo's Hackbat portable pentesting tool, released at DEF CON 32. The original Hackster.io article page was Cloudflare-blocked at every attempt; details below come from the maker's own GitHub repo (thehackbat/defcon32_badge) and Hackaday.io project page instead.
- The sweep's title ("Hackbat DC32 Badge Variant") is the archive's own paraphrase of the Hackster headline; the maker calls the item the "Hackbat Badge" / "DEFCON32 Badge" and there is no separate maker-named "variant" distinct from the badge itself.
- This appears to be the same physical badge already catalogued as dc32-hackbat-badge; flagging as a likely duplicate rather than merging, per instructions to touch only this entry.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/197688-hackbat-badge
  title: Hackbat Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc32-badges); event read as ''dc32''.'
- kind: url
  url: https://github.com/thehackbat/defcon32_badge
  title: 'thehackbat/defcon32_badge: DEFCON32 Badge'
  accessed: '2026-09-08'
  note: Maker's own repo README and files; confirmed MCU, LEDs, display, buttons, power, distribution at DEF CON 32, license, and open-source hardware/firmware files.
- kind: url
  url: https://www.hackster.io/news/pablo-trujillo-s-hackbat-hacking-tool-gets-a-new-badge-variant-for-def-con-32-83700f352150
  title: Hackbat DC32 Badge Variant
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc32-indie); event read as ''dc32''.'
- kind: url
  url: https://hackaday.io/project/197688/gallery
  title: Hackbat Badge Gallery - Hackaday.io
  accessed: '2026-09-10'
  note: Maker's Hackaday.io project page; confirms same specs and supplied gallery photos.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-08'
  notes: Maker's own Hackaday.io page and GitHub repo agree on all core specs. No price or production quantity is published anywhere; badge appears to have been a free give-away at DEF CON 32 rather than sold (repo has a section addressed to people who "received your Hackbat Badge at DEFCON32"), with a known hardware revision fixing a D9 diode placement defect in the convention-distributed batch. A related entry, dc32-hackbat-dc32-badge-variant (maker "Pablo Trujillo"), already exists in the archive for what looks like the same person's badge variant — left untouched per scope. Merged with duplicate entry 'Hackbat DC32 Badge Variant' (dc32-hackbat-dc32-badge-variant).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/dc32/hackbat-dc32-badge-variant/
model:
  file: assets/models/dc32/hackbat-badge.glb
  method: kicad
  source_file: kicad/defcon32_badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 175564
---

The Hackbat Badge is an independently designed, unofficial badge made for DEF CON 32 by a maker known as Pablo (GitHub handle thehackbat). It takes visual cues from the Game Boy, with a six-button directional-pad-and-two-face-button layout, a 1.3" OLED display in the "screen" position, and the ESP32-C3's USB port and power switch along the bottom edge. Four WS2812 addressable LEDs add color, and the board's backside holds a compartment for three AA cells so it can run untethered from a badge lanyard.

Badges were handed out to attendees at DEF CON 32; the maker's GitHub README calls out a known defect in that first run, where diode D9 was placed on the wrong side of the USB/battery circuit, causing the 5V USB rail to feed directly into the battery when both were connected. The published, corrected design fixes this. Everything needed to build one is open-sourced under GPL-3.0 in the `thehackbat/defcon32_badge` repository, including KiCad source, gerbers, a pick-and-place file, and a BOM formatted for a one-click JLCPCB order, with recommended black PCB color and LeadFree HASL finish to match the originals. No price or production run size is published; distribution reads as a free con give-away rather than a sale.

## Make your own

The hardware is fully open (KiCad, GPL-3.0) at https://github.com/thehackbat/defcon32_badge. To order a board: download the repo's `production_files` directory, compress it, and upload it to JLCPCB along with the included centroid CSV and BOM to use their PCB assembly service; select black PCB and LeadFree HASL to match the original. Firmware can be written with either the Arduino IDE or Espressif's ESP-IDF.

## Notes merged from the duplicate entry "Hackbat DC32 Badge Variant"

Pablo Trujillo, the FPGA designer and hobbyist behind the Hackbat portable pentesting tool, built a badge-form spinoff for DEF CON 32 in 2024. Nicknamed the Hackbat Badge (or "DEFCON32 Badge" in the repository), it takes on a GameBoy-style handheld layout built around an Espressif ESP32-C3, with a small OLED screen and four WS2812 addressable LEDs. It talks WiFi and Bluetooth LE, and runs off three AA cells in a case on the back, with USB available for charging and programming.

The badge was handed out in a limited run at DEF CON 32. Unlike the original Hackbat tool (an RP2040-based platform with NFC, sub-GHz radio, USB, and SD card support), the badge variant drops NFC and sub-gigahertz support in favor of the simpler, more badge-appropriate ESP32-C3 form factor. Trujillo published the full hardware design under GPL-3.0 on GitHub, including KiCad production files ready for services like JLCPCB; the repo also notes that a diode (D9) placement issue present in the units actually handed out at the con has since been fixed in the published files.

## Make your own

The hardware and firmware are open source. KiCad production files are in the repository at github.com/thehackbat/defcon32_badge, licensed GPL-3.0; note the corrected D9 diode placement relative to the originally distributed boards before ordering PCBs.
