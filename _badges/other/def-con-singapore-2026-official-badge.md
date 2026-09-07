---
title: DEF CON Singapore 2026 Official Badge
id: other-def-con-singapore-2026-official-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2026
makers:
- name: Circuit Crafters
  role: badge hardware
- name: Dani Weidman
  url: http://dani.pink/
  role: Laser* Tag game design (OpenLASIR protocol)
- name: Zach Resmer
  url: https://resmer.co.za/ch
  role: Laser* Tag game design assistance
summary: 'The official electronic badge for DEF CON Singapore 1 (DCSG1), 2026, built around an ESP32-C6. It runs a built-in infrared "Laser* Tag" game that turns the exhibit hall into a team-based tagging arena using the open OpenLASIR protocol.'
functions: 'Infrared "Laser* Tag" game: badges emit and receive coded IR "shots"; a valid hit (not against the same opponent within 15 minutes, and not against a teammate) scores a point. Players belong to one of five teams (Cyan, Magenta, Yellow, Blue, Orange); individual hits roll up into team and individual scores on an online leaderboard. Hits are stored locally on the badge and periodically synced. Internet-connected base stations around the venue talk to badges over ESP-NOW, with periodic channel/data-rate hopping. The badge also tracks whether hits came from official badges or third-party OpenLASIR-compatible devices.'
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
  - ctf
tech:
  mcu: ESP32-C6
  leds: null
  display: null
  connectivity:
  - ir
  - none
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
  firmware_url: https://github.com/danielweidman/OpenLASIR
  eda_tool: null
  notes: 'The badge hardware itself is not published; only the OpenLASIR IR protocol (used for the Laser* Tag game) is open, with MicroPython and Arduino code examples and official support in the Arduino-IRremote library. The Laser* Tag maker''s page invites third parties to build OpenLASIR-compatible devices and request their own device ID block to avoid collisions with official badges.'
links:
- label: www.dani.pink/lasertag/archive-sing/about
  url: https://www.dani.pink/lasertag/archive-sing/about
  kind: website
- label: OpenLASIR (GitHub)
  url: https://github.com/danielweidman/OpenLASIR
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- 'The event is DEF CON Singapore 1 (DCSG1), 2026 -- no matching event id exists yet in _data/events.yml (which currently has no Singapore entry), so this stays filed under "other".'
- 'ESP32-C6 badge; the earlier, separate 2025 "Laser* Tag Badge" dedicated device (a different item, see dc33-laser-tag-badge in the archive) ran on an RP2040 for comparison.'
status: released
sources:
- kind: url
  url: https://www.dani.pink/lasertag/archive-sing/about
  title: Laser* Tag Badge - DEF CON Singapore 2026 - About
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''unknown - DEF CON Singapore''.'
- kind: url
  url: https://www.dani.pink/lasertag/archive-sing/about
  title: Laser* Tag Badge - About (page content)
  accessed: '2026-09-07'
  note: 'Confirms badge maker (Circuit Crafters), game designers (Dani Weidman, Zach Resmer), ESP32-C6 MCU, IR/ESP-NOW gameplay mechanics, and OpenLASIR protocol; no price, quantity, or images of the badge on this page.'
- kind: url
  url: https://github.com/danielweidman/OpenLASIR
  title: danielweidman/OpenLASIR
  accessed: '2026-09-07'
  note: 'Confirms OpenLASIR protocol is officially used on the DEF CON Singapore 1 badge and reserves device ID block 35-64 for it; no badge images, price, or availability info.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only one primary source page was reachable (a game-feature sub-page of the badge maker''s Laser* Tag site) plus its linked OpenLASIR repo; web search quota was exhausted before broader searches (press coverage, storefront, forum posts) could be run, so price, quantity made, general availability, LED count/display, and photos of the badge itself remain unconfirmed. The source page describes the Laser* Tag game feature in detail but is not a full badge spec sheet, so overall badge appearance (colors/shape) and full tech spec are unknown. No matching "def con singapore" event id exists in _data/events.yml.'
last_modified_date: '2026-09-07'
---

The DEF CON Singapore 2026 official badge (DCSG1) was made by Circuit Crafters and is built around an ESP32-C6. Its standout feature is a built-in infrared "Laser* Tag" game, designed by Dani Weidman with help from Zach Resmer, that turns the conference's exhibit hall into a team-based tagging arena: badges fire and detect coded IR "shots," valid hits score points (subject to a 15-minute cooldown per opponent and no friendly fire), and results roll up to team and individual standings on an online leaderboard synced from each badge.

Play is supported by internet-connected base stations placed around the venue that talk to badges over ESP-NOW with periodic channel and data-rate hopping, and the badge distinguishes hits from official badges versus third-party devices. The underlying IR protocol, OpenLASIR, is intentionally open — it's documented with MicroPython and Arduino examples, is supported directly in the Arduino-IRremote library, and DEF CON Singapore reserved it a block of device IDs (35-64) so hobbyists can build their own compatible IR "blasters" without colliding with official badges. The badge hardware design itself has not been published; only the game/protocol layer is open source.

This is a distinct device from the earlier, standalone 2025 "Laser* Tag Badge" (a dedicated RP2040-based tagging device, also by Dani Weidman) already documented elsewhere in this archive — the DEF CON Singapore badge instead builds the same game into the conference's own ESP32-C6 badge.
