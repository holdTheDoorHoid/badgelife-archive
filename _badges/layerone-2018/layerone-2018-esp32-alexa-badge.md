---
title: LayerOne 2018 Badge (Mr. Meeseeks)
id: layerone-2018-layerone-2018-esp32-alexa-badge
layout: badge
parent: LayerOne 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: layerone-2018
year: 2018
makers:
- name: LayerOne / null space labs
summary: Official LayerOne 2018 conference badge built around an ESP32-WROOM-32, with a speaker/mic and WiFi-based Amazon Alexa integration that announces "I'm Mr. Meeseeks, Look at me!" when it joins the conference network.
functions: Connects to the conference "badgenet" WiFi and periodically announces itself over its onboard speaker via Alexa integration ("I'm Mr. Meeseeks, Look at me!"), a Rick and Morty reference. Has five buttons (power, BOOT, RESET, "DO NOT PRESS," and "MR MEESEEKS") and through-hole solder points around the perimeter for expansion.
look:
  colors: []
  shape: null
  themes:
  - tv
  - meme
  - pop culture
tech:
  mcu: ESP32-WROOM-32
  leds:
    count: 4
    type: null
    note: null
  display: none
  connectivity:
  - wifi
  - audio
  battery: 18650 (UltraFire)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed as the official conference badge to LayerOne 2018 attendees; an optional SMD blinking-logo add-on kit was also offered.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/badges/layerone-2018-esp32-alexa-badge
  url: https://badge.gallery/badges/layerone-2018-esp32-alexa-badge
  kind: website
- label: hackaday.com/2018/05/29/badge-bling-and-more-at-layerone-2018
  url: https://hackaday.com/2018/05/29/badge-bling-and-more-at-layerone-2018/
  kind: article
images:
- file: assets/images/badges/layerone-2018/layerone-2018-esp32-alexa-badge/ddec98fe99.gif
  source: https://hackaday.com/2018/05/29/badge-bling-and-more-at-layerone-2018/
  credit: Hackaday / LayerOne 2018
  caption: The 2018 LayerOne ESP32 badge PCB
- file: assets/images/badges/layerone-2018/layerone-2018-esp32-alexa-badge/ddec98fe99.gif
  source: https://hackaday.com/2018/05/29/badge-bling-and-more-at-layerone-2018/
  credit: Hackaday / LayerOne
  caption: LayerOne 2018 Mr. Meeseeks conference badge
- file: assets/images/badges/layerone-2018/layerone-2018-esp32-alexa-badge/e6dbb05a4a.jpg
  source: https://hackaday.com/2018/05/29/badge-bling-and-more-at-layerone-2018/
  credit: Hackaday / LayerOne
  caption: LayerOne 2018 badge with SMD blinking logo add-on kit
contact: {}
notes:
- ESP32-based official badge for LayerOne 2018, covered in Hackaday's badge roundup for that year. Found by the event-year sweep, task con-layerone.
- The sweep's title ("ESP32 Alexa Badge") describes the badge's function; retitled to match the maker's own framing (the "MR MEESEEKS" button and Alexa announcement line), matching entry layerone-2018-layerone-2018-badge-mr-meeseeks, which covers the identical board and appears to be a duplicate created by a separate sweep pass.
- ESP32-WROOM-32 LayerOne 2018 badge with speaker/mic, Alexa integration and Rick-and-Morty theming ("I'm Mr. Meeseeks"), plus an offered SMD blinking add-on kit. Found by the event-year sweep, task general-2016.
- Sweep title matches the maker's own framing (the badge's "MR MEESEEKS" button and Alexa line); no separate official title was found.
status: listed
sources:
- kind: url
  url: https://badge.gallery/badges/layerone-2018-esp32-alexa-badge
  title: LayerOne 2018 ESP32 Alexa Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''LayerOne 2018''.'
- kind: url
  url: https://hackaday.com/2018/05/29/badge-bling-and-more-at-layerone-2018/
  title: Badge Bling And More At LayerOne 2018
  accessed: '2026-09-08'
  note: 'Confirmed badge details: ESP32-WROOM-32, speaker/mic, four LEDs, five buttons, 18650 (UltraFire) battery, WiFi Alexa integration, perimeter GPIO pads, and the SMD blinking-logo add-on kit; source code was promised but not released at time of writing.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: This entry duplicates layerone-2018-layerone-2018-badge-mr-meeseeks, an already-researched entry for the same board (see that entry's research.notes). Could not confirm a specific individual maker beyond "LayerOne" / the event organizers (Hackaday credits the group, not a named designer); "null space labs" is carried over from the sheet import and unconfirmed. Could not find price, quantity made, availability, or design-file links; firmware was reportedly promised in 2018 coverage but no release was found. Merged with duplicate entry 'LayerOne 2018 Badge (Mr. Meeseeks)' (layerone-2018-layerone-2018-badge-mr-meeseeks).
last_modified_date: '2026-09-08'
redirect_from:
- /badges/layerone-2018/layerone-2018-badge-mr-meeseeks/
---

The LayerOne 2018 conference badge was built around an ESP32-WROOM-32 module and doubled as a running gag for the weekend: once it joined the conference's "badgenet" WiFi, it used Amazon Alexa integration and an onboard speaker to announce "I'm Mr. Meeseeks, Look at me!" — a Rick and Morty reference — each time it (re)connected. With hundreds of badges on one network, the line kept interrupting talks throughout the con as devices dropped and rejoined.

Beyond the audio gag, the badge carried four LEDs, ran off an 18650 cell (an UltraFire unit was the one photographed), and had five labeled buttons: power, BOOT, RESET, "DO NOT PRESS," and "MR MEESEEKS." Perimeter through-hole pads left room for attendees to add their own hardware. LayerOne also offered an optional surface-mount add-on kit featuring a blinking version of the conference logo.

This entry was created independently of layerone-2018-layerone-2018-badge-mr-meeseeks, which covers the same physical badge; see that entry for the fuller writeup. Hackaday's coverage noted that source code for the badge had been promised but was not yet public at the time of writing, and no later release was found during this research pass.

## Notes merged from the duplicate entry "LayerOne 2018 Badge (Mr. Meeseeks)"

The LayerOne 2018 badge was built around an ESP32-WROOM-32 module and doubled as a running gag for the weekend: once it joined the conference's "badgenet" WiFi, it used Amazon Alexa integration and an onboard speaker to announce "I'm Mr. Meeseeks, Look at me!" — a Rick and Morty reference — each time it (re)connected. With hundreds of badges on one network, that meant the line kept interrupting talks throughout the con as devices dropped and rejoined.

Beyond the audio gag, the badge carried four LEDs, ran off an 18650 cell (an UltraFire unit was the one photographed), and had five labeled buttons: power, BOOT, RESET, "DO NOT PRESS," and "MR MEESEEKS." Perimeter through-hole pads left room for attendees to add their own hardware. LayerOne also offered an optional surface-mount add-on kit featuring a blinking version of the conference logo, aimed at people who wanted extra soldering practice or bling to show off.

Hackaday's coverage noted that source code for the badge had been promised but was not yet public at the time of writing; no later firmware or hardware release was found during this research pass.
