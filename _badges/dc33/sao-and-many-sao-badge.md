---
title: SAO Many SAOs Badge
id: dc33-sao-and-many-sao-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Coruscant Ventures
  url: https://coruscantventures.com
  role: design/sale credited to vor_t3x1 (Discord) / u/MorningMother8622 (Reddit)
summary: A large host badge with 25 SAO ports that can power and display many add-on boards at once, sold alongside a companion "SmartAO" SAO that adds LED animation control.
functions: Hosts and powers up to 25 SAOs simultaneously (about 300 mA @ 3.3V total, 30 mA if running off USB/barrel power alone); white perimeter LEDs are driven by whichever SAO is plugged into the top-left slot, with full animated control only available when the SmartAO SAO is installed there.
look:
  colors:
  - black
  - white
  shape: rectangle
  themes:
  - village badge
tech:
  mcu: null
  leds:
    count: null
    type: white SMD (perimeter)
    note: One white LED sits at the edge of each SAO slot; full color/animation control requires the separate SmartAO SAO plugged into the top-left port.
  display: none
  connectivity: []
  battery: 2x 18650 (pre-installed), charge/run via USB or barrel connector
  sao_version: v2
  sao_ports: 25
get_one:
  price: $100
  price_usd: 100.0
  quantity: ''
  availability: available
  distribution:
  - purchase
  where: Sold directly by Coruscant Ventures via their storefront (coruscantventures.com); at DEF CON 33 arrange payment/shipping via Discord, Reddit or email since the site's PayPal checkout was reported non-functional.
  availability_note: Listed "IN STOCK" on the maker storefront as of 2026-09-06; PayPal checkout on the page is broken, maker asks buyers to contact them directly via Discord/Reddit/contact form.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  firmware_url: null
  eda_tool: null
  notes: GitHub repo has schematics (as SVG sheets), a BOM, and assembly photos; maker notes Gerbers "may be released after DEF CON."
links:
- label: coruscantventures.com/defcon-badges/p/sao-many-saos
  url: https://coruscantventures.com/defcon-badges/p/sao-many-saos
  kind: website
  archived: https://web.archive.org/web/20260506040947/https://coruscantventures.com/defcon-badges/p/sao-many-saos
- label: 'GitHub: DC33-SaO-MANY-SAOs'
  url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  kind: repo
- label: Coruscantventures.com
  url: https://Coruscantventures.com
  kind: website
- label: hackerwarehouse.com/product/sao-many-saos-badge
  url: https://hackerwarehouse.com/product/sao-many-saos-badge/
  kind: website
images:
- file: assets/images/badges/dc33/sao-and-many-sao-badge/ed1e705536.jpg
  source: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  credit: Coruscant Ventures
  caption: The SAO Many SAOs badge PCB, showing its 5x5 grid of 25 SAO header slots
- file: assets/images/badges/dc33/sao-and-many-sao-badge/43793767aa.jpg
  source: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  credit: Coruscant Ventures
  caption: The assembled badge with multiple SAOs plugged in
- file: assets/images/badges/dc33/sao-and-many-sao-badge/aa920f25c4.jpg
  source: https://coruscantventures.com/defcon-badges/p/sao-many-saos
  credit: Coruscant Ventures
  caption: SAO Many SAOs badge product photo
  archived: https://web.archive.org/web/20260506040947/https://coruscantventures.com/defcon-badges/p/sao-many-saos
contact:
  email: support@coruscantventures.com
  emails:
  - Ja@coruscantventures.com
notes:
- Holds and controls 25 SAOs, has already been released
- This entry duplicates dc33-sao-and-many-sao-badge, which was independently researched from the same maker/product and carries the full write-up plus saved images; see that entry for photos.
- SmartAO SAO required to make the LEDs around the edge light up.
- Sheet listed the title as "SAO for above"; retitled to match the maker's product name, "SAO Many SAOs Badge," per the linked storefront page.
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: sheet
  event: dc33
  row: 50
  updated: 7/28/2025
- kind: url
  url: https://coruscantventures.com/defcon-badges/p/sao-many-saos
  title: SaO MANY SAOs - Coruscant Ventures
  accessed: '2026-09-06'
  note: Product page confirming maker, price ($100), features, and that this is the host badge for the SmartAO add-on.
  archived: https://web.archive.org/web/20260506040947/https://coruscantventures.com/defcon-badges/p/sao-many-saos
- kind: url
  url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  title: 'GitHub: vortexcodes/DC33-SaO-MANY-SAOs'
  accessed: '2026-09-06'
  note: README and schematic/BOM/photos confirming power system (2x 18650, USB/barrel charging), 25-SAO capacity, perimeter LED behavior, and that gerbers were withheld until after the con.
- kind: sheet
  event: dc33
  row: 47
  updated: 8/13/2025 22:46:45
- kind: url
  url: https://coruscantventures.com
  title: Coruscant Ventures
  accessed: '2026-09-06'
  note: Homepage confirms the company and that it sells DEF CON badges; no product-level detail beyond the product page above.
- kind: sheet
  event: dc33
  row: 51
  updated: 7/28/2025
