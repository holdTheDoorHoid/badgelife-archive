---
title: SaO MANY SAOs
id: dc33-sao-many-saos-already-catalogued-as-dc33-sao-many-saos
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: Coruscant Ventures
  url: https://coruscantventures.com/defcon-badges
summary: A wearable ring-shaped board with 25 SAO header slots, letting a wearer mount an entire collection of SAOs at once; sold through Hacker Warehouse as well as the maker's own storefronts.
functions: Holds up to 25 SAOs at once; includes a companion "SmartAO" SAO module for LED control; powered by two included 18650 batteries, charged over USB or a barrel connector.
look:
  colors: []
  shape: circle
  themes:
  - sao
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: 2x 18650 (included)
  sao_version: v1.69bis
  sao_ports: 25
get_one:
  price: $140
  price_usd: 140
  quantity: ''
  availability: sold_out
  availability_note: 'As of 2026-09-07: Hacker Warehouse listing shows "out of stock."'
  distribution:
  - purchase
  where: Sold via Hacker Warehouse (hackerwarehouse.com) under "Badgelife" couture items, in addition to the maker's own Tindie and Coruscant Ventures storefronts.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  firmware_url: null
  eda_tool: null
links:
- label: hackerwarehouse.com/product/sao-many-saos-badge
  url: https://hackerwarehouse.com/product/sao-many-saos-badge/
  kind: website
- label: github.com/vortexcodes/DC33-SaO-MANY-SAOs
  url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://hackerwarehouse.com/product/sao-many-saos-badge/
  title: SAO Many SAOs Badge – Hacker Warehouse
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc33''. Confirms it as the Vortex Codes DC33 project, 25 SAO v1.69bis ports, dual-18650 power, $140, currently out of stock. Attempted to pull product photos but hackerwarehouse.com returned HTTP 403 to automated fetches.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    This is the same product already documented at dc34-sao-many-saos.md (the
    "SAO Many SAOs Badge" by Coruscant Ventures / maker handle Vortex Codes),
    which that entry's own research already identified as a DEF CON 33 (2025)
    item mis-filed under dc34. It also overlaps with dc33-sao-and-many-sao-badge
    and dc33-sao-for-above, both of which independently flagged themselves as
    duplicates of a "dc33-sao-many-saos" entry that does not actually exist as
    a file (existing_titles.txt still lists that id, but no _badges file uses
    it — the canonical copy now lives at dc34-sao-many-saos.md). Hacker
    Warehouse lists this same board at $140 (vs. $80 on Tindie / $100 on the
    maker's own site), which is left here as a separate, higher retail price
    point rather than reconciled, since it's a different storefront. No MCU,
    exact LED count, or quantity made is stated by Hacker Warehouse; left
    empty. Could not fetch product images: hackerwarehouse.com returns HTTP
    403 to both WebFetch and curl.
last_modified_date: '2026-09-07'
---

This is the Hacker Warehouse storefront listing for the "SAO Many SAOs Badge," a wearable ring-shaped board built around one idea: instead of a badge with one or two SAO headers, give it 25, so a wearer can mount an entire personal SAO collection at once. Hacker Warehouse credits it to the "Vortex Codes" DC33 project and lists it under their Badgelife couture category for $140, currently out of stock. Two included 18650 batteries, chargeable over USB or a barrel connector, power the ring, and a companion "SmartAO" module is needed to drive its LEDs.

The maker is Coruscant Ventures (the same team behind the GitHub repo `DC33-SaO-MANY-SAOs`), and this appears to be the identical product already researched in more depth at `dc34-sao-many-saos` — that entry found it was actually made for DEF CON 33 despite being filed under DC34, sold there for $80 on Tindie and $100 on the maker's own site. Hacker Warehouse's $140 price is a third distinct price point for the same board, likely reflecting a retail markup rather than a different edition. This entry is being kept as a record of the Hacker Warehouse listing rather than merged, per the archive's one-entry-per-task rule.
