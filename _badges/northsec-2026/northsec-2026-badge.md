---
title: NorthSec 2026 Badge
id: northsec-2026-northsec-2026-badge
layout: badge
parent: NorthSec 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: northsec-2026
year: 2026
makers:
- name: NorthSec
  url: https://nsec.io/
summary: The official electronic badge for NorthSec 2026, an ESP32-S3 badge with an e-ink display, 18 addressable LEDs, NFC pairing, and a WiFi-based social/CTF game.
functions: Peer-to-peer NFC pairing with other badges and sponsor badges to raise three gamified stats (Social, Sponsor, Light); a WiFi access point with a captive portal (SSID NSEC-XXXX at 192.168.4.1); an ambient light sensor that passively contributes to the Light stat; and a serial CLI used to switch between a conference firmware partition and a separate CTF-challenges firmware partition.
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
  - wearable
tech:
  mcu: ESP32-S3
  leds:
    count: 18
    type: null
    note: 18 programmable LEDs with 26 built-in animations (aurora, lava_lamp, rainbow, etc.); also used to show progress in the Social (purple), Sponsor (green), and Light (blue) stat categories.
  display: e-ink
  connectivity:
  - wifi
  - nfc
  battery: LiPo
  sao_version: null
  inputs:
  - buttons
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Included with NorthSec 2026 conference, CTF, combo, and training tickets.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/nsec/badge-2026/tree/main/hardware
  firmware_url: https://github.com/nsec/badge-2026
  eda_tool: null
links:
- label: github.com/nsec/badge-2026
  url: https://github.com/nsec/badge-2026
  kind: repo
- label: nsec.io/badge
  url: https://nsec.io/badge/
  kind: website
images:
- file: assets/images/badges/northsec-2026/northsec-2026-badge/268f8ea4ef.png
  source: https://nsec.io/badge/
  credit: NorthSec
  caption: Annotated diagram of the NorthSec 2026 electronic badge showing buttons, e-ink display, and LEDs
contact: {}
notes:
- Official NorthSec 2026 badge, released under Apache-2.0 with dock/SAO directories; included with conference, CTF, combo, and training tickets. Found by the event-year sweep, task northsec.
status: released
sources:
- kind: url
  url: https://github.com/nsec/badge-2026
  title: NorthSec 2026 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:northsec); event read as ''northsec-2026''.'
- kind: url
  url: https://nsec.io/badge/
  title: NorthSec 2026 Electronic Badge
  accessed: '2026-09-08'
  note: 'Maker''s own attendee page: features, LEDs, e-ink display, NFC/WiFi social game, LiPo battery, buttons, free with tickets.'
- kind: url
  url: https://github.com/nsec/badge-2026/blob/main/hardware/sao/README.md
  title: badge-2026 hardware/sao README
  accessed: '2026-09-08'
  note: SAO connector README is a placeholder ("tbd") as of the check date; hardware repo confirms an SAO directory exists but pinout/version were not documented.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own GitHub org and nsec.io attendee page. The repo lists dock/SAO hardware directories, but the SAO README itself only says "tbd" as of this check, so tech.sao_version and sao_ports are left empty rather than guessed. Price/quantity: given free with tickets, not sold separately, so price_usd is set to 0 and quantity is left blank (not stated). Look.colors/shape not stated on the maker page; left empty rather than guessed from the badge photo.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/northsec-2026/northsec-2026-badge.glb
  method: gerber
  source_file: hardware/badge/nsec-badge-2026.kicad_pcb
  generated: '2026-09-10'
  bytes: 197988
  size_mm:
  - 159.8
  - 139.1
---

The NorthSec 2026 badge is the official electronic badge given to attendees of NorthSec, the Montreal-based cybersecurity conference, and is bundled free with conference, CTF, combo, and training tickets. Built around an ESP32-S3, it pairs an e-ink display (showing the NorthSec logo when idle) with 18 addressable LEDs driving 26 built-in animations, six physical buttons (a directional pad plus two action buttons), and a rear power toggle.

Its central gimmick is a social/CTF game layered over NFC and WiFi: badges pair with each other and with sponsor badges over NFC to raise three tracked stats — Social, Sponsor, and Light (the last filled passively by an onboard ambient-light sensor) — each shown on the LEDs in its own color and each capped at 255. The badge also broadcasts its own WiFi access point (`NSEC-XXXX`) with a captive portal for badge management, can store up to 128 exchanged contacts, and can read or emulate NFC tags (NTAG213 emulation). Firmware is split into a conference partition and a separate CTF-challenges partition, switchable over a serial CLI, and per the closing-ceremony writeup covered by attendee "brouetterouge," the CTF side of the badge shipped with three tracks and ten challenges.

Firmware and PCB design files are published on GitHub (`nsec/badge-2026`) under Apache-2.0, including a `hardware/sao` directory, though as of this check that SAO README was still a placeholder, so no SAO pinout or version could be confirmed from the maker's own documentation.
