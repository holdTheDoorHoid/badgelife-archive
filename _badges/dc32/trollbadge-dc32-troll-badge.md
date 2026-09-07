---
title: trollbadge (DC32 Troll Badge)
id: dc32-trollbadge-dc32-troll-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: C0ldbru / Rot13 Labs
  url: https://rot13labs.com
summary: A PCB badge shaped like the "troll face" meme that scans nearby wifi networks and rebroadcasts their SSIDs as a beacon-spoofing attack, with a built-in CTF and debug console.
functions: wifi trolling (SSID-spoofing beacon attack on scanned networks), "perma-troll" auto-rescan mode, serial console with debug mode, badge CTF
look:
  colors:
  - white
  - silver
  shape: other
  themes:
  - meme
  - pop culture
tech:
  mcu: ESP32 (exact variant not stated; firmware uses the ESP32 Arduino WiFi/softAP stack)
  leds:
    count: 2
    type: NeoPixel-compatible RGB (WS2812B-class)
    note: Adafruit_NeoPixel library, random color-cycling; switches to a red "Rick" pattern in one firmware mode.
  display: none
  connectivity:
  - wifi
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
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/c0ldbru/trollbadge
  eda_tool: null
  notes: Firmware (Arduino .ino) is published in the repo; no schematic or Gerbers were found alongside it.
links:
- label: github.com/c0ldbru/trollbadge
  url: https://github.com/c0ldbru/trollbadge
  kind: repo
images:
- file: assets/images/badges/dc32/trollbadge-dc32-troll-badge/441ffdca00.jpg
  source: "https://rot13labs.com/"
  credit: "rot13labs"
  caption: "The DC32 troll badge, photographed by its maker"
contact: {}
notes:
- 'Duplicate of dc32-wifi-troll-badge, an existing, more fully researched entry for the same badge (same maker, same GitHub repo, same firmware).'
status: released
sources:
- kind: url
  url: https://github.com/c0ldbru/trollbadge
  title: trollbadge (DC32 Troll Badge)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 32''.'
- kind: url
  url: https://github.com/c0ldbru/trollbadge
  title: c0ldbru/trollbadge README and firmware
  accessed: '2026-09-07'
  note: 'README and troublemaker.ino confirm the wifi beacon-spoofing behavior, the "Troll" button and "perma-troll" switch, 9600-baud serial debug/CTF console, and the ESP32 Arduino WiFi/NeoPixel (2x) stack.'
- kind: url
  url: https://rot13labs.com/
  title: "rot13labs — WE MAKE CHAOS"
  accessed: '2026-09-07'
  note: "Maker's project photo gallery, includes a photo of the troll badge; source of the badge image."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This entry is a duplicate of dc32-wifi-troll-badge, created independently by the discovery sweep under a different slug for the same GitHub repo (c0ldbru/trollbadge). That other entry carries additional detail (price, quantity of 100 units, distribution) sourced from rot13labs.com that could not be independently re-confirmed here since the site''s shop page is currently being rebuilt; those fields are left empty in this entry rather than copied without a fresh check. No independent price, quantity, or availability information was found beyond what the sibling entry already documents.'
last_modified_date: '2026-09-07'
---

The DC32 troll badge is a wifi-trolling badge made by C0ldbru of Rot13 Labs for DEF CON 32 (2024), cut into the shape of the "troll face" meme. By default it scans for nearby wifi networks and then rebroadcasts each found SSID as its own access point, one after another, flooding the local wireless environment with spoofed networks. A front "Troll" button forces an immediate rescan, and a "perma-troll" switch puts it into a mode that automatically rescans every 30 seconds or so.

Connecting to the badge over USB opens a 9600-baud serial console that exposes a small on-board CTF, a debug-output toggle, and other hidden wifi-trolling modes. Two NeoPixel-style RGB LEDs cycle random colors while the badge runs, switching to a red pattern in one of its firmware Easter eggs. The maker published the Arduino firmware ("troublemaker.ino") on GitHub for others to reuse, though no schematic or PCB files were found alongside it.

This entry duplicates an existing, more thoroughly researched entry for the same badge, `dc32-wifi-troll-badge`, which was built from the same GitHub repo plus the maker's own site and carries additional detail (price, a 100-unit production run, and distribution).
