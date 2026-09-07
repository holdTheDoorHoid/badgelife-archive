---
title: SaO MANY SAOs
id: dc34-sao-many-saos
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Coruscant Ventures
  url: https://coruscantventures.com/defcon-badges
summary: A wearable ring-shaped badge with 25 SAO header slots, letting a wearer mount an entire collection of SAOs around their head at once.
functions: Holds up to 25 SAOs at once (300 mA @ 3.3V shared across all slots); edge-mounted white LEDs, controlled by the top-left SAO slot, light up only when a "SmartAO" companion SAO is installed there; charging status LEDs (red = charging, green = full).
look:
  colors: []
  shape: circle
  themes:
  - sao
  - hardware tool
tech:
  mcu: null
  leds:
    count: null
    type: discrete
    note: White edge-mounted LEDs around the ring, driven from the top-left SAO slot; requires the maker's separate "SmartAO" SAO to actually light up.
  display: null
  connectivity: []
  battery: 2x 18650 (pre-installed), charged via USB or barrel connector
  sao_version: v1.69bis
  sao_ports: 25
get_one:
  price: 80 usd
  price_usd: 80
  quantity: ''
  availability: unknown
  availability_note: 'As of 2026-09-06: Tindie listing shows the maker "taking a break" with the shop paused for orders; Coruscant Ventures'' own site lists it at $100 with PayPal checkout described as non-functional, directing buyers to contact the maker directly.'
  distribution:
  - purchase
  where: Sold directly by Coruscant Ventures via Tindie (https://www.tindie.com/products/coruscant_ventures/sao-many-saos-badge/) and the maker's own store at coruscantventures.com/defcon-badges.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  firmware_url: null
  eda_tool: null
  gerbers_url: null
  bom_url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  license: null
  fab_url: null
  notes: The GitHub repo (dated May 2025) includes a bill of materials and four schematic sheets, but the maker's README states gerbers "may be released after def con" — full board files were not confirmed public as of this check.
links:
- label: github.com/vortexcodes
  url: https://github.com/vortexcodes
  kind: repo
- label: DC33-SaO-MANY-SAOs (GitHub repo)
  url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  kind: repo
  archived: false
- label: SAO Many SAOs Badge (Tindie)
  url: https://www.tindie.com/products/coruscant_ventures/sao-many-saos-badge/
  kind: store
  archived: false
- label: SAO Many SAOs (Coruscant Ventures store)
  url: https://coruscantventures.com/defcon-badges/p/sao-many-saos
  kind: store
  archived: false
images:
- file: assets/images/badges/dc34/sao-many-saos/e67715c0b9.jpg
  source: https://www.tindie.com/products/coruscant_ventures/sao-many-saos-badge/
  credit: Coruscant Ventures
  caption: The SAO Many SAOs badge, a wearable ring board with 25 SAO slots
contact:
  discord: vor_t3x1
  emails:
  - JA@vortex1.dev
  raw:
  - u/MorningMother8622 on redit
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 36
  updated: 7/6/2026 21:37:08
  listing: Update to Existing
- kind: url
  url: https://www.tindie.com/products/coruscant_ventures/sao-many-saos-badge/
  title: SAO Many SAOs Badge from coruscant ventures on Tindie
  accessed: '2026-09-06'
  note: Confirmed price ($80), 25-SAO slot count, dual 18650 battery, edge LEDs needing a SmartAO, and current "taking a break" unavailable status.
- kind: url
  url: https://coruscantventures.com/defcon-badges/p/sao-many-saos
  title: SAO Many SAOs Badge - DEFCON 33 — Coruscant Ventures
  accessed: '2026-09-06'
  note: Maker's own product page; lists price as $100 there and notes checkout is broken; identifies the badge as a DEFCON 33 item and names the maker as a 14-year-old self-taught PCB designer.
- kind: url
  url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  title: DC33-SaO-MANY-SAOs (GitHub)
  accessed: '2026-09-06'
  note: Repo (dated May 2025) with BOM and schematic sheets; README notes gerbers may be released after DEF CON; confirms 300mA/3.3V SAO power budget and battery/LED design.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Important discrepancy: every source found (the maker''s own GitHub repo name "DC33-SaO-MANY-SAOs", the Coruscant Ventures product page titled "SAO Many SAOs Badge - DEFCON 33", and repo dates from May 2025) identifies this as a DEF CON 33 (2025) badge, not DEF CON 34. This entry was imported into the dc34 sheet/section, but is left filed under dc34 (matching its existing id and file location) since correcting the event would require moving the entry; a human maintainer should confirm and possibly relocate it to dc33. Price is inconsistent between sources: the community sheet and Tindie say $80, the maker''s own coruscantventures.com store currently shows $100. Exact LED count, MCU/chip (if any beyond LED driving), and PCB color/shape beyond "ring" were not stated by any source and are left empty. Quantity made was not stated anywhere found.'
last_modified_date: '2026-09-06'
related:
- dc33-sao-many-saos-already-catalogued-as-dc33-sao-many-saos
---

The SAO Many SAOs badge is a wearable ring-shaped board built around one idea: instead of a badge with one or two SAO headers, give it 25, so a wearer can mount an entire personal SAO collection at once. It was made by Coruscant Ventures, whose own product page credits the design to a 14-year-old maker who learned PCB design from YouTube and Discord. Two pre-installed 18650 batteries, chargeable over USB or a barrel connector, power the ring; onboard circuitry includes surge protection and red/green charge-status LEDs. White LEDs run around the outer edge of the board, but they only light up when the maker's companion "SmartAO" SAO is plugged into the top-left slot, which drives them.

The badge was sold directly by the maker for around $80 (the Coruscant Ventures storefront currently lists it at $100, with a note that PayPal checkout is broken and buyers should reach out directly). As of this check the Tindie listing shows the shop "taking a break," so it is not actively for sale. A GitHub repository (dc33-sao-many-saos) dated May 2025 provides a bill of materials and schematic sheets, but the maker's own README says gerbers "may be released after def con," so full open-hardware files were not confirmed public.

Every maker-controlled source — the GitHub repo name, the product page title, and the repo's May 2025 file dates — identifies this specifically as a DEF CON 33 (2025) badge, even though this entry is filed under DC34. That mismatch is noted above for a maintainer to review; the entry itself was left in place rather than moved.
