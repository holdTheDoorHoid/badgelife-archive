---
title: Hackbutt v.3 wifi testing badge
id: dc31-hackbutt-v-3-wifi-testing-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: C0ldbru (Rot thirteen labs)
  url: https://rot13labs.com
summary: A dickbutt-meme-shaped PCB badge from Rot13 Labs built around an ESP8266 running a customized fork of the SpacehuhnTech deauther, giving it wifi scanning, deauthentication, and SSID-spoofing features behind an onboard OLED screen and three-button menu.
functions: Wifi scanning and 802.11 deauthentication ("wifi testing") via a Hackbutt-v3 fork of the ESP8266 Deauther firmware; onboard OLED display navigated with back/up/enter buttons; shipped with default spoofed SSIDs that the maker says became some of the most commonly seen network names at DEF CON that year, alongside the badge's sibling project, the Duckbutt SAO.
look:
  colors:
  - black
  - white
  shape: other
  themes:
  - meme
  - security
  - radio
  - pop culture
  form_factor: pcb badge
tech:
  mcu: ESP8266
  leds: null
  display: small OLED
  connectivity:
  - wifi
  inputs:
  - buttons
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed by C0ldbru (Rot13 Labs) around DEF CON 31 (2023), packaged like a parody VHS rental tape ("Hackbutt v3: Wireless Chaos") with a membership card and stickers. The community sheet noted units were still being smoke tested for quality shortly before the con; price, quantity, and whether it was sold or given away were not found.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/c0ldbru/esp8266_deauther_hackbutt
  eda_tool: null
  notes: Firmware is a fork of SpacehuhnTech's ESP8266 Deauther adapted for "Hackbutt v3" (repo created May 2023). No schematic, Gerbers, or BOM were found in the repo or on the maker's site, so hardware files are not confirmed open.
links:
- kind: website
  label: Rot13 Labs (maker portfolio)
  url: https://rot13labs.com
  archived: https://web.archive.org/web/20260615020751/https://rot13labs.com/
- kind: repo
  label: esp8266_deauther_hackbutt firmware (GitHub)
  url: https://github.com/c0ldbru/esp8266_deauther_hackbutt
images:
- file: assets/images/badges/dc31/hackbutt-v-3-wifi-testing-badge/6f66403cdc.png
  source: https://rot13labs.com/
  credit: C0ldbru (Rot13 Labs)
  caption: Hackbutt v3 badge and its retail-style packaging, as shown in the maker's portfolio
  archived: https://web.archive.org/web/20260615020751/https://rot13labs.com/
contact: {}
notes: []
status: released
sources:
- kind: sheet
  event: dc31
  row: 19
  updated: '2023-06-21'
- kind: url
  url: https://rot13labs.com/
  title: Rot13 Labs — portfolio (C0ldbru)
  accessed: '2026-09-07'
  note: Confirms the Hackbutt V3 badge, describes the deauth/SSID-spoofing features it shares with the Duckbutt SAO, and supplied the product photo.
  archived: https://web.archive.org/web/20260615020751/https://rot13labs.com/
- kind: url
  url: https://github.com/c0ldbru/esp8266_deauther_hackbutt
  title: esp8266_deauther_hackbutt (GitHub)
  accessed: '2026-09-07'
  note: Firmware repo, a fork of SpacehuhnTech's ESP8266 Deauther adapted for "Hackbutt v3"; created May 2023, corroborating the DEF CON 31 timeframe and the ESP8266 chip.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Confirmed via the maker's own portfolio (rot13labs.com) and GitHub repo, plus the maker's own product photo. Price, quantity made, and current availability are not published anywhere found, and it's unconfirmed whether the badge was sold or given away. The maker's portfolio also shows a second, unlabeled "Hackbutt Badge" (no version number, project
last_modified_date: '2026-09-07'
---

The Hackbutt v3 is a PCB badge from C0ldbru of Rot13 Labs, shaped like the "dickbutt" internet meme and built around an ESP8266 running a heavily modified fork of SpacehuhnTech's popular ESP8266 Deauther firmware. It adds wifi scanning and deauthentication attacks to a badge form factor, with an onboard OLED screen and a three-button (back/up/enter) menu for navigating features. The maker's site notes that the badge's default spoofed SSIDs, shared with its sibling project the Duckbutt SAO released the same year, ended up among the most commonly broadcast network names at DEF CON that year.

It shipped in a tongue-in-cheek retail package styled after a VHS rental tape — "HACKBUTT v3: WIRELESS CHAOS," complete with a mock "Category: Romance / Rating: R / DC:31" rental sticker, a "Hackbutt Membership Card," and stickers reading "Hack the planet with your butt" — bundled with a Rot13 Labs lanyard. The community badge sheet recorded it as still being smoke-tested for quality shortly before DEF CON 31; no price, production quantity, or sales channel could be confirmed from public sources.

## Make your own

The firmware is public: [esp8266_deauther_hackbutt](https://github.com/c0ldbru/esp8266_deauther_hackbutt) is C0ldbru's fork of SpacehuhnTech's ESP8266 Deauther, adapted for the Hackbutt v3 hardware. No hardware design files (schematic, Gerbers, or BOM) were found published for the badge itself, so building the physical board would require reverse-engineering it from photos.