- kind: url
  url: https://hackerwarehouse.com/product/sao-many-saos-badge/
  title: SAO Many SAOs Badge – Hacker Warehouse
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc33''. Confirms it as the Vortex Codes DC33 project, 25 SAO v1.69bis ports, dual-18650 power, $140, currently out of stock. Attempted to pull product photos but hackerwarehouse.com returned HTTP 403 to automated fetches.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Sheet title "SAO and Many SAO Badge" corrected to the maker's own "SAO Many SAOs Badge" / "SaO MANY SAOs" naming. MCU, exact LED count, quantity made, and current availability are not stated by the maker anywhere found; left empty rather than guessed. The product page notes checkout (PayPal) was broken and buyers had to arrange payment directly. This appears to duplicate an existing entry for the same product, dc33-sao-many-saos, which was filled in from the community sheet under a different title/row. Merged with duplicate entry 'SaO MANY SAOs' (dc33-sao-many-saos). Merged with duplicate entry 'SAO Many SAOs Badge' (dc33-sao-for-above).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc33/sao-many-saos/
- /badges/dc33/sao-for-above/
---

The SAO Many SAOs badge is a large host board from Coruscant Ventures built around one gimmick: it has 25 separate SAO header slots arranged in a 5x5 grid, so a badge collector can plug in nearly their entire haul of add-on boards at once. It runs off two pre-installed 18650 cells that can be charged over USB or a barrel jack, with onboard red/green LEDs to show charging status and built-in surge protection so it can survive being plugged into whatever DEF CON attendees plug things into.

A row of white LEDs runs around the board's perimeter, one near each SAO slot, but they are only driven by whatever is plugged into the top-left slot. Out of the box that just lights them; to get actual animations and color control, Coruscant Ventures sold a companion "SmartAO" SAO separately for that slot. The badge shipped assembled and tested, sold for $100 through the maker's Squarespace storefront, though at least some buyers reported the site's PayPal checkout was broken during the con and had to arrange payment directly via Discord, Reddit, or email instead.

Schematics, a bill of materials, and build photos are published on GitHub, but the maker noted gerbers "may be released after DEF CON," and no firmware or MCU details were included in what was published as of this check.

## Notes merged from the duplicate entry "SaO MANY SAOs"

The SaO MANY SAOs badge is a large host board from Coruscant Ventures built around one gimmick: it has 25 separate SAO header slots arranged in a grid, so a badge collector can plug in nearly their entire haul of add-on boards at once. It runs off two pre-installed 18650 cells that can be charged over USB or a barrel jack, with onboard LEDs to show charging status and built-in surge protection.

A row of white LEDs runs around the board's perimeter, one near each SAO slot, but they are only driven by whatever is plugged into the top-left slot. Out of the box that just lights them; to get actual animations and color control, Coruscant Ventures sold a companion "SmartAO" SAO separately for that slot. The badge shipped assembled and tested, sold for $100 through the maker's Squarespace storefront, though at least some buyers reported the site's PayPal checkout was broken during the con and had to arrange payment directly via Discord, Reddit, or email instead.

Schematics, a bill of materials, and build photos are published on GitHub, but the maker noted gerbers "may be released after DEF CON," and no firmware or MCU details were published as of this check. This entry duplicates `dc33-sao-and-many-sao-badge`, which covers the same product and already has saved photos.

## Notes merged from the duplicate entry "SAO Many SAOs Badge"

Coruscant Ventures' "SAO Many SAOs Badge" is a DEF CON 33 badge built to be a carrier for other people's SAOs rather than a single fixed add-on: it exposes 25 SAO slots, each fused and surge-protected, powered by a pair of 18650 cells charged over USB or a barrel jack. White LEDs run around the badge's edge, but they only animate when the top-left SAO slot holds the maker's companion SmartAO SAO (sold separately), which drives the display.

The community badge sheet listed this row under the title "SAO for above," but that name does not appear on the maker's storefront, GitHub repo, or anywhere else found; the sheet's own link points straight to the "SAO Many SAOs Badge" product page, so the entry has been retitled to match. As of this check the badge is listed in stock for $100 (the sheet's $35 price could not be confirmed and appears to be stale or a transcription error), though the storefront's PayPal checkout is broken and the maker asks buyers to arrange payment directly via Discord or Reddit. Design files — schematics as SVG sheets and a bill of materials — are published on GitHub, with the maker noting Gerbers might follow after the con.

This is very likely the same badge already catalogued under `dc33-sao-many-saos` (and possibly overlapping with `dc33-sao-and-many-sao-badge`); the three sheet rows appear to describe the same Coruscant Ventures product.

## Notes merged from the duplicate entry "SaO MANY SAOs"

This is the Hacker Warehouse storefront listing for the "SAO Many SAOs Badge," a wearable ring-shaped board built around one idea: instead of a badge with one or two SAO headers, give it 25, so a wearer can mount an entire personal SAO collection at once. Hacker Warehouse credits it to the "Vortex Codes" DC33 project and lists it under their Badgelife couture category for $140, currently out of stock. Two included 18650 batteries, chargeable over USB or a barrel connector, power the ring, and a companion "SmartAO" module is needed to drive its LEDs.

The maker is Coruscant Ventures (the same team behind the GitHub repo `DC33-SaO-MANY-SAOs`), and this appears to be the identical product already researched in more depth at `dc34-sao-many-saos` — that entry found it was actually made for DEF CON 33 despite being filed under DC34, sold there for $80 on Tindie and $100 on the maker's own site. Hacker Warehouse's $140 price is a third distinct price point for the same board, likely reflecting a retail markup rather than a different edition. This entry is being kept as a record of the Hacker Warehouse listing rather than merged, per the archive's one-entry-per-task rule.
