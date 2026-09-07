---
title: PEOPLE BADGE
id: saintcon-2022-people-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Jup1t3r
summary: A SAINTCON 2022 minibadge with a fingerprint graphic, issued in different solder-mask colors for each involvement level (attendee, staff, volunteer, speaker).
functions: 'No interactive function beyond a single onboard LED (D1); it identifies the wearer''s role at the conference by color.'
look:
  colors: [black, green, yellow]
  shape: rectangle
  themes: [security, minibadge]
tech:
  mcu: none
  leds:
    count: 1
    type: null
    note: 'Silkscreen shows one LED (D1) and a resistor (R1); exact lighting behavior is not documented by the maker.'
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: 'Given out at SAINTCON 2022 based on involvement level: everyone received an ATTENDEE version, with separate STAFF, VOLUNTEER, and SPEAKER variants for those roles.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=PEOPLE%20BADGE&year=2022
  url: https://minibadge.wiki/?search=PEOPLE%20BADGE&year=2022
  kind: website
images:
  - file: assets/images/badges/saintcon-2022/people-badge/ebee0313d3.jpg
    source: "https://minibadge.wiki/?search=PEOPLE%20BADGE&year=2022"
    credit: "Jup1t3r"
    caption: "Front of the STAFF-color PEOPLE minibadge"
  - file: assets/images/badges/saintcon-2022/people-badge/e0d131051b.jpg
    source: "https://minibadge.wiki/?search=PEOPLE%20BADGE&year=2022"
    credit: "Jup1t3r"
    caption: "Back of the ATTENDEE-color PEOPLE minibadge"
contact: {}
notes:
- 'category: Official; rarity: Common; soldering difficulty: Beginner (per minibadge.wiki)'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=PEOPLE%20BADGE&year=2022
  title: PEOPLE BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2022''.'
- kind: url
  url: https://minibadge.wiki/2022.json
  title: 'minibadge.wiki 2022 data feed (PEOPLE BADGE entry)'
  accessed: '2026-09-07'
  note: 'Underlying JSON the site''s search page renders from; supplied description, category, rarity, soldering difficulty, and front/back image URLs. The visible search page itself is client-rendered and returns no listings to a plain fetch.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'All facts trace to the maker''s own minibadge.wiki submission (via its JSON data feed), so this is a primary source, but it is the only source found — no independent confirmation (Hackaday, forums, photos elsewhere) turned up. Quantity made and exact acquisition mechanics (e.g. whether staff/volunteers self-selected a color or were handed one) are not stated. LED behavior is inferred from the PCB silkscreen (a D1/R1 pair) and not documented in the text description, so left partly unconfirmed. No repository, Gerbers, or BOM were found, so make_your_own is empty; the maker mentions a QR-code-linked assembly video but no direct link was recovered.'
last_modified_date: '2026-09-07'
---

The PEOPLE BADGE is a SAINTCON 2022 minibadge by Jup1t3r, part of the "official" set handed out to attendees each year. It centers on a large fingerprint graphic silkscreened on the PCB, with "SAINTCON" and the wearer's role (ATTENDEE, STAFF, VOLUNTEER, or SPEAKER) printed along one edge. The badge was made in a matching set of solder-mask colors, one per role, so a glance at someone's badge signals their level of involvement at the conference — everyone got the ATTENDEE version, while staff, volunteers, and speakers received their own color.

Electrically it is simple: a single LED (D1) and a resistor (R1) are the only populated parts visible on the board, alongside a row of header pads along the top and bottom edges for connecting to a badge or chaining with other minibadges. The maker rated assembly "Beginner" difficulty but noted the badge "looks amazing, but is a little technical on how to put it together," and pointed builders to a QR-coded video for soldering instructions rather than written steps.

No hardware files, firmware, or fabrication files were found, and the only source located was the maker's own submission to the minibadge.wiki community database; no independent coverage, storefront listing, or additional photos turned up in searches for this task.
