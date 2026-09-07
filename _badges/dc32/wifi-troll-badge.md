---
title: Wifi Troll Badge
id: dc32-wifi-troll-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: C0ldbru (Rot13 labs)
  url: https://rot13labs.com
summary: A PCB badge shaped like the "troll face" meme that scans nearby wifi networks and rebroadcasts their SSIDs to jam authentication in the area, plus a built-in CTF and debug console.
functions: wifi trolling (SSID-spoofing beacon attack on scanned networks), "perma-troll" auto-rescan mode, serial console with debug mode, badge CTF, feature flags
look:
  colors:
  - white
  - silver
  shape: other
  themes:
  - meme
  - pop culture
  - wifi
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
  inputs:
  - buttons
  battery: null
  sao_version: null
get_one:
  price: $70.00
  price_usd: 70.0
  quantity: '100'
  availability: unknown
  availability_note: 'Checked 2026-09-06: maker''s storefront (shop.html on rot13labs.com) says the shop is being rebuilt from the ground up; no current listing.'
  distribution:
  - purchase
  where: Sold directly by rot13labs (C0ldbru) at DEF CON 32; a limited run of 100 units.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/c0ldbru/trollbadge
  eda_tool: null
  notes: Firmware (Arduino .ino) is published; no schematic/Gerbers found in the repo, so hardware design files are not confirmed open.
links:
- kind: repo
  label: trollbadge firmware (GitHub)
  url: https://github.com/c0ldbru/trollbadge
- kind: website
  label: rot13labs
  url: https://rot13labs.com
  archived: https://web.archive.org/web/20260615020751/https://rot13labs.com/
images:
- file: assets/images/badges/dc32/wifi-troll-badge/441ffdca00.jpg
  source: https://rot13labs.com
  credit: rot13labs
  caption: 'The Wifi Troll Badge: a white PCB cut into the shape of the "troll face" meme, worn on a lanyard printed "Rot13Labs / Y U mad bro?"'
  archived: https://web.archive.org/web/20260615020751/https://rot13labs.com/
- file: assets/images/badges/dc32/wifi-troll-badge/441ffdca00.jpg
  source: https://rot13labs.com/
  credit: rot13labs
  caption: The DC32 troll badge, photographed by its maker
  archived: https://web.archive.org/web/20260615020751/https://rot13labs.com/
contact: {}
notes:
- Duplicate of dc32-wifi-troll-badge, an existing, more fully researched entry for the same badge (same maker, same GitHub repo, same firmware).
status: released
sources:
- kind: sheet
  event: dc32
  row: 33
  updated: ''
- kind: url
  url: https://rot13labs.com
  title: rot13labs — WE MAKE CHAOS
  accessed: '2026-09-06'
  note: Maker's own project page describing the troll badge's function, the 100-unit limited run, and its role in spoofing DEF CON's most common SSIDs; source of the badge photo.
  archived: https://web.archive.org/web/20260615020751/https://rot13labs.com/
- kind: url
  url: https://github.com/c0ldbru/trollbadge
  title: c0ldbru/trollbadge
  accessed: '2026-09-06'
  note: Published firmware (troublemaker.ino) and README confirming wifi beacon-spoofing behavior, the "Troll" button and "perma-troll" switch, 9600-baud serial debug/CTF console, and the ESP32 Arduino WiFi/NeoPixel stack used.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Maker's own site and published firmware confirm the core story and the 100-unit run. Exact ESP32 variant, LED part number, battery/power arrangement, and hardware design files (schematic/Gerbers) were not found in any source, so those fields are left partial or empty rather than guessed. Price ($70) is carried over from the original community sheet; no independent confirmation of price was found on rot13labs.com. Merged with duplicate entry 'trollbadge (DC32 Troll Badge)' (dc32-trollbadge-dc32-troll-badge).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc32/trollbadge-dc32-troll-badge/
---

The Wifi Troll Badge is a DEF CON 32 (2024) badge from C0ldbru of Rot13 labs, cut into the shape of the "troll face" meme. Its main trick is wifi-based: it scans the local wireless environment and then rebroadcasts (via `WiFi.softAP`) the SSIDs of every network it finds, one after another, so that nearby devices see a flood of spoofed access points and can't reliably reconnect to their real network while the badge is active. A front "Troll" button forces an immediate rescan, and a "perma-troll" switch puts the badge into a mode that automatically rescans every ~30 seconds. Rot13 labs made 100 of them, and says the SSIDs it (and its sibling badge, the Hackbutt V3) spoofed that year ended up as the most commonly seen network names at DEF CON 32.

Beyond the trolling, the badge doubles as a puzzle: connecting to it over USB opens a 9600-baud serial console that exposes a small on-board CTF, a debug-output toggle, and other hidden wifi-trolling modes, tracked with persistent storage so a solved flag sticks across reboots. Two NeoPixel-style RGB LEDs cycle colors while it runs, switching to a red pattern in one of its firmware Easter eggs.

## Make your own

The Arduino firmware (`troublemaker.ino`) is published in the [trollbadge GitHub repo](https://github.com/c0ldbru/trollbadge) "in case anyone wants to use/adjust/modify/steal/reuse it." No schematic, PCB layout, or bill of materials was found alongside it, so the hardware design itself is not confirmed to be open — only the firmware is.

## Notes merged from the duplicate entry "trollbadge (DC32 Troll Badge)"

The DC32 troll badge is a wifi-trolling badge made by C0ldbru of Rot13 Labs for DEF CON 32 (2024), cut into the shape of the "troll face" meme. By default it scans for nearby wifi networks and then rebroadcasts each found SSID as its own access point, one after another, flooding the local wireless environment with spoofed networks. A front "Troll" button forces an immediate rescan, and a "perma-troll" switch puts it into a mode that automatically rescans every 30 seconds or so.

Connecting to the badge over USB opens a 9600-baud serial console that exposes a small on-board CTF, a debug-output toggle, and other hidden wifi-trolling modes. Two NeoPixel-style RGB LEDs cycle random colors while the badge runs, switching to a red pattern in one of its firmware Easter eggs. The maker published the Arduino firmware ("troublemaker.ino") on GitHub for others to reuse, though no schematic or PCB files were found alongside it.

This entry duplicates an existing, more thoroughly researched entry for the same badge, `dc32-wifi-troll-badge`, which was built from the same GitHub repo plus the maker's own site and carries additional detail (price, a 100-unit production run, and distribution).
