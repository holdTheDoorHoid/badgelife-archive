---
title: UltraViolet Sponsor Badge
id: saintcon-2023-ultraviolet-sponsor-badge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: Jup1t3r
summary: A beginner-level SAINTCON 2023 sponsor minibadge for UltraViolet Cyber, a purple PCB shaped like the sponsor's "U" logo with a single through-hole LED.
functions: 'No electronic functions beyond lighting the single LED once assembled; a soldering-practice sponsor giveaway rather than an interactive badge.'
look:
  colors:
  - purple
  shape: logo
  themes:
  - security
  - logo
  - minimalist
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: 5mm through-hole LED, bent over to sit in the middle of the badge
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Handed out at the UltraViolet Cyber booth in the SAINTCON 2023 vendor area
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  kind: doc
- label: MiniBadge Wiki (community catalog)
  url: https://minibadge.wiki/
  kind: website
images:
  - file: assets/images/badges/saintcon-2023/ultraviolet-sponsor-badge/d69b4f2b28.png
    source: "https://minibadge.wiki/"
    credit: "Jup1t3r / SAINTCON Minibadge Guide"
    caption: "Front of the badge, purple PCB with UltraViolet's 'U' logo"
  - file: assets/images/badges/saintcon-2023/ultraviolet-sponsor-badge/96ea0576f0.jpg
    source: "https://minibadge.wiki/"
    credit: "Jup1t3r / SAINTCON Minibadge Guide"
    caption: "Back of the badge showing the LED, resistor, and ultraviolet logo/URL"
contact: {}
notes:
- 2023 sponsor minibadge for UltraViolet Cyber. Found by the event-year sweep, task saintcon-2023.
- 'The official minibadge guide titles it "UltraViolet SPONSOR BADGE" (all caps); rendered here in title case per archive convention.'
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: UltraViolet Sponsor Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2023); event read as ''saintcon-2023''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: 2023 SAINTCON Minibadge Guide, page 9 (UltraViolet Sponsor Badge)
  accessed: '2026-09-10'
  note: Confirmed the badge is real (not just a sheet listing); read designer, description, difficulty/rarity, parts list (5mm THT LED, 1206 SMD resistor, FR4 PCB, 2-pin headers), assembly steps, and "how to get one" text; viewed the front/back photos on the page.
- kind: url
  url: https://raw.githubusercontent.com/Pips801/minibadge-wiki/main/2023.json
  title: minibadge-wiki 2023 data (Pips801/minibadge-wiki)
  accessed: '2026-09-10'
  note: Community-maintained structured record for this badge; matched the PDF guide's text exactly and supplied direct image URLs used for the saved photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: >-
    Core facts (maker, sponsor, event, appearance, parts, single LED, free at the vendor
    booth) confirmed via the official SAINTCON minibadge guide PDF and the independent
    minibadge.wiki community catalog, which agree word-for-word. No maker's-own page for
    UltraViolet Cyber was checked for corroboration, and no quantity-made figure was
    published (minibadge-wiki lists 0, which reads as "not recorded" rather than zero
    made). No SAO header — the 2-pin headers are for the minibadge chaining/display
    convention, not an SAO connector, so sao_version is set to none. No design files
    (KiCad/Gerbers) were found; make_your_own left null/empty.
last_modified_date: '2026-09-10'
---

The UltraViolet Sponsor Badge is a SAINTCON 2023 minibadge designed by Jup1t3r for UltraViolet Cyber, described in the official minibadge guide as "one of our newest sponsors." It is a small purple PCB shaped like UltraViolet's "U" logo, with a single 5mm through-hole LED bent over to sit in the middle of the badge, a 1206 SMD current-limiting resistor, and 2-pin headers on an FR4 board. The back carries the UltraViolet wordmark and the URL uvcyber.com.

Rated beginner difficulty and common rarity in the guide, it was a free giveaway: attendees got one by visiting the UltraViolet Cyber booth in the vendor area rather than buying or trading for it. No quantity-made figure, storefront, or open-source design files were found for it.
