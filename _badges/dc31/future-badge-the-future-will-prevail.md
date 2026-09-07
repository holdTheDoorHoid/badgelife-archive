---
title: Future Badge (The Future will Prevail)
id: dc31-future-badge-the-future-will-prevail
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Alt_Bier
summary: A Back to the Future / DeLorean themed movie-ticket-shaped badge made for DEF CON 31's "The Future Will Prevail" theme, with a capacitive-touch DeLorean, backlit solder-mask art, and a hidden WiFi CTF.
functions: Capacitive-touch DeLorean triggers LED effects (color-changing logo, flickering tire tracks, strobing lightning); holding the touch pad about 30 seconds switches the badge into an ESP32 WiFi access-point mode ("FUTURE-BADGE") hosting a Back to the Future themed hacking CTF.
look:
  colors: []
  shape: rectangle
  themes: [movie, sci-fi, retro computer, ctf]
tech:
  mcu: ESP32
  leds:
    count: 14
    type: RGB
    note: 'Per a third-party badge review: 4 WS2812 RGB addressable LEDs, plus 4 red/yellow LEDs, 4 blue LEDs, and 2 white discrete LEDs.'
  display: null
  connectivity: [wifi]
  battery: 9V (two included per kit; ~7-8 hours runtime)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  availability_note: 'A third-party review posted 2024-02-25 said a few were still available on Alt_Bier''s eBay store; not independently reconfirmed on 2026-09-07.'
  distribution: [crowdfunding, kit]
  where: Distributed via an Indiegogo crowdfunding campaign as a DIY solder kit or assembled badge; some later resold via the maker's eBay store.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/gowenrw/future_badge
  firmware_url: https://github.com/gowenrw/future_badge
  eda_tool: KiCad
  notes: 'GitHub repo (gowenrw/future_badge) contains art, code, KiCad (6.x) EDA files, and docs; licensed MIT. The maker''s own project site (futurebadge.altbier.us) hosts assembly instructions, schematics and build videos. The compiled CTF challenge library itself is not open source; everything else is.'
links:
- label: futurebadge.altbier.us
  url: https://futurebadge.altbier.us/
  kind: website
- label: gowenrw/future_badge (GitHub)
  url: https://github.com/gowenrw/future_badge
  kind: repo
- label: 'Badge Review: Future Badge by @alt_bier (t.fish)'
  url: https://tdot.fish/2024/02/25/futurebadge
  kind: article
- label: 'Walkthru: Future Badge by @alt_bier (t.fish)'
  url: https://tdot.fish/2024/02/25/futurebadge-walkthru
  kind: article
images:
- file: assets/images/badges/dc31/future-badge-the-future-will-prevail/3ca8dc5546.jpg
  source: "https://futurebadge.altbier.us/"
  credit: "Alt_Bier"
  caption: "Future Badge hero shot, Back to the Future themed DEF CON 31 badge"
- file: assets/images/badges/dc31/future-badge-the-future-will-prevail/f8b0f4b690.jpg
  source: "https://tdot.fish/2024/02/25/futurebadge"
  credit: "t.fish"
  caption: "PCB detail showing assembly silkscreen and stacked-board design"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- 'This appears to be a duplicate of the existing entry dc31-the-future-will-prevail (same maker Alt_Bier, same badge, same DEF CON 31 Indiegogo campaign). That entry additionally credits Richard Gowen (campaign owner) and Brian Culver as team members, and records pricing/quantity ($60 kit / $100 assembled; 120 kits offered, 65 claimed; 35 assembled, sold out) from an archived Indiegogo snapshot.'
status: released
sources:
- kind: url
  url: https://futurebadge.altbier.us/
  title: Future Badge (The Future will Prevail)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc31''. Maker''s own project page: theme, DeLorean/capacitive touch concept, ESP32, WiFi, 9V battery, open-source GitHub repo link, hero image.'
- kind: url
  url: https://github.com/gowenrw/future_badge
  title: gowenrw/future_badge
  accessed: '2026-09-07'
  note: 'Confirms repo contains art/code/eda(KiCad 6.x)/docs for the DC31 badge; license set to MIT.'
- kind: url
  url: https://tdot.fish/2024/02/25/futurebadge
  title: 'Badge Review: Future Badge by @alt_bier'
  accessed: '2026-09-07'
  note: 'Third-party hands-on review: detailed LED breakdown (4 WS2812 + 4 red/yellow + 4 blue + 2 white), 9V battery runtime, two-PCB sandwich construction, WiFi AP CTF mode details ("FUTURE-BADGE" SSID), lanyard, eBay availability as of 2024-02-25, image URLs.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Likely a duplicate of dc31-the-future-will-prevail (same maker and badge); reported as such rather than merged, per instructions. Price and exact quantity for this specific listing could not be independently confirmed here (Indiegogo page is now behind a Cloudflare challenge and could not be fetched); the sibling entry has those figures from an archived snapshot. Current (2026) availability not reconfirmed beyond the 2024 review.'
last_modified_date: '2026-09-07'
---

The Future Badge is a Back to the Future themed electronic badge Alt_Bier made for DEF CON 31, whose conference theme, "The Future Will Prevail," suggested the time-traveling DeLorean. The badge is cut to an oblong, movie-ticket-like shape and its front artwork — the Hill Valley courthouse clock tower, a sports almanac, Doc Brown, a time-machine dashboard readout, and a silver DeLorean hitting 88 MPH — is built from two stacked PCBs with backlit solder-mask voids, hiding the electronics between the boards while highlighting the art.

An ESP32 drives the badge's lighting (WS2812 RGB LEDs plus discrete red/yellow, blue, and white LEDs) and a capacitive-touch pad on the silver DeLorean toggles effects such as a color-changing logo, flickering tire tracks, and strobing lightning. Holding that touch pad for about thirty seconds switches the badge into a WiFi access-point mode, broadcasting an SSID of "FUTURE-BADGE" that hosts a hidden, Back to the Future themed CTF puzzle. The badge runs on a 9V battery (two included) for roughly seven to eight hours and ships as a mostly through-hole DIY solder kit, with silkscreened assembly guidance directly on the PCB, alongside fully-assembled units.

It was distributed through an Indiegogo crowdfunding campaign, with rewards picked up at DEF CON 31; a hands-on review from February 2024 noted a few units still available afterward through the maker's eBay store. All hardware and firmware (save the compiled CTF challenge library) are published on GitHub under the MIT license, with build videos and documentation on the maker's own project site.

This entry closely tracks another archive entry, `dc31-the-future-will-prevail`, for what appears to be the same badge and campaign; see that entry for pricing and quantity details pulled from an archived Indiegogo snapshot.
