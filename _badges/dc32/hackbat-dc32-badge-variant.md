---
title: Hackbat DC32 Badge Variant
id: dc32-hackbat-dc32-badge-variant
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Pablo Trujillo
  url: https://hackaday.io/project/197688/gallery
summary: A GameBoy-styled electronic badge based on the ESP32-C3, built as a spinoff of Pablo Trujillo's Hackbat pentesting tool and released at DEF CON 32.
functions: Runs custom firmware on the ESP32-C3; drives an OLED display and four addressable WS2812 LEDs; connects over WiFi and Bluetooth LE.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - console
  - security
  - hardware tool
tech:
  mcu: ESP32-C3
  leds:
    count: 4
    type: WS2812
    note: ''
  display: OLED
  connectivity:
  - wifi
  - ble
  battery: 3x AA cells (backside case); USB for charging/programming
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed at DEF CON 32; open-source design files also available for self-manufacture.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/thehackbat/defcon32_badge
  firmware_url: https://github.com/thehackbat/defcon32_badge
  eda_tool: KiCad
  notes: 'Repository includes KiCad production files (GPL-3.0). A manufacturing issue with diode D9 placement in the units distributed at DEF CON 32 has since been corrected in the repo files.'
links:
- label: www.hackster.io/news/pablo-trujillo-s-hackbat-hacking-tool-gets-a-new-badge-variant-for-def-con-32-83700f352150
  url: https://www.hackster.io/news/pablo-trujillo-s-hackbat-hacking-tool-gets-a-new-badge-variant-for-def-con-32-83700f352150
  kind: article
- label: github.com/thehackbat/defcon32_badge
  url: https://github.com/thehackbat/defcon32_badge
  kind: repo
- label: hackaday.io/project/197688 (Hackbat Badge Gallery)
  url: https://hackaday.io/project/197688/gallery
  kind: hackaday
images:
- file: assets/images/badges/dc32/hackbat-dc32-badge-variant/629fe5039d.jpg
  source: "https://hackaday.io/project/197688/gallery"
  credit: "Pablo Trujillo (thehackbat)"
  caption: "The Hackbat DEFCON32 Badge, GameBoy-style form factor with OLED and WS2812 LEDs"
- file: assets/images/badges/dc32/hackbat-dc32-badge-variant/bad93516e5.jpg
  source: "https://hackaday.io/project/197688/gallery"
  credit: "Pablo Trujillo (thehackbat)"
  caption: "Hackbat DEFCON32 Badge, alternate view"
contact: {}
notes:
- A badge-form variant of Pablo Trujillo's Hackbat portable pentesting tool, released at DEF CON 32. The original Hackster.io article page was Cloudflare-blocked at every attempt; details below come from the maker's own GitHub repo (thehackbat/defcon32_badge) and Hackaday.io project page instead.
- The sweep's title ("Hackbat DC32 Badge Variant") is the archive's own paraphrase of the Hackster headline; the maker calls the item the "Hackbat Badge" / "DEFCON32 Badge" and there is no separate maker-named "variant" distinct from the badge itself.
- This appears to be the same physical badge already catalogued as dc32-hackbat-badge; flagging as a likely duplicate rather than merging, per instructions to touch only this entry.
status: released
sources:
- kind: url
  url: https://www.hackster.io/news/pablo-trujillo-s-hackbat-hacking-tool-gets-a-new-badge-variant-for-def-con-32-83700f352150
  title: Hackbat DC32 Badge Variant
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc32-indie); event read as ''dc32''.'
- kind: url
  url: https://github.com/thehackbat/defcon32_badge
  title: 'GitHub - thehackbat/defcon32_badge: Badge designed for DEFCON32'
  accessed: '2026-09-10'
  note: 'Maker''s own repo: confirms ESP32-C3, OLED, 4x WS2812 LEDs, WiFi/BLE, 3xAA + USB power, KiCad files, GPL-3.0 open source, and the D9 diode fix.'
- kind: url
  url: https://hackaday.io/project/197688/gallery
  title: Hackbat Badge Gallery - Hackaday.io
  accessed: '2026-09-10'
  note: 'Maker''s Hackaday.io project page; confirms same specs and supplied gallery photos.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Core facts confirmed via the maker''s own GitHub repo and Hackaday.io page rather than the (Cloudflare-blocked) Hackster article itself, so confidence is medium rather than high. Price, quantity made, and current availability are not stated anywhere found. Likely duplicates dc32-hackbat-badge (same maker, same DEF CON 32 badge) — see duplicate_of in the automated report.'
last_modified_date: '2026-09-10'
---

Pablo Trujillo, the FPGA designer and hobbyist behind the Hackbat portable pentesting tool, built a badge-form spinoff for DEF CON 32 in 2024. Nicknamed the Hackbat Badge (or "DEFCON32 Badge" in the repository), it takes on a GameBoy-style handheld layout built around an Espressif ESP32-C3, with a small OLED screen and four WS2812 addressable LEDs. It talks WiFi and Bluetooth LE, and runs off three AA cells in a case on the back, with USB available for charging and programming.

The badge was handed out in a limited run at DEF CON 32. Unlike the original Hackbat tool (an RP2040-based platform with NFC, sub-GHz radio, USB, and SD card support), the badge variant drops NFC and sub-gigahertz support in favor of the simpler, more badge-appropriate ESP32-C3 form factor. Trujillo published the full hardware design under GPL-3.0 on GitHub, including KiCad production files ready for services like JLCPCB; the repo also notes that a diode (D9) placement issue present in the units actually handed out at the con has since been fixed in the published files.

## Make your own

The hardware and firmware are open source. KiCad production files are in the repository at github.com/thehackbat/defcon32_badge, licensed GPL-3.0; note the corrected D9 diode placement relative to the originally distributed boards before ordering PCBs.
