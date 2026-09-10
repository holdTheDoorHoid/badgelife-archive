---
title: VENT EVENT BADGE
id: saintcon-2022-vent-event-badge-2022
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Jup1t3r
summary: A SAINTCON 2022 event minibadge given to attendees who attended and participated in "VENT," a session where security professionals speak and tell stories off the record.
functions: 'No electronic gameplay; a simple LED minibadge with a BLINK/SOLID jumper option, marking participation in the VENT event.'
look:
  colors: []
  shape: null
  themes:
  - security
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 'D1 is a color-changing LED, D2 is a solid-color LED, each hand-soldered with the single-pad method; two resistors (R1 purple, R2 green).'
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to attendees who attended and participated in the VENT event at SAINTCON 2022.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  kind: website
- label: minibadge.wiki/?search=VENT%20EVENT%20BADGE&year=2022
  url: https://minibadge.wiki/?search=VENT%20EVENT%20BADGE&year=2022
  kind: website
images:
  - file: assets/images/badges/saintcon-2022/vent-event-badge-2022/ee79e12fb0.jpg
    source: "https://minibadge.wiki/?search=VENT%20EVENT%20BADGE&year=2022"
    credit: "Jup1t3r"
    caption: "VENT EVENT minibadge, front"
  - file: assets/images/badges/saintcon-2022/vent-event-badge-2022/1204bc81df.jpg
    source: "https://minibadge.wiki/?search=VENT%20EVENT%20BADGE&year=2022"
    credit: "Jup1t3r"
    caption: "VENT EVENT minibadge, back"
contact: {}
notes:
- 'Sweep title read "VENT EVENT BADGE (2022)" with the year appended; the maker''s own PDF and minibadge.wiki both title it simply "VENT EVENT BADGE" (title corrected here).'
- 'category: Official; rarity: Rare; soldering difficulty: Beginner (per minibadge.wiki).'
- 'The official 2022 SAINTCON minibadge assembly guide notes a design flaw: the resistor needs to be connected to GND at the top with a wire to work properly, which the guide says was caught too late to fix before printing.'
status: listed
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: SAINTCON MiniBadge Assembly Guide 2022 (VENT EVENT BADGE, p.32)
  accessed: '2026-09-10'
  note: 'Official SAINTCON 2022 minibadge assembly guide PDF; confirms maker (Jup1t3r), description, design-flaw note, difficulty (Beginner), rarity (Rare), LED/resistor layout (D1 color-changing, D2 solid; R1 purple, R2 green), BLINK/SOLID jumper, 4x 2-position headers, and how-to-acquire text.'
- kind: url
  url: https://minibadge.wiki/?search=VENT%20EVENT%20BADGE&year=2022
  title: VENT EVENT BADGE
  accessed: '2026-09-10'
  note: 'Community minibadge database entry; the search page is a client-rendered SPA with no content to a plain fetch, so the underlying JSON (below) was used instead.'
- kind: url
  url: https://minibadge.wiki/2022.json
  title: minibadge.wiki 2022 data (VENT EVENT BADGE record)
  accessed: '2026-09-10'
  note: 'Underlying JSON record: description, soldering instructions/difficulty, category (Official), rarity (Rare), how-to-acquire text, and front/back image URLs, matching the official PDF verbatim.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Confirmed against two independent sources that agree verbatim: the official SAINTCON 2022 minibadge assembly guide PDF and the minibadge.wiki 2022 database record. LED count/type inferred from the assembly instructions (D1, D2, R1, R2 named explicitly) rather than a spec sheet, so recorded with note text rather than as a bare spec. Quantity made is not stated by either source (minibadge.wiki records 0, most likely "not tracked" rather than zero produced), so left blank. No maker page, repo, or storefront exists beyond these two archival sources.'
last_modified_date: '2026-09-10'
---

The VENT EVENT BADGE is a SAINTCON 2022 minibadge designed by Jup1t3r for "VENT," a new event that year giving security professionals a chance to speak and share stories off the record. It was earned, not sold: attendees had to attend and participate in the VENT event to receive one.

It's a beginner-level hand-solder kit: a color-changing LED (D1) and a solid-color LED (D2), two through-hole resistors (a purple R1 and a green R2), a jumper that lets the builder choose between a blinking or solid-on mode, and four 2-position headers for the standard SAINTCON minibadge connector. The official assembly guide flags a design flaw discovered too late to fix before printing — the resistor needs an added wire to GND at the top to work correctly — and leaves it to builders to "hack it" properly. Minibadge.wiki, the community-run SAINTCON minibadge database, lists it as "Official" category with a "Rare" rarity.

No maker page, repository, or storefront listing exists beyond the official SAINTCON assembly guide and the minibadge.wiki archive, so exact quantity made and any design files remain unconfirmed.
