---
title: SEC DTMF Phone badge
id: dc32-sec-dtmf-phone-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Social Engineering Community
  url: https://www.se.community/
- name: Cyber City Circuits
  role: design and fabrication
summary: A retro-style desk-phone badge for the SEC Village at DEF CON 32, built
  around a real DTMF tone generator chip so it dials and plays actual touch-tone
  sounds.
functions: Dial-pad buttons generate real DTMF tones through a dedicated Holtek
  chip and drive 10 RGB LEDs; the badge is Arduino-programmable, and the village
  ran a programming station where attendees could load their own code (challenges
  ranged from simple LED patterns tied to keypad input to more advanced sequences).
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - phone
  - security
tech:
  mcu: ATmega328PB
  leds:
    count: 10
    type: RGB
    note: Described by the maker as "read [reverse] mounted" RGB LEDs.
  display: none
  connectivity:
  - audio
  battery: 2x AA
  sao_version: null
get_one:
  price: $80.00
  price_usd: 80.0
  quantity: limited quantity
  availability: sold_out
  distribution:
  - purchase
  where: Sold in person at the SEC Village during DEF CON 32 (cash or card); DEF
    CON 32 has since ended, so it is no longer available for purchase.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/secommunity/SEC-DEF-CON-32-Phone-Badge/blob/main/SEC%20Village%20Phone%20Badge%202024%20Schematic.pdf
  firmware_url: https://github.com/secommunity/SEC-DEF-CON-32-Phone-Badge/blob/main/DTMF_Dialer_-_Prod.ino
  eda_tool: null
links:
- label: www.se.community/2024-sec-phone-badge
  url: https://www.se.community/2024-sec-phone-badge/
  kind: website
- label: x.com/sec_defcon
  url: https://x.com/sec_defcon
  kind: social
- label: github.com/secommunity/SEC-DEF-CON-32-Phone-Badge
  url: https://github.com/secommunity/SEC-DEF-CON-32-Phone-Badge
  kind: repo
images:
- file: assets/images/badges/dc32/sec-dtmf-phone-badge/fe646158ca.png
  source: "https://www.se.community/2024-sec-phone-badge/"
  credit: "Social Engineering Community / Cyber City Circuits"
  caption: "The SEC DTMF phone badge, front view"
contact: {}
notes:
- The maker's own page (se.community) is now under construction and no longer
  serves the badge page; details here come from an Internet Archive Wayback
  Machine capture of the live page from 2024-09-30.
status: released
sources:
- kind: sheet
  event: dc32
  row: 100
  updated: ''
- kind: url
  url: https://web.archive.org/web/20240930232558/https://www.se.community/2024-sec-phone-badge/
  title: 2024 SEC Phone Badge — SE.COMMUNITY (Wayback Machine capture)
  accessed: '2026-09-06'
  note: Primary source for description, chip, LEDs, battery, price, quantity, GitHub
    link, and the badge photo. The live page now redirects to an under-construction
    placeholder.
- kind: url
  url: https://github.com/secommunity/SEC-DEF-CON-32-Phone-Badge
  title: secommunity/SEC-DEF-CON-32-Phone-Badge on GitHub
  accessed: '2026-09-06'
  note: Confirmed repo contents (Arduino sketch, schematic PDF, README with programming
    instructions); no separate license file found.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts (maker, chip, LEDs, battery, price, distribution, open-source
    files) are confirmed directly from the maker's own page (via Wayback Machine,
    since the live site is now a placeholder) and the maker's GitHub repo. No EDA
    tool or license was stated anywhere found, so those remain null/empty. PCB
    color/shape were not confirmed from a clear enough source and are left empty
    rather than guessed from the product photo alone. A related sheet entry,
    dc32-cyber-city-circuits-listed-for-def-con-32-no-details, is very likely this
    same badge (Cyber City Circuits co-designed it with SEC) but is a separate
    file and was not touched.
last_modified_date: '2026-09-06'
---

The SEC DTMF Phone Badge was the Social Engineering Community's first-ever village badge, made for their village at DEF CON 32 (2024). SEC partnered with Cyber City Circuits — who had already worked with them on the prior year's "Flux Decoder" Youth Challenge badge — to design a retro desk-phone-styled board built around a real Holtek HT9200B DTMF tone generator chip, so pressing the keypad produces genuine touch-tone dialing sounds rather than a simulated approximation. An ATmega328PB runs the show, driving 10 RGB LEDs from an 11-button front keypad (10 digits plus a utility button) and a second utility button on the back, all powered by 2 AA batteries.

Badges were sold in limited quantity in person at the SEC Village for $80 (tax included), cash or card. The village also ran a programming station where attendees could flash their own code onto the badge on the spot. SEC published the full schematic and the production Arduino sketch on GitHub, with README notes covering the Minicore board settings, ISP programmer setup, and warnings about not powering the badge from a programmer while its batteries are still installed — plus a few suggested programming challenges of increasing difficulty for people who wanted to hack on it further.

As of this research, the maker's own event page for the badge (se.community) has been replaced by a generic "under construction" placeholder; all details above were recovered from an Internet Archive capture of the live page from shortly after DEF CON 32.

## Make your own

Everything needed to build or reprogram the badge is on GitHub at [secommunity/SEC-DEF-CON-32-Phone-Badge](https://github.com/secommunity/SEC-DEF-CON-32-Phone-Badge):

1. Get the schematic (`SEC Village Phone Badge 2024 Schematic.pdf`) if you're building the hardware yourself.
2. Install the Arduino IDE with the MiniCore board package, the ButtonMatrix library, and the Adafruit MCP23017 library.
3. Select board "ATMEGA328", clock "Internal 8MHz", variant "328PB" under MiniCore, with an Arduino-as-ISP programmer.
4. Remove the AA batteries before connecting a programmer's VCC line, to avoid damaging the batteries or the badge.
5. Flash `DTMF_Dialer_-_Prod.ino` using Sketch → Upload Using Programmer.
