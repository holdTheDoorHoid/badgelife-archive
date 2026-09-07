---
title: F5 CTF Badge
id: dc33-f5-ctf-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Abhinav SP - Hackerware.io
summary: A sponsor CTF badge for F5's Black Hat 2025 booth presence, built by Hackerwares/Abhinav SP.
functions: Flip a slide switch for a 3-second LED preview. Hold the CTF key and enter a binary flag (via 1/0 switches) to unlock that challenge's LEDs; hold the MODE key to change the LED blink pattern; hold 1 and 0 together to reset progress. Visiting F5 partner booths at Black Hat progressively unlocks badge sections.
look:
  colors: []
  shape: null
  themes:
  - ctf
  - security
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: Giveaway at Black Hat
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given away by F5 at Black Hat 2025; unlocked further by visiting F5 partner booths.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: Hackerware.io/f5
  url: https://Hackerware.io/f5
  kind: website
- label: F5 Badge CTF
  url: https://www.hackerware.io/f5-ctf
  kind: website
images:
- file: assets/images/badges/dc33/f5-ctf-badge/9ff83703e4.jpg
  source: "https://hackerware.io/f5"
  credit: "Hackerwares (Abhinav SP)"
  caption: "The F5 CTF badge as shown on the maker's site"
contact: {}
notes:
- Visit F5 booth at Blackhat.
status: released
sources:
- kind: sheet
  event: dc33
  row: 67
  updated: 8/4/2025
- kind: url
  url: https://hackerware.io/f5
  title: "Welcome To Hackerware — The F5 CTF Badge"
  accessed: '2026-09-06'
  note: Maker's own page describing the badge's gameplay (slide switch preview, binary flag entry via CTF/MODE/1/0 keys, booth-unlock mechanic) and the badge photo (f5.JPG).
- kind: url
  url: https://www.hackerware.io/f5-ctf
  title: F5 Badge CTF
  accessed: '2026-09-06'
  note: The CTF puzzle page itself (four challenges — Delivery, Security, XOps, Deployment); no hardware specs.
- kind: url
  url: https://hackerware.io/index.html
  title: "Hackerware - #BadgeLife | Hardware Design, Security, & Research."
  accessed: '2026-09-06'
  note: Confirms Hackerware/Hackerwares is run by Abhinav (page author meta), consistent with sheet's "Abhinav SP - Hackerware.io".
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    Distributed by F5 as a giveaway at Black Hat 2025 (not a DEF CON con-floor
    drop; kept under dc33 as imported from the sheet). No source gave the MCU,
    LED count/type, battery, board colors/shape, quantity made, or any
    hardware/firmware release — Hackerware's page describes gameplay only, with
    no schematic, repo, or BOM found. Left those fields empty rather than
    guess. WebSearch was unavailable (session budget exhausted) so coverage
    relied on the maker's own two pages plus curl of the site root; no
    Hackaday, press, or storefront listing was found for this specific badge.
last_modified_date: '2026-09-06'
---

The F5 CTF Badge was F5's entry into badgelife culture, built for the company by Abhinav SP of Hackerwares and given away at F5's booth during Black Hat 2025. The badge doubles as a lightweight puzzle console: a slide switch triggers a 3-second preview of the LEDs at full brightness, while the real game runs through four challenges (with security-flavored names like "Delivery," "Security," "XOps," and "Deployment") hosted on a companion CTF page. Solving a challenge yields a binary flag, which the holder enters on the badge itself using dedicated 1/0 switches while holding a CTF key; a correct flag permanently lights up that section of the badge. A separate MODE key cycles the LED blink pattern, and holding both 1 and 0 together resets all progress.

Beyond the puzzle mechanic, the badge was tied to Black Hat's expo floor: visiting F5's partner booths progressively unlocked additional sections, encouraging attendees to walk the show rather than solve everything at their desk. No technical specifications (microcontroller, LED type/count, power source, PCB color or shape) were published on the maker's site, and no GitHub repository, schematic, or bill of materials was found, so the badge's open-source status and internals remain undocumented as of this writing.
