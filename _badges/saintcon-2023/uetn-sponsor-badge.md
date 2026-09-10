---
title: UETN Sponsor Badge
id: saintcon-2023-uetn-sponsor-badge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: Jup1t3r
summary: A sponsor minibadge for UETN (Utah Education and Telehealth Network), a longtime SAINTCON partner, given away by UETN staff at SAINTCON 2023.
functions: 'No interactive function beyond the standard minibadge chain: two SMD LEDs (D1, D2) wired across the board''s corner headers so the badge lights up when connected to neighboring minibadges.'
look:
  colors:
  - purple
  shape: rectangle
  themes:
  - logo
  - text
tech:
  mcu: none
  leds:
    count: 2
    type: SMD
    note: Two small LEDs (D1, D2) and one resistor (R1), wired in series across the corner headers; lights when chained with other minibadges.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: limited
  distribution:
  - free_drop
  where: 'Handed out by UETN employees on the SAINTCON 2023 show floor ("Find a UETN employee and ask for one").'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  kind: website
- label: Minibadge Wiki (Pips801/minibadge-wiki)
  url: https://github.com/Pips801/minibadge-wiki
  kind: repo
images:
  - file: assets/images/badges/saintcon-2023/uetn-sponsor-badge/5206ab970b.png
    source: "https://github.com/Pips801/minibadge-wiki"
    credit: "Jup1t3r"
    caption: "UETN Sponsor Badge, front"
  - file: assets/images/badges/saintcon-2023/uetn-sponsor-badge/6baf1fcaa9.png
    source: "https://github.com/Pips801/minibadge-wiki"
    credit: "Jup1t3r"
    caption: "UETN Sponsor Badge, back"
contact: {}
notes:
- 2023 sponsor minibadge for UETN (Utah Education and Telehealth Network). Found by the event-year sweep, task saintcon-2023.
- The community minibadge-wiki data entry titles it identically ("UETN Sponsor Badge"); no title change needed.
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: UETN Sponsor Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2023); event read as ''saintcon-2023''.'
- kind: url
  url: https://github.com/Pips801/minibadge-wiki
  title: Minibadge Wiki (Pips801/minibadge-wiki) — 2023.json entry for "UETN Sponsor Badge"
  accessed: '2026-09-10'
  note: 'Maker (Jup1t3r), description, category (Sponsor), soldering difficulty (Intermediate SMD), rarity (Rare), and how-to-acquire text; also source of the front/back board photos.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Quantity made is not recorded in the community wiki (listed as 0/unknown). No maker repo, Gerbers, or storefront found for this specific minibadge, so make_your_own fields stay empty. The board itself is a simple 2-LED "chain" minibadge with a large UETN "e" logo (from UETN.org) on the front; no MCU or standalone function beyond lighting when connected to neighboring minibadges.'
last_modified_date: '2026-09-10'
---

The UETN Sponsor Badge is a SAINTCON 2023 minibadge made for UETN (the Utah Education and Telehealth Network), which the entry's notes and the community minibadge wiki both describe as a longtime SAINTCON sponsor and partner organization. It was designed by the prolific SAINTCON minibadge maker Jup1t3r, who has produced dozens of minibadges across multiple SAINTCON years.

Electrically it is a simple board: two small SMD LEDs (labeled D1 and D2) and a single resistor (R1) wired across the standard minibadge corner headers, so the LEDs light up when the badge is chained to neighboring minibadges — there is no microcontroller, display, or standalone power source. The front carries a large stylized "e" logo referencing UETN.org in a purple and dark-purple color scheme; the back carries the UETN.org wordmark and exposes the LED/resistor traces.

The minibadge wiki lists it under the "Sponsor" category with "Intermediate" soldering difficulty and a "Rare" rarity rating, and notes it was not sold but given away: attendees were told to find a UETN employee on the show floor and ask for one. No quantity made, storefront, or open-source design files were found for this specific badge.
