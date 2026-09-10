---
title: DEF CON 26 main con badge
id: dc26-def-con-26-main-con-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Tymkrs
summary: The official electronic badge for DEF CON 26 (2018), an interactive "DEFCON City" narrative badge built around a 1983 Orwellian-collapse story where attendee choices affect alignment and relationships with other badges.
functions: Interactive story/game controlled with a directional pad and +/- buttons; a red "guard" character reacts as friend or enemy depending on choices; the DEFCON logo lights red or green to show moral alignment; badges unlock additional puzzles when linked to other badges via header pins or plugged into a computer over USB, which also exposes an ASCII-art terminal game.
look:
  colors:
  - black
  - white
  - red
  - blue
  shape: rectangle
  themes:
  - cyberpunk
  - puzzle
  - ctf
  form_factor: pcb badge
tech:
  mcu: PIC32MM0256GPM (48-pin TQFP)
  leds:
    count: 30
    type: null
    note: LEDs light the DEFCON logo and other badge elements red/green to reflect story alignment.
  display: none
  connectivity:
  - usb
  battery: 4x AA (6V total); also USB-powered
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Issued to DEF CON 26 attendees at Caesars Palace, Las Vegas (Aug 9-12, 2018); seven variants (soldermask/silkscreen color combinations) marked different attendee roles, e.g. white/black for general "Human" attendees, red/white for Goons, blue/white for Speakers, plus Contest, Artist, Press, Vendor, and CFP variants.
make_your_own:
  open_source: yes
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: DEF CON posted a post-con firmware update and write-up on the DEF CON media server for people who want to keep hacking on the badge; the design is treated as open for attendees to modify.
links:
- label: defcon.org/html/links/dc-badge.html
  url: https://defcon.org/html/links/dc-badge.html
  kind: website
- label: HackerNoon — Exploring The DEF CON 26 Badge
  url: https://hackernoon.com/exploring-the-def-con-26-badge-dfcae0a5746d
  kind: article
- label: DEF CON 26 badge write-up (PDF, DEF CON media server)
  url: https://media.defcon.org/DEF%20CON%2026/DEF%20CON%2026%20badge/DEF%20CON%2026%20badge%20writeup.pdf
  kind: doc
- label: r/Tymkrs — DEFCON 26 Badge discussion
  url: https://www.reddit.com/r/Tymkrs/comments/95tgfc/defcon_26_badge/
  kind: social
images:
- file: assets/images/badges/dc26/def-con-26-main-con-badge/83d06eecc8.jpg
  source: "https://hackernoon.com/exploring-the-def-con-26-badge-dfcae0a5746d"
  credit: "Vince Tabora / HackerNoon"
  caption: "The DEF CON 26 human badge worn around the neck"
contact: {}
notes:
- Sweep originally listed only the defcon.org badge-info page as source; title and maker were already correct on the sheet.
status: released
sources:
- kind: url
  url: https://defcon.org/html/links/dc-badge.html
  title: DEF CON 26 main con badge
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://defcon.org/html/links/dc-badge.html
  title: "DEF CON® Hacking Conference - The Badge"
  accessed: '2026-09-10'
  note: Confirmed theme ("DEFCON City"), maker Tymkrs, gameplay mechanics, and role-based color variants.
- kind: url
  url: https://hackernoon.com/exploring-the-def-con-26-badge-dfcae0a5746d
  title: Exploring The DEF CON 26 Badge - HackerNoon
  accessed: '2026-09-10'
  note: Supplied dimensions (8"x3"), MCU (PIC32MM0256GPM), LED count (30), battery (4x AA), micro-USB port, capacitive buttons, and USB terminal game detail.
- kind: url
  url: https://defcon.org/html/defcon-26/dc-26-index.html
  title: DEF CON 26 Hacking Conference
  accessed: '2026-09-10'
  note: Confirmed a post-con firmware update and write-up were published for the badge on the DEF CON media server.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Maker's own defcon.org page and a firsthand hands-on article (HackerNoon) confirm the badge and its core specs; could not reach the DEF CON media server (403) or the official write-up PDF to verify price/quantity or firmware/hardware source links, so get_one.price, quantity, and make_your_own URLs are left empty. LED type/color model not specified in sources found.
last_modified_date: '2026-09-10'
---

The DEF CON 26 main conference badge, built by the Minnesota-based collective Tymkrs for the 2018 con at Caesars Palace, is an interactive electronic badge wrapped in a dystopian "DEFCON City" narrative set in an alternate 1983. Wearers make choices via touch-capacitive buttons under the DEFCON logo and a directional pad, and those choices shift a red "guard" character between friend and enemy while the DEFCON logo's LEDs shift between red and green to reflect the wearer's moral alignment. The badge shipped in seven color-coded soldermask/silkscreen variants marking attendee role — Human, Goon, Speaker, Contest, Artist, Press, Vendor, and CFP — and badges can link to each other through header pins to unlock further puzzles.

Physically the badge measures about 8" x 3", runs on 4 AA batteries (6V) with a fallback of USB power via a micro-USB port, and is driven by a Microchip PIC32MM0256GPM processor (48-pin TQFP) with around 30 onboard LEDs. Plugging the badge into a computer over USB also exposes an ASCII-art terminal-style game in addition to powering it. DEF CON later posted a firmware update and a write-up for the badge on the DEF CON media server, which the archive could not reach directly (403 error) to pull the primary hardware/firmware links or confirm price and production quantity.
